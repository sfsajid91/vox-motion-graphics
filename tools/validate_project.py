#!/usr/bin/env python3
"""Validate deterministic v0.8 motion-project contracts.

The validator deliberately does not score aesthetics. It checks one compact JSON
manifest that joins timing, asset, storyboard, and implementation metadata so
cross-artifact mistakes can be found before an expensive render.

Manifest shape (all times are seconds):

{
  "composition": {"durationSec": 12.0, "toleranceSec": 0.05},
  "voiceover": {"endSec": 11.5},
  "captions": [{"id": "C1", "startSec": 0.0, "endSec": 2.2}],
  "scenes": [{"id": "S1", "startSec": 0.0, "durationSec": 12.0}],
  "finalHold": {
    "startSec": 11.5,
    "endSec": 12.0,
    "intentional": true,
    "reviewed": true,
    "reason": "Let the thesis land"
  },
  "assets": [{
    "id": "hero",
    "sceneIds": ["S1"],
    "role": "hero subject",
    "file": "assets/hero.png",
    "origin": "generated",
    "technicalStatus": "verified",
    "editorialStatus": "accepted",
    "rightsStatus": "self_created",
    "representationType": "metaphor",
    "requirements": {"requiresAlpha": true},
    "reviewEvidence": ["asset critic review"]
  }],
  "storyboard": {
    "status": "frozen",
    "freezeEvidence": {
      "reviewer": "external-critic",
      "reviewRef": "review-2026-09-17",
      "independent": true
    },
    "scenes": [{
      "id": "S1",
      "beatIds": ["B1"],
      "visualThesis": "The hero visibly changes state",
      "focalPoint": "hero",
      "dominantRelationship": "the before state transforms into the payoff",
      "constructionFamily": "transformation",
      "assetIds": ["hero"],
      "states": [
        {"id": "anchor", "purpose": "establish", "focalElement": "hero",
         "intentionalHoldReason": "make the starting state readable"},
        {"id": "payoff", "purpose": "resolve", "focalElement": "hero",
         "meaningfulChange": "the hero completes its transformation"}
      ],
      "transitionIntent": "carry the transformed hero into the next scene"
    }]
  },
  "implementation": {
    "scenes": [{"id": "S1", "stateIds": ["anchor", "payoff"]}]
  }
}

Paths are resolved relative to the manifest. Alpha inspection is dependency-free
and currently supports PNG. A positive tail after narration/captions is accepted
only when an explicit reviewed finalHold covers it. There are no built-in
aesthetic, stillness, safe-zone, or duration-preference thresholds.
"""

from __future__ import annotations

import argparse
import json
import struct
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


ORIGINS = {"generated", "sourced", "programmatic", "reused", "reconstructed"}
TECHNICAL_STATUSES = {"candidate", "available", "verified"}
EDITORIAL_STATUSES = {"pending", "accepted", "rejected"}
RIGHTS_STATUSES = {"unresolved", "needs_review", "verified", "self_created"}
STORYBOARD_STATUSES = {"draft", "in_review", "ready_for_approval", "frozen"}


@dataclass(frozen=True)
class Finding:
    code: str
    path: str
    message: str
    severity: str = "error"


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _object(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _add(findings: list[Finding], code: str, path: str, message: str) -> None:
    findings.append(Finding(code=code, path=path, message=message))


def _unique_ids(
    items: list[Any], collection_path: str, findings: list[Finding]
) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(items):
        item_path = f"{collection_path}[{index}]"
        if not isinstance(raw, dict):
            _add(findings, "INVALID_ITEM", item_path, "must be an object")
            continue
        item_id = raw.get("id")
        if not _nonempty_string(item_id):
            _add(findings, "MISSING_ID", f"{item_path}.id", "must be a non-empty string")
            continue
        if item_id in indexed:
            _add(findings, "DUPLICATE_ID", f"{item_path}.id", f"duplicate id {item_id!r}")
            continue
        indexed[item_id] = raw
    return indexed


def _png_has_alpha(path: Path) -> bool | None:
    """Return PNG alpha capability, or None when the file is not a valid PNG."""
    try:
        with path.open("rb") as handle:
            if handle.read(8) != b"\x89PNG\r\n\x1a\n":
                return None
            saw_ihdr = False
            color_type: int | None = None
            while True:
                raw_length = handle.read(4)
                if len(raw_length) != 4:
                    return None
                length = struct.unpack(">I", raw_length)[0]
                chunk_type = handle.read(4)
                data = handle.read(length)
                crc = handle.read(4)
                if len(chunk_type) != 4 or len(data) != length or len(crc) != 4:
                    return None
                if chunk_type == b"IHDR":
                    if length != 13:
                        return None
                    color_type = data[9]
                    saw_ihdr = True
                elif chunk_type == b"tRNS":
                    return True
                elif chunk_type == b"IEND":
                    break
            if not saw_ihdr or color_type is None:
                return None
            return color_type in {4, 6}
    except OSError:
        return None


def _validate_timing(manifest: dict[str, Any], findings: list[Finding]) -> None:
    composition = _object(manifest.get("composition"))
    duration = composition.get("durationSec")
    tolerance = composition.get("toleranceSec", 0.0)
    if not _is_number(duration) or duration <= 0:
        _add(findings, "INVALID_DURATION", "composition.durationSec", "must be greater than zero")
        return
    if not _is_number(tolerance) or tolerance < 0:
        _add(findings, "INVALID_TOLERANCE", "composition.toleranceSec", "must be zero or greater")
        tolerance = 0.0

    scenes = _list(manifest.get("scenes"))
    scene_index = _unique_ids(scenes, "scenes", findings)
    latest_scene_end = 0.0
    for scene_id, scene in scene_index.items():
        index = scenes.index(scene)
        path = f"scenes[{index}]"
        start = scene.get("startSec")
        scene_duration = scene.get("durationSec")
        if not _is_number(start) or start < 0:
            _add(findings, "INVALID_SCENE_START", f"{path}.startSec", "must be zero or greater")
            continue
        if not _is_number(scene_duration) or scene_duration <= 0:
            _add(findings, "INVALID_SCENE_DURATION", f"{path}.durationSec", "must be greater than zero")
            continue
        end = start + scene_duration
        latest_scene_end = max(latest_scene_end, end)
        if end > duration + tolerance:
            _add(
                findings,
                "SCENE_OUT_OF_BOUNDS",
                path,
                f"scene {scene_id!r} ends at {end:.3f}s after composition end {duration:.3f}s",
            )
    if scenes and latest_scene_end < duration - tolerance:
        _add(
            findings,
            "SCENES_END_EARLY",
            "scenes",
            f"latest scene ends at {latest_scene_end:.3f}s before composition end {duration:.3f}s",
        )

    voiceover = _object(manifest.get("voiceover"))
    voiceover_end = voiceover.get("endSec")
    if voiceover and (not _is_number(voiceover_end) or voiceover_end < 0):
        _add(findings, "INVALID_VOICEOVER_END", "voiceover.endSec", "must be zero or greater")
        voiceover_end = None
    if _is_number(voiceover_end) and voiceover_end > duration + tolerance:
        _add(
            findings,
            "VOICEOVER_OUT_OF_BOUNDS",
            "voiceover.endSec",
            f"voiceover ends at {voiceover_end:.3f}s after composition end {duration:.3f}s",
        )

    captions = _list(manifest.get("captions"))
    _unique_ids(captions, "captions", findings)
    latest_caption_end: float | None = None
    for index, caption in enumerate(captions):
        if not isinstance(caption, dict):
            continue
        path = f"captions[{index}]"
        start = caption.get("startSec")
        end = caption.get("endSec")
        if not _is_number(start) or start < 0:
            _add(findings, "INVALID_CAPTION_START", f"{path}.startSec", "must be zero or greater")
            continue
        if not _is_number(end) or end < start:
            _add(findings, "INVALID_CAPTION_END", f"{path}.endSec", "must be at or after startSec")
            continue
        latest_caption_end = end if latest_caption_end is None else max(latest_caption_end, end)
        if end > duration + tolerance:
            _add(
                findings,
                "CAPTION_OUT_OF_BOUNDS",
                path,
                f"caption ends at {end:.3f}s after composition end {duration:.3f}s",
            )
        if _is_number(voiceover_end) and end > voiceover_end + tolerance:
            _add(
                findings,
                "CAPTION_AFTER_VOICEOVER",
                path,
                f"caption ends at {end:.3f}s after voiceover end {voiceover_end:.3f}s",
            )

    active_end_candidates = [value for value in (voiceover_end, latest_caption_end) if _is_number(value)]
    active_end = max(active_end_candidates) if active_end_candidates else duration
    tail = duration - active_end
    hold = _object(manifest.get("finalHold"))
    if tail > tolerance and not hold:
        _add(
            findings,
            "UNDECLARED_FINAL_HOLD",
            "finalHold",
            f"composition has a {tail:.3f}s tail after narration/captions; declare and review it",
        )
    if hold:
        start = hold.get("startSec")
        end = hold.get("endSec")
        if not _is_number(start) or start < 0:
            _add(findings, "INVALID_HOLD_START", "finalHold.startSec", "must be zero or greater")
        if not _is_number(end) or (_is_number(start) and end <= start):
            _add(findings, "INVALID_HOLD_END", "finalHold.endSec", "must be after startSec")
        elif abs(end - duration) > tolerance:
            _add(
                findings,
                "HOLD_END_MISMATCH",
                "finalHold.endSec",
                "must match composition.durationSec within toleranceSec",
            )
        if _is_number(start) and start > active_end + tolerance:
            _add(
                findings,
                "HOLD_GAP",
                "finalHold.startSec",
                f"hold starts at {start:.3f}s after active content ends at {active_end:.3f}s",
            )
        if hold.get("intentional") is not True:
            _add(findings, "HOLD_NOT_INTENTIONAL", "finalHold.intentional", "must be true")
        if hold.get("reviewed") is not True:
            _add(findings, "HOLD_NOT_REVIEWED", "finalHold.reviewed", "must be true")
        if not _nonempty_string(hold.get("reason")):
            _add(findings, "MISSING_HOLD_REASON", "finalHold.reason", "must explain the editorial purpose")


def _validate_assets(
    manifest: dict[str, Any], manifest_dir: Path, findings: list[Finding]
) -> dict[str, dict[str, Any]]:
    assets = _list(manifest.get("assets"))
    asset_index = _unique_ids(assets, "assets", findings)
    for asset_id, asset in asset_index.items():
        index = assets.index(asset)
        path = f"assets[{index}]"
        origin = asset.get("origin")
        technical = asset.get("technicalStatus")
        editorial = asset.get("editorialStatus")
        rights = asset.get("rightsStatus")
        if origin not in ORIGINS:
            _add(findings, "INVALID_ASSET_ORIGIN", f"{path}.origin", f"must be one of {sorted(ORIGINS)}")
        if technical not in TECHNICAL_STATUSES:
            _add(
                findings,
                "INVALID_TECHNICAL_STATUS",
                f"{path}.technicalStatus",
                f"must be one of {sorted(TECHNICAL_STATUSES)}",
            )
        if editorial not in EDITORIAL_STATUSES:
            _add(
                findings,
                "INVALID_EDITORIAL_STATUS",
                f"{path}.editorialStatus",
                f"must be one of {sorted(EDITORIAL_STATUSES)}",
            )
        if rights not in RIGHTS_STATUSES:
            _add(
                findings,
                "INVALID_RIGHTS_STATUS",
                f"{path}.rightsStatus",
                f"must be one of {sorted(RIGHTS_STATUSES)}",
            )
        if editorial == "accepted":
            if technical != "verified":
                _add(
                    findings,
                    "ACCEPTED_ASSET_NOT_VERIFIED",
                    path,
                    "editorial acceptance requires technicalStatus=verified",
                )
            review_evidence = asset.get("reviewEvidence")
            if not isinstance(review_evidence, list) or not review_evidence or any(
                not _nonempty_string(item) for item in review_evidence
            ):
                _add(
                    findings,
                    "ACCEPTED_ASSET_MISSING_REVIEW",
                    f"{path}.reviewEvidence",
                    "editorial acceptance requires at least one review reference",
                )

        asset_path_value = asset.get("file")
        asset_path_field = "file"
        if not _nonempty_string(asset_path_value) and _nonempty_string(asset.get("path")):
            asset_path_value = asset.get("path")
            asset_path_field = "path"
        needs_file = technical in {"available", "verified"} or editorial == "accepted"
        resolved_path: Path | None = None
        if _nonempty_string(asset_path_value):
            resolved_path = (manifest_dir / asset_path_value).resolve()
            if not resolved_path.is_file():
                _add(
                    findings,
                    "ASSET_FILE_MISSING",
                    f"{path}.{asset_path_field}",
                    f"asset {asset_id!r} does not exist at {resolved_path}",
                )
        elif needs_file:
            _add(findings, "ASSET_FILE_REQUIRED", f"{path}.file", "available, verified, or accepted assets need a file")

        if rights == "verified":
            for field in ("sourceUri", "license", "rightsEvidence"):
                if not _nonempty_string(asset.get(field)):
                    _add(
                        findings,
                        "INCOMPLETE_RIGHTS_EVIDENCE",
                        f"{path}.{field}",
                        "rightsStatus=verified requires sourceUri, license, and rightsEvidence",
                    )

        requirements = _object(asset.get("requirements"))
        requires_alpha = requirements.get("requiresAlpha")
        if requires_alpha is None:
            requires_alpha = asset.get("requiredAlpha")
        if requires_alpha is True and resolved_path and resolved_path.is_file():
            alpha = _png_has_alpha(resolved_path)
            if alpha is None:
                _add(
                    findings,
                    "ALPHA_FORMAT_UNSUPPORTED",
                    f"{path}.{asset_path_field}",
                    "dependency-free alpha inspection currently supports valid PNG files only",
                )
            elif not alpha:
                _add(findings, "ALPHA_REQUIRED", f"{path}.{asset_path_field}", "asset does not contain an alpha channel")
    return asset_index


def _validate_storyboard(
    manifest: dict[str, Any],
    asset_index: dict[str, dict[str, Any]],
    findings: list[Finding],
) -> None:
    storyboard = _object(manifest.get("storyboard"))
    if not storyboard:
        return
    status = storyboard.get("status")
    if status not in STORYBOARD_STATUSES:
        _add(
            findings,
            "INVALID_STORYBOARD_STATUS",
            "storyboard.status",
            f"must be one of {sorted(STORYBOARD_STATUSES)}",
        )
    storyboard_scenes = _list(storyboard.get("scenes"))
    storyboard_index = _unique_ids(storyboard_scenes, "storyboard.scenes", findings)
    planned_index = {
        item.get("id"): item
        for item in _list(manifest.get("scenes"))
        if isinstance(item, dict) and _nonempty_string(item.get("id"))
    }
    storyboard_state_ids: dict[str, list[str]] = {}

    if status in {"ready_for_approval", "frozen"}:
        evidence_field = "freezeEvidence" if status == "frozen" else "reviewEvidence"
        review_evidence = _object(storyboard.get(evidence_field))
        for field in ("reviewer", "reviewRef"):
            if not _nonempty_string(review_evidence.get(field)):
                _add(
                    findings,
                    "INCOMPLETE_FREEZE_EVIDENCE" if status == "frozen" else "INCOMPLETE_REVIEW_EVIDENCE",
                    f"storyboard.{evidence_field}.{field}",
                    f"a {status} storyboard requires non-empty reviewer and reviewRef fields",
                )
        if review_evidence.get("independent") is not True:
            _add(
                findings,
                "FREEZE_REVIEW_NOT_INDEPENDENT" if status == "frozen" else "REVIEW_NOT_INDEPENDENT",
                f"storyboard.{evidence_field}.independent",
                f"a {status} storyboard requires independent editorial review",
            )
        for scene_id in sorted(set(planned_index) - set(storyboard_index)):
            _add(
                findings,
                "STORYBOARD_SCENE_MISSING",
                "storyboard.scenes",
                f"planned scene {scene_id!r} is missing from the review-ready storyboard",
            )
        for scene_id, scene in storyboard_index.items():
            index = storyboard_scenes.index(scene)
            path = f"storyboard.scenes[{index}]"
            for field in (
                "visualThesis",
                "focalPoint",
                "dominantRelationship",
                "constructionFamily",
                "transitionIntent",
            ):
                if not _nonempty_string(scene.get(field)):
                    _add(
                        findings,
                        "INCOMPLETE_FROZEN_SCENE",
                        f"{path}.{field}",
                        "must be a non-empty string before approval/freeze",
                    )
            beat_ids = scene.get("beatIds")
            if not isinstance(beat_ids, list) or not beat_ids or any(not _nonempty_string(value) for value in beat_ids):
                _add(
                    findings,
                    "INCOMPLETE_FROZEN_SCENE",
                    f"{path}.beatIds",
                    "must contain at least one non-empty beat id",
                )
            elif len(set(beat_ids)) != len(beat_ids):
                _add(
                    findings,
                    "DUPLICATE_BEAT_ID",
                    f"{path}.beatIds",
                    "beat ids must be unique within a scene",
                )

            scene_asset_ids = scene.get("assetIds")
            if not isinstance(scene_asset_ids, list):
                _add(findings, "INCOMPLETE_FROZEN_SCENE", f"{path}.assetIds", "must be an array")
                scene_asset_ids = []
            elif any(not _nonempty_string(asset_id) for asset_id in scene_asset_ids):
                _add(
                    findings,
                    "INVALID_ASSET_REFERENCE",
                    f"{path}.assetIds",
                    "asset ids must be non-empty strings",
                )
                scene_asset_ids = []
            elif len(set(scene_asset_ids)) != len(scene_asset_ids):
                _add(findings, "DUPLICATE_ASSET_REFERENCE", f"{path}.assetIds", "asset ids must be unique")
            for asset_id in scene_asset_ids:
                if asset_id not in asset_index:
                    _add(
                        findings,
                        "UNKNOWN_ASSET_REFERENCE",
                        f"{path}.assetIds",
                        f"unknown asset id {asset_id!r}",
                    )
                    continue
                asset = asset_index[asset_id]
                if asset.get("technicalStatus") != "verified" or asset.get("editorialStatus") != "accepted":
                    _add(
                        findings,
                        "FROZEN_ASSET_NOT_READY",
                        f"{path}.assetIds",
                        f"asset {asset_id!r} must be technically verified and editorially accepted before approval/freeze",
                    )

            states = scene.get("states")
            if not isinstance(states, list) or not states:
                _add(
                    findings,
                    "INCOMPLETE_FROZEN_SCENE",
                    f"{path}.states",
                    "must contain at least one state object",
                )
                states = []
            state_index = _unique_ids(states, f"{path}.states", findings)
            storyboard_state_ids[scene_id] = list(state_index)
            for state_id, state in state_index.items():
                state_position = states.index(state)
                state_path = f"{path}.states[{state_position}]"
                for field in ("purpose", "focalElement"):
                    if not _nonempty_string(state.get(field)):
                        _add(
                            findings,
                            "INCOMPLETE_STORYBOARD_STATE",
                            f"{state_path}.{field}",
                            "must be a non-empty string before approval/freeze",
                        )
                has_change = _nonempty_string(state.get("meaningfulChange"))
                has_hold = _nonempty_string(state.get("intentionalHoldReason"))
                if has_change == has_hold:
                    _add(
                        findings,
                        "INVALID_STATE_SEMANTICS",
                        state_path,
                        "state must declare exactly one of meaningfulChange or intentionalHoldReason",
                    )
                state_asset_ids = state.get("assetIds", [])
                if not isinstance(state_asset_ids, list):
                    _add(findings, "INVALID_STATE_ASSETS", f"{state_path}.assetIds", "must be an array")
                    continue
                if any(not _nonempty_string(asset_id) for asset_id in state_asset_ids):
                    _add(
                        findings,
                        "INVALID_STATE_ASSETS",
                        f"{state_path}.assetIds",
                        "asset ids must be non-empty strings",
                    )
                    continue
                for asset_id in state_asset_ids:
                    if asset_id not in asset_index:
                        _add(
                            findings,
                            "UNKNOWN_ASSET_REFERENCE",
                            f"{state_path}.assetIds",
                            f"unknown asset id {asset_id!r}",
                        )

    if status not in {"ready_for_approval", "frozen"}:
        for scene_id, scene in storyboard_index.items():
            states = _list(scene.get("states"))
            storyboard_state_ids[scene_id] = [
                state["id"]
                for state in states
                if isinstance(state, dict) and _nonempty_string(state.get("id"))
            ]

    implementation = _object(manifest.get("implementation"))
    if not implementation:
        return
    implementation_scenes = _list(implementation.get("scenes"))
    implementation_index = _unique_ids(implementation_scenes, "implementation.scenes", findings)
    for scene_id in sorted(set(storyboard_index) - set(implementation_index)):
        _add(
            findings,
            "IMPLEMENTATION_SCENE_MISSING",
            "implementation.scenes",
            f"storyboard scene {scene_id!r} is missing from implementation metadata",
        )
    for scene_id in sorted(set(implementation_index) - set(storyboard_index)):
        _add(
            findings,
            "IMPLEMENTATION_SCENE_EXTRA",
            "implementation.scenes",
            f"implementation scene {scene_id!r} is not present in the storyboard",
        )
    for scene_id in sorted(set(storyboard_index) & set(implementation_index)):
        storyboard_states = storyboard_state_ids.get(scene_id, [])
        implementation_states = _list(implementation_index[scene_id].get("stateIds"))
        missing = [state for state in storyboard_states if state not in implementation_states]
        extra = [state for state in implementation_states if state not in storyboard_states]
        if missing:
            _add(
                findings,
                "IMPLEMENTATION_STATE_MISSING",
                f"implementation.scenes[{scene_id}].stateIds",
                f"missing storyboard states: {missing}",
            )
        if extra:
            _add(
                findings,
                "IMPLEMENTATION_STATE_EXTRA",
                f"implementation.scenes[{scene_id}].stateIds",
                f"states not present in storyboard: {extra}",
            )
        if not missing and not extra and storyboard_states != implementation_states:
            _add(
                findings,
                "IMPLEMENTATION_STATE_ORDER_MISMATCH",
                f"implementation.scenes[{scene_id}].stateIds",
                "state order differs from the frozen storyboard",
            )


def validate_manifest(manifest: Any, manifest_path: Path) -> list[Finding]:
    findings: list[Finding] = []
    if not isinstance(manifest, dict):
        return [Finding("INVALID_MANIFEST", "$", "top-level JSON value must be an object")]
    _validate_timing(manifest, findings)
    asset_index = _validate_assets(manifest, manifest_path.parent, findings)
    _validate_storyboard(manifest, asset_index, findings)
    return findings


def _render_text(findings: Iterable[Finding], manifest_path: Path) -> str:
    rows = list(findings)
    if not rows:
        return f"OK: {manifest_path} passed deterministic project validation"
    lines = [f"FAIL: {manifest_path} has {len(rows)} validation issue(s)"]
    lines.extend(f"- {item.severity.upper()} {item.code} at {item.path}: {item.message}" for item in rows)
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate deterministic timing, asset, storyboard, and implementation contracts.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("manifest", type=Path, help="project-manifest JSON path")
    parser.add_argument("--json", action="store_true", help="emit machine-readable findings")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        finding = Finding("MANIFEST_READ_ERROR", "$", str(error))
        if args.json:
            print(json.dumps({"ok": False, "findings": [asdict(finding)]}, indent=2))
        else:
            print(f"FAIL: {finding.code}: {finding.message}", file=sys.stderr)
        return 1

    findings = validate_manifest(manifest, args.manifest.resolve())
    if args.json:
        print(json.dumps({"ok": not findings, "findings": [asdict(item) for item in findings]}, indent=2))
    else:
        print(_render_text(findings, args.manifest))
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
