title: Mixxx 1.7.0 Beta1 for Windows x64 Now Available!
authors: Albert Santoni
date: 2009-05-07 14:43:00
tags: 1.7, 1.7.0, beta, windows, release announcement
comments: no

The Mixxx team is pleased to announce the availability of a 64-Bit version of Mixxx 1.7.0 Beta1 for Windows.

In a dazzling display of masochism and borderline insanity, Sean Pappalardo has been working hard over the last month or so to get Mixxx to run **natively** on 64-bit Windows.
When asked why, he just mumbled, "full power...full power" over and over again as he rocked in his chair. Sean comes from the Commodore 64 programming days of yore when 64 KB of RAM and a 1 MHz CPU was all you had to work with, so he enjoys taking maximum advantage of the available hardware.

While 64-bit versions of Mixxx have been available on Linux for the past year, this is the first time it's been done on Windows.

Why was there no 64-bit version of Mixxx for Windows? As Sean found out, this was not simply a matter of recompiling Mixxx - *all* of Mixxx's dependencies had to be rebuilt as x64 binaries as well.
This process brought numerous headaches and profanity-littered screams because Microsoft's Visual Studio is not always easy to deal with (especially when you're trying to force the free version to compile x64 binaries which involves a [hack](http://whitemarker.blogspot.com/2006/12/c-visual-c-2005-express-edition-x64.html).)
Fortunately a couple of the libraries that Mixxx depends on (libsndfile, FFTW) already had x64 binaries available for download, and for that we are very grateful.
The good news is that, unless we decide they need upgrading, the dependencies don't have to be rebuilt in the future, so the hard part is done for now.

Mixxx is now **the first and only** known DJ software package that runs **natively** on 64-bit Windows, and this gives 64-bit Mixxx fans improved performance for free.
A native 64-bit build also improves compatibility with ASIO devices on 64-bit Windows.

To take advantage of this, you need three things:

1.  a 64-bit AMD or Intel processor (eg. AMD Athlon 64, AMD Phenom, Intel Core 2)
2.  a 64-bit version of Windows (XP Professional x64, Vista x64, Server 2003 x64, etc.)
3.  A copy of [Mixxx x64 for Windows](http://downloads.mixxx.org/mixxx-1.7.0-beta1/mixxx-1.7.0~beta1-win64.exe)

Install and run as usual, and enjoy! Please let us know if you have any problems or questions.
