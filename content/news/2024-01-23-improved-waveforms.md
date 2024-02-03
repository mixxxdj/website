title: Improved Scrolling Waveforms in Mixxx 2.4.0
authors: Maarten de Boer
tags: 2.4, improvements
status: draft
comments: yes
date: 2023-08-15 13:09:47

One of the major improvements in Mixxx 2.4 is a revision of the scrolling waveform implementation, to achieve smoother animation at a higher frame rate (60 fps), with fewer frame-drops and a lower CPU load.

## Rewrite

The revision consists of an optimized rewrite, not only of the actual waveform drawing, but also of the additional overlapping layers, i.e., the beat grid, the looping-, intro- and outro-ranges, the markers and the end-of-track indication. The improvements apply to all supported platforms and are particularly noticeable on macOS. The new waveform types are marked "(GLSL)" in the Waveforms section in the settings dialog. When upgrading from older versions of Mixxx, the GLSL waveform type that best matches the old configuration will be selected automatically, as well as a frame rate of 60 fps.

Visually, the new waveforms follow the design of the legacy waveforms, with some minor tweaks. Note for example the semi-transparently filled triangles pre- and post track. This also serves as a quick indication that you are using the new waveforms.

![RGB L/R (GLSL) Waveform type with pre-track trianges]({static}/images/news/glsl-rgb-lr-waveform.png)

The newly implemented GLSL waveforms have been beta-tested for several months now and are considered stable and recommended. The old waveform types remain available, just in case, as an option in the Waveforms section of the settings dialog, marked with "(legacy)", and might be removed in future versions. If you experience issues with the new waveform types, you are encouraged to file a bug report!

## Improved marker layout

Additionally, the markers layer has been improved: Multiple markers at the same beat grid location or sample position that would previously overlap and obscure each other, are now automatically stacked, placed at a respectively increased or decreased vertical offset. This applies to (hot) cue markers, intro- and outro-markers and loop-markers, and should be a big improvement for DJs that make heavy use of these markers.

![Overlapping markers drawn at different vertical positions]({static}/images/news/overlapping-markers.png)

## Some technical insights

Mixxx uses the Qt software framework for its user interface. Originally the layers that form the scrolling waveform display were rendered on the now deprecated QGLWidget through a combination of 'QPainter' and Legacy OpenGL function calls. Profiling showed that this combination was a performance bottleneck, particularly on macOS.

With the rewrite, all the layers mentioned above are now implemented using Modern OpenGL code: All different waveform types, i.e, Simple, Filtered, HSV, RGB and RGB L/R, are now hardware accelarated using GLSL shaders. In addition to the waveforms, the spinny widgets and VU-meters code has been revised with the same approach.

The deprecated QGLWidget has been replaced by a custom solution using a QOpenGLWindow inside a QWidget using the createWindowContainer() call. Qt also offers QOpenGLWidget to replace QGLWidget, but the QOpenGLWindow solution resulted in better performance and integrated better with the existing source code. This change will also facilitate the migration to Qt 6, planned for Mixxx 2.5.

## New display synchronization mode

Finally, a last minute addition is an alternative mode to synchronise the scrolling waveform animation with the display refresh rate, using a so-called phase-locked-loop (PLL). This mechanism attempts to track the actual refresh rate and timing of the display automatically. On particular hardware, the default periodic timer-based approach can result in jitter and frame drops, and the PLL may give better results. The PLL has been made the default on macOS. See [instructions to change the V-Sync mode](https://github.com/mixxxdj/mixxx/wiki/Changing-the-VSync-Mode-for-Scrolling-Waveforms) if you want to try which mode works best for you.
