# External Critic & Autonomous Art-Direction Loop v0.6

## Why This Exists
The supplied reference workflows repeatedly reached final quality by **watching renders and manually adjusting composition/timing**. Creative Autopilot must reproduce that last mile without asking the user to become a motion designer.

## No Self-Certification
The generation/planning agent may list risks and uncertainties only. It must not produce its own:
- PASS / FAIL;
- 5/5 scores;
- ELIMINATED labels;
- approved / production-ready claims.

A separate critic evaluates actual renders/assets.

## Diagnostic Render Set
For each scene sample semantic moments rather than arbitrary intervals:
- entry/anchor;
- just before primary action;
- signature moment;
- consequence/payoff;
- exit/handoff.

Also render a short low-resolution motion preview when timing/camera/secondary motion is the likely problem.

For a multi-beat scene, sample each handoff separately. A useful minimum is: accepted/previous payoff, new-beat entry, new-beat settle and exit. A correct final frame cannot prove that the focal transition works.

When invoking multiple Remotion still renders locally, avoid launching independent bundlers concurrently against the same webpack cache. Render sequentially or reuse one bundled render surface; cache rename/ENOENT warnings are evidence of contention even if individual frames eventually succeed.

## Critic Dimensions
- mute-readable visual thesis;
- editorial mechanism clarity;
- focal hierarchy;
- gaze/attention continuity from previous scene and into next;
- composition/crop/platform-safe layout;
- asset silhouette/readability;
- depth/contact/occlusion, including whether foreground evidence hides a face or other identity anchor;
- semantic motion clarity;
- narration sync;
- motion variety / intentional holds;
- construction diversity across neighboring scenes;
- text restraint/readability;
- style/world cohesion;
- audio/SFX sync;
- evidence/representation honesty;
- asset/provenance quality;
- complexity efficiency.

## Mute Test
Without narration, can the critic describe the intended state change or relationship? If not, adding text is not the first repair.

## Parameter-First Repair
Expose and patch high-leverage parameters:
- x/y;
- scale/width;
- rotation;
- crop/object-position;
- z-order;
- text size/position;
- camera scale/origin/offset;
- entrance/action/exit timing;
- easing/spring parameters;
- treatment intensity;
- blur/focus/light position;
- SFX offset/level.

For subject-plus-object compositions, try x/y/scale separation before fading the subject away. Foreground evidence may cover a torso or lower edge for depth, but should not cover a face, logo or essential evidence detail unless that occlusion is the semantic action.

## Accepted Anchor Frames
When the user accepts a particular composition or final frame, record it as an anchor diagnostic. Later additions may precede or follow it, but should preserve its focal hierarchy, crop and readable hold unless the user explicitly changes that direction.

After extending or re-sequencing a scene, rerender the anchor frame alongside the new beat. This catches timing shifts, compounded camera scale and overlay leakage that source review alone misses.

## Tune-Surface Contract
Implementation should emit `tunable-parameter-manifest.json` describing parameters and safe ranges. The critic should emit `parameter-patch.json` when the problem can be solved without redesign.

A patch must explain:
- target scene;
- parameter name;
- old/new value;
- reason;
- expected visual effect;
- confidence.

## Targeted Variant Search
For a low-dimensional composition issue, render a small set of controlled variants:
- focal x/y alternatives;
- scale ±5–15%;
- two camera depths;
- two crop positions;
- two timing offsets.

Critic selects the best candidate. Do not brute-force large grids.

## Gaze Repair
If a cut feels visually disconnected, first test:
- moving the next scene’s entry focal point toward the previous exit zone;
- continuing or intentionally reversing motion direction;
- carrying a line/object/color token across the cut;
- using a macro<->micro scale match.

## Concept-Level Failure
Redesign when:
- visual thesis remains unclear after two parameter repair cycles;
- metaphor is misleading or evidence-unsafe;
- assets cannot support required motion;
- composition can only be saved by explanatory text;
- scene duplicates neighboring construction too closely;
- the signature mechanism is visually weak even when well composed.

## High-Uncertainty Hero Scenes
Before full implementation:
1. create 2–4 cheap concept cards/stills;
2. render low-resolution diagnostic variants;
3. use the external critic to select one;
4. discard unselected concepts;
5. only then invest in detailed assets/motion.
