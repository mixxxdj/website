title: Mixxx 1.7.0 Beta1 Released!
author: Albert
date: 2009-04-23 09:00:00
comments: no

[![Screenshot of Mixxx 1.6.2]({static}/images/news/Picture-2.png)]({static}/images/news/Picture-2.png)

The Mixxx development team is proud to announce the first beta of **Mixxx 1.7.0**.
This latest release is the culmination of six months of work by over a dozen contributors, and contains several exciting new features as well as many bug fixes.

- Some of the new changes in Mixxx 1.7.0 Beta1 that we'd like to highlight are:
- Cue points are now saved in the library for each track, with "auto-recall" cue option added to preferences.
- The default skin is now widescreen, and fits nicely on netbook sized screens.
- Stereo master VU meter added.
- ** MIDI overhaul
  - MIDI learning wizard
  - MIDI mappings table editor
  - Upgraded, faster mapping system
- **QtScript/JavaScript-based [MIDI Scripting Environment](https://github.com/mixxxdj/mixxx/wiki/midi_scripting)** - Code up complex behaviour for your MIDI controller without recompiling Mixxx!
- MIDI output now fully supported on Windows, OS X, and Linux.
- **Added full support for the [Stanton SCS.3d]({filename}/news/2009-02-09-midi-scripting-and-the-stanton-scs-3d-videos.md) on all platforms.**
- Added Mixman DM2 mappings for Linux and OS X.
- **Vinyl Control:**
  - Scratching responsiveness improved, with needle-skip prevention option added.
  - Signal quality indicators added to vinyl control preferences.
- Merged the mixxx and mixxx-data packages for Ubuntu users into a single mixxx package.
- Fixed about 40 bugs, including:
  - Browse mode no longer disappears in certain situations
  - Skin changing is now much faster
  - Tooltips now work again
  - Fixed rare instabilities caused by certain OGG and MP3 files
  - Minor improvements to the BPM detection
  - Fixed some OpenGL issues
  - Fixed a handful of obscure issues that may have prevented Mixxx from starting up on Windows
  - Play nicer with Ubuntu systems that are running PulseAudio

Aside from these more visible changes, there was significant work done on less visible parts of Mixxx.
This includes many improvements to the organization and cleanliness of our source code, as well as a lot of work on features that didn't make it into the final 1.7.0. release.
Improving the overall codebase is important for us because it makes it easier for new developers to contribute, and it was these new contributors who helped catalyze the overhaul of our MIDI system.

Back around December, we started toying around with the idea of something we called *MIDI scripting*.
The idea of MIDI scripting is that having a small scripting engine sitting on top of our regular MIDI mappings would allow our users to [code complex behaviour](https://github.com/mixxxdj/mixxx/wiki/midi_scripting) for their MIDI controllers using a JavaScript-like language.
Soon after this idea hatched, we realized MIDI scripting would make it much easier for us to support [new controllers]({filename}/news/2009-02-09-midi-scripting-and-the-stanton-scs-3d-videos.md) in the future, and this attracted the attention of a handful of our developers.

Because we felt that both the long-term and short-term impact of implementing MIDI scripting would be very beneficial, several of our developers decided to shift their time away from other subprojects that they were working on (like effects, the new library, and looping) in order to complete the MIDI overhaul and scripting engine.
When this work was nearing completion, we collectively felt that MIDI scripting support along with the slew of other improvements we made were significant enough to call this release 1.7.0.
We're very excited about the [possibilities that scripting opens up](http://www.youtube.com/watch?v=qfkJnTqIeAw) , and we hope to see our users come up with new, cool uses for it.

We'd also like to thank [Stanton](http://www.stantondj.com/) for their support during this development cycle, which allowed us to significantly accelerate the development of our MIDI scripting functionality.
We're pleased to be the only cross-platform DJ software that fully supports the SCS.3d without the use of any extra software in the middle.

Lastly, if you encounter problems with the beta, please report them in our [bug tracker](https://bugs.launchpad.net/mixxx/+filebug) ! We hope you enjoy Mixxx 1.7.0 beta1, and we'll be working hard towards a final, stable release.
Stay tuned.

**Errata**

- The overhaul of our MIDI code included many changes to our MIDI mapping file format.
  Some of our old mappings were converted automatically by a script, but many required additional modifications by hand, which introduces the possibility of us having made errors.
  Due to the limited availability of hardware and free time within our development team, the MIDI mappings for some controllers have not been tested.
  If you have a controller that we provide a mapping for, please test it and report your results in our [controller testing matrix](https://github.com/mixxxdj/mixxx/wiki/supported_controller_test_grid).
- MIDI Pitch messages are no longer processed internally and must be mapped to a script function.
  Fortunately [`script.pitch`](https://github.com/mixxxdj/mixxx/wiki/midi_scripting#available_common_functions) can be used very easily from your script.
- M-Audio Xponent support has likely been broken.
  Support for it needs to be rewritten using scripting, but none of our developers have this device.
  (This is a great task for a user who wants to contribute to Mixxx! Come ask someone on IRC in #mixxx on Freenode about it.)
- Windows: MIDI feedback on all but the first listed controller doesn't work with more than one connected.
  It's best to disconnect/remove all (real and virtual) devices except the one you're interested in working with.
- Windows: You may need to tell Windows to send MIDI output to the correct device, especially if you hear random notes instead of see lights on your controller:
  Start → Settings → Control Panel → Classic View → Sounds and Audio Devices → Audio Tab, set "MIDI Music Playback" at the bottom to the device you're trying to use.
- The use of multiple MIDI devices simultaneously is not yet supported.
- For script developers:
  - The SelectNextTrack, SelectPrevTrack and LoadSelected controls do not work in the Browse view.
    See [bug #342120](https://bugs.launchpad.net/mixxx/+bug/342120).
  - The SelectNextTrack and SelectPrevTrack controls cause the GUI to freeze for a few seconds when you try to scroll down beyond the current page.
    See [bug #361170](https://bugs.launchpad.net/mixxx/+bug/361170).
