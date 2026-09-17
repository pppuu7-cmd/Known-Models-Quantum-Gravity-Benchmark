#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

PRESENT_MATCH = "PRESENT_IDENTITY_MATCH"
PRESENT_MISMATCH = "PRESENT_IDENTITY_MISMATCH"
MISSING = "MISSING_OR_UNAVAILABLE"
DOWNLOAD_FAILED = "DOWNLOAD_FAILED"
NOT_EXERCISED = "NOT_EXERCISED_CONTROL"
REVIEW_PASS = "ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED"
REVIEW_FAIL = "ITER504T_REPAIR_RERUN_AUTHORITY_RESTORATION_FAILED_SCOPED"
REVIEW_BLOCKED = "ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED"
INVALID = "INVALID_IMPLEMENTATION"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_result(path: Path, result: dict[str, Any]) -> None:
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["review_decision_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def entries_by_role(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {e.get("role"): e for e in manifest.get("entries", []) if isinstance(e, dict) and e.get("role")}


def boundary_classification(authority: dict[str, Any], manifest: dict[str, Any]) -> tuple[str, list[str]]:
    reasons: list[str] = []
    if manifest.get("run_identity_ok") is not True:
        return INVALID, ["terminal_run_identity_mismatch_or_unavailable"]

    role_map = entries_by_role(manifest)
    if manifest.get("mode") == "boundary_control":
        role = manifest.get("simulate_missing_role")
        entry = role_map.get(role)
        if not isinstance(entry, dict):
            return INVALID, ["boundary_control_missing_simulated_role_entry"]
        expected_name = authority.get("boundary_control", {}).get("nonexistent_name")
        ok = (
            entry.get("lookup_name") == expected_name
            and entry.get("download_attempted") is True
            and isinstance(entry.get("download_returncode"), int)
            and entry.get("download_returncode") != 0
            and entry.get("state") == MISSING
        )
        if not ok:
            return INVALID, ["boundary_control_did_not_reach_missing_download_failure"]
        return REVIEW_BLOCKED, ["workflow_boundary_required_artifact_missing_control"]

    expected_roles = [item["role"] for item in authority.get("required_terminal_artifacts", [])]
    if sorted(role_map) != sorted(expected_roles):
        return INVALID, ["artifact_manifest_role_set_mismatch"]

    states = [role_map[role].get("state") for role in expected_roles]
    if any(state == PRESENT_MISMATCH for state in states):
        return INVALID, ["present_artifact_identity_mismatch"]
    if any(state in {MISSING, DOWNLOAD_FAILED} for state in states):
        return REVIEW_BLOCKED, ["required_terminal_artifact_missing_or_unavailable_or_download_failed"]
    if not all(state == PRESENT_MATCH for state in states):
        return INVALID, ["unexpected_artifact_boundary_state"]
    return "CONTINUE_EXACT_REVIEW", reasons


def synthetic_boundary_controls(authority: dict[str, Any], manifest: dict[str, Any]) -> dict[str, bool]:
    controls: dict[str, bool] = {}
    if manifest.get("mode") != "production":
        return controls

    production_class, _ = boundary_classification(authority, manifest)
    controls["actual_all_present_identity_match_continues"] = production_class == "CONTINUE_EXACT_REVIEW"

    missing_fixture = copy.deepcopy(manifest)
    missing_fixture["entries"][0]["state"] = MISSING
    missing_fixture["entries"][0]["download_attempted"] = True
    missing_fixture["entries"][0]["download_returncode"] = 1
    missing_class, _ = boundary_classification(authority, missing_fixture)
    controls["missing_artifact_state_maps_to_blocked"] = missing_class == REVIEW_BLOCKED

    mismatch_fixture = copy.deepcopy(manifest)
    mismatch_fixture["entries"][0]["state"] = PRESENT_MISMATCH
    mismatch_class, _ = boundary_classification(authority, mismatch_fixture)
    controls["present_identity_mismatch_maps_to_invalid"] = mismatch_class == INVALID
    return controls


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--authority", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    authority = load_json(Path(args.authority))
    manifest = load_json(Path(args.manifest))
    out_path = Path(args.out)

    boundary_class, boundary_reasons = boundary_classification(authority, manifest)

    if manifest.get("mode") == "boundary_control":
        result = {
            "gate": authority["gate"],
            "classification": boundary_class,
            "mode": "boundary_control",
            "boundary_reasons": boundary_reasons,
            "artifact_manifest": manifest,
            "workflow_boundary_control_reached_classifier": True,
            "claim_ceiling": authority["interpretation_ceiling"],
        }
        write_result(out_path, result)
        print(json.dumps({
            "classification": boundary_class,
            "boundary_reasons": boundary_reasons,
            "workflow_boundary_control_reached_classifier": True,
        }, sort_keys=True))
        return

    boundary_controls = synthetic_boundary_controls(authority, manifest)
    controls_ok = bool(boundary_controls) and all(boundary_controls.values())

    if boundary_class != "CONTINUE_EXACT_REVIEW":
        classification = boundary_class if controls_ok else INVALID
        result = {
            "gate": authority["gate"],
            "classification": classification,
            "mode": "production",
            "boundary_reasons": boundary_reasons,
            "artifact_manifest": manifest,
            "boundary_controls": boundary_controls,
            "boundary_controls_all_pass": controls_ok,
            "inherited_review": None,
            "claim_ceiling": authority["interpretation_ceiling"],
        }
        write_result(out_path, result)
        print(json.dumps({
            "classification": classification,
            "boundary_reasons": boundary_reasons,
            "boundary_controls": boundary_controls,
        }, sort_keys=True))
        return

    role_map = entries_by_role(manifest)
    inherited_out = out_path.with_name(out_path.stem + "_inherited.json")
    inherited_script = Path(__file__).with_name(
        "iter504t_repair_rerun_terminal_authority_review_semantics_repair.py"
    )
    cmd = [
        sys.executable,
        str(inherited_script),
        "--authority", args.authority,
        "--assembly-a", role_map["assembly_a"]["local_path"],
        "--assembly-b", role_map["assembly_b"]["local_path"],
        "--aggregate", role_map["aggregate"]["local_path"],
        "--critic", role_map["critic"]["local_path"],
        "--verdict", role_map["verdict"]["local_path"],
        "--out", str(inherited_out),
    ]
    proc = subprocess.run(cmd, text=True, capture_output=True, check=False)

    inherited_review: dict[str, Any] | None = None
    if proc.returncode == 0 and inherited_out.exists():
        try:
            inherited_review = load_json(inherited_out)
        except Exception:
            inherited_review = None

    if inherited_review is None:
        classification = INVALID
        inherited_error = "inherited_reviewer_failed_or_unparseable"
    else:
        classification = inherited_review.get("classification", INVALID)
        inherited_error = None

    if not controls_ok:
        classification = INVALID

    result = {
        "gate": authority["gate"],
        "classification": classification,
        "mode": "production",
        "boundary_reasons": boundary_reasons,
        "artifact_manifest": manifest,
        "boundary_controls": boundary_controls,
        "boundary_controls_all_pass": controls_ok,
        "inherited_reviewer_returncode": proc.returncode,
        "inherited_reviewer_error": inherited_error,
        "inherited_review": inherited_review,
        "claim_ceiling": authority["interpretation_ceiling"],
    }
    write_result(out_path, result)
    print(json.dumps({
        "classification": classification,
        "boundary_controls": boundary_controls,
        "inherited_reviewer_returncode": proc.returncode,
        "inherited_classification": inherited_review.get("classification") if inherited_review else None,
        "review_decision_sha256": load_json(out_path)["review_decision_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
