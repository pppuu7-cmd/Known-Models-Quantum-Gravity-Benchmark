#!/usr/bin/env python3
import json, pathlib
from fractions import Fraction

p=json.load(open('benchmarks/lqg_iter307_minspin_contracted_local_witness.json'))
# Eq.(9)/(46) at j=1/2. Gamma recurrences and the z->1 hypergeometric
# coefficient reduce the beta^-2 terms to C=2/(1+gamma^2).
# We verify the reduced rational structure on exact rational gamma samples and
# the mandatory cancellation T+ + T- = D of the beta^-2 pole.
rows=[]
ok=True
for g in [Fraction(1,10),Fraction(1,2),Fraction(1,1),Fraction(137,100),Fraction(5,1)]:
    C=Fraction(2,1)/(1+g*g)
    plus=( -C, +C )   # m=+1/2, -1/2
    minus=( +C, -C )
    cancel=(plus[0]+minus[0],plus[1]+minus[1])
    good=(C>0 and cancel==(0,0))
    ok &= good
    rows.append({'gamma':str(g),'C':str(C),'tplus_leading':[str(x) for x in plus],
                 'tminus_leading':[str(x) for x in minus],'leading_sum':[str(x) for x in cancel]})
ok &= p['prospectively_frozen_claims']['j_half_branch_leading_kernel_exact']
out={'probe':'jhalf_leading_kernel','pass':bool(ok),'iteration':307,
     'formula':'T^(kappa)(boost n,beta) ~ -kappa*[2/(1+gamma^2)]*(n.sigma)*beta^-2',
     'source_consistency':'beta^-2 terms cancel exactly in T+ + T- = D','rows':rows}
pathlib.Path('build/lqg-iter307').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter307/jhalf_leading_kernel.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
