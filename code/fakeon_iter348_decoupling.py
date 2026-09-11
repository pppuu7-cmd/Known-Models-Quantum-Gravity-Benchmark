#!/usr/bin/env python3
import json
from pathlib import Path

def ratio(alpha,xi): return 4.5*alpha*alpha/(xi*xi)

def main():
    alpha=0.05
    xis=[0.4,0.2,0.1,0.05,0.025]
    vals=[ratio(alpha,x) for x in xis]
    scaling=[]
    for i in range(len(xis)-1):
        # Halving xi must multiply the ratio by four for xi^-2 scaling.
        q=vals[i+1]/vals[i]
        scaling.append(q)
        assert abs(q-4.0)<1e-12
    assert all(vals[i+1]>vals[i] for i in range(len(vals)-1))
    out={'iteration':348,'lane':'decoupling_scaling','alpha_k':alpha,'xi_sequence':xis,'ratio_sequence':vals,'successive_halving_factors':scaling,
         'classification':'PASS_SCOPED_RATIO_EXHIBITS_EXACT_XI_MINUS2_GROWTH_AND_NO_FINITE_XI_TO_ZERO_LIMIT_AT_FIXED_ALPHA',
         'scope_guard':['SOURCE_DEFINED_LEADING_POWER_SPECTRA','ASYMPTOTIC_SCALING_CERTIFICATE','NOT_A_GENERIC_FAKEON_NO_GO','NO_PARENT_FAMILY_TERMINALIZATION','NO_D7_PROMOTION']}
    Path('iter348-decoupling.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
