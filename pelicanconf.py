#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Mixxx DJ Team"
SITENAME = "Mixxx"
SITEURL = ""

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "en"

PATH = "content"

ARTICLE_PATHS = [
    "news",
]

STATIC_PATHS = [
    "images",
    "_redirects",
]

THEME = "theme"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

ARTICLE_URL = "news/{date:%Y-%m-%d}-{slug}"
ARTICLE_SAVE_AS = "news/{date:%Y-%m-%d}-{slug}/index.html"
PAGINATION_PATTERNS = (
    (1, "{url}", "{save_as}"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)

INDEX_URL = "news"
INDEX_SAVE_AS = "news/index.html"
ARCHIVES_URL = "news/archives"
ARCHIVES_SAVE_AS = "news/archives/index.html"
AUTHORS_URL = "news/authors"
AUTHORS_SAVE_AS = "news/authors/index.html"
CATEGORIES_URL = "news/category"
CATEGORIES_SAVE_AS = "news/category/index.html"
TAGS_URL = "news/tag"
TAGS_SAVE_AS = "news/tag/index.html"

YEAR_ARCHIVE_URL = "news/archives/{date:%Y}"
YEAR_ARCHIVE_SAVE_AS = "news/archives/{date:%Y}/index.html"

MONTH_ARCHIVE_URL = "news/archives/{date:%Y}/{date:%m}"
MONTH_ARCHIVE_SAVE_AS = "news/archives/{date:%Y}/{date:%m}/index.html"

AUTHOR_URL = "team/{slug}"
AUTHOR_SAVE_AS = "team/{slug}/index.html"

CATEGORY_URL = "news/category/{slug}"
CATEGORY_SAVE_AS = "news/category/{slug}/index.html"

TAG_URL = "news/tag/{slug}"
TAG_SAVE_AS = "news/tag/{slug}/index.html"

TEMPLATE_PAGES = {
    "pages/maintenance.html": "maintenance.html",
    "pages/error.html": "error.html",
}


class MenuItem:
    def __init__(self, url, title, context, css="", children=()):
        self.url = url
        self.title = title
        self.context = context
        self.css = css
        self.children = children


NAV_MENU = (
    MenuItem("/news", "News", "Navigation bar link to Mixxx News page."),
    MenuItem(
        "/discover",
        "Discover",
        "Navigation bar link to Mixxx discover page.",
        children=(
            MenuItem(
                "/features",
                "Features",
                "Navigation bar link to Mixxx features page.",
            ),
            MenuItem(
                "/screenshots",
                "Screenshots",
                "Navigation bar link to Mixxx Screenshots page.",
            ),
            MenuItem(
                "/press",
                "Press",
                "Navigation bar link to Mixxx Press page",
            ),
            MenuItem(
                "/contact",
                "Contact & Team",
                "Navigation bar link to Mixxx contact page.",
            ),
        ),
    ),
    MenuItem(
        "/support",
        "Support & Community",
        "Navigation bar link to Mixxx support page.",
        children=(
            MenuItem(
                "/manual/latest",
                "Manual",
                "Navigation bar link to Mixxx Manual.",
            ),
            MenuItem(
                "https://mixxx.discourse.group/",
                "Forums",
                "Navigation bar link to Mixxx Forums.",
            ),
            MenuItem(
                "https://github.com/mixxxdj/mixxx/wiki",
                "Wiki",
                "Navigation bar link to Mixxx Wiki.",
            ),
            MenuItem(
                "/get-involved",
                "Get Involved",
                "Navigation bar link to Mixxx Get Involved page.",
            ),
        ),
    ),
)

JINJA_GLOBALS = {
    "gettext": lambda x: x,
    "NAV_MENU": NAV_MENU,
}
JINJA_ENVIRONMENT = {
    "trim_blocks": True,
    "lstrip_blocks": True,
    "extensions": [
        "jinja2.ext.do",
        "jinja2.ext.i18n",
    ],
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
