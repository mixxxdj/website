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
          - slug: win32
            name: 32-Bit
            url: https://downloads.mixxx.org/builds/2.3/release/mixxx-2.3.0-beta-2.3-release-x86-latest.exe
            analytics_conversion: /downloads/2.3.0-beta-win32
          - slug: win64
            name: 64-Bit
            url: https://downloads.mixxx.org/builds/2.3/Windows/Mixxx-2.3-latest.msi
            analytics_conversion: /downloads/2.3.0-beta-win64
      - slug: macos
        os: macOS 10.12 or later
        packages:
        - slug: intel
          name: Intel
          url: https://downloads.mixxx.org/builds/2.3/macOS/Mixxx-2.3-latest.dmg
          analytics_conversion: /downloads/2.3.0-beta-osxintel
      - slug: ubuntu
        os: Ubuntu 18.04 "Bionic Beaver" or later
        text: |
          Open a terminal, and enter:

              sudo add-apt-repository ppa:mixxx/mixxxbetas
              sudo apt update
              sudo apt install mixxx

          This will install the latest version of Mixxx from the [PPA on Launchpad](https://launchpad.net/~mixxx/+archive/mixxxbetas).

          Using the PPA ensures that new package versions will be installed automatically with `apt`. Otherwise, you can download individual packages and install them manually.
        note: |
          **Note:** Ubuntu also provides a version of Mixxx which can be installed directly from the Ubuntu Software Centre. This version is usually woefully out of date; therefore using the PPA is advised.
        packages:
        - slug: ubuntu32
          name: 32-Bit
          url: https://downloads.mixxx.org/builds/2.3/release/mixxx-2.3.0-beta-2.3-release-bionic-i386-latest.deb
          analytics_conversion: /downloads/2.3.0-beta-ubuntu32
        - ubuntu64:
          name: 64-Bit
          url: https://downloads.mixxx.org/builds/2.3/release/mixxx-2.3.0-beta-2.3-release-bionic-amd64-latest.deb
          analytics_conversion: /downloads/2.3.0-beta-ubuntu64
      - slug: fedora
        os: Fedora
        text: |
          An [RPM package](https://admin.rpmfusion.org/pkgdb/package/free/mixxx/) for installation is available in the [RPM Fusion](https://rpmfusion.org/) repositories.

          Please refer to [RPM Fusion's instructions](https://rpmfusion.org/Configuration) on how to enable the repositories on your system. Mixxx only requires enabling the free repository; the nonfree repository is not necessary for Mixxx.

          RPM Fusion builds are maintained by the Mixxx development team. We support the next, the current, and selected previous Fedora release(s) if possible.

          The beta package will be continuously updated until Mixxx 2.3.0 is released.
      - slug: source
        name: Source Code
        text: |
          The Mixxx source code is published under the GNU General Public License (GPL) v2 or later. Please check the LICENSE file in our source tree for complete licensing information.

          Download the latest code from Mixxx's `2.3` branch on [GitHub](https://github.com/mixxxdj/mixxx/tree/2.3) by opening a terminal and running:

              git clone -b 2.3 https://github.com/mixxxdj/mixxx.git

          Compilation instructions are available for [Windows](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Windows), [macOS](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Os-X), and [Linux](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Linux).
        packages:
        - slug: source
          name: Source Code
          url: https://github.com/mixxxdj/mixxx/archive/2.3.zip
  stable:
    name: 2.2.4
    release_announcement: /news/2020-06-11-Mixxx-2-2-4-released/
    downloads:
      - slug: windows
        os: Windows 7 or later
        packages:
          - slug: win32
            name: 32-Bit
            url: https://downloads.mixxx.org/mixxx-2.2.4/mixxx-2.2.4-win32.exe
            analytics_conversion: /downloads/2.2.4-win32
          - slug: win64
            name: 64-Bit
            url: https://downloads.mixxx.org/mixxx-2.2.4/mixxx-2.2.4-win64.exe
            analytics_conversion: /downloads/2.2.4-win64
      - slug: macos
        os: macOS 10.11 or later
        packages:
          - slug: intel
            name: Intel
            url: https://downloads.mixxx.org/mixxx-2.2.4/mixxx-2.2.4-osxintel.dmg
            analytics_conversion: /downloads/2.2.4-osxintel
      - slug: ubuntu
        os: Ubuntu 16.04 "Xenial Xerus" or later
        text: |
          Open a terminal, and enter:

              sudo add-apt-repository ppa:mixxx/mixxx
              sudo apt update
              sudo apt install mixxx

          This will install the latest version of Mixxx from the [PPA on Launchpad](https://launchpad.net/~mixxx/+archive/mixxx).

          Using the PPA ensures that new package versions will be installed automatically with `apt`. Otherwise, you can download individual packages and install them manually.
        note: |
          **Note:** Ubuntu also provides a version of Mixxx which can be installed directly from the Ubuntu Software Centre. This version is usually woefully out of date; therefore using the PPA is advised.
        packages:
          - slug: ubuntu32
            name: 32-Bit
            url: https://downloads.mixxx.org/mixxx-2.2.4/mixxx-2.2.4-bionic-i386.deb
            analytics_conversion: /downloads/2.2.4-ubuntu-bionic32
          - slug: ubuntu64
            name: 64-Bit
            url: https://downloads.mixxx.org/mixxx-2.2.4/mixxx-2.2.4-bionic-amd64.deb
            analytics_conversion: /downloads/2.2.4-ubuntu-bionic64
      - slug: fedora
        os: Fedora
        text: |
          An [RPM package](https://admin.rpmfusion.org/pkgdb/package/free/mixxx/) for installation is available in the [RPM Fusion](https://rpmfusion.org/) repositories.

          Please refer to [RPM Fusion's instructions](https://rpmfusion.org/Configuration) on how to enable the repositories on your system. Mixxx only requires enabling the free repository; the nonfree repository is not necessary for Mixxx.

          RPM Fusion builds are maintained by the Mixxx development team. We support the next, the current, and selected previous Fedora release(s) if possible.
      - slug: source
        name: Source Code
        text: |
          The Mixxx source code is published under the GNU General Public License (GPL) v2 or later. Please check the LICENSE file in our source tree for complete licensing information.

          Download the latest code from Mixxx's `2.2` branch on [GitHub](https://github.com/mixxxdj/mixxx/tree/2.2) by opening a terminal and running:

              git clone -b 2.2 https://github.com/mixxxdj/mixxx.git

          The 2.2.4 release has been [tagged](https://github.com/mixxxdj/mixxx/releases/tag/release-2.2.4) with `release-2.2.4`.

          Compilation instructions are available for [Windows](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Windows), [macOS](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Os-X), and [Linux](https://github.com/mixxxdj/mixxx/wiki/Compiling-On-Linux).
        packages:
        - slug: source
          name: Source Code
          url: https://github.com/mixxxdj/mixxx/archive/release-2.2.4.tar.gz
          analytics_conversion: /downloads/2.2.4-linuxsrc
...
