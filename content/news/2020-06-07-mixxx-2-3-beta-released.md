title: Mixxx 2.3 beta released
author: Be.
date: 2020-06-07 01:00:00
comments: no

{% load markup %}
{% filter markdown:"extra" %}
We are proud to announce the release of Mixxx 2.3 beta, [download it!]({% url '/download.html' %}#unstable) This release brings hotcue colors & labels, Serato metadata import, Rekordbox metadata import, intro & outro cues, a revamped LateNight skin, multithreaded analysis, deck cloning, and more.

![Screenshot of a Mixxx deck with the intro and outro cues and hotcue editing menu]({static}/images/news/screenshot-2.3-beta-deck.png){: style="max-height: 275px" }

Please test it, [report bugs](https://bugs.launchpad.net/mixxx/+filebug), help [translate](https://mixxx.org/wiki/doku.php/internationalization), and [contribute controller mappings](https://mixxx.org/wiki/doku.php/contributing_mappings). If you want help make Mixxx even more awesome, introduce yourself on our [Zulip chat](https://mixxx.zulipchat.com/#narrow/stream/109123-introduce-yourself) and read the [developer documentation](https://mixxx.org/wiki/doku.php#developer_documentation).

A brief overview of the changes is below. In the coming weeks, we will be publishing a series of posts on this blog discussing the new features in more depth, so stay tuned!

## Hotcues ##
* Add hotcue colors and custom labels by right clicking hotcue buttons or right clicking hotcues on waveforms (both overview and scrolling waveforms) [#2016](https://github.com/mixxxdj/mixxx/pull/2016) [#2520](https://github.com/mixxxdj/mixxx/pull/2520) [#2238](https://github.com/mixxxdj/mixxx/pull/2238) [#2560](https://github.com/mixxxdj/mixxx/pull/2560) [#2557](https://github.com/mixxxdj/mixxx/pull/2557) [#2362](https://github.com/mixxxdj/mixxx/pull/2362)
* Mouse hover cues on overview waveform to show time remaining until the cue [#2238](https://github.com/mixxxdj/mixxx/pull/2238)

## Hotcue & Track Colors ##
* Add configurable color per track [#2470](https://github.com/mixxxdj/mixxx/pull/2470) [#2539](https://github.com/mixxxdj/mixxx/pull/2539) [#2545](https://github.com/mixxxdj/mixxx/pull/2545) [#2630](https://github.com/mixxxdj/mixxx/pull/2630) [lp:1100882](https://bugs.launchpad.net/mixxx/+bug/1100882)
* Add customizable color palettes for hotcue and track colors [#2530](https://github.com/mixxxdj/mixxx/pull/2530) [#2589](https://github.com/mixxxdj/mixxx/pull/2589)
* Add hotcue color find-and-replace tool [#2547](https://github.com/mixxxdj/mixxx/pull/2547)

## Importing From Other DJ Software ##
* Import cue points, track colors, and playlists from Serato file tags & database [#2480](https://github.com/mixxxdj/mixxx/pull/2480) [#2526](https://github.com/mixxxdj/mixxx/pull/2526) [#2499](https://github.com/mixxxdj/mixxx/pull/2499) [#2495](https://github.com/mixxxdj/mixxx/pull/2495) [#2673](https://github.com/mixxxdj/mixxx/pull/2673)
    * Note: Mixxx does not yet support multiple loops per track. We are [working on this for Mixxx 2.4](https://github.com/mixxxdj/mixxx/pull/2194). In Mixxx 2.3, if you import a track with multiple loops from Serato, Mixxx will use the first loop cue as the single loop Mixxx currently supports. The imported loops are still stored in Mixxx's database and are treated as hotcues in Mixxx 2.3. If you do not delete these hotcues, they will be usable as loops in Mixxx 2.4. Serato keeps loops and hotcues in separate lists, but Mixxx does not, so loops from Serato are imported starting as hotcue 9.
* Import cue points, track colors, and playlists from Rekordbox USB drives [#2119](https://github.com/mixxxdj/mixxx/pull/2119) [#2555](https://github.com/mixxxdj/mixxx/pull/2555) [#2543](https://github.com/mixxxdj/mixxx/pull/2543) [#2779](https://github.com/mixxxdj/mixxx/pull/2779)
    * Note: The first Rekordbox memory cue is imported for the main cue button in Mixxx and the remaining Rekordbox memory cues are imported as Mixxx hotcues, starting with the next hotcue number after the last hotcue from Rekordbox.
    * Note: Mixxx does not yet support multiple loops per track. Imported loops from Rekordbox are treated like imported loops from Serato, so refer to the note above for details.

## Intro & Outro Cues ##
* Add intro & outro range cues with automatic silence detection [#1242](https://github.com/mixxxdj/mixxx/pull/1242)
* Show duration of intro & outro ranges on overview waveform [#2089](https://github.com/mixxxdj/mixxx/pull/2089)
* Use intro & outro cues in AutoDJ transitions [#2103](https://github.com/mixxxdj/mixxx/pull/2103)

## Deck cloning ##
* Add deck cloning (also known as "instant doubles" in other DJ software) by dragging and dropping between decks [#1892](https://github.com/mixxxdj/mixxx/pull/1892)
* Clone decks by double pressing the load button on a controller (with option to disable this) [#2024](https://github.com/mixxxdj/mixxx/pull/2024) [#2042](https://github.com/mixxxdj/mixxx/pull/2042)

## Skins & GUI ##
* Aesthetically revamped LateNight skin [#2298](https://github.com/mixxxdj/mixxx/pull/2298) [#2342](https://github.com/mixxxdj/mixxx/pull/2342)
* Right click overview waveform to show time remaining until that point [#2238](https://github.com/mixxxdj/mixxx/pull/2238)
* Show track context menu when right clicking text in decks [#2612](https://github.com/mixxxdj/mixxx/pull/2612) [#2675](https://github.com/mixxxdj/mixxx/pull/2675) [#2684](https://github.com/mixxxdj/mixxx/pull/2684) [#2696](https://github.com/mixxxdj/mixxx/pull/2696)
* Add laptop battery widget to skins [#2283](https://github.com/mixxxdj/mixxx/pull/2283) [#2277](https://github.com/mixxxdj/mixxx/pull/2277) [#2250](https://github.com/mixxxdj/mixxx/pull/2250) [#2228](https://github.com/mixxxdj/mixxx/pull/2228) [#2221](https://github.com/mixxxdj/mixxx/pull/2221) [#2163](https://github.com/mixxxdj/mixxx/pull/2163) [#2160](https://github.com/mixxxdj/mixxx/pull/2160) [#2147](https://github.com/mixxxdj/mixxx/pull/2147) [#2281](https://github.com/mixxxdj/mixxx/pull/2281) [#2319](https://github.com/mixxxdj/mixxx/pull/2319) [#2287](https://github.com/mixxxdj/mixxx/pull/2287)
* Show when passthrough mode is active on overview waveforms [#2575](https://github.com/mixxxdj/mixxx/pull/2575) [#2616](https://github.com/mixxxdj/mixxx/pull/2616)

## Music Feature Analysis ##
* Multithreaded analysis for much faster batch analysis on multicore CPUs [#1624](https://github.com/mixxxdj/mixxx/pull/1624) [#2142](https://github.com/mixxxdj/mixxx/pull/2142) [lp:1641153](https://bugs.launchpad.net/mixxx/+bug/1641153)
* Fix bugs affecting key detection accuracy [#2137](https://github.com/mixxxdj/mixxx/pull/2137) [#2152](https://github.com/mixxxdj/mixxx/pull/2152) [#2112](https://github.com/mixxxdj/mixxx/pull/2112) [#2136](https://github.com/mixxxdj/mixxx/pull/2136)
    * Note: Users who have not manually corrected keys are advised to clear all keys in their library by pressing Ctrl + A in the library, right clicking, going to Reset -> Key, then reanalyzing their library. This will freeze the GUI while Mixxx clears the keys; this is a known problem that we will not be able to fix for 2.3. Wait until it is finished and you will be able to reanalyze tracks for better key detection results.
* Remove VAMP plugin support and use Queen Mary DSP library directly. vamp-plugin-sdk and vamp-hostsdk are no longer required dependencies. [#926](https://github.com/mixxxdj/mixxx/pull/926)

## Music Library ##
* Add support for searching for empty fields (for example `crate:""`) [lp:1788086](https://bugs.launchpad.net/mixxx/+bug/1788086)
* Improve synchronization of track metadata and file tags [#2406](https://github.com/mixxxdj/mixxx/pull/2406)
* Library Scanner: Improve hashing of directory contents [#2497](https://github.com/mixxxdj/mixxx/pull/2497)
* Rework of Cover Image Hashing [lp:1607097](https://bugs.launchpad.net/mixxx/+bug/1607097) [#2507](https://github.com/mixxxdj/mixxx/pull/2507) [#2508](https://github.com/mixxxdj/mixxx/pull/2508)
* MusicBrainz: Handle 301 status response [#2510](https://github.com/mixxxdj/mixxx/pull/2510)
* MusicBrainz: Add extended metadata support [lp:1581256](https://bugs.launchpad.net/mixxx/+bug/1581256) [#2522](https://github.com/mixxxdj/mixxx/pull/2522)
* TagLib: Fix detection of empty or missing file tags [lp:1865957](https://bugs.launchpad.net/mixxx/+bug/1865957) [#2535](https://github.com/mixxxdj/mixxx/pull/2535)

## Audio Codecs ##
* Add FFmpeg audio decoder, bringing support for ALAC files [#1356](https://github.com/mixxxdj/mixxx/pull/1356)
* Include LAME MP3 encoder with Mixxx now that the MP3 patent has expired [lp:1294128](https://bugs.launchpad.net/mixxx/+bug/1294128) [buildserver:#37](https://github.com/mixxxdj/buildserver/pull/37) [buildserver:9e8bcee](https://github.com/mixxxdj/buildserver/commit/9e8bcee771731920ae82f3e076d43f0fb51e5027)
* Add Opus streaming and recording support. [lp:1338413](https://bugs.launchpad.net/mixxx/+bug/1338413)
* Remove support for SoundSource plugins because the code was not well-maintained and could lead to crashes [lp:1792747](https://bugs.launchpad.net/mixxx/+bug/1792747)

## Controllers ##
* Improve workflow for configuring controller mappings and editing mappings [#2569](https://github.com/mixxxdj/mixxx/pull/2569)
* Improve error reporting from controller scripts [#2588](https://github.com/mixxxdj/mixxx/pull/2588)
* Make hotcue and track colors mappable on controllers [#2030](https://github.com/mixxxdj/mixxx/pull/2030) [#2541](https://github.com/mixxxdj/mixxx/pull/2541) [#2665](https://github.com/mixxxdj/mixxx/pull/2665) [#2520](https://github.com/mixxxdj/mixxx/pull/2520)
* Add way to change library table sorting from controllers [#2118](https://github.com/mixxxdj/mixxx/pull/2118)
* Add support for velocity sensitive sampler buttons in Components JS library [#2032](https://github.com/mixxxdj/mixxx/pull/2032)
* Add logging when script ControlObject callback is disconnected successfully [#2054](https://github.com/mixxxdj/mixxx/pull/2054)
* Add controller mapping for Roland DJ-505 [#2111](https://github.com/mixxxdj/mixxx/pull/2111)
* Update controller mapping for Allen & Heath Xone K2 to add intro/outro cues [#2236](https://github.com/mixxxdj/mixxx/pull/2236)

## Development ##
* Add CMake build system with Ccache support for faster compilation time [#2280](https://github.com/mixxxdj/mixxx/pull/2280)
    * Note: The old SCons build system is still supported for 2.3. We will be removing it for Mixxx 2.4.
* Make Mixxx compile even though `QT_NO_OPENGL` or `QT_OPENGL_ES_2` is defined (fixes build on Raspberry Pi) [lp:1863440](https://bugs.launchpad.net/mixxx/+bug/1863440) [#2504](https://github.com/mixxxdj/mixxx/pull/2504)
