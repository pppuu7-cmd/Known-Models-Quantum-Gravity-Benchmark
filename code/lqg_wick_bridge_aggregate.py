#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from lqg_wick_bridge_common import write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    files=sorted(Path(a.input_dir).glob('*.json'))
    if len(files)!=4: raise SystemExit(f'expected 4 guard results, found {len(files)}')
    rows=[json.loads(p.read_text(encoding='utf-8')) for p in files]
    if not all(r.get('pass') is True for r in rows): raise SystemExit('at least one guard failed')
    expected={
      'PASS_EXPLICIT_EUCLIDEAN_LORENTZIAN_EPRL_VERTEX_ANALYTIC_CONTINUATION',
      'PASS_SIGNATURE_MAP_REQUIRES_IMMIRZI_ANALYTIC_CONTINUATION__NO_SAME_REAL_GAMMA_IDENTITY',
      'PASS_VERTEX_LEVEL_SIGNATURE_RELATION__RIGGING_MAP_AND_COMPLETE_STACK_TRANSPORT_NOT_ESTABLISHED',
      'PASS_HIGH_VALUE_SIGNATURE_BRIDGE_COMPONENT__NO_YANG_TO_HAN_REAL_GAMMA_STATE_AND_STACK_TRANSPORT'}
    classes={r['classification'] for r in rows}
    if classes!=expected: raise SystemExit('classification set mismatch')
    write_json(a.output,{
      'iteration':'Iter286','pass':True,'independent_jobs':4,
      'explicit_euclidean_lorentzian_vertex_map':True,
      'structural_signature_bridge':True,
      'same_real_gamma_identity':False,
      'rigging_map_transport_ready':False,
      'complete_stack_transport_ready':False,
      'same_realization_chain_ready':False,
      'classification':'HIGH_VALUE_EPRL_SIGNATURE_ANALYTIC_CONTINUATION_BRIDGE__REAL_GAMMA_PHYSICAL_STATE_AND_COMPLETE_STACK_TRANSPORT_STILL_OPEN',
      'guard_classifications':sorted(classes)})
if __name__=='__main__': main()
