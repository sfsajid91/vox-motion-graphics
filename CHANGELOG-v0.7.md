# v0.7 — Implementation Finish Contracts

## Why

v0.6 established the directing model. v0.7 closes the gap between a good
creative plan and a Remotion composition that is visually correct, deterministic,
and editable in Studio.

## Added

- Studio-first layer contract:
  - named `Interactive.*` elements for major editable layers;
  - typed props and inline `defaultProps`;
  - Studio layer-tree verification.
- Explicit repeated-motion entrance modes:
  - `synchronized`;
  - `staggered`;
  - `sequential`.
- Deterministic texture contract for paper, grain, halftone and registration:
  - frame plus stable layer seed for procedural samples;
  - spatially stable treatment unless motion is intentional;
  - text kept outside treatment filters;
  - bounded, editable treatment controls.
- Compositing geometry invariants for fills, tint, grain, outlines and masks.
- Data-graphic finish contract covering locked datasets, shared origins, scale,
  bar geometry, axis alignment and settled-frame legibility.
- Pixel-level diagnostics for entry, in-motion and settled renders.

## Corrected Failure Modes

- Plain `div` layers hidden under `AbsoluteFill` and unavailable in Studio.
- Chart scale and chart origin drifting away from the headline origin.
- Texture clips silently reducing the visible height of bars.
- Animated edge noise reading as fabric or wind instead of printed ink.
- Bar overlays using different bounds from their source bars.
- Staggered entrances appearing where the brief requires synchronized motion.
- Procedural noise implemented with uncontrolled randomness.

## Preserved

- v0.6 editorial physicalization and reference-learning model.
- Optional treatment selection; paper, halftone and grain remain story/style
  decisions, not defaults.
- External critique and no self-awarded production approval.

## Compatibility

No existing schema contract is removed. Existing tune manifests and parameter
patches remain valid; treatment controls should now include bounded density,
size, opacity and edge-variation fields when those treatments are selected.
