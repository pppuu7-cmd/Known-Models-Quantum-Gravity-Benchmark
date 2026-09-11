#!/usr/bin/env python3
import argparse,json
p=argparse.ArgumentParser()
p.add_argument('--beta',type=float,required=True)
p.add_argument('--output',required=True)
a=p.parse_args()
assert a.beta>0
Mp=1.0
mu2_sq=Mp*Mp/a.beta
pole_k2=mu2_sq
required_s=-pole_k2
out={
 'iteration':366,
 'branch':'IHO_DQFT_SPACELIKE_PV',
 'beta':a.beta,
 'Mp':Mp,
 'mu2_sq':mu2_sq,
 'pole_k2':pole_k2,
 'pole_class':'SPACELIKE' if pole_k2>0 else 'NOT_SPACELIKE',
 'KL_required_s':required_s,
 'KL_physical_domain':'s>=0',
 'pole_inside_KL_physical_support':required_s>=0,
 'source_rho_zero_condition_supported':required_s<0,
 'scope':'algebraic spectral-support audit of the source pole relation; not an independent all-loop proof'
}
with open(a.output,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
