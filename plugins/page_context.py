#coding:utf-8

def preBuildPage(page, context, data):
    """
    Updates the context of the page to include: the page itself as {{ CURRENT_PAGE }}
    """

    # This will run for each page that Cactus renders.
    # Any changes you make to context will be passed to the template renderer for this page.

    menu = [
        ("/download", "Download", "Navigation bar link to Mixxx download page."),
        ("/features", "Features", "Navigation bar link to Mixxx features page."),
        ("/support", "Support", "Navigation bar link to Mixxx support page."),
        ("/get-involved", "Contribute", "Navigation bar link to Mixxx contributions page."),
    ]

    extra = {
        "CURRENT_PAGE": page,
        # Add your own dynamic context elements here!
        "NAV_MENU": menu
    }

    context.update(extra)
    return context, data