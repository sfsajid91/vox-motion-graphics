# Autonomous Production Orchestration v0.6

## Internal Stage Graph

`brief`
→ `research/claims`
→ `story-plan`
→ `editorial translation`
→ `scene concepts`
→ `style world`
→ `scene-plan`
→ `asset graph`
→ parallel `{asset resolution || narration generation}`
→ `narration alignment`
→ `frame-scene-spec`
→ `Remotion + tunable parameter manifest`
→ `diagnostic renders`
→ `external critic`
→ `{parameter patch -> rerender | concept redesign}`
→ `final SFX/music/captions`
→ `master / platform variants`

## User Should Not Manage This
The user may provide only a topic and objective. Intermediate artifacts are internal contracts, not required manual steps.

## Scene-Level Parallelism
After story/style/scene-plan stabilize:
- source/generate independent assets in parallel;
- build reusable programmatic primitives in parallel;
- generate narration in parallel with asset resolution;
- do not commit exact choreography until narration alignment exists.

## Gates

### Story Gate
Proceed when:
- angle is clear;
- causal/logical spine is coherent;
- factual claims needed for narration are sufficiently grounded;
- payoff answers the opening promise.

### Concept Gate
Proceed when:
- each scene has a mute-readable visual thesis;
- mechanism is more specific than generic iconography;
- neighboring construction families are sufficiently varied;
- attention handoff is plausible;
- representation type is honest.

### Asset Gate
Proceed when:
- recurring assets are deduplicated in the asset graph;
- literal evidence assets have source/provenance strategy;
- programmatic assets remain editable;
- generated/reconstructed assets are motion-aware layers, not flattened scenes.

### Choreography Gate
Proceed when final narration alignment exists and scene-relative timing is used.

### Render Gate
First render is diagnostic. Render semantic samples/contact sheet and low-res preview before expensive final output.

### Critic Gate
Only external critic can assign publish/revise/fail status.

### Publish Gate
Proceed when:
- critic marks publish candidate;
- rights/factual blockers are resolved;
- final audio/captions/platform layout are checked.

## Failure Routing
- fact problem -> research/claims;
- weak hook/payoff -> story;
- boring/static scene -> editorial translation / concept engine;
- repeated visual template -> construction-family selection;
- rights problem -> asset director;
- bad composition -> parameter patch;
- bad gaze handoff -> focal continuity repair;
- bad asset -> replace/re-source;
- bad timing -> alignment/choreography;
- persistent conceptual failure after two repair cycles -> redesign scene.

## Reference Learning Branch
If references are provided, run deconstruction before style/scene ideation:
`reference media -> scene segmentation -> contact sheets -> structured reference-analysis -> creator DNA / technique recipes -> normal creative pipeline`

Reference analysis informs choices; it does not bypass the story-specific concept stage.
