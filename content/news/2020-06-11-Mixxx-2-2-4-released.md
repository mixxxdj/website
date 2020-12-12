title: Mixxx 2.2.4 released
authors: Jan Holthuis
date: 2020-06-25 12:00:00
comments: no

Mixxx 2.2.4 has been released.
[Download it here]({filename}/pages/download.md#stable).

This release fixes some bugs and adds some controller mappings, but doesn't introduce any new features.
If you want to check out the new features of the upcoming 2.3 release, you can also [download and test the 2.3 beta instead]({filename}/news/2020-06-07-mixxx-2-3-beta-released.md).

#### Changelog

* Store default recording format after "Restore Defaults" lp:1857806 #2414
* Prevent infinite loop when decoding corrupt MP3 files #2417
* Add workaround for broken libshout versions #2040 #2438
* Speed up purging of tracks lp:1845837 #2393
* Prevent infinite loop when decoding corrupt MP3 files #2417
* Store default recording format after "Restore Defaults" lp:1857806 #2414
* Don't stop playback if vinyl passthrough input is configured and PASS button is pressed #2474
* Fix debug assertion for invalid crate names lp:1861431 #2477
* Fix crashes when executing actions on tracks that already disappeared from the DB #2527
* AutoDJ: Skip next track when both deck are playing lp:1399974 #2531
* Tweak scratch parameters for Mixtrack Platinum #2028
* Fix auto tempo going to infinity on Pioneer DDJ-SB2 #2559
* Fix bpm.tapButton logic and reject missed & double taps #2594
* Add controller mapping for Native Instruments Traktor Kontrol S2 MK3 #2348
* Add controller mapping for Soundless joyMIDI #2425
* Add controller mapping for Hercules DJControl Inpulse 300 #2465
* Add controller mapping for Denon MC7000 #2546
* Add controller mapping for Stanton DJC.4 #2607
* Fix broadcasting via broadcast/recording input lp:1876222 #2743
* Only apply ducking gain in manual ducking mode when talkover is enabed lp:1394968 lp:1737113 lp:1662536 #2759
