#!/usr/bin/env python3
import argparse,json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    files=sorted(Path(a.input_dir).glob('*.json'))
    if len(files)!=4: raise SystemExit(f'expected 4 sensitivity results, found {len(files)}')
    rows=[json.loads(p.read_text()) for p in files]
    if not all(r.get('pass') is True for r in rows): raise SystemExit('a sensitivity probe failed')
    sep=sorted((r['separation_factor'],r['analytic_gamma_critical']) for r in rows)
    expected=[(2.0,0.25),(3.0,1/9),(5.0,0.04),(10.0,0.01)]
    for (R,g),(eR,eg) in zip(sep,expected):
        if R!=eR or abs(g-eg)>1e-15: raise SystemExit('analytic sensitivity threshold mismatch')
    payload={
      'iteration':'Iter288','pass':True,'independent_jobs':4,
      'separation_sensitivity':[{ 'R':R,'gamma_critical':g } for R,g in sep],
      'bh_gamma_upper':0.5,
      'stronger_hierarchy_requires_progressively_smaller_gamma':True,
      'physical_threshold_claimed':False,
      'classification':'QUANTIFIED_SEMICLASSICAL_HIERARCHY_OVERLAP__BH_RANGE_CONTAINS_SMALL_GAMMA_SUBDOMAIN_WITH_REGGE_WINDOW_BUT_NO_UNIQUE_NUMERICAL_DOUBLE_LESS_THAN_THRESHOLD'}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
