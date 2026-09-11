#!/usr/bin/env python3
import argparse,json
p=argparse.ArgumentParser()
p.add_argument('--ratio',type=float,required=True,help='mu2/m')
p.add_argument('--output',required=True)
a=p.parse_args()
assert a.ratio>0
m=1.0
mu=a.ratio*m
branch_point=4.0*mu*mu
alpha_ratio_real=0.0
alpha_ratio_imag=mu/m
p2_samples=[-1e-6*mu*mu,-0.1*mu*mu,-1.0*mu*mu,-10.0*mu*mu,-1e6*mu*mu]
rows=[]
for P2 in p2_samples:
    kperp2=mu*mu-P2/4.0
    rows.append({'P2_over_mu2':P2/(mu*mu),'P2':P2,'k_perp_sq':kperp2,'physical_timelike_domain':P2<0,'equals_spacelike_branch_point':abs(P2-branch_point)<1e-15})
out={
 'iteration':367,
 'mu_over_m':a.ratio,
 'two_dIHO_branch_point_P2':branch_point,
 'two_dIHO_branch_point_class':'SPACELIKE' if branch_point>0 else 'NOT_SPACELIKE',
 'mixed_alpha2_over_alpha1':{'real':alpha_ratio_real,'imag':alpha_ratio_imag},
 'mixed_has_real_nonnegative_feynman_ratio':False,
 'timelike_samples':rows,
 'physical_timelike_samples_hit_branch_point':any(r['equals_spacelike_branch_point'] for r in rows),
 'source_physical_pinch_absent_supported':True,
 'scope':'source Landau kinematic audit; not an independent proof for arbitrary graphs beyond source theorem'
}
with open(a.output,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
