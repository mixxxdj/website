title: Mixxx 2.3.3 released
authors: Nikolaus Einhauser
tags: 2.3, 2.3.3, release announcement
comments: yes
date: 2022-06-22 00:04:51

Its that time again!  
Almost a year after [the release of 2.3.0]({filename}/news/2021-06-28-mixxx-2-3-0-released.md)
we're bringing you the next bugfix release [Mixxx 2.3.3](https://github.com/mixxxdj/mixxx/releases/tag/2.3.3).

This release features - you guessed it - various bugfixes and improvements:
But since we're not your run-off-the-mill mobile app, we'll get a bit into
detail:

A bunch of controller mappings have received various improvements,
such as the Pioneer DDJ-SB3, the NI Traktor S3, Behringer DDM4000 and Denon MC7000.
We've also addressed some long-standing bugs in our controller engine and the
Auto DJ, smoothed out the preference dialog and fixed a bunch of possibly
show-stopping bugs. 😬 😌

As usual, we recommend you update to the [newest stable version by visiting our
download page]({filename}/pages/download.md#stable)

If you are interested in the detailed CHANGELOG, here you go 😉:

## Changelog

* Pioneer DDJ-SB3: Fix controller breaking when releasing the shift button [#4659](https://github.com/mixxxdj/mixxx/pull/4659)
* Traktor S3: Push two deck switches to explicitly clone decks [#4665](https://github.com/mixxxdj/mixxx/pull/4665) [#4671](https://github.com/mixxxdj/mixxx/pull/4671) [lp:1960680](https://bugs.launchpad.net/mixxx/+bug/1960680)
* Behringer DDM4000: Improve stability and add soft-takeover for encoder knobs [#4318](https://github.com/mixxxdj/mixxx/pull/4318) [#4799](https://github.com/mixxxdj/mixxx/pull/4799)
* Denon MC7000: Fix 'inverted shift' bug in the controller mapping [#4755](https://github.com/mixxxdj/mixxx/pull/4755)
* Fix spinback and break effect in the controller engine [#4708](https://github.com/mixxxdj/mixxx/pull/4708)
* Fix scratch on first wheel touch [#4761](https://github.com/mixxxdj/mixxx/pull/4761) [lp:1800343](https://bugs.launchpad.net/mixxx/+bug/1800343)
* Preferences: Prevent controller settings being treated as changed even though they were not [#4721](https://github.com/mixxxdj/mixxx/pull/4721) [lp:1920844](https://bugs.launchpad.net/mixxx/+bug/1920844)
* Fix rare crash when closing the progress dialog [#4695](https://github.com/mixxxdj/mixxx/pull/4695)
* Prevent preferences dialog from going out of screen [#4613](https://github.com/mixxxdj/mixxx/pull/4613)
* Fix undesired jump-cuts in Auto DJ [#4693](https://github.com/mixxxdj/mixxx/pull/4693) [lp:1948975](https://bugs.launchpad.net/mixxx/+bug/1948975) [lp:1893197](https://bugs.launchpad.net/mixxx/+bug/1893197)
* Fix bug that caused Auto DJ to stop playback after some time [#4698](https://github.com/mixxxdj/mixxx/pull/4698) [lp:1893197](https://bugs.launchpad.net/mixxx/+bug/1893197) [lp:1961970](https://bugs.launchpad.net/mixxx/+bug/1961970)
* Do not reset crossfader when Auto DJ is deactivated [#4714](https://github.com/mixxxdj/mixxx/pull/4714) [lp:1965298](https://bugs.launchpad.net/bugs/1965298)
* Change the minimum Auto DJ transition time to -99 [#4768](https://github.com/mixxxdj/mixxx/pull/4768) [lp:1975552](https://bugs.launchpad.net/mixxx/+bug/1975552)
* Samplers, crates, playlists: fix storing import/export paths [#4699](https://github.com/mixxxdj/mixxx/pull/4699) [lp:1964508](https://bugs.launchpad.net/bugs/1964508)
* Library: keep hidden tracks in history [#4725](https://github.com/mixxxdj/mixxx/pull/4725)
* Broadcasting: allow multiple connections to same mount if only one is enabled [#4750](https://github.com/mixxxdj/mixxx/pull/4750) [lp:1972813](https://bugs.launchpad.net/mixxx/+bug/1972813)
* Fix a rare mouse vanish bug when controlling knobs [#4744](https://github.com/mixxxdj/mixxx/pull/4744) [lp:1130794](https://bugs.launchpad.net/mixxx/+bug/1130794) [lp:1969278](https://bugs.launchpad.net/mixxx/+bug/1969278)
* Restore keylock from configuration and fix pitch ratio rounding issue [#4756](https://github.com/mixxxdj/mixxx/pull/4756) [lp:1943180](https://bugs.launchpad.net/mixxx/+bug/1943180)
* Improve CSV export of playlists and crates and fix empty rating column [#4762](https://github.com/mixxxdj/mixxx/pull/4762)
* Fix passthrough-related crash in waveform code [#4789](https://github.com/mixxxdj/mixxx/pull/4789) [#4791](https://github.com/mixxxdj/mixxx/pull/4791) [lp:1959489](https://bugs.launchpad.net/mixxx/+bug/1959489) [lp:1977662](https://bugs.launchpad.net/mixxx/+bug/1977662)
* Passthrough: stop rendering waveforms and disable Cue/Play indicators [4793](https://github.com/mixxxdj/mixxx/pull/4793)
