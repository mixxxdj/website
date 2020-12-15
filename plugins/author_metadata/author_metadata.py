from pelican import signals


def update_author(settings, author):
    """ Updates the Author metadata objects with extra information. """
    author_metadata = settings.get("AUTHOR_METADATA", {})
    author_dict = author_metadata.get(author.name, {})
    author.description = author_dict.get("description")
    author.github = author_dict.get("github")
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
