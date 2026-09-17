#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

REVIEW_BLOCKED = "ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED"
INVALID = "INVALID_IMPLEMENTATION"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha_json(obj: Any) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--control", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    a = load_json(Path(args.a))
    b = load_json(Path(args.b))
    control = load_json(Path(args.control))

    lane_class_agree = a.get("classification") == b.get("classification")
    lane_canonical_agree = a.get("canonical_decision_sha256") == b.get("canonical_decision_sha256")
    lane_manifest_agree = a.get("canonical_manifest_sha256") == b.get("canonical_manifest_sha256")
    inherited_agree = a.get("inherited_review") == b.get("inherited_review")
    boundary_control_ok = (
        control.get("classification") == REVIEW_BLOCKED
        and control.get("workflow_boundary_control_reached_classifier") is True
        and control.get("artifact_manifest", {}).get("mode") == "boundary_control"
    )
    control_entries = control.get("artifact_manifest", {}).get("entries", [])
    simulated_role = control.get("artifact_manifest", {}).get("simulate_missing_role")
    simulated = next((e for e in control_entries if isinstance(e, dict) and e.get("role") == simulated_role), None)
    boundary_download_failure_observed = (
        isinstance(simulated, dict)
        and simulated.get("download_attempted") is True
        and isinstance(simulated.get("download_returncode"), int)
        and simulated.get("download_returncode") != 0
        and simulated.get("state") == "MISSING_OR_UNAVAILABLE"
    )

    aggregate_controls = {
        "lane_classification_agreement": lane_class_agree,
        "lane_canonical_decision_sha256_agreement": lane_canonical_agree,
        "lane_canonical_manifest_sha256_agreement": lane_manifest_agree,
        "lane_inherited_substantive_review_agreement": inherited_agree,
        "lane_boundary_controls_all_pass": a.get("boundary_controls_all_pass") is True and b.get("boundary_controls_all_pass") is True,
        "lane_canonicalization_controls_all_pass": a.get("canonicalization_controls_all_pass") is True and b.get("canonicalization_controls_all_pass") is True,
        "workflow_boundary_missing_artifact_control_blocked": boundary_control_ok,
        "workflow_boundary_actual_download_failure_observed": boundary_download_failure_observed,
    }
    controls_ok = all(aggregate_controls.values())
    classification = a.get("classification") if controls_ok and lane_class_agree else INVALID

    canonical_summary = {
        "gate": a.get("gate"),
        "classification": classification,
        "aggregate_controls": aggregate_controls,
        "lane_a_canonical_decision_sha256": a.get("canonical_decision_sha256"),
        "lane_b_canonical_decision_sha256": b.get("canonical_decision_sha256"),
        "canonical_manifest_sha256": a.get("canonical_manifest_sha256") if lane_manifest_agree else None,
        "boundary_control_classification": control.get("classification"),
        "boundary_control_download_failure_observed": boundary_download_failure_observed,
        "claim_ceiling": a.get("claim_ceiling"),
    }
    out = {
        "gate": a.get("gate"),
        "classification": classification,
        "lanes_agree": lane_class_agree and lane_canonical_agree and lane_manifest_agree and inherited_agree,
        "aggregate_controls": aggregate_controls,
        "aggregate_controls_all_pass": controls_ok,
        "lane_a_canonical_decision_sha256": a.get("canonical_decision_sha256"),
        "lane_b_canonical_decision_sha256": b.get("canonical_decision_sha256"),
        "lane_a_raw_execution_record_sha256": a.get("raw_execution_record_sha256"),
        "lane_b_raw_execution_record_sha256": b.get("raw_execution_record_sha256"),
        "canonical_manifest_sha256": canonical_summary["canonical_manifest_sha256"],
        "lane_a": a,
        "lane_b": b,
        "boundary_control": control,
        "claim_ceiling": a.get("claim_ceiling"),
        "aggregate_canonical_summary": canonical_summary,
    }
    out["aggregate_decision_sha256"] = sha_json(canonical_summary)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "classification": classification,
        "aggregate_controls": aggregate_controls,
        "aggregate_decision_sha256": out["aggregate_decision_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
