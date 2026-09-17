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

## Choose the Smallest Useful Path

### Lightweight path

Use for a simple film, a low-risk scene, or an already-established visual language.

Create one responsive HTML page containing:

- the target aspect-ratio frame;
- one panel per scene;
- 2-4 representative states per scene: entry, meaningful change, payoff, and exit when distinct;
- narration excerpt or semantic beat beside the frame, not as baked scene art;
- short motion and transition notes;
- asset placeholders labeled with their current status.

Static state switching is enough. Add only the JavaScript needed to step through states or preview a transition.

### Full path

Use when the film has high creative uncertainty, complex processes, several visual worlds, important hero scenes, continuous transitions, or costly/generated assets.

In addition to the lightweight path, include:

- a scene/state timeline driven by approximate seconds or semantic anchors;
- play/pause and direct state navigation;
- rough interpolation for primary motion and scene transitions;
- neighboring-scene playback to judge continuity;
- variant views for unresolved concepts, clearly marked as candidates;
- target-size and reduced-size previews for readability;
- notes for asset provenance, representation type, and unresolved risk.

Approximate motion is sufficient. Do not spend time matching final springs, filters, particles, audio mixing, or exact frame timing.

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
