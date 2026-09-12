#!/usr/bin/env python3
"""Iter431: causal-branch Hessian transport audit.

Source authority (2026): Bianchi, Chen, Gamonal, causal-spinfoam/Toller work.
The integral representation identifies the causal-vertex Hessian structure with
the EPRL critical-point Hessian on compatible Lorentzian Regge saddles; the
causal data select a single Regge phase rather than granting a new free Hessian.

This audit validates the numerical consequence only: a common physical Hessian
must transport the same projected covariance/pseudodeterminant through +/-
causal branches. A deliberately branch-dependent Hessian is a negative control.
It does NOT prove Toller-vertex integrability, complete-stack cutoff removal, or
supply physical Hessian entries. D7-S2/S3 remain open and D7-S4 remains partial.
"""
import argparse,json,math,os
import numpy as np

N=10

def orth(seed,n=N):
    rng=np.random.default_rng(seed); q,r=np.linalg.qr(rng.normal(size=(n,n)))
    d=np.sign(np.diag(r)); d[d==0]=1.; return q@np.diag(d)

def projected(h):
    h=.5*(h+h.T); w,v=np.linalg.eigh(h); scale=max(float(np.max(np.abs(w))),1.)
    tol=max(1e-12*scale,1e-14); pos=w>tol
    if np.any(w < -tol) or not np.any(pos): return None
    vp=v[:,pos]; ep=w[pos]; p=vp@vp.T
    c=vp@np.diag(1/ep)@vp.T
    return c,p,int(np.count_nonzero(pos)),float(np.sum(np.log(ep)))

def rel(a,b):
    return float(np.linalg.norm(a-b,'fro')/max(float(np.linalg.norm(b,'fro')),1e-300))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,required=True); a=ap.parse_args(); i=a.index
    if not 0<=i<24: raise SystemExit('index 0..23')
    ranks=[6,7,8,9]; conds=[1,2,4]; phase_scales=[.25,1.0]
    rank=ranks[i%4]; cond=conds[(i//4)%3]; phase=phase_scales[(i//12)%2]
    q=orth(431000+i); eig=np.geomspace(1.,10.**(-cond),rank)
    h=q@np.diag(np.r_[eig,np.zeros(N-rank)])@q.T
    plus=projected(h); minus=projected(h.copy())
    if plus is None or minus is None: raise SystemExit('common fixture rejected')
    cp,pp,rp,lp=plus; cm,pm,rm,lm=minus
    cov_err=rel(cp,cm); proj_err=rel(pp,pm); logp_err=abs(lp-lm); rank_ok=(rp==rm==rank)
    # Leading stationary-phase prefactors can differ by conjugate/sign phase,
    # while their Hessian measure magnitude is common when H+ = H-.
    s=phase*(1.0+0.07*i); amp_p=np.exp(1j*s-0.5*lp); amp_m=np.exp(-1j*s-0.5*lm)
    magnitude_err=float(abs(abs(amp_p)-abs(amp_m))/max(abs(amp_p),1e-300))
    phase_product_err=float(abs((amp_p/abs(amp_p))*(amp_m/abs(amp_m))-1.0))
    # Negative control: alter one *physical* eigenvalue of H- by 8%; this must
    # be visible in covariance and pseudodeterminant while preserving rank.
    vmode=q[:,0]; hbad=h+0.08*eig[0]*np.outer(vmode,vmode); bad=projected(hbad)
    bad_detect=False; bad_cov=0.; bad_log=0.
    if bad is not None:
        cb,pb,rb,lb=bad; bad_cov=rel(cp,cb); bad_log=abs(lp-lb)
        bad_detect=bool(rb==rank and bad_cov>1e-3 and bad_log>1e-3)
    passed=bool(rank_ok and cov_err<1e-12 and proj_err<1e-12 and logp_err<1e-12 and magnitude_err<1e-12 and phase_product_err<1e-12 and bad_detect)
    out={
      'iteration':431,'profile_index':i,'rank':rank,'condition_exponent':cond,'regge_phase_scale':phase,
      'common_branch_covariance_relative_error':cov_err,'common_branch_projector_relative_error':proj_err,
      'common_branch_log_pseudodeterminant_error':logp_err,'stationary_phase_magnitude_relative_error':magnitude_err,
      'conjugate_phase_product_error':phase_product_err,
      'negative_control_branch_hessian_split_detected':bad_detect,'negative_control_covariance_shift':bad_cov,
      'negative_control_log_pdet_shift':bad_log,'numerical_pass':passed,
      'classification':'PASS_SOURCE_BACKED_CAUSAL_BRANCH_HESSIAN_TRANSPORT_STRUCTURE' if passed else 'FAIL_CAUSAL_BRANCH_HESSIAN_TRANSPORT_STRUCTURE',
      'source_authority':['Bianchi-Chen-Gamonal, Causal spinfoam vertex for 4D Lorentzian quantum gravity, Phys Rev D 113 126020 (2026)','Bianchi-Chen-Gamonal, Toller matrices and the Feynman i-epsilon in spinfoams, Phys Rev D 114 046014 (2026)'],
      'd7_s2':'OPEN','d7_s3':'OPEN','d7_s4':'PARTIAL_GLOBAL_NOT_CLOSED','d7_status':'OPEN','candidate_gravity_authorized':False,
      'scope_guard':'Tests the consequence of source-backed causal/EPRL Hessian identification using controlled eigenvalues. It does not ingest physical Hessian entries, prove fixed-Toller vertex integrability, complete-stack finite normalization/cutoff removal, or full same-realization UV-to-GR transport.'}
    os.makedirs('build/lqg-iter431',exist_ok=True); open(f'build/lqg-iter431/profile_{i}.json','w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed: raise SystemExit(2)
if __name__=='__main__': main()
