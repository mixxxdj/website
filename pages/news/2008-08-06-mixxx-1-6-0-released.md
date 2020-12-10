title: Mixxx 1.6.0 Released!
author: Albert
date: 2008-08-06 11:00:00
comments: no

<div style="text-align: center;">The Mixxx team is proud to announce the final release of <span style="font-weight: bold;">Mixxx 1.6.0</span>
!<br />
<br />
</div>
<br />
<a href="http://www.mixxx.org/" onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}"><img alt="" border="0" src="{% static '/static/images/news/mixxx160site.png' %}" id="BLOGGER_PHOTO_ID_5231183677172499362" style="cursor: pointer; display: block; margin: 0px auto 10px; text-align: center;" />
</a>
<br />
Mixxx 1.6.0 represents over a year's worth of hard work from our growing development team. The development of 1.6.0 was been driven by continuous feedback from our users, the bulk of which began in May 2007 with our popular user survey. Since then, we've taken the features that people wanted the most and focused every effort on developing them. Needless to say, 1.6.0 is light-years ahead of 1.5.0, and our community's continued appreciation for Mixxx has served as a strong motivator for us throughout its development.<br />
<br />
We've also <a href="http://www.mixxx.org/">relaunched our website</a>
 with a fresh coat of paint. Clicking the thumbnail above will take you to the new site.<br />
<br />
<div style="font-weight: bold; text-align: center;"><span style="font-weight: bold;">Mixxx 1.6.0 is now available on our </span>
<a href="http://www.mixxx.org/download/" style="font-weight: bold;">downloads page</a>
<span style="font-weight: bold;">. </span>
</div>
<br />
We'd like to thank both <a href="http://www.hercules.com/">Hercules</a>
 and <a href="http://www.echoaudio.com/">Echo Audio</a>
 for supporting Mixxx's development. Hercules' MK2 and RMX controllers are excellent, and Echo makes fantastic professional-grade soundcards (and we mean it).<br />
<br />
If you'd like to come hang out with some of the Mixxx developers and fellow users, we're having a <a href="{% url '/news/2008-08-02-mixxx-meetup-friday-august-8th-2008-7pm-linux-caffe-toronto.html' %}">meetup at the Linuxcaffe in Toronto</a>
 on Friday, August 8th from 7 PM to 11 ish. Come check it out!<br />
<br />
Before getting to the changelog, I'd like to mention one thing - A big change we've made is that Mixxx 1.6.0 is built on the <a href="http://www.trolltech.com/">Qt 4</a>
 platform instead of Qt 3. Porting Mixxx to Qt 4 took a massive effort from many developers, and was important to modernize Mixxx's look and feel, as well as ensure that Mixxx's codebase doesn't become obsolete. We've made many technical improvements inside Mixxx in order to allow the project to grow well into the future. Mixxx is now a much more mature open source project than it was a year ago, and there's no signs of us slowing down.<br />
<br />
Since Mixxx 1.5.0 was released (March 4th, 2007), the following changes have been made:<br />
<ul><li><span style="font-weight: bold;">New MIDI mappings</span>
 for Tascam US-428, M-Audio X-Session Pro, Evolution X-Session, FaderFox DJ2, and the M-Audio Torq Xponent, Vestax VCI-100, Akai MPD24, Behringer BCD3000 (including LEDs), Numark Total Control</li>
<li>Many Hercules MK2 improvements</li>
<li>Support for the Hercules DJ Console RMX</li>
<li>Support for the Hercules DJ Console Mac Edition</li>
<li>Slick sliding VU meter peaks - Screenshots don't do this justice (download it and check it out).</li>
<li>Added the new Natt skin, from Natt from the forums.</li>
<li>Completely rewritten waveform view by Russell Ryan through Google Summer of Code. This will provide better performance for some users.</li>
<li>Some very under-the-hood improvements that should fix the odd crash-at-startup and improve performance.</li>
<li>Fixed keyboard cue keys to use whatever cue behaviour is selected in the preferences.</li>
<li>MP3 parsing fixes for files with cover art (fixes blips at the start of some songs)</li>
<li>OGG parsing improvements, fixes some library scanning problems</li>
<li>Fixed OGG playback on Intel OS X machines</li>
<li>Completed drag-and-drop support in the library. You can now import tracks to the library by drag-and-dropping a track from outside Mixxx onto the library view. You can also reorder tracks in a playlist or the library.</li>
<li>Option to disable the BPM detection.</li>
<li>Added <span style="font-weight: bold;">BPM reading from MP3/OGG files</span>
 which have it embedded in them (ID3), one of several enhancements by Martin Sakmar</li>
<li>Various accuracy improvements to the BPM detection</li>
<li>Improvements to the vinyl emulation and pitch-independent time stretch sound quality</li>
<li><span style="font-weight: bold;">Wave recording support</span>
</li>
<li><span style="font-weight: bold;">Vinyl control</span>
 with support for Serato, Traktor, and FinalScratch vinyl, as well as Serato CD.</li>
<li>Added support for multiple inputs on a single soundcard for vinyl control </li>
<li>Build flags are now cached automatically</li>
<li>Improved flanger effect, thanks to Enry</li>
<li>Configurable cue behaviour, which now defaults to<span style="font-weight: bold;"> CDJ-style cueing</span>
. (Thanks to Tom Care)</li>
<li>Enabled <span style="font-weight: bold;">realtime priority</span>
 with ALSA, improves performance with Linux RT kernels.</li>
<li><span style="font-weight: bold;">FLAC support</span>
 for Linux and OS X users (much requested)</li>
<li>Tons and tons of bug fixes.</li>
<li>Fixed crashes due to vinyl emulation mode</li>
<li>Improved compatibility with JACK (some users were experiencing choppiness)</li>
<li>Players should now only pull from the play queue if in NEXT mode</li>
<li><span style="font-weight: bold;">Search functionality:</span>
<br />
o Search box now selects all text when clicked (easier to make a new search now)<br />
o When the search box is cleared, the library view will scroll back to it's previous position.<br />
o Search now properly filters directories out</li>
<li>Library stuff:<br />
o Double-clicking on a song now sends the song to the first stopped player.<br />
o Right-click menu cleaned up, much nicer now<br />
o Library directory rescans on startup when it's been modified (*doesn't work when subdirectories are modified yet)<br />
o Library view now shows directories first<br />
o Columns in the library view are proportioned intelligently now<br />
o Renamed the "Playlist" menu to "Library"<br />
o Added "Rescan Library" menu item.<br />
o Can select multiple songs (hold shift) and send them to the play queue or a playlist</li>
<li>Playlist support:<br />
o Can create, import, delete, and rename playlists<br />
o Added "Playlists" to library drop-down box<br />
     + Can right-click to send a playlist to the play queue.</li>
<li>Fixed some bugs in the track properties dialog, and set default values</li>
<li>Fixed a soundcard channel selection bug when the second device had more channels than the first.</li>
<li>Added BPM Schemes (need to make some presets still)</li>
<li>Minor speed optimization</li>
<li>OS X/Leopard package for Intel users!</li>
<li>A few build system (dependency checking) fixes</li>
<li>MIDI LED control on Linux</li>
<li>A few MIDI tweaks here and there</li>
<li>Right-clicking on a knob/slider no longer moves with your mouse (it just centers the value)</li>
<li>Using your mouse's <span style="font-weight: bold;">scroll wheel</span>
 now changes the values of sliders and knobs (this is cool for laptop users with the little scroll bar at the side of their trackpads)</li>
<li>DirectSound is now the default API on Windows</li>
<li>ALSA Sequencer MIDI support courtesy of Cedric Gestes</li>
<li>A couple of MIDI bug fixes (knobs now center properly, thanks to Sacha Berger)</li>
<li>Added support for 14-bit MIDI pitch wheel controllers (thanks to Adam Sugerman)</li>
<li>Hercules support on Linux improved (jog wheels work again)</li>
<li><span style="font-weight: bold;">Big stability improvements</span>
</li>
<li><span style="font-weight: bold;">Multiple soundcards</span>
 can now be used for output (master/headphones), in case you don't have a soundcard with 4 outputs on it.</li>
<li>Adam's wicked<span style="font-weight: bold;"> colour scheme support</span>
 for skins</li>
<li>Can now change skins without restarting Mixxx (more hard work from Adam)</li>
<li>Channel VU meters are now pre-fader</li>
<li>VU meters are now much more <span style="font-weight: bold;">smooth</span>
</li>
<li>Added clipping indicators (courtesy of John Sully)</li>
<li><span style="font-weight: bold;">Higher quality EQs</span>
 and other sound quality improvements (also from John Sully)</li>
<li><span style="font-weight: bold;">Adjustable EQ shelves</span>
</li>
<li>New MIDI mapping format now in XML, supports controlling LEDs</li>
<li>Better Hercules support on Windows and Linux</li>
<li><span style="font-weight: bold;">New BPM detection algorithm</span>
 (Micah Lee/GSoC 2007)</li>
<li><span style="font-weight: bold;">New media library</span>
 (Nathan Prado/GSoC 2007)</li>
<li>LADSPA effects support (not yet enabled - Pawel Bartkiewicz/GSoC 2007)</li>
<li>BPM Tap tempo</li>
<li>Ported to<span style="font-weight: bold;"> Qt 4</span>
</li>
<li>Moved build system to <span style="font-weight: bold;">SCONS</span>
</li>
<li>Redesigned preferences dialogs</li>
<li><span style="font-weight: bold;">Rewritten audio core</span>
 (Albert)</li>
<li><span style="font-weight: bold;">Vinyl control</span>
 support for <span style="font-weight: bold;">Serato</span>
, Traktor Scratch, and FinalScratch (FS needs work, but the others are good)</li>
<li>Software preamp for vinyl control (can use turntables without a preamp)</li>
<li>Track info editor (double-click in library)</li>
<li>New library browse mode (CTAF)</li>
<li>Starts in fullscreen mode if launched with the -f flag.</li>
<li>Several MP3 decoder performance and stability improvements (John Sully)</li>
<li>Support for merengue</li>
<li>Reorganized "File" menu</li>
<li>NEXT mode now works as expected (plays the next track in the table)</li>
<li>Lots of little OS X improvements</li>
<li>Improved consistency of fullscreen mode</li>
<li>Customizable <span style="font-weight: bold;">constant power crossfader curve</span>
</li>
<li>Slow fade and fast cut crossfader curves</li>
<li><span style="font-weight: bold;">Play queue</span>
, for creating an on-the-fly playlist</li>
<li>Revamped playlist interface, editing</li>
<li>Reasonably intelligent library rescanning </li>
</ul>
Once again, Mixxx 1.6.0 can be downloaded for free from our <a href="http://www.mixxx.org/download.php">downloads page</a>
.
