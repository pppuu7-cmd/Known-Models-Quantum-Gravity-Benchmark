#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from fractions import Fraction
from pathlib import Path

EXPECTED = {
    "sources/arxiv_2601_23162v1_eq4_local_collision_map_expansion_v13.json": ("fdfb13f9974ebc891cb3f490ca553dd0991d9136", "cc533af3c84de8c0de57523a795ba4357523712f1746ce55fa78eb521cd51713"),
    "sources/arxiv_2604_24945v1_eq4_local_collision_map_expansion_v13.json": ("c742e8cab0648b8fbaef88f09876644c6c2c3077", "f37659f5cb4674dd0c1b81a6e55f5d1dfd992c60b0e85cb2859322b860e22046"),
}


def rank2(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    rank = 0
    col = 0
    while rank < len(a) and col < 2:
        pivot = next((i for i in range(rank, len(a)) if a[i][col] != 0), None)
        if pivot is None:
            col += 1
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        p = a[rank][col]
        a[rank] = [x / p for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col] != 0:
                f = a[i][col]
                a[i] = [x - f*y for x, y in zip(a[i], a[rank])]
        rank += 1
        col += 1
    return rank


def fixture_class(rows=None, common=True, maps=True, lift=True, norm=True, s3=True):
    if not (common and maps and lift):
        return "BLOCKED", None
    r = rank2(rows or [])
    if r != 2:
        return "FAIL", r
    if not (norm and s3):
        return "BLOCKED", r
    return "PASS", r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--authority", required=True)
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    root = Path(args.repo_root)
    authority = json.loads(Path(args.authority).read_text())

    source_identity = True
    source_facts = {}
    for path, (blob, pdf) in EXPECTED.items():
        actual = subprocess.check_output(["git", "hash-object", path], cwd=root, text=True).strip()
        rec = json.loads((root / path).read_text())
        source_identity &= actual == blob and rec.get("pdf_sha256") == pdf
        source_facts[path] = {
            "blob_sha": actual,
            "pdf_sha256": rec.get("pdf_sha256"),
            "candidate_passages": len(rec.get("candidate_passages", [])),
        }

    prims = [s["authorized_primitives"] for s in authority["source_records"]]
    common = any(p.get("common_gauge_fixed_group_tuple") is True for p in prims)
    maps_obj = next((p.get("three_wedge_group_argument_maps") for p in prims if p.get("three_wedge_group_argument_maps") is not None), None)
    lift_obj = next((p.get("common_local_group_lie_lift") for p in prims if p.get("common_local_group_lie_lift") is not None), None)
    quotient_obj = next((p.get("two_dimensional_transverse_quotient") for p in prims if p.get("two_dimensional_transverse_quotient") is not None), None)
    norm_obj = next((p.get("jacobian_haar_contact_normalization_transport") for p in prims if p.get("jacobian_haar_contact_normalization_transport") is not None), None)
    s3_obj = next((p.get("s3_orientation_coordinate_transport") for p in prims if p.get("s3_orientation_coordinate_transport") is not None), None)

    maps = maps_obj is not None
    lift = lift_obj is not None
    norm = norm_obj is not None
    s3 = s3_obj is not None
    rank = None
    if maps and lift and isinstance(maps_obj, list):
        rank = rank2(maps_obj)

    missing = []
    if not common:
        missing.append("COMMON_GAUGE_FIXED_GROUP_TUPLE")
    if not maps:
        missing.append("THREE_WEDGE_GROUP_ARGUMENT_MAPS")
    if not lift:
        missing.append("COMMON_LOCAL_GROUP_LIE_LIFT")
    if rank is None or quotient_obj is None:
        missing.append("TWO_DIMENSIONAL_TRANSVERSE_QUOTIENT")
    if not norm:
        missing.append("JACOBIAN_HAAR_CONTACT_NORMALIZATION_TRANSPORT")
    if not s3:
        missing.append("S3_ORIENTATION_COORDINATE_TRANSPORT")

    pos, pos_rank = fixture_class([[1,0],[0,1],[1,1]])
    basis, basis_rank = fixture_class([[1,1],[1,-1],[2,0]])
    orient, orient_rank = fixture_class([[-1,0],[0,1],[-1,1]])
    missing_maps, missing_maps_rank = fixture_class(None, common=True, maps=False, lift=False)
    rank_fail, rank_fail_rank = fixture_class([[1,0],[2,0],[3,0]])
    missing_transport, missing_transport_rank = fixture_class([[1,0],[0,1],[1,1]], norm=False)

    controls = {
        "source_identity": source_identity,
        "parent_terminal_commit_locked": authority.get("parent_terminal_commit") == "5f9ec01076d6867e3eeadfa285d235159c7ae24b",
        "bridge_target_not_source_authority": authority["bridge_target_only"]["authority"] == "TARGET_ONLY_NOT_SOURCE_PREMISE",
        "positive_rank2_shared_lift": pos == "PASS" and pos_rank == 2,
        "positive_basis_change_invariance": basis == "PASS" and basis_rank == 2,
        "positive_orientation_sign_invariance": orient == "PASS" and orient_rank == 2,
        "negative_missing_wedge_maps_blocked": missing_maps == "BLOCKED" and missing_maps_rank is None,
        "negative_rank_deficient_fail": rank_fail == "FAIL" and rank_fail_rank == 1,
        "negative_missing_transport_blocked": missing_transport == "BLOCKED" and missing_transport_rank == 2,
    }

    if not all(controls.values()):
        classification = "INVALID_IMPLEMENTATION"
    elif missing:
        classification = "EQ4_TRIPLE_CONTACT_COMMON_GROUP_VARIABLE_LIFT_BLOCKED_SCOPED"
    elif rank != 2:
        classification = "EQ4_TRIPLE_CONTACT_COMMON_GROUP_VARIABLE_LIFT_RANK_FAIL_SCOPED"
    else:
        classification = "EQ4_TRIPLE_CONTACT_COMMON_GROUP_VARIABLE_LIFT_DERIVED_SCOPED"

    decision = {
        "gate": authority["gate"],
        "classification": classification,
        "target_triangle": authority["target_triangle"],
        "required_fields": authority["required_fields"],
        "missing_fields": missing,
        "common_gauge_fixed_group_tuple_present": common,
        "three_wedge_group_argument_maps_present": maps,
        "common_local_group_lie_lift_present": lift,
        "transverse_rank": rank,
        "jacobian_haar_contact_normalization_transport_present": norm,
        "s3_orientation_coordinate_transport_present": s3,
        "controls": controls,
        "source_facts": source_facts,
        "claim_ceiling": authority["interpretation_ceiling"],
    }
    canonical = json.dumps(decision, sort_keys=True, separators=(",", ":"))
    decision["decision_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(decision, indent=2, sort_keys=True) + "\n")
    print(json.dumps(decision, sort_keys=True))

if __name__ == "__main__":
    main()
