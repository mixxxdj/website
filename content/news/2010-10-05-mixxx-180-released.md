title: Mixxx 1.8.0 Released!
authors: Albert Santoni
date: 2010-10-05 07:24:00
comments: no

The Mixxx team is proud to announce the final release of **[Mixxx 1.8.0]({filename}/pages/index.md)**!

[![Screenshot of Mixxx 1.8.0](%7Bstatic%7D/images/1.8/screenshots/default-1000x580.png)](%7Bstatic%7D/images/1.8/screenshots/default-1000x580.png)

**Mixxx** is *free*, open source software for **performing live DJ mixes**.
Developed by a diverse community of DJs, Mixxx is a complete replacement for a conventional "turntables and mixer" DJ setup, and is available for **Windows, Mac OS X, and Linux**.


[!["Deere" skin](%7Bstatic%7D/images/1.8/screenshots/deere-1264x700.png)](%7Bstatic%7D/images/1.8/screenshots/deere-1264x700.png)

*"Deere" skin, new in Mixxx 1.8.0*

**Mixxx 1.8.0 is now available on our [downloads page]({filename}/pages/download.md).**

This new release includes a year's worth of contributions from over 30 developers and artists, and is our most exciting release to date.
Mixxx 1.8.0 includes much anticipated features such as looping, hot cues, support for multiple MIDI devices, and a brand new database-powered library.

Since Mixxx 1.7.2 was released, the following changes have been made:

- **Looping**
  - Loop-in, Loop-out, and Reloop/Exit buttons added to our main skins.
  - Loop point indicators on main waveforms and waveform summary displays.
- **Hot cues**
  - Most of our skins gained 4 hot cue buttons, and Mixxx now internally supports up to 32 hot cues per deck.
- **A brand new database-powered library, with:**
  - iTunes library and playlists access (Windows and Mac OS X)
  - Rhythmbox library and playlists access (Linux)
  - A brand new, faster library scanner
  - Crates!
  - A simple Auto DJ mode, which crossfades to the next track in the Auto DJ queue.
  - Analyze view, which allows you to run bulk BPM detection on your songs
  - Featured Artists bundle (Windows and Mac OS X)
  - Revamped Song Properties dialog
  - Re-arrangeable, hide-able columns
- **Tons of new artwork:**
  - New Deere, Shade, Phoney, and LateNight skins
  - Better descriptions in tooltips and snazzy new look
- **MIDI**
  - New PortMidi-based MIDI device backend, supports using [multiple devices](http://www.youtube.com/watch?v=ccOvlwXW5Fw) at once
  - Timers in the [MIDI scripting engine](https://github.com/mixxxdj/mixxx/wiki/midi_scripting)
  - **New MIDI mappings:**
    - Hercules DJ Control e2
    - DJ TechTools MIDI Fighter
    - Reloop Digital Jockey2
  - **Updated MIDI mappings:**
    - Hercules DJ Control MP3, RMX, MK2
    - [Stanton SCS.3d](https://github.com/mixxxdj/mixxx/wiki/stanton_scs.3d_mixxx_user_guide), [SCS.3m](https://github.com/mixxxdj/mixxx/wiki/stanton_scs.3m_mixxx_user_guide)
    - M-Audio Xponent
    - Behringer BCD3000
    - Vestax VCI-100
    - MixMan DM2
- **Other stuff:**
  - A massive rewrite of our internal mixing engine
  - More intelligent disk access to help optimize audio latency
  - Optimized waveform rendering at 30 fps
  - Ramping pitch-bend option, smoothly applies temporary pitch adjustment for nudging
  - Import comment tags from MP3, Ogg Vorbis, and FLAC/WAV metadata.
  - New library and preferences icons
  - Improvements to UTF-8 handling
- Over 50 bug fixes and more!

**Ubuntu Users**

We have great news for Ubuntu users: Mixxx 1.8.0 is available in **Ubuntu 10.10**  (Maverick Meerkat) directly from the Ubuntu Software Center!
We also have a PPA containing Mixxx 1.8.0 for Ubuntu 10.04 (Lucid) users, accessible from our [downloads page]({filename}/pages/download.md).

**Audio Playback Plugins**

We've also added an **audio playback plugin architecture** to Mixxx, which allows Mixxx to playback extra formats with third-party plugins.
Since audio formats like M4A/AAC are encumbered by software patents which restrict distribution and usage in certain jurisdictions, Mixxx cannot natively support them.
However, the good news is that a licensed third-party can now develop and distribute an M4A plugin for Mixxx.
We'll be posting some of our own audio plugins to the [Mixxx Add-ons](https://github.com/mixxxdj/mixxx/wiki/add-ons) wiki page in the coming weeks, so be sure to check back again soon.

**Fundraiser**

We realized in the course of packaging 1.8.0 (by hand) that since we're planning on [speeding up our release cycles](%7Bfilename%7D/news/2010-06-27-turning-mixxx-blog-into-blog.md), now might time to purchase a **dedicated build server** that will allow us to create nightly builds and automate our releases.
Money raised will go to cover the cost of the server, and any leftover money will cover other ongoing expenses like web hosting, and otherwise help [keep Mixxx rocking](http://pledgie.com/campaigns/13624)!

[![Click here to lend your support to: Mixxx 1.9 Build Server Fundraiser and make a donation at www.pledgie.com!](https://www.pledgie.com/campaigns/13624.png?skin_name=chrome)](http://www.pledgie.com/campaigns/13624)

**Bugs**

We depend on feedback from our users to guide Mixxx's development, so let us know what you think of the new release!
Also, please remember to report any bugs you discover to the [Mixxx bug tracker](https://bugs.launchpad.net/mixxx).

**Join Mixxx!**

We're always looking for new contributors who are interested in working on Mixxx.
If you're a programmer or artist and want to work with a creative, enthusiastic team, hop on our IRC channel (#mixxx on Freenode) or sign up for our [developers' mailing list](https://lists.sourceforge.net/lists/listinfo/mixxx-devel).
