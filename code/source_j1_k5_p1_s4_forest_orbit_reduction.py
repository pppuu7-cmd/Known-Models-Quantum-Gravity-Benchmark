#!/usr/bin/env python3
"""Exact P1 S4 orbit reduction certificate for proper scalar K5 forests."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
from itertools import combinations, permutations
import json
from pathlib import Path

V = frozenset(range(5))
EDGES = tuple(combinations(range(5), 2))
P1_EXPONENTS = (1, 1, 1, 1, 2, 2, 2, 2, 2, 2)
ORDERS = {2: 2, 3: 7, 4: 15}


def compatible(a, b):
    return a <= b or b <= a or a.isdisjoint(b)


def proper_subsets():
    return tuple(frozenset(c) for k in range(2, 5) for c in combinations(range(5), k))


def enumerate_forests(candidates):
    candidates = tuple(sorted(candidates, key=lambda s: (len(s), tuple(sorted(s)))))
    out = []

    def rec(prefix, tail):
        out.append(tuple(prefix))
        for i, s in enumerate(tail):
            nxt = tuple(t for t in tail[i + 1 :] if compatible(s, t))
            rec(prefix + (s,), nxt)

    rec(tuple(), candidates)
    return tuple(out)


def p1_group():
    out = []
    for perm4 in permutations((1, 2, 3, 4)):
        p = {0: 0}
        for old, new in zip((1, 2, 3, 4), perm4):
            p[old] = new
        out.append(p)
    return tuple(out)


def canon_forest(forest):
    return tuple(sorted((tuple(sorted(s)) for s in forest), key=lambda x: (len(x), x)))


def permute_forest(forest, p):
    return canon_forest(frozenset(p[v] for v in s) for s in forest)


def orbit_key(forest, group):
    return min(permute_forest(forest, p) for p in group)


def edge_exponent_map():
    return {frozenset(edge): exp for edge, exp in zip(EDGES, P1_EXPONENTS)}


def full_gauge_basis():
    rows = [[Fraction(0) for _ in range(4)] for _ in range(5)]
    for v in range(1, 5):
        rows[v][v - 1] = Fraction(1)
    return rows


def barycentric_collapse(s):
    s = frozenset(s)
    full = full_gauge_basis()
    out = [row[:] for row in full]
    avg = [sum(full[v][j] for v in s) / len(s) for j in range(4)]
    for v in s:
        out[v] = avg[:]
    return [[out[v][j] - out[0][j] for j in range(4)] for v in range(1, 5)]


def permutation_representation(p):
    full = full_gauge_basis()
    new = [[Fraction(0) for _ in range(4)] for _ in range(5)]
    for old in range(5):
        new[p[old]] = full[old][:]
    return [[new[v][j] - new[0][j] for j in range(4)] for v in range(1, 5)]


def mm(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def invariant_fixture(forest):
    # Depends only on S4 invariants: subset size and whether the fixed vertex 0 is present.
    return 1 + sum(10 * len(s) + int(0 in s) for s in forest)


def noninvariant_fixture(forest):
    # Deliberately distinguishes nonzero vertex 1, so representative weighting is unsafe.
    return sum(int(1 in s) for s in forest)


def jet_box_work(forest):
    work = 1
    for s in forest:
        work *= ORDERS[len(s)] + 1
    return work


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="source_j1_k5_p1_s4_forest_orbit_reduction.json")
    args = ap.parse_args()

    proper = proper_subsets()
    forests = enumerate_forests(proper)
    group = p1_group()
    exp_map = edge_exponent_map()

    p1_map_ok = tuple((edge, exp_map[frozenset(edge)]) for edge in EDGES) == tuple(zip(EDGES, P1_EXPONENTS))
    star_pattern_ok = all(exp_map[frozenset({0, v})] == 1 for v in range(1, 5)) and all(
        exp_map[frozenset({a, b})] == 2 for a, b in combinations(range(1, 5), 2)
    )

    exponent_invariant = True
    for p in group:
        for edge, exponent in exp_map.items():
            pe = frozenset(p[v] for v in edge)
            if exp_map[pe] != exponent:
                exponent_invariant = False
                break
        if not exponent_invariant:
            break

    operator_covariant = True
    for p in group:
        rp = permutation_representation(p)
        for s in proper:
            ps = frozenset(p[v] for v in s)
            if mm(rp, barycentric_collapse(s)) != mm(barycentric_collapse(ps), rp):
                operator_covariant = False
                break
            if ORDERS[len(s)] != ORDERS[len(ps)]:
                operator_covariant = False
                break
        if not operator_covariant:
            break

    orbit_members = defaultdict(list)
    for f in forests:
        orbit_members[orbit_key(f, group)].append(f)

    sign_constant = True
    for members in orbit_members.values():
        signs = {(-1) ** len(f) for f in members}
        if len(signs) != 1:
            sign_constant = False
            break

    full_invariant_sum = sum(((-1) ** len(f)) * invariant_fixture(f) for f in forests)
    orbit_invariant_sum = sum(
        len(members) * ((-1) ** len(members[0])) * invariant_fixture(members[0])
        for members in orbit_members.values()
    )

    full_bad_sum = sum(((-1) ** len(f)) * noninvariant_fixture(f) for f in forests)
    orbit_bad_sum = sum(
        len(members) * ((-1) ** len(members[0])) * noninvariant_fixture(members[0])
        for members in orbit_members.values()
    )

    orbit_size_hist = Counter(len(members) for members in orbit_members.values())
    full_work = sum(jet_box_work(f) for f in forests)
    representative_work = sum(jet_box_work(members[0]) for members in orbit_members.values())

    representative_records = []
    for key in sorted(orbit_members, key=lambda x: (len(x), x)):
        members = orbit_members[key]
        representative_records.append(
            {
                "representative": [list(s) for s in key],
                "orbit_size": len(members),
                "forest_cardinality": len(members[0]),
                "sign": (-1) ** len(members[0]),
                "jet_box_work": jet_box_work(members[0]),
            }
        )
    rep_bytes = json.dumps(representative_records, sort_keys=True, separators=(",", ":")).encode()
    representative_digest = hashlib.sha256(rep_bytes).hexdigest()

    controls = {
        "edge_order_and_p1_map": p1_map_ok,
        "star_vs_internal_pattern": star_pattern_ok,
        "p1_exponent_invariant_under_s4": exponent_invariant,
        "group_size_24": len(group) == 24,
        "proper_forest_count_236": len(forests) == 236,
        "operator_and_order_covariance": operator_covariant,
        "orbit_partition_complete": sum(len(v) for v in orbit_members.values()) == len(forests),
        "forest_sign_constant_on_orbits": sign_constant,
        "invariant_fixture_full_equals_orbit_sum": full_invariant_sum == orbit_invariant_sum,
        "noninvariant_fixture_detected": full_bad_sum != orbit_bad_sum,
        "orbit_count_29": len(orbit_members) == 29,
        "orbit_size_histogram": dict(sorted(orbit_size_hist.items())) == {1: 2, 3: 2, 4: 6, 6: 6, 12: 12, 24: 1},
        "workload_reduced": representative_work < full_work,
    }
    controls_pass = all(controls.values())
    classification = (
        "P1_S4_FOREST_ORBIT_REDUCTION_CONFIRMED_SCOPED"
        if controls_pass
        else "INVALID_IMPLEMENTATION"
    )

    out = {
        "classification": classification,
        "controls_pass": controls_pass,
        "controls": controls,
        "p1_edge_order": [list(e) for e in EDGES],
        "p1_exponents": list(P1_EXPONENTS),
        "p1_group_size": len(group),
        "proper_forest_count": len(forests),
        "p1_orbit_count": len(orbit_members),
        "p1_orbit_size_histogram": dict(sorted(orbit_size_hist.items())),
        "representative_digest_sha256": representative_digest,
        "representative_records": representative_records,
        "invariant_fixture_full_sum": full_invariant_sum,
        "invariant_fixture_orbit_sum": orbit_invariant_sum,
        "adversarial_noninvariant_full_sum": full_bad_sum,
        "adversarial_noninvariant_orbit_sum": orbit_bad_sum,
        "full_structural_jet_box_work": full_work,
        "orbit_representative_structural_jet_box_work": representative_work,
        "exact_work_reduction_ratio_numerator": full_work,
        "exact_work_reduction_ratio_denominator": representative_work,
        "claim_ceiling": "Exact P1 computational symmetry reduction only; no forest-subtracted convergence/divergence or physical conclusion.",
    }

    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "representative_records"}, sort_keys=True))


if __name__ == "__main__":
    main()
