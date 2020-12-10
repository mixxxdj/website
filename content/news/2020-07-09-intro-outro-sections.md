title: New In 2.3: Intro & Outro Cues, Silence Detection, and AutoDJ Improvements
author: Be.
date: 2020-07-09 01:00:00

Do you use hotcues to mark the points you use to mix in and out of tracks? Have you wished AutoDJ knew to mix in and out at those points?
In Mixxx 2.3, we have introduced new intro & outro cues for these purposes. You can try them now with [Mixxx 2.3 beta](/download#unstable).
These are not ordinary cue points. Unlike hotcues, and unlike intro and outro cues in other DJ software, they do not mark only one point. The intro & outro are sections and each section is defined by two points.

When analyzing a track, Mixxx detects where the first and last sounds are to make it easy to skip playing silent parts at the beginning and end of the track.
The analyzer places the intro start point at the first sound and the outro end point at the last sound. The first and last sound are determined by the first time the signal rises above -60 dBFS and the last time it goes below -60 dBFS.

![A track with the automatically placed intro start and outro end cues](/static/images/news/intro-outro/intro-start-outro-end.png){: style="max-height: 137px" }

It is up to you to decide where to place the intro end and outro start points.
Marking the whole intro and outro allows Mixxx to calculate how long each section is and show it on the overview waveform.
You can use this information to inform when you press play on the next track. AutoDJ can also use this information to line up tracks and determine how long to crossfade.

![A track with the full intro and outro marked](/static/images/news/intro-outro/intro-outro-full.png){: style="max-height: 137px" }

## Mixing With The Intro & Outro Cues

As an example, you can line up the ends of the intro & outro so the energy of the new track picks up right as the old track ends.

![Two tracks' waveforms with the end of the intro and outro aligned](/static/images/news/intro-outro/ends-aligned-waveforms.png)

If the intro and outro are both short enough to fit on the waveforms at the same time, you can simply watch the waveforms and press play when the markers align.
Otherwise, you can watch the time remaining on the old track and press play when it is equal to the length of the intro of the next track.

If the old track has a period of silence at the end, the analyzer will mark the outro end where the sound becomes too quiet to hear.
In this case, instead of watching the time remaining on the deck, hover your mouse cursor over the outro end line on the overview waveform.
Mixxx will show how much time is left until that point.
When that time equals the length of the intro, press play to precisely line up the end of the outro with the end of the intro.
If you have changed the tempo of the track, the time remaining scales to show the real time remaining at the adjusted tempo.

![Two tracks with the ends of the outro and intro aligned](/static/images/news/intro-outro/ends-aligned-decks.png)

Alternatively, you can line up the start of the intro & outro.
In this case, watch the scrolling waveform when the outro start point is coming up on the old track.
Then, press play on the new track when the old track reaches the outro start.

![Two tracks' waveforms with the starts of the outro and intro aligned](/static/images/news/intro-outro/starts-aligned-waveforms.png)

There are no firm rules to decide which method to use; it's an artistic judgement based on the musical content of each track, what the vibe of the crowd is at that moment, and what you want to do with the mix.

If you do not have the intro end and outro start points marked when loading a track, you can find and mark these in headphones before you mix in the track.
Then, seek back to the intro start to get the track ready.
If you don't have time to find the outro end point before mixing in the track, you can use the new deck cloning feature to drag and drop to a new deck, then seek ahead on the new deck and listen in headphones to mark the outro start point.
If you don't have time to do that either, you can right click on the overview waveform where you think the outro starts.
Then, look how far that is from the end of the track to compare it to the length of the intro of the next track.

![Right clicking on the overview waveform to approximate the length of the outro](/static/images/news/intro-outro/outro-right-click.png){: style="max-height: 137px;" }

Here, the outro is approximately 30 seconds long. However, the analyzer placed the outro end point before the end of the track, so the outro is actually a little bit shorter than 30 seconds. Without marking the outro start point, you would have to do some math in your head to find exactly how long the outro is.

## Intro & Outro Cues With AutoDJ

In Mixxx 2.3, these new intro & outro section cues can be used to tell AutoDJ how long to crossfade and how to align the tracks in time.
AutoDJ uses the intro & outro cues in the new "Full Intro + Outro" and "Fade At Outro Start" modes.
In both modes, instead of crossfading over an arbitrary number of seconds, AutoDJ compares the duration of the outro of the old track and the intro of the new track.
AutoDJ picks the time of the shorter section as the crossfade time.

If the outro is shorter than the intro, AutoDJ will align the start of the outro with the start of the intro in both modes.

![AutoDJ aligning the start of the intro and outro](/static/images/news/intro-outro/autodj-align-starts.png)

The two modes work differently when the outro is longer than the intro.
In the "Full Intro + Outro" mode, AutoDJ aligns the end of the intro and outro by starting the next track during the outro of the previous track.
This way, the full length of both the intro and the outro are played.
This mode is the most likely to sound good with the widest variety of tracks.
Therefore, it is the default mode.

![AutoDJ aligning the end of the intro and outro in Full Intro + Outro mode](/static/images/news/intro-outro/autodj-align-ends.png)

The "Fade At Outro Start" mode always aligns the start of the intro and outro.
When the outro is longer than the intro, AutoDJ cuts off the end of the outro.
This can be helpful if you want to prevent the energy of the mix from declining during a long outro. However, the transition may sound abrupt if the intro is short.

![AutoDJ aligning the start of the intro and outro in Fade At Outro Start mode](/static/images/news/intro-outro/autodj-fade-at-outro-start.png)

Both modes were designed so that AutoDJ sounds good fading between any pair of tracks if the intro and outro sections have been marked reasonably.
AutoDJ does not take into account the volume of each track, nor the frequency content, nor the rhythms, so it's not intended to be a replacement for a human DJ.
However, it is good enough to give a human DJ a break without a major disruption to the mix.

If you still want the old behavior of AutoDJ using a fixed number of seconds to crossfade, that is still available with the "Full Track" mode.
The new "Skip Silence" mode behaves the same way, but cuts out the silence at the beginning and end of tracks.

## Section Detection

Now that we know how useful it is to mark intro & outro sections, we are planning to take this concept further. As part of our [Google Summer of Code 2020 projects](/news/2020-05-05-mixxx-gsoc-projects-2020), our GSOC students Harshit and Cristiano will be adding downbeat, phrase, and section markers to Mixxx and extending the analyzers to detect these.
The intros & outros added in Mixxx 2.3 will become part of a timeline of sections that cover the whole track.
We will add similar tools to show the duration of each section and the time remaining until section markers so you can get more creative with the temporal alignment of tracks.

Do you have more ideas for features that would allow you to DJ in new ways?
Do you want to turn your ideas into reality?
With Mixxx, [you have the freedom](https://www.gnu.org/philosophy/free-sw.html) to do this without begging a company to do it for you.
If you want to help make Mixxx even more awesome, [get involved](/get-involved)!
