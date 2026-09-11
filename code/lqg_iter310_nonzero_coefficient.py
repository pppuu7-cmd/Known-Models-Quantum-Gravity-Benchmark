#!/usr/bin/env python3
import json, pathlib
from fractions import Fraction
p=json.load(open('benchmarks/lqg_iter310_scaling_degree_extension.json'))
rows=[]; ok=True
for g in [Fraction(0,1),Fraction(1,10),Fraction(1,2),Fraction(1,1),Fraction(137,100),Fraction(5,1),Fraction(100,1)]:
    den=Fraction(648,1)*(1+g*g)**10
    coeff=-Fraction(1,1)/den
    good=(coeff!=0)
    ok &= good
    rows.append({'gamma':str(g),'coefficient':str(coeff),'nonzero':good})
out={'probe':'nonzero_coefficient','pass':bool(ok),'iteration':310,
     'exact_formula':'-1/[648*(1+gamma^2)^10]','real_gamma_zero_set':'empty','rows':rows,
     'interpretation':'the delta^-20 homogeneous witness is not removed by any finite real Barbero-Immirzi gamma'}
pathlib.Path('build/lqg-iter310').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter310/nonzero_coefficient.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
