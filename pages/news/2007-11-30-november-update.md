title: November Update
author: Albert
date: 2007-11-30 15:24:00
comments: no

The last month has been completely insane. We've been busy fixing bugs and not-quite-finished features like there's no tomorrow. Our Subversion repository has seen more than 70 commits (those are generally changes to Mixxx's code) in the last month, and we've still got a few things to finish before the beta.<br />
<br />
<a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="{% static '/static/images/news/Screenshot-2.png' %}"><img style="margin: 0px auto 10px; display: block; text-align: center; cursor: pointer;" src="{% static '/static/images/news/Screenshot-2.png' %}" alt="" id="BLOGGER_PHOTO_ID_5138655970529655378" border="0" />
</a>
Some cool stuff that's been done in the last month though is:<br />
<ul><li><span style="font-weight: bold;">Multithreaded library scanning</span>
. Mixxx will scan your library in the background. Unfortunately, the actual library saving/loading part is slightly broken at the moment and I don't know if that will get fixed before the beta. (It just rescans your library every time, which is semi-annoying, but you always cancel it and use "Browse" mode.)</li>
<li><span style="font-weight: bold;">Automated (opt-in) crash reporting</span>
. We've added an exciting under-the-hood feature that allows us to gather crash reports automatically. This is strictly opt-in and so you're asked on your first run whether you'd like to help us out by enabling it or not.</li>
<li>The <span style="font-weight: bold;">play queue</span>
 works more or less now. This is a good example of the kind of dangling unfinished features we've been trying to get working before the beta.</li>
<li style="font-weight: bold;">Speed optimization</li>
<li>A few <span style="font-weight: bold;">tweaks</span>
 to the <span style="font-weight: bold;">vinyl control</span>
 in order to make it a little easier to use.</li>
</ul>
Lastly, I just want to say a word about vinyl control. Since I've been busy fixing other bugs for the last month, I haven't had time to give vinyl control the level of polish that I want it to have. When we release the beta, the viny control is probably going to be "very beta". If your timecode signal quality is bad, you'll probably have no idea what's going on. However, it should be usable, just not particularly user friendly. I'm hoping the beta release will spur some people to poke at the vinyl control code, which isn't terribly difficult to understand/tweak.<br />
<br />
I've written a <a href="http://mixxx.sourceforge.net/wiki/index.php/Vinyl_Control">Vinyl Control</a>
 page on our wiki which should hopefully answer some questions people have about it.
