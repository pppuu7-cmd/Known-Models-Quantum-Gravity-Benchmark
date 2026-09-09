"""Fail-closed prospective Candidate Gravity record v1.3 validator.

This module extends the stable v1.2 validator without rewriting historical schema
semantics.  It validates repository methodology state, not physical truth.

A record may be structurally valid while scientifically BLOCKED.
"""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

from kg_candidate_record_validator import MANDATORY_GATES, validate_record as validate_v12

ALLOWED_FF = {"FINITE", "SATURATED", "GROWING", "UNKNOWN"}
ALLOWED_REALIZATION = {"PASS", "BLOCKED", "FAIL", "N_A"}
ALLOWED_BLOCKER = {"STRUCTURAL", "NUMERICAL", "STATISTICAL", "NONE"}
ALLOWED_CLAIM = {
    "ESTABLISHED_EXTERNAL",
    "DERIVED_KMQGB",
    "REPRODUCED_EXECUTABLE",
    "OPEN_BLOCKED",
    "HYPOTHESIS_ONLY",
    "FORBIDDEN_OVERCLAIM",
}

EXTRA_REQUIRED = {
    "functional_freedom",
    "same_realization",
    "compute_authorization",
    "publication_trace",
}


def validate_v13(record: dict) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    scientific_blocks: list[str] = []

    if str(record.get("record_schema_version")) != "1.3":
        errors.append("record_schema_version must be '1.3'")

    missing = sorted(EXTRA_REQUIRED - set(record))
    if missing:
        errors.append(f"missing v1.3 fields: {missing}")

    # Reuse all mature v1.2 invariants by validating a compatibility view.
    compat = copy.deepcopy(record)
    compat["record_schema_version"] = "1.2"
    base = validate_v12(compat)
    errors.extend(f"v1.2-base: {e}" for e in base["errors"])
    warnings.extend(base["warnings"])
    scientific_blocks.extend(base["scientific_blocks"])

    ff = record.get("functional_freedom", {})
    if not isinstance(ff, dict):
        errors.append("functional_freedom must be an object")
        ff = {}
    ff_class = ff.get("classification")
    if ff_class not in ALLOWED_FF:
        errors.append(f"invalid functional_freedom classification {ff_class!r}")
    cutoffs = ff.get("hard_basis_cutoffs")
    dims = ff.get("FF_D")
    if not isinstance(cutoffs, list) or not isinstance(dims, list):
        errors.append("functional_freedom hard_basis_cutoffs and FF_D must be lists")
    elif len(cutoffs) != len(dims):
        errors.append("functional_freedom hard_basis_cutoffs and FF_D must have equal length")
    elif any(not isinstance(x, int) or x < 0 for x in cutoffs + dims):
        errors.append("functional_freedom cutoffs/dimensions must be nonnegative integers")
    if ff_class in {"FINITE", "SATURATED"}:
        if ff.get("remaining_parent_dimension") is None:
            errors.append(f"{ff_class} functional freedom requires remaining_parent_dimension")
        if not ff.get("evidence_refs"):
            errors.append(f"{ff_class} functional freedom requires evidence_refs")
    else:
        scientific_blocks.append(f"functional freedom={ff_class}")

    sr = record.get("same_realization", {})
    if not isinstance(sr, dict):
        errors.append("same_realization must be an object")
        sr = {}
    sr_status = sr.get("status")
    if sr_status not in ALLOWED_REALIZATION:
        errors.append(f"invalid same_realization status {sr_status!r}")
    if not isinstance(sr.get("realization_vector"), dict):
        errors.append("same_realization.realization_vector must be an object")
    if not isinstance(sr.get("map_refs"), list):
        errors.append("same_realization.map_refs must be a list")
    if not isinstance(sr.get("uncertainty_refs"), list):
        errors.append("same_realization.uncertainty_refs must be a list")
    if sr_status == "PASS" and not sr.get("map_refs"):
        errors.append("same_realization PASS requires an explicit identity/map evidence ref")
    if sr_status not in {"PASS", "N_A"}:
        scientific_blocks.append(f"same-realization={sr_status}")

    compute = record.get("compute_authorization", {})
    if not isinstance(compute, dict):
        errors.append("compute_authorization must be an object")
        compute = {}
    blocker = compute.get("blocker_type")
    if blocker not in ALLOWED_BLOCKER:
        errors.append(f"invalid compute blocker_type {blocker!r}")
    heavy = compute.get("heavy_compute_authorized")
    can_change = compute.get("question_can_change_terminal_classification")
    if not isinstance(heavy, bool) or not isinstance(can_change, bool):
        errors.append("compute authorization booleans are malformed")
    if heavy:
        if blocker not in {"NUMERICAL", "STATISTICAL"}:
            errors.append("heavy compute forbidden unless blocker_type is NUMERICAL or STATISTICAL")
        if not can_change:
            errors.append("heavy compute forbidden when the question cannot change terminal classification")
        if not compute.get("frozen_input_refs"):
            errors.append("heavy compute requires frozen_input_refs")
        if not compute.get("threshold_refs"):
            errors.append("heavy compute requires preregistered threshold_refs")
        if not compute.get("output_artifact"):
            errors.append("heavy compute requires a named output_artifact")
    if blocker == "STRUCTURAL" and heavy:
        errors.append("structural blocker can never authorize heavy compute")

    pub = record.get("publication_trace", {})
    if not isinstance(pub, dict):
        errors.append("publication_trace must be an object")
        pub = {}
    claim_status = pub.get("claim_status")
    if claim_status not in ALLOWED_CLAIM:
        errors.append(f"invalid publication claim_status {claim_status!r}")
    if not isinstance(pub.get("permitted_claim"), str):
        errors.append("publication_trace.permitted_claim must be a string")
    if not isinstance(pub.get("evidence_refs"), list):
        errors.append("publication_trace.evidence_refs must be a list")
    if not isinstance(pub.get("forbidden_claims"), list):
        errors.append("publication_trace.forbidden_claims must be a list")
    if claim_status in {"ESTABLISHED_EXTERNAL", "DERIVED_KMQGB", "REPRODUCED_EXECUTABLE"} and not pub.get("evidence_refs"):
        errors.append(f"{claim_status} publication status requires evidence_refs")

    gates = record.get("promotion_gates", {})
    promoted = bool(record.get("promotion", {}).get("ansatz_promoted", False))
    if promoted:
        nonpass = [gid for gid in MANDATORY_GATES if gates.get(gid, {}).get("status") != "PASS"]
        if nonpass:
            errors.append(f"v1.3 promotion forbidden; non-PASS gates: {nonpass}")
        if ff_class not in {"FINITE", "SATURATED"}:
            errors.append("v1.3 promotion forbidden without FINITE/SATURATED functional freedom")
        if sr_status != "PASS":
            errors.append("v1.3 promotion forbidden without same_realization PASS")
        if claim_status in {"OPEN_BLOCKED", "HYPOTHESIS_ONLY", "FORBIDDEN_OVERCLAIM"}:
            errors.append("v1.3 promotion inconsistent with publication claim state")

    return {
        "valid": not errors,
        "record_schema_version": "1.3",
        "errors": errors,
        "warnings": warnings,
        "scientific_blocks": sorted(set(scientific_blocks)),
        "promotion_allowed": promoted and not errors,
        "heavy_compute_allowed": bool(heavy) and not errors,
    }


def self_test() -> dict:
    root = Path(__file__).resolve().parents[1]
    template_path = root / "templates" / "candidate_gravity_record_v1_3.template.json"
    with template_path.open("r", encoding="utf-8") as fh:
        template = json.load(fh)

    valid_blocked = validate_v13(template)
    assert valid_blocked["valid"], valid_blocked
    assert not valid_blocked["promotion_allowed"]
    assert not valid_blocked["heavy_compute_allowed"]
    assert valid_blocked["scientific_blocks"]

    illegal_compute = copy.deepcopy(template)
    illegal_compute["compute_authorization"]["heavy_compute_authorized"] = True
    bad_compute = validate_v13(illegal_compute)
    assert not bad_compute["valid"]

    illegal_promotion = copy.deepcopy(template)
    illegal_promotion["promotion"]["ansatz_promoted"] = True
    bad_promotion = validate_v13(illegal_promotion)
    assert not bad_promotion["valid"]

    malformed_ff = copy.deepcopy(template)
    malformed_ff["functional_freedom"]["hard_basis_cutoffs"] = [2, 4]
    malformed_ff["functional_freedom"]["FF_D"] = [1]
    bad_ff = validate_v13(malformed_ff)
    assert not bad_ff["valid"]

    false_same_realization = copy.deepcopy(template)
    false_same_realization["same_realization"]["status"] = "PASS"
    false_same_realization["same_realization"]["map_refs"] = []
    bad_sr = validate_v13(false_same_realization)
    assert not bad_sr["valid"]

    return {
        "valid_blocked_template": valid_blocked,
        "illegal_structural_heavy_compute": bad_compute,
        "illegal_promotion": bad_promotion,
        "malformed_functional_freedom": bad_ff,
        "false_same_realization_pass": bad_sr,
    }


def main(argv: list[str]) -> int:
    if len(argv) == 1:
        out = self_test()
    elif len(argv) == 2:
        with Path(argv[1]).open("r", encoding="utf-8") as fh:
            out = validate_v13(json.load(fh))
    else:
        print(f"usage: {argv[0]} [record.json]", file=sys.stderr)
        return 2

    print(json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if ("valid" not in out or out.get("valid", True)) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
