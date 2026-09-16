#!/usr/bin/env python3
"""Exact authority/action audit for the V8 physical-observable quotient gate."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from pathlib import Path

GATE = "SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_PHYSICAL_OBSERVABLE_QUOTIENT_GATE"
EXPECTED_NULLSPACE = [
    ["1","0","0","0","0","0","0","0"],
    ["0","1","0","0","0","0","0","0"],
    ["0","0","1","0","0","0","0","0"],
    ["0","0","0","0","1","0","0","0"],
    ["0","0","0","18","0","6","1","0"],
    ["0","0","0","0","0","0","0","1"],
]
EXPECTED_DEGREES = [(0,0),(2,0),(3,0),(4,0),(5,0),(6,0),(6,1),(7,0)]


def f(x):
    return Fraction(str(x))


def rank(matrix):
    if not matrix:
        return 0
    a = [[f(x) for x in row] for row in matrix]
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x/p for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                q = a[i][c]
                a[i] = [x-q*y for x,y in zip(a[i],a[r])]
        r += 1
        if r == m:
            break
    return r


def matvec(row, vec):
    return sum((f(a)*f(b) for a,b in zip(row, vec)), Fraction(0))


def action_matrix(j_rows, nullspace):
    # rows = observables, columns = six null directions
    return [[matvec(row, vec) for vec in nullspace] for row in j_rows]


def classify_map(*, same_realization, explicit_map, complete, j_rows, nullspace):
    if not same_realization:
        return "INVALID_IMPLEMENTATION", None
    if not explicit_map:
        return "PHYSICAL_OBSERVABLE_QUOTIENT_MAP_BLOCKED_SCOPED", None
    actions = action_matrix(j_rows, nullspace)
    arank = rank(actions)
    if arank > 0:
        return "PHYSICAL_OBSERVABLE_FINITE_FREEDOM_DISTINGUISHABLE_SCOPED", arank
    if complete:
        return "PHYSICAL_OBSERVABLE_QUOTIENT_ZERO_ACTION_COMPLETE_SCOPED", 0
    return "PHYSICAL_OBSERVABLE_QUOTIENT_PARTIAL_SCOPED", 0


def blob_sha(repo_root, path):
    return subprocess.check_output(["git", "-C", str(repo_root), "hash-object", path], text=True).strip()


def stable_hash(obj):
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--out", required=True)
    ap.add_argument("--lane", required=True)
    args = ap.parse_args()
    root = Path(args.repo_root)

    ledger_path = root / "inputs/source_j1_k5_triangle_derivative_contact_physical_observable_quotient_authority.json"
    ledger = json.loads(ledger_path.read_text())
    blob_checks = {}
    for name, rec in ledger["objects"].items():
        actual = blob_sha(root, rec["path"])
        blob_checks[name] = {"expected": rec["blob_sha"], "actual": actual, "match": actual == rec["blob_sha"]}

    v8 = json.loads((root / ledger["objects"]["v8_canonical"]["path"]).read_text())
    eq4 = json.loads((root / ledger["objects"]["eq4_source_snapshot"]["path"]).read_text())
    iter453_text = (root / ledger["objects"]["eq4_topology_parent"]["path"]).read_text()
    v10_audit = json.loads((root / ledger["objects"]["v10_causal_full_primary_audit"]["path"]).read_text())
    v10_terminal = (root / ledger["objects"]["v10_terminal"]["path"]).read_text()

    basis_degrees = [(int(x["degree"]), int(x["slot"])) for x in v8["basis"]]
    ns = v8["solve"]["nullspace_basis"]

    v8_lock = (
        len(v8["basis"]) == 8 and
        int(v8["solve"]["rank"]) == 2 and
        int(v8["solve"]["augmented_rank"]) == 2 and
        int(v8["solve"]["nullity"]) == 6 and
        basis_degrees == EXPECTED_DEGREES and
        ns == EXPECTED_NULLSPACE
    )

    eq4_obj = eq4.get("eq4_causal_vertex", {})
    boundary = eq4.get("boundary_state", {})
    eq4_lock = (
        eq4.get("source_id") == "arXiv:2601.23162v1" and
        eq4_obj.get("equation") == 4 and
        eq4_obj.get("wedge_count") == 10 and
        eq4_obj.get("group_integrations") == ["g_2","g_3","g_4","g_5"] and
        eq4_obj.get("gauge_fix") == "g_1=identity" and
        eq4_obj.get("gamma_simple") == "(rho,k)=(gamma*j_ab,j_ab)" and
        boundary.get("spin_count") == 10 and
        boundary.get("intertwiner_count") == 5 and
        "contract" in boundary.get("contraction_relation", "")
    )

    iter453_scope = (
        "synthetic deterministic finite-dimensional tensors, not physical Toller matrix elements" in iter453_text and
        "does **not** establish convergence, absolute integrability, finite normalization" in iter453_text
    )
    v10_scope = (
        v10_audit.get("actionable_selector_count") == 0 and
        any(x.get("id") == "CV_EQ4_PRODUCT_VERTEX" and x.get("status") == "NON_ACTIONABLE" for x in v10_audit.get("candidate_passages", [])) and
        "does not provide a simultaneous-contact product-extension or finite-normalization prescription" in v10_terminal
    )

    # Actionable maps must be explicit in the frozen authority corpus. No field-name heuristic can create authority;
    # these exact reserved keys are accepted only if a future prospectively frozen source record supplies them.
    explicit_records = []
    for holder_name, holder in (("eq4_source_snapshot", eq4), ("v10_causal_audit", v10_audit)):
        rec = holder.get("v8_local_collision_observable_jet_map") if isinstance(holder, dict) else None
        if isinstance(rec, dict):
            explicit_records.append((holder_name, rec))

    map_present = len(explicit_records) == 1
    complete = False
    map_rows = []
    map_same_realization = True
    if map_present:
        _, rec = explicit_records[0]
        map_same_realization = rec.get("same_eq4_realization") is True and rec.get("observable_identity_preserved") is True
        complete = rec.get("observable_family_complete_for_local_extension_quotient") is True
        map_rows = rec.get("jet_rows", [])
        if not (isinstance(map_rows, list) and all(isinstance(r, list) and len(r) == 8 for r in map_rows)):
            map_same_realization = False

    classification, actual_rank = classify_map(
        same_realization=map_same_realization,
        explicit_map=map_present,
        complete=complete,
        j_rows=map_rows,
        nullspace=ns,
    )

    # Outcome-sensitive exact fixtures.
    zero_complete_cls, zero_complete_rank = classify_map(
        same_realization=True, explicit_map=True, complete=True,
        j_rows=[["0"]*8, ["0"]*8], nullspace=ns)
    distinguish_cls, distinguish_rank = classify_map(
        same_realization=True, explicit_map=True, complete=True,
        j_rows=[["1","0","0","0","0","0","0","0"]], nullspace=ns)
    zero_incomplete_cls, zero_incomplete_rank = classify_map(
        same_realization=True, explicit_map=True, complete=False,
        j_rows=[["0"]*8], nullspace=ns)
    wrong_cls, _ = classify_map(
        same_realization=False, explicit_map=True, complete=True,
        j_rows=[["0"]*8], nullspace=ns)

    controls = {
        "all_authority_blob_locks": all(x["match"] for x in blob_checks.values()),
        "v8_exact_parent_lock": v8_lock,
        "eq4_boundary_object_lock": eq4_lock,
        "iter453_synthetic_scope_lock": iter453_scope,
        "v10_no_extension_selector_scope_lock": v10_scope,
        "synthetic_complete_zero_classifies_zero_quotient": zero_complete_cls == "PHYSICAL_OBSERVABLE_QUOTIENT_ZERO_ACTION_COMPLETE_SCOPED" and zero_complete_rank == 0,
        "synthetic_nonzero_classifies_distinguishable": distinguish_cls == "PHYSICAL_OBSERVABLE_FINITE_FREEDOM_DISTINGUISHABLE_SCOPED" and distinguish_rank == 1,
        "zero_without_completeness_not_quotient": zero_incomplete_cls == "PHYSICAL_OBSERVABLE_QUOTIENT_PARTIAL_SCOPED" and zero_incomplete_rank == 0,
        "wrong_realization_invalid": wrong_cls == "INVALID_IMPLEMENTATION",
    }
    controls_pass = all(controls.values())
    if not controls_pass:
        classification = "INVALID_IMPLEMENTATION"
        actual_rank = None

    decision = {
        "gate": GATE,
        "classification": classification,
        "map_present": map_present,
        "observable_completeness_authority": complete,
        "nullspace_action_rank": actual_rank,
        "v8_basis_count": len(v8["basis"]),
        "v8_affine_nullity": int(v8["solve"]["nullity"]),
        "eq4_source_id": eq4.get("source_id"),
        "eq4_equation": eq4_obj.get("equation"),
    }
    decision_sha256 = stable_hash(decision)

    out = {
        **decision,
        "decision_sha256": decision_sha256,
        "controls": controls,
        "controls_pass": controls_pass,
        "authority_blob_checks": blob_checks,
        "v8_nullspace_basis": ns,
        "basis_degree_slots": basis_degrees,
        "explicit_map_records_found": [x[0] for x in explicit_records],
        "frozen_actionable_map_predicate": ledger["actionable_map_predicate"],
        "zero_quotient_extra_requirement": ledger["zero_quotient_extra_requirement"],
        "new_fact": "Whether the terminal V8 six-dimensional local finite-renormalization freedom has an exact source-authorized action on the pinned Eq. (4) boundary observable family, distinguishing zero-action quotient, nonzero physical sensitivity, partial coverage, and missing-map BLOCKED outcomes.",
        "claim_ceiling": "Same-realization V8 local delta-double-prime triangle versus pinned Eq. (4) boundary observable authority only; no distributional existence/nonexistence, full-K5/model/family failure, D7 closure/selector, or Candidate Gravity authority.",
        "lane": args.lane,
    }
    p = Path(args.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"classification": classification, "controls_pass": controls_pass, "decision_sha256": decision_sha256, "map_present": map_present, "nullspace_action_rank": actual_rank}, sort_keys=True))


if __name__ == "__main__":
    main()
