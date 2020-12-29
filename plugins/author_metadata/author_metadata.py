import logging
import os
import urllib.error
import urllib.request

from pelican import signals
from pelican.utils import mkdir_p, get_relative_path, path_to_url

logger = logging.getLogger(__name__)


def download_avatar(username):
    url = f"https://avatars.githubusercontent.com/{username}?size=60"
    with urllib.request.urlopen(url) as response:
        data = response.read()
    return data


def update_author(article_generator, author):
    """ Updates the Author metadata objects with extra information. """
    settings = article_generator.settings

    author_metadata = settings.get("AUTHOR_METADATA", {})
    author_dict = author_metadata.get(author.name, {})

    author.tagline = author_dict.get("tagline")
    author.discourse = author_dict.get("discourse")
    author.discourse_url = (
        "https://mixxx.discourse.group/u/{}/".format(author.discourse)
        if author.discourse
        else ""
    )
    author.facebook = author_dict.get("facebook")
    author.facebook_url = (
        "https://www.facebook.com/{}/".format(author.facebook)
        if author.facebook
        else ""
    )
    author.github = author_dict.get("github")
    author.github_url = (
        "https://github.com/{}".format(author.github) if author.github else ""
    )
    author.twitter = author_dict.get("twitter")
    author.twitter_url = (
        "https://twitter.com/{}/".format(author.twitter)
        if author.twitter
        else ""
    )
    author.email = author_dict.get("email")

    author.avatar_url = None
    if not author.github or "images" not in settings["STATIC_PATHS"]:
        return
    path = os.path.join(article_generator.path, "images", "avatars")
    avatar_path = os.path.join(path, f"{author.github}.png")
    if not os.path.exists(avatar_path):
        logger.warning(
            "Missing avatar for author '%s', expected %s",
            author.name,
            avatar_path,
        )
        logger.debug(
            "Downloading missing avatar for GitHub user %s...",
            author.github,
        )
        try:
            data = download_avatar(author.github)
        except urllib.error.URLError:
            logger.warning("Download of avatar failed, skipping...")
            return
        mkdir_p(path)
        with open(avatar_path, "w+b") as fp:
            fp.write(data)
        logger.warning("Downloaded missing avatar to: %s", avatar_path)
    author.avatar_url = path_to_url(
        os.path.relpath(avatar_path, article_generator.path)
    )


def article_generator_context(article_generator, metadata):
    """
    Iterate through author objects in metadata and add some additional
    properties.
    """
    for author in metadata.get("authors", []):
        update_author(article_generator, author)

    if "author" in metadata:
        update_author(article_generator, metadata["author"])


def register():
    """ Subscribe to Pelican's signals. """
    signals.article_generator_context.connect(article_generator_context)
