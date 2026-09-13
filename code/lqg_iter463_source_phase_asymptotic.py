import argparse, json, math, os
import numpy as np

RHOS=(0.35,1.60)
RADII=np.array([80.,160.,320.,640.,1280.])


def dsrc(m,r,b):
    r=np.asarray(r,dtype=np.complex128); den=r+r**3
    if m==0:
        return -12*np.exp(2*b)*(((np.exp(2*b)-1)*r*np.cos(b*r)-(np.exp(2*b)+1)*np.sin(b*r)))/((np.exp(2*b)-1)**3*den)
    if m==-1:
        return 12*np.exp(3*b)*(-np.sin(b*r)+np.exp(1j*b*r)*r*np.sinh(b)*(np.cosh(b)-1j*r*np.sinh(b)))/((np.exp(2*b)-1)**3*den)
    return 6*np.exp(b*(3-1j*r))*(1j*(np.exp(2j*b*r)-r*r-1)+r*(1j*r*np.cosh(2*b)+np.sinh(2*b)))/((np.exp(2*b)-1)**3*den)


def p11a(x,rho):
    z=np.ones_like(x,dtype=np.complex128)
    for n in range(3):
        z *= (1j*x-(n-1))/(1j*rho-(n-1))
    return z


def p11b(x,rho):
    return ((1j*x+1)*(1j*x)*(1j*x-1))/((1j*rho+1)*(1j*rho)*(1j*rho-1))


def wrap(a):
    return (a+np.pi)%(2*np.pi)-np.pi


def local_window(R,beta,side,n=1201):
    width=4*np.pi/beta
    if side=='positive':
        return np.linspace(R,R+width,n)
    return np.linspace(-R-width,-R,n)


def rms(z):
    return float(np.sqrt(np.mean(np.abs(z)**2)))


def lane(m,beta,rho,side):
    p=1 if m==0 else 2
    scaled_rms=[]; wrong_scaled_rms=[]; polyerr=0.0; finite=True
    phase_errors=[]; wrong_phase_errors=[]
    h=0.15/beta
    for R in RADII:
        x=local_window(R,beta,side)
        pa=p11a(x,rho); pb=p11b(x,rho); f=pb*dsrc(m,x,beta)
        polyerr=max(polyerr,float(np.max(np.abs(pa-pb)/np.maximum(1.0,np.abs(pb)))))
        finite &= bool(np.all(np.isfinite(f.real)) and np.all(np.isfinite(f.imag)))
        q=f/(x**p)
        scaled_rms.append(rms(q))
        wrong_scaled_rms.append(rms(f/(x**(p-1))))
        # Local phase diagnostic.  For m=+/-1 the leading channel is single-frequency;
        # for m=0 the leading pair +/- beta obeys the exact cosine recurrence.
        xm=x[100:-100]
        if m!=0:
            s=1.0 if m==-1 else -1.0
            fm=p11b(xm,rho)*dsrc(m,xm,beta)/(xm**p)
            fp=p11b(xm+h,rho)*dsrc(m,xm+h,beta)/((xm+h)**p)
            ratio=np.vdot(fm,fp)/np.vdot(fm,fm)
            phase_errors.append(abs(float(wrap(np.angle(ratio)-s*beta*h))))
            wrong_phase_errors.append(abs(float(wrap(np.angle(ratio)+s*beta*h))))
        else:
            f0=p11b(xm,rho)*dsrc(0,xm,beta)/xm
            fp=p11b(xm+h,rho)*dsrc(0,xm+h,beta)/(xm+h)
            fn=p11b(xm-h,rho)*dsrc(0,xm-h,beta)/(xm-h)
            denom=np.vdot(f0,f0)
            c=float(np.real(np.vdot(f0,0.5*(fp+fn))/denom))
            c=max(-1.0,min(1.0,c))
            inferred=math.acos(c)
            phase_errors.append(abs(inferred-beta*h))
            wrong_phase_errors.append(abs(inferred-1.35*beta*h))
    mag_dev=abs(scaled_rms[-1]/scaled_rms[-2]-1.0)
    wrong_ratio=wrong_scaled_rms[-1]/wrong_scaled_rms[-2]
    max_phase=max(phase_errors[-2:])
    mean_wrong=float(np.mean(wrong_phase_errors[-2:]))
    passed=(finite and polyerr<=1e-12 and mag_dev<=0.15 and max_phase<=0.08 and wrong_ratio>=1.35 and mean_wrong>=0.20)
    return {
        'm':m,'beta':beta,'rho':rho,'side':side,'leading_power':p,
        'radii':RADII.tolist(),'scaled_rms':scaled_rms,'wrong_power_scaled_rms':wrong_scaled_rms,
        'scaled_last_ratio_fractional_deviation':mag_dev,'wrong_power_last_ratio':wrong_ratio,
        'phase_errors_rad':phase_errors,'wrong_phase_errors_rad':wrong_phase_errors,
        'max_last2_phase_error_rad':max_phase,'mean_last2_wrong_phase_error_rad':mean_wrong,
        'p11_route_relative_error_max':polyerr,'finite':finite,'pass':passed
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--m',type=int,required=True); ap.add_argument('--beta',type=float,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    records=[lane(a.m,a.beta,r,s) for r in RHOS for s in ('positive','negative')]
    ok=all(r['pass'] for r in records)
    out={
      'iteration':463,'m':a.m,'beta':a.beta,'records':records,'n_records':len(records),'pass_records':sum(r['pass'] for r in records),
      'classification':'ITER463_SOURCE_P11_D_LEADING_OSCILLATORY_ASYMPTOTICS_QUALIFIED_SCOPED' if ok else 'SCIENTIFIC_FAIL_ITER463_SOURCE_PHASE_ASYMPTOTIC_MODEL',
      'pass':ok,
      'scope':'Source-tail leading powers/phases only; no causal-vertex convergence/divergence theorem; D7-S2 remains open; Candidate Gravity inactive.'
    }
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))
    raise SystemExit(0 if ok else 1)

if __name__=='__main__': main()
