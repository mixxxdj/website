title: Mixxx 2.3.6 released
authors: Daniel Schürmann
tags: 2.3, 2.3.6, release announcement
status: draft
comments: yes

Welcome the Mixxx release version 2.3.6, the final maintenance release before releasing the upcoming 2.4.0 with exiting new features.

This small bug fix release may appear insignificant, but it's a testament to the rock-solid quality we bring to every user and tp ensure a reliable mixing experience.

This release improves, among other things, some details with looping, allows playing tracks exceeding 6 hours and fixes rare crashes in exceptional situations.

You can download the new version from https://mixxx.org/download/ There, you will also find the 2.4&nbsp;beta to test the new features that will be released soon.

Here is the full changelog of Mixxx 2.3.6 for more details:

* Fixed possible crash when closing Mixxx while browsing the file system
  [#11593](https://github.com/mixxxdj/mixxx/pull/11593)
  [#11589](https://github.com/mixxxdj/mixxx/issues/11589)
* No longer stop a track with an active loop at the very end
  [#11558](https://github.com/mixxxdj/mixxx/pull/11558)
  [#11557](https://github.com/mixxxdj/mixxx/issues/11557)
* Fixed resyncing when moving an active loop
  [#11152](https://github.com/mixxxdj/mixxx/pull/11152)
  [#11381](https://github.com/mixxxdj/mixxx/issues/11381)
* Allow true gapless playback when repeating full tracks
  [#11532](https://github.com/mixxxdj/mixxx/pull/11532)
  [#9842](https://github.com/mixxxdj/mixxx/issues/9842)
  [#11704](https://github.com/mixxxdj/mixxx/pull/11704)
* Rhythmbox: Fixed bulk track imports from playlists
  [#11661](https://github.com/mixxxdj/mixxx/pull/11661)
* Console log spam reduced
  [#11690](https://github.com/mixxxdj/mixxx/pull/11690)
  [#11691](https://github.com/mixxxdj/mixxx/issues/11691)
* Numark DJ2GO2 Touch: Add missing loop_out mapping for the right deck
  [#11595](https://github.com/mixxxdj/mixxx/pull/11595)
  [#11659](https://github.com/mixxxdj/mixxx/pull/11659)
* Shade: Fixed VU-Meter and other minor issues
  [#11598](https://github.com/mixxxdj/mixxx/pull/11598)
* Fixed a rare crash when disabling quantize form a controller
  [#11744](https://github.com/mixxxdj/mixxx/pull/11744)
  [#11709](https://github.com/mixxxdj/mixxx/issues/11709)
* Controller Preferences: Avoid scrollbars in I/O tabs if Info tab exceeds page height
  [#11756](https://github.com/mixxxdj/mixxx/pull/11756)
* Broadcast: Improved error message in case of timeout
  [#11775](https://github.com/mixxxdj/mixxx/pull/11775)
* Handle setting `loop_in` and `loop_out` to the same position
  [#11771](https://github.com/mixxxdj/mixxx/pull/11771)
  [#10600](https://github.com/mixxxdj/mixxx/issues/10600)
* Fix build issues with Protobuf v23.4 and with clang 32
  [#11751](https://github.com/mixxxdj/mixxx/pull/11751)
  [#11765](https://github.com/mixxxdj/mixxx/pull/11765)
  [#11762](https://github.com/mixxxdj/mixxx/issues/11762)
* Disable GL VU-Meters on Windows by default. They can be re-enabled via the command line option `--enableVuMeterGL`.
  [#11787](https://github.com/mixxxdj/mixxx/pull/11787)
  [#11785](https://github.com/mixxxdj/mixxx/issues/11785)
  [#11789](https://github.com/mixxxdj/mixxx/issues/11789)
* Library preferences: Uncheck Serato metadata export when file metadata export is unchecked
  [#11782](https://github.com/mixxxdj/mixxx/pull/11782)
  [#11226](https://github.com/mixxxdj/mixxx/issues/11226)
* Denon MC6000MK2: Delete mapping for master gain
  [#11792](https://github.com/mixxxdj/mixxx/pull/11792)
* Improve output in case of some failed file system operations
  [#11783](https://github.com/mixxxdj/mixxx/pull/11783)
* Fix overlapping buffers when decoding M4A files using FFmpeg before 4.4
  [#11760](https://github.com/mixxxdj/mixxx/pull/11760)
  [#11545](https://github.com/mixxxdj/mixxx/issues/11545)
* Don't reject key values from file metadata with non-minor/-major scales.
  [#11001](https://github.com/mixxxdj/mixxx/pull/11001)
  [#10995](https://github.com/mixxxdj/mixxx/issues/10995)
* Allow playing tracks with durations of more than 6 h
  [#11511](https://github.com/mixxxdj/mixxx/pull/11511)
  [#10995](https://github.com/mixxxdj/mixxx/issues/10995)
* Soundtouch latency compensation updated for version 2.1.1 to 2.3
  [#11154](https://github.com/mixxxdj/mixxx/pull/11154)
