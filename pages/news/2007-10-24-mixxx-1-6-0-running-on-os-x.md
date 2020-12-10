title: Mixxx 1.6.0 Running on OS X
author: Albert
date: 2007-10-24 02:23:00
comments: no

I picked up a Macbook a few days ago after weeks of trying to find a decent laptop. This is good news for Mixxx because it means our OS X maintainer (*cough* me) now has a Mac at home. :)<br />
<br />
Since the last time I compiled Mixxx on OS X, we've done a tremendous amount of work to port the project to QT4. Because of all the changes, I needed to give our SCONS build files an update in order to make Mixxx 1.6.0 build properly on OS X. After a few hours of tweaking away, I got it compiling, linking, <span style="font-weight: bold;">and</span>
 running (don't take that for granted):<br />
<br />
<a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="{% static '/static/images/news/Picture-3.png' %}"><img style="margin: 0px auto 10px; display: block; text-align: center; cursor: pointer;" src="{% static '/static/images/news/Picture-3.png' %}" alt="" id="BLOGGER_PHOTO_ID_5124724854553470482" border="0" />
</a>
In the long run, hopefully we'll be able to better tackle OS X-only bugs. Despite this screenshot, we're still a ways off from the 1.6.0 beta release. We've got a fair number of bugs to fix in the meantime before anything is releasable.
