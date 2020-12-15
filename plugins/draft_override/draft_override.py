import datetime
import os

from pelican import signals


def article_generator_context(article_generator, metadata):
    if metadata.get("status") != "draft":
        return

    # This environment variable is set when building a deploy preview on
    # Netlify. We use it to update the draft status of articles to "published",
    # so we get a nice preview. That way we don't have to navigate to the
    # drafts/ directory manually and we can also check that the summary is
    # displayed correctly in the article listing.
    if os.getenv("CONTEXT") != "deploy-preview":
        return

    if "date" not in metadata:
        metadata["date"] = datetime.datetime.now()
    metadata["status"] = "published"


def register():
    signals.article_generator_context.connect(article_generator_context)
