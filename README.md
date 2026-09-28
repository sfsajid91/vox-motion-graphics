# Editorial Motion Director v0.9.0

`vox-motion-graphics` directs and implements editorial motion-graphics videos without requiring the user to storyboard or speak motion-design jargon.

v0.9.0 turns the storyboard-first workflow into an executable directing procedure: select a visible relationship, stage object/camera/attention/sound together, compose with captions, and conform semantic events to final speech. Intent-blind critique distinguishes concept failures from implementation defects and taste. Publication checks bind independent review to the actual frozen board and mastered output; draft previews remain available.

This release operationalizes lessons from two independent production postmortems without copying their surface style. It does not claim measured improvement in small-model video quality; the held-out evaluation procedure lives in `tests/vague-autopilot-prompts.md`. See `V0.9.0-CHANGELOG.md` for changes and limits.

Start with `SKILL.md`. Load only the references linked for the current production stage.

## Package shape

- `SKILL.md` — workflow, routing, gates, and non-negotiables
- `references/` — focused directing, reference-analysis, orchestration, and implementation guidance
- `examples/positive/` and `examples/negative/` — corrected outcomes and instructive failures
- `schemas/` — core handoff contracts plus optional tuning/reference contracts
- `tools/validate_project.py` — deterministic timing, asset, storyboard, implementation, and publication-evidence checks
- `tools/make_contact_sheet.py` — representative-frame contact sheets
- `tools/halftone.py` — optional image treatment, not a default style

## Validation

From this directory:

```bash
python tests/test_schemas.py
python -m unittest discover -s tests -p 'test_validate_project.py'
python tools/validate_project.py --help
python tools/validate_project.py path/to/project-manifest.json --stage draft
python tools/validate_project.py path/to/project-manifest.json --stage publish
```

The first two commands run the repository tests. The manifest commands operate on a production's real artifacts; use `--help` and [orchestration](references/orchestration.md) for the publication receipt contract. Draft is the default and does not confer publication approval.

The validator checks metadata, references, and artifact identity, not visual relationships, audible cues, source truth, reviewer honesty, or aesthetic quality. Independent review must inspect the actual mastered output. Behavioral prompts are development evaluations, not deterministic proof that a model follows the skill.
