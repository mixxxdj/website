from pelican import signals


def update_author(settings, author):
    """ Updates the Author metadata objects with extra information. """
    author_metadata = settings.get("AUTHOR_METADATA", {})
    author_dict = author_metadata.get(author.name, {})

    author.description = author_dict.get("description")
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


def article_generator_context(article_generator, metadata):
    """
    Iterate through author objects in metadata and add some additional
    properties.
    """
    for author in metadata.get("authors", []):
        update_author(article_generator.settings, author)


def register():
    """ Subscribe to Pelican's signals. """
    signals.article_generator_context.connect(article_generator_context)
