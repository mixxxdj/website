title: Mixxx 2.3.5 released
authors: Nikolaus Einhauser
tags: 2.3, 2.3.5, release announcement
comments: yes
status: draft

Another bugfix release, this soon?

Yes, unfortunately it turned out that [2.3.4 introduced a couple of serious
bugs](https://github.com/mixxxdj/mixxx/issues?q=is%3Aissue+is%3Aclosed+milestone%3A2.3.5+label%3Aregression)
that required prompt action to fix in order to rectify this subpar release.

The most serious issue we fixed was a regression that caused an empty waveform
overview after loading a track. This issue has been fixed in version 2.3.5,
along with several other bug fixes and improvements.

Other notable changes include requesting microphone and line-in access
on macOS, allowing explicit selection of buffers of 2048 and 4096
frames per period in the JACK API, making the Beat FX section of the Pioneer DDJ-400
more intuitive, and fixing a visual issue with the the VU peak indicators in the
Tango skin.

Overall, version 2.3.5 aims to improve stability and performance while
addressing the issues introduced in the previous release. Users are encouraged
to update to this version as soon as possible to ensure the best possible
experience while using Mixxx.

Here is the full change log if you're interested:

* Fix empty waveform overview after loading a track (Mixxx 2.3.4 regression)
  Fixed by [#11333](https://github.com/mixxxdj/mixxx/pull/11333)
  [#11359](https://github.com/mixxxdj/mixxx/pull/11359)
  [#11344](https://github.com/mixxxdj/mixxx/issues/11344)
* Fullscreen: Fix a crash that occurs on Linux after enabling fullsceen and using menu
  shortcuts e.g. Alt-F.
  [#11328](https://github.com/mixxxdj/mixxx/pull/11328)
  [#11320](https://github.com/mixxxdj/mixxx/issues/11320)
* Fullscreen: Rebuild & reconnect menu only on desktops with global menu
  [#11350](https://github.com/mixxxdj/mixxx/pull/11350)
* macOS: Request Microphone and line-in access permission.
  [#11367](https://github.com/mixxxdj/mixxx/pull/11367)
  [#11365](https://github.com/mixxxdj/mixxx/issues/11365)
* JACK API: Allow to explicit select buffers of 2048 and 4096 frames/period. They are not
  supported by the automatic buffer setting of the used PortAudio library.
  [#11366](https://github.com/mixxxdj/mixxx/pull/11366)
  [#11341](https://github.com/mixxxdj/mixxx/issues/11341)
* Pioneer DDJ-400: Make Beat FX section more intuitive
  [#10912](https://github.com/mixxxdj/mixxx/pull/10912)
* Playlist export: Adopt new extension after changing the playlist type
  [#11332](https://github.com/mixxxdj/mixxx/pull/11332)
  [#11327](https://github.com/mixxxdj/mixxx/issues/11327)
* LateNight: brighter fx parameter buttons
  [#11397](https://github.com/mixxxdj/mixxx/pull/11397)
* Fix drift in analyzis data after exporting metadata to MP3 files with ID3v1.1 tags
  [#11168](https://github.com/mixxxdj/mixxx/pull/11168)
  [#11159](https://github.com/mixxxdj/mixxx/issues/11159)
* Fix broadcasting using Opus encoding
  [#11349](https://github.com/mixxxdj/mixxx/pull/11349)
  [#10666](https://github.com/mixxxdj/mixxx/issues/10666)
* Tango: Remove VU peak indicators from stacked layout. This fixes a visual regression in Mixxx 2.3.4.
  [#11430](https://github.com/mixxxdj/mixxx/pull/11430)
  [#11362](https://github.com/mixxxdj/mixxx/issues/11362)
