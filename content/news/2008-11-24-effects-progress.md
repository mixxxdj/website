title: Effects Progress
author: Albert
date: 2008-11-24 07:05:00
comments: no

Since the 1.6.1 release, we've been hard at work integrating several new features that have been in the works for a while.

In our last user survey, many people told us that Mixxx needed some effects besides the flanger.
In response to your feedback, we had Pawel Bartkiewicz work on LADSPA integration through Google Summer of Code in 2007.
**LADSPA** is a terribly misleading acronym for "Linux Audio Developers Simple Plugin API".
As it turns out, LADSPA isn't just for Linux - it's a *cross-platform* effects plugin framework, and that made it the natural choice for us.
Pawel did great work last Summer, but it came in middle of our 1.6.0 development cycle and in order to properly integrate his work into Mixxx, several other tasks needed to be completed first.

One of these more noticeable tasks has been to create a new **tabbed view, ** where both the library and effects pane can be managed.


[![Screenshot of new Effects]({static}/images/news/Picture-1.png)]({static}/images/news/Picture-1.png)

*With the new reverb and "DJFlanger" effects, you can add some interesting flavour to your mixes.*

The screenshot above shows the effects panel inside the new tabbed view.
It also shows several of the effects that we're going to bundle, on the left.
The tabbed view will also give us a compact place to expand Mixxx's user interface in the future.

If you look at the screenshot closely, you can spot some rough edges that we're trying to fix before our next major release.
The main tasks that remain are bug fixing, polishing, and updating our distribution stuff (installers, packaging scripts, etc.).

For Windows and OS X users hoping for **VST support** , we think it should be possible via Audacity's awesome [VST enabler](http://audacityteam.org/vst/).
The VST enabler should allow us to load VST plugins, but to my knowledge, nobody's tested it yet.
The reason we can't build native VST support directly into Mixxx is because of Steinberg's restrictive license on their VST software development kit.

That's all for now!
We're going to keep hacking away at LADSPA and the rest of the new features we're working on, and hopefully we'll have something out the door before the end of the year.
