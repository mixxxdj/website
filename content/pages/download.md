---
title: Download
template: pages/download
versions:
  stable:
    name: 2.3.2
    #release_announcement: /news/xxxx-xx-xx-mixxx-2-3-2-released/
    download_manifest: https://downloads.mixxx.org/releases/2.3.2/manifest.json
    downloads:
      - slug: windows
        os: Windows 7 or later
        packages:
          - slug: win64
            name: 64-Bit
      - slug: macos
        os: macOS 10.12 or later
        packages:
        - slug: macosintel
          name: Intel
      - slug: ubuntu
        os: Ubuntu 18.04 "Bionic Beaver" or later
        text: |
          We provide a [PPA on Launchpad](https://launchpad.net/~mixxx/+archive/mixxx) to make installing install the latest stable version of Mixxx as easy as possible.
          Open a terminal, and enter:

              sudo add-apt-repository ppa:mixxx/mixxx
              sudo apt update
              sudo apt install mixxx

          Using the PPA ensures that new package versions will be installed automatically with `apt`. Otherwise, you can [download individual packages](https://launchpad.net/~mixxx/+archive/ubuntu/mixxx/+packages) and install them manually.
        note: |
          **Note:** Ubuntu also provides a version of Mixxx which can be installed directly from the Ubuntu Software Centre. This version is usually woefully out of date; therefore using the PPA is advised.
      - slug: fedora
        os: Fedora
        text: |
          RPM Fusion builds are maintained by the Mixxx development team. We support the next, the current, and selected previous Fedora release(s) if possible. If you do not have the RPM Fusion repository installed already, before installing Mixxx, run:

              sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm

          Then to install Mixxx:

              sudo dnf install mixxx

          WARNING: GNOME Software defaults to installing an unofficial package from Flathub which does not work with PipeWire yet. This setup is not supported by the Mixxx development team. Install with `dnf` instead.
      - slug: archlinux
        os: Arch Linux
        text: |
          The latest stable version of Mixxx is [available](https://archlinux.org/packages/community/x86_64/mixxx/) in the community repository and can be installed using `pacman`.
          Open a terminal, and enter:

              sudo pacman -S mixxx
      - slug: source
        name: Source Code
        icon: terminal.svg
        text: |
          The Mixxx source code is published under the GNU General Public License (GPL) v2 or later. Please check the `LICENSE` file in our source tree for complete licensing information.

          Download the latest code from Mixxx's `2.3` branch on [GitHub](https://github.com/mixxxdj/mixxx/tree/2.3) by opening a terminal and running:

              git clone -b 2.3 https://github.com/mixxxdj/mixxx.git

          The 2.3.2 release has been [tagged](https://github.com/mixxxdj/mixxx/releases/tag/2.3.2) with `2.3.2`.

          Compilation instructions are available for [Windows](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Windows), [macOS](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Os-X), and [Linux](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Linux).
        packages:
        - slug: source
          name: 2.3 branch
          file_url: https://github.com/mixxxdj/mixxx/archive/2.3.zip
        - slug: source
          name: 2.3.2 release
          file_url: https://github.com/mixxxdj/mixxx/archive/2.3.2.tar.gz
  testing:
    title: Development Snapshots
    text: |
      A great way to contribute to Mixxx is testing the latest code we're working on and giving early feedback. Refer to the [Testing wiki page](https://github.com/mixxxdj/mixxx/wiki/Testing) for where to find the latest builds and instructions how to test pull requests before they are merged.

      **Development snapshots are not intended for live use!** Expect crashes and make sure to back up your Mixxx settings and library before upgrading as explained in the Testing wiki page.
    download_manifest: https://downloads.mixxx.org/snapshots/main/manifest.json
    downloads:
      - slug: windows
        os: Windows 7 or later
        packages:
          - slug: win64
            name: 64-Bit
      - slug: macos
        os: macOS 10.12 or later
        packages:
        - slug: macosintel
          name: Intel
      - slug: ubuntu
        os: Ubuntu 20.04 "Focal Fossa" or later
        text: |
          We provide a [PPA on Launchpad](https://launchpad.net/~mixxx/+archive/ubuntu/nightlies) to make installing the latest development snapshot of Mixxx as easy as possible.
          Open a terminal, and enter:

              $ sudo add-apt-repository ppa:mixxx/nightlies
              $ sudo apt update
              $ sudo apt install mixxx

          Using the PPA ensures that new package versions will be installed automatically with `apt`. Otherwise, you can [download individual packages](https://launchpad.net/~mixxx/+archive/ubuntu/nightlies/+packages) and install them manually.
      - slug: archlinux
        os: Arch Linux
        text: |
          The development version of Mixxx can be [installed](https://aur.archlinux.org/packages/mixxx-git/) from the Arch User Repository (AUR).
          Open a terminal, and enter:

              $ git clone https://aur.archlinux.org/mixxx-git.git
              $ cd mixxx-git
              $ makepkg -si

          Alternatively, you can also use an [AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers) to make the installation more straightforward.
        note: |
          **The AUR is an untrusted source.** Although the `mixxx-git` package is maintained by the Mixxx development team, you should always read the `PKGBUILD` of each AUR package you install to make sure it doesn't contain malicious code.
      - slug: source
        name: Source Code
        icon: terminal.svg
        text: |
          The Mixxx source code is published under the GNU General Public License (GPL) v2 or later. Please check the `LICENSE` file in our source tree for complete licensing information.

          Download the latest code from Mixxx's `main` branch on [GitHub](https://github.com/mixxxdj/mixxx/tree/main) by opening a terminal and running:

              git clone -b main https://github.com/mixxxdj/mixxx.git

          Compilation instructions are available for [Windows](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Windows), [macOS](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Os-X), and [Linux](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Linux).
        packages:
        - slug: source
          name: main branch
          file_url: https://github.com/mixxxdj/mixxx/archive/main.zip
...
