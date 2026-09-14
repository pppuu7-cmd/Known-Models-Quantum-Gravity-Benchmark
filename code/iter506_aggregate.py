#!/usr/bin/env python3
import argparse, glob, json, os

PASS='ITER506_UNIFORM_FULL_K5_NEIGHBORHOOD_CERTIFIED_SCOPED'
FAIL='SCIENTIFIC_FAIL_ITER506_NO_CERTIFIED_OPEN_NEIGHBORHOOD_AT_FROZEN_RADII'
BLOCK='BLOCKED_OR_INFRASTRUCTURE_ITER506'
ETAS=(1e-12,1e-10,1e-8,1e-6)
PANELS=('T0','T1','T2')
CAUSALS=('0to5','1to4','2to3')
RHOS=(7,8)
EXPECTED={f'{p}-{c}-rho{r}' for p in PANELS for c in CAUSALS for r in RHOS}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    recs=[]
    for fn in glob.glob(os.path.join(a.root,'**','iter506-*.json'),recursive=True):
        if fn.endswith('summary.json'): continue
        try:
            with open(fn) as f: recs.append(json.load(f))
        except Exception: pass
    by={}; duplicates=[]
    for x in recs:
        lane=x.get('lane')
        if lane in by: duplicates.append(lane)
        else: by[lane]=x
    found=set(by)
    missing=sorted(EXPECTED-found)
    extra=sorted(found-EXPECTED)
    invalid=sorted(k for k,v in by.items() if not v.get('valid',False))
    qualified=sorted(k for k,v in by.items() if v.get('classification')==PASS and v.get('pass',False))
    sci_fail=sorted(k for k,v in by.items() if v.get('classification')==FAIL)
    counts={}
    min_margin={}
    for eta in ETAS:
        key=f'{eta:.0e}'
        vals=[]
        for lane,v in by.items():
            for q in v.get('radii',[]):
                if abs(float(q.get('eta',-1))-eta) <= eta*1e-12:
                    if q.get('certified',False): vals.append(float(q.get('normalized_margin')))
                    break
        counts[key]=len(vals)
        min_margin[key]=min(vals) if vals else None
    largest=[float(v.get('largest_certified_eta',0.0)) for v in by.values() if v.get('valid',False)]
    if missing or duplicates or extra or invalid:
        gate=BLOCK
    elif len(qualified)==18:
        gate=PASS
    elif sci_fail:
        gate=FAIL
    else:
        gate=BLOCK
    common=[eta for eta in ETAS if counts[f'{eta:.0e}']==18]
    out={
      'iteration':506,'lane_count_expected':18,'lane_count_found':len(found),
      'missing_lanes':missing,'extra_lanes':extra,'duplicates':sorted(set(duplicates)),'invalid_lanes':invalid,
      'qualified_lane_count':len(qualified),'scientific_fail_lanes':sci_fail,
      'certified_lane_count_by_eta':counts,'minimum_normalized_positive_margin_by_eta':min_margin,
      'minimum_largest_certified_eta_across_valid_lanes':min(largest) if largest else 0.0,
      'largest_common_certified_eta':max(common) if common else 0.0,
      'gate_status':gate,
      'next_gate': 'After PASS, preregister a uniform finite-t remainder/blow-up domination gate before any positive-measure/Haar claim; otherwise repair only the first causal blocker without post-hoc radius insertion.',
      'claim_lock':'No Haar theorem, spectral theorem, D7-S2 closure, terminal D7 classifier, or Candidate Gravity activation.'
    }
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
