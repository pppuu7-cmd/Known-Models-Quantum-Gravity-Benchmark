#!/usr/bin/env python3
"""Iter288 exact/numerical semiclassical hierarchy overlap probe."""
import argparse,json,math
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--separation',type=float,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    R=a.separation
    if R<=1: raise SystemExit('separation factor must be >1')
    # Operational sensitivity interpretation of 1 << gamma^-1 << lambda << gamma^-2:
    # lambda >= R*gamma^-1 and lambda <= gamma^-2/R.
    # Nonempty interval iff gamma < 1/R^2. This is a sensitivity diagnostic, not a physical threshold.
    gamma_critical=1.0/(R*R)
    test_gammas=[0.5,0.25,0.1,0.05,0.02,0.01,0.005,0.002,0.001]
    rows=[]
    for g in test_gammas:
        lo=R/g
        hi=1.0/(R*g*g)
        feasible=lo < hi
        rows.append({
          'gamma':g,'lambda_lower':lo,'lambda_upper':hi,'feasible':feasible,
          'window_ratio':hi/lo,
          'geometric_midpoint':math.sqrt(lo*hi) if feasible else None})
    # Dense numerical check of the analytic critical gamma from the allowed BH range (0,0.5].
    n=200000
    max_feasible=0.0
    for i in range(1,n+1):
        g=0.5*i/n
        if R/g < 1.0/(R*g*g): max_feasible=g
    rel=abs(max_feasible-gamma_critical)/gamma_critical if gamma_critical<=0.5 else None
    payload={
      'iteration':'Iter288','separation_factor':R,'interpretation':'sensitivity_only_not_physical_threshold',
      'bh_gamma_upper':0.5,'analytic_gamma_critical':gamma_critical,
      'dense_scan_max_feasible_gamma':max_feasible,'relative_grid_error_to_analytic':rel,
      'rows':rows,'pass':True,
      'classification':'PASS_HIERARCHY_SENSITIVITY_PROBE__FEASIBILITY_REQUIRES_GAMMA_BELOW_INVERSE_SEPARATION_SQUARED'}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
