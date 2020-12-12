title: Mixxx 1.9.0 Beta1 and 1.8.2 Released!
authors: Albert Santoni
date: 2010-12-06 00:32:00
comments: no

Hot off the heels of 1.8.1, the Mixxx development team is pleased to
announce the release of **Mixxx 1.9.0 Beta1** !


[![Screenshot of Mixxx]({static}/images/news/Picture-12.png)]({static}/images/news/Picture-12.png)

[**Download Mixxx 1.9.0 Beta1 and 1.8.2**]({filename}/pages/download.md)

This public beta is intended to give (brave) Mixxx users a chance to try out some new features and help us find bugs.
We do not recommend using beta software for live performance because there will be bugs.
You can help improve Mixxx by [reporting any bugs you find](https://bugs.launchpad.net/mixxx/+filebug) .

**Important:** Mixxx 1.9.0 beta1 will upgrade your library to a new format.
This will make it incompatible with Mixxx 1.8.1.
**In order to try out Mixxx 1.9.0 beta1 you should upgrade to Mixxx 1.8.2, which we are also announcing today.**
You can switch back and forth between Mixxx 1.9.0 and Mixxx 1.8.2 with no trouble.

Among the new features in 1.9.0 Beta1 are:

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
- **HSS1394 support** (Windows, OS X)
  - Mixxx now supports firewire HSS1394 MIDI devices such as the Stanton
    SCS 1 series.
- **Improved FLAC support**
  - We're now using libFLAC directly for smoother FLAC decoding.
- **Revamped metadata parsing**
  - Integration of
    [TagLib](http://developer.kde.org/~wheeler/taglib.html) allows Mixxx
    to parse more metadata from songs, and do it more consistently.
- **Metadata writing**
  - Mixxx can now write changes in song metadata back to disk. This
    feature is off by default, and can be enabled in the Library
    preferences pane.
- **Millisecond time display**
  - The time counters in Mixxx now have an extra millisecond display.
- **Library improvements:**
  - **Played column -** The library now indicates whether a song has
    been played in the current session already, and also counts the
    total number of times the song has been played.
  - **Ratings column - 5** stars, no stars, or [anywhere in
    between](http://www.mail-archive.com/mixxx-devel@lists.sourceforge.net/msg03273.html)
    .
  - **Better search** - Search now searches in more columns, and by-term
    instead of by-phrase.
  - **Revamped iTunes integration** - A rewrite yielded a significant
    speedup of iTunes parsing.
  - **Faster library scanning -** The library scanner should perform
    much better on large libraries.
  - **Inline Editing -** double click any item in the track table to
    edit its contents.
  - **Record in MP3/Ogg -** Now your recordings can be saved in either
    MP3 or Ogg/Vorbis format.
- **New MIDI mappings:**
  - Vestax Typhoon
  - Hercules DJ Console Mk4
  - Numark MIXTRACK
  - Pioneer CDJ-350
- **Updated MIDI mappings:**
  - Hercules DJ Control MP3
  - Hercules DJ Control e2
  - Hercules DJ Control Steel
  - Vestax VCI-100
  - Reloop Digital Jockey 2
- **Tons of bug fixes and performance improvements!**

Mixxx 1.8.2 has a wide variety of bug fixes, performance improvements, and the same MIDI mapping updates that 1.9.0 beta1 has.

The Mixxx team would like to give a shout out to these up-and-coming contributors who had a huge hand in helping make 1.9.0 awesome (in alphabetical order):

- Irwin Céspedes
- Vittorio Colao
- Joseph Colosimo
- Bill Good
- Anders Gunnarson
- Tobias Rafreider
- Owen Williams

**Fundraiser**

We're making great progress on our 1.9.0 Build Server fund, but we still need your help!
This project will finance a **dedicated build server** that we will use to create nightly builds and automate our release process.
This means the development team will have way more time to focus on making Mixxx better instead of dealing with packaging.
Money raised will go to cover the cost of the server, and any leftover money will cover other ongoing expenses like web hosting, and otherwise help [keep Mixxx rocking](http://pledgie.com/campaigns/13624)!

[![Click here to lend your support to: Mixxx 1.9 Build Server Fundraiser and make a donation at www.pledgie.com!](https://www.pledgie.com/campaigns/13624.png?skin_name=chrome)](http://www.pledgie.com/campaigns/13624)

**New Ubuntu PPAs**

We've moved our official Mixxx repository for Ubuntu to a [new PPA](https://launchpad.net/~mixxx/+archive/mixxx/) to increase security.
The old repository is still online for now, but Ubuntu users will have to follow the instructions on our [downloads page](http://www.mixxx.org/download.php) (click the Ubuntu download link) to get the new versions of Mixxx we've just released.
There's also a separate [Mixxx betas PPA](https://launchpad.net/~mixxx/+archive/mixxxbetas/), for brave souls.

**Bugs**

We depend on feedback from our users to guide Mixxx's development, so please file any bugs you find in this beta release on the [Mixxx bug tracker](https://bugs.launchpad.net/mixxx).
If you don't file a bug for the beta, don't be surprised when it isn't fixed in the final version!

**Join Mixxx!**

We're always looking for new contributors who are interested in working on Mixxx.
If you're a programmer or artist and want to work with a creative, enthusiastic team, hop on our IRC channel (#mixxx on Freenode) or sign up for our [developers' mailing list](https://lists.sourceforge.net/lists/listinfo/mixxx-devel).
