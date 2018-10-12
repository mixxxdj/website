#coding:utf-8

def preBuildPage(page, context, data):
    """
    Updates the context of the page to include: the page itself as {{ CURRENT_PAGE }}
    """

    # This will run for each page that Cactus renders.
    # Any changes you make to context will be passed to the template renderer for this page.

    menu = [
        ("/download.html", "big", "Download", "Navigation bar link to Mixxx download page."),
        ("/features.html", "big", "Features", "Navigation bar link to Mixxx features page."),
        ("/support.html", "big", "Support & Community", "Navigation bar link to Mixxx support page."),
        ( "/manual/latest", "medium", "Manual", "Navigation bar link to Mixxx Manual."),
        ( "/forums", "medium", "Forums", "Navigation bar link to Mixxx Forums."),
        ( "/wiki", "medium", "Wiki", "Navigation bar link to Mixxx Wiki."),
        ( "http://mixxxblog.blogspot.com", "medium", "Blog", "Navigation bar link to Mixxx blog."),
        ( "/press.html", "small", "Press", "Navigation bar link to Mixxx Press page"),
        ( "/get-involved.html", "small", "Get Involved", "Navigation bar link to Mixxx Get Involved page." ),
        ( "/contact.html", "small", "Contact", "Navigation bar link to Mixxx contact page.")
    ]

    extra = {
        "CURRENT_PAGE": page,
        # Add your own dynamic context elements here!
        "NAV_MENU": menu
    }

    context.update(extra)
    return context, data