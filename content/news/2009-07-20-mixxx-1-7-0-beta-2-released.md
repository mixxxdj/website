title: Mixxx 1.7.0 Beta 2 Released!
authors: Albert Santoni
date: 2009-07-20 18:00:00
comments: no

[![Screenshot of Mixxx 1.7.0-beta2]({static}/images/news/Screenshot-Mixxx-1.7.0-beta2-2.png)]({static}/images/news/Screenshot-Mixxx-1.7.0-beta2-2.png)

The Mixxx team is pleased to announce the release of **[Mixxx 1.7.0 Beta 2](http://www.mixxx.org/download/)**!
This is primarily a bugfix release that addresses issues from our previous beta.

We also recently discovered a critical issue in an external software library which affects Mixxx users on **Ubuntu 9.04**.
Please see the note at the bottom of this post for more information.

Some of the changes in Mixxx 1.7.0 Beta 2 include:

-   Fixed missing MIDI bytes under heavy load on Linux.
-   Fixed vinyl control input for users with multi-channel input.
-   Fixed vinyl control channel selection bug
-   A slew of SCS.3d improvements and tweaks.
-   Hercules MK2 and RMX improvements
-   Stanton SCS.1m support
-   Internal control engine optimizations
-   Fixed several crash-on-startup scenarios
-   Fixed library rescans not finding new files added in subdirectories
-   Fixed Ubuntu menu shortcut
-   Fixed missing Ubuntu package dependencies
-   **Added Universal Package for OS X 10.4+**
    (Special thanks to Brian Jackson for leading the effort to put this together.)

Mixxx 1.7.0 Beta 2 is available on our [downloads page]({filename}/pages/download.md#beta).

Formality aside, this list of changes doesn't do the last few months justice.
After our last beta, we received dozens of helpful bug reports.
Some of those brought new problems to our attention, while others shed light on old ones.
With your valuable feedback, we managed to not only fix your most pressing bugs, but we were also able to track down and fix some other *very* tricky bugs.
The result of your great bug reporting and our team's commitment to fixing bugs is the most stable, polished release of Mixxx to date, and we couldn't have done it without you.

Thank you to everyone who's been testing our beta releases and reporting bugs.
You've made a valuable contribution to open source and the whole Mixxx community, and together we're going to continue to make Mixxx the best DJ software we can.

As usual, please report any new bugs or regressions to our [bug tracker](https://bugs.launchpad.net/mixxx).
If you want to get in touch with other Mixxx DJs, show some love on [our forums](http://www.mixxx.org/forums)!

Stay tuned for our final 1.7.0 release!

**Important note for Ubuntu 9.04 users:**
A flaw has been discovered in a library provided by Ubuntu 9.04 that can cause critical hangups in Mixxx.
Ubuntu 9.04 users are advised to install the version of PortAudio from Ubuntu 8.10, available as .deb packages here:

-   [PortAudio for i386](http://packages.ubuntu.com/intrepid/i386/libportaudio2/download)
-   [PortAudio for amd64](http://packages.ubuntu.com/intrepid/amd64/libportaudio2/download)
