# Mixxx Website

This repository contains the source to [Mixxx website][mixxx.org]. This site is
built with [Pelican][pelican], a static site generator.

## Quick Start

To get started contributing to the Mixxx website, first install all requirements
(e.g. Pelican). Optionally, use a [virtual environment][virtualenv] to isolate
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

## Adding new articles

To add a new article, add a file named `XXXX-XX-XX-my-first-post.md` to `content/news/`:

```markdown
title: My first post
authors: Jan Holthuis
status: draft
tags: some tag, some other tag, yet another tag
comments: yes

Here goes the article content.
Articles are formatted in [Markdown](https://python-markdown.github.io/).

YouTube videos can be embedded like this:

@Video(https://www.youtube.com/watch?v=rt5Ed5GZ1U8)
```

Note that the `XXXX-XX-XX` part of the filename is *not* meant to be a placeholder, just use it literally.
Let the `status` on `draft` and don't add a `date` field.
When the PR is merged, GitHub actions will automatically rename the file, add the appropriate date and remove the draft status.

If you are previewing your changes locally, Pelican will not add the new post to the blog unless you set the environment variable `CONTEXT` to `deploy-preview`:

    $ CONTEXT=deploy-preview pelican --listen --autoreload

Run that command from the root of this git repository.

## Submitting Changes

Regardless of whether you'd like to submit website content (blog posts, new
pages, etc.) or changes in website coding. You will need to conform to our
coding styles. As with most of our other repositories, we use
[pre-commit](https://pre-commit.com/) for that. Since you should already have a
working python setup, [installing pre-commit is very
easy](https://pre-commit.com/#installation).

```bash
pip install pre-commit # to install pre-commit on your machine
pre-commit install # to register pre-commit with git so your changes are checked before committing ("pre-commit" so to speak :) )
```

Afterwards, submitting changes is as easy as making your commits (make sure you
make those on your own branch instead of the `website` one ), pushing them to
your fork and filing a Pull request on the `mixxxdj/website` repository. If
you're having trouble with this step and need a more in depth guide, there are
plenty of good tutorials on the internet on how to use git and github.

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
[virtualenv]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
