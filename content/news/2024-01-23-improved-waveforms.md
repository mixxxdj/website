title: Improved Scrolling Waveforms in Mixxx 2.4.0
authors: Maarten de Boer
tags: 2.4, improvements
status: draft
comments: yes
date: 2023-08-15 13:09:47

One of the major improvements of Mixxx 2.4 is an optimization of the scrolling waveforms. This results in smoother animation at a higher frame rate (60 fps), with less frame-drops and lower CPU load.

## Rewrite

The optimization consist of a rewrite not only of the actual waveform drawing, but also of the additional overlapping layers: The beat grid, the looping-, intro- and outro-ranges, the markers and the end-of-track indication. The improvements are particularly noticeable on macOS, but also apply to Windows and Linux. The new waveform types are marked (GLSL) in the Waveforms sections in the settings dialog. When upgrading from older versions of Mixxx, the GLSL waveform type that best matches the old selection will be selected automatically, as well as the 60 fps frame rate.

Visually the new waveforms follow the design of the legacy waveforms, with some minor tweaks. Note for example the semi-transparently filled triangles pre- and post track, which also serves as a quick indication that you are using the new waveforms.

![RGB L/R (GLSL) Waveform type with pre-track trianges]({static}/images/news/glsl-rgb-lr-waveform.png)

While the newly implemented waveforms have been beta-tested for quite a while now and are considered stable and recommended, the old waveform types have been maintained as selectable options just in case, marked as (legacy) in the Waveforms section of the settings dialog, and might be removed in future versions. If you experience issues with the new waveform types, you are encouraged to file a bug report.

## Improved marker layout

An additional improvement is the layout of the markers layer: Overlapping markers (multiple markers at the same beat grid location or sample position) that would previously obfuscate each other, are now automatically placed at an increasing / decreasing vertical position. This applies to (hot) cue markers, intro- and outro-markers and loop-markers, and should be a big improvement for DJs that make heavy use of these markers.

![Overlapping markers drawn at different vertical positions]({static}/images/news/overlapping-markers.png)

## Technical background

Originally the layers that form the scrolling waveform display were rendered with a combination of Qt (QPainter) and Legacy OpenGL calls, on the now deprecated QGLWidget. Profiling showed that this combination was a performance bottleneck, particularly on macOS. With the rewrite, all these layers are now using Modern OpenGL, with hardware accelerated GLSL shaders. The different waveform types (Simple, Filtered, HSV, RGB and RGB L/R) all come with a GLSL implementation. In addition to the waveforms, the spinny widgets and VU-meters have been rewritten with the same approach.

The deprecated QGLWidget has been replaced by a custom solution using a QOpenGLWindow inside a QWidget using the createWindowContainer() call. Qt also offers QOpenGLWidget to replace QGLWidget, but the QOpenGLWindow solution resulted in better performance and integrated better with the existing source code. This change will also facilitate the migration to Qt 6, planned for Mixxx 2.5.

## New display synchronization mode

Finally, a last minute addition is an alternative mode to synchronise the scrolling waveform animation with the display refresh rate, using a so-called phase-locked-loop (PLL), which attempts to track the actual refresh rate and timing automatically. On particular hardware, the default periodic timer-based approach can result in jitter and frame drops and the PLL may gives better results. See [instructions to activate this mode](https://github.com/mixxxdj/mixxx/wiki/Activating-Phase%E2%80%90Locked%E2%80%90Loop-VSync-Mode-for-Scrolling-Waveforms).
