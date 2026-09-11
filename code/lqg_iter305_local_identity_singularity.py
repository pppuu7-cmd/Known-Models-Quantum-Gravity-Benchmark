#!/usr/bin/env python3
import json, math, pathlib

contract=json.load(open('benchmarks/lqg_iter305_toller_tail_local_integrability_split.json'))
# Source-explicit gamma-simple example: k=j=l=1/2, m=+1/2, plus branch.
# |t_+(beta)| = 1 / [2*sinh(beta)^2*(rho^2+1/4)] for real rho.
# Choose physical gamma=1, j=1/2 => rho=1/2. Then beta^2 |t_+| -> 1.
rho=0.5
betas=[1e-1,5e-2,2e-2,1e-2,5e-3,2e-3,1e-3]
rows=[]
for beta in betas:
    mag=1.0/(2.0*(math.sinh(beta)**2)*(rho*rho+0.25))
    scaled=(beta*beta)*mag
    rows.append({'beta':beta,'abs_t_plus':mag,'beta2_abs_t_plus':scaled})
last=rows[-1]['beta2_abs_t_plus']
# The finite nonzero beta^2-scaled limit establishes a beta^-2 local singularity.
ok=(abs(last-1.0)<1e-5 and rows[-1]['abs_t_plus']>rows[0]['abs_t_plus']*1000 and
    contract['prospectively_frozen_claims']['explicit_fixed_branch_identity_neighborhood_singularity_exists'] and
    not contract['prospectively_frozen_claims']['local_identity_neighborhood_integrability_closed'])
out={
  'probe':'local_identity_singularity',
  'pass':bool(ok),
  'iteration':305,
  'physical_example':{'gamma':1.0,'j':0.5,'rho':rho,'m':0.5,'branch':'plus'},
  'source_formula_magnitude':'1/[2 sinh(beta)^2 (rho^2+1/4)]',
  'local_behavior':'|t_plus| ~ beta^-2 for beta->0',
  'scaled_limit':'beta^2 |t_plus| -> 1 for rho=1/2',
  'rows':rows,
  'interpretation':'radial-infinity decay cannot by itself provide a global bounded hyperbolic majorant for each fixed Toller branch'
}
pathlib.Path('build/lqg-iter305').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter305/local_identity_singularity.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
