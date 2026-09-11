#!/usr/bin/env python3
import json, math
from pathlib import Path

# Dondarini PRD 108, 083526 (2023): Eq. 3.18 and Eq. 4.16, leading terms.
# Common positive factor G*m_phi^2/pi cancels in the normalized ratio.
def p_gr(alpha):
    return 16.0/(9.0*alpha*alpha)

def p_fakeon(xi):
    return 8.0/(xi*xi)

def main():
    probes=[]
    max_res=0.0
    for alpha in [0.01,0.03,0.07,0.1]:
        for xi in [0.02,0.05,0.1,0.2]:
            direct=p_fakeon(xi)/p_gr(alpha)
            closed=4.5*alpha*alpha/(xi*xi)
            res=abs(direct-closed)
            max_res=max(max_res,res)
            probes.append({'alpha_k':alpha,'xi':xi,'direct_ratio':direct,'closed_ratio':closed,'residual':res})
    assert max_res < 1e-12
    out={'iteration':348,'lane':'algebra_identity','probe_count':len(probes),'max_identity_residual':max_res,'probes':probes,
         'classification':'PASS_SCOPED_PUBLISHED_LEADING_TENSOR_SPECTRA_GIVE_RATIO_9_OVER_2_ALPHA2_OVER_XI2',
         'scope_guard':['QUADRATIC_INFLATION_ONLY','LEADING_EQUAL_PUBLISHED_ORDER','NORMALIZED_TENSOR_POWER_SPECTRUM','NO_PARENT_FAMILY_TERMINALIZATION','NO_D7_PROMOTION']}
    Path('iter348-ratio.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
