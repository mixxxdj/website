title: Mixxx 2.2 released
author: Be.
date: 2018-12-24 18:07:00
comments: no

Mixxx 2.2.0 has been released, [download it!](https://mixxx.org/download/) Since we are now releasing Mixxx more often, the changes are not as big as between Mixxx 2.0 and Mixxx 2.1. Here is a quick overview of the changes since Mixxx 2.1:

#### General

- Update from Qt4 to Qt5.
- Use Qt5's automatic high DPI scaling.
- Vectorize remaining raster graphics for better HiDPI support.

#### Effects

- Add mix mode switch (Dry/Wet vs Dry+Wet) for effect units.
- Add support for LV2 effects plugins (currently no way to show plugin GUIs).
- Add preference option for selecting which effects are shown in the list of available effects in the main window (all LV2 effects are hidden by default and must be explicitly enabled by users).

#### Library

- Text searches without any field qualifiers (such as "title: some-title") now search crates.

#### Skins

- Add 8 sampler and small sampler options to LateNight.
- Add key / BPM expansion indicators to Deere decks.
- Add skin settings menu to LateNight.

#### Controllers

- Add controller mapping for Numark Mixtrack Platinum.
- Update controller mapping for Numark N4.
- Add spinback and break for Vestax VCI-400 mapping.

#### Miscellaneous

- Add preference option to adjust the play position marker of scrolling waveforms.
- Add preference option to adjust opacity of beatgrid markers on scrolling waveforms.
- Support IRC/AIM/ICQ broadcast metadata.

The focus of development for Mixxx 2.2 was switching from Qt 4 to Qt 5. Qt is the toolkit that allows us to write one Mixxx application that runs on Linux, macOS, and Windows. For users, the most noticeable difference from this will be improved support for scaling the graphical user interface (GUI) for high pixel density (high DPI) screens. The scaling we used with Qt 4 in Mixxx 2.1 scaled most parts of the GUI, but some small parts like the arrows on menus and widgets in the preferences did not scale. Now with Qt 5, everything scales automatically according to the operating system scaling settings. Going forward, we will be able to use new features of Qt sooner (for example, [work is ongoing](https://github.com/mixxxdj/mixxx/pull/1795) for supporting ECMAScript 7 in controller scripts). Note that Qt 5 requires Windows 7 or later, so Mixxx 2.2 no longer supports Windows XP and Windows Vista.

We have added a new button to the effects units that adds a new mode for mixing effects. Previously, the mix knob always crossfaded between the dry signal (input to the first effect) and wet signal (output of the last effect). This is now called Dry/Wet mode and is the default. The new Dry+Wet mode always keeps the dry signal at full volume and the mix knob controls how much of the wet signal is added. This allows for adding sounds with effects without modifying the underlying track. For example, with the effect unit in Dry+Wet mode, you can load an equalizer or filter effect before the Echo effect to remove bass frequencies from the echoed signal without removing the bass from the track.

Mixxx 2.2 introduces initial support for LV2 sound effects plugins. Many GNU/Linux distributions package LV2 effects plugins that can be installed separately from Mixxx. Because many LV2 plugins are not useful for DJing, you must explicitly enable plugins in the Effects section of the preferences before you can load them in the Mixxx main window. Currently there is no way to show the GUI for LV2 plugins in Mixxx. While LV2 effects are technically cross-platform, in practice there are very few LV2 plugins that are distributed for macOS and Windows. Mixxx 2.2 has LV2 support enabled for GNU/Linux and macOS, but not for Windows.

Want to help make Mixxx more awesome? We could always use more people, whether you can write code or not. If you are interested in getting involved, join us on our [Zulip chat](https://mixxx.zulipchat.com/) and introduce yourself.
