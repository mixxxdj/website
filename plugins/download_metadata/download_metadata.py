import json
import logging
import datetime
import urllib.request
from pelican import signals


def format_size(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, "Yi", suffix)


def page_generator_context(page_generator, metadata):
    """
    Iterate through author objects in metadata and add some additional
    properties.
    """
    logger = logging.getLogger(__name__)

    for version_name, version_data in metadata.get("versions", {}).items():
        manifest_url = version_data.get("download_manifest")
        if not manifest_url:
            continue

        try:
            resp = urllib.request.urlopen(manifest_url, timeout=10)
            manifest_data = resp.read().decode()
        except IOError:
            logger.warning("Failed to retrieve manifest URL: %s", manifest_url)
            continue

        print(manifest_data)

        manifest = json.loads(manifest_data)
        for download in version_data.get("downloads", []):
            for package in download.get("packages", []):
                slug = f"{download['slug']}-{package['slug']}"
                metadata = manifest.get(slug)
                if not metadata:
                    continue

                logger.debug("Updating download: %s", slug)
                package["url"] = metadata["file_url"]
                package["size"] = format_size(int(metadata["file_size"]))
                package["date"] = datetime.datetime.fromisoformat(
                    metadata["file_date"]
                )
                package["commit_id"] = metadata["commit_id"]
                package["commit_url"] = metadata["commit_url"]
                package["build_log_url"] = metadata["build_log_url"]


def register():
    """ Subscribe to Pelican's signals. """
    signals.page_generator_context.connect(page_generator_context)
