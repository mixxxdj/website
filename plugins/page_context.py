# -*- coding: utf-8 -*-

class MenuItem:
    def __init__(self, url, title, context, css="", children=()):
        self.url = url
        self.title = title
        self.context = context
        self.css = css
        self.children = children


def preBuildPage(page, context, data):
    """
    Updates the context of the page to include: the page itself as {{ CURRENT_PAGE }}
    """

    # This will run for each page that Cactus renders.
    # Any changes you make to context will be passed to the template renderer for this page.

    menu = (
        MenuItem("/news", "News", "Navigation bar link to Mixxx News page."),
        MenuItem("/about", "About", "Navigation bar link to Mixxx About page.", children=(
            MenuItem("/features", "Features", "Navigation bar link to Mixxx features page."),
            MenuItem("/screenshots", "Screenshots", "Navigation bar link to Mixxx Screenshots page."),
            MenuItem("/contact", "Contact", "Navigation bar link to Mixxx contact page."),
            MenuItem("/press", "Press", "Navigation bar link to Mixxx Press page"),
        )),
        MenuItem("/support", "Support", "Navigation bar link to Mixxx support page.", children=(
            MenuItem("/manual/latest", "Manual", "Navigation bar link to Mixxx Manual."),
            MenuItem("https://github.com/mixxxdj/mixxx/wiki", "Wiki", "Navigation bar link to Mixxx Wiki."),
            MenuItem("https://github.com/mixxxdj/mixxx/wiki/Hardware%20compatibility", "Compatible Hardware", "Navigation bar link to Mixxx supported hardware wiki page."),
            MenuItem("https://mixxx.discourse.group/", "Forums", "Navigation bar link to Mixxx Forums."),
        )),
        MenuItem("/get-involved", "Get Involved", "Navigation bar link to Mixxx Community page.", children=(
            MenuItem("https://mixxx.zulipchat.com/", "Chat", "Navigation bar link to Mixxx Zulip chat."),
            MenuItem("https://github.com/mixxxdj/mixxx", "Code", "Navigation bar link to Mixxx code repository."),
            MenuItem("https://bugs.launchpad.net/mixxx/", "Bugs & Feature Ideas", "Navigation bar link to Mixxx bug tracker."),
        )),
    )

    extra = {
        "CURRENT_PAGE": page,
        # Add your own dynamic context elements here!
        "NAV_MENU": menu
    }

    context.update(extra)
    return context, data
