import json
import logging
import datetime
import urllib.request
from pelican import signals

# from pydiscourse import DiscourseClient


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

    controllers = metadata.get("controllers", {})

    # check if the page has controllers in the metadata
    if controllers:
        # remove dummy entry
        controllers.clear()

        for x in range(10):
            streetno = {}
            streetno["name"] = "Fancy Controller"
            streetno["heat"] = x
            streetno[
                "forum_link"
            ] = "https://mixxx.discourse.group/t/denon-sc2000/11122"
            controllers[str(x)] = streetno

        # client = DiscourseClient(
        #    'https://mixxx.discourse.group/',
        #    api_username='username',
        #    api_key='areallylongstringfromdiscourse')


def register():
    """ Subscribe to Pelican's signals. """
    signals.page_generator_context.connect(page_generator_context)
