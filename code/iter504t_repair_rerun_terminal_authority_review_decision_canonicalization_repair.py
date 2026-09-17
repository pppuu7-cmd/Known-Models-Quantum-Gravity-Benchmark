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
REVIEW_PASS = "ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED"
REVIEW_BLOCKED = "ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED"
INVALID = "INVALID_IMPLEMENTATION"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha_json(obj: Any) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def entries_by_role(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {e.get("role"): e for e in manifest.get("entries", []) if isinstance(e, dict) and e.get("role")}


def boundary_classification(authority: dict[str, Any], manifest: dict[str, Any]) -> tuple[str, list[str]]:
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
    return "CONTINUE_EXACT_REVIEW", []


def synthetic_boundary_controls(authority: dict[str, Any], manifest: dict[str, Any]) -> dict[str, bool]:
    if manifest.get("mode") != "production":
        return {}
    controls: dict[str, bool] = {}
    production_class, _ = boundary_classification(authority, manifest)
    controls["actual_all_present_identity_match_continues"] = production_class == "CONTINUE_EXACT_REVIEW"

    missing_fixture = copy.deepcopy(manifest)
    missing_fixture["entries"][0]["state"] = MISSING
    missing_fixture["entries"][0]["download_attempted"] = True
    missing_fixture["entries"][0]["download_returncode"] = 1
    controls["missing_artifact_state_maps_to_blocked"] = (
        boundary_classification(authority, missing_fixture)[0] == REVIEW_BLOCKED
    )

    mismatch_fixture = copy.deepcopy(manifest)
    mismatch_fixture["entries"][0]["state"] = PRESENT_MISMATCH
    controls["present_identity_mismatch_maps_to_invalid"] = (
        boundary_classification(authority, mismatch_fixture)[0] == INVALID
    )
    return controls


def canonical_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key in (
        "gate", "mode", "terminal_run_expected", "run_query_returncode", "run_observed",
        "run_identity_ok", "artifact_query_returncode", "simulate_missing_role",
    ):
        if key in manifest:
            out[key] = copy.deepcopy(manifest[key])
    entries: list[dict[str, Any]] = []
    for entry in manifest.get("entries", []):
        if not isinstance(entry, dict):
            entries.append({"malformed_entry": True})
            continue
        entries.append({k: copy.deepcopy(v) for k, v in entry.items() if k != "local_path"})
    out["entries"] = entries
    return out


def canonical_projection(result: dict[str, Any]) -> dict[str, Any]:
    manifest = result.get("artifact_manifest") if isinstance(result.get("artifact_manifest"), dict) else {}
    cm = canonical_manifest(manifest)
    projection: dict[str, Any] = {
        "canonicalization_version": "iter504t-decision-v1-path-free",
        "gate": result.get("gate"),
        "classification": result.get("classification"),
        "mode": result.get("mode"),
        "boundary_reasons": copy.deepcopy(result.get("boundary_reasons")),
        "canonical_manifest": cm,
        "canonical_manifest_sha256": sha_json(cm),
        "boundary_controls": copy.deepcopy(result.get("boundary_controls")),
        "boundary_controls_all_pass": result.get("boundary_controls_all_pass"),
        "inherited_reviewer_returncode": result.get("inherited_reviewer_returncode"),
        "inherited_reviewer_error": result.get("inherited_reviewer_error"),
        "inherited_review": copy.deepcopy(result.get("inherited_review")),
        "canonicalization_controls": copy.deepcopy(result.get("canonicalization_controls")),
        "canonicalization_controls_all_pass": result.get("canonicalization_controls_all_pass"),
        "workflow_boundary_control_reached_classifier": result.get("workflow_boundary_control_reached_classifier"),
        "claim_ceiling": result.get("claim_ceiling"),
    }
    return projection


def projection_sha(result: dict[str, Any]) -> str:
    return sha_json(canonical_projection(result))


def mutate_paths(result: dict[str, Any], prefix: str, raw_manifest_tag: str) -> dict[str, Any]:
    fixture = copy.deepcopy(result)
    manifest = fixture.get("artifact_manifest", {})
    for entry in manifest.get("entries", []):
        if isinstance(entry, dict) and entry.get("local_path"):
            entry["local_path"] = f"{prefix}/{entry.get('role','role')}/{Path(str(entry['local_path'])).name}"
    manifest["manifest_sha256"] = hashlib.sha256(raw_manifest_tag.encode()).hexdigest()
    return fixture


def canonicalization_controls(base_result: dict[str, Any]) -> dict[str, bool]:
    baseline = projection_sha(base_result)
    cm_baseline = sha_json(canonical_manifest(base_result["artifact_manifest"]))

    pa = mutate_paths(base_result, "/tmp/canonical-prefix-A", "path-fixture-A")
    pb = mutate_paths(base_result, "/opt/canonical-prefix-B", "path-fixture-B")
    controls: dict[str, bool] = {
        "different_local_prefixes_same_canonical_manifest": (
            sha_json(canonical_manifest(pa["artifact_manifest"])) == cm_baseline
            and sha_json(canonical_manifest(pb["artifact_manifest"])) == cm_baseline
        ),
        "different_local_prefixes_same_canonical_decision": (
            projection_sha(pa) == baseline and projection_sha(pb) == baseline
        ),
    }

    def changed(mutator) -> bool:
        fixture = copy.deepcopy(base_result)
        mutator(fixture)
        return projection_sha(fixture) != baseline

    controls["artifact_id_mutation_changes_canonical_decision"] = changed(
        lambda x: x["artifact_manifest"]["entries"][0].__setitem__(
            "expected_id", int(x["artifact_manifest"]["entries"][0]["expected_id"]) + 1
        )
    )
    controls["artifact_digest_mutation_changes_canonical_decision"] = changed(
        lambda x: x["artifact_manifest"]["entries"][0].__setitem__("expected_digest", "sha256:" + "0" * 64)
    )
    controls["content_sha_mutation_changes_canonical_decision"] = changed(
        lambda x: x["artifact_manifest"]["entries"][0].__setitem__("local_file_sha256", "1" * 64)
    )

    if isinstance(base_result.get("inherited_review"), dict):
        controls["substantive_review_mutation_changes_canonical_decision"] = changed(
            lambda x: x["inherited_review"].__setitem__("classification", "MUTATED_SUBSTANTIVE_CONTROL")
        )
    else:
        controls["substantive_review_mutation_changes_canonical_decision"] = False
    return controls


def write_result(path: Path, result: dict[str, Any]) -> None:
    raw_payload = copy.deepcopy(result)
    result["raw_execution_record_sha256"] = sha_json(raw_payload)
    cm = canonical_manifest(result.get("artifact_manifest", {}))
    result["canonical_manifest_sha256"] = sha_json(cm)
    result["canonical_decision_sha256"] = projection_sha(result)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--authority", required=True)
    ap.add_argument("--inherited-authority", required=True)
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
            "workflow_boundary_control_reached_classifier": True,
            "canonical_decision_sha256": load_json(out_path)["canonical_decision_sha256"],
        }, sort_keys=True))
        return

    boundary_controls = synthetic_boundary_controls(authority, manifest)
    boundary_controls_ok = bool(boundary_controls) and all(boundary_controls.values())

    if boundary_class != "CONTINUE_EXACT_REVIEW":
        classification = boundary_class if boundary_controls_ok else INVALID
        result = {
            "gate": authority["gate"],
            "classification": classification,
            "mode": "production",
            "boundary_reasons": boundary_reasons,
            "artifact_manifest": manifest,
            "boundary_controls": boundary_controls,
            "boundary_controls_all_pass": boundary_controls_ok,
            "inherited_review": None,
            "canonicalization_controls": {},
            "canonicalization_controls_all_pass": False,
            "claim_ceiling": authority["interpretation_ceiling"],
        }
        write_result(out_path, result)
        print(json.dumps({"classification": classification}, sort_keys=True))
        return

    role_map = entries_by_role(manifest)
    inherited_out = out_path.with_name(out_path.stem + "_inherited.json")
    inherited_script = Path(__file__).with_name("iter504t_repair_rerun_terminal_authority_review_semantics_repair.py")
    cmd = [
        sys.executable, str(inherited_script),
        "--authority", args.inherited_authority,
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

    base_result = {
        "gate": authority["gate"],
        "classification": classification,
        "mode": "production",
        "boundary_reasons": boundary_reasons,
        "artifact_manifest": manifest,
        "boundary_controls": boundary_controls,
        "boundary_controls_all_pass": boundary_controls_ok,
        "inherited_reviewer_returncode": proc.returncode,
        "inherited_reviewer_error": inherited_error,
        "inherited_review": inherited_review,
        "claim_ceiling": authority["interpretation_ceiling"],
    }
    canon_controls = canonicalization_controls(base_result)
    canon_controls_ok = all(canon_controls.values())
    if not boundary_controls_ok or not canon_controls_ok:
        classification = INVALID
    base_result["classification"] = classification
    base_result["canonicalization_controls"] = canon_controls
    base_result["canonicalization_controls_all_pass"] = canon_controls_ok

    write_result(out_path, base_result)
    final = load_json(out_path)
    print(json.dumps({
        "classification": final["classification"],
        "canonical_manifest_sha256": final["canonical_manifest_sha256"],
        "canonical_decision_sha256": final["canonical_decision_sha256"],
        "canonicalization_controls": final["canonicalization_controls"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
