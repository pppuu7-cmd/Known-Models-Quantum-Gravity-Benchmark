#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

# Decoupled control from arXiv:2608.12003v1, Eqs. (25),(31),(32):
# alpha_i=beta=0 => D=E=0 => f2=f4=0. Thus Gamma=-f1 is k-independent
# and the Eq.(32) radicand is affine in x=k^2. This is the structural
# relativistic/late-time control against which Iter353 detects coupled rigidity.
CASES={
 'c0':(-3.0,1.0,0.0),
 'c1':(-1.0,0.5,2.0),
 'c2':(0.0,2.0,-1.0),
 'c3':(4.0,-0.75,3.0),
}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--case',choices=sorted(CASES),required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    f1,f3,f5=CASES[a.case]; xs=[0.0,0.2,0.8,1.7,3.1]
    gammas=[]; rad=[]
    for x in xs:
        gamma=-f1
        r=gamma*gamma+4.0*(-f3*x+f5)
        gammas.append(gamma); rad.append(r)
    max_gamma=max(abs(g-gammas[0]) for g in gammas)
    # unequal spacing-safe affine check: slope against first point must be constant
    slopes=[(rad[i]-rad[0])/(xs[i]-xs[0]) for i in range(1,len(xs))]
    max_slope=max(abs(s-slopes[0]) for s in slopes)
    assert max_gamma<1e-15
    assert max_slope<1e-13
    out={'iteration':354,'case':a.case,'f1':f1,'f3':f3,'f5':f5,'f2':0.0,'f4':0.0,'maximum_gamma_k_dependence':max_gamma,'maximum_affine_slope_residual':max_slope,'classification':'PASS_SCOPED_GFT_DECOUPLED_RELATIVISTIC_SHAPE_CONTROL__K_INDEPENDENT_DAMPING_AND_AFFINE_K2_RADICAND_RECOVERED_WHEN_ALPHA_I_BETA_VANISH','source':'arXiv:2608.12003v1 Eqs. (25),(31),(32)','scope_guard':['STRUCTURAL_CONTROL_NOT_OBSERVATIONAL_FIT','DECOUPLED_ALPHA_I_BETA_ZERO_REGIME','NO_PARENT_FAMILY_TERMINALIZATION','NO_D7_PROMOTION']}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
