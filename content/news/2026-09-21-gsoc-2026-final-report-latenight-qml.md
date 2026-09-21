---
title: "Final GSoC 2026 Report: Rebuilding the LateNight Theme in QML"
authors: Ayush Sah (arsenic)
tags: gsoc, gsoc-2026, development, UI, QML, LateNight
comments: yes
summary: A final report on rebuilding Mixxx's LateNight skin in QML, from the legacy library bridge to native decks, mixer, effects, samplers, Mic/Aux, menus, responsive layouts, and waveform work.
---

<!-- DRAFT: Add final screenshots/video and update the publication date before publishing. -->

Disclaimer: *The blog post primarily serves as the documentation for the [Google Summer of Code](https://summerofcode.withgoogle.com/programs/2026/projects/kEDmkJTi) 2026 project: "Rebuilding the LateNight Theme in QML". Thus, it contains a lot more detailed description than the other Mixxx blog posts.*

Hi everyone! I am Ayush Sah (arsenic), and I am back with the final report for my Google Summer of Code (GSoC) 2026 project with Mixxx.

In my [introductory post](https://mixxx.org/news/2026-06-06-gsoc-2026-rebuild-latenight-qml/), I described the plan to rebuild Mixxx’s iconic LateNight skin in native QML. The motivation was simple: preserve the dense, familiar LateNight experience that makes the skin useful to DJs while moving its presentation and interaction layer to a more flexible and modern UI technology.

The introductory post described a 12-week implementation plan. The project ultimately ran for 16 weeks, giving enough time to take the initial shell through the major LateNight workflows and the shared infrastructure needed to support them.

The result is a substantially complete LateNight QML interface with native QML decks, waveform integration and controls, toolbar, mixer, effects rack, samplers, microphone and auxiliary-input racks, menus, responsive deck layouts, and the theme infrastructure needed for Classic and PaleMoon styling.

The short version is that the original goal was not just to make a new skin that merely looked like LateNight. The aim was also to make the LateNight workflow available in QML, with the same controls, states, layouts, and visual language wherever the scope allowed.

You can take a look at the video below to see LateNight QML in action:

@Video(https://www.youtube.com/watch?v=sjlBAVZFUqQ)

## From a bridge to a working skin

The first milestone was deliberately modest. It introduced the QML skin shell and the `QmlLegacyLibraryItem`, a bridge that hosts the existing QWidget-based Library inside the QML scene.

That bridge was important for two reasons. It made the experimental skin usable early in the project and let the rest of the interface be ported incrementally while keeping the Library in its existing QWidget implementation. It also exposed a number of details that are easy to miss when porting a skin: scrollbar and header behavior, sorting, search input, keyboard focus, drag-and-drop, splitters, preview controls, palette changes, and repaint scheduling.

The Library, its cover art and preview deck components, and the Preferences dialog remain deliberate QWidget transition boundaries in the current scope. Work on the wider New UI is progressing: the native Library and Settings work is underway, while the [interim QWidget bridge for the preview deck and cover art is in progress](https://github.com/mixxxdj/mixxx/pull/17099). Native QML replacements for those components remain follow-up work.

Once the bridge was stable, the work could proceed from the outside in. LateNight-specific composition lives in `res/skins/LateNightQML`, while generic infrastructure was added to Mixxx’s shared `res/qml` layer. Splitting these layers makes the project more than a one-off skin port. It provides building blocks for future skin ports and independent skin implementations: developers of custom skins can move toward QML and use LateNight QML as a reference, building on shared controls, action proxies, effect infrastructure, and input behaviors instead of starting every skin from scratch.

## Screenshots of LateNight QML: PaleMoon and Classic

<figure style="display: flex; flex-direction: column; align-items: center;">
  <a href="{static}/images/news/latenight-qml-palemoon.png">
    <img src="{static}/images/news/latenight-qml-palemoon.png" alt="LateNight QML PaleMoon">
  </a>
  <div style="font-size: small; margin: 5px 0; font-weight: normal;">
    LateNight QML PaleMoon
  </div>
  <a href="{static}/images/news/latenight-palemoon.png">
    <img src="{static}/images/news/latenight-palemoon.png" alt="LateNight PaleMoon">
  </a>
  <figcaption style="font-size: small; margin-top: 5px; font-weight: normal;">
    LateNight PaleMoon
  </figcaption>
</figure>

<figure style="display: flex; flex-direction: column; align-items: center;">
  <a href="{static}/images/news/latenight-qml-classic.png">
    <img src="{static}/images/news/latenight-qml-classic.png" alt="LateNight QML Classic">
  </a>
  <div style="font-size: small; margin: 5px 0; font-weight: normal;">
    LateNight QML Classic
  </div>
  <a href="{static}/images/news/latenight-classic.png">
    <img src="{static}/images/news/latenight-classic.png" alt="LateNight Classic">
  </a>
  <figcaption style="font-size: small; margin-top: 5px; font-weight: normal;">
    LateNight Classic
  </figcaption>
</figure>

## Styling changes

The styling work focused on the places where QML could preserve the LateNight experience while making the interface clearer or more space-efficient.

### Toolbar

The old “Settings” button was removed from the toolbar. It was a long-standing discoverability issue: a small button acted as the entry point for skin and layout settings, but its purpose was not clear to new users and its behavior was often discovered only by accident. Users might also confuse it with the application Preferences entry, which was available from the menu bar. The relevant skin and layout settings are now exposed through dropdowns next to the toolbar sections. These dropdowns are implemented as overlays, so they can open over the skin without forcing the rest of the layout to move. This keeps the toolbar compact while making its controls easier to discover.

<figure style="display: flex; flex-direction: column; align-items: center;">
  <video controls preload="metadata" style="max-width: 100%; height: auto;">
    <source src="{static}/images/news/latenight-qml-toolbar.mp4" type="video/mp4">
    Your browser does not support embedded videos.
  </video>
  <figcaption style="font-size: small; margin-top: 5px; font-weight: normal;">
    Toolbar layout and skin controls in LateNight QML
  </figcaption>
</figure>

On platforms and desktop environments that use an in-window menu bar, including Windows and some Linux desktop environments, the in-window menu bar is replaced by a hamburger button in the toolbar. The button opens the main menu as an overlay, so the menu itself does not add another layout row or push the decks, mixer, or Library out of place. In the legacy layout, users could reclaim the menu bar’s vertical space only by hiding it. On desktop environments that provide a native application menu, such as macOS and some Linux desktop setups, actions continue to use that system menu.

<figure style="display: flex; flex-direction: column; align-items: center;">
  <video controls preload="metadata" style="max-width: 100%; height: auto;">
    <source src="{static}/images/news/latenight-qml-windows-hamburger-menu.mp4" type="video/mp4">
    Your browser does not support embedded videos.
  </video>
  <figcaption style="font-size: small; margin-top: 5px; font-weight: normal;">
    Hamburger Menu in action
  </figcaption>
</figure>

### Waveform stem and beatgrid control overlays

The waveform reskin places stem and beatgrid controls over the waveform. This was a problem in the legacy layout, while QML allows controls to be positioned over other elements without changing their geometry. The split-stem display and its states are now styled as part of the waveform surface. The implementation also restores the backgrounds, markers, gutters, separators, splitters, and filter-menu sizing needed to make the waveform area feel like LateNight while keeping both control sets available without introducing another layout row.

<figure style="display: flex; flex-direction: column; align-items: center;">
  <video controls preload="metadata" style="max-width: 100%; height: auto;">
    <source src="{static}/images/news/latenight-qml-stem-beatgrid-overlay.mp4" type="video/mp4">
    Your browser does not support embedded videos.
  </video>
  <figcaption style="font-size: small; margin-top: 5px; font-weight: normal;">
    Stem and beatgrid controls are displayed as overlays on the waveform
  </figcaption>
</figure>

### Effects Rack space saving

The effects rack supports a space-saving arrangement in which Effects 1 and 4 can remain compact while Effects 2 and 3 are open, and vice versa. This keeps the parameter-rich middle of the rack accessible without making the whole interface unnecessarily tall.

<figure style="display: flex; flex-direction: column; align-items: center;">
  <a href="{static}/images/news/latenight-qml-effects-1-4.png">
    <img src="{static}/images/news/latenight-qml-effects-1-4.png" alt="Effects 1 and 4 open in LateNight QML">
  </a>
  <figcaption style="font-size: small; margin-top: 5px; font-weight: normal;">
    Effects 1 and 4 open while Effects 2 and 3 remain compact
  </figcaption>
</figure>

<figure style="display: flex; flex-direction: column; align-items: center;">
  <a href="{static}/images/news/latenight-qml-effects-2-3.png">
    <img src="{static}/images/news/latenight-qml-effects-2-3.png" alt="Effects 2 and 3 open in LateNight QML">
  </a>
  <figcaption style="font-size: small; margin-top: 5px; font-weight: normal;">
    Effects 2 and 3 open while Effects 1 and 4 remain compact
  </figcaption>
</figure>

### 64 samplers without a separate skin

The legacy widget-based LateNight implementation is split into two skins because sampler count affects startup time. `LateNight` starts Mixxx with 16 samplers, while `LateNight (64 Samplers)` starts it with 64 and includes the additional static sampler-row hierarchy. Initializing that larger hierarchy creates and configures far more sampler controls and their UI at startup, even when most of the rack is collapsed. Keeping the 64-sampler layout in a separate skin meant that DJs who did not need it did not pay that startup cost.

LateNight QML brings these choices into one skin, exposing 4, 8, 16, 32, 48, and 64 samplers without constructing every expanded sampler at once. It creates the compact rows for the selected count, then caches and warms expanded content one row at a time. The higher sampler count still needs its underlying Mixxx sampler channels, but QML avoids eagerly building the entire expanded visual rack. This keeps the larger layout manageable while preserving the rest of the interface, and removes the need to choose between separate LateNight skins.

<figure style="display: flex; flex-direction: column; align-items: center;">
  <a href="{static}/images/news/latenight-qml-64-samplers.png">
    <img src="{static}/images/news/latenight-qml-64-samplers.png" alt="64-sampler layout in LateNight QML">
  </a>
  <figcaption style="font-size: small; margin-top: 5px; font-weight: normal;">
    LateNight QML displaying the 64-sampler layout
  </figcaption>
</figure>

## Startup experience and performance improvements
*As of 20th September, 2026.*

Performance work covered two parts of the experience: startup and responsiveness after loading. The measurements came from three repeated launches on a MacBook Air with Apple’s M2 chip (macOS ARM64), using a Release Qt 6.10.3 build with `LateNightQML` enabled through `--developer`.

### Startup experience

Each run started from a temporary copy of the same frozen Mixxx profile: a prepared, unchanged snapshot of the settings, local tracks, analysis data, display configuration, and audio device. These are repeated-launch measurements rather than cold-boot results.

The first startup frame was submitted in under 2 seconds. The base LateNight QML layout was constructed within about 11 seconds, while the remaining startup work continued preparing sampler content before the loading overlay was removed. This longer preparation phase does not represent the time before Mixxx first begins rendering. The median time until the LateNight QML interface became visible was **78.96 seconds**, and every measured launch completed in under 2 minutes.

| Benchmark event                  | What it means in Mixxx                                            |       Measured time |
| -------------------------------- | ----------------------------------------------------------------- | ------------------: |
| First submitted frame            | Mixxx produced its first startup frame                            |   0.74–1.63 seconds |
| `MainWindow` component completed | Base LateNight QML layout was constructed                         |  9.61–10.69 seconds |
| Outer `Loader.Ready`             | Main LateNight QML component finished loading                     | 42.03–79.21 seconds |
| `visible_content_ready`          | Startup overlay removed and LateNight QML interface became visible | 45.97–84.21 seconds |

<div class="performance-metrics" markdown="1">

### Frame Metrics

Once loaded, the Library became the main performance concern in this capture. LateNight QML currently displays the Library through a legacy QWidget hierarchy rendered offscreen by `QmlLegacyLibraryItem`, so repeated Library redraws cross a bridge between the legacy widget path and QML. The frame timings record when Mixxx produced frames, not when they appeared on the display or how long the GPU took. This was an idle loaded-state capture, so it does not support claims about waveform smoothness during active playback. Waveform rendering did not stand out as the main CPU cost here: `updatePaintNode` was negligible, while repeated Library bridge work used much of the 16.67 ms main-thread budget and the first Library render was substantially more expensive. This highlights the importance of a native QML Library.

#### Frame timing measurements

| Metric | Value |
| ------ | ----- |
| Frame counts | <ul><li>Frames measured: 442</li><li>Intervals measured: 441</li></ul> |
| Effective rate | <ul><li>91.74 FPS</li></ul> |
| Frame intervals | <ul><li>Median: 11.49 ms</li><li>p95: 24.30 ms</li><li>p99: 27.64 ms</li><li>Maximum: 108.21 ms</li></ul> |
| Over 16.67 ms | <ul><li>91 of 441 intervals exceeded 16.67 ms</li><li>4 exceeded 33.33 ms</li><li>2 exceeded 50 ms</li></ul> |

#### Library bridge

| Metric | Value |
| ------ | ----- |
| During capture | <ul><li>Render requests: 1,030</li><li>Coalesced requests: 723</li></ul> |
| `update_polish` | <ul><li>Samples: 306</li><li>Median: 10.83 ms</li><li>p95: 12.12 ms</li><li>p99: 12.25 ms</li><li>Maximum: 12.47 ms</li></ul> |
| Over 16.67 ms | <ul><li>0 `update_polish` samples</li></ul> |
| Whole process | <ul><li>326 Library bridge renders</li></ul> |

#### Waveform and GUI

| Metric | Value |
| ------ | ----- |
| `updatePaintNode` | <ul><li>Samples: 442</li><li>p95: 0.01 ms</li><li>Maximum: 0.01 ms</li></ul> |
| GUI-thread timing signal | <ul><li>Records how late the GUI thread handled the timing check</li><li>p95 lateness: 11.78 ms</li><li>Maximum: 118.22 ms</li></ul> |
| Over 16.67 ms | <ul><li>`updatePaintNode`: 0 samples</li><li>GUI-thread timing: 9 checks</li></ul> |
| Over 33.33 ms | <ul><li>GUI-thread timing: 3 checks</li></ul> |

#### Initial Library-render capture

| Metric | Value |
| ------ | ----- |
| First Library `update_polish` | <ul><li>Maximum 85.08 ms</li></ul> |
| Frame intervals | <ul><li>p95: 46.83 ms</li><li>Maximum: 579.95 ms</li></ul> |
| Over 16.67 ms | <ul><li>49 of 95 frame intervals</li></ul> |

</div>

## Reaching parity within the GSoC scope

Parity within the project scope was the main acceptance criterion. It meant more than matching a screenshot; the major LateNight workflows had to remain available and behave consistently.

The LateNight QML surface now covers:

- Deck playback, track actions, waveform and overview displays, rate and pitch controls, vinyl-style controls, key controls, hotcues, cue editing, intro/outro cues, loops, beatjumps, beat sizes, and beatgrid-related controls.
- Toolbar settings indicators, menu actions, skin settings, and platform-aware application menus.
- Two- and four-deck layouts with Full, Compact, and Mini variants, responsive sizing, and transitions between layout states.
- A mixer with two- and four-deck configurations, gain, EQ, kill switches, quick effects, filters, volume, metering, PFL, output and headphone routing, effects routing, and crossfader assignment.
- An effects rack with two- and four-unit configurations, collapsed and expanded layouts, effect selectors, presets, parameters, assignments, persisted visibility, and the Super Knob.
- Sampler racks with sampler-count choices from 4 to 64, compact and expanded states, playback controls, hotcues, waveforms, effects, PFL, gain, VU, sync, pitch, and expansion behavior.
- Microphone and auxiliary-input racks with configured and unconfigured states, up to four units of each type, talkover and ducking, pregain, PFL, effects, VU metering, main-mix routing, and crossfader assignment.
- Responsive library arrangements and layout transitions that make the skin usable at different window sizes.

This is feature and visual parity for the intended LateNight QML scope, not a claim that every Mixxx interface surface already has a native QML implementation. The remaining QWidget boundaries are intentional: the Library and Preferences migrations for the New UI are underway, while the interim Preview deck and cover-art bridge is in progress and native QML replacements remain to be ported.

## New work in `res/qml`

Beyond the skin itself, the project added generic QML infrastructure to Mixxx’s shared `res/qml` layer for features that were not previously available there as reusable components. This includes functionality added to the wider New UI, not only LateNight QML-specific layout code. These components give LateNight QML and future custom skins a common foundation to build on, preventing the same infrastructure from being implemented separately in each skin. See the [detailed breakdown of the `res/qml` contributions below](#new-work-in-resqml).

Work on the New UI Settings window has extended this migration. Antoine's open [waveform-settings work](https://github.com/mixxxdj/mixxx/pull/15381) fills in the remaining waveform controls. In the New UI, the legacy Interface page is hidden to avoid presenting duplicate or misleading settings that do not apply to the new skin, while the Preferences action remains available through the application menu.

The merged waveform work extends the shared QML Settings infrastructure used by the New UI: it moves waveform preferences into a dedicated Waveforms page and connects those shared settings to active QML scrolling and overview waveforms. It supports waveform type, zoom, visual gain, stem, marker, and related overview settings, refreshing renderer stacks when renderer-affecting options change. Overview waveform caching remains unchanged, and analyzer status and progress reporting are retained without progressive waveform repainting. Some settings are intentionally unavailable in the current QML renderer: the frame-rate control is hidden, and the legacy High Detail setting is disabled because it is not supported by the QML scene-graph renderer. Adding High Detail rendering to the SceneGraph backend is tracked in [issue #14990](https://github.com/mixxxdj/mixxx/issues/14990). Split stereo signal is available only when the RGB waveform renderer is selected.

<figure style="display: flex; flex-direction: column; align-items: center;">
  <video controls preload="metadata" style="max-width: 100%; height: auto;">
    <source src="{static}/images/news/latenight-qml-waveform-settings.mp4" type="video/mp4">
    Your browser does not support embedded videos.
  </video>
  <figcaption style="font-size: small; margin-top: 5px; font-weight: normal;">
    Waveform Settings in LateNightQML
  </figcaption>
</figure>

The deck port led to reusable button, cycle-control, overview-marker, hotcue, intro/outro, beat-size, beatgrid, and marker behaviors. Key formatting and harmonic-display support was exposed to QML and is used by the deck key display and the key-color indicator logic.

The control layer gained reusable QML knobs, faders, orientation controls, relative dragging, right-click reset behavior, slider-bar settings, and backend proxies for toolbar state. These pieces keep interaction behavior in one place instead of reimplementing it in every skin component. The `SkinControlCreator` infrastructure also lets QML skins create their own [Mixxx Control Objects (COs)](https://manual.mixxx.org/2.5/en/chapters/appendix/mixxx_controls.html), including `[Skin]`-prefixed objects. It retains the control names expected by existing controller mappings while tying their creation, persistence, and lifetime to QML components. This makes skin-control lifetime explicit while preserving controller-mapping compatibility.

Larger surfaces also benefited from shared infrastructure. Application-menu and action proxies connect QML menus to Mixxx commands and dialogs. Effects infrastructure provides effect selectors, presets, parameter controls, routing, and tests. Reusable sampler, microphone, auxiliary-input, and ducking components keep rack implementations consistent while allowing the LateNight layout to control their presentation.

Finally, the project added QML-focused validation and CI smoke coverage. These checks help catch regressions and ensure that the interface is tested as a first-class Mixxx UI rather than as a special demo mode.

## Challenges and lessons learned

Porting a dense, mature skin showed that visual parity depends on interaction details as much as on geometry. A control can look correct and still feel wrong if its focus behavior, state indicator, reset action, or relationship with the rest of the layout is different from what existing users expect.

The largest practical challenge was coordinating QML state with Mixxx’s existing control and preference systems while the interface was being rebuilt piece by piece. The mixed QWidget and QML boundary was most visible in areas such as focus, menus, splitters, palette changes, and repaint behavior. The sampler rack presented a similar challenge at a different scale: high sampler counts needed to remain usable without constructing every expanded view at once.

The project reinforced two architectural lessons: keep reusable behavior in shared `res/qml` components, and give an experimental interface production-minded checks. Theme validation, startup smoke tests, explicit fallback behavior, and testing across layouts make the result easier for the wider Mixxx community to review and continue.

## Protecting user data

Most of this project changes presentation and runtime controls, but several surfaces can affect persistent user data. The main risks were accidental changes to the Library or track metadata, invalid saved preferences, and automated tests running against a real user profile. The mixer, effects, samplers, and styling work do not introduce direct paths for writing to audio files or the Library database.

For the Library, the project kept the established QWidget implementation behind `QmlLegacyLibraryItem` instead of rewriting collection storage at the same time as the skin. QML menu and deck actions go through Mixxx’s existing Library and player backends, with [Mixxx Control Objects (COs)](https://manual.mixxx.org/2.5/en/chapters/appendix/mixxx_controls.html) accessed through `ControlProxy`, rather than a skin-specific persistence layer. The File menu asks for confirmation before replacing a track on a playing deck, while shared drop handling ignores empty URLs and prevents a deck from being dropped onto itself.

Hotcue labels, colors, types, and clear actions can alter saved track metadata. The QML controls use the existing cue and control APIs, reject missing tracks, cues, or invalid cue positions, close the editor if the loaded track changes, and suppress keyboard mappings while label text is being edited. The clear action is a separate explicit control in the hotcue popup rather than part of ordinary cue triggering. Focused tests cover the new proxy and cue-direction behavior.

Preferences carry a separate risk because invalid values could persist across sessions. The waveform-preferences work stages edits until the user selects Save, provides Cancel and Reset paths, constrains values in the interface, and sanitizes supported ranges before they reach the configuration. Settings unsupported by the QML renderer are hidden or disabled instead of being silently applied.

Finally, the QML startup smoke tests use an isolated temporary profile, a no-audio configuration, and offscreen rendering, so they do not run against a user’s normal settings or Library. LateNight QML also remains explicitly marked as experimental and is only exposed from developer mode while this wider testing continues.

## Testing and validation

Validation combined automated checks with manual testing. Theme colors and SVG assets have dedicated validation, the shared effects infrastructure includes tests, and the QML skin has a startup smoke-test path in CI. These checks catch malformed assets, missing QML registrations, and regressions that are easy to overlook when the main focus is visual work.

Manual testing focused on both color schemes, two- and four-deck layouts, different window sizes, high sampler counts, effects routing, library searches, track actions, and switching between the legacy skin and LateNight QML. The remaining issues collected under the LateNight QML triage label point to areas where broader hardware, platform, display-scale, and accessibility testing is still needed. Representative issues and the full label are listed in the Future work and known issues section below.

## Trying LateNight QML

LateNight QML will be available to everyone as an experimental skin in Mixxx 2.7. As of today, you can try it in a current developer build.  Start Mixxx with the developer flag:

```text
./build/mixxx --developer
```

Then open:

```text
Preferences → Interface → LateNight QML (Experimental)
```

The Classic and PaleMoon schemes can be selected from the QML interface preferences. For a meaningful trial, compare both schemes with the legacy skin across the layouts and workflows that matter to you.

## Pull requests

The following list records the merged project work as of 21 September 2026. It includes 42 merged project contributions. In-progress and planned LateNight QML work is listed separately below.

### Feature PRs

| PR | Status | Contribution |
|---|---|---|
| [#16489](https://github.com/mixxxdj/mixxx/pull/16489) | Merged | Introduces LateNight QML and embeds the legacy Library via a QML bridge. |
| [#16555](https://github.com/mixxxdj/mixxx/pull/16555) | Merged | Adds Classic/PaleMoon color schemes and theme infrastructure. |
| [#16598](https://github.com/mixxxdj/mixxx/pull/16598) | Merged | Adds the first native QML deck structure, controls, waveforms, and settings. |
| [#16687](https://github.com/mixxxdj/mixxx/pull/16687) | Merged | Implements the LateNight QML toolbar and its bindings and styling. |
| [#16691](https://github.com/mixxxdj/mixxx/pull/16691) | Merged | Adds deck track actions, waveform styling, beatgrids, vinyl/pass visuals, and rate controls. |
| [#16850](https://github.com/mixxxdj/mixxx/pull/16850) | Merged | Adds the platform-aware menu bar and hamburger menu. |
| [#16858](https://github.com/mixxxdj/mixxx/pull/16858) | Merged | Implements the two- and four-deck mixer, routing, and monitoring controls. |
| [#16884](https://github.com/mixxxdj/mixxx/pull/16884) | Merged | Implements the LateNight QML effects rack and effect-chain controls. |
| [#16936](https://github.com/mixxxdj/mixxx/pull/16936) | Merged | Adds sampler-count choices up to 64 samplers. |
| [#16937](https://github.com/mixxxdj/mixxx/pull/16937) | Merged | Implements the LateNight QML sampler racks and high-count handling. |
| [#16962](https://github.com/mixxxdj/mixxx/pull/16962) | Merged | Implements the microphone and auxiliary-input racks. |
| [#17001](https://github.com/mixxxdj/mixxx/pull/17001) | Merged | Completes hotcues, cue editing, intro/outro controls, loops, beatjumps, and beat-size controls. |
| [#17004](https://github.com/mixxxdj/mixxx/pull/17004) | Merged | Adds the asynchronous startup loading screen. |
| [#17014](https://github.com/mixxxdj/mixxx/pull/17014) | Merged | Adds Full, Compact, and Mini responsive deck layouts. |
| [#17047](https://github.com/mixxxdj/mixxx/pull/17047) | Merged | Reskins waveforms with overlay-based stem and beatgrid controls. |

### Improvements and fixes

| PR | Status | Contribution |
|---|---|---|
| [#16463](https://github.com/mixxxdj/mixxx/pull/16463) | Merged | Fixes stale QML waveform marker geometry and textures after resizing. |
| [#16596](https://github.com/mixxxdj/mixxx/pull/16596) | Merged | Fixes the Library column-header assertion crash in the QML skin. |
| [#16992](https://github.com/mixxxdj/mixxx/pull/16992) | Merged | Fixes the menu-bar Preferences action and start-in-full-screen behavior. |
| [#17035](https://github.com/mixxxdj/mixxx/pull/17035) | Merged | Matches toolbar settings indicators and check states. |
| [#17036](https://github.com/mixxxdj/mixxx/pull/17036) | Merged | Improves key-color indicator logic and related styling. |
| [#17087](https://github.com/mixxxdj/mixxx/pull/17087) | Merged | Improves Classic parity for knobs, toolbar styling, and crossfader-assignment backgrounds. |
| [#17101](https://github.com/mixxxdj/mixxx/pull/17101) | Merged | Removes redundant toolbar options and compacts the relevant popups. |
| [#17103](https://github.com/mixxxdj/mixxx/pull/17103) | Merged | Aligns scheme-specific rack gutters and deck, mixer, sampler, and VU-meter margins. |
| [#17104](https://github.com/mixxxdj/mixxx/pull/17104) | Merged | Matches the legacy vinyl-control layout. |
| [#17108](https://github.com/mixxxdj/mixxx/pull/17108) | Merged | Fixes clipped deck transport buttons with the mixer visible and uses the correct Play button SVG in Full and Compact layouts. |
| [#17109](https://github.com/mixxxdj/mixxx/pull/17109) | Merged | Adds waveform track-drop support to LateNight QML. |
| [#17112](https://github.com/mixxxdj/mixxx/pull/17112) | Merged | Matches legacy key-control sizing and fixes the overflowing key control in Full and Compact layouts. |

### Shared `res/qml` work

| PR | Status | Contribution |
|---|---|---|
| [#16464](https://github.com/mixxxdj/mixxx/pull/16464) | Merged | Adds validation tests for QML theme colors and SVG assets. |
| [#16475](https://github.com/mixxxdj/mixxx/pull/16475) | Merged | Improves screen and HiDPI handling for QML preference windows. |
| [#16476](https://github.com/mixxxdj/mixxx/pull/16476) | Merged | Hides the legacy Interface preferences page in QML mode. |
| [#16488](https://github.com/mixxxdj/mixxx/pull/16488) | Merged | Adds relative dragging and right-click reset behavior to QML faders and knobs. |
| [#16583](https://github.com/mixxxdj/mixxx/pull/16583) | Merged | Exposes key formatting and harmonic utilities to QML. |
| [#16652](https://github.com/mixxxdj/mixxx/pull/16652) | Merged | Adds shared deck buttons, cycle controls, drop handling, and overview markers. |
| [#16654](https://github.com/mixxxdj/mixxx/pull/16654) | Merged | Adds shared hotcue, intro/outro, beat-size, beatgrid, and marker behaviors. |
| [#16660](https://github.com/mixxxdj/mixxx/pull/16660) | Merged | Adds shared toolbar status, skin settings, player APIs, and QML Skin Control Object creation. |
| [#16690](https://github.com/mixxxdj/mixxx/pull/16690) | Merged | Adds shared QML knobs, faders, orientation controls, and mixer primitives. |
| [#16699](https://github.com/mixxxdj/mixxx/pull/16699) | Merged | Removes the temporary Qt-widget deck track-menu bridge from QML. |
| [#16717](https://github.com/mixxxdj/mixxx/pull/16717) | Merged | Exposes typed slider-bar styling settings to QML controls. |
| [#16849](https://github.com/mixxxdj/mixxx/pull/16849) | Merged | Adds shared QML application menus, Library actions, dialogs, and proxies. |
| [#16883](https://github.com/mixxxdj/mixxx/pull/16883) | Merged | Adds shared QML effects proxies, selectors, presets, parameters, routing, and tests. |
| [#16935](https://github.com/mixxxdj/mixxx/pull/16935) | Merged | Adds reusable QML sampler, microphone, auxiliary-input, and ducking components. |
| [#16938](https://github.com/mixxxdj/mixxx/pull/16938) | Merged | Adds CI smoke tests for QML skin startup. |
| [#17034](https://github.com/mixxxdj/mixxx/pull/17034) | Merged | Adds the shared QML Waveforms page and connects shared preferences to active QML waveforms. |

### In Progress

| PR | Status | Contribution |
|---|---|---|
| [#17020](https://github.com/mixxxdj/mixxx/pull/17020) | Open | Fixes LateNight QML scaling across high-DPI and fractional-scale configurations, with DPR-aware rendering, reload safety, and focused tests. |
| [#17099](https://github.com/mixxxdj/mixxx/pull/17099) | Open | Adds the interim QWidget Preview deck and cover-art bridge, preserving legacy behavior and styling while native QML replacements are developed. |

## Planned LateNightQML Work

| Planned work | Description |
|---|---|
| Knob scaling artifact | Resolve the scaling artifact reported in the [PR #16858 discussion](https://github.com/mixxxdj/mixxx/pull/16858#issuecomment-5363364699). |
| Reskinning About Mixxx dialog | Bring the About Mixxx dialog into the LateNight QML visual language. |
| Deck Track Edit Menu | Add a QML track-edit menu for deck actions while preserving the existing behavior. |

## Future work and known issues

The project reached the intended GSoC milestone, and the next steps are clear:

1. Continue the open scaling work and validate LateNight QML across more operating systems, display scales, graphics backends, and window configurations.
2. Replace the current QWidget implementation of the Library with the New UI's native QML Library when [Antoine's Library splitview and search work](https://github.com/mixxxdj/mixxx/pull/16686) is ready. That work relies on newer Qt APIs requiring Qt 6.10, so the current bridge is an intentional transition point until that dependency is available across supported builds.
3. Complete the New UI Settings migration by finishing the remaining preference categories, routing all Preferences entry points to the New UI Settings window, and eventually replacing the QWidget `DlgPreferences` shell. The current dialog is an intentional transition boundary, not the final architecture.
4. Replace the in-progress QWidget Preview deck and cover-art bridge with native QML components in the New UI once they are ready.
5. Give every QML control support for the MIDI Learning Wizard and tooltips. Tooltips are tracked in [issue #17038](https://github.com/mixxxdj/mixxx/issues/17038), which covers both normal and `--developer` modes. The learning workflow will need every QML control to be discoverable through the same control metadata and interaction path as its QWidget counterpart.
6. Continue accessibility and interaction polish, including [screen-reader support](https://github.com/mixxxdj/mixxx/issues/17051), [consistent keyboard focus on startup](https://github.com/mixxxdj/mixxx/issues/17052), and [QML focus scopes](https://github.com/mixxxdj/mixxx/issues/17053), alongside the smaller visual issues that emerge from wider testing.
7. Port controller-display offscreen rendering from its legacy OpenGL-specific path to a solution compatible with the modern graphics acceleration APIs used by the QML scene graph.

LateNight QML is currently a dense desktop interface. QML makes direct-touch interaction more practical, but the current layout has not been designed as a dedicated touch interface: some controls remain small, and several menus rely on hover behavior. A future touch-oriented pass could define larger target sizes, touch-friendly popups and menus, gesture behavior for continuous controls, and responsive tablet layouts validated on real hardware.

LateNight QML is also a practical reference for a broader transition away from the legacy QWidget-based skinning system, but retiring legacy skin support would be a long-term project rather than a consequence of this GSoC alone. Tango and Deere share much of the existing infrastructure used by LateNight, so their ports could reuse much of the QML foundation established here. Shade has considerably more Shade-specific C++ code and would be rather difficult to port to QML. Any decision to remove the legacy-skinning system must wait until the official skins, custom-skin users, and their extension points have an equally capable and supportable QML path.

There are also a few cleanup items already in triage, including startup warnings and control-registration messages ([#16996](https://github.com/mixxxdj/mixxx/issues/16996), [#17048](https://github.com/mixxxdj/mixxx/issues/17048), [#17049](https://github.com/mixxxdj/mixxx/issues/17049)), effects-rack knob sizing ([#17040](https://github.com/mixxxdj/mixxx/issues/17040)), minimum-window-size handling ([#16997](https://github.com/mixxxdj/mixxx/issues/16997)), preview color-scheme fallback ([#17050](https://github.com/mixxxdj/mixxx/issues/17050)), and reskinning the track-scan dialog ([#17110](https://github.com/mixxxdj/mixxx/issues/17110)). The complete list can be followed through the [LateNight QML triage label](https://github.com/mixxxdj/mixxx/issues?q=is%3Aissue+label%3A%22LateNight+QML%22).

### AI-assisted work disclosure

The [scaling follow-up in PR #17020](https://github.com/mixxxdj/mixxx/pull/17020) is the only contribution in this GSoC effort where I used GPT Astra to generate code instead of writing it by hand. AI tools also assisted with repository exploration, comparing legacy and QML implementations, debugging, planning, and comment generation in a few places. I also experimented with agentic coding as part of the GSoC learning experience. I manually reviewed every change, made the final technical decisions, built and tested the code, manually tested the LateNight QML developer build, and handled all commits and PR communication myself. Based on my experience, relying on AI for larger or deeper tasks would require many iterations, substantial context, and careful handling of hallucinations, which can become counterproductive. In this project, using AI for review, validation, and an initial blueprint was more useful than relying on it for most of the development; responsible use still requires human review and judgment.

## Testing request

Please test LateNight QML in real DJ workflows, especially for performance and visual parity with the legacy LateNight skin across both Classic and PaleMoon. A lot of care has gone into making DJs feel at home with LateNight QML, with the goal of [restoring the same look and feel](https://mixxx.org/news/2026-06-06-gsoc-2026-rebuild-latenight-qml/#:~:text=restore%20the%20same%20look%20and%20feel!) as the original skin. Tell us what feels right, what feels different, and what needs work through Zulip or GitHub issue trackers.

## Acknowledgments

A project of this size is never a solo effort. I want to thank [Jörg Wartenberg (DJ D_Town, @JoergAtGithub)](https://github.com/JoergAtGithub) for his guidance throughout the project, from the early architecture and scope discussions to the many small decisions needed to keep the port moving. Thank you to [Antoine Colombier (@acolombier)](https://github.com/acolombier) for reviewing several parts of the work, and to [Daniel Schürmann (@daschuer)](https://github.com/daschuer) for his early review and feedback.

I am especially grateful to [ronso0](https://github.com/ronso0) for doing so much work on the original LateNight skin and for helping preserve the details that make it so familiar. This project stands on the work of everyone who has contributed to the legacy LateNight skin over the years. It is arguably Mixxx’s favourite skin.

Thank you also to the people who tested the new skin across different configurations and helped uncover issues that code review alone could not: [Evelynne Veys (@Eve00000)](https://github.com/Eve00000), [VespaDJ (@vespadj)](https://github.com/vespadj), [Lysander Treumann (@SammyMcFly)](https://github.com/SammyMcFly), [nomiapps (@nomiapps)](https://github.com/nomiapps), and [Owen Williams (@ywwg)](https://github.com/ywwg). Everyone else who tried the skin, reported a problem, or shared feedback during the project also helped make it better.

I am also grateful to Google for making this opportunity possible through [Google Summer of Code](https://summerofcode.withgoogle.com/), a program that brings open-source contributors and communities together.

## Closing

At the end of the 16-week GSoC period, LateNight QML is a working experimental skin that preserves the familiar LateNight experience while establishing a reusable QML foundation for future Mixxx interfaces.

The remaining QWidget boundaries are intentional follow-up work, not a gap in the project’s direction. The central migration is no longer hypothetical, and the next steps have a clear roadmap.

## Get Involved!

This project is fully open source, and I would love to hear feedback and ideas from the community, especially regarding accessibility and touch-screen usability.

- **Follow the Issues**: Keep track of LateNight QML work in the [GitHub issue tracker](https://github.com/mixxxdj/mixxx/issues?q=is%3Aissue+label%3A%22LateNight+QML%22). If you encounter a bug, usability issue, or have other feedback about LateNight QML, open an issue with steps to reproduce and relevant platform details. Mixxx maintainers will triage the report and apply the appropriate labels.
- **Join the Community**: Come chat with us in the [Mixxx Zulip organization](https://mixxx.zulipchat.com/) and follow the project discussions there.
- **Learn More**: Read about the wider [QML project](https://mixxx.org/news/2025-08-06-qml-project/) and its direction for Mixxx.
- **Contribute**: If you're familiar with QML or C++, we are always looking for reviewers and testers!
- **Make Reviews Easy**: Small, self-contained pull requests are especially valuable in a project of this size. They let maintainers understand the intent, verify the behavior, and spot unintended changes without having to untangle unrelated work. A careful self-review of every new commit and the final GitHub diff also makes collaboration more efficient and gives good contributions a clearer path forward.

Happy Mixxxing!
