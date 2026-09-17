# AI Video Director v0.7 — Creative Autopilot + Finish Contracts

Drop-in successor to `vox-motion-graphics` v0.6.

Start with `SKILL.md`.

## What v0.7 adds
v0.7 keeps the v0.6 directing, evidence and reference-learning model and adds implementation safeguards learned from a Remotion chart build:
- **Studio-first structure**: major visual layers use named `Interactive.*` elements and typed inline defaults.
- **Deterministic treatment**: procedural grain derives from frame plus stable layer seeds; static print texture does not accidentally animate.
- **Compositing invariants**: fill, tint, grain, outline and mask layers preserve the same source bounds.
- **Data-graphic finish contract**: dataset, origins, scale, axis, bar geometry, entrance mode and settled-frame legibility are explicit.
- **Entrance modes**: synchronized, staggered and sequential motion are declared instead of inferred.
- **Pixel-level finish checks**: inspect actual entry, in-motion and settled renders and confirm Studio layer visibility.

It still rejects overfitted universal rules: mandatory paper/halftone/grunge, fixed scene counts, fixed audio ratios, one sentence = one scene, mandatory conflict, fixed safe zones and self-awarded QA.

## Validation
Run:
```bash
python tests/test_schemas.py
```

The package validates all schema files and checks important guardrails such as:
- generator cannot self-mark scene QA as pass;
- evidence scenes require claim references;
- literal historical assets cannot route directly to generation;
- rights cannot be marked verified without provenance/license/evidence.

## Philosophy
**Learn why the reference works, then invent a fresh solution for the new story.**
