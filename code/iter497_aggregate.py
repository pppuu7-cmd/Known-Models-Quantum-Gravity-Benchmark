#!/usr/bin/env python3
import argparse, glob, json, math, os

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    files=sorted(glob.glob(os.path.join(a.root,'**','*.json'),recursive=True))
    rows=[]; invalid=[]
    for p in files:
        try:
            d=json.load(open(p)); rows.append(d)
            if not d.get('valid',False): invalid.append((p,d.get('classification')))
        except Exception as e: invalid.append((p,repr(e)))
    expected=12
    valid_files=[d for d in rows if d.get('valid',False)]
    total=sum(int(d.get('n_holdouts',0)) for d in valid_files)
    covered=sum(int(d.get('n_covered',0)) for d in valid_files)
    ratios=[]; worst=None
    for d in valid_files:
        for r in d.get('records',[]):
            for h in r.get('holdouts',[]):
                q=float(h['coverage_ratio']); ratios.append(q)
                item={'coverage_ratio':q,'causal':d['causal'],'block':d['block'],'rho':r['rho'],'direction':r['direction'],'sign':r['sign'],'amplitude':h['amplitude'],'abs_remainder':h['abs_remainder'],'E_total':h['E_total'],'E3':h['E3'],'EC':h['EC'],'covered':h['covered']}
                if worst is None or q>worst['coverage_ratio']: worst=item
    controls_ok=(len(files)==expected and len(invalid)==0 and len(valid_files)==expected and total>0)
    all_covered=bool(controls_ok and covered==total)
    if not controls_ok:
        cls='INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER497'
    elif all_covered:
        cls='ITER497_RICHARDSON_ENCLOSURE_HOLDOUT_QUALIFIED_SCOPED'
    else:
        cls='SCIENTIFIC_FAIL_ITER497_RICHARDSON_ENCLOSURE_HOLDOUT'
    out={'iteration':497,'classification':cls,'n_files':len(files),'n_valid_files':len(valid_files),'missing_or_invalid_jobs':expected-len(valid_files),'n_holdouts':total,'n_covered':covered,'coverage_fraction':float(covered/total) if total else 0.0,'all_covered':all_covered,'max_coverage_ratio':max(ratios) if ratios else None,'median_coverage_ratio':sorted(ratios)[len(ratios)//2] if ratios else None,'worst_holdout':worst,'invalid':invalid,'scope':'finite preregistered holdout validation only; not continuous interval/uniform or positive-measure theorem'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    json.dump(out,open(a.out,'w'),indent=2,sort_keys=True); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
