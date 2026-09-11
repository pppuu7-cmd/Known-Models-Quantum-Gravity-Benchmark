#!/usr/bin/env python3
import json, math, pathlib
# Exact analytic witness: a polynomially bounded function need not be integrable
# against the noncompact radial Lorentz/H^3 volume factor sinh(r)^2 dr.
# f(r)=1 is polynomially bounded, while integral_0^R sinh(r)^2 dr = sinh(2R)/4 - R/2 -> infinity.
Rs=[1,2,3,4,5]
vals=[math.sinh(2*r)/4-r/2 for r in Rs]
ok=all(vals[i+1]>vals[i] for i in range(len(vals)-1)) and vals[-1]>1000
out={'probe':'polynomial_bound_nonintegrability_witness','pass':bool(ok),'iteration':304,
     'witness_function':'f(r)=1','polynomially_bounded':True,
     'radial_measure':'sinh(r)^2 dr','cutoffs':Rs,'partial_integrals':vals,
     'analytic_primitive':'sinh(2R)/4 - R/2',
     'tested_claim':'polynomial boundedness alone is insufficient to infer noncompact Haar/radial integrability'}
pathlib.Path('build/lqg-iter304').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter304/polynomial_bound_nonintegrability_witness.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
