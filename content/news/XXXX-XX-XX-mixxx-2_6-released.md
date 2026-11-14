title: Mixxx 2.6 Released
authors: Evelynne Veys
tags: 2.6, release announcement
comments: yes
status: draft

#### Mixxx 2.6: A new stable version containing STEMS, Library upgrades and much more.

We're excited to announce Mixxx 2.6!
This release finally brings STEM-file support to Mixxx, along with a substantial set of library improvements, waveform enhancements and workflow refinements that will benefit every DJ, music lover and sound enthusiast, whether you're working with STEMS or not.
Let's go back in time for a moment:
With [Antoine's newspost about Adding Stem mixing support to Mixxx](https://mixxx.org/news/2024-08-26-stem-mixing/) and when we announced Mixxx 2.6 Beta, about 18 months ago in [Mixxx 2.6 beta Released](https://mixxx.org/news/2025-05-11-mixxx-2_6_beta-released/), we demonstrated the use of STEMS with an example that made use of text.
In that example we showed the use of 'Mute' and 'Effect', at that time we described the use of STEMS for a DJ as a game-changer.

The time between those newsposts could be easily described as a rollercoaster:

- people started exploring the use of STEMS,
- people started developing STEM-generators (tools to create STEM-containers from an original track) based on different models and architecture,
- DJs developed their own tricks and workflow with STEMS in their sets
- Mixxx-users asked for a lot of features regarding STEM-use,
- Mixxx-contributors developed a lot of features regarding representation of STEMS in waveform, controlling STEMS, controlling effects etc.
- Mixxx-beta-users reported issues, regressions etc.

We took the time to combine all requests, development and above all: have the STEM-engine profoundly tested, double tested, triple tested ...

Therefore we are very proud to present our users the first 'Official Mixxx Release' containing our STEMS-functionality and we're especially proud to do so in our 25th year of existence 🎉


#### STEMS ??

For those who need a small recap:
STEM containers hold the original track + its individual components, typically drums, bass, "other" (melody, guitar) & vocals.
Controls let you mute, solo, set the volume on individual STEMS, or apply effects to each STEM independently.
Drop the bass out while keeping vocals and drums running. Layer effects on just the melody. Deconstruct a track live in ways that simply weren't possible before.

See the example used in the Beta release:

@Video(https://www.youtube.com/watch?v=oEJuvVFSbnE)


In Mixxx 2.6, stem files load like any other track. Mixxx handles analysis automatically, detecting the individual stem streams and preparing them for playback.

- The engine has been extended to support multi-stream playback natively
- The Rubberband stretcher engine (used for adapting the rate or key of the track) is extended with multithreaded processing keeping everything in sync.
- Each deck now features controls for every stem in your track (mute, volume and quick effects).
- The waveforms display stem information in an overlapping (all stems combined) or stacked mode (a separate mini waveform for each STEM)
- Controller support for stems is growing too: a lot of Mixxx users were keen on adding Stem support to their favourite controllers. The new stem controls are also available for custom mappings through the controller preferences, so you can set up your own hardware "Your Way".


////// I'll create (a) videos:  walkthrough demonstrating the controls & waveforms & different skins & Effects and Creative Mixing


#### Library Improvements

The library got a lot of attention in this release:

- Key color coding: the Key column can now be color-coded, with customizable palettes to match your workflow. If you've been using color as a visual aid for harmonic mixing, this makes it much easier.
- Overview column: a new column shows a small waveform for each track, giving you a quick visual reference without loading anything.
- Search filters: search has become much more powerful. You can now filter by locked or constant BPM (bpm:locked and bpm:const), by directory, and use field shortcuts like t|title, a|artist, cm|comment, or y|year. The NOT operator (e.g. ``-artist:""``) has also been fixed.
- Library scanning: Scans now show a progress bar and a summary popup when complete (with an opt-out if you prefer the old behavior). You can also rescan the library on startup with the new ``--rescan-library`` command line option.
- Directory drag-and-drop: you can now drag and drop directories directly into the library.
- Playlist management: the Playlist context menu now supports "Unlock all" and "Delete all unlocked", making it easier to manage large collections.
- Column and display fixes: BPM and Bitrate column widths are restored properly, key text elides from the right, and the overview column has been refined across several iterations.


////// I'll create (a) videos demonstrating the library changes + Search Improvements + filters

#### Waveform and Visual Updates

The waveform system received significant attention:

- A new rendergraph library now powers waveform rendering, improving performance and consistency
- Minute markers appear on the horizontal waveform overview
- Slip waveform visualization is now available in Textured/High Details mode
- Waveform overview scaling can be adjusted by ReplayGain
- Markers on waveforms have improved appearance
- Scaling of scrolling waveforms is now unified across types
- The waveform combobox in preferences has been simplified and reorganized


////// I'll create (a) videos demonstrating the waveform changes (markers, scaling, settings)

#### Workflow Refinements

- Hotcue improvements: you can now swap hotcues by dragging and dropping hotcue buttons in the skin. Hotcues can be ordered by position in the track. Dropping a hotcue or the main cue button onto the Play button latches play.
- Auto-DJ: a new transition mode, "Skip Silence, Start with Xfader Centered," gives you more control over automatic mixing. There's also an option to recenter the crossfader when turning Auto-DJ off (default off), and a context menu action for enabling/disabling Auto-DJ.
- Effects: the Compressor effect has an adjusted Makeup Time constant calculation, White Noise leveling and ramp logic have been improved, and QuickEffect crackling when switching has been fixed.
- Preferences: controller preferences have been reorganized into tabs with extended device information. The Mixer preferences now show the "real" crossfader configuration applied by controller mappings. Sound Hardware preferences open with the specific I/O tab selected.


#### Controller Backend
- A screen renderer now supports controllers with displays (///// picture of NI S4 MK2)
- New beats_translate_half control moves the beatgrid a half beat
- File and color controller setting types have been added
- The MIDI Through Port can now be enabled in non-developer sessions
- Softtakeover code has been modernized
- Controller settings now include a collapsible group box and improved click event filtering
- The control picker now includes STEM controls

#### Platform and Build Updates

- Windows and macOS builds updated to Qt 6.8.3 (requires MSVC 2022)
- Flatpak packaging files added
- Ubuntu 24.04.01 LTS is now the Linux GitHub runner
- Ubuntu Jammy 22.04 retired
- Building without tests-tools is now possible
- Various build fixes for Qt 6.9 and 6.10 compatibility




As always, Mixxx is built by and for its community. This release represents countless hours of work from developers, designers, translators and testers from all around the world. Thank you to everyone for contributing, filing bug reports, testing builds!
We've got a lot of attention during the last year regarding our 25th Anniversary celebration: [get your Mixxx T-Shirts](https://shop.mixxx.org/).

Download [Mixxx 2.6](https://mixxx.org/download/) and spread the word about our Magic Mixxx Tool.

If you encounter any issues, please report them on our GitHub issue tracker. If you created something amazing with stems or just have a great mix to share: we'd love to hear (and see) about it.

#### 2.6 Changelog

The complete changelog can be found [here](https://github.com/mixxxdj/mixxx/blob/main/CHANGELOG.md).
