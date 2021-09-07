title: Mixxx 2.3.0 released
authors: Jan Holthuis
tags: 2.3, 2.3.0, release announcement
comments: yes
date: 2021-06-28 18:11:51

We are proud to announce the [release of Mixxx 2.3.0](https://github.com/mixxxdj/mixxx/releases/tag/2.3.0)!
If you want to give it a spin, [you can download it now]({filename}/pages/download.md#stable) on Windows, macOS and Linux.

This release brings a lot of new features and bugfixes:

Prepare your DJ set using [hotcue colors & labels]({filename}/news/2020-08-25-new-in-2-3-hotcue-colors.md), mark [intro/outro sections]({filename}/news/2020-07-09-intro-outro-sections.md) in your tracks and add [track colors]({filename}/news/2020-10-24-new-in-2-3-track-colors.md) for easier library navigation.
Our new multithreaded analysis and [more accurate key detection]({filename}/news/2021-04-08-new-in-2-3-keyfinder.md) will improve the preparation process further.

Mixxx 2.3.0 comes with a new default skin:
"LateNight" underwent a massive redesign and replaces "Deere" as default skin, so check out the [screenshots page]({filename}/pages/screenshots.md).

!["LateNight" is the new default Skin in Mixxx 2.3.0](/theme/images/2.3/screenshots/latenight-palemoon-3840x2160.png)

If you're a Rekordbox or Serato user, switching to Mixxx has become a lot easier:
You can now play tracks directly from USB drives that contain [Rekordbox]({filename}/news/2020-07-20-new-in-2-3-rekordbox-support.md) and [Serato](2021-02-08-new-in-2-3-serato-support.md) libraries.

We also added support for recording/streaming in the [Opus](https://opus-codec.org/) and [HE-AAC](https://www.iis.fraunhofer.de/en/ff/amm/broadcast-streaming/heaac.html) codecs, introduced [deck cloning]({filename}/news/2020-11-15-new-in-2-3-deck-clone.md) and polished the library and preferences (including the controller workflow).

2.3.0 also adds out-of-the-box support for the [Pioneer DDJ-200](https://manual.mixxx.org/2.3/en/hardware/controllers/pioneer_ddj_200.html) and [DDJ-400](https://manual.mixxx.org/2.3/en/hardware/controllers/pioneer_ddj_400.html), the [Native Instruments Traktor Kontrol S3](https://manual.mixxx.org/2.3/en/hardware/controllers/native_instruments_traktor_kontrol_s3.html), the [Hercules DJControl Inpulse 200](https://manual.mixxx.org/2.3/en/hardware/controllers/hercules_djcontrol_inpulse_200.html) and [Jogvision](https://manual.mixxx.org/2.3/en/hardware/controllers/hercules_djcontrol_jogvision.html), the [Roland DJ-505](https://manual.mixxx.org/2.3/en/hardware/controllers/roland_dj_505.html), the [Behringer B-Control BCR2000](https://manual.mixxx.org/2.3/en/hardware/controllers/behringer_bcr2000.html) and [DDM4000](https://manual.mixxx.org/2.3/en/hardware/controllers/behringer_ddm4000.html), the [ION Discover DJ Pro](https://manual.mixxx.org/2.3/en/hardware/controllers/ion_discover_dj_pro.html) and the [Numark iDJ Live II](https://manual.mixxx.org/2.3/en/hardware/controllers/numark_idj_live_ii.html). A few existing controller mappings have received fixes and new features, too.

For the full list of changes, have a look at the [changelog](https://manual.mixxx.org/2.3/en/chapters/appendix/changelog.html) and the [2.3.0 milestone on Launchpad](https://launchpad.net/mixxx/+milestone/2.3.0).

**Note:** Linux users who see broken icons are affected by [a bug in the KDE kIconThemes 5.80 package](https://bugs.kde.org/show_bug.cgi?id=434451). If you don't have a newer version of that package in your repos, yet, see [this comment](https://bugs.launchpad.net/mixxx/+bug/1922966/comments/36) for how to fix the issue.

This has been a rather big release, with lots of useful changes, bug fixes and improvements.
All in all, with a total of 7477 changes over 1 million lines of code were modified since the [2.2.4 release]({filename}/news/2020-06-11-Mixxx-2-2-4-released.md)!

<!-- Numbers acquired using `git shortlog -sn release-2.2.4..upstream/2.3 | wc -l`, `git log --oneline --no-merges release-2.2.4..upstream/2.3 -- . ':!lib' | wc -l` and `git diff --shortstat release-2.2.4..upstream/2.3 -- . ':!lib`. -->

Despite our plans to release Mixxx more often, it's been two years since the 2.2.x release, and 2.3 has been in the beta phase for almost a year now.
The reason for these delays is that we [switched to the CMake build system generator]({filename}/news/2020-12-14-scons-cmake-migration.md), worked on some big refactorings and [infrastructure updates]({filename}/news/2021-02-23-build-infrastructure-updates.md) that were necessary to streamline our process, but also took a lot of time.

Our small development team can always need a helping hand, so if you want to help out and make Mixxx better, [get in touch with us]({filename}/pages/get-involved.md)!
Unfortunately, we receive almost no C++ contributions from Windows or macOS developers despite our large user base on those systems.
Our whole core development team uses Linux, which makes it extremely hard to maintain support for other systems.
Without significantly more contributions, the future of Mixxx on Windows and macOS is at stake.
If you know a bit of C++ and use Windows or macOS, please consider helping out.

Many people spent their free time working on Mixxx and reported bugs, translated Mixxx into other languages, contributed controller mappings, improved skins and hacked on the core code.
This release also features improvements to our manual made by our first intern from the [Outreachy program](https://www.outreachy.org/).
Thanks a lot to all our contributors, we really appreciate it!

The Mixxx code (including skins and controller mappings) has received contributions by almost 100 people:

    $ git log --pretty="format:%an" release-2.2.4..upstream/2.3 | sort -u
    abseits
    Adam Szmigin
    Albert Aparicio Isarn
    Alex
    Alexander Horner
    Balló György
    Be
    beenisss
    Ben
    Be Wilson
    Chris Hills
    Christian
    Christian Wolf
    Codecat
    Cristiano
    Dan Giddins
    Daniel Poelzleithner
    Daniel Schürmann
    David
    David Baker
    David Lowenfels
    David TV
    denvercoder21
    dj3730
    d-j-a-y
    DJ Phatso
    DJPhatso
    Edward Millen
    ehendrikd
    ehmic
    esbrandt
    Evan Dekker
    Fayaaz Ahmed
    Ferran Pujol Camins
    Frank Breitling
    Geovanni Pacheco
    geraldog
    Geraldo Nascimento
    Harshit Maurya
    haslersn
    Ilkka Tuohela
    Jan Holthuis
    Javier Vilarroig
    JoergAtGithub
    JosepMaJAZ
    Josep Maria Antolín Segura
    jusko
    Justin Kourie
    Katsarov
    Kerrick Staley
    ketan-lambat
    luz.paz
    Martin Kirchgessner
    Matthew Nicholson
    Matthieu Bouron
    Matthieu Imbert
    meltedpianoman
    Michael
    Nathan Korth
    naught101
    ned haughton
    Nico Schlömer
    Nik Martin
    nikolas
    Nino Miškić-Pletenac
    Nino MP
    nopeppermint
    NotYourAverageAl
    OsZ
    Owen Williams
    perseo22
    Philip Gottschling
    Pierre Le Gall
    Pino Toscano
    Pradyuman
    Raphael Graf
    Rebecca Wallander
    RJ Ryan
    RJ Skerry-Ryan
    ronso0
    Sanskar Bajpai
    s.brandt
    S.Brandt
    Sean M. Pappalardo
    Sebastien Blaisot
    Sebastien BLAISOT
    Sébastien Blaisot
    Sergey Ukolov
    Simon Harst
    Stefan
    Stéphane L
    Stéphane Lepin
    Swiftb0y
    Thomas
    Timothy Karani
    toszlanyi
    Uwe Klotz
    Valefungo
    Waylon Robertson
    xerus
    xerus2000
    YunQiang Su
    z411
