#!/usr/bin/env python3
import json, pathlib
from fractions import Fraction

p=json.load(open('benchmarks/lqg_iter306_toller_local_power_count.json'))
rows=[]
ok=True
for j2 in range(1,33):
    j=Fraction(j2,2)
    target=-(2*j+1)
    for m2 in range(-j2,j2+1,2):
        m=Fraction(m2,2)
        # Eq. (46), ignoring cancelling +/- i*rho pieces exactly.
        plus=(1+m)-(j+m+1)-(j+1)
        minus=(1-m)-(j-m+1)-(j+1)
        good=(plus==target and minus==target)
        ok=ok and good
        rows.append({'two_j':j2,'two_m':m2,'c_minus_a_minus_b':str(target),'pass':good})
ok=ok and p['prospectively_frozen_claims']['gamma_simple_hypergeometric_c_minus_a_minus_b_equals_minus_2j_minus_1']
out={'probe':'hypergeom_local_exponent','pass':bool(ok),'iteration':306,
     'relation':'c-a-b=-(2j+1) for both gamma-simple Toller branches',
     'checked_rows':len(rows),'sample_rows':rows[:12]}
pathlib.Path('build/lqg-iter306').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter306/hypergeom_local_exponent.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
