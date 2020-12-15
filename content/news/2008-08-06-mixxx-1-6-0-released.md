title: Mixxx 1.6.0 Released!
authors: Albert Santoni
date: 2008-08-06 11:00:00
tags: 1.6, 1.6.0, release announcement
comments: no

The Mixxx team is proud to announce the final release of **Mixxx 1.6.0** !


[![Mixxx 1.6.0]({static}/images/news/mixxx160site.png)]({filename}/pages/index.md)

Mixxx 1.6.0 represents over a year's worth of hard work from our growing development team. The development of 1.6.0 was been driven by continuous feedback from our users, the bulk of which began in May 2007 with our popular user survey. Since then, we've taken the features that people wanted the most and focused every effort on developing them.  Needless to say, 1.6.0 is light-years ahead of 1.5.0, and our community's continued appreciation for Mixxx has served as a strong motivator for us throughout its development.

We've also [relaunched our website](http://www.mixxx.org/) with a fresh coat of paint. Clicking the thumbnail above will take you to the new site.

**Mixxx 1.6.0 is now available on our [downloads page]({filename}/pages/download.md).**

We'd like to thank both [Hercules](http://www.hercules.com/) and [Echo Audio](http://www.echoaudio.com/) for supporting Mixxx's development.
Hercules' MK2 and RMX controllers are excellent, and Echo makes fantastic professional-grade soundcards (and we mean it).

If you'd like to come hang out with some of the Mixxx developers and fellow users, we're having a [meetup at the Linuxcaffe in Toronto]({filename}/news/2008-08-02-mixxx-meetup-friday-august-8th-2008-7pm-linux-caffe-toronto.md) on Friday, August 8th from 7 PM to 11 ish.
Come check it out!

Before getting to the changelog, I'd like to mention one thing - A big change we've made is that Mixxx 1.6.0 is built on the [Qt 4](http://www.trolltech.com/) platform instead of Qt 3.
Porting Mixxx to Qt 4 took a massive effort from many developers, and was important to modernize Mixxx's look and feel, as well as ensure that Mixxx's codebase doesn't become obsolete.
We've made many technical improvements inside Mixxx in order to allow the project to grow well into the future.
Mixxx is now a much more mature open source project than it was a year ago, and there's no signs of us slowing down.

Since Mixxx 1.5.0 was released (March 4th, 2007), the following changes have been made:

- **New MIDI mappings** for Tascam US-428, M-Audio X-Session Pro, Evolution X-Session, FaderFox DJ2, and the M-Audio Torq Xponent, Vestax VCI-100, Akai MPD24, Behringer BCD3000 (including LEDs), Numark Total Control
- Many Hercules MK2 improvements
- Support for the Hercules DJ Console RMX
- Support for the Hercules DJ Console Mac Edition
- Slick sliding VU meter peaks - Screenshots don't do this justice (download it and check it out).
- Added the new Natt skin, from Natt from the forums.
- Completely rewritten waveform view by Russell Ryan through Google Summer of Code.
  This will provide better performance for some users.
- Some very under-the-hood improvements that should fix the odd crash-at-startup and improve performance.
- Fixed keyboard cue keys to use whatever cue behaviour is selected in the preferences.
- MP3 parsing fixes for files with cover art (fixes blips at the start of some songs)
- OGG parsing improvements, fixes some library scanning problems
- Fixed OGG playback on Intel OS X machines
- Completed drag-and-drop support in the library.
  You can now import tracks to the library by drag-and-dropping a track from outside Mixxx onto the library view.
  You can also reorder tracks in a playlist or the library.
- Option to disable the BPM detection.
- Added **BPM reading from MP3/OGG files** which have it embedded in them (ID3), one of several enhancements by Martin Sakmar
- Various accuracy improvements to the BPM detection
- Improvements to the vinyl emulation and pitch-independent time stretch sound quality
- **Wave recording support**
- **Vinyl control** with support for Serato, Traktor, and FinalScratch vinyl, as well as Serato CD.
- Added support for multiple inputs on a single soundcard for vinyl control
- Build flags are now cached automatically
- Improved flanger effect, thanks to Enry
- Configurable cue behaviour, which now defaults to **CDJ-style cueing**. (Thanks to Tom Care)
- Enabled **realtime priority** with ALSA, improves performance with Linux RT kernels.
- **FLAC support** for Linux and OS X users (much requested)
- Tons and tons of bug fixes.
- Fixed crashes due to vinyl emulation mode
- Improved compatibility with JACK (some users were experiencing choppiness)
- Players should now only pull from the play queue if in NEXT mode
- **Search functionality:**
  - Search box now selects all text when clicked (easier to make a new search now)
  - When the search box is cleared, the library view will scroll back to it's previous position.
  - Search now properly filters directories out
- Library stuff:
  - Double-clicking on a song now sends the song to the first stopped player.
  - Right-click menu cleaned up, much nicer now
  - Library directory rescans on startup when it's been modified (*doesn't work when subdirectories are modified yet*)
  - Library view now shows directories first
  - Columns in the library view are proportioned intelligently now
  - Renamed the "Playlist" menu to "Library"
  - Added "Rescan Library" menu item.
  - Can select multiple songs (hold shift) and send them to the play queue or a playlist
- Playlist support:
  - Can create, import, delete, and rename playlists
  - Added "Playlists" to library drop-down box
    - Can right-click to send a playlist to the play queue.
- Fixed some bugs in the track properties dialog, and set default values
- Fixed a soundcard channel selection bug when the second device had more channels than the first.
- Added BPM Schemes (need to make some presets still)
- Minor speed optimization
- OS X/Leopard package for Intel users!
- A few build system (dependency checking) fixes
- MIDI LED control on Linux
- A few MIDI tweaks here and there
- Right-clicking on a knob/slider no longer moves with your mouse (it just centers the value)
- Using your mouse's **scroll wheel** now changes the values of sliders and knobs (this is cool for laptop users with the little scroll bar at the side of their trackpads)
- DirectSound is now the default API on Windows
- ALSA Sequencer MIDI support courtesy of Cedric Gestes
- A couple of MIDI bug fixes (knobs now center properly, thanks to Sacha Berger)
- Added support for 14-bit MIDI pitch wheel controllers (thanks to Adam Sugerman)
- Hercules support on Linux improved (jog wheels work again)
- **Big stability improvements**
- **Multiple soundcards** can now be used for output (master/headphones), in case you don't have a soundcard with 4 outputs on it.
- Adam's wicked** colour scheme support** for skins
- Can now change skins without restarting Mixxx (more hard work from Adam)
- Channel VU meters are now pre-fader
- VU meters are now much more **smooth**
- Added clipping indicators (courtesy of John Sully)
- **Higher quality EQs** and other sound quality improvements (also from John Sully)
- **Adjustable EQ shelves**
- New MIDI mapping format now in XML, supports controlling LEDs
- Better Hercules support on Windows and Linux
- **New BPM detection algorithm** (Micah Lee/GSoC 2007)
- **New media library** (Nathan Prado/GSoC 2007)
- LADSPA effects support (not yet enabled - Pawel Bartkiewicz/GSoC 2007)
- BPM Tap tempo
- Ported to** Qt 4**
- Moved build system to **SCONS**
- Redesigned preferences dialogs
- **Rewritten audio core** (Albert)
- **Vinyl control** support for **Serato**, Traktor Scratch, and FinalScratch (FS needs work, but the others are good)
- Software preamp for vinyl control (can use turntables without a preamp)
- Track info editor (double-click in library)
- New library browse mode (CTAF)
- Starts in fullscreen mode if launched with the -f flag.
- Several MP3 decoder performance and stability improvements (John Sully)
- Support for merengue
- Reorganized "File" menu
- NEXT mode now works as expected (plays the next track in the table)
- Lots of little OS X improvements
- Improved consistency of fullscreen mode
- Customizable **constant power crossfader curve**
- Slow fade and fast cut crossfader curves
- **Play queue**, for creating an on-the-fly playlist
- Revamped playlist interface, editing
- Reasonably intelligent library rescanning

Once again, Mixxx 1.6.0 can be downloaded for free from our [downloads page]({filename}/pages/download.md) .
