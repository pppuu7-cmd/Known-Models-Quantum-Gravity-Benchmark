#!/usr/bin/env python3
import argparse, glob, json, os
EPS=[0.0025,0.005,0.01,0.02]; CAUSALS={'0to5','1to4','2to3'}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    rows=[]
    for p in glob.glob(os.path.join(a.root,'**','*.json'),recursive=True):
        with open(p) as f: rows.append(json.load(f))
    expected={(c,i) for c in CAUSALS for i in range(4)}; present={(r.get('causal'),r.get('radius_index')) for r in rows}
    complete=(present==expected and len(rows)==12); invalid=[r for r in rows if not r.get('valid')]
    robust=[]; nondec=[]
    for i,e in enumerate(EPS):
        rr=[r for r in rows if r.get('radius_index')==i]
        if len(rr)==3 and all(r.get('all_sampled_robust') for r in rr): robust.append(e)
        if len(rr)==3 and all(r.get('all_sampled_nondecay') for r in rr): nondec.append(e)
    if not complete or invalid: cls='INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER490'
    elif robust: cls='ITER490_FULL_ANGULAR_SAMPLED_ROBUST_THICKENING_QUALIFIED_SCOPED'
    elif nondec: cls='ITER490_FULL_ANGULAR_SAMPLED_NONDECAY_THICKENING_QUALIFIED_SCOPED'
    else: cls='SCIENTIFIC_FAIL_ITER490_ANGULAR_THICKENING'
    out={'iteration':490,'expected_lanes':12,'present_lanes':len(present),'classification':cls,'robust_radii':robust,'sampled_nondecay_radii':nondec,'largest_robust_radius':max(robust) if robust else None,'largest_sampled_nondecay_radius':max(nondec) if nondec else None,'invalid_lanes':[f"{r.get('causal')}-r{r.get('radius_index')}" for r in invalid],'lane_results':rows,'scope':'sampled 20-D angular thickening only; no uniform open-neighborhood/Haar-divergence theorem'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True); json.dump(out,open(a.out,'w'),indent=2,sort_keys=True); print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0)
if __name__=='__main__': main()
