#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    rows=[]
    for p in sorted(Path(a.input_dir).glob('*.json')):
        rows.append(json.loads(p.read_text(encoding='utf-8')))
    required={'cfs_geometric_einstein_scope_guard','cfs_geometric_conservation_scaling_guard','cfs_geometric_corrections_maturity_guard','cfs_geometric_blocker_guard'}
    names={r.get('probe') for r in rows}
    ok=(required==names and all(r.get('pass') is True for r in rows))
    payload={
      'iteration':'Iter294','pass':ok,'probes':rows,
      'explicit_lorentzian_einstein_endpoint':True if ok else None,
      'systematic_correction_hierarchy':True if ok else None,
      'concrete_normalized_beyond_einstein_residual_comparator':False,
      'family_terminal':False,
      'd7_authorized':False,
      'classification':'HIGH_VALUE_CFS_GEOMETRIC_LORENTZIAN_EINSTEIN_DERIVATION_AND_SYSTEMATIC_CORRECTION_HIERARCHY__CONCRETE_NORMALIZED_BEYOND_EINSTEIN_RESIDUAL_COMPARATOR_STILL_MISSING' if ok else 'FAIL_ITER294_AGGREGATE_CONTRACT'
    }
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()
