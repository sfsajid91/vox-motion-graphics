# Remotion Implementation

Use this reference after storyboard freeze.

## Implement the frozen decision

Preserve:

- scene and state order;
- visual thesis and focal hierarchy;
- defining object/causal relationship;
- accepted asset identity;
- transition job and focal handoff;
- intentional holds.

Implementation may refine interpolation, easing, overlap, compositing, and performance. If it changes the thesis, focal owner, defining relationship, accepted hero asset, or transition logic, return to storyboard review.

## Deterministic frame-driven motion

Use current official patterns from the installed Remotion version, such as frame/config hooks, interpolation, springs/easing, sequences/series, and Remotion media primitives.

- Write scene motion against local frame zero.
- Convert aligned seconds to frames at the implementation boundary.
- Clamp interpolation where overshoot would break composition.
- Use stable seeds for render-visible procedural variation.
- Do not use timed CSS transitions, CSS keyframes, or browser-time animation for render-visible motion.

Current installed documentation overrides remembered APIs.

## Component boundaries

Keep the composition registry thin. Place scene-specific components, props, and data under the project/scene boundary. Name layers and parameters by semantic owner so local asset transforms cannot silently collide with camera transforms.

Property controls and interactive Studio layers are optional. Use them when manual editability or bounded critic repair is valuable, not as a universal finish requirement.

## Small tune surface

Expose only high-leverage repair decisions, for example:

- focal x/y and scale;
- crop/object position;
- headline position/size;
- camera origin/depth;
- action/settle/transition offsets;
- chosen treatment strength;
- relevant SFX offset/level.

Use typed bounds. Avoid exposing arbitrary CSS. Emit a tune manifest/parameter patch only when the workflow will consume it.

## Geometry and compositing

- Compose cutouts using visible/alpha bounds and important features.
- Account for the complete transform chain, including asset, entrance, camera, and overscan scale.
- Preserve faces, logos, dates, and evidence details from accidental occlusion.
- Keep fills, tint, grain, outlines, masks, and clip paths on consistent source bounds.
- Keep text outside image filters unless occlusion is intentional.
- Preserve the owning scene's background across nested panels and embedded playback.

## Charts and evidence graphics

- Lock values, units, date range, source, order, and label copy before choreography.
- Use one explicit origin for axes, marks, and labels.
- Scale the complete chart group rather than only its fill.
- Keep overlays and masks on the source geometry.
- Render entry, in-motion, and settled states; verify all data and labels remain legible and in frame.

## Media and reliability

Use current Remotion guidance for media loading, premounting, asset readiness, and fonts. When rendering many stills locally, avoid concurrent bundlers fighting over the same cache; reuse one bundle or render sequentially.

Prefer HTML/CSS/SVG/2.5D compositing before true 3D unless the story geometry requires depth that simpler methods cannot express.

