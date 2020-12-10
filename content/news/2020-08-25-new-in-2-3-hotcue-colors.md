title: New in 2.3: Color your Hotcues
author: Holzhaus
date: 2020-08-25 12:00:00

Hotcues are a neat thing and one of the major benefits of digital DJing.
On analogue vinyl decks, you had had to put stickers to mark the different sections of a song and physically pick up, move and drop the needle to move to it.
With the move to digital DJ setups, a new way to navigate tracks emerged: Hotcues now allow you to "bookmark" different spots in a track and quickly move to these positions in the blink of an eye, even while track is playing on the PA.

Mixxx has supported them for more than 10 years now:
Initial support for numbered hotcues has been added in 2009.

However, it can be challenging to remember the correct number in the heat of the moment.
Accidentally pressing the wrong hotcue pad is not something you or your audience want to hear.

## Better Hotcue Labels

In 2015, support for hotcue labels was added to mitigate this problem.
These can be arbitrary text that is shown on the waveforms.
However, these were only shown on the scrolling waveforms, so you could not see them unless the track was close to that position.
Also, it was cumbersome to edit labels because this was buried in the track Properties dialog that was only accessible from the library.

In Mixxx 2.3, we overhauled the way you can interact with hotcues using the mouse:
It's now possible to see the labels on the overview waveforms.
You can edit them directly from the waveform by right clicking.

If you have long, descriptive labels on hotcues that are close together, Mixxx will elide the labels so they don't overlap.
You can still see the full label by hovering your mouse over an elided label.
Mixxx will hide any other labels this would be drawn over so the text is legible.

![Hotcue labels on overview waveforms]({static}/images/news/hotcue-colors-labels.png)

## Color your Hotcues

But Mixxx 2.3 has yet another next major improvement for hotcues in the pipeline:
Hotcues can now have individual colors to make them visually distinguishable.

How you color code your hotcues is up to you - one example would be to set red cues 16 beats before the drop or chorus, yellow 8 beats before it and color the start of vocals blue.

![Hotcue buttons and color picker]({static}/images/news/hotcue-colors-picker.png)

## Pick the colors YOU like

By default, you can pick a color from the Mixxx Hotcue Color palette.
That palette contains 9 colors that are easy to distinguish.

Personal preferences differ though, and it's probably impossible to suit everyones taste.
This is why - unlike most other DJ software - you are not restricted to the single predefined color palette we picked.

If you previously used Serato DJ Pro, Rekordbox, Traktor or VirtualDJ and like their color palettes better ours, we've got you covered.
You can also use one of their palettes instead.

![Hotcue color palette selection]({static}/images/news/hotcue-colors-palette-combobox.png)

But it doesn't stop there:
We also added a powerful color palette editor that can be used to rearrange and customize these palettes and even design *your own palette* using any RGB colors you like.

![Hotcue color palette editor]({static}/images/news/hotcue-colors-palette-editor.png)

## Automatic Coloring

When setting a hotcue, a single default color is assigned that you can select in the preferences.
You can then go ahead and change the color to your liking.

While assigning a custom color to cue points after you set them is a nice feature, coloring all your cue points this way can be tedious and a lot of extra work.
If you want, Mixxx 2.3 can color new hotcues automatically for you - based on the hotcue number.

A small example:
Say you want to set a cue point before the main vocal part, and you want it colored "blue".
You can configure Mixxx to always assign "blue" to the hotcues number 5, and then just set hotcue number 5 at the desired position - done.

If you do this, that also means that a hotcue of the same type (e.g. "before main vocals") does not only have the same color but is also assigned to the same hotcue pad.
Hence, the possibility of getting confused during a gig is reduced even more than when just using colors as visual aid.

## Bulk replace old hotcue colors

At some point, you might feel like your current scheme for color code hotcues lacking and unintuitive.
Maybe you simply don't like the colors anymore and would like to switch to a different palette.
Or you realize that you find the colorful hotcue buttons actually distracting and want to get rid of them.
If that happens, you may want to bulk replace the colors of existing hotcue in your library.

We're not aware that any of our competitors in the DJ software market have such an option - Mixxx 2.3 has.
You can find a dialog for replacing colors on the "Colors" page in the preferences window.

It allows bulk replacing hotcue colors for hotcues in your library and can be used to

  - replace colors by hotcue number ("Set the color of all hotcues with number 5 to blue"),
  - replace colors by current color ("Set the color of all red hotcues to blue"),
  - combine the two conditions ("Set the color of all red hotcues with index 5 to blue"),
  - negate them ("Set the color of all hotcues that are red but don't have number 5 to blue")  or
  - just replace all hotcue colors in your library unconditionally ("Set the color of all hotcues to blue").

![Hotcue color replace dialog]({static}/images/news/hotcue-colors-replace.png)

## Support for colored hotcues on controllers

You're a controller mapping creator and wondered how to make use of hotcue colors on your controller?
Then don't worry - we designed this feature with controller support in mind.

When it comes to hotcue buttons, there are 4 types of controllers:

  1. Controllers without hotcue buttons
  2. Controllers with uncolored buttons
  3. Controllers with colored hotcue buttons that allow setting an arbitrary RGB color
  4. Controllers with colored hotcue buttons that only allow setting certain, predefined colors

For controllers of types 1 and 2, nothing changes (obviously).

For type 3, we made the RGB color of a hotcue accessible in controller scripts, so you can go ahead and implement support for it.
If your controller mapping uses our JavaScript Components library, this is quite simple:
You only need to implement the `HotcueButton::sendRGB(color)` method, that sends the 3-byte RGB color value to the controller (e.g. via a MIDI-SysEx message, depending on your hardware).

What about type 4?
Controllers that only allow choosing from a predefined color set were probably designed that way because they were sold with a software that does not allow assigned arbitrary colors to hotcues.
You can think of these predefined colors as a list, and usually you can set the pad color of these controllers by sending the color's index in that list as MIDI value.
For example, red could be color 1, blue is color 2, yellow is color 3, green is color 4 and so on.

We added a `ColorMapper` class that you can use to establish a mapping between these IDs and can be used to get the appropriate MIDI value for a given color.

But what happens if you set a hotcue to a color that isn't supported by the controller?
Obviously, it's not possible to show the exact same color on your controller if the hardware simply doesn't support it - but don't worry, we've got you covered.

In this case, `ColorMapper` returns the ID of the color that is *most similar* to the color you put in.
As an example, the hotcue color in Mixxx could be a darker shade of blue - ColorMapper will simply return the color for the regular blue color in this case, because it's the best match.

![Hotcue colors on a controller]({static}/images/news/hotcue-colors-controller.gif){: style="width: 100%" }

Seems complicated?
It doesn't have to be.
If your mapping already uses our JavaScript Components library, you can just create a `ColorMapper` object, add it to the `HotcueButton` and your colored hotcue pads should start working!

We also added [controls](https://mixxx.org/wiki/doku.php/mixxxcontrols) to to make it possible assign a different color to an existing hotcue from your controller - for example, the mapping for the Roland DJ-505 uses the PARAMETER -/+ buttons next to the hotcue pads to cycle through the color palette for most recently activated hotcue.

Refer to our wiki if you want to integrate it into your controller mapping and check out the video below:
