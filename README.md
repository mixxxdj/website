# Mixxx Website

This repository contains the source to [Mixxx website][mixxx.org]. This site is
built with [Pelican][pelican], a static site generator.

## Quick Start

To get started contributing to the Mixxx website, first install all requirements
(e.g. Pelican). Optionally, use a [Virtualenv][virtualenv] to isolate
dependencies.

    $ pip install -r requirements.txt

Then build the site from its templates, run this in root directory of the git
repository:

    $ pelican

If all goes well, you should have the rendered HTML in your `output/`
directory. To stand up a development server to test out your change, type:

    $ pelican --listen --autoreload

You can then visit ```http://127.0.0.1:8000``` to see your development version
of the site.

## Documentation

Pelican uses [Jinja2][jinja2] templates for rendering pages.

The main templates are stored in the `theme/templates/` folder. Leaf pages are
stored in `theme/templates/pages/`. If there is a snippet of code you want to
use in multiple places on the site, place it in the `/theme/templates/` folder
-- for example [theme/templates/download_button.html][download_button.html].

* [Jinja2 template language][jinja2_templates]
* [template internationalization][jinja2_template_i18n]
* [Pelican documentation][pelican_docs]

## Internationalization / Translation

All strings wrapped with `{% trans %}Hello World {% endtrans %}` are flagged
for translation. Whenever adding new English strings to the website, please
wrap them in a `{% trans %}Hello World{% endtrans %}` block.

[mixxx.org]: http://mixxx.org/
[pelican]: https://github.com/getpelican/pelican
[pelican_docs]: https://docs.getpelican.com/en/latest/
[django_templates]: https://jinja.palletsprojects.com/en/2.11.x/templates/
[jinja2_template_i18n]: https://jinja.palletsprojects.com/en/2.11.x/extensions/#i18n-extension
[download_button.html]: https://github.com/mixxxdj/website/blob/website/templates/download_button.html
[virtualenv]: https://virtualenv.pypa.io/en/stable/
