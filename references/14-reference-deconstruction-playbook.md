# Reference Video Deconstruction Playbook

## Goal
Learn a creator's **decision grammar** without turning the creator's specific compositions, assets or treatments into universal templates.

## When to Use
Use when the user provides:
- a reference video;
- a practice kit;
- storyboard/prompt/assets from another creator;
- “make it feel like this” examples;
- a corpus intended for creative learning.

## Step 1 — Segment by Visual Ideas
Do not blindly split every five seconds.

Find:
- scene/world changes;
- major composition changes;
- signature motion events;
- camera transition boundaries;
- meaningful long holds;
- sound-driven visual hits.

Fixed-interval samples are useful only as a supplementary inspection grid.

## Step 2 — Build Diagnostic Contact Sheets
Capture frames at:
- scene entry;
- pre-action;
- signature moment;
- payoff/settle;
- exit/handoff.

For continuous camera scenes, sample important waypoints.

Use `tools/make_contact_sheet.py` if useful.

## Step 3 — Deconstruct Each Scene
Record:
- semantic job / narration beat;
- visual thesis;
- construction family;
- anchor/action/consequence/launchpad;
- focal entry/exit zones;
- layer stack (background/midground/foreground);
- primary mechanism;
- secondary/ambient motion;
- camera geometry;
- motion personality;
- treatment / texture;
- text role;
- SFX/music events;
- transition logic;
- reusable rig/primitive;
- what would fail if copied into a different story.

## Step 4 — Classify Findings
Every observation must be tagged:

### `creator_dna`
Repeated high-level principle likely transferable.
Examples: few assets/high choreography; semantic SFX; visual transformations; render/tune loop.

### `surface_style`
Optional aesthetic.
Examples: halftone portraits, cream paper, red offset stroke, scan lines, vintage grain.

### `technique_recipe`
Reusable implementation move.
Examples: weld/detach portal, floor-shadow 2.5D, swinging lamp cone, staggered paper cascade.

### `benchmark_specific`
Exact source-video choice that should not generalize.
Examples: exact frame count, exact scene layout, exact person/prop, exact camera coordinate, story-specific statistic.

## Step 5 — Promote Only Repeated Principles
One clever scene is not automatically creator DNA.

Across multiple references ask:
- what repeats despite different topics?
- what is a one-off aesthetic?
- what is caused by the story rather than creator preference?
- what is a reusable rig?
- what is only an exact benchmark fact?

Promote repeated high-confidence patterns to creator-DNA references.

## Step 6 — Convert to New-Story Questions
Never tell the new project “copy Scene 3.”
Instead ask:
- what is this new scene's semantic job?
- does it need the same relationship geometry?
- is there a technique from the reference that solves that geometry?
- how should the material world and assets change?

## Reference Analysis Contract
Use `reference-analysis.schema.json` when structured handoff is useful.

## Copyright / Originality Principle
The system learns directing concepts, editing grammar and technical patterns. It should not redistribute source asset packs or reproduce a reference's exact sequence by default. Create a fresh composition appropriate to the new story.
