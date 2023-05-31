#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import jinja2
import markdown

AUTHOR = "Mixxx DJ Team"
SITENAME = "Mixxx"
SITEURL = ""

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "en"

PATH = "content"
FEED_ATOM = "feed.xml"

ARTICLE_PATHS = [
    "news",
]

STATIC_PATHS = [
    "images",
    "_redirects",
]

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "full_yaml_metadata": {
            "allow_missing_delimiters": True,
        },
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown_video": {},
    },
    "output_format": "html5",
}

THEME = "theme"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

ARTICLE_URL = "news/{date:%Y-%m-%d}-{slug}"
ARTICLE_SAVE_AS = "news/{date:%Y-%m-%d}-{slug}/index.html"
PAGINATION_PATTERNS = (
    (1, "{url}", "{save_as}"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)
FILENAME_METADATA = r"^((?P<date>\d{4}-\d{2}-\d{2})|XXXX-XX-XX)-(?P<slug>.+)$"
DEFAULT_METADATA = {
    "comments": "yes",
}

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

AUTHOR_URL = "news/author/{slug}"
AUTHOR_SAVE_AS = "news/author/{slug}/index.html"

CATEGORY_URL = "news/category/{slug}"
CATEGORY_SAVE_AS = "news/category/{slug}/index.html"

TAG_URL = "news/tag/{slug}"
TAG_SAVE_AS = "news/tag/{slug}/index.html"

TEMPLATE_PAGES = {
    "pages/error.html": "error.html",
}

PLUGIN_PATHS = [
    "plugins",
]

PLUGINS = [
    "author_metadata",
    "download_metadata",
    "draft_override",
    "md_yaml",
]


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
                "https://github.com/mixxxdj/mixxx/issues/",
                "Bug Tracker",
                "Navigation bar link to Mixxx Bug Tracker.",
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


AUTHOR_METADATA = {
    "Mixxx Team": {
        "github": "mixxxdj",
        "mastodon": "@mixxx@floss.social",
        "twitter": "mixxxdj",
        "facebook": "mixxxdj",
        "email": "core-team@mixxx.org",
        "tagline": "Mixxx DJ Software Development Team",
    },
    "Be.": {
        "github": "Be-ing",
        "discourse": "Be0",
        "email": "be@mixxx.org",
        "tagline": "Mixxx Core Developer",
    },
    "Albert Santoni": {
        "github": "asantoni",
        "discourse": "albert",
        "tagline": "Mixxx Core Developer",
    },
    "Jan Holthuis": {
        "github": "Holzhaus",
        "discourse": "hlzhs",
        "email": "jholthuis@mixxx.org",
        "tagline": "Mixxx Core Developer",
    },
    "RJ Ryan": {
        "github": "rryan",
        "discourse": "rryan",
        "email": "rryan@mixxx.org",
        "tagline": "Mixxx Core Developer",
    },
    "Pegasus": {
        "github": "Pegasus-RPG",
        "discourse": "Pegasus",
        "tagline": "Mixxx Core Developer",
    },
    "Owen Williams": {
        "github": "ywwg",
        "discourse": "owilliams",
        "tagline": "Mixxx Core Developer",
    },
    "Uwe Klotz": {
        "github": "uklotzde",
        "discourse": "tapir",
        "tagline": "Mixxx Core Developer",
    },
    "April M. Crehan": {
        "github": "ThisGrrrlFriday",
        "email": "amcrehan@gmail.com",
        "tagline": "Mixxx Supporter",
    },
    "Evan": {
        "github": "ehendrikd",
        "discourse": "ehendrikd",
        "tagline": "Mixxx Contributor",
    },
    "Cristiano Lacerda": {
        "github": "crisclacerda",
        "discourse": "crisclacerda",
        "tagline": "GSoC 2020 Student",
    },
    "Aanyu Deborah Oduman": {
        "github": "deborahtrez",
        "discourse": "deborahao",
        "email": "deborahtrez12@gmail.com",
        "tagline": "Outreachy contributor (Dec 2020 - Mar 2021)",
    },
    "Daniel Schürmann": {
        "github": "daschuer",
        "discourse": "daschuer",
        "email": "daschuer@mixxx.org",
        "tagline": "Mixxx Core Developer",
    },
    "Nikolaus Einhauser": {
        "github": "Swiftb0y",
        "discourse": "swiftb0y",
        "email": "nikolaus.einhauser@mixxx.org",
        "tagline": "Mixxx Core Developer",
    },
    "David Chocholatý": {
        "github": "davidchocholaty",
        "discourse": "davidchocholaty",
        "email": "david.chocholaty12@gmail.com",
        "tagline": "GSoC 2022 Student",
    },
    "Fatih Emre YILDIZ": {
        "github": "fatihemreyildiz",
        "discourse": "fatihemreyildiz",
        "email": "fatihemreyildiz@gmail.com",
        "tagline": "GSoC 2022 Student",
    },
}

# Needed for Jinja2 markdown filter
md = markdown.Markdown()

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
JINJA_FILTERS = {"markdown": lambda text: jinja2.Markup(md.convert(text))}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
