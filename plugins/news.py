import os
import posixpath
import datetime
import logging

from django.template import Context
from django.template.loader import get_template
from django.template.loader_tags import BlockNode, ExtendsNode

ORDER = 999
POSTS_PATH = "news/"
POSTS = []
DEFAULTS = {
    "author": "Mixxx Team",
}


def getNode(template, context, name="subject"):
    """
    Get django block contents from a template.
    http://stackoverflow.com/questions/2687173/
    django-how-can-i-get-a-block-from-a-template
    """
    for node in template:
        if isinstance(node, BlockNode) and node.name == name:
            return node.render(context)
        elif isinstance(node, ExtendsNode):
            return getNode(node.nodelist, context, name)
    raise Exception("Node '%s' could not be found in template." % name)


def preBuild(site):

    global POSTS

    context = Context(site.context())

    # Build all the posts
    for page in site.pages():
        if not page.path.startswith(POSTS_PATH):
            continue

        # Skip non html posts for obious reasons
        if os.path.splitext(page.path)[1] != ".html":
            continue

        # Find a specific defined variable in the page context,
        # and throw a warning if we're missing it.
        def find(name):
            value = page.context().get(name, DEFAULTS.get(name, ""))
            if not value:
                logging.warning(
                    "Missing info '%s' for post %s" % (name, page.path)
                )
            return value

        # Build a context for each post
        postContext = {}
        postContext["title"] = find("title")
        postContext["author"] = find("author")
        postContext["date"] = find("date")
        postContext["path"] = posixpath.join("/", page.path)
        context.update({"__CACTUS_CURRENT_PAGE__": page})
        postContext["post"] = getNode(
            get_template(page.path), context, name="post"
        )

        # Parse the date into a date object
        try:
            postContext["date"] = datetime.datetime.strptime(
                postContext["date"], "%Y-%m-%d %H:%M:%S"
            )
        except Exception as e:
            logging.warning(
                "Date format not correct for page %s, "
                "should be 'YYYY-MM-DD HH:MM:SS'\n%s" % (page.path, e)
            )
            continue

        POSTS.append(postContext)

    # Sort the posts by date
    POSTS = list(sorted(POSTS, key=lambda x: x["date"], reverse=True))

    # Add reference to previous/nexts post
    for i, post in enumerate(POSTS):
        if i == 0:
            continue
        next_post = POSTS[i - 1]
        next_post["prevPost"] = post
        post["nextPost"] = next_post


def preBuildPage(site, page, context, data):
    """
    Add the list of posts to every page context so we can
    access them from wherever on the site.
    """
    context["posts"] = POSTS

    for post in POSTS:
        if post["path"] == posixpath.join("/", page.path):
            context.update(post)
            break

    return context, data
