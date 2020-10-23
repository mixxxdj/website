#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import datetime
import feedparser
import slugify
import re
import sys


DEFAULT_RSS_URL = (
    "https://mixxxblog.blogspot.com/feeds/posts/default" "?max-results=1000"
)


def parse_feed(rss_url):
    feed = feedparser.parse(rss_url)
    items = feed["items"]
    for item in items:
        date = datetime.datetime(*item["published_parsed"][:6])
        date_short = date.strftime("%Y-%m-%d")
        date_long = date.isoformat(sep=" ")
        title = item["title"]
        author = item["author_detail"]["name"]
        filename = "{}-{}.html".format(date_short, slugify.slugify(title))
        value = item["content"][0]["value"]
        value = re.sub(r"(\</[^>]*>)", r"\g<1>\n", value)
        value = re.sub(r"(\<[^>]*/>)", r"\g<1>\n", value)
        if re.match(r"<h\d>.*</h\d>.*", value.splitlines()[0]):
            value = "".join(value.splitlines()[1:])
        if re.match(r"<br(\s+[^>]*)>", value.splitlines()[0].strip()):
            value = "".join(value.splitlines()[1:])
        with open(filename, "w") as f:
            f.write(
                (
                    "title: {title}\n"
                    "author: {author}\n"
                    "date: {date}\n"
                    "\n"
                    '{{% extends "post.html" %}}\n'
                    "\n"
                    "{{% block post %}}\n"
                    "\n"
                    "{content}\n"
                    "\n"
                    "{{% endblock %}}\n"
                ).format(
                    title=title,
                    date=date_long,
                    author=author,
                    content=value,
                )
            )
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("url_or_file", metavar="URL_OR_FILE", nargs="?")
    args = parser.parse_args(argv)
    if not args.url_or_file:
        args.url_or_file = DEFAULT_RSS_URL
    return parse_feed(args.url_or_file)


if __name__ == "__main__":
    sys.exit(main())
