title: SCons build system dropped in favor of CMake
author: Jan Holthuis
date: 2020-12-14 14:07:57
tags: development, 2.3, beta, cmake, scons

If you wanted to compile a recent version of Mixxx 2.3 beta or 2.4 yourself, you may have already noticed that we removed our old and rusty [SCons](https://scons.org/) setup in favor of [CMake](https://cmake.org/).

[A few months ago]({filename}/news/2020-07-15-new-in-2-3-cmake.md) we said that we were planning to ship Mixxx 2.3 with both SCons and CMake configurations (the latter would be considered "experimental").
However, that turned out to be impractical.

![Mixxx 2.3 building with CMake]({static}/images/news/mixxx-cmake-build.png)

All of core developers started using CMake as their primary build system since [initial support for it was added](https://github.com/mixxxdj/mixxx/pull/2280) more than a year ago.
Our build servers that we use to compile and test Mixxx during development have also been switched to CMake.
That means that the SCons build received a lot less testing compared to the CMake build.

Due to the maintenance burden of keeping an additional build system and some problems with our SCons configuration that popped up recently, we decided to [remove SCons](https://github.com/mixxxdj/mixxx/pull/2777) and use CMake exclusively for the upcoming 2.3 release.
That should free some resources and will allow us to work on more important issues than keeping our SCons build alive.
