#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from lqg_stack_uv_entropy_common import write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    files=sorted(Path(a.input_dir).glob('*.json'))
    if len(files)!=4: raise SystemExit(f'expected 4 guard results, found {len(files)}')
    rows=[json.loads(p.read_text(encoding='utf-8')) for p in files]
    if not all(r.get('pass') is True for r in rows): raise SystemExit('at least one guard failed')
    expected={
      'PASS_HIGH_VALUE_SHARED_LORENTZIAN_STACK_ARCHITECTURE_UV_AND_ENTROPY',
      'PASS_SHARED_STACK_COUPLING_STRUCTURE_WITH_ENTROPY_GAMMA_SELECTION__NO_FULL_PARAMETER_FLOW_CERTIFICATE',
      'PASS_UV_SMALL_SPIN_AND_SEMICLASSICAL_IR_DIRECTION_IDENTIFIED__CONTINUOUS_TRAJECTORY_NOT_COMPUTED',
      'PASS_OBSERVABLE_ANCHOR_INSIDE_SHARED_STACK_ARCHITECTURE__UV_TO_GR_OBSERVABLE_TRANSPORT_STILL_OPEN'}
    classes={r['classification'] for r in rows}
    if classes!=expected: raise SystemExit('classification set mismatch')
    write_json(a.output,{
      'iteration':'Iter287','pass':True,'independent_jobs':4,
      'shared_lorentzian_stack_architecture':True,
      'observable_anchor_inside_shared_stack':True,
      'coupling_gamma_directional_anchor':True,
      'uv_ir_regime_orientation_identified':True,
      'continuous_same_realization_transport_ready':False,
      'classification':'HIGH_VALUE_SAME_STACK_UV_ENTROPY_ALIGNMENT__REALIZATION_IDENTITY_GAP_REDUCED_BUT_CONTROLLED_UV_TO_GR_TRANSPORT_STILL_OPEN',
      'guard_classifications':sorted(classes)})
if __name__=='__main__': main()
