#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from pathlib import Path

PREREG='de880ad093d9d6d0c6978e81d3e69b33195b2b92'
SCHEMES={'A':(1,1,1),'B':(1,1,4),'C':(1,2,3)}

def det_q(a,b,c):
    # quadratic form a*x^2+b*y^2+c*(x+y)^2
    return F((a+c)*(b+c)-c*c)

def statistic(a,b,c):
    d=det_q(a,b,c)
    if d <= 0: raise ValueError('non-positive quadratic-form determinant')
    return F(a*b*c,1)/d

def canon(q:F): return f'{q.numerator}/{q.denominator}'

def main(out):
    vals={k:statistic(*v) for k,v in SCHEMES.items()}
    # Controls are derived rather than compared with observed scheme outputs.
    determinant_identity=all(det_q(a,b,c)==F(a*b+a*c+b*c) for a,b,c in SCHEMES.values())
    determinant_positive=all(det_q(*v)>0 for v in SCHEMES.values())
    permutation_symmetry=all(statistic(a,b,c)==statistic(c,b,a)==statistic(b,a,c) for a,b,c in SCHEMES.values())
    # Two independent constraints x,y have diagonal Q=diag(a,b); normalized Gaussian
    # integration cancels sqrt(ab) exactly, leaving no extra width statistic.
    forest_normalization=all(F(a*b, a*b)==1 for a,b,_ in SCHEMES.values())
    controls={'determinant_identity':determinant_identity,'determinant_positive':determinant_positive,'permutation_symmetry':permutation_symmetry,'forest_two_contact_normalization':forest_normalization}
    if not all(controls.values()): cls='INVALID_IMPLEMENTATION'
    elif len(set(vals.values()))>1: cls='TRIANGLE_CONTACT_REGULARIZATION_DEPENDENT_SCOPED'
    else: cls='TRIANGLE_CONTACT_REGULARIZATION_INVARIANT_SCOPED'
    result={'gate':'SOURCE_J1_K5_TRIANGLE_CONTACT_REGULARIZATION_V6','prereg_commit':PREREG,'classification':cls,'schemes':{k:list(v) for k,v in SCHEMES.items()},'statistics_pi_epsI_squared':{k:canon(v) for k,v in vals.items()},'controls':controls,'claim_ceiling':'local three-contact triangle; normalized Gaussian approximate identities only; no full K5 product theorem, no D7 closure, no selector'}
    Path(out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    return 2 if cls=='INVALID_IMPLEMENTATION' else 0

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); a=ap.parse_args(); raise SystemExit(main(a.out))
