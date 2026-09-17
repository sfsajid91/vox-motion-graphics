# Asset Direction & Resolution v0.6

## Core Principle
**Produce reusable motion-ready assets, not flattened generated scenes.**

A beautiful poster is often a bad motion-graphics asset because its subject, background, shadows, text and lighting cannot be independently choreographed.

## Asset Graph First
Before creating files, deduplicate recurring visual objects across the whole film.

Track:
- master asset id;
- scene usages;
- semantic roles per scene;
- derivative treatments/crops;
- representation type;
- motion needs;
- source/generation strategy.

Reuse recurring master objects when continuity benefits from visual identity.

## Routing Ladder
Prefer:
`reuse -> programmatic -> source real/licensed -> reconstruction -> generate`

### Reuse
Use an approved master asset or rig if the same real/semantic object recurs.

### Programmatic
Use SVG/HTML/CSS/Remotion for:
- charts/data;
- maps/routes;
- abstract UI;
- timelines;
- labels/frames;
- networks;
- arrows/paths;
- simple phones/devices when exact identity is unnecessary;
- shadows/light cones/treatments.

### Source Real / Licensed
Prefer sourced real media for historically identifiable:
- people;
- products;
- buildings;
- documents/screenshots;
- events;
- logos where necessary.

Record source URI/provider/license/evidence. Unknown rights are not “verified”.

### Reconstruction
Use a visibly reconstructed/simplified version when exact source media is unavailable/unnecessary. Generated historically identifiable imagery is a reconstruction unless it is not claiming to reproduce a real source artifact.

### Generate
Use image generation for:
- original editorial characters/cutouts;
- impossible illustrative scenes;
- stylized non-evidence props;
- non-literal backgrounds/plates;
- reconstructions where clearly labeled internally.

## Semantic Disambiguation for Asset Prompts
Generative models often literalize ambiguous nouns incorrectly. Before writing a prompt:
1. identify the concrete physical subject;
2. remove domain jargon that causes semantic confusion;
3. state visible geometry/material/context;
4. state camera/viewpoint/crop;
5. state isolation/alpha needs;
6. state forbidden elements.

Example pattern:
`[concrete visible subject], [material/geometry], [viewpoint], [lighting if needed], isolated clean background or transparent-ready silhouette, full object visible, no text, no watermark, no baked frame, no decorative UI.`

Do not prompt “bankruptcy”, “platform”, “packaging”, “chokepoint”, etc. when a more concrete physical subject is available.

## Motion-Aware Asset Spec
Before source/generation record:
- full-body/full-object requirement;
- minimum resolution / expected zoom;
- alpha/transparency;
- viewpoint;
- independent parts required;
- crop tolerance;
- parallax/depth requirement;
- expected rotation;
- whether shadows/light should remain external.

## Visible-Bounds Composition
The file rectangle is not necessarily the visual rectangle. Transparent cutouts and sourced plates may contain asymmetric alpha padding, off-center architecture, or a focal feature far from the canvas center.

Before locking placement:
- inspect visible/alpha bounds rather than relying on nominal width and height;
- identify the feature that must anchor attention (face, lens, tower, logo, label, etc.);
- tune x/y/scale against that feature at the intended crop;
- verify the asset again after camera push/overscan, since effective scale can change the composition materially.

Do not “correct” a visually centered subject back to mathematically centered file coordinates.

## Keep Raw Assets Clean
Default generated/source normalization:
- no baked subtitles;
- no baked drop shadow unless the shadow is inseparable from the literal source;
- no baked film grain/halftone unless the asset itself is intentionally a treated derivative;
- no baked color grade that prevents global cohesion;
- no unexplained lens flare or decorative HUD.

Treatments should usually be applied in Remotion or as explicitly derived asset variants.

## One Treatment Beats Five Matched Sources
Heterogeneous source imagery can be unified through a shared treatment: grayscale/contrast, print treatment, edge mask, shadow, palette, frame, crop language, etc. Do not regenerate real evidence merely to make it match aesthetically.

## Candidate Policy
- deterministic/programmatic asset: one candidate;
- normal generated support asset: one candidate, regenerate only on failure;
- important hero/face/ambiguous generated asset: 2–3 candidates;
- difficult composition: prototype scene concepts before generating expensive assets.

## Representation Safety
`literal`, `evidence`, `reconstruction`, `metaphor`, `abstract` are separate.

- evidence must map to claims/source;
- metaphor must not masquerade as evidence;
- fake historical memos/screenshots/newspapers are prohibited;
- literal asset identity and rights must be reviewable.

## Asset Failure Rule
A fallback must preserve semantic capability.

Do **not** replace a failed generated portrait with a generic SVG merely because the output extension matches. Valid fallback examples:
- diagram generation fails -> deterministic SVG fallback;
- literal source unavailable -> reconstruction if editorially acceptable;
- hero historical portrait source unavailable -> blocker/replan rather than meaningless placeholder.
