title: Beyond Mixxx 1.8
authors: Philip "Madjester" Whelan
date: 2010-12-10 03:18:00
comments: no

Mixxx 1.8 was a big step ahead, bringing new features like hot cues, looping, and a brand new library, but as we speak, **many other new features** are being developed behind the scenes.
These new features are still in the lab, so to speak, but some of them are maturing rapidly and will likely make it into a Mixxx release.
Some of them are even stable enough for the brave to start testing. Although, I wouldn't use any of them in a live performance yet... *or would I* ?

![Chemical Flasks]({static}/images/news/Chemical-Flasks.png)

Some of these features include:

- **Samplers**
- **Support for More than Two Decks**
- **External Mixer Mode**
- **Beat Detection**
- **Vinyl Control Rewrite**

Here's a brief overview of some of these new features:

## External Mixer Mode (1.9)

**Bill Good**  recently developed this feature through the [Google Summer of Code](http://code.google.com/soc/) program.
With External Mixer Mode, Mixxx will be able to output the audio from each deck through a separate audio channel.
This is a heavily requested feature, and is especially handy for vinyl control users.
Our internal audio routing code was significantly overhauled during this project, and as a result, we'll be able to add microphone input to Mixxx in the future with relative ease.

Bill has also been helping improve support for FLAC files in Mixxx.

## Support for Multiple Decks (1.10)

Since the first release of Mixxx, we've been stuck with only two channels for mixing.
Fortunately, we've been rescued by **RJ Ryan**, who has put in some long hours refactoring anything and everything he can get his hands on so that we can support more channels.
Thanks to his efforts, our development version of Mixxx can support any number of decks internally.
We're still working on modifying our user interface to support more decks, but it looks like we may rely on 4-deck variants of our skins in the short term.

## Sampler (1.10)

Built upon our support for multiple decks, a prototype sampler was developed by **Ryan Baker** through Google Summer of Code this year.
 These small miniature decks allow you to play audio samples.
For example, you will be able to add sirens, air horns and vocal samples into your mixes.
This feature still requires more work on the user interface and some under-the-hood polish, but there's been great progress made so far.

## Beat Detection (?)

This feature will use the open source audio library [aubio](http://www.aubio.org/) to detect beats.
This will allow us to do many things (in theory), including:

- Beat Smashing effects, a la Aphex Twin.
- Quantized Hotcues: your hotcues could sync up to the beat.
- Quantized Loops: automatically create precise loops with X beats.
- More precise Auto-Sync.
-
The main difference between BPM detection, which is what we have now, and *beat detection* is that each individual beat will be detected and marked and not just guessed from the BPM.
Coupled with a good grid editor and other groovy features this could make Mixxx a truly killer program for mixing and mashing songs, especially those with variable tempos.


As you can see, future versions of Mixxx have the potential to be pretty
exciting!
You can help support development of Mixxx by donating to our [build server fund](http://www.pledgie.com/campaigns/13624) or by [getting involved](https://mixxx.org/forums/viewtopic.php?f=1&t=1773) directly.
Thanks for your support!

[![Click here to lend your support to: Mixxx 1.9 Build Server Fundraiser and make a donation at www.pledgie.com!](https://www.pledgie.com/campaigns/13624.png?skin_name=chrome)](http://www.pledgie.com/campaigns/13624)
