#!/usr/bin/env python3
"""Exact K5 scalar collision-strata power-counting certificate."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from itertools import permutations
import json
from math import comb
from pathlib import Path

VERTICES = (1, 2, 3, 4, 5)
TOTAL_EDGES = 10
EDGE_SCALING_DEGREE = 3
EXPECTED_MULTIPLICITIES = {
    "2+1+1+1": 10,
    "2+2+1": 15,
    "3+1+1": 10,
    "3+2": 10,
    "4+1": 5,
    "5": 1,
}


def set_partitions(seq):
    if not seq:
        yield []
        return
    first, *rest = seq
    for p in set_partitions(rest):
        yield [[first]] + [block[:] for block in p]
        for i in range(len(p)):
            q = [block[:] for block in p]
            q[i] = [first] + q[i]
            yield q


def canonical(partition):
    blocks = [tuple(sorted(block)) for block in partition]
    return tuple(sorted(blocks, key=lambda b: (b[0], len(b), b)))


def partition_type(partition):
    return "+".join(str(s) for s in sorted((len(b) for b in partition), reverse=True))


def record(partition, edge_sd=EDGE_SCALING_DEGREE, dimension_multiplier=1):
    sizes = sorted((len(b) for b in partition), reverse=True)
    internal = sum(comb(s, 2) for s in sizes)
    cross = TOTAL_EDGES - internal
    scalar_normal = sum(s - 1 for s in sizes)
    d_perp = dimension_multiplier * scalar_normal
    omega = edge_sd * internal - d_perp
    return {
        "partition": [list(b) for b in partition],
        "type": "+".join(map(str, sizes)),
        "block_sizes": sizes,
        "internal_edges": internal,
        "cross_edges": cross,
        "scalar_normal_dimension": scalar_normal,
        "dimension_multiplier": dimension_multiplier,
        "d_perp": d_perp,
        "edge_scaling_degree": edge_sd,
        "omega": omega,
        "proper_collision": len(partition) > 1 and len(partition) < 5,
        "full_collision": len(partition) == 1,
    }


def relabel(partition, perm):
    mapping = dict(zip(VERTICES, perm))
    return canonical([[mapping[v] for v in block] for block in partition])


def type_omega_multiset(records):
    return Counter((r["type"], r["omega"]) for r in records)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    all_parts = sorted({canonical(p) for p in set_partitions(list(VERTICES))})
    collision_parts = [p for p in all_parts if len(p) < 5]
    records = [record(p) for p in collision_parts]
    proper = [r for r in records if r["proper_collision"]]
    full = [r for r in records if r["full_collision"]]

    grouped = defaultdict(list)
    for r in records:
        grouped[r["type"]].append(r)

    type_table = {}
    same_type_invariant = True
    for t, rs in sorted(grouped.items()):
        triples = {(r["internal_edges"], r["d_perp"], r["omega"]) for r in rs}
        same_type_invariant &= len(triples) == 1
        e, d, w = next(iter(triples))
        type_table[t] = {
            "multiplicity": len(rs),
            "internal_edges": e,
            "d_perp": d,
            "omega": w,
            "all_superficially_divergent": all(r["omega"] >= 0 for r in rs),
        }

    multiplicities = {t: len(rs) for t, rs in grouped.items()}

    # Label-permutation adversarial control: the exact multiset must be invariant for all 120 S5 permutations.
    base_multiset = type_omega_multiset(records)
    permutation_invariance = True
    for perm in permutations(VERTICES):
        relabeled = sorted({relabel(p, perm) for p in collision_parts})
        relabeled_records = [record(p) for p in relabeled]
        if type_omega_multiset(relabeled_records) != base_multiset:
            permutation_invariance = False
            break

    # Explicitly demonstrate that the historical 3D dimension formula is not the scalar table.
    table_3d = {}
    table_sd1 = {}
    for t, rs in sorted(grouped.items()):
        exemplar = canonical(rs[0]["partition"])
        r3 = record(exemplar, edge_sd=3, dimension_multiplier=3)
        r1 = record(exemplar, edge_sd=1, dimension_multiplier=1)
        table_3d[t] = {"d_perp": r3["d_perp"], "omega": r3["omega"]}
        table_sd1[t] = {"d_perp": r1["d_perp"], "omega": r1["omega"]}

    scalar_vs_3d_diff = any(
        type_table[t]["d_perp"] != table_3d[t]["d_perp"] or type_table[t]["omega"] != table_3d[t]["omega"]
        for t in type_table
    )
    sd1_changes = any(type_table[t]["omega"] != table_sd1[t]["omega"] for t in type_table if t != "5")

    checks = {
        "bell_total_52": len(all_parts) == 52,
        "collision_partitions_51": len(collision_parts) == 51,
        "six_collision_types": len(grouped) == 6,
        "type_multiplicities": multiplicities == EXPECTED_MULTIPLICITIES,
        "edge_identity": all(r["internal_edges"] + r["cross_edges"] == TOTAL_EDGES for r in records),
        "scalar_dimension_identity": all(r["d_perp"] == 5 - len(r["partition"]) for r in records),
        "block_contribution_identity": all(
            r["internal_edges"] == sum(comb(s, 2) for s in r["block_sizes"])
            and r["d_perp"] == sum(s - 1 for s in r["block_sizes"])
            for r in records
        ),
        "full_collision_parent_count": len(full) == 1 and full[0]["internal_edges"] == 10 and full[0]["d_perp"] == 4 and full[0]["omega"] == 26,
        "same_type_invariant": same_type_invariant,
        "all_120_label_permutations_invariant": permutation_invariance,
        "scalar_formula_differs_from_3d_control": scalar_vs_3d_diff,
        "edge_sd1_control_changes_omega": sd1_changes,
    }
    controls_pass = all(checks.values())

    proper_divergent = [r for r in proper if r["omega"] >= 0]
    proper_convergent = [r for r in proper if r["omega"] < 0]
    all_proper_divergent = len(proper) > 0 and len(proper_divergent) == len(proper)

    if not controls_pass:
        classification = "INVALID_IMPLEMENTATION"
    elif proper_divergent:
        classification = "AUX_GAUSSIAN_K5_PROPER_COLLISION_SUBDIVERGENCES_PRESENT_SCOPED"
    elif len(proper_convergent) == len(proper):
        classification = "AUX_GAUSSIAN_K5_NO_PROPER_COLLISION_SUBDIVERGENCE_BY_FROZEN_COUNT_SCOPED"
    else:
        classification = "SCIENTIFIC_FAIL_GAUSSIAN_SCALAR_COLLISION_STRATA_POWER_COUNTING"

    result = {
        "gate": "SOURCE_J1_K5_GAUSSIAN_SCALAR_COLLISION_STRATA_POWER_COUNTING_GATE",
        "classification": classification,
        "controls_pass": controls_pass,
        "checks": checks,
        "bell_total": len(all_parts),
        "collision_partition_count": len(collision_parts),
        "proper_collision_partition_count": len(proper),
        "type_multiplicities": multiplicities,
        "scalar_type_table": type_table,
        "synthetic_3d_type_table": table_3d,
        "synthetic_sd1_type_table": table_sd1,
        "proper_superficially_divergent_count": len(proper_divergent),
        "proper_superficially_convergent_count": len(proper_convergent),
        "all_proper_collision_strata_superficially_divergent": all_proper_divergent,
        "proper_omega_values": sorted({r["omega"] for r in proper}),
        "records": records,
        "claim_ceiling": "Exact scalar uniform power counting only: a nonnegative omega authorizes stratum/forest extension analysis but is not by itself a proof of a renormalized extension, Eq4 failure, model failure, or D7 closure.",
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "classification": classification,
        "controls_pass": controls_pass,
        "type_table": type_table,
        "proper_count": len(proper),
        "proper_divergent_count": len(proper_divergent),
        "all_proper_divergent": all_proper_divergent,
        "proper_omega_values": result["proper_omega_values"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
