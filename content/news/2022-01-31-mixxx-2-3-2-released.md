title: Mixxx 2.3.2 released
authors: Jan Holthuis
tags: 2.3, 2.3.2, release announcement
comments: yes
date: 2022-01-31 22:18:57

New year, new Mixxx - we're starting 2022 with the release of [Mixxx 2.3.2](https://github.com/mixxxdj/mixxx/releases/tag/2.3.2)!
[Grab it from our download page]({filename}/pages/download.md#stable) and install it on Windows, macOS and Linux.

This release irons out a few bugs and adds support for the [Pioneer DDJ-SB3 controller](https://manual.mixxx.org/2.3/en/hardware/controllers/pioneer_ddj_sb3.html). The [full changelog](https://manual.mixxx.org/2.3/en/chapters/appendix/changelog.html#v2-3-2) can be found below. In case you're a Linux package maintainer please double check the [Packaging section](https://github.com/mixxxdj/mixxx/blob/2.3.2/CHANGELOG.md#packaging) in the changelog and modify your packaging script if necessary.


## Changelog

* Playlist: Enable sorting by color [#4352](https://github.com/mixxxdj/mixxx/pull/4352) [lp:1945976](https://bugs.launchpad.net/mixxx/+bug/1945976)
* Fix crash when using Doubling/Halving/etc. BPM from track's Properties window on tracks without BPM [#4587](https://github.com/mixxxdj/mixxx/pull/4587) [lp:1955853](https://bugs.launchpad.net/mixxx/+bug/1955853)
* Fix writing metadata on Windows for files that have never been played [#4586](https://github.com/mixxxdj/mixxx/pull/4586) [lp:1955331](https://bugs.launchpad.net/mixxx/+bug/1955331)
* Preserve file creation time when writing metadata on Windows [#4586](https://github.com/mixxxdj/mixxx/pull/4586) [lp1955314](https://bugs.launchpad.net/mixxx/+bug/1955314)
* Fix handling of file extension when importing and exporting sampler settings [#4539](https://github.com/mixxxdj/mixxx/pull/4539)
* Fix crash when using an empty directory as resource path using the `--resource-path` command line option [#4575](https://github.com/mixxxdj/mixxx/pull/4575) [lp:1934560](https://bugs.launchpad.net/mixxx/+bug/1934560)
* Pioneer DDJ-SB3: Add controller mapping [#3821](https://github.com/mixxxdj/mixxx/pull/3821)
* Don't wipe sound config during startup if configured devices are unavailable [#4544](https://github.com/mixxxdj/mixxx/pull/4544)
* Append selected file extension when exporting to playlist files [#4531](https://github.com/mixxxdj/mixxx/pull/4531) [lp:1889352](https://bugs.launchpad.net/mixxx/+bug/1889352)
* Fix crash when using midi.sendShortMsg and platform vnc [#4635](https://github.com/mixxxdj/mixxx/pull/4635) [lp:1956144](https://bugs.launchpad.net/mixxx/+bug/1956144)
* Traktor S3: Fix timedelta calculation bugs [#4646](https://github.com/mixxxdj/mixxx/pull/4646) [lp:1958925](https://bugs.launchpad.net/mixxx/+bug/1958925)

### Packaging

- Downloads of external dependencies are placed in build/downloads
- The sources for libkeyfinder are now expected in build/downloads/libkeyfinder-2.2.6.zip instead of build/download/libkeyfinder/v2.2.6.zip
- CMake: Adjust the download directory and name of external dependencies [#4511](https://github.com/mixxxdj/mixxx/pull/4511)
- Fix/Improve Appstream metainfo [#4344](https://github.com/mixxxdj/mixxx/pull/4344) [#4346](https://github.com/mixxxdj/mixxx/pull/4346) [#4349](https://github.com/mixxxdj/mixxx/pull/4349)
