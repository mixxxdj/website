title: Guest Article: DJ on the fly with Mixxx and Raspberry Pi
authors: dennis
tags: mixxx in the wild, raspberry pi
date: 2020-08-22 12:00:00

*One of the things that make Mixxx special is that it works on more platforms that just Windows or macOS.*
*Thanks to Mixxx being open-source, it's possible to create "unusual" setups that the developers didn't expect - for example by running it on a low-cost Raspberry Pi single board computer combined with a touchscreen.*
*It's always great to see what cool stuff our users do with Mixxx, so when we discovered a video of it on Reddit, we asked Dennis to write a blog post about his project.*

https://www.youtube.com/watch?v=UZam2aeX3Nc

### Going portable

Since the advent of small, portable netbook computers and single board computers I have been trying to downsize my DJ setup.
Frustrated by power issues, lack of performance and audio quality I resorted to a bulky but solid Thinkpad, a cheap controller and my software of choice: Mixxx.

This is a small story on how developments in both open source hard- and software as well as a well-equipped parts bin ends up in a somewhat specific but usable portable DJ setup using Mixxx and a Raspberry Pi.

This was until I was commissioned to make a random sound file player for an exhibition by [De Player](https://www.deplayer.nl/).
In a move that later proved to be somewhat overkill, I grabbed a Raspberry Pi 3 that had been collecting dust and wrote some scripts to play random audio files.

Up until then I had only worked with the original Raspberry Pi and I was quite shocked at the greatly improved performance of the Pi model 3.
Out of curiosity, a quick search of the Rasbian software repository brought up a match for "Mixxx"... but wait, would it actually run?

### Gaining power

To my surprise Mixxx did run fine!
With new found hope of building a "laptop-less" portable DJ setup I connected my USB sound card and cheap controller only to find out the Raspberry Pi could not deliver enough current to the USB port of the controller - no surprise there.

Eager to keep the setup simple and portable, I did not want to deal with external powered USB hubs.
To no avail I tried various cheap USB cards and after many more low power warnings and high latencies, my eye fell on a white label brand controller (Akiyama Pulsar) with built-in soundcard.
This "Traktor ready" controller had been given to me over the previous owner's frustrations with the lack of mappings for any other software than Traktor.

### Putting one and two together

Being both a controller and audio interface, the Akiyama Pulsar reduced the overhead created by multiple USB devices (?) allowing the Raspberry Pi to run Mixxx smoothly with less than 20ms latency and no underruns.
Note, this is without any optimizations to the Raspbian OS (no realtime kernel, no JACK) so there is possibly room for improvement!

As there was no mapping for the controller I set out to create my own.
Most buttons are easily mapped using the GUI, but the jogwheels can be problematic.
Starting from an existing community contributed mapping script that did not intimidate me (Icon iDJ) and by launching Mixxx with the `--controllerDebug` argument I was able to at least get the jogwheels to be somewhat reactive.

### Skinning the fat

To make the setup extra portable I dressed my Raspberry Pi in a 2.8" Touch Screen that is long out of production.
Being rather impractical, I would suggest getting a larger screen.
Nevertheless, you will need a skin that accommodates the data you are interested in, while being readable on a small screen.

Again I started off with an existing skin, an older "minimal" skin found on in an old Mixxx install (< 2.0.0) only to find out there is no scaling, only absolute values for size and position as well a different naming convention for buttons, making it incompatible with newer skins and mappings ("library" verus "playlist" for example).

The skins provided by the later Mixxx distributions seemed rather indimidating at first but soon made me realized they are far more flexible than they look.
Next to dynamic scaling using `(e,e)` units the newer default skins are somewhat modular.
Departing from LateNight i simply deleted the style xml files for the buttons/sections I did not need, ending up with a minimal two deck view of waveforms, track name, bpm and using a leftover key on my controller to show and hide the fullscreen library!

The paths where Mixxx stores its default skins and controller mappings are different on various operating systems.
Working with both OSX and Raspbian this was somewhat confusing at times.
To add to this, the directory of the built-in skins/mappings is not the same as the user skins/mappings.
As soon as you edit a default mapping for example, it gets copied to your "user" settings directory.
Keep this in mind (and just edit/copy your custom mapping directly to your "user" settings folder).

### In short

* Get a Raspberry Pi 3 Model B or newer
* Find a USB DJ controller with built-in sound-card.
* Get a powerbank that can deliver the right amount of current.
  The specifications advertised about most electronics don't seem to tell much, there is only one way to find out...try it out and let the [community](https://mixxx.zulipchat.com/) know!

### What is next?

The current setup is far from perfect. While being portable, allowing for a quick session at a friends place or even outdoors, the controller mapping and skin still need work.
So rather than sharing an end result I hope this post will encourage you to start tweaking your own settings and contributing to the Mixxx cause!

### Read more

* Check out the complete how-to guide on this [git repo](https://github.com/dennisdebel/pi_dj). You will also find the skin and controller mapping there.
* A separate post for the skin I modified can be found [here](https://mixxx.discourse.group/t/skin-for-small-screens-wip/19607/5).
