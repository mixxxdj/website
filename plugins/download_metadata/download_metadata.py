import datetime
import json
import logging
import os
import os.path
import urllib.request
from pelican import signals


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)


def format_size(num, suffix="B"):
    """Convert a file size in bytes into a human-readable format."""
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, "Yi", suffix)


def url_add_query_params(original_url, query_params):
    """Returns the URL with the given query parameters added."""
    url = urllib.parse.urlparse(original_url)
    query = urllib.parse.parse_qs(url.query)
    query.update(query_params)
    query = urllib.parse.urlencode(query)
    return urllib.parse.urlunparse(
        (url.scheme, url.netloc, url.path, url.params, query, url.fragment)
    )


def page_generator_context(page_generator, metadata):
    """
    Iterate through page objects and augment the download page's package data
    with information from the download manifest file (if specified).
    """
    logger = logging.getLogger(__name__)

    if metadata.get("slug") != "download":
        return

    # Get the configured datetime format
    try:
        date_format = tuple(
            page_generator.context["generated_content"].values()
        )[0].date_format
    except IndexError:
        date_format = "%Y-%m-%d"
    datetime_format = f"{date_format} %H:%M"

    for version_name, version_data in metadata.get("versions", {}).items():
        if "name" not in version_data:
            version_data["name"] = version_data["version"]

        # Check if a manifest URL is specified for this version and download it
        manifest_url = version_data.get("download_manifest")
        if not manifest_url:
            continue

        # FIXME: This is a hack to get around Cloudflare's caching. By adding a
        # timestamp to the query parameters, we ensure that this URL is
        # "fresh" and Cloudflare doesn't respond with cached (stale) data.
        manifest_url = url_add_query_params(
            manifest_url, {"timestamp": datetime.datetime.now().strftime("%s")}
        )

        req = urllib.request.Request(
            manifest_url,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
            },
        )
        try:
            resp = urllib.request.urlopen(req, timeout=10)
            manifest_data = resp.read().decode()
        except IOError:
            # If the download manifest file failed to download, print a warning
            # and continue. This allows to build the website locally without
            # and internet connection (it will use the hardcoded values in
            # `download.md` in that case). On Netlify, we build the website
            # with `--fatal warnings` so that the deploy will fail and the
            # website is not updated if the download manifest fails to
            # download.
            # In any case, the metadata and URL will never be inconsistent
            # unless the data in `download.md` or `manifest.json` are wrong.
            logger.warning(
                "Failed to retrieve manifest URL: %s",
                manifest_url,
                exc_info=True,
            )
            continue

        manifest = json.loads(manifest_data)

        # Override the package data with information from the manifest file
        for download in version_data.get("downloads", []):
            for package in download.get("packages", []):
                slug = f"{download['slug']}-{package['slug']}"
                package_metadata = manifest.get(slug)
                if not package_metadata:
                    continue

                logger.debug("Updating download: %s", slug)

                for key, value in package_metadata.items():
                    if key.endswith("_date"):
                        package[key] = datetime.datetime.fromisoformat(value)
                        package[f"locale_{key}"] = package[key].strftime(
                            datetime_format
                        )
                    elif key.endswith("_size"):
                        package[key] = format_size(int(package_metadata[key]))
                    else:
                        package[key] = package_metadata[key]

    # Build update metadata for auto-updater
    siteurl = page_generator.settings.get("SITEURL")
    if not siteurl:
        logger.warning("Cannot generate download.json without SITEURL")
        return

    download_data = {}
    for version_name, version_data in metadata.get("versions", {}).items():
        release_announcement_url = None
        if version_data.get("release_announcement"):
            release_announcement_url = urllib.parse.urljoin(
                siteurl, version_data["release_announcement"]
            )
        download_data[version_name] = {
            "version": version_data["version"],
            "name": version_data.get("name", version_data["version"]),
            "release_announcement_url": release_announcement_url,
            "download_url": urllib.parse.urljoin(
                siteurl, f"download#{version_name}"
            ),
        }

    os.makedirs(page_generator.output_path, exist_ok=True)
    output_path = os.path.join(page_generator.output_path, "download.json")
    with open(output_path, mode="w") as fp:
        json.dump(download_data, fp, cls=JSONEncoder)


def register():
    """ Subscribe to Pelican's signals. """
    signals.page_generator_context.connect(page_generator_context)
