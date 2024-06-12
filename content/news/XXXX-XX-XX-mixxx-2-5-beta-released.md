title: Mixxx 2.5 beta released
authors: Evelynne Veys
tags: 2.5, beta, release announcement
comments: yes
status: draft


It's springtime, and baby birds recently hatched from their eggs are looking out of their nests deciding if they are ready to fly. So too it is with Mixxx, and version 2.5 is almost ready to greet the world.
A bit late for Easter but it is a magnificent giant gift filled with smaller gifts: Mixxx 2.5 beta!
You can find the details about the new version below.

#### Appeal

Before releasing 2.5 as the next stable release, we need it to be tested thoroughly, something we can't do all on our own.
After some time looking at the same release and searching for solutions, we might overlook minor bugs or problems.  
That's why we need **YOU** to help us. The more people testing this beta and reporting eventual bugs to the [bug tracker](https://github.com/mixxxdj/mixxx/issues), the faster the beta can be promoted to stable.  
In case you're scared of messing up your neatly configured PC and losing your holy data is your Halloween nightmare, read the new wiki article [Safeguard Your Mixxx Data](https://github.com/mixxxdj/mixxx/wiki/Safeguard-your-Digital-DJ-Data).
It explains how to create a timestamped image, how to back up your data, and other tips and tricks.  
A beta release contains the solutions for problems that occurred and were notified by users who tested the alpha release.
The beta release is a general check before the new version can be released.  
The Mixxx database and settings of Mixxx 2.4.x stable are equal to those in Mixxx 2.5 beta, which means you can install the 2.5 over the 2.4 and vice versa without a problem.  
After you have successfully tested this 2.5 beta for yourself, you can continue using this version in your bedroom or even during live DJ-ing, and thus benefit from the new features.  
Please [join Mixxx](https://mixxx.org/get-involved/).
In Mixxx, we (can) trust.

#### Highlights

* In version 2.5, Mixxx moves from depending on Qt 5 to [Qt 6](https://www.qt.io/product/qt6). This will improve hardware support and will enable Mixxx to be compatible with latest operating systems and hardware. However, this upgrade necessitates the discontinuation of support for older operating systems, specifically macOS versions earlier than 11, Windows 7 and 8.1 and Ubuntu 20.04 "Focal Fossa" and older.
* Controller mapping settings can now be adjusted directly in the preferences, compared to previously where they would have to be manually edited in script files.
  Controller settings are only available for JavaScript mappings. We will remain open for mapping contributions to 2.5 which add setting definitions. An example on how to do so can be found on [this pull request for the S4 Mk3](https://github.com/mixxxdj/mixxx/pull/12995).

Here are some more highlights:

* Display the number of beats and the time until next hot-cue or loop in the waveform [#12994](https://github.com/mixxxdj/mixxx/pull/12994)
* Visualization of Slip Mode when using the RGB GLSL waveform [#13002](https://github.com/mixxxdj/mixxx/pull/13002)
* An option to hide the main window menu bar [#11526](https://github.com/mixxxdj/mixxx/pull/11526)
* A command line option `--start-autodj` to start Auto DJ immediately after Mixxx starts. [#13017](https://github.com/mixxxdj/mixxx/pull/13017)
* A beatloop anchor to set and adjust loop from either start or end [#12745](https://github.com/mixxxdj/mixxx/pull/12745)
* New effects: A Compressor [#12523](https://github.com/mixxxdj/mixxx/pull/12523) and Glitch [#11329](https://github.com/mixxxdj/mixxx/pull/11329)
* Support for Audio Unit (AU) plugins on macOS [#12112](https://github.com/mixxxdj/mixxx/pull/12112)
* Modify properties on multiple tracks at once [#12548](https://github.com/mixxxdj/mixxx/pull/12548)
* An experimental QML Skin that can be tested via the --qml command line option [#13152](https://github.com/mixxxdj/mixxx/pull/13152)


#### What's else new / changed / corrected in 2.5 beta

The full list of changes can be found in the [ChangeLog](https://github.com/mixxxdj/mixxx/blob/2.5/CHANGELOG.md)

You can download the new release from the [Download](https://mixxx.org/download/) page.
