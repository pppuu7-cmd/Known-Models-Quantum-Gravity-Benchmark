#!/usr/bin/env python3
import json, math
rows=[]
for n in [10,100,1000,10**6,10**12,10**30,10**60,10**133]:
    # Source states suppression factor has form 2^{-k n^2}, k>0.
    # Report coefficient multiplying k in log10 suppression; do not choose k.
    coeff=-(n*n)*math.log10(2.0)
    rows.append({'n':str(n),'log10_suppression_per_unit_k':coeff if abs(coeff)<1e308 else f'-{math.log10(2.0)}e{2*len(str(n))-2}'})
out={
 'iteration':362,
 'source_form':'suppression factor 2^(-k n^2), k>0',
 'rows':rows,
 'quoted_physical_example_n':'~1e133 for 1 ns x 1 cm^3 at Planck discreteness',
 'quoted_order':'~2^(-1e266)',
 'remaining_open_sector':['sparse layered measure-zero sets','non-layered non-continuumlike sets','dimension-selection problem'],
 'family_status':'PARTIAL_SUBFAMILY_ONLY',
 'family_terminal':False,
 'd7_promotion_authorized':False,
 'scope_guard':['LAYERED_SUPPRESSION_NOT_FULL_EMERGENT_MANIFOLD_CERTIFICATE','NO_SPARSE_OR_NONLAYERED_EXHAUSTION','NO_DIMENSION_SELECTION_CLOSURE','NO_BLOCKED_TO_FAIL','NO_D7_PROMOTION']
}
with open('iter362-causal-set-scope.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
