#!/usr/bin/env python3
import argparse,glob,json,math,os,statistics
EXPECTED=[f'{c}-b{b}' for c in ['0to5','1to4','2to3'] for b in range(4)]

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
 docs=[]
 for f in glob.glob(a.root+'/**/iter496-*.json',recursive=True):
  try: docs.append(json.load(open(f)))
  except Exception: pass
 by={d.get('job'):d for d in docs if isinstance(d,dict)}
 missing=[j for j in EXPECTED if j not in by]; invalid=[j for j in EXPECTED if j in by and not by[j].get('valid',False)]
 vals=[]; conv={k:[] for k in ['D','Qii','M']}; suppress=[]; ratios={lab:[] for lab in ['0.005','0.0025','0.00125','richardson']}
 for j in EXPECTED:
  d=by.get(j)
  if not d: continue
  for k in conv:
   conv[k].append(d['convergence'][k])
  for rec in d.get('records',[]):
   for amp,aa in rec['by_amp'].items():
    for row in aa['per_rho']:
     vals.extend(row['abs_remainders'].values()); suppress.append(row['richardson_suppression_ratio'])
   for rr in rec['remainder_ratios']:
    for lab,v in rr['small_over_large'].items(): ratios[lab].append(v)
 valid=(not missing and not invalid and len(by)==12)
 out={'iteration':496,'valid':valid,'job_count':len(by),'missing_jobs':missing,'invalid_jobs':invalid,
      'classification':'ITER496_COEFFICIENT_STENCIL_CONVERGENCE_QUALIFIED_SCOPED' if valid else 'INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER496',
      'abs_remainder_max':max(vals) if vals else None,
      'richardson_suppression_ratio_median':statistics.median(suppress) if suppress else None,
      'richardson_suppression_ratio_max':max(suppress) if suppress else None,
      'remainder_small_over_large_median':{k:statistics.median(v) if v else None for k,v in ratios.items()},
      'remainder_small_over_large_max':{k:max(v) if v else None for k,v in ratios.items()},
      'coefficient_convergence':{},
      'interpretation_ceiling':'finite-set coefficient-stencil/Richardson diagnostic only; no interval/uniform open-neighborhood, positive-measure Haar, D7-S2 closure, terminal label, or Candidate Gravity authorization'}
 for k,rows in conv.items():
  out['coefficient_convergence'][k]={q:(max(r[q] for r in rows) if q.endswith('_max') else statistics.median(r[q] for r in rows)) for q in ['delta_h0_h1_max','delta_h0_h1_median','delta_h1_h2_max','delta_h1_h2_median','halving_ratio_max','halving_ratio_median']} if rows else {}
 os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True); json.dump(out,open(a.out,'w'),indent=2,sort_keys=True); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
