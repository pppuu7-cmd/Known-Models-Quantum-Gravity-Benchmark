#!/usr/bin/env python3
import json, pathlib
from fractions import Fraction

contract=json.load(open('benchmarks/lqg_iter305_toller_tail_local_integrability_split.json'))
# Toller poles obey i*rho = integer in [-j,l].  For physical gamma-simple labels
# rho=gamma*j with real gamma>0 and j>0, rho is real and nonzero, so i*rho is
# purely imaginary and cannot equal a real integer.
samples=[]
for gamma in (Fraction(1,10), Fraction(1,1), Fraction(137,100), Fraction(5,1)):
    for j2 in range(1,17):
        j=Fraction(j2,2)
        rho=gamma*j
        samples.append({'gamma':str(gamma),'two_j':j2,'rho':str(rho),'rho_nonzero':rho!=0})
all_nonzero=all(s['rho_nonzero'] for s in samples)
ok=(all_nonzero and
    contract['prospectively_frozen_claims']['positive_real_gamma_simple_rho_hits_toller_pole'] is False)
out={
  'probe':'physical_rho_pole_guard',
  'pass':bool(ok),
  'iteration':305,
  'pole_condition':'i*rho belongs to the real integer interval {-j,...,l}',
  'physical_domain':'real gamma>0, j>0, rho=gamma*j>0',
  'conclusion':'positive real gamma-simple rho cannot coincide with a Toller pole in rho',
  'zero_spin_boundary':'j=0 gives rho=0 and is not certified by this guard',
  'sample_count':len(samples)
}
pathlib.Path('build/lqg-iter305').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter305/physical_rho_pole_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
