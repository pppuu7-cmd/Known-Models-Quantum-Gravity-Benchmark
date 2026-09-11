#!/usr/bin/env python3
import json, pathlib
from fractions import Fraction

contract=json.load(open('benchmarks/lqg_iter305_toller_tail_local_integrability_split.json'))
mins=[]
rows=[]
for j2 in range(1, 33):
    j=Fraction(j2,2)
    local=[]
    for m2 in range(-j2, j2+1, 2):
        m=Fraction(m2,2)
        a_plus=Fraction(1,1)+abs(j+m)
        a_minus=Fraction(1,1)+abs(j-m)
        local.extend([a_plus,a_minus])
    mn=min(local)
    mins.append(mn)
    rows.append({'two_j':j2,'min_decay_exponent':float(mn)})
expected=Fraction(1,1)
ok=(all(x==expected for x in mins) and
    contract['prospectively_frozen_claims']['gamma_simple_minimum_radial_decay_exponent']==1.0)
out={
  'probe':'gamma_simple_decay_floor',
  'pass':bool(ok),
  'iteration':305,
  'analytic_relation':'a_plus=1+|j+m|, a_minus=1+|j-m| for k=j',
  'minimum_over_m_and_branch':'1 exactly',
  'checked_two_j_range':[1,32],
  'rows':rows
}
pathlib.Path('build/lqg-iter305').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter305/gamma_simple_decay_floor.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
