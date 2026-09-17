# Remotion Implementation & Tune-Surface Rules v0.6

## Frame-Driven Motion
All timed motion must derive deterministically from the current frame and video config.

Use current Remotion patterns such as:
- `useCurrentFrame()`;
- `useVideoConfig()`;
- `interpolate()` with explicit/clamped ranges;
- `spring()` / easing;
- `<Sequence>` / `<Series>`;
- Remotion media primitives and `staticFile()` conventions.

Do not use timed CSS transitions, CSS keyframes or Tailwind animation/transition classes for render-visible motion.

## Local Scene Time
Inside each scene/sequence, write motion against local frame zero. Convert aligned scene-relative seconds to frames at compile time.

## Parameterize Visual Decisions
Every important composition should expose a tune surface.

High-value tunables:
- focal x/y;
- subject scale/width;
- crop/object position;
- rotation;
- z-index/layer order;
- headline/label x/y/size/max width;
- camera scale/x/y/origin;
- action/entrance/exit offsets;
- spring damping/stiffness/mass or easing family;
- blur/focus/light position/intensity;
- texture/posterization strength;
- SFX offset/level.

Do not expose every CSS property. Expose parameters that a visual critic can reason about.

For layered cutouts, keep asset placement props independent from the whole-scene camera rig. Name them by semantic owner (`subjectScale`, `evidenceX`, `cameraPushScale`, etc.) so a foreground-object scale cannot collide with or silently compound the global camera scale.

When evaluating final size, account for the complete transform chain: asset scale, entrance/hold scale, parent camera scale and overscan. The effective rendered scale—not a single prop value—is what the viewer sees.

## Zod / Studio Property Controls
Where the installed Remotion version supports schemas/property controls, define typed props/defaults for tuneable decisions. Studio controls are useful for debugging and optional manual polish, but Creative Autopilot treats them primarily as a **machine-addressable control surface**.

Example pattern:
```tsx
const SceneProps = z.object({
  heroX: z.number().min(-300).max(300),
  heroY: z.number().min(-500).max(500),
  heroScale: z.number().min(0.5).max(2.0),
  cameraScale: z.number().min(0.8).max(3.0),
  headlineSize: z.number().min(28).max(120),
  actionOffsetFrames: z.number().min(-30).max(60),
});
```

The exact API/imports should follow the installed/current Remotion documentation.

## Tune Manifest
Generate `tunable-parameter-manifest.json` from scene props/config. Include safe min/max/step, semantic role and repair priority.

## Apply Critic Patches
A patcher should be able to apply `parameter-patch.json` without rewriting scene code. Changes should remain deterministic and auditable.

## Premount / Media Reliability
Use current Remotion guidance for premounting, image/media loading and asset readiness. Avoid raw browser loading assumptions when Remotion primitives provide deterministic behavior.

## Determinism
Use seeded/deterministic noise for grain, boil, gate weave or procedural variation. Never use uncontrolled `Math.random()` in render-visible behavior.

## 2.5D Before 3D
Prefer HTML/CSS/SVG transforms, masks, shadows, parallax and compositing. Use true 3D only when story geometry genuinely requires it.

## Semantic Primitives
Reusable rigs may include:
- CameraRig
- LayeredCutout
- GroundedShadow
- Paper/Card placement
- CountUp
- PathDraw
- Highlight/Underline
- LightCone
- FocusHunt
- PosterizeMotion
- ObjectPortal
- TypewriterReveal
- NetworkFlow
- PropCascade
- DampedGesture
- HoldFlicker

These are mechanics, not complete scene templates.

## Current Docs Rule
When implementing in a live repo, current installed package documentation / official Remotion guidance overrides remembered API details.
