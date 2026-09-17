#!/usr/bin/env python3
from pathlib import Path
import json

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def load(name):
    return json.loads((SCHEMAS / name).read_text())


def assert_valid(schema_name, obj):
    Draft202012Validator(load(schema_name)).validate(obj)


def assert_invalid(schema_name, obj):
    errors = list(Draft202012Validator(load(schema_name)).iter_errors(obj))
    assert errors, f"expected {schema_name} to reject object"


def storyboard():
    return {
        "projectId": "p",
        "preview": {"path": "storyboard/index.html", "mode": "playable"},
        "status": "frozen",
        "freezeEvidence": {
            "reviewer": "independent-critic",
            "reviewRef": "review-01",
            "independent": True,
        },
        "scenes": [
            {
                "id": "S1",
                "beatIds": ["B1"],
                "visualThesis": "One route becomes the bottleneck for the whole system",
                "focalPoint": "flow through the narrow gate",
                "dominantRelationship": "many inputs depend on one constrained route",
                "constructionFamily": "constraint",
                "assetIds": ["route"],
                "states": [
                    {
                        "id": "anchor",
                        "purpose": "establish flow",
                        "focalElement": "moving inputs",
                        "meaningfulChange": "inputs enter the shared route",
                        "assetIds": ["route"],
                    },
                    {
                        "id": "payoff",
                        "purpose": "show consequence",
                        "focalElement": "blocked gate",
                        "meaningfulChange": "flow queues and depletes downstream",
                        "assetIds": ["route"],
                    },
                ],
                "transitionIntent": "follow the last output into the next system",
            }
        ],
    }


def main():
    schema_files = sorted(SCHEMAS.glob("*.schema.json"))
    for path in schema_files:
        Draft202012Validator.check_schema(json.loads(path.read_text()))

    assert_valid("storyboard-plan.schema.json", storyboard())
    no_freeze = storyboard()
    no_freeze.pop("freezeEvidence")
    assert_invalid("storyboard-plan.schema.json", no_freeze)
    self_frozen = storyboard()
    self_frozen["freezeEvidence"]["independent"] = False
    assert_invalid("storyboard-plan.schema.json", self_frozen)
    no_change = storyboard()
    no_change["scenes"][0]["states"][0].pop("meaningfulChange")
    assert_invalid("storyboard-plan.schema.json", no_change)

    ready = storyboard()
    ready["status"] = "ready_for_approval"
    ready.pop("freezeEvidence")
    ready["reviewEvidence"] = {
        "reviewer": "independent-critic",
        "reviewRef": "review-ready-01",
        "independent": True,
    }
    assert_valid("storyboard-plan.schema.json", ready)
    ready.pop("reviewEvidence")
    assert_invalid("storyboard-plan.schema.json", ready)

    candidate = {
        "projectId": "p",
        "assets": [
            {
                "id": "hero",
                "sceneIds": ["S1"],
                "role": "illustrative hero",
                "origin": "generated",
                "technicalStatus": "candidate",
                "editorialStatus": "pending",
                "rightsStatus": "self_created",
                "representationType": "metaphor",
            }
        ],
    }
    assert_valid("asset-manifest.schema.json", candidate)

    accepted = json.loads(json.dumps(candidate))
    asset = accepted["assets"][0]
    asset.update(
        {
            "technicalStatus": "verified",
            "editorialStatus": "accepted",
            "file": "assets/hero.png",
            "reviewEvidence": ["storyboard-freeze-01"],
        }
    )
    assert_valid("asset-manifest.schema.json", accepted)

    not_verified = json.loads(json.dumps(accepted))
    not_verified["assets"][0]["technicalStatus"] = "available"
    assert_invalid("asset-manifest.schema.json", not_verified)

    rights = json.loads(json.dumps(accepted))
    rights["assets"][0]["rightsStatus"] = "verified"
    assert_invalid("asset-manifest.schema.json", rights)

    evidence = json.loads(json.dumps(accepted))
    evidence["assets"][0]["representationType"] = "evidence"
    assert_invalid("asset-manifest.schema.json", evidence)

    timing = {
        "fps": 30,
        "alignmentSource": "voiceover-alignment.json",
        "compositionDurationSec": 12,
        "voiceoverEndSec": 11.5,
        "captionEndSec": 11.5,
        "finalHold": {
            "startSec": 11.5,
            "endSec": 12,
            "intentional": True,
            "reviewed": True,
            "reason": "let the thesis land",
        },
        "scenes": [
            {
                "sceneId": "S1",
                "sceneStartSec": 0,
                "sceneDurationSec": 12,
                "microbeats": [
                    {
                        "offsetSec": 0,
                        "event": "establish flow",
                        "motionRole": "primary",
                        "storyboardStateId": "anchor",
                    }
                ],
            }
        ],
    }
    assert_valid("frame-scene-spec.schema.json", timing)

    editorial = {
        "critic": "critic-agent",
        "independent": True,
        "renderRefs": ["contact-sheet.png"],
        "overallStatus": "publish_candidate",
        "sceneFindings": [
            {
                "sceneId": "S1",
                "status": "approve",
                "checks": {
                    "thesisClear": True,
                    "hierarchyClear": True,
                    "stateChangeMeaningful": True,
                    "pacingResolved": True,
                    "continuityResolved": True,
                    "assetFit": True,
                },
                "findings": [],
            }
        ],
    }
    assert_valid("editorial-qa-report.schema.json", editorial)
    self_approved = json.loads(json.dumps(editorial))
    self_approved["independent"] = False
    assert_invalid("editorial-qa-report.schema.json", self_approved)
    unresolved_editorial = json.loads(json.dumps(editorial))
    unresolved_editorial["sceneFindings"][0]["checks"]["hierarchyClear"] = False
    assert_invalid("editorial-qa-report.schema.json", unresolved_editorial)

    technical = {
        "runId": "qa-01",
        "overallStatus": "pass",
        "checks": [{"id": "render", "status": "pass", "evidence": "render exited 0"}],
    }
    assert_valid("technical-qa-report.schema.json", technical)
    false_pass = json.loads(json.dumps(technical))
    false_pass["checks"][0]["status"] = "fail"
    assert_invalid("technical-qa-report.schema.json", false_pass)

    reference = {
        "referenceId": "ref1",
        "scenes": [
            {
                "id": "S1",
                "semanticJob": "reveal",
                "constructionFamily": "portal",
                "visualThesis": "frame becomes world",
                "mechanism": "weld-detach",
            }
        ],
        "findings": [
            {
                "finding": "few assets, high choreography",
                "classification": "creator_dna",
                "confidence": "high",
                "evidenceSceneIds": ["S1"],
            }
        ],
    }
    assert_valid("reference-analysis.schema.json", reference)

    tune = {
        "projectId": "p",
        "scenes": [
            {
                "sceneId": "S1",
                "parameters": [
                    {
                        "name": "heroScale",
                        "type": "number",
                        "currentValue": 1.0,
                        "min": 0.5,
                        "max": 2.0,
                        "step": 0.05,
                        "allowedValues": None,
                        "semanticRole": "focal hierarchy",
                        "repairPriority": "high",
                        "studioExposed": True,
                    }
                ],
            }
        ],
    }
    assert_valid("tunable-parameter-manifest.schema.json", tune)

    patch = {
        "critic": "vision-critic",
        "renderId": "r1",
        "changes": [
            {
                "sceneId": "S1",
                "parameter": "heroScale",
                "oldValue": 1.0,
                "newValue": 1.15,
                "reason": "hero too weak",
                "expectedEffect": "stronger focal hierarchy",
                "confidence": "high",
            }
        ],
        "requiresRedesign": False,
        "redesignReason": None,
    }
    assert_valid("parameter-patch.schema.json", patch)

    print(f"OK: {len(schema_files)} schemas + v0.8 behavioral guardrails")


if __name__ == "__main__":
    main()
