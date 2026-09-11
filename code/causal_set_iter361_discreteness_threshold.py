#!/usr/bin/env python3
import argparse,json
p=argparse.ArgumentParser()
p.add_argument('--mode',required=True,choices=['d4','all_d'])
p.add_argument('--output',required=True)
a=p.parse_args()
ratios=[1.0,1.1,1.13,1.135,1.136,1.14,1.2,2.0,2.33,2.34,3.0]
rows=[]
for r in ratios:
    if a.mode=='d4':
        # Source quotes ell_0 approximately 1.136 ell_p. Use >1.136 as a fail-closed certified side.
        certified=r>1.136
        basis='quoted d=4 approximate threshold ell_0~1.136 ell_p; strict greater-than used conservatively'
    else:
        # Source quotes 1.13 < ell_0/ell_p < 2.33 across dimensions. r>2.33 is sufficient for all quoted dimensions.
        certified=r>2.33
        basis='quoted all-d upper bound ell_0/ell_p<2.33; r>2.33 sufficient across quoted dimensions'
    rows.append({'ell_over_ell_p':r,'suppression_certified_by_quoted_threshold':certified})
out={
 'iteration':361,
 'mode':a.mode,
 'rows':rows,
 'basis':basis,
 'threshold_is_sufficient_scope_only':True,
 'family_terminal':False,
 'scope':'quoted-threshold robustness audit; does not recompute beta_d coefficients'
}
with open(a.output,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
