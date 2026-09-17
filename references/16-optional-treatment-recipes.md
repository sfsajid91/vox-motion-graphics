# Optional Treatment Recipes

Treatments create cohesion after the story/scene mechanism is chosen. They are **not quality requirements**.

## Editorial Paper Collage
Useful when tactile/history/editorial material fits the story.
Possible ingredients:
- warm or neutral paper field;
- cutout edges;
- hard/offset shadow;
- restrained grain/paper fiber;
- marker strokes or stamped labels;
- optional halftone derivative.

Do not automatically add all ingredients.

## Vintage Film Montage
Useful for archival/period mood.
Possible ingredients:
- restrained contrast/saturation shift;
- vignette;
- gate weave;
- dust/grain;
- stepped motion/posterization;
- scan-line/print artifacts where stylistically justified.

Do not fake archival evidence with treatment.

## Clean Data / Technical Editorial
Useful for science/tech/business systems.
Possible ingredients:
- dark/light matte base;
- thin rules/grid;
- tabular/mono labels;
- programmatic diagrams;
- restrained accent colors;
- crisp motion and evidence highlighting.

## Glass / Digital Platform
Useful for UI/platform/software transitions.
Possible ingredients:
- translucent planes;
- specular sweeps;
- soft screen bloom;
- magnetic/snapping alignment;
- frictionless easing;
- node/path systems.

## Blueprint / Engineering
Useful for manufacturing/hardware/process stories.
Possible ingredients:
- drafting grid;
- measurement lines;
- exploded views;
- callouts;
- mechanical motion personality;
- paper/technical surfaces.

## Halftone Cutout
Use when print/editorial texture is chosen.
`tools/halftone.py` creates a transparent cutout derivative from one or more approved source images:

```bash
python3 tools/halftone.py IN.png [IN2.png ...] --out OUT_DIR [--pitch 5] [--long-edge 1100]
```

It trims each input to its alpha bounds, normalizes the long edge for a consistent dot pitch, applies a high-contrast 45-degree round-dot screen, and preserves the source alpha. Output is white fill with black dots inside the silhouette, saved as `<input-stem>.png`.

Halftone is a derived treatment, not a replacement for sourcing/provenance.

## Posterized Motion
Render/project at normal FPS while snapping selected motion to a lower temporal cadence. Use to create handmade/stop-motion feel.

Do not posterize everything if the story needs polished digital movement. Mixed cadence can itself communicate contrast (e.g. physical world stepped, digital world smooth).

## Treatment Cohesion Rule
Prefer 2–4 strong continuity tokens over a “texture sandwich” with every effect enabled.
