title: Mixxx 2.2.2 released
author: tapir
date: 2019-08-15 07:06:00
comments: no

{% extends "post.html" %}

{% block post %}

{% load markup %}
{% filter markdown %}

Mixxx 2.2.2 has been released and is available on the [download](https://www.mixxx.org/download/) page.

This release includes many stability and usability fixes. Please note that we had to disable writing of file tags for .ogg files with the current TagLib version 1.11.1 that would otherwise corrupt your precious files. Upgrading from version 2.2.1 is strongly recommended.

#### Changelog

- Fix battery widget with upower <= 0.99.7. #2221
- Fix BPM adjust in BpmControl. lp:1836480
- Disable track metadata export for .ogg files and TagLib 1.11.1. lp:1833190
- Fix interaction of hot cue buttons and looping. lp:1778246
- Fix detection of moved tracks. #2197
- Fix playlist import. lp:16878282
- Fix updating playlist labels. lp:1837315
- Fix potential segfault on exit. lp:1828360
- Fix parsing of invalid bpm values in MP3 files. lp:1832325
- Fix crash when removing rows from empty model. #2128
- Fix high DPI scaling of RGB overview waveforms. #2090
- Fix for OpenGL SL detection on macOS. lp:1828019
- Fix OpenGL ES detection. lp:1825461
- Fix FX1/2 buttons missing Mic unit in Deere (64 samplers). lp:1837716
- Tango64: Re-enable 64 samplers. #2223
- Numark DJ2Go re-enable note-off for deck A cue button. #2087
- Replace Flanger with QuickEffect in keyboard mapping. #2233

{% endfilter %}
{% endblock %}
