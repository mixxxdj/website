title: MIDI Scripting and the Stanton SCS.3d (Videos)
authors: Albert Santoni
date: 2009-02-09 16:25:00
tags: hardware, videos, midi, development
comments: no

[![Stanton SCS.3d]({static}/images/news/scs3d.jpg)]({static}/images/news/scs3d.jpg)

One of Mixxx's newer developers, **Sean Pappalardo** ([DJ Pegasus](http://www.djpegasus.com/)), has been hacking away at MIDI scripting for the past few months so that we can fully support more advanced MIDI controllers.
One of the new controllers scripting will allow us to support is [Stanton's SCS.3d](http://www.enterthesystem.com/system/scs3d/index.php) (aka "DaScratch").

The **Stanton SCS.3d** replaces conventional knobs, buttons and sliders found on other MIDI controllers with touch-sensitive surfaces laid out in a DJ-friendly format.
It's compact, rugged, light-weight, and best of all, reliable, since there are almost no moving parts to break.
The large central circular area is where all the magic happens as it can be configured to serve multiple purposes (jog dial/vinyl emulation, three sliders, or 9 buttons) depending on the control needs of the software.

http://www.youtube.com/watch?v=qfkJnTqIeAw

*Sean demonstrating the SCS.3d with Mixxx 1.6.2*

Mixxx's previous MIDI system only allowed you to map one MIDI control to one property and provided no means of feedback or otherwise sending commands to the device.
However, controllers like the SCS.3d are of limited use without being able to illuminate LEDs and toggle various modes, since there would be no physical indicators.

Stanton gets around this by offering a free *middleware* solution called "DaRouter" which essentially acts as a MIDI translation bridge between your DJ software and the SCS.3d.
However, it is difficult to get feedback to the controller from your DJ software, and your ability to customize the device's behaviour is limited.
Additionally, this middleware solution is not available for Linux.

Enter Mixxx's new MIDI Scripting Engine.

After scratching our heads for some time, we conjured up and coded a system that **allows DJs to link hardware MIDI controls with custom script functions**.
These scripts are written in QtScript, which is an easy language that's almost identical to JavaScript.
Scripts can contain functions that can affect any number of Mixxx controls and also send feedback to a hardware MIDI device, freeing Mixxx from a one-to-one mapping ideology.
These user-created scripts can then do anything desired with the MIDI event data such as have a single controller button simultaneously affect two or more Mixxx properties, adjust incoming control values to work better with Mixxx (scratching,) display a complex LED sequence, or even send messages to text displays on the controller.

This approach provides a number of key benefits:

- Script functions are evaluated at run time and and can access or modify Mixxx's internal properties.
- QtScript brings all of the advantages of a **full scripting language** .
  For example, functions can use variables, allowing a single piece of code to be used for multiple cases and to remember states between invocations (this is how we implement mode and deck switching).
- Functions can **send any MIDI messages** they like including SYStem EXclusive messages, needed for advanced controllers like the SCS series for mode changes and text displays.
- Functions can be connected to Mixxx properties so that when the property changes, the function is called with the new value, allowing** automatic controller response**.
- **DJs can customize** the script functions to suit their particular work flow and desires without compiling anything.
- Support for complex controllers can be added to Mixxx at any time between releases by anyone since no compilation is needed!
- **No middleware** is needed to use advanced controllers like the SCS.3d with Mixxx
- Our MIDI scripting system is **platform-independent** , which makes it available to Windows, Mac OS X, and Linux users!

Our new MIDI scripting engine is going to be the biggest new feature in **Mixxx 1.6.2**, and we're currently polishing it up along with some of our other MIDI code.
We hope to have a beta release out within the next month or two for our DJs to play with.

Lastly, we'd like to thank [Stanton](http://www.stantondj.com/) for their gracious support and cooperation.
We think the [SCS.3d](http://www.enterthesystem.com/system/scs3d/) is going to be a great device for [Mixxx](http://www.mixxx.org/) users in the future!

http://www.youtube.com/watch?v=FgARVcLsfl0
