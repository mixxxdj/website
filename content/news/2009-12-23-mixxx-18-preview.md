title: Mixxx 1.8 Preview
authors: Albert Santoni
date: 2009-12-23 21:56:00
comments: no

After many months of planning and development, we're finally
approaching a beta release of Mixxx 1.8. Since our last release, several
major new features have matured and are almost ready for public
testing.

[ ]{.Apple-style-span style="white-space: pre;"} Our main focus for 1.8
has been improving the library, which is a direct result of continued
feedback from our users. We're also excited to have been able to
address several other major feature requests, and we think 1.8 is a big
step in the right direction.

## Library

The brand new database-powered library is not only faster, but much more flexible as well.
The new library features include:

- Keep your library organized by sorting your tracks into **crates**.
- Need to take a break for a few minutes?
  Throw some tracks into the **Auto DJ** playlist and let Mixxx cover you.
- The new **Analyze** view lets you peek at your recently added tracks and perform batch BPM detection.
- A brand new **intelligent library scanning** algorithm is both quick and accurate at importing new tracks when you launch Mixxx.
  The library scanner is even smart enough to notice when you've moved tracks around inside your library and preserves any extra metadata you've added in Mixxx like comments and BPMs.

[![Crates in the new library]({static}/images/news/Picture-2.png)]({static}/images/news/Picture-2.png)

## Looping and Ramping Pitch Bend

A major rework of our audio engine also brings **looping** to the next release of Mixxx.
Running out of time to find that perfect next track for your mix? Lay down a loop and buy yourself more time.
Unlike the competition, Mixxx has no limitations on the length of your loop, so you can be as creative as you want to be.

Additional work on our mixing engine has lead to a new feature we call **ramping pitch bend**.
Ramping pitch bend helps you add extra smoothness to your mixes by making temporary pitch bends accelerate rather than jump suddenly.

## MIDI Enhancements

A brand new MIDI backend completes the rewrite of Mixxx's MIDI code, the first part of which was included in 1.7 and enabled [innovative]({filename}/news/2009-06-19-mixxx-with-stanton-scs3d-and-scs1m.md) new features like our [MIDI scripting
engine](https://github.com/mixxxdj/mixxx/wiki/midi_scripting).
The hot new addition for 1.8 is integrated **multiple MIDI device support** .

What do we mean by integrated? Check it out:

http://www.youtube.com/v/ccOvlwXW5Fw

## AAC and iTunes Support

Mixxx 1.8 can playback DRM-free AAC/M4A files on Windows, Mac OS X, and Linux.
On Windows and OS X, Mixxx can also now see your iTunes library and let you play tracks from it without importing them.

In addition to a 1.8 beta, we're also preparing a 1.7.2 bug fix release.
This release will fix MIDI on OS X and improve stability for certain hardware configurations.

2009 has been an exciting year for Mixxx, and 2010 is shaping up to be even better.
As the year closes, we'd like to thank all of our generous contributors and supporters.
We hope you're looking forward to next year as much as we are!
