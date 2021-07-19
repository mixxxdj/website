title: Mixxx 2.3.1 released
authors: Owen Williams
tags: 2.3, 2.3.1, release announcement
comments: yes
date: 2021-07-19 14:55:00

Mixxx is releasing version 2.3.1, a minor update to the recent major [2.3.0 release]({filename}/news/2021-06-28-mixxx-2-3-0-released.md).
It contains some small critical fixes and we recommend that all users [update to this version]({filename}/pages/download.md#stable).

## Changes
* AutoDJCratesDAO: Fix crash after loading/unloading tracks. [lp1936396](https://bugs.launchpad.net/mixxx/ [#4107](https://github.com/mixxxdj/mixxx/pull/4107)+bug/1936396)
* Fix bad phase seek when starting from preroll. [lp1930143](https://bugs.launchpad.net/mixxx/+bug/1930143) [#4093](https://github.com/mixxxdj/mixxx/pull/4093)
* Fix wrong track being recorded in History [lp1933991](https://bugs.launchpad.net/mixxx/+bug/1933991) [#4041](https://github.com/mixxxdj/mixxx/pull/4041)
* Rekordbox: Handle exception when parsing corrupt .pdb files [lp1933853](https://bugs.launchpad.net/mixxx/+bug/1933853) [#4040](https://github.com/mixxxdj/mixxx/pull/4040)