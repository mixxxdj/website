title: Mixxx 2.4.2 Release Announcement
authors: Evelynne Veys
tags: update, 2.4.2
comments: yes
status: draft

#### Winter and Summer are coming

Contrasts.
As the leaves fall and the first snowflakes start drifting down in the North, while the southern skies start warming up
with summer sun, we are thrilled to finally release Mixxx 2.4.2! Finally because perfection can take some time. 
So we are proud to present you this release, a major bugfix-release for the 2.4 series before stepping over to a new number.
Don't be scared, development won't hibernate.

#### Testing and translating

A special thank you to everyone who takes the time to test alfa and beta versions,
to who report issues and proposes and to those who propose features and improvements.
Your feedback is invaluable.
A lot of new users and contributors have joined our community the past months,
we'd like to welcome them all, spin it up, your energy and fresh ideas have already left a mark.
Everybody can contribute to Mixxx. Did you remark an error on the website,
an incomplete subject in the manual, an error in translation?
[Contribute](https://mixxx.org/get-involved/).

#### Treasure hunt

When you dive in the code to add a feature or when you are looking for a function when want
to customize a mapping, you can discover small little snippets, real pearls, the intensive
work of someone to make a function smooth, to let a conversion work some milliseconds faster,
to offer a conversion of a value to another without having to write it all over again.
For all these little snippets, for all these forgotton pearls: thank you to all who ever contributed.

#### What's in the 2.4.2-bag?

All new and shiny: [the complete changelog 2.4.2](https://github.com/mixxxdj/mixxx/blob/2.4/CHANGELOG.md)
This new stable release can be downloaded from the [Download page](https://mixxx.org/download/).

Problems that were solved:
* Handle not supported files when dragging to waveforms and spinnies
  [#13208](https://github.com/mixxxdj/mixxx/pull/13208)
  [#13271](https://github.com/mixxxdj/mixxx/pull/13271)
  [#13275](https://github.com/mixxxdj/mixxx/pull/13275)
* Fix Sqlite 3.45 builds by using only single quotes for SQL strings
  [#13247](https://github.com/mixxxdj/mixxx/pull/13247)
  [#13257](https://github.com/mixxxdj/mixxx/pull/13257)
* LateNight: Use default colors for sampler overviews (like main decks)
  [#13274](https://github.com/mixxxdj/mixxx/pull/13274)
* Library: Allow to drop files to decks with unsupported or no file extensions
  [#13209](https://github.com/mixxxdj/mixxx/pull/13209)
  [#13204](https://github.com/mixxxdj/mixxx/issues/13204)
* Update build environment with libdjinterop 0.21.0
  [#13288](https://github.com/mixxxdj/mixxx/pull/13288)
* Move to GitHub workflow runner macos-12
  [#13296](https://github.com/mixxxdj/mixxx/pull/13296)
  [#13248](https://github.com/mixxxdj/mixxx/issues/13248)
* Recording: with empty config, save default split size immediately
  [#13304](https://github.com/mixxxdj/mixxx/pull/13304)
* Allow to drop files with supported MIME type regardless off the file extensions
  [#13209](https://github.com/mixxxdj/mixxx/pull/13209)
  [#13204](https://github.com/mixxxdj/mixxx/issues/13204)
* Add support for Ubuntu Oracular Oriole and remove Lunar Lobster
  [#13348](https://github.com/mixxxdj/mixxx/pull/13348)
* Recordbox: Fix string decoding issues
  [#13293](https://github.com/mixxxdj/mixxx/pull/13293)
  [#13291](https://github.com/mixxxdj/mixxx/issues/13291)
* Mixer preferences: Don't update EQs/QuickEffects while applying
  [#13333](https://github.com/mixxxdj/mixxx/pull/13333)
* Hardware preferences: Fix UX when applying config with missing/busy devices
  [#13312](https://github.com/mixxxdj/mixxx/pull/13312)
* Fix minor 64 bit CPU performance issue
  [#13355](https://github.com/mixxxdj/mixxx/pull/13355)
* Fix clicks at loop-out when looping into lead-in
  [#13294](https://github.com/mixxxdj/mixxx/pull/13294)
* Fix wrong pitch value on startup, caused by `components.Pot`
  [#11814](https://github.com/mixxxdj/mixxx/issues/11814)
  [#13463](https://github.com/mixxxdj/mixxx/pull/13463)
* Engine Prime: Fix build-failure
  [#13397](https://github.com/mixxxdj/mixxx/pull/13397)
* Engine Prime: Friendlier error message if export fails
  [#13524](https://github.com/mixxxdj/mixxx/pull/13524)
* macOs: Fix Keyboard shortcuts by not catching num key modifier
  [#13481](https://github.com/mixxxdj/mixxx/pull/13481)
  [#13305](https://github.com/mixxxdj/mixxx/issues/13305)
* Skins: fix time display to allow AM/PM
  [#13430](https://github.com/mixxxdj/mixxx/pull/13430)
  [#13421](https://github.com/mixxxdj/mixxx/issues/13421)
* Fix detection last sound if track does not end with silence.
  [#13545](https://github.com/mixxxdj/mixxx/pull/13545)
  [#13449](https://github.com/mixxxdj/mixxx/issues/13449)
* Remove false positive critical warning related to library columns
  [#13165](https://github.com/mixxxdj/mixxx/pull/13165)
  [#13164](https://github.com/mixxxdj/mixxx/issues/13164)
* Fix reading metadata for files with wrong extensions
  [#13218](https://github.com/mixxxdj/mixxx/pull/13218)
  [#13205](https://github.com/mixxxdj/mixxx/issues/13205)
* History: remove purged tracks, auto-remove empty playlists
  [#13579](https://github.com/mixxxdj/mixxx/pull/13579)
  [#13578](https://github.com/mixxxdj/mixxx/issues/13578)
* Synchronize AutoDJ next deck with top track in queue
  [#12909](https://github.com/mixxxdj/mixxx/pull/12909)
  [#8956](https://github.com/mixxxdj/mixxx/issues/8956)
* Playlists: Update play duration and bold state in sidebar when dragging tracks into the playlist table
  [#13591](https://github.com/mixxxdj/mixxx/pull/13591)
  [#13590](https://github.com/mixxxdj/mixxx/issues/13590)
  [#13575](https://github.com/mixxxdj/mixxx/pull/13575)
* Playlists: Keep correct track selection (# position) when sorting
  [#13103](https://github.com/mixxxdj/mixxx/pull/13103)
* Track file export: Various fixes
  [#13610](https://github.com/mixxxdj/mixxx/pull/13610)
* Controller engine: Unify/improve logging, expand error dialog's Details box
  [#13626](https://github.com/mixxxdj/mixxx/pull/13626)
* Fix quantization in the effect engine (metronome effect)
  [#13636](https://github.com/mixxxdj/mixxx/pull/13636)
  [#13733](https://github.com/mixxxdj/mixxx/pull/13733)
* Musicbrainz: Improved messages
  [#13672](https://github.com/mixxxdj/mixxx/pull/13672)
  [#13673](https://github.com/mixxxdj/mixxx/pull/13673)
* Fix ReplayGain detection in case of short tracks
  [#13680](https://github.com/mixxxdj/mixxx/pull/13680)
  [#13676](https://github.com/mixxxdj/mixxx/issues/13676)
  [#13702](https://github.com/mixxxdj/mixxx/issues/13702)
  [#13703](https://github.com/mixxxdj/mixxx/pull/13703)
* Track menu: Avoid crash and UX issues with track nullptr
  [#13685](https://github.com/mixxxdj/mixxx/pull/13685)
* Disable Properties shortcut in Computer feature views
  [#13698](https://github.com/mixxxdj/mixxx/pull/13698)
* Overview waveform: Add tooltip info about left-click dragging
  [#13739](https://github.com/mixxxdj/mixxx/pull/13739)
* Make `hotcue_focus_color_next`/`_prev` COs `ControlPushButton`s to allow direct mappings
  [#13764](https://github.com/mixxxdj/mixxx/pull/13764)
* Scaled svg cache to speed up drawing in hidpi mode
  [#13679](https://github.com/mixxxdj/mixxx/pull/13679)
* Update to libdjinterop 0.22.1 for Enigine Prime 4.0.1 support
  [#13790](https://github.com/mixxxdj/mixxx/pull/13790)
* HID: Avoid repeated error messages from hid_write()/hid_read() in case of errors
  [#13692](https://github.com/mixxxdj/mixxx/pull/13692)
  [#13660](https://github.com/mixxxdj/mixxx/issues/13660)
* Fix unnecessary painting with covers in library
  [#13715](https://github.com/mixxxdj/mixxx/pull/13715)

Controller Mappings that needed an update:
* Denon MC7000: Fix star up/down logic by only handling button down events
  [#13588](https://github.com/mixxxdj/mixxx/pull/13588)
* Korg Kaoss DJ: Update script
  [#12683](https://github.com/mixxxdj/mixxx/pull/12683)
* MIDI for light: Fix unsound timer handling
  [#13117](https://github.com/mixxxdj/mixxx/pull/13117)
* Novation Dicer: Remove flanger mapping with quickeffect toggle
  [#13196](https://github.com/mixxxdj/mixxx/pull/13196)
  [#13134](https://github.com/mixxxdj/mixxx/issues/13134)
* Novation Launchpad X: Fix detection on macOS
  [#13691](https://github.com/mixxxdj/mixxx/pull/13691)
  [#13633](https://github.com/mixxxdj/mixxx/issues/13633)
* Numark PartyMix: Fix EQ (script binding) display name
  [#13255](https://github.com/mixxxdj/mixxx/pull/13255)
* Numark Scratch: Add initial mapping
  [#4834](https://github.com/mixxxdj/mixxx/pull/4834)
  [#13375](https://github.com/mixxxdj/mixxx/pull/13375)
* Pioneer DDJ-400 and DDJ-FLX4: Remove tap beat mapping to resolve conflict with toggle quantize
  [#13815](https://github.com/mixxxdj/mixxx/pull/13815)
  [#13813](https://github.com/mixxxdj/mixxx/issues/13813)
* Reloop Beatmix 2/4: Fix eject button and jog LED being lit on track unload
  [#13601](https://github.com/mixxxdj/mixxx/pull/13601)
  [#13605](https://github.com/mixxxdj/mixxx/pull/13605)
* Reloop Mixage MK1, MK2, Controller Edition: Add initial mapping
  [#12296](https://github.com/mixxxdj/mixxx/pull/12296)
* Sony SIXAXIS: Fix mapping
  [#13319](https://github.com/mixxxdj/mixxx/pull/13319)
