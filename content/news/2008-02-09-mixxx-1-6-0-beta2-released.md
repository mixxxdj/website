title: Mixxx 1.6.0 Beta2 Released!
author: Albert
date: 2008-02-09 20:51:00
comments: no

![Mixxx 1.6.0 beta 2 logo]({static}/images/news/mixxx-beta2.png)

We're proud to announce that the **second beta** of Mixxx 1.6.0 **[has been released](http://mixxx.sourceforge.net/download/)**!

Among the **changes** since 1.6.0 beta1:

- Fixed crashes due to vinyl emulation mode
- Improved compatibility with JACK (some users were experiencing choppiness)
- Players should now only pull from the play queue if in NEXT mode
- Search functionality:
  - Search box now selects all text when clicked (easier to make a new search now)
  - When the search box is cleared, the library view will scroll back to it's previous position.
  - Search now properly filters directories out
- Library stuff:
  - Double-clicking on a song now sends the song to the first stopped player.
  - Right-click menu cleaned up, much nicer now
  - Library directory rescans on startup when it's been modified
    (*doesn't work when subdirectories are modified yet)
  - Library view now shows directories first
  - Columns in the library view are proportioned intelligently now
  - Renamed the "Playlist" menu to "Library"
  - Added "Rescan Library" menu item.
  - Can select multiple songs (hold shift) and send them to the play queue or a playlist
- Playlist support:
  - Can create, import, delete, and rename playlists
  - Added "Playlists" to library drop-down box
    - Can right-click to send a playlist to the play queue.
- Fixed some bugs in the track properties dialog, and set default values
- Fixed a soundcard channel selection bug when the second device had more channels than the first.
- Added BPM Schemes (need to make some presets still)
- Minor speed optimization
- [OS X/Leopard package for Intel users!](http://mixxx.sourceforge.net/download.php)
- A few build system (dependency checking) fixes
- MIDI LED control on Linux
- A few MIDI tweaks here and there
- Right-clicking on a knob/slider no longer moves with your mouse (it just centers the value)
- Using your mouse's scroll wheel now changes the values of sliders and knobs (this is cool for laptop users with the little scroll bar at the side of their trackpads)
- DirectSound is now the default API on Windows
- Cleaned up the vinyl control preferences

We've also been working tirelessly on some **other big features** that haven't made it into a release yet:
- [Shoutcast support]({filename}/news/2008-02-01-feature-preview-shoutcast-broadcasting.md)
  (and indirectly, recording support)
- [MixxxScript]({filename}/news/2008-01-05-mixxxscript-sneaky-feature-preview.md)

We're having some trouble sorting out this **JACK/Ubuntu bug**.
A huge number of people can't get JACK to appear in our Sound API selection box on Ubuntu, and this is due to Ubuntu's PortAudio package not being able to find the JACK package when it's being built (I think).
I've been unable to fix this, but someone from Ubuntu Studio told me that they'd have this fixed for Hardy.
However, if someone wants to take a crack at fixing it (because I think there's still a good chance it'll be broken in Hardy if someone doesn't fix it very soon), the details of the problem are [available here](https://bugs.launchpad.net/mixxx/+bug/183011).

Once again, you can pick up Mixxx 1.6.0 beta 2 on our [downloads page](http://www.mixxx.org/download/), and be sure to report any bugs you find in our [bug tracker](https://bugs.launchpad.net/mixxx/).
Your feedback from beta 1 helped us identify the big issues people were having, and helped us make this release even better - thank you!
