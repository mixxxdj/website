title: Mixxx 2.4 Release
authors: Jörg Wartenberg
status: draft
tags: release, 2.4
comments: yes



## Mixxx 2.4

Mixxx 2.4 is our next major release shipping the work of 2 years continuous development on features, code refacturing and bug fixing.

### EngineOS export
Mixxx 2.4 adds support for exporting crates, playlists and the library to Engine OS devices ( Denon and Numark standalone controllers).
This allows users to prepare their tracks on a laptop using Mixxx, export them on an USB stick and plug it to the standalone controller at your gig.

### Saved Loops
Mixxx 2.4 adds support for Saved loops
If you have already tracks with Saved Loops defined by Serato DJ, Mixxx 2.4 will automatically read them from the track metadata.


### Effects
Mixxx 2.4 introduces Effect Chains, a set of effects with parameters which can be saved and loaded with all it's parameters. Mixxx 2.4 visualizes these effect parameter by value, unit and knob position.

### Sync
Mixxx 2.4 adds support for setting an explicit leader for sync. Only one deck can be the sync leader, this is set and indicated by the new crown symbol button.
This mode is useful if you work with tracks, with variable BPM.

### Track Menu
The track menu in Mixxx 2.4 is extended by several new features:
-An action to select loaded track in library
-An action to analyze/re-analyze with variable/constant BPM on a per-track basis
-An action for looking up track metadata at Discogs, Soundcoud and LastFM
-An action to remove track files from disk

### Many other changes

#### Soundstrecher / Key-Shift-Algorithms
Mixxx 2.4 supports now 3 alternative Key-Shift-Algorithms
- Soundtouch (Basic audio quality - high performance)
- Rubberband R2 (High audio quality - higher CPU usage)
- Rubberband R3 (HIFI audio quality - very high CPU usage)

#### Major rework of the Waveform Rendering code
Solves some long lasting performance issue, especially on macOS.

#### Native macOS ARM builds for M1/M2 Apple silicon

#### Controller Backend
ES6 based controller mapping system
HID backend rework

## Mixxx 2.4 Factsheet

Supported platforms:
- Windows7 or later on x64 processors
- macOS 10.12 or later on x64 processors
- macOS 11.0 or later on ARM processors (M1/M2 Apple silicon)
- Ubuntu Linux 20.4 or later (other Linux distributions are supported by third-parties)

Supported controllers:
- Mappings for 100 MIDI controllers included
- Mappings for 100 HID controllers included



## Media information
Test builds of Mixxx 2.4 can be found here before the final release:
https://mixxx.org/download/#beta

The manual for Mixxx 2.4 can be found here:
https://manual.mixxx.org/2.4/en/

Images for media use
High-Resolution images of the Mixxx logo can be downloaded here:
https://mixxx.org/press/logo

Full-Resolution images of the Mixxx 2.4 screenshots above can be downloaded here:
https://mixxx.org/tbd

Press contact
Feel free to contact us via:
press@mixxx.org
