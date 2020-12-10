title: Mixxx 1.7.0 Beta 2 Released!
author: Albert
date: 2009-07-20 18:00:00
comments: no

<a href="{% static '/static/images/news/Screenshot-Mixxx-1.7.0-beta2-2.png' %}" onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}"><img alt="" border="0" src="{% static '/static/images/news/Screenshot-Mixxx-1.7.0-beta2-2.png' %}" id="BLOGGER_PHOTO_ID_5360332606147228482" style="cursor: pointer; display: block; height: 246px; margin: 30px auto 20px; text-align: center; width: 400px;" />
</a>
<br />
The Mixxx team is pleased to announce the release of <a href="http://www.mixxx.org/download/"><span style="font-weight: bold;">Mixxx 1.7.0 Beta 2</span>
</a>
! This is primarily a bugfix release that addresses issues from our previous beta.<br />
<br />
We also recently discovered a critical issue in an external software library which affects Mixxx users on <span style="font-weight: bold;">Ubuntu 9.04</span>
. Please see the note at the bottom of this post for more information.<br />
<br />
Some of the changes in Mixxx 1.7.0 Beta 2 include:<br />
<ul><li>Fixed missing MIDI bytes under heavy load on Linux.</li>
<li>Fixed vinyl control input for users with multi-channel input.</li>
<li>Fixed vinyl control channel selection bug</li>
<li>A slew of SCS.3d improvements and tweaks. </li>
<li>Hercules MK2 and RMX improvements</li>
<li>Stanton SCS.1m support</li>
<li>Internal control engine optimizations</li>
<li>Fixed several crash-on-startup scenarios</li>
<li>Fixed library rescans not finding new files added in subdirectories</li>
<li>Fixed Ubuntu menu shortcut</li>
<li>Fixed missing Ubuntu package dependencies</li>
<li><span style="font-weight: bold;">Added Universal Package for OS X 10.4+</span>
 (Special thanks to Brian Jackson for leading the effort to put this together.)</li>
</ul>
Mixxx 1.7.0 Beta 2 is available on our <a href="http://www.mixxx.org/download.php#beta">downloads page</a>
.<br />
<br />
Formality aside, this list of changes doesn't do the last few months justice. After our last beta, we received dozens of helpful bug reports. Some of those brought new problems to our attention, while others shed light on old ones. With your valuable feedback, we managed to not only fix your most pressing bugs, but we were also able to track down and fix some other <span style="font-style: italic;">very</span>
 tricky bugs. The result of your great bug reporting and our team's commitment to fixing bugs is the most stable, polished release of Mixxx to date, and we couldn't have done it without you.<br />
<br />
Thank you to everyone who's been testing our beta releases and reporting bugs. You've made a valuable contribution to open source and the whole Mixxx community, and together we're going to continue to make Mixxx the best DJ software we can.<br />
<br />
As usual, please report any new bugs or regressions to our <a href="https://bugs.launchpad.net/mixxx">bug tracker</a>
. If you want to get in touch with other Mixxx DJs, show some love on <a href="http://www.mixxx.org/forums">our forums</a>
!<br />
<br />
Stay tuned for our final 1.7.0 release!<br />
<br />
<span style="font-weight: bold;">Important note for Ubuntu 9.04 users:</span>
A flaw has been discovered in a library provided by Ubuntu 9.04 that can cause critical hangups in Mixxx. Ubuntu 9.04 users are advised to install the version of PortAudio from Ubuntu 8.10, available as .deb packages here:<br />
<ul><li><a href="http://packages.ubuntu.com/intrepid/i386/libportaudio2/download">PortAudio for i386</a>
</li>
<li><a href="http://packages.ubuntu.com/intrepid/amd64/libportaudio2/download">PortAudio for amd64</a>
</li>
</ul>
