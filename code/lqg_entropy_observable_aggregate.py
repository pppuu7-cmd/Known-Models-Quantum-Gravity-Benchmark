#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from lqg_entropy_observable_common import write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.input_dir)
    files=sorted(root.glob('*.json'))
    if len(files)!=4: raise SystemExit(f'expected 4 guard results, found {len(files)}')
    rows=[json.loads(p.read_text(encoding='utf-8')) for p in files]
    if not all(r.get('pass') is True for r in rows): raise SystemExit('at least one guard failed')
    classes=[r['classification'] for r in rows]
    expected={
      'PASS_SCOPED_BH_NORMALIZATION_IDENTITY_BETA_EQUALS_PI_GAMMA',
      'PASS_SCOPED_BH_MATCH_REQUIRES_EXPLICIT_COUPLING_GAMMA_SELECTION',
      'PASS_LEADING_AREA_COEFFICIENT_2COMPLEX_INDEPENDENT__SUBLEADING_GRAPH_DEPENDENCE_REMAINS',
      'PASS_HIGH_VALUE_LORENTZIAN_GRAVITATIONAL_OBSERVABLE_ANCHOR__UV_IR_TRANSPORT_STILL_MISSING'}
    if set(classes)!=expected: raise SystemExit('classification set mismatch')
    write_json(a.output,{
      'iteration':'Iter285','pass':True,'independent_jobs':4,
      'material_lorentzian_observable_anchor':True,
      'bh_normalization_identity_verified':True,
      'parameter_free_bh_normalization':False,
      'leading_2complex_independence':True,
      'full_discretization_independence':False,
      'same_realization_uv_ir_observable_transport_ready':False,
      'classification':'HIGH_VALUE_LORENTZIAN_ENTROPY_OBSERVABLE_ANCHOR_WITH_BH_NORMALIZATION__COUPLING_SELECTION_AND_UV_IR_TRANSPORT_REMAIN_OPEN',
      'guard_classifications':sorted(classes)})
if __name__=='__main__': main()
