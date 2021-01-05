---
title: Download
template: pages/download
versions:
  unstable:
    name: 2.3.0 Beta
    next_stable_version: 2.3.0
    release_announcement: /news/2020-06-07-mixxx-2-3-beta-released/
    downloads:
      - slug: windows
        os: Windows 7 or later
        packages:
          - slug: windows64
            name: 64-Bit
            url: https://downloads.mixxx.org/builds/2.3/Windows/Mixxx-2.3-latest.msi
      - slug: macos
        os: macOS 10.12 or later
        packages:
        - slug: macosintel
          name: Intel
          url: https://downloads.mixxx.org/builds/2.3/macOS/Mixxx-2.3-latest.dmg
      - slug: ubuntu
        os: Ubuntu 18.04 "Bionic Beaver" or later
        text: |
          We provide a [PPA on Launchpad](https://launchpad.net/~mixxx/+archive/mixxxbetas) to make installing install the latest beta version of Mixxx as easy as possible.
          Open a terminal, and enter:

              $ sudo add-apt-repository ppa:mixxx/mixxxbetas
              $ sudo apt update
              $ sudo apt install mixxx

          Using the PPA ensures that new package versions will be installed automatically with `apt`. Otherwise, you can download individual packages and install them manually.
        note: |
          **Note:** Ubuntu also provides a version of Mixxx which can be installed directly from the Ubuntu Software Centre. This version is usually woefully out of date; therefore using the PPA is advised.
        packages:
        - slug: ubuntu32
          name: 32-Bit
          url: https://downloads.mixxx.org/builds/2.3/release/mixxx-2.3.0-beta-2.3-release-bionic-i386-latest.deb
        - ubuntu64:
          name: 64-Bit
          url: https://downloads.mixxx.org/builds/2.3/release/mixxx-2.3.0-beta-2.3-release-bionic-amd64-latest.deb
      - slug: fedora
        os: Fedora
        text: |
          An [RPM package](https://admin.rpmfusion.org/pkgdb/package/free/mixxx/) for installation is available in the [RPM Fusion](https://rpmfusion.org/) repositories.

          Please refer to [RPM Fusion's instructions](https://rpmfusion.org/Configuration) on how to enable the repositories on your system. Mixxx only requires enabling the free repository; the nonfree repository is not necessary for Mixxx.

          RPM Fusion builds are maintained by the Mixxx development team. We support the next, the current, and selected previous Fedora release(s) if possible.

          The beta package will be continuously updated until Mixxx 2.3.0 is released.
      - slug: archlinux
        os: Arch Linux
        text: |
          The beta version of Mixxx can be [installed](https://aur.archlinux.org/packages/mixxx_beta-git/#comment-783242) from the Arch User Repository (AUR).
          Open a terminal, and enter:

              $ git clone https://aur.archlinux.org/mixxx_beta-git.git
              $ cd mixxx_beta-git
              $ makepkg -si

          Alternatively, you can also use an [AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers) to make the installation more straightforward.
        note: |
          **The AUR is an untrusted source.** Before installing any package from the AUR, always read its `PKGBUILD` to make sure it doesn't contain malicious code. Please note that the `mixxx_beta-git` package is maintained by a third-party contributor, not the Mixxx development team.
      - slug: source
        name: Source Code
        icon: terminal.svg
        text: |
          The Mixxx source code is published under the GNU General Public License (GPL) v2 or later. Please check the `LICENSE` file in our source tree for complete licensing information.

          Download the latest code from Mixxx's `2.3` branch on [GitHub](https://github.com/mixxxdj/mixxx/tree/2.3) by opening a terminal and running:

              git clone -b 2.3 https://github.com/mixxxdj/mixxx.git

          Compilation instructions are available for [Windows](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Windows), [macOS](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Os-X), and [Linux](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Linux).
        packages:
        - slug: source
          name: 2.3 branch
          url: https://github.com/mixxxdj/mixxx/archive/2.3.zip
  stable:
    name: 2.2.4
    release_announcement: /news/2020-06-11-Mixxx-2-2-4-released/
    downloads:
      - slug: windows
        os: Windows 7 or later
        packages:
          - slug: windows32
            name: 32-Bit
            url: https://downloads.mixxx.org/mixxx-2.2.4/mixxx-2.2.4-win32.exe
          - slug: windows64
            name: 64-Bit
            url: https://downloads.mixxx.org/mixxx-2.2.4/mixxx-2.2.4-win64.exe
      - slug: macos
        os: macOS 10.11 or later
        packages:
          - slug: macosintel
            name: Intel
            url: https://downloads.mixxx.org/mixxx-2.2.4/mixxx-2.2.4-osxintel.dmg
      - slug: ubuntu
        os: Ubuntu 16.04 "Xenial Xerus" or later
        text: |
          We provide a [PPA on Launchpad](https://launchpad.net/~mixxx/+archive/mixxx) to make installing install the latest stable version of Mixxx as easy as possible.
          Open a terminal, and enter:

              $ sudo add-apt-repository ppa:mixxx/mixxx
              $ sudo apt update
              $ sudo apt install mixxx

          Using the PPA ensures that new package versions will be installed automatically with `apt`. Otherwise, you can download individual packages and install them manually.
        note: |
          **Note:** Ubuntu also provides a version of Mixxx which can be installed directly from the Ubuntu Software Centre. This version is usually woefully out of date; therefore using the PPA is advised.
        packages:
          - slug: ubuntu32
            name: 32-Bit
            url: https://downloads.mixxx.org/mixxx-2.2.4/mixxx-2.2.4-bionic-i386.deb
          - slug: ubuntu64
            name: 64-Bit
            url: https://downloads.mixxx.org/mixxx-2.2.4/mixxx-2.2.4-bionic-amd64.deb
      - slug: fedora
        os: Fedora
        text: |
          An [RPM package](https://admin.rpmfusion.org/pkgdb/package/free/mixxx/) for installation is available in the [RPM Fusion](https://rpmfusion.org/) repositories.

          Please refer to [RPM Fusion's instructions](https://rpmfusion.org/Configuration) on how to enable the repositories on your system. Mixxx only requires enabling the free repository; the nonfree repository is not necessary for Mixxx.

          RPM Fusion builds are maintained by the Mixxx development team. We support the next, the current, and selected previous Fedora release(s) if possible.
      - slug: archlinux
        os: Arch Linux
        text: |
          The latest stable version of Mixxx is [available](https://archlinux.org/packages/community/x86_64/mixxx/) in the community repository and can be installed using `pacman`.
          Open a terminal, and enter:

              # pacman -S mixxx
      - slug: source
        name: Source Code
        icon: terminal.svg
        text: |
          The Mixxx source code is published under the GNU General Public License (GPL) v2 or later. Please check the `LICENSE` file in our source tree for complete licensing information.

          Download the latest code from Mixxx's `2.2` branch on [GitHub](https://github.com/mixxxdj/mixxx/tree/2.2) by opening a terminal and running:

              git clone -b 2.2 https://github.com/mixxxdj/mixxx.git

          The 2.2.4 release has been [tagged](https://github.com/mixxxdj/mixxx/releases/tag/release-2.2.4) with `release-2.2.4`.

          Compilation instructions are available for [Windows](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Windows), [macOS](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Os-X), and [Linux](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Linux).
        packages:
        - slug: source
          name: 2.2 branch
          url: https://github.com/mixxxdj/mixxx/archive/2.2.zip
        - slug: source
          name: 2.2.4 release
          url: https://github.com/mixxxdj/mixxx/archive/release-2.2.4.tar.gz
  testing:
    title: Development Snapshots
    text: |
      Testing the latest code we're working on and giving early feedback is a great way to contribute to Mixxx. Refer to the [Testing wiki page](https://github.com/mixxxdj/mixxx/wiki/Testing) for where to find the latest builds and instructions how to test pull requests before they are merged.

      **Development snapshots are not intended for live use!** Expect crashes and make sure to [back up your Mixxx settings and library](https://manual.mixxx.org/2.4/en/chapters/getting_started.html#upgrading-mixxx) before upgrading.
    downloads:
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
          **The AUR is an untrusted source.** Before installing any package from the AUR, always read its `PKGBUILD` to make sure it doesn't contain malicious code. Please note that the `mixxx-git` package is maintained by a third-party contributor, not the Mixxx development team.
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
          url: https://github.com/mixxxdj/mixxx/archive/main.zip
...
