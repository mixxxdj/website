title: Quick Vinyl Control Video, SSE optimizations
authors: Albert Santoni
date: 2007-12-03 01:56:00
tags: video, hardware, development
summary: A few nights ago I captured a video while doing a quick test mix using Mixxx's vinyl control.
comments: no

A few nights ago I captured a video while doing a quick test mix using Mixxx's vinyl control.

http://www.youtube.com/watch?v=9dRLNT2yspg

Not my best transition ever, but it works. :)

I've been trying to do some tweaking to get the latency down and one of the biggest improvements came from compiling Mixxx with SSE and MMX optimizations.
The tricky part with turning on these optimizations is that they'll only work on post-Pentium III CPUs.
That's fine for our Windows and OS X builds, but it's a problem for our Ubuntu package because we can't assume any specific CPU architecture.
One possible solution for this is to disable SSE/MMX optimizations in the package that lives in the Ubuntu repositories and host a different (SSE/MMX optimized) Ubuntu package on our website.

In the meantime, I still have lots of work to do on fixing up the library.
Busy, busy!
