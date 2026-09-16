#!/usr/bin/env python3
"""Exact source/realization audit for the Eq.(4) local collision test-jet map gate."""
from __future__ import annotations
import argparse, hashlib, json, math, platform
from fractions import Fraction
from pathlib import Path

REQ = (
    "EQ4_PARENT_IDENTITY",
    "TOLLER_INSERTION_IDENTITY",
    "LOCAL_COLLISION_CHART",
    "SMOOTH_REMAINDER_OBJECT",
    "PARAMETER_NORMALIZATION_LOCK",
    "JET_ORDER_7_COMPLETENESS",
    "PERMUTATION_COORDINATE_CONSISTENCY",
)
EXPECTED_SOURCE = "arXiv:2601.23162v1"


def canon_sha(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def factorial(n):
    return math.factorial(n)


def polynomial_fixture_derivatives(order=7):
    d = {}
    for i in range(order + 1):
        for j in range(order + 1 - i):
            coeff = Fraction((i + 1) * (j + 2), i + j + 1)
            d[(i, j)] = coeff * factorial(i) * factorial(j)
    return d


def basis_actions(basis, derivatives):
    vals = []
    for b in basis:
        total = Fraction(0)
        for term in b["terms"]:
            key = (int(term["i"]), int(term["j"]))
            total += Fraction(term["coefficient"]) * derivatives.get(key, Fraction(0))
        vals.append(total)
    return vals


def source_field_audit(src, v10):
    eq3 = src.get("eq3_toller_feynman", {})
    eq4 = src.get("eq4_causal_vertex", {})
    eq7 = src.get("eq7_cartan_magnetic", {})
    boundary = src.get("boundary_state", {})
    parent = (
        src.get("source_id") == EXPECTED_SOURCE
        and eq4.get("equation") == 4
        and eq4.get("wedge_count") == 10
        and eq4.get("gauge_fix") == "g_1=identity"
    )
    insertion = (
        eq3.get("equation") == 3
        and eq7.get("equation") == 7
        and "T^(" in str(eq4.get("wedge_factor", ""))
        and "T^(" in str(eq7.get("decomposition", ""))
    )
    parameter_lock = (
        "epsilon" in str(eq3.get("branch_kernel", ""))
        and bool(eq3.get("measure"))
        and bool(eq4.get("gamma_simple"))
        and bool(boundary.get("contraction_relation"))
    )
    fields = {
        "EQ4_PARENT_IDENTITY": parent,
        "TOLLER_INSERTION_IDENTITY": insertion,
        "LOCAL_COLLISION_CHART": bool(src.get("local_collision_chart") or src.get("triangle_collision_chart")),
        "SMOOTH_REMAINDER_OBJECT": bool(src.get("local_smooth_remainder") or src.get("smooth_remainder_object")),
        "PARAMETER_NORMALIZATION_LOCK": parameter_lock,
        "JET_ORDER_7_COMPLETENESS": bool(src.get("local_test_jet_order7") or src.get("jet_order_7")),
        "PERMUTATION_COORDINATE_CONSISTENCY": bool(src.get("local_collision_permutation_map")),
    }
    v10_open = any(
        p.get("id") == "CV_FINITE_OPEN_QUESTION" and p.get("status") == "NON_ACTIONABLE"
        for p in v10.get("candidate_passages", [])
    )
    return fields, v10_open


def classify(fields, *, source_id=EXPECTED_SOURCE, chart_det=1, contradictory=False, numerical_stable=True):
    if source_id != EXPECTED_SOURCE or chart_det == 0:
        return "INVALID_IMPLEMENTATION"
    if contradictory:
        return "EQ4_LOCAL_COLLISION_TEST_JET_MAP_SOURCE_INCONSISTENT_SCOPED"
    if all(fields.get(k, False) for k in REQ):
        return "EQ4_LOCAL_COLLISION_TEST_JET_MAP_CONSTRUCTED_SCOPED" if numerical_stable else "EQ4_LOCAL_COLLISION_TEST_JET_MAP_NUMERICAL_METHOD_BLOCKED_SCOPED"
    return "EQ4_LOCAL_COLLISION_TEST_JET_MAP_SOURCE_BLOCKED_SCOPED"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    root = Path(args.repo_root)
    src = load(root / "sources/arxiv_2601_23162v1_causal_vertex.json")
    v10 = load(root / "sources/arxiv_2601_23162v1_finite_renormalization_full_primary_audit_v10.json")
    v8 = load(root / "results/SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_COUNTERTERM_EQUIVALENCE_V8_CANONICAL_2026-09-16.json")
    v11 = (root / "results/SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_PHYSICAL_OBSERVABLE_QUOTIENT_TERMINAL_2026-09-16.md").read_text()

    basis = v8.get("basis", [])
    basis_lock = len(basis) == 8 and [(b.get("degree"), b.get("slot")) for b in basis] == [(0,0),(2,0),(3,0),(4,0),(5,0),(6,0),(6,1),(7,0)]
    v11_lock = "PHYSICAL_OBSERVABLE_QUOTIENT_MAP_BLOCKED_SCOPED" in v11 and "nullspace_action_rank = null" in v11
    fields, v10_open = source_field_audit(src, v10)

    # Positive exact polynomial fixture and invariant swap-chart transport.
    d = polynomial_fixture_derivatives()
    vals = basis_actions(basis, d)
    swapped = {(i,j): d.get((j,i), Fraction(0)) for (i,j) in d}
    swap_vals = basis_actions(basis, swapped)
    fixture_nontrivial = any(v != 0 for v in vals)
    swap_invariant = vals == swap_vals

    complete_fixture = {k: True for k in REQ}
    missing_fixture = dict(complete_fixture); missing_fixture["LOCAL_COLLISION_CHART"] = False
    controls = {
        "source_id_lock": src.get("source_id") == EXPECTED_SOURCE,
        "eq3_eq4_eq7_numbers_lock": src.get("eq3_toller_feynman",{}).get("equation") == 3 and src.get("eq4_causal_vertex",{}).get("equation") == 4 and src.get("eq7_cartan_magnetic",{}).get("equation") == 7,
        "v8_basis_lock": basis_lock,
        "v11_missing_map_parent_lock": v11_lock,
        "v10_open_finiteness_parent_lock": v10_open,
        "polynomial_fixture_nontrivial": fixture_nontrivial,
        "swap_chart_invariant_basis_actions": swap_invariant,
        "complete_fixture_passes": classify(complete_fixture) == "EQ4_LOCAL_COLLISION_TEST_JET_MAP_CONSTRUCTED_SCOPED",
        "missing_field_fixture_blocks": classify(missing_fixture) == "EQ4_LOCAL_COLLISION_TEST_JET_MAP_SOURCE_BLOCKED_SCOPED",
        "singular_chart_fixture_invalid": classify(complete_fixture, chart_det=0) == "INVALID_IMPLEMENTATION",
        "wrong_source_fixture_invalid": classify(complete_fixture, source_id="wrong") == "INVALID_IMPLEMENTATION",
        "contradictory_fixture_inconsistent": classify(complete_fixture, contradictory=True) == "EQ4_LOCAL_COLLISION_TEST_JET_MAP_SOURCE_INCONSISTENT_SCOPED",
        "numerical_fixture_blocks": classify(complete_fixture, numerical_stable=False) == "EQ4_LOCAL_COLLISION_TEST_JET_MAP_NUMERICAL_METHOD_BLOCKED_SCOPED",
    }
    controls_pass = all(controls.values())
    substantive = classify(fields) if controls_pass else "INVALID_IMPLEMENTATION"
    missing = [k for k in REQ if not fields.get(k, False)]
    decision = {
        "gate": "SOURCE_J1_K5_EQ4_LOCAL_COLLISION_TEST_JET_MAP_GATE",
        "classification": substantive,
        "controls_pass": controls_pass,
        "required_map_fields": fields,
        "missing_required_fields": missing,
        "map_complete": all(fields.values()),
        "jet_order_7_constructed": bool(fields.get("JET_ORDER_7_COMPLETENESS")) and all(fields.values()),
        "v8_basis_count": len(basis),
        "v8_affine_nullity": v8.get("solve",{}).get("nullity"),
        "nullspace_action_rank": None,
        "source_id": src.get("source_id"),
        "v10_open_finiteness_lock": v10_open,
        "claim_ceiling": "Local Eq4 collision/test-jet map audit only; no physical nullspace action rank, quotient, distributional existence/nonexistence, model/family failure, D7 closure, selector, or Candidate Gravity conclusion."
    }
    decision["decision_sha256"] = canon_sha(decision)
    out = {
        **decision,
        "controls": controls,
        "runtime_python": platform.python_version(),
        "fixture_basis_actions": [str(x) for x in vals],
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(decision, sort_keys=True))

if __name__ == "__main__":
    main()
