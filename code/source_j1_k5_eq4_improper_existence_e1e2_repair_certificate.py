#!/usr/bin/env python3
"""Outcome-sensitive closure certificate for the repaired Eq.(4) E1/E2 existence gate.

No network access and no external packages are used.  The scientific decision is a
pure function of source-locked structured premises plus an independently
recomputed exact K5 conormal-cycle certificate.  The current terminal label is
not stored in the input manifest.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "inputs/source_j1_k5_eq4_improper_existence_e1e2_repair_manifest_2026-09-15.json"

EXISTENCE = "SOURCE_J1_K5_EQ4_DISTRIBUTIONAL_EXISTENCE_ESTABLISHED_SCOPED"
NONEXISTENCE = "SOURCE_J1_K5_EQ4_DISTRIBUTIONAL_NONEXISTENCE_ESTABLISHED_SCOPED"
BLOCKED = "SOURCE_J1_K5_EQ4_DISTRIBUTIONAL_EXISTENCE_BLOCKED_SCOPED"
INVALID = "INVALID_IMPLEMENTATION"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def exact_rank(rows: List[List[int]]) -> int:
    """Exact rational row rank."""
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    nrow, ncol = len(a), len(a[0])
    r = 0
    for c in range(ncol):
        pivot = next((i for i in range(r, nrow) if a[i][c] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(nrow):
            if i == r or a[i][c] == 0:
                continue
            q = a[i][c]
            a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == nrow:
            break
    return r


def conormal(a: int, b: int) -> List[int]:
    """dB_ab=(e_a-e_b) tensor n0 in 4x3 gauge-fixed coords; vertex 1 fixed."""
    out = [0] * 12
    # n0=(0,0,1); vertices 2..5 occupy consecutive 3-blocks.
    if a != 1:
        out[(a - 2) * 3 + 2] += 1
    if b != 1:
        out[(b - 2) * 3 + 2] -= 1
    return out


def add(*vecs: List[int]) -> List[int]:
    return [sum(xs) for xs in zip(*vecs)]


def neg(v: List[int]) -> List[int]:
    return [-x for x in v]


def recompute_k5_witness() -> Dict[str, Any]:
    edges = [(a, b) for a in range(1, 6) for b in range(a + 1, 6)]
    vectors = {f"{a}{b}": conormal(a, b) for a, b in edges}
    all_rows = list(vectors.values())
    triangle = add(vectors["12"], vectors["23"], neg(vectors["13"]))
    star = [vectors[x] for x in ("12", "13", "14", "15")]
    wrong_sign = add(vectors["12"], vectors["23"], vectors["13"])
    rank_all = exact_rank(all_rows)
    rank_star = exact_rank(star)
    return {
        "ambient_dimension": 12,
        "edge_count": 10,
        "all_conormals_nonzero": all(any(x != 0 for x in v) for v in all_rows),
        "triangle_12_23_minus_13_exact_zero": all(x == 0 for x in triangle),
        "wrong_sign_triangle_nonzero": any(x != 0 for x in wrong_sign),
        "conormal_rank": rank_all,
        "relation_space_dimension": len(all_rows) - rank_all,
        "star_spanning_tree_rank": rank_star,
        "expected_cycle_dimension": 10 - 5 + 1,
    }


def classify(p: Dict[str, bool]) -> str:
    """Generic frozen classifier. Every scientific branch is reachable by fixtures."""
    existence = p["e1_joint_prescription"] or p["e2_sufficient_criterion_passes"]
    nonexistence = p["e4_necessary_nonexistence_theorem"]

    if p["invalidated_authority_used"]:
        return INVALID
    if existence and nonexistence:
        return INVALID
    if existence:
        return EXISTENCE
    if nonexistence:
        return NONEXISTENCE
    if (
        not p["e1_joint_prescription"]
        and not p["e2_sufficient_criterion_passes"]
        and p["e2_criterion_fails_at_allowed_witness"]
        and not p["e4_necessary_nonexistence_theorem"]
    ):
        return BLOCKED
    return INVALID


def require_bool(d: Dict[str, Any], key: str) -> bool:
    v = d.get(key)
    if type(v) is not bool:  # bool exactly, not truthy integers/strings
        raise ValueError(f"{key} must be a JSON boolean")
    return v


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("schema") != "kmqgb.eq4_improper_distributional_existence_e1e2_repair.v1":
        raise ValueError("wrong manifest schema")
    if manifest.get("prereg_commit") != "0d9615e1dec1f2fe5bcf66f3458a0e541a6b2ba4":
        raise ValueError("wrong prereg commit in manifest")

    obj = manifest["object"]
    expected_object = {
        "source_order": True,
        "j": 1,
        "rho_scope": "nonzero_real",
        "channel": "00000",
        "stratum": "full_K5_collision",
        "group_object": "gauge_fixed_SL2C^4_product_of_ten_source_defined_Toller_distributions",
    }
    if obj != expected_object:
        raise ValueError("object identity mismatch")

    records: Dict[str, Dict[str, Any]] = {}
    file_hashes: Dict[str, str] = {}
    for premise in manifest["premises"]:
        pid = premise["id"]
        if pid in records:
            raise ValueError(f"duplicate premise id {pid}")
        path = ROOT / premise["path"]
        text = path.read_text(encoding="utf-8")
        missing = [s for s in premise["required_text"] if s not in text]
        if missing:
            raise ValueError(f"{pid}: missing locked source text: {missing}")
        sf = premise["semantic_facts"]
        if not require_bool(sf, "validated"):
            raise ValueError(f"{pid}: premise not validated")
        records[pid] = premise
        file_hashes[premise["path"]] = sha256_file(path)

    required_ids = {
        "P1_PUBLISHED_IEPSILON_SCOPE",
        "P2_COHERENT_CONTACT_HORMANDER",
        "P3_ALIGNED_CONTACT_CYCLESPACE",
        "P4_FULL_COLLISION_ABSOLUTE_DIVERGENCE",
        "P5_EQ4_V2_CRITIC_INVALIDATION",
    }
    if set(records) != required_ids:
        raise ValueError("premise set mismatch")

    p1 = records["P1_PUBLISHED_IEPSILON_SCOPE"]["semantic_facts"]
    p2 = records["P2_COHERENT_CONTACT_HORMANDER"]["semantic_facts"]
    p3 = records["P3_ALIGNED_CONTACT_CYCLESPACE"]["semantic_facts"]
    p4 = records["P4_FULL_COLLISION_ABSOLUTE_DIVERGENCE"]["semantic_facts"]
    p5 = records["P5_EQ4_V2_CRITIC_INVALIDATION"]["semantic_facts"]

    witness = recompute_k5_witness()
    witness_ok = all(
        [
            witness["all_conormals_nonzero"],
            witness["triangle_12_23_minus_13_exact_zero"],
            witness["wrong_sign_triangle_nonzero"],
            witness["conormal_rank"] == 4,
            witness["relation_space_dimension"] == 6,
            witness["star_spanning_tree_rank"] == 4,
            witness["expected_cycle_dimension"] == 6,
        ]
    )

    # Cross-check semantic premises. These are constraints, not terminal labels.
    if require_bool(p1, "joint_K5_collision_prescription_established"):
        e1_joint = True
    else:
        e1_joint = False
    if not require_bool(p1, "one_wedge_distributions_source_defined"):
        raise ValueError("one-wedge source identity lost")

    e2_pass = (
        require_bool(p2, "standard_Hormander_sufficient_product_criterion_passes")
        or require_bool(p3, "standard_Hormander_sufficient_product_criterion_passes")
    )
    e2_fail_witness = (
        require_bool(p2, "allowed_collision_witness")
        and require_bool(p3, "allowed_collision_witness")
        and require_bool(p2, "standard_Hormander_sufficient_product_criterion_fails_at_allowed_witness")
        and require_bool(p3, "standard_Hormander_sufficient_product_criterion_fails_at_allowed_witness")
        and witness_ok
    )
    if e2_pass and e2_fail_witness:
        raise ValueError("contradictory E2 premises")

    # A necessary nonexistence theorem must be explicitly validated as such.
    necessary_flags = [
        require_bool(p1, "necessary_nonexistence_theorem"),
        require_bool(p2, "necessary_nonexistence_theorem"),
        require_bool(p3, "necessary_nonexistence_theorem"),
        require_bool(p4, "necessary_nonexistence_theorem"),
        require_bool(p5, "necessary_nonexistence_theorem"),
    ]
    e4_nonexistence = any(necessary_flags)
    if not require_bool(p4, "distributional_nonexistence_implied") and require_bool(
        p4, "ordinary_absolute_Haar_local_integrability"
    ):
        # This branch is allowed in a synthetic future manifest, but the present
        # frozen record says absolute integrability is false. Keep it explicit.
        pass

    if require_bool(p5, "v2_authority_result_validated_scientific_premise"):
        invalidated_used = True
    else:
        invalidated_used = False
    if not require_bool(p5, "must_exclude_from_decision"):
        raise ValueError("Critic exclusion guard missing")

    predicates = {
        "e1_joint_prescription": e1_joint,
        "e2_sufficient_criterion_passes": e2_pass,
        "e2_criterion_fails_at_allowed_witness": e2_fail_witness,
        "e4_necessary_nonexistence_theorem": e4_nonexistence,
        "invalidated_authority_used": invalidated_used,
    }

    # Outcome-sensitivity controls use the exact same decision function.
    fixture_cases = {
        "positive_source_joint": {
            "input": {**predicates, "e1_joint_prescription": True, "e2_criterion_fails_at_allowed_witness": False},
            "expected": EXISTENCE,
        },
        "positive_sufficient_criterion": {
            "input": {**predicates, "e2_sufficient_criterion_passes": True, "e2_criterion_fails_at_allowed_witness": False},
            "expected": EXISTENCE,
        },
        "positive_necessary_nonexistence": {
            "input": {**predicates, "e1_joint_prescription": False, "e2_sufficient_criterion_passes": False, "e4_necessary_nonexistence_theorem": True},
            "expected": NONEXISTENCE,
        },
        "negative_blocked": {
            "input": {**predicates, "e1_joint_prescription": False, "e2_sufficient_criterion_passes": False, "e2_criterion_fails_at_allowed_witness": True, "e4_necessary_nonexistence_theorem": False},
            "expected": BLOCKED,
        },
        "invalidated_authority": {
            "input": {**predicates, "invalidated_authority_used": True},
            "expected": INVALID,
        },
        "contradictory_exist_nonexist": {
            "input": {**predicates, "e1_joint_prescription": True, "e4_necessary_nonexistence_theorem": True},
            "expected": INVALID,
        },
    }
    controls: Dict[str, Any] = {}
    for name, case in fixture_cases.items():
        got = classify(case["input"])
        controls[name] = {"expected": case["expected"], "got": got, "pass": got == case["expected"]}
    all_controls_pass = all(x["pass"] for x in controls.values())
    if not all_controls_pass:
        raise ValueError("outcome-sensitivity fixture failure")

    classification = classify(predicates)

    result = {
        "schema": "kmqgb.eq4_improper_distributional_existence_e1e2_repair.result.v1",
        "prereg_commit": manifest["prereg_commit"],
        "manifest_sha256": sha256_file(MANIFEST),
        "object": obj,
        "source_locked_file_sha256": file_hashes,
        "exact_k5_witness_recomputation": witness,
        "derived_predicates": predicates,
        "outcome_sensitivity_controls": controls,
        "all_controls_pass": all_controls_pass,
        "classification": classification,
        "claim_ceiling": {
            "distributional_nonexistence_proved": classification == NONEXISTENCE,
            "uniqueness_decided": False,
            "family_closure": False,
            "D7_S2_closed": False,
            "D7_S3_closed": False,
            "D7_S4_closed": False,
            "candidate_gravity_active": False,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
