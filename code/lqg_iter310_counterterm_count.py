#!/usr/bin/env python3
import json, math, pathlib
p=json.load(open('benchmarks/lqg_iter310_scaling_degree_extension.json'))
c=p['prospectively_frozen_claims']
d=c['relative_dimension']; N=c['max_local_delta_derivative_order']
# Number of multiindices alpha in N^d with |alpha|<=N = C(d+N,N).
count=math.comb(d+N,N)
ok=(d==12 and N==8 and count==125970 and c['unconstrained_multiindex_counterterm_count_in_12d_through_order_8']==count)
out={'probe':'counterterm_count','pass':bool(ok),'iteration':310,'dimension':d,'max_order':N,
     'unconstrained_multiindex_count':count,'formula':'C(d+N,N)',
     'scope':'raw local ambiguity count before covariance, gauge, parity, permutation, gluing or normalization constraints'}
pathlib.Path('build/lqg-iter310').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter310/counterterm_count.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
