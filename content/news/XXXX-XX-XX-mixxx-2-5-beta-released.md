title: Mixxx 2.5 beta released
authors: Evelynne Veys
tags: 2.5, beta, release announcement
comments: yes
status: draft

#### Dear Mixxx-ers

Funny things happen in spring, birds start nesting and lay eggs, and so did the Mixxx developers.
A bit late for Easter but it is a magnificent giant gift filled with smaller gifts: Mixxx 2.5 beta!
You can find the details about the new version below.

#### Appeal

Before releasing 2.5 as the next stable release, we need it to be tested thoroughly, something we can't do all on our own.
After some time looking at the same release and searching for solutions, we might forget minor bugs or problems.  
That's why we need **YOU** to help us. The more people testing this Beta and reporting eventual bugs to the [bug tracker](https://github.com/mixxxdj/mixxx/issues), the faster the beta can be promoted to stable.  
In case you're scared of messing up your neatly configured PC and losing your holy data is your Haloween nightmare, read the new wiki article [Safeguard Your Mixxx Data](https://github.com/mixxxdj/mixxx/wiki/Safeguard-your-Digital-DJ-Data).
It explains how to creata a timestamped image, how to back up your data and offers tips and tricks.  
A beta release contains the solutions for problems that occurred and were notified by users who tested the alpha release.
The beta release is a general check before the new version can be released.  
The Mixxx database and settings of Mixxx 2.4.x stable are equal to those in Mixxx 2.5 beta, which means you can install the 2.5 over the 2.4 and vice versa without a problem.  
After you have successfully tested this 2.5 beta for yourself, you can continue using this version in your bedroom or even during live DJ-ing, and thus benefit from the new features.  
Please [join Mixxx](https://mixxx.org/get-involved/).
In Mixxx, we (can) trust.

#### Highlights

* In version 2.5, Mixxx steps up from Qt 5 to [Qt 6](https://www.qt.io/product/qt6). This will improve hardware support, and should allow Mixxx to gain in compatibility with latest operating systems and hardware.
* There is now a GUI for adjusting custom controller mapping settings directly in the preferences, compared to previously where they would have to be edited the script file manually.
  ![Controller setting example]({static}/images/news/controller_setting.png)
  This is only supported on JavaScript mapping. Note that the 2.5 version will remain open for mapping contributions which add setting definitions. An example on how to do so can be found on [this pull request for the S4 Mk3](https://github.com/mixxxdj/mixxx/pull/12995).

Here are some more highlights:

* Display the number of beats and the time until next hot-cue or loop in the waveform [#12994](https://github.com/mixxxdj/mixxx/pull/12994)
* Visualization of Slip Mode when using the RGB GLSL waveform [#13002](https://github.com/mixxxdj/mixxx/pull/13002)
* A hideable main window menu [#11526](https://github.com/mixxxdj/mixxx/pull/11526)
* A command line option `--start-autodj` to start Auto DJ immediately after Mixxx start. [#13017](https://github.com/mixxxdj/mixxx/pull/13017)
* A beatloop anchor to set and adjust loop from either start or end [#12745](https://github.com/mixxxdj/mixxx/pull/12745)
* A Compressor [#12523](https://github.com/mixxxdj/mixxx/pull/12523) and Glitch effect [#11329](https://github.com/mixxxdj/mixxx/pull/11329)
* Support for Audio Unit (AU) plugins on macOS [#12112](https://github.com/mixxxdj/mixxx/pull/12112)
* A track property editor for multiple track at once [#12548](https://github.com/mixxxdj/mixxx/pull/12548)
* An experimental QML Skin that can be tested via the --qml command line option [#13152](https://github.com/mixxxdj/mixxx/pull/13152)


#### What's else new / changed / corrected in 2.5 beta

The full list of changes can be found in the [ChangeLog](https://github.com/mixxxdj/mixxx/blob/2.5/CHANGELOG.md)

You can download the new release from the [Download](https://mixxx.org/download/) page.
