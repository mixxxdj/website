title: Mixxx 1.8.0 Beta 1 Released!
author: Albert
date: 2010-02-15 03:56:00
comments: no

[![Mixxx 1.8.0]({static}/images/news/Picture-10.png)]({static}/images/news/Picture-10.png)

The Mixxx team is proud to announce the first beta of **Mixxx 1.8.0** !

This beta release is intended to give DJs an opportunity to play with our [new features]({filename}/news/2009-12-23-mixxx-18-preview.md) and help us [find bugs](https://bugs.launchpad.net/mixxx/+filebug).

[**Download Now!**]({filename}/pages/download.md)

**Mixxx 1.8.0 Beta 1** features a slew of major improvements over our last release, including looping controls, support for multiple MIDI devices, and a completely revamped library.

Although our code for playing M4A files in Mixxx is complete, we were disappointed to learn that we cannot ship Mixxx 1.8.0 Beta 1 with M4A support for legal reasons. We're currently exploring other options to bring you this much-requested feature, but in the meantime, we still wanted to have a public beta release for everyone to play with.

We don't expect the stability of this beta release to be as good as 1.7.2, so if you're planning on DJing live, please don't use the 1.8.0 betas. Please report any bugs you find on [our bug tracker](https://bugs.launchpad.net/mixxx/+filebug) - It's very difficult for us to keep track of bugs that are reported on the forums or in comments on the blog, so having all our bug reports in [one place](http://bugs.launchpad.net/mixxx) makes them much easier to manage. Thanks for your cooperation!

If you're planning on switching back and forth between 1.7 and 1.8, we recommend backing up your Mixxx XML library file. You can find your library file, called [mixxxtrack.xml]{.Apple-style-span style="font-family: 'Courier New', Courier, monospace;"} in the following places:

-   **Windows**: Click *Start → Run...*, and paste in: `explorer %USERPROFILE%\%Local Settings\Application Data\Mixxx`
-   **Mac OS X**: Open Finder, and from the top menu select *Go → Go to Folder...*, and paste in: `~/.mixxx`
-   **Linux**: Open a terminal, and paste in: `cd ~/.mixxx`

From there, copy and paste your `mixxxtrack.xml` file to a safe location.
When you first run Mixxx 1.8, your library will be upgraded to our new database format and stored in a different file called `mixxxdb.sqlite`.
Your `mixxxtrack.xml` file will be renamed `mixxxtrack.bak`, and so if you'd like 1.7 to see your old library again, you will either need to rename `mixxxtrack.bak` to `mixxxtrack.xml`, or restore the backed up copy of `mixxxtrack.xml` from your safe location.

Lastly, we wanted to release a beta version to not only let you help us find bugs, but also as an invitation to get involved and **help us fix bugs** .
If you know C++, we encourage you to dive into our source code and try to fix bugs that affect you.
We're perpetually short-handed and we're always looking for more help.
The more people that get involved, the more fun it is for us too.
We understand that looking at a new codebase can be daunting, so if you'd like some extra direction, we'd be more than happy to help you - Come hang out in our IRC channel (#mixxx on Freenode), and we'll get you started!
