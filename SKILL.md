---
name: vox-motion-graphics
description: Direct and implement polished editorial motion-graphics videos in Remotion from vague or complete briefs. Use for research-led explainers, documentary shorts, visual storytelling, storyboards, motion systems, asset direction, narration-led timing, and editorial plus technical QA without requiring the user to be a designer.
---

# Editorial Motion Director — v0.8.1

## Mission

Turn a topic, script, or rough brief into a clear, original, polished motion-graphics video. Own the directing decisions unless they change factual meaning, rights, brand identity, material cost, or another user-owned constraint.

Optimize for fewer expensive iterations: resolve the visual argument in a cheap browser storyboard, freeze it, then implement it faithfully in Remotion.

Default to autonomous direction. Infer ordinary creative decisions, continue through the workflow without asking the user to choose motion-design details, and pause only for a real blocker or an approval gate the user explicitly wants to own.

## Operating principles

1. **Show the mechanism, not the noun.** Visualize relationships, causes, constraints, transformations, and consequences instead of defaulting to icons or literal vocabulary.
2. **Hierarchy before treatment.** The factual claim, focal point, and dominant change must read before texture, effects, labels, or ambient motion.
3. **One visual thesis per scene.** A scene may contain many events, but each state needs a clear focal point and the events must support one idea.
4. **Narrative change needs visual response.** When the narration introduces a new cause, stage, contrast, or consequence, change the visual structure or explicitly justify a hold.
5. **Technical success is not editorial success.** A valid render can still be confusing, static, generic, or badly paced. Run separate technical and editorial QA.
6. **Generated is not accepted.** Track asset origin, technical verification, editorial acceptance, rights, and factual representation separately.
7. **References teach grammar, not templates.** Reuse a useful mechanism only when it solves the new story; do not inherit exact layouts, assets, colors, timings, or surface style by default.
8. **The approval surface is not the production spec.** Storyboards optimize for visual judgment. Keep prompts, frame math, source notes, and implementation detail secondary or collapsed until design freeze.

## Production graph

`research/script -> narrative beats -> visual concepts -> HTML storyboard/preview -> editorial critique -> refinement -> design freeze -> final VO/alignment -> Remotion implementation -> SFX/music/captions -> editorial QA + technical QA -> render`

Final voice performance is recorded or synthesized after the story and design are stable but before frame-accurate choreography. Scratch narration or timing estimates may drive the storyboard. Sound design and music remain finishing stages.

## 1. Brief, evidence, and story

Infer reasonable audience, format, duration envelope, tone, and platform defaults. Ask only when missing information materially changes facts, rights, brand, cost, or scope.

For factual work:

- record claims as `verified`, `unverified`, `disputed`, or `inference`;
- keep rights and factual accuracy as separate axes;
- never make narration, labels, charts, or reconstructed visuals more specific than their supporting evidence;
- distinguish `literal`, `evidence`, `reconstruction`, `metaphor`, and `abstract` representations;
- never style invented or retypeset material so it can be mistaken for a recovered primary document. Use a real sourced artifact, or clearly label an editorial reconstruction/retypeset excerpt and keep invented mastheads, quotations, and article copy out of evidence scenes.

Build one editorial angle, a causal/logical spine, a viewer promise, and narrative beats. Scene boundaries follow visual ideas, not punctuation, fixed durations, or one-sentence-per-scene formulas.

If the user supplies reference videos, creators, or a target look, deconstruct them before concept generation and classify transferable grammar separately from benchmark-specific surface details. After analysis, translate named references into observable grammar; do not use creator names as a substitute for direction in production prompts unless the user explicitly wants those names retained as human shorthand. Read [reference-analysis.md](references/reference-analysis.md).

Read [story-director.md](references/story-director.md) for story construction and [research-and-representation.md](references/research-and-representation.md) for factual work.

## 2. Editorial translation and visual concepts

For each beat, decide:

1. what the viewer must understand;
2. the real relationship or mechanism;
3. the story-specific material vocabulary;
4. the visible state change;
5. the focal point and payoff;
6. how attention hands to the next beat.

Use `Anchor -> Action -> Consequence -> Launchpad` as a compact scene grammar, not a rigid timing template.

When narration describes causality, systems, economics, loops, growth/decline, transformation, or dependencies, prefer connected structures such as flows, handoffs, accumulation/depletion, networks, object systems, diagrams, or state changes. Use archival media when it supplies identity, evidence, emotion, or context—not as a substitute for explaining the mechanism.

When creative uncertainty is meaningful, compare 2–4 cheap concepts across different scene families. Uncertainty is meaningful when the mechanism, asset feasibility, factual representation, or neighboring-scene distinctness is unresolved. Do not polish several full scenes.

Read [scene-patterns.md](references/scene-patterns.md), [visual-language.md](references/visual-language.md), and [transitions.md](references/transitions.md).

## 3. HTML storyboard is the creative decision surface

Create a browser-viewable HTML/CSS/JS storyboard or motion preview before Remotion implementation.

Use it to decide:

- composition and focal hierarchy;
- asset choice and representation;
- scene structure and meaningful states;
- camera/object relationships;
- motion and transition intent;
- rough pacing and readable holds;
- continuity across scenes.

Do not reproduce every Remotion prop, counter, SFX control, easing curve, implementation prompt, or frame table. Document runtime-only behavior in notes after the visual direction is approved. The default approval view should foreground the actual target-ratio frame, playback/scrub controls when useful, and concise scene intent; keep research, provenance, long motion tables, and build prompts collapsed or in secondary files.

Use a lightweight storyboard for simple/low-risk scenes and a playable multi-state preview for uncertain, continuous, or transition-heavy scenes. The storyboard may use placeholders, but every asset must expose its current status. Keep status language unambiguous: distinguish script lock, final voice-performance lock, and frame-timing lock. Do not call narration "locked" when only the words are approved but the final performance/alignment is still provisional.

Critique and refine the storyboard before implementation. The HTML preview is the creative source of truth; structured files may index or validate it, but must not become a second competing storyboard. Freeze only when each scene has a clear thesis, focal point, defining relationship/state change, asset direction, transition intent, and no unresolved editorial blocker. Record frozen states in `storyboard-plan.json` only when a machine-readable handoff is actually useful.

If the user asked to approve the storyboard, an independent critic may mark it ready for approval but must not substitute for that human gate. If approval was explicitly delegated, an independent critic may freeze it.

After freeze, Remotion may refine timing, easing, compositing, and technical execution. A change to the scene thesis, focal hierarchy, defining relationship, asset identity, or transition logic returns to the storyboard.

Read [storyboard.md](references/storyboard.md).

## 4. Assets and visual language

Route assets deliberately:

`reuse -> programmatic -> source real/licensed -> reconstruction -> generate`

Prefer real or licensed material when identity/evidence matters; programmatic graphics for systems, charts, routes, interfaces, and neutral reconstructions; generated media for original illustrative material or clearly identified reconstructions.

Track orthogonal asset fields:

- `origin`: how it was obtained;
- `technicalStatus`: candidate, available, or verified;
- `editorialStatus`: pending, accepted, or rejected;
- `rightsStatus`: unresolved, needs review, verified, or self-created;
- `representationType`: literal, evidence, reconstruction, metaphor, or abstract.

An asset enters implementation only when its editorial status is accepted. Verification never implies suitability, and generation never implies either verification or acceptance.

Read [asset-selection.md](references/asset-selection.md). For style, typography, hierarchy, treatments, and text restraint, read [visual-language.md](references/visual-language.md).

## 5. Narration, timing, motion, and transitions

Final narration performance is the authoritative clock. Before that performance exists, storyboard timing is provisional: use semantic anchors and approximate scene-local seconds, and avoid presenting exact global frame ranges as authoritative. After final VO/alignment, align words or phrases and reconcile:

- narration end;
- scene start/end;
- caption start/end and sentence boundaries;
- transition windows;
- SFX attacks/settles;
- declared final hold;
- total composition duration.

Do not cut a scene before its narration/captions resolve. Do not leave an inactive tail after they resolve unless a reviewed hold has an editorial purpose.

Meaningful motion changes state: it reveals, routes, transforms, accumulates, compares, blocks, replaces, or reframes. A static image plus slow zoom is insufficient when the narration is explaining a process or changing ideas. Stillness is valid when it creates tension, gives evidence time to read, or lets a payoff land; record that reason.

Choose repeated-object entrance semantics explicitly:

- `synchronized` when uniformity or one shared event matters;
- `staggered` when sequence, scale, or accumulation matters;
- `sequential` when one state causally enables the next.

Read [motion-patterns.md](references/motion-patterns.md), [transitions.md](references/transitions.md), and [audio.md](references/audio.md).

## 6. Remotion implementation

The implementation agent is primarily an implementer of the frozen visual decision, not a second director.

- Derive render-visible motion from frames and video configuration.
- Use current official Remotion patterns and installed-package APIs.
- Do not use timed CSS transitions/keyframes for render-visible motion.
- Preserve the storyboard's defining objects, relationships, state order, hierarchy, and transition logic.
- Keep scene-local time local and use final alignment for offsets.
- Use deterministic seeded variation; never uncontrolled render-visible randomness.
- Keep text sharp and outside destructive image-treatment filters.
- Verify visible bounds, crops, identity anchors, and settled data labels in actual renders.

Expose a small typed tune surface only for decisions likely to need safe repair. Property controls, parameter manifests, and patches are conditional tools—not requirements for every scene. Studio-specific layer structures are optional unless the project needs manual editability.

Read [remotion-implementation.md](references/remotion-implementation.md).

## 7. Critique and QA

Render representative evidence around semantic moments: anchor, pre-action, defining change, payoff/settle, and handoff. Use short motion previews when timing or camera behavior matters. Build contact sheets with `tools/make_contact_sheet.py` when useful.

### Editorial QA

Evaluate actual storyboard/renders for:

- mute-readable thesis and factual honesty;
- clear focal hierarchy;
- meaningful structure/state changes;
- process/causal legibility;
- anti-slideshow behavior;
- composition, crop, and readable text;
- pacing, holds, and transition intent;
- continuity and construction variety;
- asset suitability and style cohesion;
- sound supporting semantic events without implying unsourced historical authenticity;
- status consistency: script/voice/timing claims do not contradict each other across the approval surface;
- evidence density: visible labels and specifications advance the scene thesis instead of turning the frame into a production/research dashboard.

### Technical QA

Verify:

- render/build/type/lint success as applicable;
- deterministic frame-driven motion;
- timing bounds and declared final hold;
- captions and critical content inside named platform-safe presets;
- asset existence, dimensions, alpha needs, provenance, and lifecycle coherence;
- scene/state IDs preserved from the frozen storyboard;
- representative frames and audio files exist.

Both gates must pass. A technical pass cannot override an editorial revision, and editorial approval cannot waive factual, rights, or rendering failures.

The generating/implementation pass must not self-award `publish_candidate`. Use an independent critic when available. If independent review is unavailable, report `needs_review` rather than claiming production readiness.

Read [critique.md](references/critique.md) and [anti-patterns.md](references/anti-patterns.md). For compact before/correction patterns, read [positive editorial decisions](examples/positive/editorial-decisions.md) and [editorial failures](examples/negative/editorial-failures.md). Use `tools/validate_project.py` for deterministic cross-artifact checks when a project manifest is available. For autonomous stage ownership, bounded retries, approval gates, and resumable execution, read [orchestration.md](references/orchestration.md).

## Artifacts: one source of truth per decision

Do not emit JSON merely because a schema exists. Structured artifacts are optional machine contracts for handoffs, validation, or resumability—not a second creative workspace.

Typical minimum:

- script/research notes in the project's natural format;
- `storyboard.html` or equivalent browser preview as the creative source of truth;
- final render/preview evidence.

Add structured artifacts only when they solve a concrete need:

- `claim-set.json` for evidence-heavy factual work;
- `storyboard-plan.json` to index frozen states across agents or resume runs;
- `asset-manifest.json` when external/generated assets need provenance or acceptance tracking;
- `frame-scene-spec.json` after final VO when timing/alignment needs a machine contract;
- editorial/technical QA reports when another agent or automation consumes verdicts;
- `reference-analysis.json` when references materially drive decisions;
- tune manifests/patches when bounded parameter repair is actually used.

If structured metadata disagrees with an approved HTML storyboard, do not silently trust either copy. Treat it as drift, inspect the approved preview/review evidence, and reconcile the metadata before implementation.

## Stop conditions

Continue until:

- the frozen storyboard has no unresolved editorial blocker;
- accepted assets and final narration are available;
- implementation matches the frozen defining relationships;
- technical QA passes;
- independent editorial QA marks a publish candidate, or the result is clearly labeled `needs_review` when independence is unavailable;
- factual and rights blockers are resolved;
- the requested render/preview exists.

Do not keep adding effects after the thesis, hierarchy, timing, and transitions are resolved.
