title: Mixxx 1.7.0 Beta1 Released!
author: Albert
date: 2009-04-23 09:00:00
comments: no

<div style="text-align: center;"><a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="{static}/images/news/Picture-2.png"><img style="margin: 0px auto 10px; display: block; text-align: center; cursor: pointer; width: 400px; height: 241px;" src="{static}/images/news/Picture-2.png" alt="" id="BLOGGER_PHOTO_ID_5327645996858682802" border="0" />
</a>
<br />
<div style="text-align: left;">The Mixxx development team is proud to announce the first beta of <span style="font-weight: bold;">Mixxx 1.7.0</span>
. This latest release is the culmination of six months of work by over a dozen contributors, and contains several exciting new features as well as many bug fixes.<br />
<span style="font-style: italic;"></span>
</div>
</div>
<br />
Some of the new changes in Mixxx 1.7.0 Beta1 that we'd like to highlight are:<br />
<ul><li>Cue points are now saved in the library for each track, with "auto-recall" cue option added to preferences.</li>
<li>The default skin is now widescreen, and fits nicely on netbook sized screens.</li>
<li>Stereo master VU meter added.<br />
</li>
<li><span style="font-weight: bold;">MIDI overhaul</span>
:<br />
<ul><li>MIDI learning wizard</li>
<li>MIDI mappings table editor</li>
<li>Upgraded, faster mapping system<br />
</li>
</ul>
</li>
<li><span style="font-weight: bold;">QtScript/JavaScript-based <a href="https://github.com/mixxxdj/mixxx/wiki/midi_scripting">MIDI Scripting Environment</a>
</span>
 - Code up complex behaviour for your MIDI controller without recompiling Mixxx!</li>
<li>MIDI output now fully supported on Windows, OS X, and Linux.</li>
<li><span style="font-weight: bold;">Added full support for the <a href="{filename}/news/2009-02-09-midi-scripting-and-the-stanton-scs-3d-videos.md">Stanton SCS.3d</a>
 on all platforms. </span>
<br />
</li>
<li>Added Mixman DM2 mappings for Linux and OS X.</li>
<li style="font-weight: bold;">Vinyl Control:</li>
<ul><li>Scratching responsiveness improved, with needle-skip prevention option added.</li>
<li>Signal quality indicators added to vinyl control preferences.<br />
</li>
</ul>
<li>Merged the mixxx and mixxx-data packages for Ubuntu users into a single mixxx package.</li>
<li>Fixed about 40 bugs, including:</li>
<ul><li>Browse mode no longer disappears in certain situations</li>
<li>Skin changing is now much faster<br />
</li>
<li>Tooltips now work again</li>
<li>Fixed rare instabilities caused by certain OGG and MP3 files</li>
<li>Minor improvements to the BPM detection</li>
<li>Fixed some OpenGL issues</li>
<li>Fixed a handful of obscure issues that may have prevented Mixxx from starting up on Windows</li>
<li>Play nicer with Ubuntu systems that are running PulseAudio<br />
</li>
</ul>
</ul>
    Aside from these more visible changes, there was significant work done on less visible parts of Mixxx. This includes many improvements to the organization and cleanliness of our source code, as well as a lot of work on features that didn't make it into the final 1.7.0. release. Improving the overall codebase is important for us because it makes it easier for new developers to contribute, and it was these new contributors who helped catalyze the overhaul of our MIDI system.<br />
<br />
Back around December, we started toying around with the idea of something we called <span style="font-style: italic;">MIDI scripting</span>
. The idea of MIDI scripting is that having a small scripting engine sitting on top of our regular MIDI mappings would allow our users to <a href="https://github.com/mixxxdj/mixxx/wiki/midi_scripting">code complex behaviour</a>
 for their MIDI controllers using a JavaScript-like language. Soon after this idea hatched, we realized MIDI scripting would make it much easier for us to support <a href="{filename}/news/2009-02-09-midi-scripting-and-the-stanton-scs-3d-videos.md">new controllers</a>
 in the future, and this attracted the attention of a handful of our developers.<br />
<br />
Because we felt that both the long-term and short-term impact of implementing MIDI scripting would be very beneficial, several of our developers decided to shift their time away from other subprojects that they were working on (like effects, the new library, and looping) in order to complete the MIDI overhaul and scripting engine. When this work was nearing completion, we collectively felt that MIDI scripting support along with the slew of other improvements we made were significant enough to call this release 1.7.0. We're very excited about the <a href="http://www.youtube.com/watch?v=qfkJnTqIeAw">possibilities that scripting opens up</a>
, and we hope to see our users come up with new, cool uses for it.<br />
<br />
We'd also like to thank <a href="http://www.stantondj.com/">Stanton</a>
 for their support during this development cycle, which allowed us to significantly accelerate the development of our MIDI scripting functionality. We're pleased to be the only cross-platform DJ software that fully supports the SCS.3d without the use of any extra software in the middle.<br />
<br />
Lastly, if you encounter problems with the beta, please report them in our <a href="https://bugs.launchpad.net/mixxx/+filebug">bug tracker</a>
! We hope you enjoy Mixxx 1.7.0 beta1, and we'll be working hard towards a final, stable release. Stay tuned.<br />
<br />
<span style="font-weight: bold;">Errata</span>
<br />
<ul><li>The overhaul of our MIDI code included many changes to our MIDI mapping file format. Some of our old mappings were converted automatically by a script, but many required additional modifications by hand, which introduces the possibility of us having made errors. Due to the limited availability of hardware and free time within our development team, the MIDI mappings for some controllers have not been tested. If you have a controller that we provide a mapping for, please test it and report your results in our <a href="https://github.com/mixxxdj/mixxx/wiki/supported_controller_test_grid">controller testing matrix</a>
. </li>
<li>MIDI Pitch messages are no longer processed internally and must be mapped to a script function. Fortunately <a href="https://github.com/mixxxdj/mixxx/wiki/midi_scripting#available_common_functions" class="wikilink1" title="midi_scripting">script.pitch</a>
 can be used very easily from your script.</li>
<li>M-Audio Xponent support has likely been broken. Support for it needs to be rewritten using scripting, but none of our developers have this device. (This is a great task for a user who wants to contribute to Mixxx! Come ask someone on IRC in #mixxx on Freenode about it.)<br />
</li>
<li class="level1"> Windows: MIDI feedback on all but the first listed controller doesn't work with more than one connected. It's best to disconnect/remove all (real and virtual) devices except the one you're interested in working with.</li>
<li class="level1"><div class="li"> Windows: You may need to tell Windows to send MIDI output to the correct device, especially if you hear random notes instead of see lights on your controller: Start→Settings→Control Panel→Classic View→Sounds and Audio Devices→Audio Tab, set “MIDI Music Playback” at the bottom to the device you're trying to use.</div>
 </li>
<li class="level1"><div class="li"> The use of multiple MIDI devices simultaneously is not yet supported.<br />
</div>
 </li>
<li class="level1">For script developers:<br />
</li>
<ul><li class="level1">The SelectNextTrack, SelectPrevTrack and LoadSelected controls do not work in the Browse view. See <a href="https://bugs.launchpad.net/mixxx/+bug/342120" class="urlextern" title="https://bugs.launchpad.net/mixxx/+bug/342120" rel="nofollow">bug #342120</a>
.</li>
<li class="level1"><div class="li"> The SelectNextTrack and SelectPrevTrack controls cause the <acronym title="Graphical User Interface">GUI</acronym>
 to freeze for a few seconds when you try to scroll down beyond the current page. See <a href="https://bugs.launchpad.net/mixxx/+bug/361170" class="urlextern" title="https://bugs.launchpad.net/mixxx/+bug/361170" rel="nofollow">bug #361170</a>
.<br />
</div>
</li>
</ul>
</ul>
