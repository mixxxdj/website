title: Rewriting the Library
author: Albert
date: 2008-12-03 01:03:00
comments: no

{% extends "post.html" %}

{% block post %}

<span style="font-style: italic;">This developer commentary explains the trials and tribulations of Mixxx's library code, and what the Mixxx developers are doing to improve it.</span>
<br />
<br />
In the (long) development cycle between Mixxx 1.5.0 and 1.6.0, several changes were made to the library. Some of the more visible changes were the addition of our search box and "Browse" mode, which allows you to play songs off your hard drive without importing them into the library. There was also significant work done on playlist handling and management.<br />
<br />
<a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="{% static '/static/images/news/mixxx-150beta-linux.png' %}"><img style="margin: 0px auto 10px; display: block; text-align: center; cursor: pointer; width: 400px; height: 320px;" src="{% static '/static/images/news/mixxx-150beta-linux.png' %}" alt="" id="BLOGGER_PHOTO_ID_5275366722578779602" border="0" />
</a>
<br />
<center><span style="font-style: italic;">Mixxx 1.5.0, with our old-school library</span>
</center>
<br />
<br />
<a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="{% static '/static/images/news/Picture-1.png' %}"><img style="margin: 0px auto 10px; display: block; text-align: center; cursor: pointer; width: 400px; height: 319px;" src="{% static '/static/images/news/Picture-1.png' %}" alt="" id="BLOGGER_PHOTO_ID_5275367396220777410" border="0" />
</a>
<br />
<center><span style="font-style: italic;">Mixxx 1.6.1, with the new library</span>
</center>
<br />
<br />
One not-so-apparent difference is that the underlying code was changed to use the <a href="http://en.wikipedia.org/wiki/Model-view-controller">Model-View-Controller</a>
 (MVC) paradigm, which is easy to do with Qt 4 (... or so we thought).<br />
<br />
As it turns out, many of the library problems that have been discovered since 1.6.0 are tied to the fact that we botched our use of MVC. Even if you grasp the MVC concepts at a high level, when you get deep into coding it, the separation between "models", "views", and the organization of GUI code can become mucky. Basically, we made some design mistakes, and the only way to correct them and allow us to continue improving the library is to go back and rewrite it from scratch. Some of the library-related bugs in our tracker are going to be <span style="font-style: italic;">very</span>
 tough to fix because of the current poor design (<a href="https://bugs.launchpad.net/mixxx/+bug/194415">#194415</a>
, <a href="https://bugs.launchpad.net/mixxx/+bug/202594">#202594</a>
, <a href="https://bugs.launchpad.net/mixxx/+bug/257769">#257769</a>
, <a href="https://bugs.launchpad.net/mixxx/+bug/258955">#258955</a>
, <a href="https://bugs.launchpad.net/mixxx/+bug/275198">#275198</a>
, etc!). Rewriting the library code will prevent many of these bugs from reappearing, and should also prevent us from being in a quagmire like this again in the future. Of course, this all depends on us having learned from our mistakes, and I hope that we have. :)<br />
<br />
<br />
<a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="{% static '/static/images/news/Picture-2.png' %}"><img style="margin: 0px auto 10px; display: block; text-align: center; cursor: pointer; width: 400px; height: 319px;" src="{% static '/static/images/news/Picture-2.png' %}" alt="" id="BLOGGER_PHOTO_ID_5275368386039352834" border="0" />
</a>
<br />
<center><span style="font-style: italic;">Mixxx with the even newer library! (work-in-progress)</span>
</center>
<br />
<br />
Back in October at the <a href="{% url '/news/2008-11-12-mixxx-gsoc-mentor-summit.html' %}">GSoC Mentor Summit</a>
, I started hacking our library to use an integrated <a href="http://www.sqlite.org/">SQLite</a>
 database to store track metadata, instead of storing them in a flat <a href="http://en.wikipedia.org/wiki/XML">XML</a>
 file on disk. I quickly discovered that there were <span style="font-weight: bold;">two separate problems</span>
 - The first being how the library was stored inside Mixxx at runtime, and the other being how it was stored on disk (XML).<br />
<br />
At runtime, we were using a <span style="font-weight: bold;">gigantic</span>
 <a href="http://en.wikipedia.org/wiki/Skip_list">skip-list</a>
 to store the metadata of every single track in the library. If you had a library with 100,000 songs, we were keeping the metadata (eg. ID3 tag info) for every song in memory. As you might guess, this was probably something the original Mixxx developers didn't think very hard about, because it doesn't scale well to large libraries. This brings us to the second problem.<br />
<br />
When Mixxx starts up or is shut down, it read/writes <span style="font-weight: bold;">all</span>
 of this track metadata to an XML file (mixxxtrack.xml). Again, this simply doesn't scale well for large libraries because it takes a very long time to write metadata for a library of 100,000 songs (and is another example of where the original Mixxx developers didn't think hard enough).<br />
<br />
When I started hacking <span style="font-weight: bold;">SQLite integration into Mixxx</span>
, I started replacing the XML file loading/saving stuff. I quickly realized that I was going to need to fix the skip-list problem too, and then the lightbulb went on - Switching to SQLite solves both of these problems. Rather than storing metadata for all the tracks in memory at runtime, we could simply query the database to retrieve what we need. With that thought, I started deleting as much of the old library code as possible - <span style="font-weight: bold;">It was a complete write-off</span>
.<br />
<br />
I wanted to start from scratch to prevent myself from falling into the trap of the poor design of the old library. I coded many of the changes to the library that were made in 1.6.0, and it took a long time for me to finally give up and realize it was never going to be salvageable. I find this amusing because history is repeating itself - I made major changes to the soundcard I/O code inside Mixxx several times before I gave up and rewrote it all from scratch (which enabled things like vinyl control and multiple soundcard support to happen). For me, this is the fuel that keeps me coding. I know that <span style="font-weight: bold;">cool things</span>
 will be possible if I rewrite the library the Right Way (TM).<br />
<br />
There is still a very long way to go before the new library code is complete, but I already have a few <span style="font-weight: bold;">new features</span>
 that people have been requesting, like the ability to move the columns in the library around (which saves automatically too!). Starting and shutting down Mixxx is faster, and I'm hoping that searching will be faster as well. The rewrite has also improved other areas of Mixxx's code - Some pieces of the old library were tied to seemingly unrelated parts of Mixxx, and fortunately I've been able to separate them, which solves many of the code organization problems that the old library had.<br />
<br />
Some of the (big) things that need to be added still are playlist support, browse mode, and some sort of intelligent library scanning. The last item is being worked on by a new contributor, and we've been playing around with some cool ideas that we're both hoping will improve the library scanning/rescanning situation greatly. (That topic probably deserves a blog article on it's own.) :) In any event, the new library code won't be ready for at least another release or two.<br />
<br />
Anyways, the main focus is to reimplement all the library functionality that was there before, but while I'm hacking the library, <span style="font-weight: bold;">I want to hear what cool new features you (Mixxx users) want</span>
. If you want to share a neat idea, please leave a comment!

{% endblock %}
