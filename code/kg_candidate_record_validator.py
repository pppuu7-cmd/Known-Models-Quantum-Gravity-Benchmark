"""Fail-closed validator for KMQGB future Candidate Gravity candidate records.

This validator checks methodology state only. It does not decide physical truth.
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


def validate_record(record: dict) -> dict:
    errors = []
    warnings = []

    missing = sorted(MANDATORY_TOP - set(record))
    if missing:
        errors.append(f"missing top-level fields: {missing}")

    blocks = record.get("observable_blocks", [])
    for b in blocks:
        comp = b.get("completeness", {})
        if comp.get("status") != "PASS":
            errors.append(f"observable block {b.get('id')} has incomplete response: {comp.get('status', 'MISSING')}")

    gates = record.get("promotion_gates", {})
    for gid in MANDATORY_GATES:
        g = gates.get(gid)
        if g is None:
            errors.append(f"missing mandatory promotion gate {gid}; fail-closed as BLOCKED")
            continue
        status = g.get("status")
        if status not in ALLOWED_GATE_STATUS:
            errors.append(f"gate {gid} invalid status {status!r}")
        if not g.get("evidence_refs") and status == "PASS":
            errors.append(f"gate {gid} PASS without evidence refs")

    promoted = bool(record.get("promotion", {}).get("ansatz_promoted", False))
    if promoted:
        bad = [gid for gid in MANDATORY_GATES if gates.get(gid, {}).get("status") != "PASS"]
        if bad:
            errors.append(f"ansatz promotion forbidden; non-PASS gates: {bad}")

    robust_residual = bool(record.get("promotion", {}).get("robust_global_residual", False))
    fisher = bool(record.get("promotion", {}).get("fisher_promoted", False))
    resources = bool(record.get("promotion", {}).get("resources_promoted", False))
    if (fisher or resources) and not robust_residual:
        errors.append("Fisher/resources promotion forbidden without robust global comparator-subtracted residual")

    rigidity = record.get("rigidity", {})
    holdout = rigidity.get("holdout", {}) if isinstance(rigidity, dict) else {}
    if holdout and holdout.get("shared_parameter_retuning_on_holdout", False):
        errors.append("holdout shared-parameter retuning violates predictive rigidity unless explicitly reclassified as a local parent parameter")

    covariance = record.get("covariance", {})
    if covariance and not covariance.get("cross_block_correlations_included", False):
        warnings.append("cross-block covariance not marked included; valid only if independence was explicitly established")

    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "promotion_allowed": promoted and not errors,
    }


def self_test():
    blocked = {
        "candidate_id": "EXAMPLE",
        "authority": {},
        "parent_dynamics": {},
        "parameters": [],
        "observable_blocks": [],
        "comparators": [],
        "covariance": {"cross_block_correlations_included": True},
        "attribution_stack": {},
        "rigidity": {},
        "promotion_gates": {gid: {"status": "BLOCKED", "evidence_refs": [], "scope": "test"} for gid in MANDATORY_GATES},
        "promotion": {"ansatz_promoted": False, "robust_global_residual": False, "fisher_promoted": False, "resources_promoted": False},
    }
    out = validate_record(blocked)
    assert out["valid"]
    assert not out["promotion_allowed"]

    illegal = dict(blocked)
    illegal["promotion"] = {"ansatz_promoted": True, "robust_global_residual": False, "fisher_promoted": True, "resources_promoted": True}
    out2 = validate_record(illegal)
    assert not out2["valid"]
    return {"blocked_record": out, "illegal_promotion": out2}


if __name__ == "__main__":
    print(self_test())
