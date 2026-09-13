import argparse, json, math, os
import numpy as np

MS=(-1,0,1); RHOS=(0.35,1.60); BETAS=(0.80,2.10)
RADII=np.array([40.,80.,160.,320.,640.]); WIDTH=40.; N=4001

def dsrc(m,r,b):
    r=np.asarray(r,dtype=np.complex128); den=r+r**3
    if m==0:
        return -12*np.exp(2*b)*(((np.exp(2*b)-1)*r*np.cos(b*r)-(np.exp(2*b)+1)*np.sin(b*r)))/((np.exp(2*b)-1)**3*den)
    if m==-1:
        return 12*np.exp(3*b)*(-np.sin(b*r)+np.exp(1j*b*r)*r*np.sinh(b)*(np.cosh(b)-1j*r*np.sinh(b)))/((np.exp(2*b)-1)**3*den)
    return 6*np.exp(b*(3-1j*r))*(1j*(np.exp(2j*b*r)-r*r-1)+r*(1j*r*np.cosh(2*b)+np.sinh(2*b)))/((np.exp(2*b)-1)**3*den)

def poly1(x,r):
    z=np.ones_like(x,dtype=np.complex128)
    for n in range(3): z*= (1j*x-(n-1))/(1j*r-(n-1))
    return z

def poly2(x,r):
    return ((1j*x+1)*(1j*x)*(1j*x-1))/((1j*r+1)*(1j*r)*(1j*r-1))

def slope(rs,ys,k):
    rr=np.log(np.asarray(rs[-k:],float)); yy=np.log(np.asarray(ys[-k:],float))
    return float(np.polyfit(rr,yy,1)[0])

def window(R,side):
    if side=='positive': return np.linspace(R,R+WIDTH,N)
    return np.linspace(-R-WIDTH,-R,N)

def one(m,rho,beta,side):
    fenv=[]; denv=[]; penv=[]; polyerr=0.; finite=True
    for R in RADII:
        x=window(R,side)
        p1=poly1(x,rho); p2=poly2(x,rho); d=dsrc(m,x,beta); f=p2*d
        rel=np.max(np.abs(p1-p2)/np.maximum(1.0,np.abs(p2)))
        polyerr=max(polyerr,float(rel))
        finite &= bool(np.all(np.isfinite(f.real)) and np.all(np.isfinite(f.imag)) and np.all(np.isfinite(d.real)) and np.all(np.isfinite(d.imag)))
        fenv.append(float(np.max(np.abs(f)))); denv.append(float(np.max(np.abs(d)))); penv.append(float(np.max(np.abs(p2))))
    sf3,sf4=slope(RADII,fenv,3),slope(RADII,fenv,4)
    sd3,sd4=slope(RADII,denv,3),slope(RADII,denv,4)
    sp3,sp4=slope(RADII,penv,3),slope(RADII,penv,4)
    stable=abs(sf3-sf4)<=0.20
    if sf4 <= -1.05: tail_class='ABSOLUTE_ENVELOPE_DECAY_CANDIDATE'
    elif sf4 < 0: tail_class='DECAYING_NON_L1_ENVELOPE_CANDIDATE'
    else: tail_class='POLYNOMIAL_GROWTH_OR_BOUNDED_OSCILLATORY_ENVELOPE'
    return {'m':m,'rho':rho,'beta':beta,'side':side,'radii':RADII.tolist(),'F_envelope':fenv,'d_envelope':denv,'P11_envelope':penv,
            'F_slope_last3':sf3,'F_slope_last4':sf4,'d_slope_last3':sd3,'d_slope_last4':sd4,'P11_slope_last3':sp3,'P11_slope_last4':sp4,
            'tail_power_stability_abs':abs(sf3-sf4),'poly_route_relative_error_max':polyerr,'tail_class':tail_class,
            'finite':finite,'pass':finite and polyerr<=1e-12 and stable}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default='iter460_summary.json'); a=ap.parse_args()
    records=[one(m,r,b,s) for m in MS for r in RHOS for b in BETAS for s in ('positive','negative')]
    ok=all(q['pass'] for q in records)
    out={'iteration':460,'records':records,'n_records':len(records),'pass_records':sum(q['pass'] for q in records),
         'max_poly_route_relative_error':max(q['poly_route_relative_error_max'] for q in records),
         'max_tail_power_stability_abs':max(q['tail_power_stability_abs'] for q in records),
         'classification':'ITER460_SOURCE_P11_D_TAIL_CHARACTERIZED_SCOPED' if ok else 'SCIENTIFIC_FAIL_ITER460_SOURCE_TAIL_MODEL',
         'pass':ok,'scope':'Tail characterization only; no physical vertex convergence/divergence theorem; D7-S2 remains open; Candidate Gravity inactive.'}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True); json.dump(out,open(a.out,'w'),indent=2); print(json.dumps(out,indent=2))
if __name__=='__main__': main()
