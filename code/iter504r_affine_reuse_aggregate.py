#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
PASS='ITER504R_ROOT_AFFINE_REUSE_NARROWED_WITHIN_TOLERANCE_SCOPED'
INC='ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED'
INVALID='ITER504R_ROOT_AFFINE_REUSE_INVALID'

def one(root):
 p=sorted(Path(root).rglob('*.json'))
 if len(p)!=1: raise SystemExit(f'expected one json under {root}, got {len(p)}')
 raw=p[0].read_bytes(); return json.loads(raw),hashlib.sha256(raw).hexdigest()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--a',required=True);ap.add_argument('--b',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
 x,xh=one(a.a);y,yh=one(a.b)
 byte=xh==yh; same=x.get('classification')==y.get('classification'); cls=x.get('classification') if byte and same and x.get('classification') in (PASS,INC) else INVALID
 out={
  'gate':x.get('gate'),'classification':cls,'independent_environment_outputs_byte_identical':byte,
  'lane_a_json_sha256':xh,'lane_b_json_sha256':yh,
  'exact_covers_valid':x.get('exact_covers_valid'),'root_controls_valid':x.get('root_controls_valid'),
  'root_model_build_count_valid':x.get('root_model_build_count_valid'),'all_243_channels_retained':x.get('all_243_channels_retained'),
  'total_node_count':x.get('total_node_count'),'total_leaf_count':x.get('total_leaf_count'),
  'certified_leaf_count':x.get('certified_leaf_count'),'unresolved_leaf_count':x.get('unresolved_leaf_count'),
  'leaf_depth_histogram':x.get('leaf_depth_histogram'),'per_root_leaf_count':x.get('per_root_leaf_count'),
  'root_max_drift':x.get('root_max_drift'),'root_max_possible_counts':x.get('root_max_possible_counts'),
  'max_terminal_leaf_possible_count':x.get('max_terminal_leaf_possible_count'),
  'max_terminal_leaf_drift_upper':x.get('max_terminal_leaf_drift_upper'),
  'max_terminal_leaf_drift_witness':x.get('max_terminal_leaf_drift_witness'),
  'minimum_terminal_leaf_S_lower':x.get('minimum_terminal_leaf_S_lower'),
  'per_rho_worst':x.get('per_rho_worst'),'covers':x.get('covers'),'claim_ceiling':x.get('claim_ceiling')}
 payload=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['aggregate_sha256']=hashlib.sha256(payload).hexdigest()
 p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));return 0 if cls!=INVALID else 2
if __name__=='__main__': raise SystemExit(main())
