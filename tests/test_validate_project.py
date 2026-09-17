#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import io
import json
import struct
import sys
import tempfile
import unittest
import zlib
from contextlib import redirect_stdout
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_project", ROOT / "tools" / "validate_project.py")
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


def png(path: Path, color_type: int) -> None:
    channels = 4 if color_type == 6 else 3
    raw = b"\x00" + (b"\xff" * channels)

    def chunk(name: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + name + data + struct.pack(">I", zlib.crc32(name + data) & 0xFFFFFFFF)

    path.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, color_type, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw))
        + chunk(b"IEND", b"")
    )


def base_manifest(asset_file: str = "hero.png") -> dict:
    return {
        "composition": {"durationSec": 12.0, "toleranceSec": 0.05},
        "voiceover": {"endSec": 11.5},
        "captions": [{"id": "C1", "startSec": 0.0, "endSec": 11.5}],
        "scenes": [{"id": "S1", "startSec": 0.0, "durationSec": 12.0}],
        "finalHold": {
            "startSec": 11.5,
            "endSec": 12.0,
            "intentional": True,
            "reviewed": True,
            "reason": "Let the thesis land",
        },
        "assets": [
            {
                "id": "hero",
                "sceneIds": ["S1"],
                "role": "hero subject",
                "file": asset_file,
                "origin": "generated",
                "technicalStatus": "verified",
                "editorialStatus": "accepted",
                "rightsStatus": "self_created",
                "representationType": "metaphor",
                "requirements": {"requiresAlpha": True},
                "reviewEvidence": ["asset critic review"],
            }
        ],
        "storyboard": {
            "status": "frozen",
            "freezeEvidence": {
                "reviewer": "external-critic",
                "reviewRef": "review-1",
                "independent": True,
            },
            "scenes": [
                {
                    "id": "S1",
                    "beatIds": ["B1"],
                    "visualThesis": "The hero visibly changes state",
                    "focalPoint": "hero",
                    "dominantRelationship": "the before state transforms into the payoff",
                    "constructionFamily": "transformation",
                    "assetIds": ["hero"],
                    "states": [
                        {
                            "id": "anchor",
                            "purpose": "establish",
                            "focalElement": "hero",
                            "intentionalHoldReason": "make the starting state readable",
                        },
                        {
                            "id": "payoff",
                            "purpose": "resolve",
                            "focalElement": "hero",
                            "meaningfulChange": "the hero completes its transformation",
                        },
                    ],
                    "transitionIntent": "carry the transformed hero into the next scene",
                }
            ],
        },
        "implementation": {"scenes": [{"id": "S1", "stateIds": ["anchor", "payoff"]}]},
    }


def codes(findings) -> set[str]:
    return {finding.code for finding in findings}


class ValidateProjectTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        png(self.root / "hero.png", 6)
        self.manifest_path = self.root / "project-manifest.json"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def validate(self, manifest: dict):
        return VALIDATOR.validate_manifest(manifest, self.manifest_path)

    def test_complete_manifest_passes(self) -> None:
        self.assertEqual(self.validate(base_manifest()), [])

    def test_non_narrated_project_does_not_invent_a_dead_tail(self) -> None:
        manifest = base_manifest()
        manifest.pop("voiceover")
        manifest["captions"] = []
        manifest.pop("finalHold")
        self.assertEqual(self.validate(manifest), [])

    def test_timing_bounds_and_undeclared_tail_are_reported(self) -> None:
        manifest = base_manifest()
        manifest["composition"]["durationSec"] = 10.0
        manifest["voiceover"]["endSec"] = 10.5
        manifest["captions"][0]["endSec"] = 10.7
        manifest["scenes"][0]["durationSec"] = 11.0
        manifest.pop("finalHold")
        result = codes(self.validate(manifest))
        self.assertTrue(
            {"VOICEOVER_OUT_OF_BOUNDS", "CAPTION_OUT_OF_BOUNDS", "SCENE_OUT_OF_BOUNDS"}.issubset(result)
        )

        tail = base_manifest()
        tail["voiceover"]["endSec"] = 9.0
        tail["captions"][0]["endSec"] = 9.0
        tail.pop("finalHold")
        self.assertIn("UNDECLARED_FINAL_HOLD", codes(self.validate(tail)))

    def test_final_hold_must_be_explicit_reviewed_and_cover_the_tail(self) -> None:
        manifest = base_manifest()
        manifest["finalHold"] = {
            "startSec": 11.8,
            "endSec": 11.9,
            "intentional": False,
            "reviewed": False,
            "reason": "",
        }
        result = codes(self.validate(manifest))
        self.assertTrue(
            {
                "HOLD_GAP",
                "HOLD_END_MISMATCH",
                "HOLD_NOT_INTENTIONAL",
                "HOLD_NOT_REVIEWED",
                "MISSING_HOLD_REASON",
            }.issubset(result)
        )

    def test_asset_status_file_rights_and_alpha_checks(self) -> None:
        manifest = base_manifest("opaque.png")
        png(self.root / "opaque.png", 2)
        asset = manifest["assets"][0]
        asset["technicalStatus"] = "available"
        asset["rightsStatus"] = "verified"
        result = codes(self.validate(manifest))
        self.assertIn("ACCEPTED_ASSET_NOT_VERIFIED", result)
        self.assertIn("INCOMPLETE_RIGHTS_EVIDENCE", result)
        self.assertIn("ALPHA_REQUIRED", result)

        asset["technicalStatus"] = "verified"
        asset.pop("reviewEvidence")
        self.assertIn("ACCEPTED_ASSET_MISSING_REVIEW", codes(self.validate(manifest)))

        candidate = base_manifest()
        candidate["assets"] = [
            {
                "id": "candidate",
                "sceneIds": ["S1"],
                "role": "candidate hero",
                "origin": "generated",
                "technicalStatus": "candidate",
                "editorialStatus": "pending",
                "rightsStatus": "unresolved",
                "representationType": "metaphor",
            }
        ]
        candidate["storyboard"]["scenes"][0]["assetIds"] = ["candidate"]
        self.assertIn("FROZEN_ASSET_NOT_READY", codes(self.validate(candidate)))

        candidate["storyboard"]["status"] = "in_review"
        candidate["storyboard"].pop("freezeEvidence")
        self.assertEqual(self.validate(candidate), [])

    def test_verified_asset_requires_existing_file(self) -> None:
        manifest = base_manifest("missing.png")
        self.assertIn("ASSET_FILE_MISSING", codes(self.validate(manifest)))

    def test_frozen_storyboard_requires_complete_reviewed_scenes(self) -> None:
        manifest = base_manifest()
        manifest["storyboard"].pop("freezeEvidence")
        scene = manifest["storyboard"]["scenes"][0]
        scene["focalPoint"] = ""
        scene["states"] = [
            {"id": "hold", "purpose": "hold", "focalElement": "hero"},
            {"id": "hold", "purpose": "hold", "focalElement": "hero", "meaningfulChange": "moves"},
        ]
        result = codes(self.validate(manifest))
        self.assertIn("INCOMPLETE_FREEZE_EVIDENCE", result)
        self.assertIn("INCOMPLETE_FROZEN_SCENE", result)
        self.assertIn("DUPLICATE_ID", result)
        self.assertIn("INVALID_STATE_SEMANTICS", result)

        manifest = base_manifest()
        manifest["storyboard"]["freezeEvidence"]["independent"] = False
        self.assertIn("FREEZE_REVIEW_NOT_INDEPENDENT", codes(self.validate(manifest)))

    def test_storyboard_status_uses_canonical_review_values(self) -> None:
        manifest = base_manifest()
        manifest["storyboard"]["status"] = "in_review"
        manifest["storyboard"].pop("freezeEvidence")
        self.assertEqual(self.validate(manifest), [])

        ready = base_manifest()
        ready["storyboard"]["status"] = "ready_for_approval"
        ready["storyboard"].pop("freezeEvidence")
        ready["storyboard"]["reviewEvidence"] = {
            "reviewer": "external-critic",
            "reviewRef": "review-ready-1",
            "independent": True,
        }
        self.assertEqual(self.validate(ready), [])

        ready["storyboard"]["reviewEvidence"]["independent"] = False
        self.assertIn("REVIEW_NOT_INDEPENDENT", codes(self.validate(ready)))

        manifest["storyboard"]["status"] = "review"
        self.assertIn("INVALID_STORYBOARD_STATUS", codes(self.validate(manifest)))

    def test_frozen_storyboard_requires_every_planned_scene(self) -> None:
        manifest = base_manifest()
        manifest["scenes"].append({"id": "S2", "startSec": 11.5, "durationSec": 0.5})
        self.assertIn("STORYBOARD_SCENE_MISSING", codes(self.validate(manifest)))

    def test_storyboard_implementation_scene_and_state_mismatches(self) -> None:
        manifest = base_manifest()
        manifest["implementation"]["scenes"] = [
            {"id": "S1", "stateIds": ["payoff", "anchor", "extra"]},
            {"id": "S2", "stateIds": ["entry"]},
        ]
        result = codes(self.validate(manifest))
        self.assertIn("IMPLEMENTATION_SCENE_EXTRA", result)
        self.assertIn("IMPLEMENTATION_STATE_EXTRA", result)

        manifest["implementation"]["scenes"] = [{"id": "S1", "stateIds": ["payoff", "anchor"]}]
        self.assertIn("IMPLEMENTATION_STATE_ORDER_MISMATCH", codes(self.validate(manifest)))

        manifest["implementation"]["scenes"] = []
        self.assertIn("IMPLEMENTATION_SCENE_MISSING", codes(self.validate(manifest)))

    def test_cli_returns_nonzero_for_invalid_manifest_and_json_output(self) -> None:
        manifest = base_manifest()
        manifest.pop("finalHold")
        self.manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        with redirect_stdout(io.StringIO()):
            self.assertEqual(VALIDATOR.main([str(self.manifest_path), "--json"]), 1)


if __name__ == "__main__":
    unittest.main()
