# Mixxx Website

This repository contains the source to [Mixxx website][mixxx.org]. This site is
built with [Cactus][cactus], a static site generator.

## Quick Start

To get started contributing to the Mixxx website, first install cactus:

    $ pip install cactus

Then build the site from its templates:

    $ cactus build

If all goes well, you should have the rendered HTML in your ```.build```
directory. To stand up a development server to test out your change, type:

    $ cactus serve

You can then visit ```http://127.0.0.1:8000``` to see your development version
of the site.

## Internationalization / Translation

All strings wrapped with ```{% trans 'Hello World' %}``` are flagged for
translation. Whenever adding new English strings to the website, please wrap
them in a ```{% trans 'Hello World' %}``` block.

[mixxx.org]: http://mixxx.org/
[cactus]: https://www.staticgen.com/cactus
