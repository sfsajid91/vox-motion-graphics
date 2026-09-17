# Editorial Motion Director v0.8

`vox-motion-graphics` directs and implements editorial motion-graphics videos without requiring the user to storyboard or speak motion-design jargon.

v0.8 makes the HTML storyboard/preview the creative source of truth, freezes accepted visual decisions before Remotion, separates editorial QA from technical QA, and replaces overlapping asset contracts with one orthogonal lifecycle. It also includes bounded autonomous orchestration so coding agents can run the pipeline without endless repair loops.

Start with `SKILL.md`. Load only the references linked for the current production stage.

## Package shape

- `SKILL.md` — workflow, routing, gates, and non-negotiables
- `references/` — focused directing, reference-analysis, orchestration, and implementation guidance
- `examples/positive/` and `examples/negative/` — corrected outcomes and instructive failures
- `schemas/` — core handoff contracts plus optional tuning/reference contracts
- `tools/validate_project.py` — deterministic timing, asset, storyboard, and implementation checks
- `tools/make_contact_sheet.py` — representative-frame contact sheets
- `tools/halftone.py` — optional image treatment, not a default style

## Validation

From this directory:

```bash
python tests/test_schemas.py
python -m unittest discover -s tests -p 'test_validate_project.py'
python tools/validate_project.py --help
```

The validator intentionally does not score “cinematic,” “Vox-like,” or other aesthetic qualities. Those remain editorial review decisions.
