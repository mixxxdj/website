# Mixxx Website

This repository contains the source to [Mixxx website][mixxx.org]. This site is
built with [Cactus][cactus], a static site generator.

## Quick Start

To get started contributing to the Mixxx website, first install all requirements
(e.g. Cactus). Optionally, use a [Virtualenv][virtualenv] to isolate
dependencies.

    $ pip install -r requirements.txt

If using conda (Anaconda/Miniconda) we recommend setting an environment with python 2.7:

    $ conda create --name mixxx_website python=2.7
    $ conda activate mixxx_website

Then build the site from its templates:

    $ cactus build

If all goes well, you should have the rendered HTML in your ```.build```
directory. To stand up a development server to test out your change, type:

    $ cactus serve

You can then visit ```http://127.0.0.1:8000``` to see your development version
of the site.

## Documentation

Cactus uses [Django][django]'s templates for rendering pages.

The main templates are stored in the ```templates/``` folder. Leaf pages are
stored in ```pages/```. If there is a snippet of code you want to use in
multiple places on the site, place it in the ```templates/``` folder -- for
example [templates/download_button.html][download_button.html].

* [Django template language][django_templates]
* [template internationalization][django_template_i18n]
* [Cactus documentation][cactus_docs] (not super useful)

## Internationalization / Translation

All strings wrapped with ```{% trans 'Hello World' %}``` are flagged for
translation. Whenever adding new English strings to the website, please wrap
them in a ```{% trans 'Hello World' %}``` block.

## Publishing

**Note: Requires SSH access to mixxx.org.**

First, publish to http://staging.mixxx.org:

```
$ fab staging rebuild publish
```

Visit the staging site to verify everything looks ok. Then, publish to the production site:

```
$ fab production rebuild publish
```

Visit https://mixxx.org to verify everything looks ok.

[mixxx.org]: http://mixxx.org/
[cactus]: https://www.staticgen.com/cactus
[cactus_docs]: http://cactusformac.com/docs/
[django]: http://djangoproject.com/
[django_templates]: https://docs.djangoproject.com/en/1.8/ref/templates/language/
[django_template_i18n]: https://docs.djangoproject.com/en/1.8/topics/i18n/translation/#internationalization-in-template-code
[download_button.html]: https://github.com/mixxxdj/website/blob/website/templates/download_button.html
[virtualenv]: https://virtualenv.pypa.io/en/stable/
