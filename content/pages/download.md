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
        ppa:
          org: mixxx
          name: mixxxbetas
          analytics_conversion: /downloads/2.3.0-beta-ubuntu-ppa
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
        rpmfusion: true
      - slug: source
        name: Source Code
        git_branch: 2.3
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
        ppa:
          org: mixxx
          name: mixxx
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
        rpmfusion: true
      - slug: source
        name: Source Code
        git_branch: 2.2
        git_tag: 2.2.4
        packages:
        - slug: source
          name: Source Code
          url: https://github.com/mixxxdj/mixxx/archive/release-2.2.4.tar.gz
          analytics_conversion: /downloads/2.2.4-linuxsrc
...
