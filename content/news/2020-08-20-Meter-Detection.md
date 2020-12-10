title: GSoC 2020: Adding Experimental Meter Detection
author: Cristiano Lacerda
date: 2020-08-20 12:00:00

One of the parts where Mixxx is lacking is how it handles time signatures and downbeats.
Currently, Mixxx only has individual beats but has no support for detecting or displaying additional information about the rhythm.

This is going to change during this year's [Google Summer of Code (GSoC)](https://summerofcode.withgoogle.com/), because we have two students working on detecting and on displaying rhythm information.
This post focuses on the implementation of meter detection, which is a chance to put Mixxx ahead of some of its commercial competitors that just assume a 4/4 time signature for all tracks.

The meter detection code is an extension of the tempogram [as described by Peter Grosche, Meinard Muller and Frank Kurth](http://resources.mpi-inf.mpg.de/MIR/tempogramtoolbox/2010_GroscheMuellerKurth_TempogramCyclic_ICASSP.pdf) and is based on the QM Vamp plugin that implement such features.

The tempogram is an analogy to spectogram and is a two-dimensional representation of onset detection function that captures the periodicity rate of note events. There are two main methods for capturing this periodicity the fourier transform which compares the onset function with periodic signals and the auto correlation function that compares the onsets with time shifted versions of itself. It's widely accepted that the salience of tempograms are able to capture the metrical structure of the music, but it's also easy to see that not all peaks are related to metrical information. This constitutes one of the biggest challenges for extracting the meter from such representations.

It has been reported that combining both representations helps to enhance the meter relevant peaks. This is the approach followed in the meter detection code. As proposed by [Elio Quinton](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/25936/QUINTON_Elio_Final_PhD_030817.pdf?isAllowed=y&sequence=1) we call this combined tempograms the metergram.

While the metergram does indeed improve the metrical information periodicity it's still not clear and easy to distinguish the metrical peaks from other spurious saliencies. Following the ideas of Quinton we implement a musically informed peak picking algorithm based on the fact that neighbor metrical levels are related by an integer ratio. We start with out beat pulse which is computed from the QM beat tracker and then filter the integer pulses that might match the measure level considering the range of 6 to 60 beats per minute. Here we use the term beat not to refer to the beat itself but the metrical in analysis.

We then build metrical hierarchies by combining pulses that are apart by integer ratios and compute their weights by accumulating the weight of their constituent pulses and averaging them. Our chosen tempo range is usually large enough to accommodate the meter hierarchy of the accented beats inside a measure, beats per bar and phrases made of bars but this varies based on the beat pulse. By combining these pulses we are able to filter out individual pulses that do not match the metrical structure of the track.

The track [*Fuego* by Alok & Bhaskar](https://m.youtube.com/watch?v=VQ2EyU75p2o) illustrates nicely the advantage of creating metrical hierarchies, instead of just looking at the highest peak. In this straight 4 on the floor beat, but the strongest pulse has a 17 beats length. However we can correctly detect the best hierarchy as <4,8,16>. In this case though there is an ambiguity of the phrase length, which could be 2 or 4 measures. By looking at the other hierarchies we can see that the <2,4,16> is stronger than the <2,4,8> which correctly indicates the 4 bar phrase used in this track.

A second advantage of our metrical hierarchy is that it's very common for the strongest pulse of 4/4 tracks to be of length equal 2 beats, but these could be of any simple meter, again by combining the pulses we are usually able to correctly identify if a track is 4/4 or not. There are still some challenges to address. If our best hierarchy is <2,4,8> for example, how can we possibly distinguish a 2/4 track with 2 bars phrases from a 4/4 track that has its strongest pulse of 2 beats?

One idea is to use the tempo as a hint, in the same way we can reasonably assume the right BPM is the one closest to 120, as opposed to double of half, we should also be able to reasonably assume that the a measure should be close to 2 seconds.

A track that nicely illustrates this property is [*All Blues* by Miles Davis](https://youtu.be/-488UORrfJ0). It has a 6/4 meter and is around 156bpm. Our best meter hierarchy is <3,6,12> and it's strongest pulse is of 3 beats length. But a 3 beats bar would be around 1.15 seconds while the 6 beats bar is 2.3 seconds.

Finally we have a different kind of problem, that time signatures can be misleading and not always corvetely nicely in the meter hierarchy.  A 6/8 time signature for example, indicates that the measure has 6 eight beats, but it's a common practice for musicians to fit 2 dotted quarter notes, instead of 6 eights on those time signatures. For example, [Pat Menethy's *Minuano (Six eight)*](https://youtu.be/__N8fMTZa-s) is played like that. Our meter code estimates it's meter hierarchy as <2,4,8> which is wrong if we consider the time signature alone but 2 beats measure actually are correct if we consider the actual feel and meter of the song. Look how nice the 2 bar measure actually captures the six eight note onsets in this case:
![6/8 track with 2 beats per measure]({static}/images/news/PatMenethyMinuano.png)

On informal preliminary tests the meter detection code has an accuracy of around 80% which sounds nice on paper, but if we consider that probably 95% of tracks our users spins are 4/4 it still is more misleading than helpful.

Another huge limitation is that it uses a winner-takes-it-all strategy and is unable to find time signature changes or metric modulations.
Although the meter is actually estimated at around 0.26 seconds windows, the output is to noise to be followed blindly and some smart algorithm still need to be developed with we want to follow changes.

There are still issues to address and the code is still very experimental with a lot of rough edges, but can be tested at [2877](https://github.com/mixxxdj/mixxx/pull/2877).
