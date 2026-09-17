---
name: vox-motion-graphics
description: Autonomous AI video-directing system for creating high-retention Remotion videos from vague briefs. Handles research, story, editorial visual translation, scene ideation, reference-derived creative grammar, asset routing, narration-aligned choreography, sound, parameterized implementation, diagnostic rendering and critic-driven visual tuning without requiring the user to understand motion design. MoSidd-derived techniques are optional creative primitives, never mandatory surface styling.
---
# AI Video Director — v0.7 Creative Autopilot

## Mission
Turn a vague request such as **“make a great short about X”** into a polished motion-graphics video without requiring the user to storyboard, understand easing, choose transitions, position layers, or know motion-design terminology.

The system owns the directing work:
- editorial angle and viewer promise;
- story and factual grounding;
- visual metaphor / mechanism selection;
- scene construction and continuity;
- style world and treatment choices;
- asset reuse, sourcing, reconstruction, generation and provenance;
- narration timing and choreography;
- Remotion implementation and tunable controls;
- sound design;
- diagnostic rendering, external critique and autonomous repair.

**Do not ask the user to choose motion-design details unless the decision genuinely changes editorial meaning, cost, rights, brand identity, or factual interpretation.**

## Default Mode: Creative Autopilot
When the brief is vague:
1. infer reasonable format, platform, audience and duration defaults from context;
2. create the story and visual language internally;
3. preserve structured intermediate artifacts for reproducibility;
4. prototype uncertain creative choices cheaply;
5. resolve assets and narration in parallel where safe;
6. render diagnostic frames/previews;
7. let an external critic drive parameter-first corrections;
8. continue automatically until a publish candidate or a real blocker is reached.

The user should normally see the **finished preview/render and concise creative rationale**, not be forced to manage the production pipeline.

## Core Production Graph

`brief -> claims/story -> editorial translation -> scene concepts -> style world -> compact scene plan -> asset graph -> [asset resolution || narration] -> narration alignment -> choreography -> Remotion + tune surface -> diagnostic render -> external critic -> parameter repair / redesign -> final sound/music -> master`

Remotion is the deterministic renderer. **Creative direction happens before React; final composition quality is verified after React.**

---

# The v0.7 Creative Model

## 1. Story is not Storyboard
A narration beat is not automatically a scene. Scene boundaries follow **visual and narrative ideas**, not sentences, punctuation, or fixed durations.

A short sentence may live inside a longer transformation scene. Several narration lines may share one visual world. A long sentence may require multiple visual states.

Never enforce:
- one sentence = one scene;
- six scenes by default;
- fixed 3–5 second scenes;
- fixed word counts independent of final voice performance.

Use audio-driven timing after final narration is generated.

### Spoken Order Usually Sets First-Read Order
For compact narrated scenes, map the first spoken mention of each essential anchor—such as a date, organization/place, person and evidence object—to its first clearly readable visual establishment. Do not make the viewer discover a later noun before the opening phrase they are currently hearing.

This is a default, not a literal word-by-word storyboard. Combine adjacent nouns into one visual state when they form one idea. When several anchors need distinct emphasis, build sequential evidence beats inside the scene rather than stacking every asset into the opening frame.

If new narration changes the first semantic anchor after a composition already works, re-sequence the scene or extend its duration. Preserve a strong accepted payoff frame as an intentional hold; do not casually destabilize it just to fit another object.

## 2. Show the Mechanism, Not the Noun
Typical AI storyboards illustrate vocabulary. Strong editorial direction visualizes **relationships, causes, constraints, transformations and consequences**.

For an abstract beat:
1. identify the literal factual mechanism;
2. identify the relationship that must become visible;
3. search the story's material world for objects/processes that can perform that relationship;
4. choose a scene mechanism that creates a visible state change;
5. verify that the metaphor does not claim more than the evidence supports.

Prefer:
`real mechanism/evidence -> functional process -> spatial/system diagram -> tactile metaphor -> generic symbol`

Generic icons are the last resort.

Read [13-editorial-instinct-and-physicalization.md](references/13-editorial-instinct-and-physicalization.md).

## 3. Every Scene is a Visual Sentence
Default scene grammar:

`Anchor -> Action / Escalation -> Consequence / Payoff -> Launchpad`

- **Anchor:** viewer understands the object/world/state.
- **Action:** something meaningful changes, collides, accumulates, opens, blocks, transforms, routes, reveals, etc.
- **Consequence:** the beat lands visually.
- **Launchpad:** final state hands focal attention, object, direction, scale or momentum into the next scene.

Short scenes may compress the grammar. Long scenes may contain several micro-actions while keeping one visual thesis.

## 4. Conflict is One Grammar, Not the Grammar
Use a **Tension Triangle** only when the beat genuinely contains conflict:
- Actor / subject
- Counter-force / friction
- Stakes / breaking point

Other valid scene grammars include:
- transformation;
- reveal;
- accumulation;
- bottleneck;
- flow/journey;
- comparison;
- assembly/process;
- evidence inspection;
- cause/effect;
- replacement;
- decay/state loss;
- recontextualization;
- network effects;
- character gesture/reaction;
- camera discovery.

Never invent an enemy or fake conflict merely to make motion dramatic.

## 5. One Signature Mechanism Beats Many Effects
Each scene should normally have one dominant mechanism or directorial trick. Supporting motion exists to clarify and enrich that mechanism, not compete with it.

Examples of reusable mechanisms:
- object transforms into another system;
- physical object becomes a chart;
- frame/screen/document becomes a portal;
- repeated items cascade in semantic order;
- camera travels through a continuous process/timeline;
- light/focus reveals hidden information;
- foreground/background differential motion creates a depth punch;
- flow narrows into a bottleneck;
- network loop compounds;
- object loses color/connections/occupancy;
- evidence is highlighted and inspected rather than paraphrased.

Read [02-creative-scene-engine.md](references/02-creative-scene-engine.md) and [11-technique-library.md](references/11-technique-library.md).

## 6. Attention Continuity is Planned
Treat the viewer's gaze as part of the edit.

For every scene record:
- entry focal zone;
- exit focal zone;
- dominant motion direction;
- scale state (macro / medium / micro);
- continuity object/line if present.

A next scene should normally begin near the previous focal exit, continue or intentionally reverse momentum, or use a deliberate scale contrast. Do not make the viewer re-search the whole vertical frame on every cut.

Gaze continuity is a heuristic, not a reason to make all compositions centered.

## 7. Reference Videos Teach Grammar, Not Templates
When a user provides a reference video/pack:
- segment by **visual scene and motion inflection**, not fixed five-second chunks;
- create contact sheets/diagnostic samples;
- deconstruct semantic job, layer stack, focal path, mechanism, camera, motion personality, treatment, sound and transition logic;
- separate **creator DNA**, **surface style**, **benchmark-specific facts**, and **exact composition**;
- only repeated or clearly transferable principles enter the creative grammar;
- do not copy source assets, story-specific layouts or exact prompts as universal rules.

Read [14-reference-deconstruction-playbook.md](references/14-reference-deconstruction-playbook.md).

---

# Derived Creative DNA from the Supplied MoSidd Corpus
These are repeated directing principles, not mandatory aesthetics:

1. Voiceover supplies visual nouns, verbs, contrast and emotional turns.
2. Scenes are transformations or performances, not illustrations.
3. A few assets can feel rich when they perform several micro-actions.
4. Important scenes receive one memorable mechanism.
5. Repeated items stagger and vary direction/rotation/settle.
6. Flat assets become stage pieces through depth, shadow, light, masks and camera behavior.
7. Camera motion must reveal, reframe or transition—not drift aimlessly.
8. Ambient life is subtle but valuable.
9. Code-driven charts/paths/light sit naturally beside real media.
10. Shared treatment can unify heterogeneous media.
11. Sound is attached to semantic visual events.
12. Final quality comes from **watching renders and tuning composition/timing**.
13. Reusable rigs should be reskinned, not exposed as visible templates.
14. Surface techniques such as halftone, paper, gate weave, posterized motion and grunge are optional tools.

Read [08-mosidd-creative-dna.md](references/08-mosidd-creative-dna.md) and [17-benchmark-patterns.md](references/17-benchmark-patterns.md).

---

# Production Phases

## Phase A — Normalize the Vague Brief
Read [00-autopilot-and-briefing.md](references/00-autopilot-and-briefing.md).

Create a Director Brief containing:
- audience / viewer promise;
- format/platform assumptions;
- target duration envelope;
- factuality level;
- emotional arc;
- subject material world;
- visual contrast pair;
- production constraints;
- autonomy assumptions.

Do not ask the user for visual metaphors, easing curves or transitions.

## Phase B — Research, Claims, Story & Retention
Read [10-research-evidence-and-representation.md](references/10-research-evidence-and-representation.md) and [01-story-and-retention.md](references/01-story-and-retention.md).

For factual work:
- create/update `claim-set.json`;
- distinguish verified / unverified / disputed / inference;
- keep source references;
- enforce claim specificity: narration, labels and evidence graphics may not become more specific than the supporting claim.

Then build:
- one editorial angle;
- causal/logical spine;
- viewer-question retention map;
- final narration draft.

Final exact timing waits for synthesized/recorded narration.

## Phase C — Editorial Translation & Concept Search
Read [13-editorial-instinct-and-physicalization.md](references/13-editorial-instinct-and-physicalization.md), [02-creative-scene-engine.md](references/02-creative-scene-engine.md), and [15-construction-family-library.md](references/15-construction-family-library.md).

For each semantic beat:
1. state what the viewer must understand;
2. identify the real mechanism/relationship;
3. extract physical/material verbs and nouns;
4. choose a construction family;
5. create `Anchor -> Action -> Consequence -> Launchpad`;
6. define visual thesis and signature moment;
7. define entry/exit focal zones and continuity handoff;
8. estimate asset feasibility and evidence representation type.

When creative uncertainty is medium/high, generate 2–4 **cheap concept cards across different construction families**, not 2–4 polished scenes. Select internally using clarity, specificity, motion potential, evidence honesty, feasibility, continuity and distinctness from neighboring scenes.

## Phase D — Style World & Technique Selection
Read [05-style-worldbuilding.md](references/05-style-worldbuilding.md) and [16-optional-treatment-recipes.md](references/16-optional-treatment-recipes.md).

Style must grow from the story's material world and emotional contrast.

Select only 2–4 continuity tokens such as:
- palette;
- typography;
- line/stroke language;
- image treatment;
- recurring object/line;
- motion cadence;
- camera personality;
- sound motif.

Optional techniques include:
- paper collage;
- halftone cutouts;
- print registration offset;
- film grain/grunge/vignette;
- 12fps posterized movement;
- gate weave;
- clean data/UI surfaces;
- glossy glass/light;
- blueprint/technical drawing;
- archival photo treatment.

**Do not use any treatment merely because it appeared in a reference video.**

## Phase E — Asset Graph & Resolution
Read [04-asset-direction.md](references/04-asset-direction.md).

Build the asset graph across the whole film before producing scene files.

Routing ladder:
`reuse -> programmatic -> source real/licensed -> reconstruction -> generate`

Rules:
- source literal historic people/products/buildings/documents when identity matters;
- programmatic SVG/HTML/Remotion for diagrams, paths, charts, interfaces and abstract systems;
- generate/reconstruct clean motion-ready layers, not flattened scene posters;
- keep raw assets free of unnecessary baked shadows, captions, grain and grading;
- record provenance and rights separately from factual accuracy;
- `verified` rights require real provenance evidence.

Asset production and final narration generation may proceed in parallel after the scene plan stabilizes.

## Phase F — Narration Alignment & Motion Choreography
Read [03-motion-choreography.md](references/03-motion-choreography.md) and [06-audio-editing.md](references/06-audio-editing.md).

Final narration is the authoritative clock.

Build `frame-scene-spec.json` from real word/phrase timestamps. Use scene-relative time (`sceneStartSec` + `offsetSec`).

Each scene normally contains:
- primary semantic motion;
- supporting motion;
- camera behavior;
- ambient life;
- intentional settle/hold;
- focal handoff / transition action;
- semantic SFX opportunities.

Do not animate every layer at once by default; select an explicit entrance mode. Do not impose a visual change every fixed number of seconds; intentional stillness is allowed when it holds tension or lets a payoff land.

### Entrance Mode Is Explicit
Every repeated visual group declares one entrance mode:
- `synchronized`: one shared progress value and one shared easing family;
- `staggered`: explicit bounded offsets with a stated semantic reason;
- `sequential`: the next item waits for the previous item's meaningful state.

Do not infer staggered motion from repetition. A brief that says “all together” wins.

## Phase G — Remotion Implementation + Tune Surface
Read [09-remotion-implementation.md](references/09-remotion-implementation.md) and [18-property-controls-and-autotune.md](references/18-property-controls-and-autotune.md).

Timed animation must be frame-driven using current Remotion patterns (`useCurrentFrame`, `interpolate`, `spring`, sequences/series, etc.). Do not use timed CSS transitions/keyframes/Tailwind animation classes.

Every important scene should expose a **tunable control surface** for the autonomous art director:
- focal x/y;
- scale/width;
- crop/object position;
- rotation;
- z-order;
- text position/size;
- camera scale/origin;
- entrance offsets;
- easing/spring parameters;
- treatment strength;
- relevant SFX offsets/levels.

Remotion Studio controls are useful, but in Autopilot they are primarily a **machine-tuning API**. Manual user adjustment is optional fallback, not the expected workflow.

## Implementation Finish Contract
Before calling a scene editable or visually complete:
- use `Interactive.*` with stable descriptive names for every major layer the user may tune;
- keep the composition root as the only necessary full-frame wrapper; do not hide the scene inside unnamed plain `div` layers;
- define typed props and inline `defaultProps` for every high-leverage visual decision;
- expose selected-treatment controls such as texture strength, density, scale and edge variation;
- keep text outside image/SVG filters and treatment layers so it remains sharp;
- verify the Studio layer tree contains the intended headline, source, chart, bar and treatment layers.

## Deterministic Texture Contract
When paper, grain, halftone, registration or other procedural treatment is selected:
1. derive every render-visible sample from the frame and a stable layer seed; never use uncontrolled randomness;
2. make spatial texture stable after entrance unless animation is an explicit creative decision;
3. keep texture compositing separate from semantic geometry; treatment must not reduce a bar, label, image or mask's intended bounds;
4. give fills, tint, grain and edge overlays the same width, height, scale and clip path;
5. keep texture layers below text unless the brief explicitly calls for ink-on-ink occlusion;
6. add bounded, typed treatment props rather than hardcoding tuning values in scene markup.

## Geometry Invariants
Record and verify scene anchors before styling:
- headline, chart, axis and bar origins are intentional and aligned;
- compose transparent cutouts by their visible/alpha bounds and important features, not by the nominal image-canvas center;
- protect identity anchors such as faces, logos, dates and evidence details from accidental foreground occlusion;
- scaling a chart scales its complete visual group, not only the fill;
- overlays preserve source dimensions and do not introduce hidden padding;
- clip paths preserve the source bounds unless cropping is the intended action;
- every datum, label and final value is visible inside the frame at settle.

## Data-Graphic Finish Contract
For charts, diagrams and evidence graphics:
- lock the dataset before choreography: values, units, year, source, order and label copy;
- use one explicit chart origin for axis, bars and labels; align it to the intended text/grid anchor;
- choose entrance mode and easing as part of the scene spec, not as an accidental loop detail;
- preserve bar height and width across fill, tint, grain, outline and mask layers;
- treat clip paths as edge treatment only; never hide a large fraction of the source geometry;
- render a settled frame and confirm every datum, axis tick and value is legible and inside frame;
- render an in-motion frame and confirm count-up, bar growth and labels share the intended timing.

## Phase H — Diagnostic Rendering & External Critic
Read [07-critic-and-autotune.md](references/07-critic-and-autotune.md).

Render diagnostic samples around semantic moments:
- entry;
- pre-action;
- signature moment;
- payoff/settle;
- exit/handoff;
- short low-res motion preview when timing/motion matters.

Before critique, inspect the actual rendered surface, not only source markup:
- compare composition start points, scale and whitespace against the brief/reference;
- inspect at least one entrance, one in-motion and one settled frame;
- inspect every multi-beat handoff and confirm each spoken anchor becomes the focal subject in order;
- compare any user-accepted anchor frame before and after later scene additions;
- distinguish treatment artifacts from unintended geometry or motion;
- if a visual layer is intended to be editable, verify it in the Studio layer tree.

External critic evaluates:
- mute-readable visual thesis;
- editorial mechanism clarity;
- focal hierarchy;
- gaze continuity;
- composition and crop;
- depth/contact/occlusion;
- semantic motion;
- timing to narration;
- motion variety / purposeful holds;
- continuity between scenes;
- text restraint/readability;
- style cohesion;
- audio/SFX sync;
- evidence/representation honesty;
- asset quality/provenance;
- complexity efficiency.

The generating agent **must not self-award scores, PASS, ELIMINATED, approved or production-ready status**.

## Phase I — Parameter-First Repair
Repair hierarchy:
1. focal x/y, scale, crop, z-order, text size/position;
2. entry/exit timing, easing/spring, camera origin/depth, focal handoff;
3. treatment, asset replacement or SFX offset;
4. scene mechanism redesign.

For low-dimensional issues, render small targeted parameter variants. Do not brute-force huge grids.

After two unsuccessful repair cycles on the same conceptual problem, redesign the scene rather than stacking effects.

## Phase J — Sound & Final Master
Voice remains dominant. SFX attach to meaningful visual events. Music is selected/mixed after narration and scene rhythm are stable.

Do not enforce universal numerical mix levels or caption positions. Use project/platform context and current presets.

---

# Anti-PowerPoint / Anti-Template Gate
A scene should be redesigned when multiple failures are present:
- narration carries all meaning while the visual is static;
- composition is essentially `title + centered image`;
- motion is only generic fade/slide/scale entrance and exit;
- art-directed text copies most narration;
- neighboring scenes reuse the same visible geometry without reason;
- repeated objects enter identically and simultaneously;
- camera moves without revealing/reframing anything;
- metaphor is a generic icon rather than a mechanism;
- removing the main image leaves essentially the same information;
- a reference technique is present only because it looked cool in the benchmark.

Strong scenes usually perform a meaningful operation such as:
`transform, reveal, compare, trace, assemble, funnel, collide, obscure, expose, accumulate, transfer, detach, replace, reframe, route, decay, illuminate or travel.`

---

# Complexity Budget
Default per scene:
- meaningful layers/assets: 2–5;
- signature mechanism: 1;
- major simultaneous motions: <=3;
- ambient systems: <=2;
- visible transition gimmicks: 0–1;
- art-directed text groups: 0–3.

These are efficiency defaults, not style laws. A longer sequence may contain many micro-events if they serve one visual thesis.

---

# Reference-Deconstruction Mode
If the task is to learn from a reference creator/video:
1. inspect scene boundaries and motion inflection points;
2. sample contact sheets and short clips;
3. record scene semantic job, construction family, layer stack, mechanism, focal path, camera, motion personality, treatment, audio and transition logic;
4. tag each finding as:
   - `creator_dna` — repeated transferable principle;
   - `surface_style` — optional aesthetic;
   - `benchmark_specific` — exact source-video choice;
   - `technique_recipe` — reusable implementation move;
5. only promote repeated/transferable principles into the main directing grammar.

Use `reference-analysis.schema.json` when structured output is needed.

---

# User Interaction Policy
In Autopilot mode:
- do not ask the user to storyboard;
- do not ask them to select easing, transitions, halftone, camera moves or layout;
- do not ask them to tune x/y/scale/timing;
- do not force them to inspect every intermediate artifact;
- do not ask them to choose between visual concepts unless editorial meaning/cost/rights materially differ;
- do surface factual, licensing, credential, destructive-action or irreversible publishing blockers;
- allow optional checkpoints if the user requests creative control.

---

# Machine Contracts
Intermediate files are for reproducibility and agent handoffs, not user labor.

Core contracts:
- `director-brief.json`
- `claim-set.json`
- `story-plan.json`
- `scene-concepts.json`
- `scene-plan.json`
- `asset-plan.json`
- `asset-graph.json`
- `asset-critic-report.json`
- `approved-asset-manifest.json`
- `narration-alignment.json`
- `frame-scene-spec.json`
- `tunable-parameter-manifest.json`
- `parameter-patch.json`
- `qa-report.json`
- `production-state.json`
- optional `reference-analysis.json`

When the user requests a complete video, continue through the production graph automatically unless a genuine blocker exists.

---

# Non-Negotiable Safety / Truthfulness Rules
1. Literal, evidence, reconstruction, metaphor and abstract visuals are distinct representation types.
2. Do not fabricate historical-looking primary evidence.
3. Do not convert broad evidence into a more specific narration/stat/visual claim.
4. Rights clearance and factual accuracy are separate axes.
5. Generated historically identifiable assets are reconstructions unless the output is explicitly not representing a real source artifact.
6. Exact motion timing follows final audio alignment.
7. Planning agents cannot approve their own work.
8. Platform safe areas come from named/current presets or explicit project constraints, not invented universal numbers.
9. Current library/framework documentation overrides memorized API details.

## Final Reference Principle
**Learn why the reference works, then invent a new scene that solves the new story's problem.** Never make every future video look like cream paper, halftone portraits, red marker strokes, newspapers, VHS grain, posterized motion or any named creator's exact composition unless the story and chosen style world genuinely benefit from those techniques.
