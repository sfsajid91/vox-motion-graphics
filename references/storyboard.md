# HTML Storyboard & Design Freeze

## Purpose

The storyboard is the film's primary **visual decision surface**. Build it after the narrative beats and scene concepts are credible, and before production Remotion work begins.

Use ordinary HTML, CSS, and minimal JavaScript to resolve the decisions that are expensive to discover after implementation:

- composition and focal hierarchy;
- asset choice and crop;
- scene structure and meaningful visual states;
- motion and transition intent;
- pacing and intentional holds;
- text density and readability;
- continuity between neighboring scenes.

The storyboard is not a second renderer. It should communicate the intended experience without reproducing Remotion's frame math, media pipeline, effects stack, or component architecture.

Treat the browser preview itself as the creative source of truth. JSON/Markdown may index scene IDs, review state, or machine-checkable metadata, but should not restate the whole storyboard in a second format. If two representations drift, stop and reconcile them instead of letting an agent guess which one is current.

## Place in the Workflow

`research/script -> narrative beats -> visual concepts -> HTML storyboard -> editorial critique -> refinement -> freeze -> Remotion implementation -> technical QA -> editorial render QA`

Do not begin detailed scene implementation while important composition, asset, or mechanism decisions remain unresolved in the storyboard.

## Storyboard Architecture (Editorial Control Room standard)

The default storyboard is a **multi-frame editorial approval surface** with a stable, reusable page shell. It should feel like an editorial control room: scan the whole sequence first, then inspect one scene at a time without losing navigation or context.

Before building the shell:

- Always load [storyboard-layout.md](storyboard-layout.md). It is the embedded canonical copy of the extracted `DESIGN.md` and is the default layout contract.
- If the project has a root `DESIGN.md`, use it as the local override for tokens and named rules; preserve the embedded shell anatomy unless its `Layout` section explicitly changes it.
- Treat the shell as layout grammar, not as a template for another project's topic, assets, copy, scene count, or animation.
- Keep frame art, scene-specific visual systems, and motion studies inside the shell; do not let them redefine the outer anatomy.

### Layout shell (required default)

Unless the brief explicitly requests another approval surface, include these regions in this order:

1. **Masthead (`.masthead`):** A centered page-frame header with a serif display title, short project description, and compact metadata/status block. Use `max-width: 1540px`, a `1fr auto` grid, `32px` gap, bottom alignment, and `52px 40px 32px` padding.
2. **Sticky director rail (`.director-rail`):** A full-width sticky navigation band at `top: 0` with direct scene-jump links and one utility action. Use a `1540px` inner frame, `10px 40px` padding, a bottom rule, translucent paper, subtle blur, and horizontal overflow for the jump group.
3. **Overview contact sheet (`.overview-section`):** A whole-sequence scan before detailed scenes. Use 9:16 thumbnail cards with an identifier and time/status caption. Use seven equal columns with `14px` gaps on wide screens, four columns below `1080px`, and a horizontal row with `130px` minimum cards below `680px`.
4. **Repeated scene shell (`.scene`):** Each scene is an article with a stable metadata rail and flexible body: `140px minmax(0, 1fr)` columns, `36px` gap, `52px 0` padding, and a structural bottom rule. The metadata rail may stick at `top: 76px`.
5. **Scene context block (`.scene-editorial-header`):** Place the title/status row, concise thesis, and context or voiceover card before the inspection pair. Let the title/status row wrap rather than force overflow.
6. **Inspection pair (`.canvas-row`):** Place the primary focal stage beside a flexible sequence area using `minmax(300px, 350px) minmax(0, 1fr)` and a `32px` gap.
7. **Sequence area (`.sequence-section`):** Start with a shared section-label bar, then use a four-column frame grid with `12px` gaps. Each frame unit may contain a timing row, state title, 9:16 preview, and concise note. Use 4–6 cards when beat-level inspection is needed.
8. **Director notes (`.director-notes`):** Close each scene with a two-column rationale/handoff block, `28px` apart, separated by a top rule.

The shell is the approval surface. It must make the hierarchy obvious without requiring the reviewer to read implementation notes.

### Responsive contract

- Below `1180px`, reduce the focal column to `minmax(260px, 320px)` with a `24px` gap and use two frame columns.
- Below `860px`, stack the masthead, scene metadata, and inspection pair; make metadata static and horizontal; center the focal stage; cap the focal canvas at `360px`; use `24px` page gutters.
- Below `680px`, make the contact sheet horizontally scrollable with `130px` minimum cards and stack director notes with a `16px` gap.
- Below `580px`, use one frame column, compact scene-jump buttons, and hide secondary director tools.
- Preserve a minimum `44px` interaction target for navigation and controls at every width.

### Surface baseline

When no project-specific `DESIGN.md` overrides it, use:

- warm paper page and card surfaces;
- dark ink and muted secondary text;
- Newsreader/Georgia for editorial display;
- system sans for body copy;
- JetBrains Mono for production metadata;
- `4px` container radii and `999px` only for scene navigation;
- 1px hairline rules and restrained shadows;
- red only for active, selected, locked, or otherwise meaningful signals.

The baseline is a structural and visual default, not a topic or animation prescription. A project design document may change tokens, type, depth, or component treatment while preserving the inspection hierarchy unless its `Layout` section explicitly changes it.

### Scene content modules

Inside the stable shell, add only the modules needed for the review:

1. **Section context:** Scene title, timing status, and one-sentence visual thesis.
2. **Voiceover blockquote (`.vo`):** Exact narration and word count when narration is part of the approval decision.
3. **Multi-frame keyframe grid (`.frames`):** Distinct states such as entry, reveal, mechanism, payoff, and handoff. Each card needs a 9:16 stage, state/timing metadata, and a short explanation.
4. **Editorial support:** Tension triangle, pacing track, asset notes, audio notes, or an expandable motion study when they clarify approval.

These modules are content decisions, not shell decisions. They may vary by story without changing the page frame, navigation, overview, scene anatomy, or focal/sequence relationship.
---

## Storyboard Content Contract

For each scene, make the following visible or inspectable:

- semantic job: what the viewer must understand;
- visual thesis: what should read with the sound muted;
- focal subject for every meaningful state;
- entry state, primary state change, payoff state, and exit/handoff;
- primary mechanism and any supporting motion;
- scene construction family;
- asset roles and current asset status;
- art-directed text, if any;
- narration anchors that cause visible changes;
- transition intent into and out of the scene;
- known uncertainty or representation risk.

The storyboard should answer these questions without reading implementation code:

1. Where does the eye go first?
2. What changes, and why does that change matter?
3. Does the visual structure respond when the narration changes idea?
4. Is the payoff clearer and usually simpler than the buildup?
5. Can the next scene inherit attention, direction, object, or scale?
6. Are the selected assets capable of the intended action?


## Approval-Surface Ergonomics

The user should be able to judge the direction by watching and scanning, not by reading a production document. Default each scene to the target-ratio visual, playback/scrub controls when motion matters, a one-sentence visual thesis, and only the notes required to approve the idea.

Keep these secondary, collapsed, or in separate files until freeze:

- long research/source discussions;
- full Remotion or coding prompts;
- exact easing/transform values;
- dense frame tables;
- exhaustive SFX cue sheets;
- internal implementation parameters;
- provenance/legal notes that do not change the immediate visual decision.

A storyboard may contain deep documentation, but the approval path must remain visually obvious. Do not let planning text, telemetry, or UI chrome compete with the scene itself.

## Status and Precision Discipline

Use separate status concepts:

- **script status**: draft / approved / locked words;
- **voice-performance status**: missing / scratch / final;
- **timing status**: estimated / aligned / frame-locked.

Do not use a single ambiguous label such as `narration locked` to cover all three. If final VO is not aligned, scene times are editorial estimates. Exact frame numbers may be shown only as explicitly provisional blocking aids; do not present them as the production timing contract.

A scene can be design-ready before final VO, but frame-accurate choreography waits for the final performance.

## Evidence-Looking Objects

A newspaper, document, screenshot, memo, archival card, quotation panel, or chart can visually imply primary evidence even when the text is invented. Before approval, classify it.

- **real evidence**: use the sourced artifact or a faithful crop/retypeset with source identity preserved;
- **retypeset excerpt**: clearly identify it as a retypeset/editorial excerpt and do not add a fake masthead, invented article body, quotation, stamp, or date that makes it look recovered;
- **reconstruction/metaphor**: make the reconstruction visibly editorial rather than counterfeit archival evidence.

If the viewer could reasonably mistake a fabricated document for a historical source, the storyboard is not ready for approval.

## Information Budget

Source notes may be rich; the frame should not be. Every visible specification, telemetry label, date, badge, or caption must either orient the viewer, prove the beat, or deliver the payoff. Move supporting provenance and unused specifications out of the visual canvas. A simple narration beat should not become a dense engineering dashboard merely because the research found many facts.

## Asset Status in Storyboards

Never compress acquisition, usability, taste, and rights into one status. Show the asset ledger's independent fields:

- `origin`: `reused`, `programmatic`, `sourced`, `reconstructed`, or `generated`;
- `technicalStatus`: `candidate`, `available`, or `verified`;
- `editorialStatus`: `pending`, `accepted`, or `rejected`;
- `rightsStatus`: `unresolved`, `needs_review`, `verified`, or `self_created`;
- representation type and claim references where factual meaning is involved.

`generated` describes origin only. It does not imply that the asset is technically verified, editorially accepted, rights-cleared, or suitable as evidence. Likewise, a technically verified asset may still be editorially rejected.

Placeholders are allowed during concept work and review. Resolve identity-critical, evidence-critical, and composition-defining assets early because replacing them can invalidate the design. Before final freeze, every referenced production asset must be technically verified and editorially accepted; otherwise keep the storyboard in review. Rights and representation requirements remain separate gates.

## Motion and Timing Fidelity

Storyboard timing is for editorial judgment. Use semantic anchors and approximate durations until final narration alignment exists.

Preview:

- when the primary state change occurs;
- whether a hold has a reading or dramatic purpose;
- whether narration changes while the image remains structurally unchanged;
- whether a transition begins before the current payoff resolves;
- whether the scene appears to end before its narration or captions;
- whether an unexplained dead tail follows the final meaningful event.

Exact word timestamps, spring parameters, frame rounding, audio trimming, and render-safe media handling belong to the Remotion implementation stage.

## Critique and Refinement

Run editorial critique on the storyboard before freeze. Review at the intended aspect ratio and at a realistic small viewing size.

Resolve, in this order:

1. truthfulness and representation risk;
2. visual thesis and process/mechanism clarity;
3. focal hierarchy and composition;
4. meaningful state progression and pacing;
5. asset fitness and readability;
6. continuity and transition intent;
7. surface treatment.

Repair the responsible decision. Do not conceal a weak mechanism with more text, texture, camera drift, or decorative motion.

Use [critique.md](critique.md) for verdict ownership and [anti-patterns.md](anti-patterns.md) for common failure recovery.

## Freeze Gate

An independent editorial critic may mark a storyboard `ready_for_approval` when:

- every scene has a readable thesis and focal hierarchy;
- narration changes are matched by appropriate visual state changes or justified holds;
- process/system beats visualize relationships rather than defaulting to cards or archival stills;
- identity/evidence-critical assets are accepted and correctly represented;
- transitions and final holds are intentional;
- unresolved issues are implementation details rather than design questions.

If the user asked to approve the preview, stop at `ready_for_approval` and show the preview plus concise review notes. Freeze only after that approval. If the user explicitly delegated approval, an independent critic may freeze automatically.

Record the freeze identifier or timestamp and the accepted scene states only when another agent/tool needs a machine-readable handoff. The generating agent may declare its own work ready for review, but may not self-award approval.

## Handoff to Remotion

After freeze, the Remotion agent is primarily an implementer. It should preserve:

- scene order and semantic jobs;
- accepted composition and focal hierarchy;
- meaningful visual states;
- asset selection and representation type;
- motion and transition intent;
- readable payoff and handoff states.

It may refine deterministic timing, responsive geometry, easing, compositing, accessibility, and render reliability without reopening design.

## Change Control After Freeze

Classify proposed changes before editing:

### Implementation refinement

May proceed without returning to storyboard when it preserves the accepted visual meaning. Examples: frame rounding, safer crop bounds, deterministic easing, caption layout, media loading, or small position adjustments.

### Design deviation

Return to the storyboard and re-run editorial critique when a change alters:

- the focal subject or hierarchy;
- the scene mechanism or construction family;
- an accepted hero/evidence asset;
- the number or order of meaningful states;
- the visual meaning of a transition;
- the payoff composition;
- factual or representational interpretation.

Do not let implementation convenience silently redesign a frozen scene.

## Storyboard-to-Render Check

At implementation review, compare representative rendered frames with the frozen storyboard. Differences are acceptable when they improve fidelity or technical safety without changing the design intent. Record material deviations and route design changes back through storyboard critique.
