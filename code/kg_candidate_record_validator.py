"""Fail-closed validator for KMQGB future Candidate Gravity candidate records.

This validator checks methodology state only. It does not decide physical truth.
A scientifically BLOCKED record can still be structurally valid.
"""

from __future__ import annotations

MANDATORY_TOP = {
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

MANDATORY_GATES = [f"G{i}" for i in range(11)]
ALLOWED_GATE_STATUS = {"PASS", "BLOCKED", "FAIL", "N_A"}
ALLOWED_COMPLETENESS_STATUS = {"PASS", "BLOCKED", "FAIL", "N_A"}


def _gate_status(gates: dict, gid: str):
    return gates.get(gid, {}).get("status")


def validate_record(record: dict) -> dict:
    errors = []
    warnings = []
    scientific_blocks = []

    missing = sorted(MANDATORY_TOP - set(record))
    if missing:
        errors.append(f"missing top-level fields: {missing}")

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

    # A BLOCKED/FAIL observable is a valid scientific state.  It becomes a
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
        bad = [
            gid
            for gid in MANDATORY_GATES
            if _gate_status(gates, gid) != "PASS"
        ]
        if bad:
            errors.append(f"ansatz promotion forbidden; non-PASS gates: {bad}")

    robust_residual = bool(
        record.get("promotion", {}).get("robust_global_residual", False)
    )
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
        "covariance": {
            "matrix_ref": None,
            "cross_block_correlations_included": True,
        },
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
    assert out["valid"]
    assert not out["promotion_allowed"]

    # Scientifically blocked response is still a valid record.
    incomplete = dict(blocked)
    incomplete["observable_blocks"] = [
        {"id": "B1", "completeness": {"status": "BLOCKED"}}
    ]
    incomplete["promotion_gates"] = dict(blocked["promotion_gates"])
    out_incomplete = validate_record(incomplete)
    assert out_incomplete["valid"]

    # The same block makes G1 PASS internally inconsistent.
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

    return {
        "blocked_record": out,
        "incomplete_blocked_record": out_incomplete,
        "inconsistent_G1_PASS": out_bad_g1,
        "illegal_promotion": out_illegal,
    }


if __name__ == "__main__":
    print(self_test())
