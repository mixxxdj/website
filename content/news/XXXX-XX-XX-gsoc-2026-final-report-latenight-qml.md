---
title: "Final GSoC 2026 Report: Rebuilding the LateNight Theme in QML"
authors: Ayush Sah (arsenic)
tags: gsoc, gsoc-2026, development, UI, QML, LateNight
comments: yes
status: draft
summary: A final report on rebuilding Mixxx's LateNight skin in QML, from the legacy library bridge to native decks, mixer, effects, samplers, Mic/Aux, menus, responsive layouts, and waveform work.
---

<!-- DRAFT: Add final screenshots/video and update the publication date before publishing. -->

> **Disclaimer:** This post primarily serves as the documentation for my Google Summer of Code (GSoC) 2026 project, “Rebuilding the LateNight Theme in QML”. It is therefore longer and more technical than a typical Mixxx news post.

Hi everyone! I am Ayush Sah (arsenic), and I am back with the final report for my Google Summer of Code (GSoC) 2026 project with Mixxx.

In my [introductory post](https://mixxx.org/news/2026-06-06-gsoc-2026-rebuild-latenight-qml/), I described the plan to rebuild Mixxx’s iconic LateNight skin in native QML. The motivation was simple: preserve the dense, familiar workflow that makes LateNight useful to DJs while moving the skin’s presentation and interaction layer to a more flexible and modern UI technology.

The introductory post described a 12-week implementation plan. The project ultimately ran for 16 weeks, giving enough time to take the initial shell through the major LateNight workflows and the shared infrastructure needed to support them.

The result is a substantially complete LateNight QML interface with native QML decks, waveform integration and controls, toolbar, mixer, effects rack, samplers, microphone and auxiliary-input racks, menus, responsive deck layouts, and the theme infrastructure needed for Classic and PaleMoon styling.

The short version is that the original goal was not to make a new skin that merely looked like LateNight. It was to make the LateNight workflow available in QML, with the same controls, states, layouts, and visual language wherever the scope allowed.

You can also take a look at the video below to see LateNight QML in action.

<!-- YouTube video to be added -->

## From a bridge to a working skin

The first milestone was deliberately modest. It introduced the QML skin shell and the `QmlLegacyLibraryItem`, a bridge that hosts the existing QWidget-based Library inside the QML scene.

That bridge was important for two reasons. It made the experimental skin usable early in the project, and it let the rest of the interface be ported incrementally instead of waiting for a complete Library rewrite. It also exposed a number of details that are easy to miss when porting a skin: scrollbar and header behavior, sorting, search input, keyboard focus, drag-and-drop, splitters, preview controls, palette changes, and repaint scheduling.

The Library, its cover-art and Preview deck components, and the Preferences dialog remain deliberate QWidget transition boundaries in the current scope. The wider QML migration is already underway: native Library and Settings work is progressing, while QML replacements for the Preview deck and cover art remain follow-up work.

Once the bridge was stable, the work could proceed from the outside in. Shared controls and behaviors were added to `res/qml`, while the LateNight-specific composition lives in `res/skins/LateNightQML`. This separation makes the project more than a one-off skin port. It also provides a roadmap for future skin ports and independent skin implementations: enthusiasts can build on the shared QML controls, action proxies, effect infrastructure, and input behaviors instead of starting every skin from scratch.

<!-- TODO: Add a comparison Legacy vs LateNightQML Classic and PaleMoon end to end connection screenshots. -->

## Styling changes

The styling work focused on the places where QML could preserve the LateNight workflow while making the interface clearer or more space-efficient.

### Toolbar

The old Settings button was removed from the toolbar. It was a long-standing discoverability issue: a small button acted as the entry point for skin and layout settings, but its purpose was not obvious to new users and its behavior was often discovered only by accident. Users could also confuse it with the application Preferences entry, which was available from the menu bar. The relevant skin and layout settings are now exposed through dropdowns next to the toolbar sections. These dropdowns are implemented as overlays, so they can open above the skin without forcing the rest of the layout to move. This keeps the toolbar compact while making its controls easier to discover.

<!-- TODO: Add a toolbar GIF, video, or screenshot here. -->

On Windows and Linux desktop environments where a global application menu is not used, the traditional menu bar is replaced by a hamburger icon in the toolbar. It provides access to the same application actions through a hierarchical menu while saving vertical space. That gives DJs more room for the decks, mixer, and library without hiding essential application functions. On macOS, the actions continue to use the native system menu bar.

<!-- TODO: Add a hamburger GIF, video, or screenshot here. -->

### Waveform stem and beatgrid control overlays

The waveform reskin places stem and beatgrid controls over the waveform instead of taking space away from it. This is difficult to express cleanly in the old widget layout, but is natural in QML: controls can sit above the waveform without changing the geometry underneath it. The split-stem display and its states are styled as part of the waveform surface rather than as a separate block below it. The implementation restores the backgrounds, markers, gutters, separators, splitters, and filter-menu sizing needed to make the waveform area feel like LateNight while keeping both control sets available without introducing another layout row.

<!-- TODO: Add a waveform overlay GIF, video, or screenshot here. -->

### Effects Rack space saving

The effects rack supports a space-saving arrangement in which Effects 1 and 4 can remain compact while Effects 2 and 3 are open. This keeps the parameter-rich middle of the rack accessible without making the whole interface unnecessarily tall.

<!-- TODO: Add an effects-layout GIF, video, or screenshot here. -->

### 64 samplers without a separate skin

The old widget-based LateNight workflow used a separate `LateNight (64 Samplers)` skin for a high sampler count. LateNight QML can expose 4, 8, 16, 32, 48, and 64 samplers directly from the same skin without constructing every expanded sampler at once. Rows are reused, expanded content is cached, and warming happens sequentially, keeping the larger rack manageable while preserving the rest of the layout. This is one of the places where QML’s dynamic composition makes a unified skin possible without giving up the practical performance considerations that made a separate skin useful before.

<!-- TODO: Add a 64-sampler GIF, video, or screenshot here. -->

The final result is intentionally recognisable. QML gives us a different implementation and more adaptable layout primitives, but the Classic scheme should still feel like LateNight, and PaleMoon should still feel like the alternate LateNight scheme that existing users know.

## Startup experience and performance improvements

<!-- To be worked upon -->

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

This is feature and visual parity for the intended LateNight QML scope, not a claim that every Mixxx subsystem has already moved to QML. The remaining QWidget boundaries are intentional: Library and Preferences migrations are underway, while the Preview deck and cover-art path remain to be ported.

## New work in `res/qml`

Beyond the skin itself, the project contributed reusable QML work to `res/qml`.

The QML Settings work extended this migration. Native pages now cover sound hardware, the Library, controllers, and interface settings. Antoine's open [QML waveform-settings work](https://github.com/mixxxdj/mixxx/pull/15381) fills in the remaining waveform controls. In QML mode, the legacy Interface page is hidden to avoid presenting duplicate or misleading settings that do not apply to the new skin, while the Preferences action remains available through the application menu.

The waveform work adds a dedicated QML Waveforms page and connects shared waveform preferences to the active QML waveforms. It supports waveform type, zoom, visual gain, stem, marker, and related overview and scrolling-waveform settings, refreshing renderer stacks when renderer-affecting options change. Overview waveform caching remains unchanged, and analyzer status and progress reporting are retained without progressive waveform repainting. Some settings are intentionally unavailable in the current QML renderer: the frame-rate control is hidden, the legacy High Detail setting is disabled because it is not supported by the QML scene-graph renderer, and Split stereo signal is available only when the RGB waveform renderer is selected.

The deck port led to reusable button, cycle-control, overview-marker, hotcue, intro/outro, beat-size, beatgrid, and marker behaviors. Key formatting and harmonic-display support was exposed to QML and is used by the deck key display and the key-color indicator logic.

The control layer gained reusable QML knobs, faders, orientation controls, relative dragging, right-click reset behavior, slider-bar settings, and backend proxies for toolbar state. These pieces keep interaction behavior in one place instead of reimplementing it in every skin component.

Larger surfaces also benefited from shared infrastructure. Application-menu and action proxies connect QML menus to Mixxx commands and dialogs. Effects infrastructure provides effect selectors, presets, parameter controls, routing, and tests. Reusable sampler, microphone, auxiliary-input, and ducking components keep rack implementations consistent while allowing the LateNight layout to control their presentation.

Finally, the project added QML-focused validation and CI smoke coverage so the interface can behave like a first-class Mixxx UI rather than a special demo mode.

## Challenges and lessons learned

Porting a dense, mature skin showed that visual parity depends on interaction details as much as on geometry. A control can look correct and still feel wrong if its focus behavior, state indicator, reset action, or relationship with the rest of the layout is different from what existing users expect.

The largest practical challenge was coordinating QML state with Mixxx’s existing control and preference systems while the interface was being rebuilt piece by piece. The mixed QWidget and QML boundary was most visible in areas such as focus, menus, splitters, palette changes, and repaint behavior. The sampler rack presented a similar challenge at a different scale: high sampler counts needed to remain usable without constructing every expanded view at once.

The project reinforced two architectural lessons: keep reusable behavior in shared `res/qml` components, and give an experimental interface production-minded checks. Theme validation, startup smoke tests, explicit fallback behavior, and testing across layouts make the result easier for the wider Mixxx community to review and continue.

## Testing and validation

Validation combined automated checks with manual testing. Theme colors and SVG assets have dedicated validation, the shared effects infrastructure includes tests, and the QML skin has a startup smoke-test path in CI. These checks catch malformed assets, missing QML registrations, and regressions that are easy to overlook when the main focus is visual work.

Manual testing focused on both color schemes, two- and four-deck layouts, different window sizes, high sampler counts, effects routing, library searches, track actions, and switching between the legacy skin and LateNight QML. The remaining issues in the triage list show where broader hardware, platform, display-scale, and accessibility testing is still needed.

## Trying LateNight QML

LateNight QML remains an experimental skin. To try it from a developer build, start Mixxx with the developer flag:

```text
./build/mixxx --developer
```

Then open:

```text
Preferences → Interface → LateNight QML (Experimental)
```

The Classic and PaleMoon schemes can be selected from the QML interface preferences. For a meaningful trial, compare both schemes with the legacy skin across the layouts and workflows that matter to you.

## Pull requests

The following list records the project work as of 17 September 2026. It includes 37 project contributions: 35 merged and 2 still open. An earlier closed bootstrap attempt is intentionally excluded because it was superseded by the merged Library-integration path listed below.

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
| [#16596](https://github.com/mixxxdj/mixxx/pull/16596) | Merged | Fixes the Library column-header assertion crash in the QML skin. |
| [#16992](https://github.com/mixxxdj/mixxx/pull/16992) | Merged | Fixes the menu-bar Preferences action and start-in-full-screen behavior. |
| [#17035](https://github.com/mixxxdj/mixxx/pull/17035) | Merged | Matches toolbar settings indicators and check states. |
| [#17036](https://github.com/mixxxdj/mixxx/pull/17036) | Merged | Improves key-color indicator logic and related styling. |

### Shared `res/qml` work

| PR | Status | Contribution |
|---|---|---|
| [#16463](https://github.com/mixxxdj/mixxx/pull/16463) | Merged | Fixes stale QML waveform marker geometry and textures after resizing. |
| [#16464](https://github.com/mixxxdj/mixxx/pull/16464) | Merged | Adds validation tests for QML theme colors and SVG assets. |
| [#16475](https://github.com/mixxxdj/mixxx/pull/16475) | Merged | Improves screen and HiDPI handling for QML preference windows. |
| [#16476](https://github.com/mixxxdj/mixxx/pull/16476) | Merged | Hides the legacy Interface preferences page in QML mode. |
| [#16488](https://github.com/mixxxdj/mixxx/pull/16488) | Merged | Adds relative dragging and right-click reset behavior to QML faders and knobs. |
| [#16583](https://github.com/mixxxdj/mixxx/pull/16583) | Merged | Exposes key formatting and harmonic utilities to QML. |
| [#16652](https://github.com/mixxxdj/mixxx/pull/16652) | Merged | Adds shared deck buttons, cycle controls, drop handling, and overview markers. |
| [#16654](https://github.com/mixxxdj/mixxx/pull/16654) | Merged | Adds shared hotcue, intro/outro, beat-size, beatgrid, and marker behaviors. |
| [#16660](https://github.com/mixxxdj/mixxx/pull/16660) | Merged | Adds shared toolbar status, skin settings, and player APIs. |
| [#16690](https://github.com/mixxxdj/mixxx/pull/16690) | Merged | Adds shared QML knobs, faders, orientation controls, and mixer primitives. |
| [#16699](https://github.com/mixxxdj/mixxx/pull/16699) | Merged | Removes the temporary Qt-widget deck track-menu bridge from QML. |
| [#16717](https://github.com/mixxxdj/mixxx/pull/16717) | Merged | Exposes typed slider-bar styling settings to QML controls. |
| [#16849](https://github.com/mixxxdj/mixxx/pull/16849) | Merged | Adds shared QML application menus, Library actions, dialogs, and proxies. |
| [#16883](https://github.com/mixxxdj/mixxx/pull/16883) | Merged | Adds shared QML effects proxies, selectors, presets, parameters, routing, and tests. |
| [#16935](https://github.com/mixxxdj/mixxx/pull/16935) | Merged | Adds reusable QML sampler, microphone, auxiliary-input, and ducking components. |
| [#16938](https://github.com/mixxxdj/mixxx/pull/16938) | Merged | Adds CI smoke tests for QML skin startup. |

### In progress

| PR | Status | Contribution |
|---|---|---|
| [#17020](https://github.com/mixxxdj/mixxx/pull/17020) | Open | Continues scaling, Library bridge rendering, reload safety, diagnostics, and tests. |
| [#17034](https://github.com/mixxxdj/mixxx/pull/17034) | Open | Adds QML waveform preferences, loading/analyzer integration, and the [#17011](https://github.com/mixxxdj/mixxx/issues/17011) follow-up. |

## Future work and known issues

The project reached the intended GSoC milestone, but LateNight QML is still marked experimental. The next steps are clear:

1. Continue the QML work in the open scaling and waveform PRs, and validate it across more operating systems, display scales, graphics backends, and window configurations.
2. Replace the current QWidget implementation of the Library with a native QML Library when [Antoine's Library splitview and search work](https://github.com/mixxxdj/mixxx/pull/16686) is ready. The current bridge is an intentional transition point, not the final architecture.
3. Complete the QML Settings migration by finishing the remaining QML preference categories, routing all Preferences entry points to the QML Settings window, and eventually replacing the QWidget `DlgPreferences` shell. The current dialog is an intentional transition boundary, not the final architecture.
4. Replace the current Preview deck and cover-art implementation with QML once their native components are ready.
5. Add tooltips to LateNight QML and the New UI. This is tracked in [issue #17038](https://github.com/mixxxdj/mixxx/issues/17038), which covers both normal and `--developer` modes.
6. Continue accessibility and interaction polish, including [screen-reader support](https://github.com/mixxxdj/mixxx/issues/17051), [consistent keyboard focus on startup](https://github.com/mixxxdj/mixxx/issues/17052), and [QML focus scopes](https://github.com/mixxxdj/mixxx/issues/17053), alongside the smaller visual issues that emerge from wider testing.

There are also a few cleanup items already in triage, including startup warnings and control-registration messages ([#16996](https://github.com/mixxxdj/mixxx/issues/16996), [#17048](https://github.com/mixxxdj/mixxx/issues/17048), [#17049](https://github.com/mixxxdj/mixxx/issues/17049)), effects-rack knob sizing ([#17040](https://github.com/mixxxdj/mixxx/issues/17040)), minimum-window-size handling ([#16997](https://github.com/mixxxdj/mixxx/issues/16997)), and preview color-scheme fallback ([#17050](https://github.com/mixxxdj/mixxx/issues/17050)). The complete list can be followed through the [LateNight QML triage label](https://github.com/mixxxdj/mixxx/issues?q=is%3Aissue+label%3A%22LateNight+QML%22), just as in the introductory post.

### AI-assisted work disclosure

The [scaling follow-up in PR #17020](https://github.com/mixxxdj/mixxx/pull/17020) is the only contribution in this GSoC effort where I used GPT Astra for code generation. It helped prepare a plan, generate small code snippets, and review branch changes; implementation decisions, testing, and validation remained my responsibility.

## Testing request

A lot of care has gone into making DJs feel at home with LateNight QML. The goal has been to [“restore the same look and feel”](https://mixxx.org/news/2026-06-06-gsoc-2026-rebuild-latenight-qml/) of the original skin. Please test it in real DJ workflows, especially for performance and visual parity with the legacy LateNight skin across both Classic and PaleMoon. Tell us what feels right, what feels different, and what needs work through Zulip or GitHub issue trackers.

## Acknowledgments

A project of this size is never a solo effort. I want to thank [Jörg Wartenberg (DJ D_Town, @JoergAtGithub)](https://github.com/JoergAtGithub) for his guidance throughout the project, from the early architecture and scope discussions to the many small decisions needed to keep the port moving. Thank you to [Antoine Colombier (@acolombier)](https://github.com/acolombier) for reviewing several parts of the work, and to [Daniel Schürmann (@daschuer)](https://github.com/daschuer) for his early review and feedback.

I am especially grateful to [ronso0](https://github.com/ronso0) for doing so much work on the original LateNight skin and for helping preserve the details that make it so familiar. This project stands on the work of everyone who has contributed to the legacy LateNight skin over the years. It is arguably Mixxx’s favourite skin.

Thank you also to the people who tested the new skin across different configurations and helped uncover issues that code review alone could not: [Eve (@Eve00000)](https://github.com/Eve00000), [VespaDJ (@vespadj)](https://github.com/vespadj), [Sam McFly (@SammyMcFly)](https://github.com/SammyMcFly), [nomiapps (@nomiapps)](https://github.com/nomiapps), and [Owen Williams (@ywwg)](https://github.com/ywwg). Everyone else who tried the skin, reported a problem, or shared feedback during the project also helped make it better.

I am also grateful to Google for making this opportunity possible through [Google Summer of Code](https://summerofcode.withgoogle.com/), a program that brings open-source contributors and communities together.

## Closing

At the end of the 16-week GSoC period, LateNight QML is a working experimental skin that preserves the familiar LateNight workflow while establishing a reusable QML foundation for future Mixxx interfaces.

The remaining QWidget boundaries are intentional follow-up work, not a gap in the project’s direction. The central migration is no longer hypothetical, and the next steps have a clear roadmap.

## Get Involved!

This project is fully open source, and I would love to hear feedback and ideas from the community, especially regarding accessibility and touch-screen usability.

- **Follow the Issues**: Keep track of LateNight QML work in the [GitHub issue tracker](https://github.com/mixxxdj/mixxx/issues?q=is%3Aissue+label%3A%22LateNight+QML%22).
- **Join the Community**: Come chat with us in the [Mixxx Zulip organization](https://mixxx.zulipchat.com/) and follow the project discussions there.
- **Learn More**: Read about the wider [QML project](https://mixxx.org/news/2025-08-06-qml-project/) and its direction for Mixxx.
- **Contribute**: If you're familiar with QML or C++, we are always looking for reviewers and testers!

Happy Mixxxing!
