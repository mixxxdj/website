title: GSoC 2022 Work Product - Pitch Shift effect and Group delay handling
authors: David Chocholatý
status: draft
tags: gsoc, gsoc-2022
comments: yes

Disclaimer: *The blog post primarily serves as the documentation
for the Google Summer of Code 2022 project: "Pitch Shift effect
and Group delay handling". Thus, it contains a lot more detailed description,
than the other Mixxx blog posts.*

#### Introduction
The project implements the Pitch Shift effect for the Mixxx DJ
application. The Pitch Shift effect raises or lowers the original pitch
of an audio signal[^1]. Thanks to the long working period, the project was expanded
with the implementation of the Group Delay handling for the effect chain.

#### Motivation
Before the effect is implemented, the pitch could be changed using the deck's
rate slider separately only. This imposes significant restrictions on the ways
other effects can interact with the sound. In this project, the new Pitch Shift
effect is introduced in the built-in effects, which can be used
in the effect chain. It implements the wish
[Add a Transpose / Pitch Shift effect](
 https://github.com/mixxxdj/mixxx/issues/7389)
for the Mixxx application. The effect has to work with the effect chain API.
With that, the other extensional options can be used. Primarily, it allows
for the user to use a much wider range, than the Pitch Shifter
for the deck player. Due to the produced latency based on the pitch processing,
the production delay has to be handled for the wet/dry or wet+dry mode
to ensure that the original (dry) and processed (wet) signals overlap.

#### Background
List of terms from the field of music, sound processing
and development in general:

* Scale
    * In music theory, a scale is any set of musical notes ordered
     by fundamental frequency or pitch. The scale ordered
     by increasing pitch is an ascending scale, and a scale ordered
     by decreasing pitch is a descending scale[^2].
* Octave
    * In music, an octave is an interval between one musical pitch
     and another with double its frequency[^3].
* Interval
    * In music theory, an interval is a difference in pitch between
     two sounds. In western scales, intervals are most commonly differences
     between whole tones and semitones[^4].
* Semitone
    * A semitone is a distance in pitch between a note
     and the very next note, higher or lower. It is the smallest interval
     in most western scales[^5].
* Chromatic scale
    * A chromatic scale is a set of twelve pitches used
     in tonal music, with notes separated by the interval
     of a semitone[^6].
* Pitch
    * Pitch is a perceptual property of sounds that allows
     their ordering on a frequency-related scale. The pitch
     is the quality that makes it possible to judge sounds as "higher"
     and "lower" in the sense associated with musical melodies[^7].
* Wet and dry signals
    * Dry sound signals refer to the raw or unprocessed sounds
     that usually come from a direct recording. On the other hand,
     wet sounds refer to the processed sound/signal[^8].
* Ring buffer (circular buffer)
    * In computer science, a circular buffer or ring buffer
     is a data structure that uses a single, fixed-size buffer
     as if it were connected end-to-end. This structure lends itself
     easily to buffering data streams[^9].
* Audio buffer
    * An audio buffer holds a fixed size amount of sampled audio data.
     The audio buffer size determines the time allowed for the computer
     to process the audio data. Thus, it also determines Latency.
* Latency
    * In the audio world, “latency” is another word for “delay”[^10].
     The latency (time) of an audio system refers to the time difference
     from the moment a signal is fed into the system, to the moment it appears
     at the output[^11]. For example, audio latency is when there’s a noticeable
     delay between the sound being played and the moment it reaches
     the speakers[^10]. Depending on the application, such a delay can have various
     effects. Usually, the aim is to achieve the lowest possible latency[^11].

#### Pull requests and issues
[mixxx#4775](https://github.com/mixxxdj/mixxx/pull/4775)
- PitchShiftEffect: add independent effect

*Status: Merged*

The PR adds an independent effect to Mixxx's built-in effects.
The implementation uses the RubberBand library for changing a pitch
of an input track. The effect works in real-time mode and adheres
to the “push model” implementation. It means that the input data are offered
to the RubberBand library instead of that the library requires the amount
of input data.

---

[mixxx#4810](https://github.com/mixxxdj/mixxx/pull/4810)
- EngineEffectsDelay: effect chain delay handling

*Status: Merged*

This PR adds the structure for the group delay handling of the effect chain.
Based on that, some effects can produce latency due to their inner processing.
The latency has to be handled for the wet/dry and wet+dry modes that the dry
and wet signals overlapped. The structure for delay reporting from the effects
into the effect chain was implemented. With that, the dry signal delaying
to overlap with the wet signal was implemented too. Because it is
a critical part of the application engine performance, the tests and benchmarks
were included in the development.

In this PR, the `std::span` was newly introduced into the Mixxx app code
with the design proposal and cooperation of my Mentor. The util for working
with spans was implemented, so other developers can easily work with spans
directly from the custom Mixxx data structures. With that, the Mixxx code
is being upgraded using the C++20 standard.

---

[mixxx#4848](https://github.com/mixxxdj/mixxx/pull/4848)
- Fix EngineDelay and EngineFilterDelay modulo calculation documentation

*Status: Merged*

Based on the code changes in the `EngineEffectsDelay` and discussion
with my mentor, the explanation commentary was added to two other Mixxx
structures working on a quite similar principle.

---

[mixxx#4852](https://github.com/mixxxdj/mixxx/pull/4852)
- RingDelayBuffer: ring buffer for delay handling

*Status: Merged*

During the creation of the `EngineEffectsDelay` for the group delay handling
of the effect chain, it was suggested to create an optimized data structure
for the inner processing based on the ring buffer. This widely-known
signal processing structure was improved and optimized specifically
for the use case with handling of delay. Again, tests and benchmarks
were created for the `RingDelayBuffer` and based on benchmarks the used data
copy functions were compared.

---

[vcpkg#48](https://github.com/mixxxdj/vcpkg/pull/48)
- [rubberband] add overlaid rubberband v3

*Status: Merged*

During the coding period, the new RubberBand library release v3.0.0
was announced. Based on the implementation for adding RubberBand v2.0.2 directly
into the microsoft / vcpkg repository by the Mixxx organization admin,
the RubberBand v3.0.0 was added into the overlaid ports in the Mixxx fork
of the original repository.

---

[mixxx#4869](https://github.com/mixxxdj/mixxx/pull/4869)
- EngineFilterDelay: clamp wrong delay values

*Status: Merged*

While working on [mixxx#4810](https://github.com/mixxxdj/mixxx/pull/4810),
I encountered a bug in the `EngineFilterDelay` structure: The structure
works in a similar way but for a little different use case.
Newly the unacceptably huge delay values are clamped in the setter, so,
based on the inner calculation the structure will not produce absolutely wrong
output. The PR was merged the same day as its creation.

---

[mixxx#4898](https://github.com/mixxxdj/mixxx/pull/4898)
- PitchShiftEffect: decrease and report latency

*Status: Draft (WIP), last GSoC commit: [146f104](
 https://github.com/mixxxdj/mixxx/pull/4898/commits/146f104e0e3d544178428f12f2f0c295b4545966)*

In this draft PR was worked as another project extension. The implemented “push”
way model is extended into the “pull” model instead. The new approach decreases
the effect latency and this latency is reported in the effect chain
delay handler. This PR is still a Work In Progress. As the last work done
the latency measurements were performed for several implementations
and for different pitch settings. The measured data was plotted
for demonstration. The new implementation was accepted and the PR will be done
in the non-GSoC time as a future Mixxx contributor. With the new implementation,
the Mixxx circular buffer data structure was improved and optimized
for performance. So, it remains to finish the pull implementation by setting
the right size of the input ring buffer.  Eventually, implement the input
ring buffer size depending on the range that was set. As the last thing,
the valid delay value propagation for the effect will be finished.

---

[mixxx#4901](https://github.com/mixxxdj/mixxx/pull/4901)
- PitchShiftEffect: extend effect options

*Status: Merged*

The PR extends options of the Pitch shift effect. The Range knob is added
to the setting of the range of Pitch knob. These two knobs work similarly
to the real professional Pioneer DJM-900NX2 mixer which is widely used
in clubs for live DJ mixing. With that, the Semitones mode toggle was added
for changing the scale of the Pitch knob.  By default, this toggle is on,
and the Pitch knob works in the semitones mode. In musical terminology,
the pitch is changed based on the semitone chromatic scale. If the toggle
is off, the Pitch knob works in the continuous mode, which is also the default
in the RubberBand library. At last, the Formant preserving option was added
which works with the RubberBand library option. It preserves
the resonant frequencies (formants) of the human vocal tract
and other instruments (compensates for “chipmunk” or “growling” voices).
With the PR, the new function for the calculation of the Sign function was added
to the Mixxx util for math operations.

---

[mixxx#10827](https://github.com/mixxxdj/mixxx/pull/10827)
- Improve buffers size function const-correctness

*Status: Merged*

The PR improves Mixxx’s buffers data structures by using the C++ constant
expressions for the size function.

---

[mixxx#10832](https://github.com/mixxxdj/mixxx/issues/10832)
- EngineEffect: invalid engine parameters handed over into an effect

*Status: Open*

During the work on the Pitch shift effect, it was figured out, that the actual
parameter settings are not propagated into the effects. The maximum
possible values are used instead and based on that, some newly added effects
can work wrong, based on the invalid values for sample rate or size
of the buffer, for example.

---

[mixxx#10835](https://github.com/mixxxdj/mixxx/pull/10835)
- EngineBufferScaleRubberBand: remove unused include

*Status: Merged*

The unused include was removed from the implemented Mixxx structure.

---


[mixxx#10840](https://github.com/mixxxdj/mixxx/pull/10840)
- EngineEffectsDelay: introduce ring delay buffer

*Status: Open (WIP), last (non-failing) GSoC commit: [0c01e34](
 https://github.com/mixxxdj/mixxx/pull/10840/commits/0c01e340f43386155896f56333e608695d407677)*

The implemented optimized ring buffer data structure for delay handling is built
into the effect chain handling structure. With the use of the new
data structure, the delay handling performance is highly improved based on
the benchmark measurements. Unfortunately, the PR was not merged during
the coding period due to a failing test for the macOS CI (based on the inner
rounding problem for zero value). At the same time, Mixxx's macOS CI
started crashing during the configuration stage because of an issue
that the workflow runner has changed. For that reason, the bug fix
couldn't be tested and the PR was not merged in time.

---


[mixxx#10843](https://github.com/mixxxdj/mixxx/pull/10843)
- RingDelayBufferTest: refactor includes and span creation

*Status: Merged*

The tests for the `RingDelayBuffer` are refactored and the span creations
are deduplicated.

---

[mixxx#10858](https://github.com/mixxxdj/mixxx/pull/10858)
- PitchShiftEffect: add description comments

*Status: Merged*

Added the comments for the Pitch shift effect processing.

---

[website#279](https://github.com/mixxxdj/website/pull/279)
- content/news: add GSoC 2022 Work Product

*Status: Merged*

Adds a blog post containing the *"Work Product"* for Google Summer of Code 2022
on the Mixxx website.

---

#### Implementation

##### *Pitch shift effect*
The Pitch shift effect main algorithm is implemented
in the `PitchShiftEffect` class. The implementation uses the widely known
audio time-stretching and pitch-shifting library RubberBand.
The implementation adheres to the “push model”. That means, that
the input audio samples are offered to the RubberBand library API directly.
Instead of the main Pitch shifter for each deck player, which
has a limited range (only 7 semitones up and down in musical terms,
which means not even an octave), the independent Pitch shift effect offers
to work in the range of ± 2 octaves (± 24 semitones).
The pitch shift effect has the following options:

* Pitch knob
* Range knob
* Semitones mode
* Formant preserving

The Pitch knob changes the Pitch of the track up or down. For the default
middle position, the track pitch is unchanged. The Range knob ensures setting
the range of the Pitch knob. The Pitch knob based on the range setting can work
from zero range to 2 octaves range. These two knobs work similarly to the real
professional Pioneer DJM-900NX2 mixer which is widely used in clubs for live
DJ mixing. Then, the Semitones mode toggle was added. This option sets the scale
of the Pitch knob. The knob can work in two modes: continuous or semitones mode.
In the semitones mode, the pitch is changed based on the chromatic scale
in a musical way. Otherwise, the pitch is processed continuously working,
which is the default approach of the used RubberBand library. By default,
the semitones mode is on. As last, the Formant preserving option was added
which uses the RubberBand API same called option. It preserves
the resonant frequencies (formants) of the human vocal tract
and other instruments (compensates for “chipmunk” or “growling” voices).

Related files:

* [pitchshifteffect.cpp](
 https://github.com/mixxxdj/mixxx/blob/f3a3e04fe5a732d0a3e61b3bc2e2c3ec904a8630/src/effects/backends/builtin/pitchshifteffect.cpp)
* [pitchshifteffect.h](
 https://github.com/mixxxdj/mixxx/blob/f3a3e04fe5a732d0a3e61b3bc2e2c3ec904a8630/src/effects/backends/builtin/pitchshifteffect.h)

Screenshots:

*Pitch shift effect in the Mixxx app*
![Pitch shift effect in the Mixxx app]({static}/images/news/mixxx-pitch-shift-app.png)

*Pitch shift effect in the effect chain*
![Pitch shift effect in the effect chain]({static}/images/news/mixxx-pitch-shift-effect.png)

##### *Group delay handling*

As a project extension, the group delay handling of the effect chain
was implemented. Based on the Pitch shift effect processing,
using the RubberBand library, the effect produces some amount of latency.
Based on that, if we would like to play the original unprocessed signal
and the processed one together using the wet/dry or wet+dry mode, the two
audio signals will not overlap based on the latency. With that, the common
audio processing approach is to delay the original signal by the amount
of latency to overlap the signals. Based on the Mixxx effect chain API
(`EngineEffectChain`), the group delay latency handling was implemented
for the whole effect chain and works for the total produced latency
from the effect chain used effects. The main algorithm of the group delay
handling for the effect chain is implemented in the `EngineEffectsDelay` class.
The implemented APIs take the group delay and the input signal and return
the delayed signal using the inner data structures. For group delay changes,
it performs cross-fading to avoid unwanted clicks in the output audio signal.
The implemented API was used and built into the implementation
of the effect chain. Now, the sum of the latency reported by effects
is processed. As was mentioned, lastly, the group delay reporting
from the effects was implemented using the Mixxx API structures for effects
(`EngineEffect` and `EffectProcessor`).


Related files:

* [engineeffectsdelay.cpp](
 https://github.com/mixxxdj/mixxx/blob/f3a3e04fe5a732d0a3e61b3bc2e2c3ec904a8630/src/engine/effects/engineeffectsdelay.cpp)
* [engineeffectsdelay.h](
 https://github.com/mixxxdj/mixxx/blob/f3a3e04fe5a732d0a3e61b3bc2e2c3ec904a8630/src/engine/effects/engineeffectsdelay.h)
* [engineeffectsdelay_test.cpp](
 https://github.com/mixxxdj/mixxx/blob/f3a3e04fe5a732d0a3e61b3bc2e2c3ec904a8630/src/test/engineeffectsdelay_test.cpp)
* [effectprocessor.h](
 https://github.com/mixxxdj/mixxx/blob/f3a3e04fe5a732d0a3e61b3bc2e2c3ec904a8630/src/effects/backends/effectprocessor.h)
* [engineeffect.h](
 https://github.com/mixxxdj/mixxx/blob/f3a3e04fe5a732d0a3e61b3bc2e2c3ec904a8630/src/engine/effects/engineeffect.h)
* [engineeffectchain.cpp](
 https://github.com/mixxxdj/mixxx/blob/f3a3e04fe5a732d0a3e61b3bc2e2c3ec904a8630/src/engine/effects/engineeffectchain.cpp)
* [engineeffectchain.h](
 https://github.com/mixxxdj/mixxx/blob/f3a3e04fe5a732d0a3e61b3bc2e2c3ec904a8630/src/engine/effects/engineeffectchain.h)

Based on the implementation of the `EngineEffectsDelay`, it was soon figured out,
that the custom optimized data structure for the group delay handling
should be created. A common approach for working with the audio signal stream
is to use the ring buffer data structure. However, based on the specification
of group delay handling and requirements on the buffer data structure,
the classic widely known implementation is not appropriate for use. So,
the new improved and optimized variant of the ring buffer data structure
was created specifically for the group delay handling use case.
The implementation can be found in the `RingDelayBuffer` class.

Related files:

* [ringdelaybuffer.cpp](
 https://github.com/mixxxdj/mixxx/blob/f3a3e04fe5a732d0a3e61b3bc2e2c3ec904a8630/src/util/ringdelaybuffer.cpp)
* [ringdelaybuffer.h](
 https://github.com/mixxxdj/mixxx/blob/f3a3e04fe5a732d0a3e61b3bc2e2c3ec904a8630/src/util/ringdelaybuffer.h)
* [ringdelaybuffer_test.cpp](
 https://github.com/mixxxdj/mixxx/blob/f3a3e04fe5a732d0a3e61b3bc2e2c3ec904a8630/src/test/ringdelaybuffer_test.cpp)

After the `RingDelayBuffer` was implemented, the new optimized data structure
was introduced in the `EngineEffectsDelay` for group delay handling. With that,
the performance has highly improved based on the benchmark results comparison.
The benchmarking process and results will be described in detail
in the Testing and benchmarking chapter later.

##### *Pitch shift effect improvement*

At the latest, it was started the “pull model” implementation for decreasing
the Pitch shift effect latency in the GSoC period. In the new
model implementation, the RubberBand API requires the amount of input samples
and this amount of samples is passed. The main difference between the usage
of these two implementations in the Mixxx app is, which little tradeoff
has to be done. When the “push model” implementation is used, the input
data samples have not to be prefilled between the processing
but the audio dropouts can occur. On the other hand,
the “pull model” implementation with correctly set structure sizes
avoids dropouts, but the input data samples have to be prefilled
before the processing, and a delay will be produced before the output
is produced.  To compare the differences in group delay between the “push model”
and “pull model” implementation, a measurement was made.
The results are captured in the following two graphs.

Based on the first graph, the “pull model” implementation with the size
of the circular buffer of 4096 frames produces a lower latency than
the “push model” even with the latency produced before the output data.
Simultaneously, the delay between dynamic Pitch changes is in a smaller range.

*Push and pull model group delay comparison*
![Pitch Shift effect graph - Push and pull model group delay comparison](
 {static}/images/news/pitch-shift-effect-graph-1.svg)

In the second graph, the group delay for the unchanged pitch was measured.
The differences in the measurements are, that the previous pitch values
before the unchanged pitch settings are different. With the results
of the last measurement, the “pull model” implementation is more stable
and produces a similar, almost constant delay after dynamic pitch changes
for the same pitch setting.

*Push and pull model group delay comparison for unchanged pitch*

![Pitch Shift effect graph - Push and pull model group delay comparison
for unchanged pitch]({static}/images/news/pitch-shift-effect-graph-2.svg)

The results of the measurements clearly show, that despite the “pull model”
implementation for the Pitch shift effect in the effect chain is not optimal,
it should be preferred over the “push model” implementation.

#### Testing and benchmarking
With the implementation of the `EngineEffectsDelay` for group delay handling
and the `RingDelayBuffer` as an optimized data structure for the same use case,
the tests were included with the use of the GoogleTest framework. Basically,
the common situations were tested, then extreme cases and cases
that are not allowed but have to be handled for the release builds.
On the basis that these implemented structures are critical
from the point of view of performance, with tests, the benchmarks were created
with the use of the Google Benchmark. Based on the results of benchmarks,
the used functions and algorithms were compared. After both of the mentioned
structures were implemented, tested and optimized, the `RingDelayBuffer`
was introduced in the `EngineEffectsDelay` as an inner structure
for the group delay handling. Based on the changes and use of optimized
data structure the performance has highly improved. The performance differences
are shown in the following benchmarks results taken over
from the Ubuntu GitHub CI’s results.

##### *Without RingDelayBuffer*

Run on (2 X 2593.91 MHz CPU s)  
CPU Caches:

* L1 Data 32 KiB (x2)
* L1 Instruction 32 KiB (x2)
* L2 Unified 1024 KiB (x2)
* L3 Unified 36608 KiB (x1)

Load Average: 1.39, 1.82, 1.75

| Benchmark                          | Time     | CPU      | Iterations |
|------------------------------------|----------|----------|------------|
| BM_ZeroDelay/64                    | 260 ns   | 260 ns   | 2690728    |
| BM_ZeroDelay/512                   | 2079 ns  | 2078 ns  | 336963     |
| BM_ZeroDelay/4096                  | 16616 ns | 16614 ns | 42139      |
| BM_DelaySmallerThanBufferSize/64   | 269 ns   | 269 ns   | 2600146    |
| BM_DelaySmallerThanBufferSize/512  | 2119 ns  | 2119 ns  | 330263     |
| BM_DelaySmallerThanBufferSize/4096 | 16978 ns | 16977 ns | 40822      |
| BM_DelayGreaterThanBufferSize/64   | 269 ns   | 269 ns   | 2597728    |
| BM_DelayGreaterThanBufferSize/512  | 2125 ns  | 2125 ns  | 329431     |
| BM_DelayGreaterThanBufferSize/4096 | 16979 ns | 16978 ns | 40976      |
| BM_DelayCrossfading/64             | 608 ns   | 608 ns   | 1151956    |
| BM_DelayCrossfading/512            | 4865 ns  | 4865 ns  | 143875     |
| BM_DelayCrossfading/4096           | 40081 ns | 40079 ns | 17621      |
| BM_DelayNoCrossfading/64           | 539 ns   | 539 ns   | 1298494    |
| BM_DelayNoCrossfading/512          | 4238 ns  | 4238 ns  | 165164     |
| BM_DelayNoCrossfading/4096         | 33939 ns | 33936 ns | 20622      |

##### *With RingDelayBuffer*

Run on the same system as above.

Load Average: 1.50, 1.85, 1.76


| Benchmark                           | Time    | CPU     | Iterations |
|-------------------------------------|---------|---------|------------|
| BM_ZeroDelay/64                     | 14.3 ns | 14.3 ns | 48804839   |
| BM_ZeroDelay/512                    | 84.7 ns | 84.7 ns | 8291923    |
| BM_ZeroDelay/4096                   | 510 ns  | 510 ns  | 1345199    |
| BM_DelaySmallerThanBufferSize/64    | 21.7 ns | 21.7 ns | 32209113   |
| BM_DelaySmallerThanBufferSize/512   | 108 ns  | 108 ns  | 6460461    |
| BM_DelaySmallerThanBufferSize/4096  | 1627 ns | 1627 ns | 429938     |
| BM_DelayGreaterThanBufferSize/64    | 21.9 ns | 21.9 ns | 31799348   |
| BM_DelayGreaterThanBufferSize/512   | 108 ns  | 108 ns  | 6471893    |
| BM_DelayGreaterThanBufferSize/4096  | 1625 ns | 1624 ns | 435414     |
| BM_DelayCrossfading/64              | 153 ns  | 153 ns  | 4596623    |
| BM_DelayCrossfading/512             | 841 ns  | 841 ns  | 832905     |
| BM_DelayCrossfading/4096            | 9451 ns | 9450 ns | 73944      |
| BM_DelayNoCrossfading/64            | 44.1 ns | 44.1 ns | 15865504   |
| BM_DelayNoCrossfading/512           | 209 ns  | 209 ns  | 3345740    |
| BM_DelayNoCrossfading/4096          | 3236 ns | 3235 ns | 215491     |
| BM_WriteReadWholeBufferNoDelay/64   | 714 ns  | 715 ns  | 978487     |
| BM_WriteReadWholeBufferNoDelay/512  | 796 ns  | 797 ns  | 878388     |
| BM_WriteReadWholeBufferNoDelay/4096 | 1594 ns | 1628 ns | 429600     |
| BM_WriteReadWholeBufferDelay/64     | 714 ns  | 715 ns  | 978692     |
| BM_WriteReadWholeBufferDelay/512    | 795 ns  | 796 ns  | 878389     |
| BM_WriteReadWholeBufferDelay/4096   | 1500 ns | 1528 ns | 457952     |
| BM_MemCpy/64                        | 4.68 ns | 4.68 ns | 174373476  |
| BM_MemCpy/512                       | 33.0 ns | 33.0 ns | 21221060   |
| BM_MemCpy/4096                      | 154 ns  | 154 ns  | 4535488    |
| BM_StdCpy/64                        | 4.68 ns | 4.68 ns | 152600697  |
| BM_StdCpy/512                       | 32.1 ns | 32.1 ns | 21839231   |
| BM_StdCpy/4096                      | 158 ns  | 158 ns  | 4418188    |
| BM_SampleUtilCopy/64                | 4.68 ns | 4.68 ns | 174349198  |
| BM_SampleUtilCopy/512               | 33.0 ns | 33.0 ns | 21194709   |
| BM_SampleUtilCopy/4096              | 154 ns  | 154 ns  | 4515069    |
| BM_Copy2WithGain/64                 | 8.03 ns | 8.03 ns | 87167131   |
| BM_Copy2WithGain/512                | 64.2 ns | 64.2 ns | 10889704   |
| BM_Copy2WithGain/4096               | 823 ns  | 823 ns  | 847146     |
| BM_Copy2WithRampingGain/64          | 15.6 ns | 15.6 ns | 44785697   |
| BM_Copy2WithRampingGain/512         | 116 ns  | 116 ns  | 6011618    |
| BM_Copy2WithRampingGain/4096        | 1113 ns | 1113 ns | 629003     |

#### Demo video
*The video with a couple of examples of Pitch shift effect possible usage*

@Video(https://www.youtube.com/watch?v=NTjV7s5Jb_o)

#### Challenges
Several problems arose during the coding period.
Despite the medium project size, it was needed to spend much more time
working on the project based on the issues. I think the biggest challenge
in this project was exactly the implementation of the Pitch Shift effect
using the RubberBand library. The issue occurred soon, that the effect chain
offers the effect to work only with the fixed size audio chunks. Based on that,
it is not possible to require an amount of input audio data as needed
for the RubberBand library “pull model” implementation. The SoundTouch library
for Pitch Shifting was tested too but produced results with worse
audio quality and with the same amount of delay. Based on all
the discussions, the RubberBand library has shown as the best option
for the effect, despite the issues which are associated with it. After that,
the Mixxx application did not have implemented the effects delay handler
for the effect chain, so, the implementation of this structure
was automatically needed. Based on that, the goals of the project were changed.
The original proposal contained the Pitch shift effect, and with that
as a project extension to the project requirements of the Mixxx organization,
the Auto-tune effect was proposed. After consideration, the Zulip chat survey
for other Mixxx developers and users was created to be able to vote for possible
project extensions. Based on the survey results, the project extension goal
was changed to the implementation and optimization of the group delay handling
for the effect chain to improve the performance of the Pitch Shift effect
for the wet/dry and wet+dry mode. As the last challenge, I would like to mention
the usage of the std::span from the standard library which is supported
by C++20. Because the Mixxx organization adheres to the own
[Minimum requirements policy](
 https://github.com/mixxxdj/mixxx/wiki/Minimum%20requirements%20policy)
for the Ubuntu LTS, the `EngineEffectsDelay` and `RingDelayBuffer`
could be merged after the official Ubuntu release was announced in the middle
of August due to support of C++20.

#### Future work
Concretely for the Pitch Shift effect, the effect will be improved
using the “pull model” implementation after the end of the GSoC period.
With that, the wet/dry mode will be done for the effect too.
As the next project extensions, based on the survey, the following options
or features can be added to the Pitch shift effect implementation:

* Auto-tune effect
* A piano keyboard interface
* Optimize interface for common controllers
* CPU load balancing
* Consider interaction with the main Pitch shifter
* Expose compensation delay as additional parameter for making
 funny things without extra CPU cycles

More widely, as the future work for the Mixxx application, the wider support
for the LV2 standard for effects can be implemented or better, the Carla
audio plugin host can be introduced in the Mixxx application.
It will allow users to use their favorite effects enabled via audio plugin
standards such as LADSPA, DSSI, LV2, VST2, VST3 and so on,
in the application instead of offering only the built-in effects or poor API
for the LV2 standard. After consultation with my mentor, we agreed,
that I will take on this task as a regular Mixxx contributor after the end
of GSoC.

#### Things I learned from GSoC
I don't think I can even express how much the GSoC experience has given me.
Even though I had the experience with open source in one small project,
the workflow and development for the greater organization as Mixxx
was completely different and gives me a lot. I have learned so many cool things
about audio processing, development in C++ with the best practices,
using the new C++20 standard, testing and benchmarking with the use
of Google frameworks, and improving my knowledge with git and approaches
to open source development in general. Thanks to the change
in the proposed project extension, I learned a lot about real-time audio signal
processing and about cool data structures. I had a chance to try to design
the data structure with extensions too. I am really glad about the plan change
now. I really improved my English, both, written and spoken. I think,
that it was the best experience so far for me as a developer I ever had.
It is awesome, that I can publish my work and have immediately the feedback
and proposed improvements. With that, I liked the open source development
to just how much I can learn by the awesome people and create new cool stuff.
Despite I’m a college student, this actually missed me a lot,
to just have feedback on my work which opens me the opportunities to learn.
I really felt that I’m a part of the community. I will be happy to continue
being part of the Mixxx organization and contributing to open source.

#### Conclusion
The wished new effect was implemented, and the issue which requested
this new feature was closed with the "Fix Committed" status.  All requirements
by the Mixxx organization in their project idea, on which the project proposal
was based, were met. Thanks to enough time in the GSoC Coding period was worked
on the project extension. Based on the situation and the importance of new
Mixxx features, the originally proposed extension was replanned and changed.
The new group delay handling structure was successfully implemented
and optimized with the implementation of the extended data structure.
In the GSoC Coding period, work was started to minimize the effects latency as
well as to polish the effect even more.  Unfortunately, that work could
not be finished before the GSoC deadline.

During the coding period, I lined up among the top Mixxx contributors
for the last month, with 61 commits authored, and I became
the 27th of 238 contributors for the Mixxx application, with 119 commits
in total.

*August 2022 mixxxdj/mixxx contributors*
![August 2022 mixxxdj/mixxx contributors insight](
 {static}/images/news/august-2022-contributors.png)

*Contributor summary*
![Contributor summary insight]({static}/images/news/contributor-summary.png)

#### Acknowledgements
First, I would like to many thank my mentor [@Swiftb0y](
{author}nikolaus-einhauser) for his guidance, help, reviews, and a lot of new
information and lessons he gave me during the summer. I'm just motivated
and learned a lot. I would like to thank the Mixxx organization admin
[@Daniel Schürmann]({author}daniel-schurmann) for his help, reviews
and active contributions with new ideas and improvements to my project
and pull requests. Thank you both for involving me in the Mixxx development
process and for constructive criticism which offers me learn many new things
in the past weeks. I would like to thank my summer colleague for the Mixxx
organization and friend [@Fatih Emre](https://github.com/fatihemreyildiz)
for his help and synergy on the final blog structure and chapters. Of course,
I would like to thank all Mixxx developers for welcoming me into the Mixxx
family and for their help. I would like to continue our cooperation after GSoC
end as Mixxx developers. I look forward to our future teamwork. Many thanks
to the Google Summer of Code team they made this amazing experience possible
for me.

#### Resources

* [https://bugs.launchpad.net/mixxx/+bug/1299035](
 https://bugs.launchpad.net/mixxx/+bug/1299035)
* [https://breakfastquay.com/rubberband/](
 https://breakfastquay.com/rubberband/)
* [https://kx.studio/Applications:Carla](
 https://kx.studio/Applications:Carla)
* [https://lv2plug.in/](
 https://lv2plug.in/)
* [https://github.com/google/googletest](
 https://github.com/google/googletest)
* [https://github.com/google/benchmark](
 https://github.com/google/benchmark)
* [https://support.focusrite.com/hc/en-gb/articles/115004120965-Sample-Rate-Bit-Depth-Buffer-Size-Explained](
 https://support.focusrite.com/hc/en-gb/articles/115004120965-Sample-Rate-Bit-Depth-Buffer-Size-Explained)
* [https://developer.apple.com/documentation/coreaudiotypes/audiobuffer](
 https://developer.apple.com/documentation/coreaudiotypes/audiobuffer)

[^1]: Wikipedia, Pitch shift, Modified: 6 June 2022,
Accessed 2 Sept. 2022, Retrieved from:
[https://en.wikipedia.org/wiki/Pitch_shift](
 https://en.wikipedia.org/wiki/Pitch_shift)
[^2]: Wikipedia, Scale (music), Modified: 13 July 2022,
Accessed 1 Sept. 2022, Retrieved from:
[https://en.wikipedia.org/wiki/Scale_(music)](
 https://en.wikipedia.org/wiki/Scale_(music))
[^3]: Wikipedia, Octave, Modified: 18 June 2022,
Accessed 1 Sept. 2022, Retrieved from:
[https://en.wikipedia.org/wiki/Octave](
 https://en.wikipedia.org/wiki/Octave)
[^4]: Wikipedia, Interval (music), Modified: 6 Sept. 2022,
Accessed: 1 Sept. 2022, Retrieved from:
[https://en.wikipedia.org/wiki/Interval_(music)](
 https://en.wikipedia.org/wiki/Interval_(music))
[^5]: Dan Farrant, A Guide To Semitones & Tones (Half & Whole Steps),
Modified: 25 June 2022, Accessed: 2 Sept. 2022, Retrieved from:
[https://hellomusictheory.com/learn/semitones-tones/](
 https://hellomusictheory.com/learn/semitones-tones/)
[^6]: Wikipedia, Chromatic scale, Modified: 15 March 2022,
Accessed: 1 Sept. 2022, Retrieved from:
[https://en.wikipedia.org/wiki/Chromatic_scale](
 https://en.wikipedia.org/wiki/Chromatic_scale)
[^7]: Wikipedia, Pitch (music), Modified: 6 Sept. 2022,
Accessed: 1 Sept. 2022, Retrieved from:
[https://en.wikipedia.org/wiki/Pitch_(music)](
 https://en.wikipedia.org/wiki/Pitch_(music))
[^8]: Celine, Difference Between Wet and Dry Signals or Sounds,
Modified: 22 Feb. 2012, Accessed: 3 Sept. 2022, Retrieved from:
[http://www.differencebetween.net/technology/difference-between-wet-and-dry-signals-or-sounds/](
 http://www.differencebetween.net/technology/difference-between-wet-and-dry-signals-or-sounds/)
[^9]: Wikipedia, Circular buffer, Modified: 29 Oct. 2018,
Accessed: 2 Sept. 2022, Retrieved from:
[https://en.wikipedia.org/wiki/Circular_buffer](
 https://en.wikipedia.org/wiki/Circular_buffer)
[^10]: Audio Modeling,  Grow Your Knowledge, Accessed: 3 Sept. 2022,
Retrieved from:
[https://kb.audiomodeling.com/en/c/grow-your-knowledge/d/what-is-audio-latency-how-do-i-fix-latency-issues-while-recording/](
 https://kb.audiomodeling.com/en/c/grow-your-knowledge/d/what-is-audio-latency-how-do-i-fix-latency-issues-while-recording/)
[^11]: NTi Audio, Latency in Audio Systems, Modified: 10 March 2021,
Accessed: 7 Sept. 2022, Retrieved from:
[https://www.nti-audio.com/en/news/latency-in-audio-systems](
 https://www.nti-audio.com/en/news/latency-in-audio-systems)
