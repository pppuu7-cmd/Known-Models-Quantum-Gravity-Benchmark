#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path

# Source: Dekhil, Greco, Liberati, Oriti, arXiv:2608.12003v1,
# Eqs. (24),(28),(29),(32), in the early-time Q≈q I approximation.
# Let S=2 theta_dot-gamma. Source definitions give
# A=1+q S^2, D=-alpha_i q S, E=-alpha_i^2 q,
# f2=D/A, f4=E/A. With x=k^2, Eq.(32) has
# Gamma=f2*x-f1 and a radicand whose x^2 coefficient is f2^2+4 f4.
# Exact identity: f2^2+4f4 = -alpha_i^2*q*(3A+1)/A^2.
# For alpha_i*q !=0, f2 and this x^2 coefficient cannot vanish together.

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--alpha',type=float,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    alpha=float(a.alpha)
    if alpha==0: raise ValueError('coupled audit requires alpha_i != 0')
    qs=[-2.0,-0.5,0.25,1.0,3.0]
    Ss=[0.0,0.2,1.0,3.0]
    rows=[]; min_joint=math.inf; max_identity=0.0
    for q in qs:
      for S in Ss:
        A=1.0+q*S*S
        if abs(A)<0.08:  # exclude the coefficient singular surface A=0; not a physical prior
            continue
        D=-alpha*q*S; E=-(alpha**2)*q
        f2=D/A; f4=E/A
        quad=f2*f2+4.0*f4
        identity=-(alpha**2)*q*(3.0*A+1.0)/(A*A)
        resid=abs(quad-identity)/(1.0+abs(identity)); max_identity=max(max_identity,resid)
        joint=math.hypot(f2,quad); min_joint=min(min_joint,joint)
        assert joint>1e-12,(alpha,q,S,A,f2,quad)
        assert resid<1e-13,(alpha,q,S,resid)
        rows.append({'q':q,'S':S,'A':A,'f2':f2,'f4':f4,'radicand_x2_coefficient':quad,'identity_value':identity,'joint_nonstandard_norm':joint})
    out={'iteration':353,'alpha_i':alpha,'case_count':len(rows),'minimum_joint_nonstandard_norm':min_joint,'maximum_identity_scaled_residual':max_identity,'classification':'PASS_SCOPED_GFT_COUPLED_DISPERSION_FUNCTIONAL_RIGIDITY__SOURCE_RELATIONS_FORBID_SIMULTANEOUSLY_K_INDEPENDENT_DAMPING_AND_AFFINE_K2_RADICAND_WHEN_ALPHA_I_Q_IS_NONZERO','source':'arXiv:2608.12003v1 Eqs. (24),(28),(29),(32)','exact_identity':'f2^2+4*f4 = -alpha_i^2*q*(3*A+1)/A^2 with A=1+q*S^2','scope_guard':['ALGEBRAIC_COEFFICIENT_STRESS_NOT_PHYSICAL_PRIOR','EARLY_TIME_Q_APPROX_Q_IDENTITY','EXCLUDES_A_ZERO_SINGULAR_SURFACE','EMERGENT_MATTER_PROPAGATION_IN_GFT_CONDENSATE_COSMOLOGY_ONLY','NOT_FULL_GRAVITY_OBSERVABLE','NO_PARENT_FAMILY_TERMINALIZATION','NO_D7_PROMOTION'],'rows':rows}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='rows'},sort_keys=True))
if __name__=='__main__': main()
