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

## Storyboard Architecture (The Multi-Frame Grid Standard)

The approved storyboard format is a **multi-frame editorial approval document** (following the reference architecture in `storyboard_standalone.html`). It combines visual scanning, beat-by-beat frame inspection, and interactive playback.

A high-quality editorial storyboard MUST provide:

### 1. Masthead & Sticky Navigation
- **Masthead:** Editorial display title with serif emphasis (`Newsreader` / `Georgia`), project introduction, and status line pills (Narration lock, scene counts, target aspect ratio, fps, audio status).
- **Sticky Navigation (`.board-nav`):** Sticky bar with direct anchor jump links to every scene (`#scene-1`, `#scene-2`, ...) for rapid reviewer navigation.

### 2. Overview Contact Sheet (`.overview`)
- A horizontal grid displaying a 9:16 aspect-ratio thumbnail card for every scene.
- Each card displays the scene number, hero visual state, timing range, and current approval status (e.g. `01 · The reversal / 00–10s / LOCKED`).

### 3. Detailed Per-Scene Breakdown (`.section id="scene-X"`)
Every scene must have its own comprehensive editorial section containing:

1. **Section Heading:**
   - Large serif scene number (`01`, `02`...) in `Newsreader`/`Georgia`.
   - Scene title (`h2`) and concise director's description.
   - Precise timing block: `00:00 – 00:08 | Frames 0 – 240 (8.0s) @ 30fps`.

2. **Voiceover Blockquote (`.vo`):**
   - Prominent blockquote displaying the exact spoken narration.
   - Header tag: `<small>VOICEOVER (XX WORDS)</small>`.

3. **Multi-Frame Keyframe Grid (`.frames` — CORE REQUIREMENT):**
   - A grid of **4 to 6 distinct keyframe cards** side-by-side per scene (`<figure class="keyframe-card">`), visually demonstrating the progression across beats:
     * Entry / Anchor
     * First Reveal / Evidence
     * Transformation / Mechanism
     * Payoff / Settle / Launchpad
   - **Each keyframe card MUST contain:**
     * A 9:16 vertical visual stage (`.keyframe-visual`, `aspect-ratio: 9/16`) built with real HTML/CSS/SVG layers, cutouts, telemetry callouts, and lighting.
     * A prominent motion cue badge (`.kf-motion-cue`, e.g. `HERO PUSH ↑`, `BLUEPRINT REVEAL ↗`, `SYSTEM FRACTURES ⚡`, `PAYOFF HOLDS`).
     * `<figcaption>` detailing:
       - Frame range and seconds (`<time>F00–F18 · 0.0–0.6s</time>`)
       - Bold state title (`<b>The date burns in</b>`)
       - Concise explanation of what visual change occurs in this beat and why.

4. **Editorial Tension Triangle (`.tension-triangle-card`):**
   - Clearly defines the dramatic core of the scene:
     * **Actor:** The primary subject / agent of change.
     * **Counter-Force:** The opposing constraint, legacy system, or competitor.
     * **Stakes:** What is won or lost in this beat.

5. **Visual Sentence Track (`.pacing-track`):**
   - Multi-column timeline grid breaking the scene into sequential visual micro-beats (e.g. `Anchor (f0–32)`, `Mechanism (f32–80)`, `Payoff (f80–120)`).
   - Color-coded top borders (blue for anchor, red for clash, gold/yellow for punch/payoff).

6. **Technical Physics & Audio Notes:**
   - **Camera Physics:** Explicit camera movement, sampling rate (e.g. 12 FPS vs 30 FPS), focal push, and easing behavior.
   - **Audio / SFX Cues:** Exact sound design sync points (whoosh, click, mechanical advance, tone shift) and voice timing anchors.
   - **Required Scene Assets:** Asset pill links (`.asset-link-pill`) and visual reference card grid.

7. **Interactive Motion Study / Playable Blocking Sketch (`<details>`):**
   - Expandable interactive review panel.
   - Interactive 9:16 canvas with Play, Pause, Reset, and scrub controls, synchronized to the narration audio (`*.wav`).
   - **Motion Choreography Score Table (`.score`):**
     * `Local time / frame`
     * `Motion, direction & easing` (exact transform, scale, rotation, bezier curves)
     * `Meaning & narrative justification`

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
