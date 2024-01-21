title: Improved Scrolling Waveform in Mixxx 2.4.0
authors: Maarten de Boer
tags: 2.4, improvements
status: draft
comments: yes
date: 2023-08-15 13:09:47

One of the improvements of Mixxx 2.4 is a rewrite of the scrolling waveforms code. This results in smoother animation at a higher frame rate (60 fps), with less frame-drops and lower CPU load. These improvements are particularly noticeable on macOS, but also apply to Windows and Linux.

The Mixxx scrolling waveforms are drawn with a number of overlapping layers: The beat grid, the looping-, intro- and outro-ranges, the markers, the end-of-track indication, and the actual waveform. Originally these layers were rendered with a combination of Qt (QPainter) and Legacy OpenGL calls, on the now deprecated QGLWidget. Profiling showed that this combination was a performance bottleneck, particularly on macOS. With the rewrite, all these layers are now using Modern OpenGL, with hardware accelerated GLSL shaders. The different waveform types (Simple, Filtered, HSV, RGB and RGB L/R) all come with a GLSL implementation. In addition to the waveforms, the spinny widgets and VU-meters have been rewritten with the same approach.

Visually the new waveforms follow the design of the legacy waveforms, with some minor tweaks (note for example the semi-transparently filled triangles pre- and post track). What has been improved is the layout of the markers layers: Overlapping markers (multiple markers at the same beat grid location) which would previously obfuscate each other, are now automatically placed at an increasing / decreasing vertical position.

The newly implemented waveforms have been beta-tested for quite a while now and are considered stable and recommended. When upgrading from older versions of Mixxx, the GLSL waveform type that best matches the old selection will be selected automatically, as well as the 60 fps frame rate. The legacy waveform types have been maintained as selectable options just in case, in the Waveforms section of the settings dialog.

The deprecated QGLWidget has been replaced by a custom solution using a QOpenGLWindow inside a QWidget using the createWindowContainer() call. Qt also offers QOpenGLWidget to replace QGLWidget, but the QOpenGLWindow solution resulted in better performance and integrated better with the existing source code. This change will also facilitate the migration to Qt 6, planned for Mixxx 2.5.

Finally, a last minute addition is an alternative mode to synchronise the scrolling waveform animation with the display refresh rate, using a so-called phase-locked-loop (PLL), which attempts to track the actual refresh rate and timing automatically. On particular hardware, the default periodic timer-based approach can result in jitter and frame drops and the PLL may gives better results. See [instructions to activate this mode](https://github.com/mixxxdj/mixxx/wiki/Activating-Phase%E2%80%90Locked%E2%80%90Loop-VSync-Mode-for-Scrolling-Waveforms) to activate this mode.
