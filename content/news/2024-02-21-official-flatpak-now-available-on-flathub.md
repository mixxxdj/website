title: Official Flatpak now available on Flathub
authors: Be.
comments: yes

An unofficial Mixxx Flatpak package for Linux users has been available on Flathub since Mixxx 2.2.1. Today, all major technical issues with the Flatpak have been resolved, so we have decided to officially support this Flatpak package with [Mixxx 2.4.0](/news/2024-02-16-mixxx-2-4-0-features) and verify [Mixxx on Flathub](https://flathub.org/apps/org.mixxx.Mixxx).

In the past, upstream Mixxx builds for Linux users have only been available on Ubuntu via a PPA. Now, this Flatpak brings upstream builds maintained by the Mixxx developers directly to users on all Linux distributions. The Ubuntu PPA is still maintained. If the PPA or a package from your distribution is up to date and works for you, there is no need to switch to the Flatpak.

### Migrating to Flatpak

If you do want to switch from a distribution package or Mixxx built from source code to the Flatpak, a little setup is required. Flatpak stores Mixxx's database, settings, and custom controller mappings in a different location than the `~/.mixxx` directory that Mixxx has always used before. Flatpak uses `~/.var/app/org.mixxx.Mixxx/.mixxx` instead. To copy your database, settings, and controller mappings into the Flatpak sandbox, run:

```
mkdir -p ~/.var/app/org.mixxx.Mixxx
cp -r ~/.mixxx ~/.var/app/org.mixxx.Mixxx
```

If your library contains any directories outside of your XDG Music Directory (`~/Music` unless you have reconfigured this), you will need to relink these directories to access the files inside of Flatpak's sandbox. Run Mixxx from the Flatpak and go to Options > Preferences > Library. Any directories that have a warning icon with `!` in a yellow triangle need to be relinked. Select the directory in the preferences window and click the Relink button, then select the directory in the file picker dialog. Flatpak will automatically remap the directory under `/run/user` so Mixxx can read and write your music files from inside the Flatpak sandbox. Press Ok in the preferences window, then in Mixxx's main window, go to Library > Rescan Library.

### Technical requirements

Using the JACK sound API for audio input and output with the Flatpak requires running Pipewire with JACK support outside the Flatpak sandbox. Most distributions now install Pipewire configured as an audio server by default as a replacement for PulseAudio. However, Pipewire-JACK might not be installed by default and may need to be installed from your distribution package manager.

If your distribution uses systemd, the Mixxx Flatpak requires a recent version of systemd to use HID controllers. A [bug fix](https://github.com/systemd/systemd/pull/30611) for this has been backported to systemd stable versions from 252 and later. If your distribution, for example [Ubuntu 22.04](https://packages.ubuntu.com/jammy-updates/systemd), has an older version of systemd, HID controllers will not work with the Flatpak by default. You can work around this by copying [this udev rule file](https://raw.githubusercontent.com/mixxxdj/mixxx/main/res/linux/mixxx-usb-uaccess.rules) to `/usr/lib/udev/rules.d/` and rebooting.
