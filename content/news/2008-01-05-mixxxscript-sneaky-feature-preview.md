title: MixxxScript - A Sneaky Feature Preview
author: Adam Davison
date: 2008-01-05 16:42:00
comments: no

Although we're technically in the beta part of the release cycle, we've still been spending some time on features for future releases. I've been working on adding a macro/scripting style environment to Mixxx which would allow users to extend Mixxx without the work of recompiling. Here's a screenshot of the very basic test GUI in action:<br />
<br />
<a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="{% static '/static/images/news/mixxxmacros.png' %}"><img style="margin: 0px auto 10px; display: block; text-align: center; cursor: pointer;" src="{% static '/static/images/news/mixxxmacros.png' %}" alt="" id="BLOGGER_PHOTO_ID_5152039624722077778" border="0" />
</a>
<br />
The script interpreting is done using the new QtScript ECMAScript interpreter built in to Qt 4.3 and the example you can see typed in above implements a basic auto-crossfader.<br />
<br />
The potential here is fairly unlimited. API documentation and so on will follow soon so that people using Mixxx from SVN will be able to have a play.
