title: Mixxx 1.9.0 Released!
authors: Albert Santoni
date: 2011-02-19 19:19:00
tags: 1.9, 1.9.0, release announcement
comments: no

The Mixxx development team is pleased to announce the release of **Mixxx 1.9.0!**


[![Mixxx 1.9]({static}/images/news/Picture-12.png)]({static}/images/news/Picture-12.png)

**[Download Mixxx 1.9.0 Now!]({filename}/pages/download.md)**
Available for Windows, Mac OS X, and Linux.

[![Mixxx on the Mac App Store]({static}/images/news/available-on-mac-app-store-mixxxblog.png)](http://itunes.apple.com/us/app/mixxx/id413756578?mt=12&ls=1)

Mixxx 1.9.0 adds **several major new features** including Shoutcast support, direct deck outputs for external mixers, and ReplayGain normalization. We've also added many enhancements to the library, a revamped default skin, and more!

Some of the new features added since our last major release are:

- **Shoutcast / Icecast support**
  - Mixxx can now broadcast over the internet (heavily requested
    feature)
- **External Mixer Support**
  - The new Sound Hardware preferences pane allows you to route each
    playback deck separately, which allows you to use Mixxx with an
    external mixer.
- **ReplayGain normalization**
  - A user from our forum worked closely with our developers to fully
    implement volume normalization, including performing the ReplayGain
    analysis for tracks which are not tagged.
- **Waveform Gain**
  - The scrolling waveforms now scale according to the channel gain for
    better visual feedback.
- **Key lock buttons**
  - Formerly known as "pitch-independent time stretch", there are now
    easily accessible key-lock buttons for each for deck.
- **Revamped default skin**
  - Since the original source material for the Outline Netbook skin was
    lost eons ago, our artist completely redid it from scratch and
    tweaked it for better visibility. The new skin has also added EQ
    kill switches.
- **HSS1394 support**  (Windows, OS X)
  - Mixxx now supports firewire HSS1394 MIDI devices such as the Stanton
    SCS.1 series.
- **Improved FLAC support**
  - We're now using libFLAC directly for smoother FLAC decoding.
- **Revamped metadata parsing**
  - Integration of [TagLib](http://developer.kde.org/~wheeler/taglib.html) allows
    Mixxx to parse more metadata from songs, and do it more consistently.
- **Metadata writing**
  - Mixxx can now write changes in song metadata back to disk. This
    feature is off by default, and can be enabled in the Library
    preferences pane.
- **Millisecond time display**
  - The time counters in Mixxx now have an extra millisecond display.
- **Library improvements:**
  - **Played column - ** The library now indicates whether a song has
    been played in the current session already, and also counts the
    total number of times the song has been played.
  - **Ratings column -** 5 stars, no stars, or [anywhere in
    between](http://www.mail-archive.com/mixxx-devel@lists.sourceforge.net/msg03273.html)
  - **Better search ** - Search now searches in more columns, and
    by-term instead of by-phrase.
  - **Revamped iTunes integration**  - A rewrite yielded a significant
    speedup of iTunes parsing.
  - **Faster library scanning - ** The library scanner should perform
    much better on large libraries.
  - **Inline Editing** -** ** Double click any item in the track table
    to edit its contents.
  - **Recording to MP3/Ogg -**  Now your recordings can be saved in
    either MP3 or Ogg/Vorbis format.
- **New MIDI mappings:**
  - Vestax Typhoon
  - Vestax Spin
  - Hercules DJ Console Mk4
  - Numark MIXTRACK
  - Pioneer CDJ-350
- **Updated MIDI mappings:**
  - Hercules DJ Control MP3
  - Hercules DJ Control e2
  - Hercules DJ Control Steel
  - Hercules MK2
  - Vestax VCI-100
  - Reloop Digital Jockey 2
  - M-Audio Xponent
- **Tons of bug fixes and performance improvements!**

The Mixxx team would like to give a shout out to these up-and-coming contributors who had a huge hand in helping make 1.9.0 awesome (in alphabetical order):

  - Irwin Céspedes
  - Vittorio Colao
  - Joseph Colosimo
  - Bill Good
  - Anders Gunnarson
  - Tobias Rafreider
  - Owen Williams

**Mac App Store**

We're excited that Mixxx 1.9 is also [now available]({filename}/news/2011-02-20-mixxx-19-now-available-in-mac-app-store.md) in the [Mac App Store](http://itunes.apple.com/us/app/mixxx/id413756578?mt=12&ls=1).
The version in the App Store comes with AAC/M4A support and is 64-bit as an extra bonus for Mac OS X users.
However, due to licensing constraints, vinyl control is not included in this version.
A version including vinyl control for Mac OS X 10.5+ Intel and PPC users is available on our [downloads page]({filename}/pages/download.md).

**Bugs and Feedback**

You can help improve Mixxx by [reporting any bugs you find](https://bugs.launchpad.net/mixxx/+filebug).
Your feedback plays a crucial role in Mixxx's development cycle, and even filing a quick bug report makes an important contribution to the project.

**Join Mixxx!**

We're always looking for new contributors who are interested in working on Mixxx.
If you're a programmer or artist and want to work with a creative, enthusiastic team, hop on our IRC channel (#mixxx on Freenode) or sign up for our [developers' mailing list](https://lists.sourceforge.net/lists/listinfo/mixxx-devel).

**Update (March 14th, 2011):**

Our 32-bit Mac OS X package has been upgraded to provide better compatibility with Mac OS X 10.5.
The new package is available on our [downloads page]({filename}/pages/download.md).
