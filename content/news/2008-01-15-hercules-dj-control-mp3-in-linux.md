title: Hercules DJ Control MP3 in Linux
authors: Albert Santoni
date: 2008-01-15 04:21:00
comments: no

[![Hercules DJ Control MP3]({static}/images/news/hercules-dj-control-mp3.jpg)]({static}/images/news/hercules-dj-control-mp3.jpg)

[Robin](http://www.kallisti.net.nz/) , one of our newer developers, has been [working hard](http://www.kallisti.net.nz/blog/2008/01/making-the-hercules-dj-control-mp3-work-with-mixxx/) on improving our support for the [Hercules DJ Control MP3](http://www.amazon.com/Hercules-4780288-DJ-Control-MP3/dp/B000BK2EOY) in Linux.
I did some work on this myself last year, but unfortunately certain things were broken at the kernel-level and I wasn't able to get the LEDs working.
After many attempts by several people, Robin managed to make a kernel patch to solve the remaining issues.

"Yuck, a kernel patch!", you say?
As Robin [writes](http://www.kallisti.net.nz/blog/2008/01/making-the-hercules-dj-control-mp3-work-with-mixxx/):

> This is all very hacky, but hopefully it won't be in the future.
> I'm going to see if I can get that patch put in the kernel proper, which will solve the most annoying part of the problem.
> It would also be good to get Mixxx supporting both legacy mode and the newer one at the same time.
>
> **However, we've heard from Hercules, and they say that some time in the first part of this year, they're going to try to get some Linux drivers out.**
> Hopefully they're open source, and turn the Herc devices into MIDI devices, which would make life a whole lot easier for support.

It looks like there's light at the end of the tunnel for Hercules users.
[Read more on Robin's blog](http://www.kallisti.net.nz/blog/2008/01/making-the-hercules-dj-control-mp3-work-with-mixxx/).

**Note:** I should add that the Hercules MK2 and the Hercules MP3 Control are both supported *very well* on **Windows**.
