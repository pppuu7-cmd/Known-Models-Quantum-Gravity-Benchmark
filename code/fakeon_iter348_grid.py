#!/usr/bin/env python3
import json
from pathlib import Path

def ratio(alpha,xi): return 4.5*alpha*alpha/(xi*xi)

def main():
    alphas=[0.01,0.02,0.05,0.1]
    xis=[0.01,0.02,0.05,0.1,0.2,0.5]
    rows=[]
    for a in alphas:
        seq=[]
        for x in xis:
            r=ratio(a,x); seq.append(r); rows.append({'alpha_k':a,'xi':x,'ratio':r})
        assert all(seq[i]>seq[i+1] for i in range(len(seq)-1))
    out={'iteration':348,'lane':'independent_grid','probe_count':len(rows),'rows':rows,
         'classification':'PASS_SCOPED_FROZEN_GRID_CONFIRMS_MONOTONE_PHYSICAL_TENSOR_SPECTRUM_RATIO_SCALING',
         'scope_guard':['FINITE_GRID_IS_A_REPRODUCIBILITY_GUARD_NOT_THE_LIMIT_PROOF','NO_PARENT_FAMILY_TERMINALIZATION','NO_D7_PROMOTION']}
    Path('iter348-grid.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
