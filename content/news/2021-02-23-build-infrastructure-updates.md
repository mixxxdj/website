title: "Improving the Mixxx developer experience with maintainable build infrastructure"
authors: Be.
tags: 2.3, builds, infrastructure
date: 2021-02-23 19:17:51

Since we [published Mixxx 2.3 beta in June 2020]({filename}/news/2020-06-07-mixxx-2-3-beta-released.md), you may have been wondering what has taken so long to get the 2.3.0 release out. Well, we have been very busy the past few months building a more sustainable technical infrastructure for the Mixxx project. We have [moved this website to the Pelican static site generator]({filename}/news/2020-12-15-website-improvents.md) and moved the [forums](https://mixxx.discourse.group/) to [Discourse](https://www.discourse.org/). Additionally, we had to do a ton of work for the macOS and Windows builds. "Building" software is the process of transforming the code that we write into an executable file that you can run on your computer.

## Build Servers

We [introduced support for the CMake build system]({filename}/news/2020-07-15-new-in-2-3-cmake.md) with the release of 2.3 beta, but there were still rough edges at that time, particularly for building Mixxx on Windows and macOS. When we released 2.3 beta, we planned to keep using the old SCons build system for 2.3 on the servers that make our official builds. However, shortly after we announced 2.3 beta, the self-hosted [Jenkins](https://www.jenkins.io/) Windows build server stopped working. That was far from the first time our self-hosted build servers went offline and we got tired of continually troubleshooting these self-hosted servers. So, we decided to not bother fixing the old build server and instead move our builds to a hosted service.

We were already using [AppVeyor](https://www.appveyor.com/) for Windows and [Travis](https://travis-ci.com/) for macOS & Linux continuous integration to build each commit (change to the code) to catch bugs early. However, we were not uploading the builds from AppVeyor or Travis to our file server at [downloads.mixx.org](https://downloads.mixxx.org/). Also, we were using the free options for these services. Together with the slow, old SCons build system, these CI builds hit the time limits on the free tiers so often or took so long to run that we often ignored them. When [Travis announced tighter restrictions on their free service](https://blog.travis-ci.com/2020-11-02-travis-ci-new-billing), we decided to evaluate other options.

It turned out that [GitHub Actions](https://github.com/features/actions) met all our needs with support for macOS, Windows, and Ubuntu. GitHub Actions allows us to run a maximum of 20 concurrent builds or 5 concurrent macOS builds with a 6 hour time limit for jobs. The 6 hour time limit for jobs is important because Mixxx's dependencies take about 4 hours for a full build without a cache.

While we are wary of being dependent on services that are powered by proprietary software and have [other serious issues](https://www.theverge.com/2019/10/9/20906213/github-ice-microsoft-software-email-contract-immigration-nonprofit-donation), no other service provides comparable computing resources as GitHub Actions does for free. For a busy project with little budget, that is super helpful. Moreover, GitHub Actions hosts the artifacts from every build, even on pull requests. This allows users to [test Mixxx](https://github.com/mixxxdj/mixxx/wiki/Testing) before we merge changes to the code without the users needing to know how to build Mixxx. This also makes it much easier for developers to test changes on operating systems they do not use personally, which is very helpful because all of our core development team runs Linux.

## macOS Woes

Since we were switching to a whole new build server setup, we decided to get the new system working with CMake rather than keep using the old SCons build system. Although CMake comes with tools to make macOS application bundle packages (the files users download and drag and drop to their `/Applications` folder), they are [sorely lacking](https://gitlab.kitware.com/cmake/cmake/-/issues/21568) and [badly documented](https://discourse.cmake.org/t/lost-with-getting-cpack-to-make-a-macos-bundle/2102/). Since none of our core developers use macOS and macOS is cumbersome to run in virtual machines, one of our core developers had to borrow an old Macbook Air from a friend to do this work. Getting CMake correctly building macOS packages took more than a week, but that was only the beginning of the journey.

A great aspect of using GitHub Actions for our builds is that GitHub does the work of keeping the operating systems and build tools in the virtual machine images up to date for us. However, when we tried to build Mixxx with our old archive of dependencies on GitHub Actions, it would not build because GitHub Actions no longer had a version of XCode old enough to support the macOS 10.13 SDK which was used on our old macOS build server.

So, we got GitHub Actions to run the scripts we used on the old build server to build all of Mixxx's dependencies. This took about another week of work. With a new archive of dependencies built by GitHub Actions, we could build Mixxx on GitHub Actions. Then, more complications became apparent.

The builds from GitHub Actions were so laggy that they were completely unusable, but the builds from the old build server with the same code were okay. It turned out that having our own build server that was such a hassle to upgrade that we didn't do it for years was masking a serious bug. Building Mixxx with a macOS SDK 10.14 or newer made Qt use layer backing. Combined with the legacy QGLWidget API we still use for Mixxx's waveforms, this was extremely slow. We have [previously attempted](https://github.com/mixxxdj/mixxx/pull/1974) to update to the newer QOpenGLWidget API. Although this performed much better on macOS, the waveforms jerked back and forth instead of scrolling smoothly. We considered trying to finish this work for 2.3, but the task is difficult and would require major changes to the waveform rendering code.

Ultimately solving this performance issue will require [rewriting our whole GUI for Qt6](https://forum.qt.io/topic/121746/determing-graphics-frame-swap-time-when-rendering-in-qt-6/) which will also be a huge challenge. If anyone reading this is skilled at graphics programming, please get in touch on our [Zulip chat](https://mixxx.zulipchat.com/). We could really use help figuring out how to rewrite waveform rendering for Qt6. For now, we are using an ugly hack of automatically downloading the macOS 10.13 SDK to build Mixxx with current versions of XCode that do not officially support that old of a macOS SDK.

But that was not the end of the macOS-specific bugs. While working on rebuilding our dependencies, we updated to Qt 5.12.10 from 5.12.3. However, when Mixxx was built with Qt 5.12.10, it [would not show any windows at all](https://bugreports.qt.io/browse/QTBUG-87014) on macOS 11. So for now we are stuck with Qt 5.12.3 and the macOS 10.13 SDK. Altogther, dealing with these macOS-specific problems took about 3 months of work, and we are glossing over some details here.

With CMake working on every OS we support, we changed our plans and decided to [drop support for SCons for 2.3]({filename}/news/2020-12-14-scons-cmake-migration.md).

## Winwoes

With macOS builds finally working on GitHub Actions, we still had challenges with Windows. Although we could build Mixxx on Windows on GitHub Actions using our old archive of dependencies, the server we used to build those dependencies was no longer functioning. In Mixxx 2.3, we have added support for analyzing tracks' musical key with [libkeyfinder](https://github.com/mixxxdj/libkeyfinder), but this new dependency was not in the old Windows build environment. We could not work around that by simply downloading libkeyfinder automatically when building Mixxx because libkeyfinder has its own dependency on [FFTW](http://fftw.org/). Moreover, if Mixxx users were affected by bugs in any of our dependencies, we would not be able to update them if we kept using the dependency archive from the old server.

We tried to get our [old Windows batch scripts for building Mixxx's dependencies](https://github.com/mixxxdj/buildserver/tree/2.3.x-windows) to run on GitHub Actions. However, like on macOS, we ran into challenges because GitHub Actions' virtual machine images had a more up to date version of the MSVC C++ toolchain than our old Windows build server. Our old scripts relied on old Visual Studio project files to build many of the dependencies. These did not work without modification on GitHub Actions. Updating those would have required a developer using Windows to update them using Visual Studio, but all of our core developers use Linux and nobody wanted to learn how to do that. If we did manage to do that, we would likely have to do that all over again when Microsoft releases a new version of Visual Studio.

Rather than update our old build scripts for Mixxx's Windows dependencies, we decided to abandon them in favor of Microsoft's new [vcpkg](https://github.com/microsoft/vcpkg) package manager for C & C++ libraries. Using a package manager is a much easier way of building our dependencies than our own custom build scripts. Many of our dependencies were already available in vcpkg, but many were not or had various issues using them with Mixxx. We had to add new packages for:

  * [chromaprint](https://github.com/microsoft/vcpkg/pull/15986)
  * [libdjinterop](https://github.com/microsoft/vcpkg/pull/15990) (will be a new dependency for Mixxx 2.4)
  * [libebur128](https://github.com/microsoft/vcpkg/pull/15988)
  * [libkeyfinder](https://github.com/microsoft/vcpkg/pull/15878)
  * [libid3tag](https://github.com/microsoft/vcpkg/pull/15991)

For several other packages, we had to get them building with CMake or make changes to their CMake build systems to make them usable for Mixxx on Windows. These are still waiting for CMake support to be merged upstream to the libraries before we submit packages to vcpkg upstream:

  * [hidapi](https://github.com/libusb/hidapi/pull/220)
  * [portaudio](https://github.com/PortAudio/portaudio/pull/461)
  * [rubberband](https://github.com/breakfastquay/rubberband/pull/18)
  * [fdk-aac](https://gitlab.freedesktop.org/wtaymans/fdk-aac-stripped/-/merge_requests/1)

![UPSTREAM ALL THE CODE!]({static}/images/news/upstream-all-the-code.png)

This took another month of work after spending three months working on the macOS builds, but it was well worth it. The old scripts to build Mixxx's Windows dependencies on the old server took 36 hours to run because the server built both 32 and 64 bit binaries and built each with two different set of compiler options. We are dropping support for 32 bit Windows in Mixxx 2.3, so half of that build time is gone. A full build of Mixxx's Windows dependencies with vcpkg takes about 4 hours. Now, with caching on GitHub Actions, adding or modifying a dependency for Mixxx only takes about 20 minutes.

Using vcpkg has allowed us to build Mixxx with some dependencies that were missing on Windows before because nobody wanted to put in the effort to write Windows batch scripts to build them. Now, Mixxx can play module tracker files with [libmodplug](https://github.com/Konstanty/libmodplug) and use LV2 effects plugins on Windows. Coincidentally, as we were working on this, falkTX at DISTRHO published the first release of [PawPaw](https://kx.studio/News/?action=view&url=announcing-pawpaw-cross-platform-lv2-ports-for-macos-and-windows) bringing many LV2 plugins common on Linux to Windows and macOS, which can now be used with Mixxx! Here is Mixxx working on Windows with LV2 plugins, Modplug, and KeyFinder all working:

![Screenshot showing Mixxx with LV2 plugins, module tracker support, and KeyFinder support]({static}/images/news/lv2-modplug-keyfinder-windows.png)

vcpkg is great for us because it works on Windows, macOS, and Linux. This allows us to work on packaging Mixxx's dependencies for Windows while we work on Linux. As long as the dependency's build system is crossplatform (CMake or Meson), this is quite easy. If they do not have crossplatform build systems, that is one reason we are working on getting CMake support merged upstream. Plus vcpkg's [overlay feature](https://github.com/microsoft/vcpkg/blob/master/docs/specifications/ports-overlay.md) makes it easy for us to make custom modifications to certain packages while easily merging updates from upstream for every other package.

Most of our dependencies already work on macOS and Linux with vcpkg, with the notable exception of the unmaintained [portmidi](http://portmedia.sourceforge.net/portmidi/) library. When we get that working with vcpkg, or potentially replace it with a currently maintained crossplatform MIDI library such as [RtMidi17](https://github.com/jcelerier/RtMidi17), we will be able to use vcpkg for all our dependencies for both Windows and macOS. For Linux, we are considering distributing Mixxx as a Flatpak using the dependencies from vcpkg in the future, but this [will have to wait](https://github.com/flatpak/flatpak/issues/1509) until [PipeWire](https://pipewire.org/) is included in more Linux distributions, which will start happening in the next couple of months with the releases of [Fedora 34](https://fedoraproject.org/wiki/Changes/DefaultPipeWire) and [Ubuntu 21.04](https://bugs.launchpad.net/ubuntu/+source/pipewire/+bug/1802533/comments/33).

## Developer Experience

All of this work has been very tedious. We would have much rather spent this effort writing fun new features for Mixxx, but this had to be done to keep the project going. Now that it is working, developing for Mixxx is much nicer.

As we got the new setup going with GitHub Actions, we wrote scripts that can be used both by GitHub Actions and by developers that want to set up a development environment on their computer. The scripts automatically download the archive of Mixxx's dependencies. On macOS, the script sets the appropriate environment variables. On Windows, the script generates a [`CMakeSettings.json` file](https://docs.microsoft.com/en-us/cpp/build/cmakesettings-reference) which can be used to setup Visual Studio to work on Mixxx very easily. We hope this makes Mixxx more welcoming for Windows and macOS developers to contribute.

Developers on every OS can now easily have their code built and tested automatically on Windows, macOS, and Linux simply by pushing commits to GitHub, and we can ask users to give feedback using the build artifacts from GitHub Actions.

On macOS and Linux, the builds on GitHub Actions only take a few minutes now that we are using [ccache](https://ccache.dev/) which was [easy to implement with CMake](https://cmake.org/cmake/help/latest/prop_tgt/RULE_LAUNCH_COMPILE.html). We have tried getting compiler caching working on Windows with [sccache](https://github.com/mixxxdj/mixxx/pull/3618) and [clcache](https://github.com/mixxxdj/mixxx/pull/3473) but have not succeeded yet, so the Windows builds still take about 40 minutes.

Historically, issues with the build servers have been a major factor why Mixxx releases have been so few and far between. We hope that by having this automated on a reliable service that we do not need to maintain ourselves, we can focus more on programming cool new features and getting Mixxx releases published more regularly.

If you want to [get involved](https://mixxx.org/get-involved/) in making Mixxx more awesome, come introduce yourself on our [Zulip chat](https://mixxx.zulipchat.com/#narrow/stream/109123-introduce-yourself). You do not need to be a coder to contribute. Our new infrastructure makes contributing easier both for developers and testers!

## Addendum: compiler caching on Windows

After figuring out [undocumented requirements](https://github.com/mozilla/sccache/pull/963) for [sccache](https://github.com/mozilla/sccache), [fixing](https://github.com/mozilla/sccache/pull/962) a bug in it, and [fixing](https://github.com/google/googletest/pull/3291) another bug in [Google Test](https://github.com/google/googletest), and working around [a bug in GitHub Actions caching](https://github.com/actions/cache/issues/531), we have compiler caching [working on Windows](https://github.com/mixxxdj/mixxx/pull/3618). Windows builds now take 16-18 minutes. That is significantly longer than macOS which takes about 10 minutes, but it is a
big improvement from 40 minutes per Windows build without compiler caching!
