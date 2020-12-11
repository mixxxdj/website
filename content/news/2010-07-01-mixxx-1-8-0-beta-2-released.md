title: Mixxx 1.8.0 Beta 2 Released!
author: Albert
date: 2010-07-01 05:40:00
comments: no

The Mixxx team is pleased to announce the second beta of **Mixxx 1.8.0**!
This release brings a large number of bug fixes, performance improvements, and even some small new features.

[![Screenshot of Mixxx 1.8.0 beta2](%7Bstatic%7D/images/news/Screenshot-Mixxx-1.8.0-beta2.png)](%7Bstatic%7D/images/news/Screenshot-Mixxx-1.8.0-beta2.png)

**[Download Now!]({filename}/pages/download.md)**

Here's a summary of the changes in this release:

- **Library:**
  - Massive optimization of the new SQLite database-powered library, including:
    - Faster searches
    - In-memory caching layer which minimizes hard disk access
    - Faster library scanning
  - Fixed some Auto DJ bugs
  - Added tooltips to library table
  - Polished up song Properties dialog
  - Library search now looks at album names too
  - Fixed minor library rescanning bugs
  - Fixed crate and playlist creation bugs
  - Fixed drag-and-drop from network shares on Windows
  - Show iTunes playlists as sorted
- **Audio:**
  - Added plugin architecture for audio playback
  - Fixed some cueing bugs with pitch-independent time stretch
  - Improvements to vinyl emulation sound quality
  - Improved performance by optimizing hard disk access for audio decoding
  - Legacy 1.7 library importer now imports cue points
  - Faster MP3 loading
  - Improved reliability with certain MP3s and OGGs
- **MIDI:**
  - Improved scratching with the SCS.3d
  - Timers now available in MIDI scripts
- Fullscreen key changed to F11 to conform to de-facto standard.
- Tons of other bug fixes!

**Hotcues**
Since everyone's been waiting ever so patiently for this release, we decided to slip a bonus in for you.
Mixxx 1.8.0 Beta 2 adds **hotcues**, which are cue points that start playing when triggered.
These are handy for impromptu drumming and remixing because you can trigger different parts of a song quickly.
Although our default "Outline Netbook" skin doesn't yet show the hotcue positions on the main scrolling waveform display, the hotcues do show up in the smaller waveform summary.

The keyboard shortcuts for hotcues are Z, X, C, and V on Player 1, and M, <, >, and ? on Player 2.
Now go chop some beats!
(**Update:** Forgot to mention that using the Shift key in combination with the above keys clears the hot cues.)

**Audio Playback Plugins**
The new audio playback plugin framework lets you to install third-party plugins that give Mixxx the ability to playback extra audio formats.
Sometimes support for an obscure audio format is difficult to maintain or may be legally encumbered in certain jurisdictions, either of which would preventing us from supporting it.
However, third-party developers can now add support for extra audio formats to Mixxx at their own discretion.

The Mixxx Development Team will not distribute audio playback plugins that carry legal uncertainty for us.
The responsibility is solely yours to ensure that you are legally entitled to obtain and use any playback plugins provided by a third-party.

Although we don't have any official audio playback plugins available yet, we'd like to invite developers to post their plugins on the [Mixxx Add-ons wiki page](https://github.com/mixxxdj/mixxx/wiki/add-ons).

**The Road to 1.8.0**
Over the next month or so, we'll be wrapping up development of 1.8.0.
We've still got many bugs to fix (and could use your help), but we think this latest beta release is a big improvement over the previous one.
Give it a shot, and please [report any bugs you find](https://bugs.launchpad.net/mixxx/+filebug)!
Enjoy, and stay tuned for more news as we finally approach Mixxx 1.8.0.
