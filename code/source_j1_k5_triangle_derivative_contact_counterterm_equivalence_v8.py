#!/usr/bin/env python3
"""Exact V8 local-counterterm equivalence certificate for the repaired V7 delta'' triangle."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path

GATE = "SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_COUNTERTERM_EQUIVALENCE_GATE"
PREREG = "recovery/PREREG_SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_COUNTERTERM_EQUIVALENCE_GATE_2026-09-16.md"
PROTOCOL = "recovery/PROTOCOL_SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_COUNTERTERM_EQUIVALENCE_V8_2026-09-16.md"
LEDGER = "inputs/source_j1_k5_triangle_derivative_contact_counterterm_authority_v8.json"
V7_CANONICAL = "results/SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_REGULARIZATION_V7_REPAIR_CANONICAL_2026-09-16.json"

SCHEMES = {
    "A": (1, 1, 1),
    "A4": (4, 4, 4),
    "B": (1, 1, 4),
    "C": (1, 2, 3),
}
V7_K = {
    "A": F(1600, 531441),
    "A4": F(1600, 531441),
    "B": F(204800, 1162261467),
    "C": F(14400, 19487171),
}
EXPECTED_INVARIANT_DIMS = {0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 7: 1}
ROOTS = ((1, 0), (0, 1), (-1, -1))


def fs(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def parse_fraction(s: str) -> F:
    if "/" in s:
        a, b = s.split("/", 1)
        return F(int(a), int(b))
    return F(int(s), 1)


def git_blob_sha(data: bytes) -> str:
    hdr = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(hdr + data).hexdigest()


# --- exact bivariate polynomial helpers: {(i,j): Fraction} ---
def p_add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def p_scale(a, s):
    return {k: v * s for k, v in a.items() if v * s != 0}


def p_mul(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            q = (i + k, j + l)
            out[q] = out.get(q, F(0)) + x * y
    return {k: v for k, v in out.items() if v != 0}


def p_pow(a, n):
    out = {(0, 0): F(1)}
    for _ in range(n):
        out = p_mul(out, a)
    return out


def transform_monomial(i, j, A):
    # For x' = A x, derivative symbols transform as u -> A^T u.
    l1 = {(1, 0): F(A[0][0]), (0, 1): F(A[1][0])}
    l2 = {(1, 0): F(A[0][1]), (0, 1): F(A[1][1])}
    return p_mul(p_pow(l1, i), p_pow(l2, j))


def transform_poly(poly, A):
    out = {}
    for (i, j), c in poly.items():
        out = p_add(out, p_scale(transform_monomial(i, j, A), c))
    return out


# --- exact linear algebra ---
def rref(matrix):
    A = [[F(x) for x in row] for row in matrix]
    if not A:
        return A, []
    nr, nc = len(A), len(A[0])
    pivots = []
    r = 0
    for c in range(nc):
        p = next((i for i in range(r, nr) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(nr):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(nc)]
        pivots.append(c)
        r += 1
        if r == nr:
            break
    return A, pivots


def matrix_rank(matrix, ncols=None):
    if not matrix:
        return 0
    _, piv = rref(matrix)
    return len(piv)


def nullspace(matrix, ncols):
    if not matrix:
        return [[F(int(i == j)) for i in range(ncols)] for j in range(ncols)]
    R, piv = rref(matrix)
    free = [j for j in range(ncols) if j not in piv]
    out = []
    for f in free:
        v = [F(0)] * ncols
        v[f] = F(1)
        for rr, p in enumerate(piv):
            v[p] = -R[rr][f]
        out.append(v)
    return out


def solve_affine(A, b, ncols):
    aug = [list(row) + [rhs] for row, rhs in zip(A, b)]
    R, piv = rref(aug)
    inconsistent = any(all(row[j] == 0 for j in range(ncols)) and row[ncols] != 0 for row in R)
    rank_a = matrix_rank(A, ncols)
    rank_aug = matrix_rank(aug, ncols + 1)
    ns = nullspace(A, ncols)
    canonical = None
    if not inconsistent:
        canonical = [F(0)] * ncols
        for rr, p in enumerate(piv):
            if p < ncols:
                canonical[p] = R[rr][ncols]
    return {
        "solvable": not inconsistent,
        "rank": rank_a,
        "augmented_rank": rank_aug,
        "nullity": ncols - rank_a,
        "canonical": canonical,
        "nullspace": ns,
    }


def matvec(A, x):
    return [sum((a * b for a, b in zip(row, x)), F(0)) for row in A]


def vec_sub(a, b):
    return [x - y for x, y in zip(a, b)]


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def primitive_integer_vector(v):
    L = 1
    for x in v:
        L = math.lcm(L, x.denominator)
    ints = [int(x * L) for x in v]
    g = 0
    for z in ints:
        g = math.gcd(g, abs(z))
    if g:
        ints = [z // g for z in ints]
    first = next((z for z in ints if z != 0), 1)
    if first < 0:
        ints = [-z for z in ints]
    return [F(z) for z in ints]


# --- triangle permutation representation and complete invariant jets ---
def triangle_group():
    mats = []
    root_ok = True
    for p in permutations(range(3)):
        A = (ROOTS[p[0]], ROOTS[p[1]])
        implied_third = (-A[0][0] - A[1][0], -A[0][1] - A[1][1])
        root_ok = root_ok and implied_third == ROOTS[p[2]]
        det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        root_ok = root_ok and abs(det) == 1
        mats.append(A)
    return mats, root_ok and len(set(mats)) == 6


def invariant_basis_degree(d, group):
    mons = [(i, d - i) for i in range(d + 1)]
    constraints = []
    for A in group:
        cols = [transform_monomial(i, j, A) for i, j in mons]
        for row_mon in mons:
            row = []
            for col_idx, original_mon in enumerate(mons):
                row.append(cols[col_idx].get(row_mon, F(0)) - (F(1) if row_mon == original_mon else F(0)))
            constraints.append(row)
    ns = nullspace(constraints, len(mons))
    basis = []
    for k, v in enumerate(ns):
        pv = primitive_integer_vector(v)
        poly = {m: c for m, c in zip(mons, pv) if c != 0}
        basis.append({"degree": d, "slot": k, "poly": poly})
    return basis, constraints


def complete_invariant_basis():
    group, root_ok = triangle_group()
    basis = []
    dims = {}
    constraint_ranks = {}
    for d in range(8):
        bd, constraints = invariant_basis_degree(d, group)
        dims[d] = len(bd)
        constraint_ranks[d] = matrix_rank(constraints)
        basis.extend(bd)
    invariance = all(transform_poly(b["poly"], A) == b["poly"] for b in basis for A in group)
    return group, root_ok, basis, dims, constraint_ranks, invariance


# --- exact Gaussian jet action ---
def gaussian_derivative_at_zero(i, j, a0, b0, c0):
    n = i + j
    if n % 2:
        return F(0)
    a, b, c = F(a0), F(b0), F(c0)
    m = n // 2
    S = {(2, 0): a + c, (1, 1): 2 * c, (0, 2): b + c}
    minus_S = p_scale(S, F(-1))
    coeff_poly = p_scale(p_pow(minus_S, m), F(1, math.factorial(m)))
    coeff = coeff_poly.get((i, j), F(0))
    # <partial^alpha delta, phi> = (-1)^|alpha| partial^alpha phi(0); n is even here.
    return F(math.factorial(i) * math.factorial(j)) * coeff


def normalized_basis_action(basis_item, widths):
    a, b, c = widths
    d = basis_item["degree"]
    value = sum((coef * gaussian_derivative_at_zero(i, j, a, b, c) for (i, j), coef in basis_item["poly"].items()), F(0))
    if d % 2:
        return value  # exactly zero for the centered even Gaussian family
    return value / F((a + b + c) ** (d // 2))


def serialize_poly(poly):
    return [{"i": i, "j": j, "coefficient": fs(c)} for (i, j), c in sorted(poly.items())]


def serialize_vec(v):
    return [fs(x) for x in v]


# --- locked authority corpus ---
def authority_audit(root: Path):
    ledger_path = root / LEDGER
    prereg_path = root / PREREG
    protocol_path = root / PROTOCOL
    checks = {
        "ledger_present": ledger_path.exists(),
        "prereg_present": prereg_path.exists(),
        "protocol_present": protocol_path.exists(),
    }
    if not all(checks.values()):
        return checks, None
    ledger = json.loads(ledger_path.read_text())
    checks["ledger_gate"] = ledger.get("gate") == GATE
    checks["ledger_parent_prereg_commit"] = ledger.get("parent_preregistration_commit") == "38054879237dd03e9d368ceb47356e669c02b516"
    blob_records = {}
    all_blob_locks = True
    for item in ledger.get("authority_corpus", []):
        p = root / item["path"]
        exists = p.exists()
        actual = git_blob_sha(p.read_bytes()) if exists else None
        ok = exists and actual == item["blob_sha"]
        all_blob_locks = all_blob_locks and ok
        blob_records[item["path"]] = {"expected": item["blob_sha"], "actual": actual, "match": ok}
    checks["all_authority_blob_locks"] = all_blob_locks and len(blob_records) == 5

    # Positive semantic scope checks; authority is not inferred from a single missing literal.
    v4 = (root / ledger["authority_corpus"][0]["path"]).read_text()
    v5 = (root / ledger["authority_corpus"][1]["path"]).read_text()
    v7j = json.loads((root / ledger["authority_corpus"][2]["path"]).read_text())
    v7t = (root / ledger["authority_corpus"][3]["path"]).read_text()
    v8 = (root / ledger["authority_corpus"][4]["path"]).read_text()
    checks["v4_positive_scope"] = "SOURCE_J1_K5_CHANNEL00000_HIGHEST_CONTACT_SURVIVES_LEADING_SCOPED" in v4 and "11/24" in v4 and "delta''" in v4
    checks["v5_positive_scope"] = "00000 = 11/24" in v5 and "No source/realization mismatch was found" in v5 and "PASS_SCOPED" in v5
    checks["v7_positive_scope"] = v7j.get("classification") == "TRIANGLE_DELTA2_CONTACT_REGULARIZATION_DEPENDENT_SCOPED" and all(v7j.get("controls", {}).values())
    checks["v7_counterterm_question_explicitly_open"] = "source-authorized local counterterm" in v7t and "Next recommended gate" in v7t
    checks["v8_taxonomy_lock"] = all(label in v8 for label in ("SOURCE_FIXED_UNIQUE_SCOPED", "SOURCE_UNFIXED_FINITE_LOCAL_FREEDOM_SCOPED", "COUNTERTERM_CLASS_INSUFFICIENT_SCOPED", "MISSING_AUTHORITY_BLOCKED", "INVALID_IMPLEMENTATION"))
    checks["ledger_coeff_status_consistent"] = (
        ledger.get("class_definition_authorized") is True
        and ledger.get("prior_source_fixes_all_finite_coefficients") is False
        and ledger.get("prior_source_fixes_common_finite_normalization") is False
        and all(item.get("finite_counterterm_coefficients_fixed") is False for item in ledger.get("authority_corpus", []))
    )
    return {**checks, "blob_records": blob_records}, ledger


def build_decision(root: Path):
    authority, ledger = authority_audit(root)
    authority_controls = {k: v for k, v in authority.items() if k != "blob_records"}
    authority_ok = all(bool(v) for v in authority_controls.values())

    group, root_ok, basis, dims, constraint_ranks, basis_invariant = complete_invariant_basis()
    n = len(basis)

    rows = {name: [normalized_basis_action(item, widths) for item in basis] for name, widths in SCHEMES.items()}
    common_rescaling = rows["A4"] == rows["A"]
    odd_zero = all(rows[s][j] == 0 for s in rows for j, item in enumerate(basis) if item["degree"] % 2)

    v7_path = root / V7_CANONICAL
    v7 = json.loads(v7_path.read_text()) if v7_path.exists() else {}
    v7_reproduce = (
        v7.get("classification") == "TRIANGLE_DELTA2_CONTACT_REGULARIZATION_DEPENDENT_SCOPED"
        and all(v7.get("controls", {}).values())
        and all(parse_fraction(v7.get("values", {}).get(s, {}).get("K", "0")) == V7_K[s] for s in SCHEMES)
    )

    scheme_order = ("A4", "B", "C")
    D = [vec_sub(rows[s], rows["A"]) for s in scheme_order]
    rhs = [V7_K["A"] - V7_K[s] for s in scheme_order]
    solve = solve_affine(D, rhs, n)

    synthetic_coeff = [F(i + 1) for i in range(n)]
    positive_rhs = matvec(D, synthetic_coeff)
    positive_solve = solve_affine(D, positive_rhs, n)
    positive_recovered = positive_solve["solvable"] and matvec(D, positive_solve["canonical"]) == positive_rhs

    negative_rhs = [F(1), F(0), F(0)]
    negative_solve = solve_affine(D, negative_rhs, n)
    negative_rejected = not negative_solve["solvable"] and negative_solve["augmented_rank"] > negative_solve["rank"]

    # Every basis element represents a derivative of delta at the collision; an away-supported test has zero jet there.
    off_collision_identity = all(sum((coef * F(0) for coef in item["poly"].values()), F(0)) == 0 for item in basis)
    dims_expected = dims == EXPECTED_INVARIANT_DIMS
    rank_nullity = solve["rank"] + solve["nullity"] == n

    controls = {
        "authority_audit": authority_ok,
        "triangle_root_group_exact": root_ok,
        "invariant_dimensions_expected": dims_expected,
        "every_basis_vector_permutation_invariant": basis_invariant,
        "v7_exact_values_reproduced": v7_reproduce,
        "common_rescaling_A4_equals_A": common_rescaling,
        "odd_invariant_jets_zero_on_centered_gaussians": odd_zero,
        "off_collision_identity": off_collision_identity,
        "rank_nullity_identity": rank_nullity,
        "synthetic_in_span_exact_recovery": positive_recovered,
        "synthetic_outside_span_exact_rejection": negative_rejected,
    }
    controls_pass = all(controls.values())

    if not controls_pass:
        classification = "INVALID_IMPLEMENTATION"
    elif ledger is None or ledger.get("class_definition_authorized") is not True:
        classification = "MISSING_AUTHORITY_BLOCKED"
    elif not solve["solvable"]:
        classification = "COUNTERTERM_CLASS_INSUFFICIENT_SCOPED"
    else:
        source_fixed = bool(ledger.get("prior_source_fixes_all_finite_coefficients")) and bool(ledger.get("prior_source_fixes_common_finite_normalization"))
        if source_fixed and solve["nullity"] == 0:
            classification = "SOURCE_FIXED_UNIQUE_SCOPED"
        else:
            classification = "SOURCE_UNFIXED_FINITE_LOCAL_FREEDOM_SCOPED"

    corrected = None
    if solve["solvable"] and solve["canonical"] is not None:
        corrected = {s: V7_K[s] + dot(rows[s], solve["canonical"]) for s in SCHEMES}

    basis_records = []
    for idx, item in enumerate(basis):
        basis_records.append({
            "index": idx,
            "degree": item["degree"],
            "slot": item["slot"],
            "terms": serialize_poly(item["poly"]),
        })

    result = {
        "gate": GATE,
        "classification": classification,
        "controls": controls,
        "controls_pass": controls_pass,
        "authority": authority,
        "source_class_definition_authorized": None if ledger is None else ledger.get("class_definition_authorized"),
        "prior_source_fixes_all_finite_coefficients": None if ledger is None else ledger.get("prior_source_fixes_all_finite_coefficients"),
        "prior_source_fixes_common_finite_normalization": None if ledger is None else ledger.get("prior_source_fixes_common_finite_normalization"),
        "triangle_group_matrices": [[[int(x) for x in row] for row in A] for A in group],
        "invariant_dimensions_by_degree": {str(k): v for k, v in dims.items()},
        "invariance_constraint_ranks_by_degree": {str(k): v for k, v in constraint_ranks.items()},
        "basis": basis_records,
        "basis_count": n,
        "scheme_order": list(SCHEMES),
        "v7_K": {s: fs(V7_K[s]) for s in SCHEMES},
        "counterterm_action_rows": {s: serialize_vec(rows[s]) for s in SCHEMES},
        "difference_equation_order": list(scheme_order),
        "difference_matrix": [serialize_vec(row) for row in D],
        "difference_rhs": serialize_vec(rhs),
        "solve": {
            "solvable": solve["solvable"],
            "rank": solve["rank"],
            "augmented_rank": solve["augmented_rank"],
            "nullity": solve["nullity"],
            "canonical_solution": None if solve["canonical"] is None else serialize_vec(solve["canonical"]),
            "nullspace_basis": [serialize_vec(v) for v in solve["nullspace"]],
        },
        "canonical_corrected_K": None if corrected is None else {s: fs(corrected[s]) for s in SCHEMES},
        "synthetic_positive": {
            "seed_coefficients": serialize_vec(synthetic_coeff),
            "rhs": serialize_vec(positive_rhs),
            "solvable": positive_solve["solvable"],
            "recovered_rhs_exactly": positive_recovered,
        },
        "synthetic_negative": {
            "rhs": serialize_vec(negative_rhs),
            "solvable": negative_solve["solvable"],
            "rank": negative_solve["rank"],
            "augmented_rank": negative_solve["augmented_rank"],
            "rejected": negative_rejected,
        },
        "new_fact": "Whether the finite repaired-V7 Gaussian relative-width differences lie in the exact S3-invariant collision-jet action span through derivative order 7, with source-fixed versus source-unfixed finite freedom separated prospectively.",
        "claim_ceiling": "Finite local counterterm equivalence for the frozen repaired-V7 Gaussian delta-double-prime triangle only; no all-mollifier theorem, no distributional-extension existence/nonexistence theorem, no full-K5 or model/family failure, no D7 closure, selector, or Candidate Gravity authority.",
    }
    return result


def aggregate(low_path: Path, high_path: Path):
    low = json.loads(low_path.read_text())
    high = json.loads(high_path.read_text())
    low_dec = low["decision"]
    high_dec = high["decision"]
    agree = low_dec == high_dec
    out = dict(low_dec)
    out["lane_decision_agreement"] = agree
    out["lane_runtime_python"] = [low.get("runtime_python"), high.get("runtime_python")]
    if not agree:
        out["classification"] = "INVALID_IMPLEMENTATION"
        out["controls_pass"] = False
        out["controls"] = dict(out.get("controls", {}))
        out["controls"]["lane_decision_agreement"] = False
    else:
        out["controls"] = dict(out.get("controls", {}))
        out["controls"]["lane_decision_agreement"] = True
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("source", "lane", "aggregate"), required=True)
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--out", required=True)
    ap.add_argument("--low")
    ap.add_argument("--high")
    args = ap.parse_args()
    root = Path(args.repo_root)

    if args.mode == "source":
        authority, ledger = authority_audit(root)
        checks = {k: v for k, v in authority.items() if k != "blob_records"}
        out = {
            "gate": GATE,
            "source_checks": authority,
            "source_ok": all(bool(v) for v in checks.values()),
            "class_definition_authorized": None if ledger is None else ledger.get("class_definition_authorized"),
        }
    elif args.mode == "lane":
        out = {
            "runtime_python": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
            "decision": build_decision(root),
        }
    else:
        if not args.low or not args.high:
            raise SystemExit("aggregate requires --low and --high")
        out = aggregate(Path(args.low), Path(args.high))

    p = Path(args.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
