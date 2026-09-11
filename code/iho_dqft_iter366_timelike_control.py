#!/usr/bin/env python3
import argparse,json
p=argparse.ArgumentParser()
p.add_argument('--beta',type=float,required=True)
p.add_argument('--output',required=True)
a=p.parse_args()
assert a.beta<0
Mp=1.0
m2_sq=-Mp*Mp/a.beta
pole_k2=-m2_sq
required_s=-pole_k2
out={
 'iteration':366,
 'branch':'FEYNMAN_TIMELIKE_CONTROL',
 'beta':a.beta,
 'Mp':Mp,
 'm2_sq':m2_sq,
 'pole_k2':pole_k2,
 'pole_class':'TIMELIKE' if pole_k2<0 else 'NOT_TIMELIKE',
 'KL_required_s':required_s,
 'KL_physical_domain':'s>=0',
 'pole_inside_KL_physical_support':required_s>=0,
 'contrast_with_beta_positive_dIHO':True,
 'scope':'sign/control lane only; no branch unitarity conclusion'
}
with open(a.output,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
