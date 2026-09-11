#!/usr/bin/env python3
import json, pathlib
from fractions import Fraction

p=json.load(open('benchmarks/lqg_iter308_causal_support_pole_cancellation.json'))
# Iter307 coefficient per inequivalent causal sector:
# -1/[648(1+gamma^2)^10] * delta^-20.
per_sector=Fraction(-1,648)
class_factors={'0_5':1,'1_4':5,'2_3':10}
class_coeff={k:per_sector*v for k,v in class_factors.items()}
total=per_sector*16
ok=(total==Fraction(-2,81) and class_coeff['0_5']==Fraction(-1,648) and
    class_coeff['1_4']==Fraction(-5,648) and class_coeff['2_3']==Fraction(-5,324) and
    p['prospectively_frozen_claims']['unit_weight_causal_sum_witness_coefficient']=='-2/[81*(1+gamma^2)^10]')
out={'probe':'unit_causal_sum_witness','pass':bool(ok),'iteration':308,
     'per_sector_coefficient_without_common_denominator':str(per_sector),
     'class_coefficients_without_(1+gamma^2)^-10':{k:str(v) for k,v in class_coeff.items()},
     'unit_weight_16_sector_coefficient_without_(1+gamma^2)^-10':str(total),
     'full_unit_weight_leading_term':'-2/[81*(1+gamma^2)^10] * delta^-20'}
pathlib.Path('build/lqg-iter308').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter308/unit_causal_sum_witness.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
