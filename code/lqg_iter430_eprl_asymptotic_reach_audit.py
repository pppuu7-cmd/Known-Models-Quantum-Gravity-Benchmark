#!/usr/bin/env python3
"""Iter430: strict asymptotic-reach audit following Iter429.

Does not relax Iter429's 2e-5 terminal scaled-limit gate. It extends the
fixed-area trajectory and tests the perturbative O(1/j) approach expected from
(H_eps + A K/j)^-1. Passing means the controlled fixture reaches the original
gate with the predicted tail law; D7 remains open.
"""
import argparse, json, math, os
import numpy as np

N_REST=44
THRESH=2.0e-5

def orthogonal(rng,n):
    q,r=np.linalg.qr(rng.normal(size=(n,n))); d=np.sign(np.diag(r)); d[d==0]=1.0
    return q@np.diag(d)

def make_core(rng,cond_exp,imag_strength):
    q=orthogonal(rng,N_REST); eig=np.geomspace(1.0,10.0**(-cond_exp),N_REST)
    real=q@np.diag(eig)@q.T
    s=rng.normal(size=(N_REST,N_REST)); s=.5*(s+s.T); s/=max(float(np.linalg.norm(s,ord=2)),1e-300)
    h=-(real+1j*imag_strength*math.sqrt(float(eig[-1]))*s)
    k=rng.normal(size=(N_REST,N_REST))+1j*rng.normal(size=(N_REST,N_REST)); k=.5*(k+k.T); k/=max(float(np.linalg.norm(k,ord=2)),1e-300)
    return h,k

def slope(xs,ys):
    return float(np.polyfit(np.log(np.asarray(xs,float)),np.log(np.asarray(ys,float)),1)[0])

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,required=True); a=ap.parse_args(); idx=a.index
    if not 0<=idx<24: raise SystemExit('index must be 0..23')
    areas=[.25,.5,1.,2.]; conds=[1,2,4]; corrs=[.03,.10]
    area=areas[idx%4]; cond=conds[(idx//4)%3]; corr=corrs[(idx//12)%2]; imag=[.03,.10,.25][(idx//2)%3]
    rng=np.random.default_rng(429000+idx); h,k=make_core(rng,cond,imag); k*=corr
    v=rng.normal(size=N_REST)+1j*rng.normal(size=N_REST); v/=max(float(np.linalg.norm(v)),1e-300)
    hinv=np.linalg.inv(h); target=complex(v.T@hinv@v)
    if abs(target)<1e-10: raise SystemExit('fixture target accidentally near zero')
    js=np.asarray([1e4,3e4,1e5,3e5,1e6,3e6,1e7,3e7,1e8],float)
    errs=[]; inv_errs=[]; rest=[]; scaled=[]
    for j in js:
        gamma=area/j; hr=j*(h+gamma*k); hi=np.linalg.inv(hr); lead=hinv/j
        inv_errs.append(float(np.linalg.norm(hi-lead,ord='fro')/max(np.linalg.norm(lead,ord='fro'),1e-300)))
        d=(gamma**2)*(j**2)*v; g=complex(d.T@hi@d); rest.append(abs(g)); z=complex((j/(area**4))*g); scaled.append(z); errs.append(float(abs(z-target)/abs(target)))
    tail=slice(-5,None); err_tail=slope(js[tail],np.asarray(errs)[tail]); inv_tail=slope(js[tail],np.asarray(inv_errs)[tail]); rest_tail=slope(js[tail],np.asarray(rest)[tail])
    monotone=bool(all(errs[i+1] < errs[i] for i in range(len(errs)-4,len(errs)-1)))
    crossed=[float(j) for j,e in zip(js,errs) if e<THRESH]; first_cross=min(crossed) if crossed else None
    # O(1/j) predicts j*error approximately constant on the asymptotic tail.
    scaled_err=(js*np.asarray(errs)); plateau_rel=float((np.max(scaled_err[-4:])-np.min(scaled_err[-4:]))/max(np.median(scaled_err[-4:]),1e-300))
    source=(area/js)**4*js**3; algebra=(area**4)/js; identity=float(np.max(np.abs(source-algebra)/np.maximum(np.abs(algebra),1e-300)))
    # Same negative control as Iter429.
    bad=[]
    for j in js:
        gamma=area/j; d=(gamma**2)*(j**2)*v; bad.append(abs(complex(d.T@np.linalg.inv(h+gamma*k)@d)))
    bad_slope=slope(js[tail],np.asarray(bad)[tail]); neg=bool(abs(bad_slope+1)>0.5 and abs(bad_slope)<0.15)
    passed=bool(errs[-1] < THRESH and first_cross is not None and -.20 < err_tail+1.0 < .20 and abs(inv_tail+1)<.15 and abs(rest_tail+1)<.035 and monotone and plateau_rel<.20 and identity<5e-14 and neg)
    out={'iteration':430,'profile_index':idx,'fixed_area':area,'condition_exponent':cond,'correction_strength':corr,'imag_strength':imag,'j_grid':js.tolist(),'scaled_limit_relative_errors':errs,'first_j_below_original_2e-5_gate':first_cross,'final_scaled_limit_relative_error':errs[-1],'tail_scaled_error_log_slope':err_tail,'tail_inverse_error_log_slope':inv_tail,'tail_rest_log_slope':rest_tail,'j_times_error_tail_relative_spread':plateau_rel,'tail_error_monotone':monotone,'source_scaling_identity_relative_error':identity,'negative_control_log_slope':bad_slope,'negative_control_detected':neg,'numerical_pass':passed,'classification':'PASS_FINITE_ASYMPTOTIC_REACH_CLOSURE' if passed else 'FAIL_FINITE_ASYMPTOTIC_REACH_CLOSURE','original_gate_unchanged':THRESH,'d7_status':'OPEN','scope_guard':'Controlled 44D EPRL asymptotic fixture only. Passing resolves Iter429 finite-reach failure without relaxing its gate; it does not provide physical H^epsilon entries, causal measure transport, boundary alpha, or authorize Candidate Gravity / terminal D7 classification.'}
    os.makedirs('build/lqg-iter430',exist_ok=True); p=f'build/lqg-iter430/profile_{idx}.json'; open(p,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
    if not passed: raise SystemExit(2)
if __name__=='__main__': main()
