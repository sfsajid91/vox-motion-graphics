# Property Controls as an Autonomous Art-Direction API

## Purpose
Remotion property controls/default props are not merely conveniences for a human slider session. In Creative Autopilot they form a **bounded, typed control surface** that an external visual critic can tune safely.

## What to Expose
Expose only parameters with meaningful visual leverage:

### Composition
- heroX / heroY;
- heroScale / width;
- crop/objectPosition;
- headlineX/Y/size/maxWidth;
- foreground/background depth;
- z-order variants.

### Camera
- cameraX/Y;
- cameraScale;
- transform origin / pivot;
- push depth;
- travel distance.

### Timing
- entrance offset;
- action offset;
- settle duration;
- transition offset;
- spring/easing family and bounded physical parameters.

### Treatment
- shadow strength/offset;
- blur/focus;
- light cone angle/intensity;
- grain/halftone/posterization strength when selected by style.

### Audio
- SFX offsets;
- SFX relative level;
- music duck amount when needed.

## What Not to Expose
Avoid hundreds of arbitrary CSS values. A control surface should make likely critic repairs easy and safe.

## Typed Bounds
Every tunable should define:
- type;
- current/default value;
- min/max or allowed enum;
- step;
- semantic role;
- repair priority.

Record in `tunable-parameter-manifest.json`.

## Critic Patch Flow
1. render diagnostic frame/preview;
2. critic identifies problem in visual language;
3. map problem to tunable parameters;
4. emit `parameter-patch.json`;
5. apply patch;
6. rerender only affected diagnostics;
7. compare before/after;
8. accept patch only if critic confirms improvement.

## Examples
Problem: hero feels too small / weak hierarchy.
- patch `heroScale: 1.0 -> 1.15`
- perhaps `cameraScale: 1.0 -> 1.06`

Problem: cut loses attention continuity.
- patch next scene `heroX` toward previous exit zone;
- shift entrance origin/direction;
- preserve continuity line/object.

Problem: payoff fires before narration lands.
- patch `payoffOffsetFrames` later;
- extend settle/hold rather than adding effects.

## Studio as Fallback
Human Studio tuning remains valuable for:
- optional final polish;
- debugging a parameter range;
- brand/client-directed adjustments.

But the default user should not be asked to manually tune coordinates/easing.
