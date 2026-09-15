#!/usr/bin/env python3
"""Exact same-realization repair for scalar K5 laminar-forest metadata."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, permutations
import hashlib
import json
from pathlib import Path

V = frozenset(range(5))
PERMS = tuple(permutations(range(5)))


def subset_key(s):
    return (len(s), tuple(sorted(s)))


def canon_subset(s):
    return tuple(sorted(s))


def canon_forest(forest):
    return tuple(sorted((canon_subset(s) for s in forest), key=lambda x: (len(x), x)))


def compatible(a, b):
    return a <= b or b <= a or a.isdisjoint(b)


def enumerate_forests(candidates):
    candidates = tuple(sorted(candidates, key=subset_key))
    out = []

    def rec(prefix, tail):
        out.append(tuple(prefix))
        for i, s in enumerate(tail):
            nxt = tuple(t for t in tail[i + 1 :] if compatible(s, t))
            rec(prefix + (s,), nxt)

    rec(tuple(), candidates)
    return tuple(out)


def permute_forest(forest, p):
    return canon_forest(frozenset(p[i] for i in s) for s in forest)


def orbit_key(forest):
    return min(permute_forest(forest, p) for p in PERMS)


def orbit_sizes(forests):
    d = Counter(orbit_key(f) for f in forests)
    return Counter(d.values()), len(d)


def omega_scalar(k):
    e_int = k * (k - 1) // 2
    d_perp = k - 1
    return 3 * e_int - d_perp


def omega_three_normal(k):
    e_int = k * (k - 1) // 2
    d_perp = 3 * (k - 1)
    return 3 * e_int - d_perp


def digest_records(records):
    raw = json.dumps(records, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="source_j1_k5_scalar_laminar_forest_order_repair.json")
    args = ap.parse_args()

    subsets = tuple(
        frozenset(c)
        for k in range(2, 6)
        for c in combinations(range(5), k)
    )
    proper = tuple(s for s in subsets if s != V)

    all_forests = enumerate_forests(subsets)
    proper_forests = enumerate_forests(proper)

    subset_census = Counter(len(s) for s in subsets)
    all_hist = Counter(len(f) for f in all_forests)
    proper_hist = Counter(len(f) for f in proper_forests)

    all_orbit_hist, all_orbits = orbit_sizes(all_forests)
    proper_orbit_hist, proper_orbits = orbit_sizes(proper_forests)

    scalar_orders = {k: omega_scalar(k) for k in range(2, 6)}
    old_three_normal_orders = {k: omega_three_normal(k) for k in range(2, 6)}

    proper_keys = {canon_forest(f) for f in proper_forests}
    with_v_keys = {canon_forest(f) for f in all_forests if V in f}
    added_v_keys = {canon_forest(tuple(f) + (V,)) for f in proper_forests}

    relabel_ok = True
    scalar_order_invariant = True
    for f in proper_forests:
        for p in PERMS:
            pf = tuple(frozenset(p[i] for i in s) for s in f)
            if not all(compatible(a, b) for i, a in enumerate(pf) for b in pf[i + 1 :]):
                relabel_ok = False
                break
        if not relabel_ok:
            break

    for s in subsets:
        target = omega_scalar(len(s))
        for p in PERMS:
            ps = frozenset(p[i] for i in s)
            if omega_scalar(len(ps)) != target:
                scalar_order_invariant = False
                break
        if not scalar_order_invariant:
            break

    controls = {
        "subset_census": dict(sorted(subset_census.items())) == {2: 10, 3: 10, 4: 5, 5: 1},
        "historical_all_forest_count": len(all_forests) == 472,
        "historical_all_histogram": dict(sorted(all_hist.items())) == {0: 1, 1: 26, 2: 130, 3: 210, 4: 105},
        "proper_only_enumerated": len(proper_forests) == 236,
        "proper_only_histogram": dict(sorted(proper_hist.items())) == {0: 1, 1: 25, 2: 105, 3: 105},
        "full_set_bijection": with_v_keys == added_v_keys and len(with_v_keys) == len(proper_keys),
        "all_s5_orbit_count": all_orbits == 24,
        "proper_s5_orbit_count": proper_orbits == 12,
        "relabel_invariance": relabel_ok,
        "scalar_order_relabel_invariance": scalar_order_invariant,
        "full_collision_order_26": scalar_orders[5] == 26,
        "scalar_order_table": scalar_orders == {2: 2, 3: 7, 4: 15, 5: 26},
        "three_normal_negative_control": old_three_normal_orders == {2: 0, 3: 3, 4: 9, 5: 18} and old_three_normal_orders != scalar_orders,
        "overlap_rejected": not compatible(frozenset({0, 1}), frozenset({1, 2})),
        "disjoint_accepted": compatible(frozenset({0, 1}), frozenset({2, 3})),
        "proper_excludes_full_set": all(V not in f for f in proper_forests),
    }

    all_pass = all(controls.values())
    classification = (
        "SCALAR_K5_LAMINAR_FOREST_ORDER_REPAIR_CONFIRMED_SCOPED"
        if all_pass
        else "INVALID_IMPLEMENTATION"
    )

    all_records = [canon_forest(f) for f in all_forests]
    proper_records = [canon_forest(f) for f in proper_forests]

    out = {
        "classification": classification,
        "controls_pass": all_pass,
        "controls": controls,
        "scalar_realization": {
            "edge_scaling_degree": 3,
            "normal_dimension_per_relative_vertex": 1,
            "formula": "omega=3*C(k,2)-(k-1)",
            "subtraction_orders_by_subset_size": scalar_orders,
        },
        "negative_control_three_normal_realization": {
            "normal_dimension_per_relative_vertex": 3,
            "subtraction_orders_by_subset_size": old_three_normal_orders,
        },
        "subset_census": dict(sorted(subset_census.items())),
        "all_forest_count_including_empty": len(all_forests),
        "all_forest_cardinality_histogram": dict(sorted(all_hist.items())),
        "all_s5_orbit_count": all_orbits,
        "all_s5_orbit_size_histogram": dict(sorted(all_orbit_hist.items())),
        "proper_only_forest_count_including_empty": len(proper_forests),
        "proper_only_cardinality_histogram": dict(sorted(proper_hist.items())),
        "proper_only_s5_orbit_count": proper_orbits,
        "proper_only_s5_orbit_size_histogram": dict(sorted(proper_orbit_hist.items())),
        "all_forest_records_sha256": digest_records(all_records),
        "proper_only_forest_records_sha256": digest_records(proper_records),
        "claim_ceiling": "Exact scalar same-realization topology/order metadata only; does not execute forest subtraction and does not close D7.",
    }

    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
