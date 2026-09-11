#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter312_partial_diagonal_causal_sign_cancellation.json'))
# Need W=w0+5w1+10w2=0 to cancel K3/K5 and Q=w0-3w1+2w2=0 to cancel K4.
# Exact null direction is proportional to (-5,-1,+1).
base=(-5,-1,1)
W=base[0]+5*base[1]+10*base[2]
Q=base[0]-3*base[1]+2*base[2]
signed_ok=(W==0 and Q==0)
# For nonnegative weights, W=0 implies every weight is zero.
nonnegative_samples=[(1,0,0),(0,1,0),(0,0,1),(1,1,1),(2,3,4)]
nonnegative_no_cancel=all((w0+5*w1+10*w2)>0 for w0,w1,w2 in nonnegative_samples)
ok=(signed_ok and nonnegative_no_cancel and
    p['prospectively_frozen_claims']['signed_class_weight_null_direction']==[-5,-1,1] and
    p['prospectively_frozen_claims']['nontrivial_nonnegative_class_weights_cancel_triangle_and_k5'] is False and
    p['prospectively_frozen_claims']['signed_class_weight_null_direction_source_grounded_or_physically_admissible'] is False)
out={'probe':'weight_solution_guard','pass':bool(ok),'iteration':312,
     'equations':['W=w0+5w1+10w2=0','Q=w0-3w1+2w2=0'],
     'signed_null_direction':list(base),'signed_null_checks':{'W':W,'Q':Q},
     'nonnegative_nontrivial_solution_exists':False,
     'physical_status':'the signed null direction is algebraic only; no source-grounded admissibility is established'}
pathlib.Path('build/lqg-iter312').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter312/weight_solution_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
