title: Mixxx 1.6.0 Beta 3 Released!
author: Albert
date: 2008-05-27 18:52:00
comments: no

[![Mixxx Logo]({static}/images/news/logo-mixxx.png)]({static}/images/news/logo-mixxx.png)

The Mixxx development team is proud to announce the release of **Mixxx 1.6.0 Beta 3** ([download]({filename}/pages/download.md))!

It's been 3 months since our last beta release, and in that time we've been busy fixing tons of bugs and sneaking in the occasional new feature.
We put major effort into solving a few stability issues people encountered with our last beta, as well as fixing many other quirks.
We'd like to thank all of our users who've been reporting bugs in our [bug tracker](https://bugs.launchpad.net/mixxx/), as your reports have saved us a great deal of time.

Anyways, on with the juicy **changelog** since Beta 2:

- Added BPM reading from MP3/OGG files which have it embedded in them (ID3), one of several enhancements by Martin Sakmar
- Various accuracy improvements to the BPM detection
- Added preliminary support for multiple inputs with vinyl control
  (consecutive channel pairs only - eg. 1/2 and 3/4)
- Support for the Hercules DJ Console RMX
- Hercules DJ Console MK2 bug fixes
- Support for the Hercules DJ Console Mac Edition
- Support for the Behringer BCD3000, including LEDs
- Support for the Akai MPD24
- Improvements to the vinyl emulation and pitch-independent time stretch sound quality
- LADSPA effects support is rapidly improving, but is not compiled in by default yet (`scons ladspa=1`)
- Finished adding recording support
- Performance improvements while using vinyl control
- Support for 96000 Hz samplerates with Serato vinyls
- Build flags are now cached automatically
- Improved flanger effect, thanks to [Enry](http://www.jamendo.com/pl/album/21933)
- [Configurable cue behaviour](https://github.com/mixxxdj/mixxx/wiki/configurable_cue_behaviour), which now defaults to CDJ-style cueing. (Thanks to Tom Care)
- Enabled realtime priority with ALSA, improves performance with Linux RT kernels.
- FLAC support for Linux and OS X users (much requested)
- Tons and tons of bug fixes.

Mixxx 1.6.0 Beta 3 is available on our [downloads page]({filename}/pages/download.md).

The development of multiple-input soundcard support (with vinyl control) was made possible by [Echo Digital Audio](http://www.echoaudio.com/).
Echo makes *very* nice professional soundcards, and their [AudioFire](http://www.echoaudio.com/Products/FireWire/index.php) line of cards are excellent FireWire solutions for DJs on-the-road and in the studio.
I've been using one of their cards for development, and they work very well on Windows and OS X.
Support for AudioFire cards on Linux is improving rapidly through the [FFADO](http://www.ffado.org/) project as well.

We've also bundled some **free tracks** from [Ugress](http://www.ugress.com/) and [Carlo Carosi](http://www.myspace.com/carlocarosi) with this release.
These tunes will give DJs something to mix right out-of-the-box, and we think you'll like them.

For our next release, we're going to shift focus towards polishing the remaining rough edges and fixing the remaining critical bugs we find.
Whether our next release will be a fourth beta or the 1.6.0 final release remains to be decided, as it depends mainly on how many critical bugs we find and how much time we have to fix them.
If you want to **help us** fix bugs, please join us on IRC (#mixxx on Freenode) and we'd be glad to help you get started hacking Mixxx.
