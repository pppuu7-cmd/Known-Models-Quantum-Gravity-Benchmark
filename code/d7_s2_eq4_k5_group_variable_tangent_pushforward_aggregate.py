#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

INVALID="D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_INVALID"
TERMINAL={
  "D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_PASS_SCOPED",
  "D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_FAIL_SCOPED",
  "D7_S2_EQ4_K5_GROUP_VARIABLE_TANGENT_PUSHFORWARD_BLOCKED_SCOPED",
}


def load(root):
    fs=sorted(Path(root).rglob('*.json'))
    if len(fs)!=1: raise SystemExit(f'expected one json in {root}, got {len(fs)}')
    return json.loads(fs[0].read_text()), hashlib.sha256(fs[0].read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--rref',required=True);ap.add_argument('--trees',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
    r,hr=load(a.rref);t,ht=load(a.trees)
    methods_ok=(r.get('method')=='rref' and t.get('method')=='trees')
    payload_agree=(r.get('scientific_payload_sha256')==t.get('scientific_payload_sha256'))
    cls=r.get('classification') if methods_ok and payload_agree and r.get('classification')==t.get('classification') and r.get('classification') in TERMINAL else INVALID
    out={
      'gate':r.get('gate'),'classification':cls,'independent_methods_agree':methods_ok and payload_agree,
      'rref_json_sha256':hr,'trees_json_sha256':ht,'scientific_payload_sha256':r.get('scientific_payload_sha256') if payload_agree else None,
      'root_ranks':r.get('root_ranks'),'full_real_domain_dimension':r.get('full_real_domain_dimension'),'full_real_codomain_dimension':r.get('full_real_codomain_dimension'),'full_real_rank':r.get('full_real_rank'),'full_real_domain_nullity':r.get('full_real_domain_nullity'),'full_real_edge_left_nullity':r.get('full_real_edge_left_nullity'),
      'spanning_tree_count':r.get('spanning_tree_count'),'all_spanning_tree_minors_unimodular':r.get('all_spanning_tree_minors_unimodular'),'spanning_tree_minor_determinant_values':r.get('spanning_tree_minor_determinant_values'),
      'fundamental_cycle_basis_count':r.get('fundamental_cycle_basis_count'),'fundamental_cycle_rank_all_roots':r.get('fundamental_cycle_rank_all_roots'),'fundamental_cycle_annihilates_tangent_map_all_roots':r.get('fundamental_cycle_annihilates_tangent_map_all_roots'),
      'root_changes_unimodular':r.get('root_changes_unimodular'),'s5_permutation_count':r.get('s5_permutation_count'),'s5_signed_orientation_transport_exact':r.get('s5_signed_orientation_transport_exact'),
      'triangle_parent_match':r.get('triangle_parent_match'),'iter466_negative_transpose_match_all_roots':r.get('iter466_negative_transpose_match_all_roots'),'raw_linear_tree_coordinate_jacobian_abs_det':r.get('raw_linear_tree_coordinate_jacobian_abs_det'),
      'group_variable_tangent_pushforward_prerequisite_closed':r.get('group_variable_tangent_pushforward_prerequisite_closed') if cls!=INVALID else False,
      'distributional_contact_pushforward_authorized':False,'physical_transverse_quotient_authorized':False,'haar_contact_normalization_authorized':False,'observable_pushforward_authorized':False,'d7_s2_closed':False,
      'claim_ceiling':r.get('claim_ceiling')
    }
    raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['aggregate_sha256']=hashlib.sha256(raw).hexdigest()
    Path(a.out).parent.mkdir(parents=True,exist_ok=True);Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));return 0 if cls!=INVALID else 2


if __name__=='__main__':raise SystemExit(main())
