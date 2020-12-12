title: Feature Preview: Shoutcast Broadcasting
authors: Albert Santoni
date: 2008-02-01 15:40:00
tags: development, broadcasting
comments: no

One of our newer contributors, **[Wesley Stessens**](http://wesley.debianbox.be/), has been hard at work on Shoutcast/Icecast broadcasting support for [Mixxx](http://mixxx.sf.net/).

[![Screenshot of Mixxx Preferences]({static}/images/news/Screenshot-Preferences.png)]({static}/images/news/Screenshot-Preferences.png)

It turns out Shoutcast support was a little bit more complicated than we had been expecting, but Wesley's done a great job of tackling all the problems that have come up.
Wesley also wrote a modular Ogg Vorbis encoder for the Shoutcast code, which we hope to reuse in our recording code in the future.

As a sub-project, adding Shoutcast support to Mixxx has been interesting because it's one of the nice modular projects we listed as a "[Weekend Project](http://mixxx.sourceforge.net/wiki/index.php/Developer#Weekend_Projects)" on our Wiki.
When Wesley came along and said he was interested in coding Shoutcast support, I had already sketched out what work needed to be done and was able to help him get started writing code for Mixxx right away.
If anyone's interested in adding a particular feature to Mixxx, come join our IRC channel (**#mixxx** on chat.freenode.net) and talk to one of us developers.
We'd be more than happy to help you get started writing code.

People who want to use Mixxx for live broadcasting will appreciate not having to use crazy routing through JACK in order to broadcast now.
For example, our friends over at [Radio Olympus](http://www.radiolympus.com/) have been looking for new live broadcasting software, and we hope Mixxx will soon be a candidate to replace their existing software.
Be sure to check out their newly [relaunched online radio station](http://musicworldradio.com/), broadcasting live from the UK.

Depending on how much work we can get done this weekend, Shoutcast support may or may not make it into 1.6.0 Beta2.
However, Shoutcasting should make it into the final 1.6.0 release.
(There's at least one more surprise coming for Beta2 though...)
