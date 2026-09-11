#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from cfs_currents_correction_common import write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    files=sorted(Path(a.input_dir).glob('*.json'))
    if len(files)!=4: raise SystemExit(f'expected 4 guard results, found {len(files)}')
    rows=[json.loads(p.read_text(encoding='utf-8')) for p in files]
    if not all(r.get('pass') is True for r in rows): raise SystemExit('at least one guard failed')
    expected={
      'PASS_EXPLICIT_CFS_CURRENT_FORMALISM_AND_RANK_ONE_MAXWELL_CONTROL',
      'PASS_SYSTEMATIC_CURRENT_FORMALISM_EXTENDS_IN_SCOPE_TO_GRAVITATION_AND_HIGHER_ORDER_CORRECTIONS',
      'PASS_RANK_TWO_AND_HIGHER_RANK_BOUNDARY__GRAVITY_AND_CORRECTIONS_REMAIN_PROSPECTIVE',
      'PASS_HIGH_VALUE_PATHWAY_TOWARD_CFS_CORRECTION_TENSOR__FROZEN_NORMALIZED_GRAVITY_RESIDUAL_OBJECT_STILL_MISSING'}
    classes={r['classification'] for r in rows}
    if classes!=expected: raise SystemExit('classification set mismatch')
    write_json(a.output,{
      'iteration':'Iter289','pass':True,'independent_jobs':4,
      'explicit_rank_one_control':True,
      'gravity_extension_pathway':True,
      'rank_two_gravity_tensor_explicit':False,
      'higher_rank_correction_tensor_explicit':False,
      'frozen_cfs_blocker_closed':False,
      'classification':'HIGH_VALUE_CFS_SYSTEMATIC_CURRENT_AND_HIGHER_RANK_PATHWAY__GRAVITY_CORRECTION_TENSOR_REMAINS_PROSPECTIVE_AND_BLOCKER_STAYS_OPEN',
      'guard_classifications':sorted(classes)})
if __name__=='__main__': main()
