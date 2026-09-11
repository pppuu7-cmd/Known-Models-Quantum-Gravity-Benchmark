#!/usr/bin/env python3
import json, pathlib
from fractions import Fraction

p=json.load(open('benchmarks/lqg_iter308_causal_support_pole_cancellation.json'))
# Every causal sector has the same nonzero leading factor +1, so a weighted
# sum has factor sum(w_sigma).  Nonnegative weights, not all zero, cannot cancel.
samples=[
 [Fraction(1,1)]*16,
 [Fraction(i+1,17) for i in range(16)],
 [Fraction(0,1)]*15+[Fraction(3,7)],
 [Fraction(1,5) if i%3==0 else Fraction(0,1) for i in range(16)],
]
rows=[]; ok=True
for weights in samples:
    nonnegative=all(w>=0 for w in weights)
    nontrivial=any(w>0 for w in weights)
    factor=sum(weights,Fraction(0,1))
    good=(nonnegative and nontrivial and factor>0)
    ok &= good
    rows.append({'sum_weights':str(factor),'nonnegative':nonnegative,'nontrivial':nontrivial,'cancels':factor==0})
ok &= (p['prospectively_frozen_claims']['positive_weight_causal_sum_can_cancel_common_nonzero_leading_term'] is False)
out={'probe':'nonnegative_weight_guard','pass':bool(ok),'iteration':308,
     'general_rule':'if all leading sector factors are +1, weighted leading factor=sum_sigma w_sigma; for w_sigma>=0 and some w_sigma>0 this is strictly positive',
     'sample_rows':rows,'signed_or_complex_counterweights_out_of_scope':True}
pathlib.Path('build/lqg-iter308').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter308/nonnegative_weight_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
