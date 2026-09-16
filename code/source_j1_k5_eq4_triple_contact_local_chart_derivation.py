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
    rows = [[Fraction(x) for x in r] for r in rows]
    rank = 0
    col = 0
    while rank < len(rows) and col < 2:
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if pivot is None:
            col += 1; continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        p = rows[rank][col]
        rows[rank] = [x/p for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col]:
                f = rows[i][col]
                rows[i] = [a-f*b for a,b in zip(rows[i], rows[rank])]
        rank += 1; col += 1
    return rank

def fixture_class(rows, common=True, norm=True, s3=True):
    if not common: return "BLOCKED"
    r = rank2(rows)
    if r < 2: return "FAIL"
    if not (norm and s3): return "BLOCKED"
    return "PASS"

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--authority', required=True); ap.add_argument('--repo-root', default='.'); ap.add_argument('--out', required=True); a=ap.parse_args()
    root=Path(a.repo_root); authority=json.loads(Path(a.authority).read_text())
    source_identity=True; source_facts={}
    for path,(blob,pdf) in EXPECTED.items():
        actual=subprocess.check_output(['git','hash-object',path], cwd=root, text=True).strip()
        rec=json.loads((root/path).read_text())
        source_identity &= actual == blob and rec.get('pdf_sha256') == pdf
        source_facts[path] = {"blob_sha":actual,"pdf_sha256":rec.get('pdf_sha256'),"candidate_passages":len(rec.get('candidate_passages',[]))}
    bridge_ok=authority['bridge_target_only']['authority']=='TARGET_ONLY_NOT_SOURCE_PREMISE'
    prims=[]
    for s in authority['source_records']:
        prims.append(s['authorized_primitives'])
    common = any(p.get('common_triangle_local_coordinates') is not None for p in prims)
    maps = any(p.get('three_contact_maps_on_common_coordinates') is not None for p in prims)
    norm = any(p.get('triangle_jacobian_normalization_transport') is not None for p in prims)
    s3 = any(p.get('s3_local_coordinate_transport') is not None for p in prims)
    rank = None
    if common and maps:
        # Production may only supply rows through explicit frozen source primitives. No fallback to V8 target.
        rows = next((p.get('three_contact_maps_on_common_coordinates') for p in prims if isinstance(p.get('three_contact_maps_on_common_coordinates'), list)), None)
        if rows is not None: rank=rank2(rows)
    missing=[]
    if not common: missing.append('COMMON_LOCAL_COORDINATES')
    if not maps: missing.append('THREE_CONTACT_MAPS')
    if rank is None: missing.append('RANK_TRANSVERSALITY')
    if not norm: missing.append('JACOBIAN_NORMALIZATION_TRANSPORT')
    if not s3: missing.append('S3_COORDINATE_TRANSPORT')
    controls={
      'source_identity':source_identity,
      'bridge_target_not_source_authority':bridge_ok,
      'positive_shared_chart': fixture_class([[1,0],[0,1],[1,1]])=='PASS',
      'positive_invertible_basis_change': fixture_class([[1,1],[1,-1],[2,0]])=='PASS',
      'negative_disjoint_missing_joint_map': fixture_class([],common=False)=='BLOCKED',
      'negative_rank_deficient': fixture_class([[1,0],[2,0],[3,0]])=='FAIL',
      'negative_missing_transport': fixture_class([[1,0],[0,1],[1,1]],norm=False)=='BLOCKED'
    }
    if not all(controls.values()): classification='INVALID_IMPLEMENTATION'
    elif missing: classification='EQ4_TRIPLE_CONTACT_LOCAL_CHART_DERIVATION_BLOCKED_SCOPED'
    elif rank is not None and rank < 2: classification='EQ4_TRIPLE_CONTACT_LOCAL_CHART_TRANSVERSALITY_FAIL_SCOPED'
    else: classification='EQ4_TRIPLE_CONTACT_LOCAL_CHART_DERIVED_SCOPED'
    decision={
      'gate':authority['gate'],'classification':classification,'target_triangle':authority['target_triangle'],
      'required_fields':authority['required_fields'],'missing_fields':missing,'common_coordinates_present':common,
      'three_contact_maps_present':maps,'contact_differential_rank':rank,'jacobian_normalization_transport_present':norm,
      's3_coordinate_transport_present':s3,'controls':controls,'source_facts':source_facts,
      'claim_ceiling':authority['interpretation_ceiling']
    }
    canonical=json.dumps(decision,sort_keys=True,separators=(',',':'))
    decision['decision_sha256']=hashlib.sha256(canonical.encode()).hexdigest()
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(decision,indent=2,sort_keys=True)+'\n')
    print(json.dumps(decision,sort_keys=True))
if __name__=='__main__': main()
