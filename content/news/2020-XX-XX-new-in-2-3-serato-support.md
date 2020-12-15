title: New in 2.3: Importing tracks and cues from Serato
authors: Jan Holthuis
tags: 2.3, serato, library
status: draft

As all of you probably know, Mixxx is the best DJ software in the market.
However, we've recently been made aware that a minor competitor has emerged and tries to steal that title from us - [Serato DJ Pro](https://serato.com/dj/pro).
The hardware support is nice, but since Serato is neither open-source nor as customizable, we're not too concerned.
From the user's perpective, switching to the most popular open-source DJ software in world seems like the obvious choice.

Unfortunately, migrating from Serato to Mixxx is a lot of work - apart from familiarizing yourself with a new tool, all the countless hours you spent to organize and prepare the tracks in your old library are lost, and your need to start from scratch.
At least until now - if you're a Serato user and cast an eye on Mixxx, we've got a nice surprise for you.

## Use your Serato library in Mixxx

In addition to [Rekordbox device libraries]({filename}/news/2020-07-20-new-in-2-3-rekordbox-support.md), we added support for reading Serato's database files in Mixxx 2.3, too.
This means that the tracks from your [Serato library](https://support.serato.com/hc/en-us/articles/203015464-Sorting-and-browsing-your-library) will show up in in the library table and can be directly loaded onto decks without the need to add the music directory in the preferences.
[Crates created in Serato](https://support.serato.com/hc/en-us/articles/227561407-Crates) are also supported, so your collection is still neatly organized.

If you have USB drives with a [portable Serato library](https://support.serato.com/hc/en-us/articles/202304844-Using-a-USB-external-hard-drive-for-your-portable-library) on it, we've got you covered as well:
Libraries and crates on external USB drives will work on all supported platforms - even on Linux!

![Serato library feature]({static}/images/news/serato-import-library.png)

## Import your Beatgrid and Hotcues

Sorting tracks in your library is important, but preparing [cue points](https://support.serato.com/hc/en-us/articles/226518228-Cue-Points) in tracks is probably the most time-consuming task.
Serato saves them in special file tags along with the other track metadata like title, artist and so on.
It took months of work, but we finally managed to [reverse-engineer the binary formats](https://github.com/Holzhaus/serato-tags) used by Serato to a degree that allow us to parse this information and use it in Mixxx.

This means you can import the positions, labels and [colors of your hotcues]({filename}/news/2020-08-25-new-in-2-3-hotcue-colors.md) into Mixxx automatically when you load the track for the first time.
Mixx will also import the Beatgrid from Serato, which works for both Beatgrid that were automatically detected by Serato's track analyzer and those that you edited manually.

![Beatgrid and Hotcues imported from Serato]({static}/images/news/serato-import-sbs.png)

If you already added a track to your Mixxx library before support for reading Serato's hotcues was added, you can trigger a reimport of the metadata via the track context menu.
Note that this will clear your existing cuepoints in Mixxx if the track has any Serato hotcues.

![Reimport metadata via context menu]({static}/images/news/serato-import-contextmenu.png)

Unfortunately, a myriad of encoders and decoders for lossy formats such as MP3 and M4A/AAC exist, which leads to a situation where all decodes detect slightly different track start and end times for files from different sources.
Hence, your cues might end up shifted by a few milliseconds.

We've done our best to mitigate the problem, but if you experience issues we'd appreciate if you get in touch with us on Zulip and work with us to make the offset correction more accurate.
Additionally, we've added a way to shift all cues for a track at once. This makes it possible to fix the cue positions if Mixxx fails to determine the correct offsets.

## Support for other Serato metadata

Mixxx 2.3 will also import saved loops from Serato, but proper support for saving and restoring loops is scheduled for 2.4.
For the time being, we just import these loops into the Mixxx database and allows using their start position as regular hotcues.
That way, you can start using your loops once 2.4 is out without the need to reimport your metadata (which would undo your cue modifications in Mixxx).
Other Serato metadata that we parse include the [track color]({filename}/news/2020-10-24-new-in-2-3-track-colors.md) and the BPM lock status.

Serato also stores other information like the overview waveform image, but we don't import that information in Mixxx 2.3.
[Serato Flip](https://serato.com/dj/pro/expansions/flip) macros are not imported either, because Mixxx does not support that kind of functionality yet.
This is going to change with [this year's GSoC project by Janek Fischer]({filename}/news/2020-05-05-mixxx-gsoc-projects-2020.md), so hopefully we'll be able to import them in the future.

## Can Mixxx write Serato's Tags?

If you're running our development snapshots, you may have noticed that it's not possible to write cues from Mixxx into Serato metadata tags yet.

At Mixxx, we believe vendor lock-in is a bad thing and that users should be free to use the DJ software they like best.
While these changes allow you to migrate from Serato to Mixxx with less friction we don't want to lock user into Mixxx either.

This means we're looking into adding support for Serato metadata export in upcoming Mixxx releases.
Even for Mixxx-only users this would make it easy to transfer cue points between multiple computers.

We [already](https://github.com/mixxxdj/mixxx/pull/3097) [have](https://github.com/mixxxdj/mixxx/pull/3101) [some](https://github.com/mixxxdj/mixxx/pull/3409) [code](https://github.com/mixxxdj/mixxx/pull/3421) in the pipeline, but since it's a complex undocumented binary-only format we didn't want to rush adding support for writing these tags.
Bugs in the code or misconceptions about the format might lead to data loss and potentially even crash Serato, so extensive testing is necessary.

Hence, it's still uncertain if support for Serato tag export will already land in Mixxx 2.3 - but stay tuned!
