#!/usr/bin/env python3
import json, pathlib
from fractions import Fraction

p=json.load(open('benchmarks/lqg_iter306_toller_local_power_count.json'))
rows=[]
for j2 in range(1,9):
    j=Fraction(j2,2)
    q=int(2*j+1)
    subset=[]
    for s in range(2,6):
        P=(s*(s-1)//2)*q
        D=3*(s-1)
        delta=P-D
        subset.append({'s':s,'delta':delta,'status':'safe' if delta<0 else ('marginal' if delta==0 else 'risk')})
    rows.append({'two_j':j2,'q':q,'subsets':subset,'worst_delta':max(x['delta'] for x in subset)})
ok=(rows[0]['q']==2 and rows[0]['worst_delta']==8 and rows[1]['q']==3 and rows[1]['subsets'][0]['delta']==0 and
    p['prospectively_frozen_claims']['component_level_power_count_risk_established'])
out={'probe':'uniform_spin_threshold_map','pass':bool(ok),'iteration':306,
     'rule':'q=2j+1; delta_s=C(s,2) q - 3(s-1)','rows':rows,
     'interpretation':'risk grows monotonically with spin at component level; this is not a contracted-vertex divergence result'}
pathlib.Path('build/lqg-iter306').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter306/uniform_spin_threshold_map.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
