"""Fail-closed validator for KMQGB future Candidate Gravity candidate records.

This validator checks methodology state only. It does not decide physical truth.
A scientifically BLOCKED record can still be structurally valid.

Schema policy:
- legacy records without ``record_schema_version`` are treated as v1.0;
- new prospective beyond-C5 seed records should use v1.1 and must declare
  one or more E1--E5 escape doors plus an explicit escape claim.
"""

from __future__ import annotations

MANDATORY_TOP_V10 = {
    "candidate_id",
    "authority",
    "parent_dynamics",
    "parameters",
    "observable_blocks",
    "comparators",
    "covariance",
    "attribution_stack",
    "rigidity",
    "promotion_gates",
}

MANDATORY_TOP_V11 = MANDATORY_TOP_V10 | {
    "record_schema_version",
    "escape_doors",
    "escape_claim",
    "escape_evidence_refs",
    "door_specific_blockers",
    "promotion",
}

MANDATORY_GATES = [f"G{i}" for i in range(11)]
ALLOWED_GATE_STATUS = {"PASS", "BLOCKED", "FAIL", "N_A"}
ALLOWED_COMPLETENESS_STATUS = {"PASS", "BLOCKED", "FAIL", "N_A"}
ALLOWED_ESCAPE_DOORS = {"E1", "E2", "E3", "E4", "E5"}


def _gate_status(gates: dict, gid: str):
    return gates.get(gid, {}).get("status")


def validate_record(record: dict) -> dict:
    errors = []
    warnings = []
    scientific_blocks = []

    version = str(record.get("record_schema_version", "1.0"))
    if version not in {"1.0", "1.1"}:
        errors.append(f"unsupported record_schema_version {version!r}")

    mandatory_top = MANDATORY_TOP_V11 if version == "1.1" else MANDATORY_TOP_V10
    missing = sorted(mandatory_top - set(record))
    if missing:
        errors.append(f"missing top-level fields: {missing}")

    # v1.1 makes the beyond-C5 escape hypothesis explicit.  A blocked escape
    # theorem is acceptable; an absent or empty declaration is not.
    if version == "1.1":
        doors = record.get("escape_doors", [])
        if not isinstance(doors, list) or not doors:
            errors.append("v1.1 prospective seed requires at least one escape_doors entry")
        else:
            bad_doors = sorted(set(doors) - ALLOWED_ESCAPE_DOORS)
            if bad_doors:
                errors.append(f"invalid escape doors: {bad_doors}")
        claim = record.get("escape_claim")
        if not isinstance(claim, str) or not claim.strip():
            errors.append("v1.1 prospective seed requires a non-empty escape_claim")
        if not isinstance(record.get("escape_evidence_refs"), list):
            errors.append("escape_evidence_refs must be a list")
        if not isinstance(record.get("door_specific_blockers"), list):
            errors.append("door_specific_blockers must be a list")

    gates = record.get("promotion_gates", {})
    for gid in MANDATORY_GATES:
        g = gates.get(gid)
        if g is None:
            errors.append(f"missing mandatory promotion gate {gid}; fail-closed as BLOCKED")
            continue
        status = g.get("status")
        if status not in ALLOWED_GATE_STATUS:
            errors.append(f"gate {gid} invalid status {status!r}")
        if status == "PASS" and not g.get("evidence_refs"):
            errors.append(f"gate {gid} PASS without evidence refs")

    # A BLOCKED/FAIL observable is a valid scientific state. It becomes a
    # methodology error only if the record simultaneously claims G1 PASS.
    blocks = record.get("observable_blocks", [])
    nonpass_blocks = []
    for b in blocks:
        comp = b.get("completeness", {})
        status = comp.get("status")
        if status not in ALLOWED_COMPLETENESS_STATUS:
            errors.append(
                f"observable block {b.get('id')} invalid completeness status {status!r}"
            )
            continue
        if status != "PASS":
            nonpass_blocks.append(b.get("id"))
            scientific_blocks.append(
                f"observable block {b.get('id')} completeness={status}"
            )

    if nonpass_blocks and _gate_status(gates, "G1") == "PASS":
        errors.append(
            f"G1 PASS inconsistent with incomplete observable blocks: {nonpass_blocks}"
        )
    if nonpass_blocks:
        warnings.append(
            "record is scientifically blocked at response completeness until all required residual blocks are PASS"
        )

    authority = record.get("authority", {})
    parent = record.get("parent_dynamics", {})
    parent_missing = (
        not authority.get("parent_object_ref")
        or not parent.get("object_ref")
        or not parent.get("declared_domain")
    )
    if parent_missing:
        scientific_blocks.append("parent dynamics/provenance incomplete")
        if _gate_status(gates, "G0") == "PASS":
            errors.append("G0 PASS inconsistent with missing parent dynamics/provenance")

    comparators = record.get("comparators", [])
    if not comparators:
        scientific_blocks.append("common-domain comparator registry absent")
        if _gate_status(gates, "G3") == "PASS" or _gate_status(gates, "G5") == "PASS":
            errors.append("G3/G5 PASS inconsistent with empty comparator registry")

    covariance = record.get("covariance", {})
    if covariance and not covariance.get("cross_block_correlations_included", False):
        warnings.append(
            "cross-block covariance not marked included; valid only if independence was explicitly established"
        )
    if not covariance.get("matrix_ref"):
        scientific_blocks.append("numeric covariance object absent")
        if _gate_status(gates, "G6") == "PASS":
            errors.append("G6 PASS inconsistent with missing covariance matrix_ref")

    promoted = bool(record.get("promotion", {}).get("ansatz_promoted", False))
    if promoted:
        bad = [gid for gid in MANDATORY_GATES if _gate_status(gates, gid) != "PASS"]
        if bad:
            errors.append(f"ansatz promotion forbidden; non-PASS gates: {bad}")

    robust_residual = bool(record.get("promotion", {}).get("robust_global_residual", False))
    fisher = bool(record.get("promotion", {}).get("fisher_promoted", False))
    resources = bool(record.get("promotion", {}).get("resources_promoted", False))
    if (fisher or resources) and not robust_residual:
        errors.append(
            "Fisher/resources promotion forbidden without robust global comparator-subtracted residual"
        )

    rigidity = record.get("rigidity", {})
    holdout = rigidity.get("holdout", {}) if isinstance(rigidity, dict) else {}
    if holdout and holdout.get("shared_parameter_retuning_on_holdout", False):
        errors.append(
            "holdout shared-parameter retuning violates predictive rigidity unless explicitly reclassified as a local parent parameter"
        )

    return {
        "valid": not errors,
        "record_schema_version": version,
        "errors": errors,
        "warnings": warnings,
        "scientific_blocks": scientific_blocks,
        "promotion_allowed": promoted and not errors,
    }


def self_test():
    blocked = {
        "candidate_id": "EXAMPLE",
        "authority": {"parent_object_ref": None},
        "parent_dynamics": {"object_ref": None, "declared_domain": None},
        "parameters": [],
        "observable_blocks": [],
        "comparators": [],
        "covariance": {"matrix_ref": None, "cross_block_correlations_included": True},
        "attribution_stack": {},
        "rigidity": {},
        "promotion_gates": {
            gid: {"status": "BLOCKED", "evidence_refs": [], "scope": "test"}
            for gid in MANDATORY_GATES
        },
        "promotion": {
            "ansatz_promoted": False,
            "robust_global_residual": False,
            "fisher_promoted": False,
            "resources_promoted": False,
        },
    }

    out = validate_record(blocked)
    assert out["valid"] and out["record_schema_version"] == "1.0"
    assert not out["promotion_allowed"]

    incomplete = dict(blocked)
    incomplete["observable_blocks"] = [
        {"id": "B1", "completeness": {"status": "BLOCKED"}}
    ]
    incomplete["promotion_gates"] = dict(blocked["promotion_gates"])
    out_incomplete = validate_record(incomplete)
    assert out_incomplete["valid"]

    bad_g1 = dict(incomplete)
    bad_g1["promotion_gates"] = dict(incomplete["promotion_gates"])
    bad_g1["promotion_gates"]["G1"] = {
        "status": "PASS",
        "evidence_refs": ["synthetic-ref"],
        "scope": "test",
    }
    out_bad_g1 = validate_record(bad_g1)
    assert not out_bad_g1["valid"]

    illegal = dict(blocked)
    illegal["promotion"] = {
        "ansatz_promoted": True,
        "robust_global_residual": False,
        "fisher_promoted": True,
        "resources_promoted": True,
    }
    out_illegal = validate_record(illegal)
    assert not out_illegal["valid"]

    v11 = dict(blocked)
    v11.update(
        {
            "record_schema_version": "1.1",
            "escape_doors": ["E1"],
            "escape_claim": "exploratory nonlocal seed leaves the local analytic EFT assumption",
            "escape_evidence_refs": [],
            "door_specific_blockers": ["parent-fixed kernel derivation missing"],
        }
    )
    out_v11 = validate_record(v11)
    assert out_v11["valid"] and out_v11["record_schema_version"] == "1.1"

    bad_v11 = dict(v11)
    bad_v11["escape_doors"] = []
    out_bad_v11 = validate_record(bad_v11)
    assert not out_bad_v11["valid"]

    return {
        "blocked_v10": out,
        "incomplete_blocked_v10": out_incomplete,
        "inconsistent_G1_PASS": out_bad_g1,
        "illegal_promotion": out_illegal,
        "valid_blocked_v11": out_v11,
        "invalid_empty_escape_v11": out_bad_v11,
    }


if __name__ == "__main__":
    print(self_test())
