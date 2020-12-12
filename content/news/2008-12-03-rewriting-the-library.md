title: Rewriting the Library
authors: Albert Santoni
date: 2008-12-03 01:03:00
comments: no

*This developer commentary explains the trials and tribulations of Mixxx's library code, and what the Mixxx developers are doing to improve it.*

In the (long) development cycle between Mixxx 1.5.0 and 1.6.0, several changes were made to the library.
Some of the more visible changes were the addition of our search box and "Browse" mode, which allows you to play songs off your hard drive without importing them into the library.
There was also significant work done on playlist handling and management.

[![Mixxx 1.5.0, with our old-school library]({static}/images/news/mixxx-150beta-linux.png)]({static}/images/news/mixxx-150beta-linux.png)

[![Mixxx 1.6.1, with the new library]({static}/images/news/Picture-1.png)]({static}/images/news/Picture-1.png)

One not-so-apparent difference is that the underlying code was changed to use the [Model-View-Controller](http://en.wikipedia.org/wiki/Model-view-controller) (MVC) paradigm, which is easy to do with Qt 4 (... or so we thought).

As it turns out, many of the library problems that have been discovered since 1.6.0 are tied to the fact that we botched our use of MVC.
Even if you grasp the MVC concepts at a high level, when you get deep into coding it, the separation between "models", "views", and the organization of GUI code can become mucky.
Basically, we made some design mistakes, and the only way to correct them and allow us to continue improving the library is to go back and rewrite it from scratch.
Some of the library-related bugs in our tracker are going to be *very* tough to fix because of the current poor design ([#194415](https://bugs.launchpad.net/mixxx/+bug/194415) , [#202594](https://bugs.launchpad.net/mixxx/+bug/202594) , [#257769](https://bugs.launchpad.net/mixxx/+bug/257769) , [#258955](https://bugs.launchpad.net/mixxx/+bug/258955) , [#275198](https://bugs.launchpad.net/mixxx/+bug/275198) , etc!).
Rewriting the library code will prevent many of these bugs from reappearing, and should also prevent us from being in a quagmire like this again in the future.
Of course, this all depends on us having learned from our mistakes, and I hope that we have. :)

[![Mixxx with the even newer library!  (work-in-progress)]({static}/images/news/Picture-2.png)]({static}/images/news/Picture-2.png)

Back in October at the [GSoC Mentor Summit]({filename}/news/2008-11-12-mixxx-gsoc-mentor-summit.md) , I started hacking our library to use an integrated [SQLite](http://www.sqlite.org/) database to store track metadata, instead of storing them in a flat [XML](http://en.wikipedia.org/wiki/XML) file on disk.
I quickly discovered that there were **two separate problems** - The first being how the library was stored inside Mixxx at runtime, and the other being how it was stored on disk (XML).

At runtime, we were using a **gigantic** [skip-list](http://en.wikipedia.org/wiki/Skip_list) to store the metadata of every single track in the library.
If you had a library with 100,000 songs, we were keeping the metadata (eg.  ID3 tag info) for every song in memory.
As you might guess, this was probably something the original Mixxx developers didn't think very hard about, because it doesn't scale well to large libraries.
This brings us to the second problem.

When Mixxx starts up or is shut down, it read/writes **all** of this track metadata to an XML file (`mixxxtrack.xml`).
Again, this simply doesn't scale well for large libraries because it takes a very long time to write metadata for a library of 100,000 songs (and is another example of where the original Mixxx developers didn't think hard enough).

When I started hacking **SQLite integration into Mixxx** , I started replacing the XML file loading/saving stuff.
I quickly realized that I was going to need to fix the skip-list problem too, and then the lightbulb went on - Switching to SQLite solves both of these problems.
Rather than storing metadata for all the tracks in memory at runtime, we could simply query the database to retrieve what we need.
With that thought, I started deleting as much of the old library code as possible - **It was a complete write-off** .

I wanted to start from scratch to prevent myself from falling into the trap of the poor design of the old library.
I coded many of the changes to the library that were made in 1.6.0, and it took a long time for me to finally give up and realize it was never going to be salvageable.
I find this amusing because history is repeating itself - I made major changes to the soundcard I/O code inside Mixxx several times before I gave up and rewrote it all from scratch (which enabled things like vinyl control and multiple soundcard support to happen).
For me, this is the fuel that keeps me coding.
I know that **cool things** will be possible if I rewrite the library the Right Way (TM).

There is still a very long way to go before the new library code is complete, but I already have a few **new features** that people have been requesting, like the ability to move the columns in the library around (which saves automatically too!).
Starting and shutting down Mixxx is faster, and I'm hoping that searching will be faster as well.
The rewrite has also improved other areas of Mixxx's code - Some pieces of the old library were tied to seemingly unrelated parts of Mixxx, and fortunately I've been able to separate them, which solves many of the code organization problems that the old library had.

Some of the (big) things that need to be added still are playlist support, browse mode, and some sort of intelligent library scanning.
The last item is being worked on by a new contributor, and we've been playing around with some cool ideas that we're both hoping will improve the library scanning/rescanning situation greatly.
(That topic probably deserves a blog article on it's own.) :) In any event, the new library code won't be ready for at least another release or two.

Anyways, the main focus is to reimplement all the library functionality that was there before, but while I'm hacking the library, **I want to hear what cool new features you (Mixxx users) want**.
If you want to share a neat idea, please leave a comment!
