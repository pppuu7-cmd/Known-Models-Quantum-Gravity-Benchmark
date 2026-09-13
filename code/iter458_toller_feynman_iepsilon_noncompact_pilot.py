import argparse,json,math,os
import numpy as np

RHOS=(0.35,1.60); BETAS=(0.80,2.10); EPS=(0.20,0.08,0.032,0.0128); RS=(50.,100.,200.,400.); H=0.0125

def dsrc(m,r,b):
    r=np.asarray(r,dtype=np.complex128); den=r+r**3
    if m==0:
        return -12*np.exp(2*b)*(((np.exp(2*b)-1)*r*np.cos(b*r)-(np.exp(2*b)+1)*np.sin(b*r)))/((np.exp(2*b)-1)**3*den)
    if m==-1:
        return 12*np.exp(3*b)*(-np.sin(b*r)+np.exp(1j*b*r)*r*np.sinh(b)*(np.cosh(b)-1j*r*np.sinh(b)))/((np.exp(2*b)-1)**3*den)
    return 6*np.exp(b*(3-1j*r))*(1j*(np.exp(2j*b*r)-r*r-1)+r*(1j*r*np.cosh(2*b)+np.sinh(2*b)))/((np.exp(2*b)-1)**3*den)

def branches(m,r,b):
    den=r+r**3; cs=1/np.sinh(b); ct=np.cosh(b)/np.sinh(b)
    if m==0:
        tp=-3*np.exp(1j*b*r)*(r+1j*ct)*cs**2/(2*den); tm=-3*np.exp(-1j*b*r)*(r-1j*ct)*cs**2/(2*den)
    elif m==-1:
        tp=3*np.exp(1j*b*r)*cs**3*(1j*(1+r*r)+r*(np.sinh(2*b)-1j*r*np.cosh(2*b)))/(4*den); tm=-3j*np.exp(-1j*b*r)*cs**3/(4*den)
    else:
        tp=3j*np.exp(1j*b*r)*cs**3/(4*den); tm=3*cs**3*(1j*np.cos(b*r)+np.sin(b*r))*(-r*r+r*r*np.cosh(2*b)-1j*r*np.sinh(2*b)-1)/(4*den)
    return complex(tp),complex(tm)

def poly1(x,r):
    z=np.ones_like(x,dtype=np.complex128)
    for n in range(3): z*= (1j*x-(n-1))/(1j*r-(n-1))
    return z

def poly2(x,r):
    return ((1j*x+1)*(1j*x)*(1j*x-1))/((1j*r+1)*(1j*r)*(1j*r-1))

def kahan_complex(a):
    sr=cr=si=ci=0.0
    for z in a:
        y=z.real-cr; t=sr+y; cr=(t-sr)-y; sr=t
        y=z.imag-ci; t=si+y; ci=(t-si)-y; si=t
    return complex(sr,si)

def integ(m,r,b,eps,R,sgn,wrong=False):
    n=int(round(2*R/H)); x=-R+(np.arange(n,dtype=np.float64)+0.5)*H
    p1=poly1(x,r); p2=poly2(x,r); poly_err=float(np.max(np.abs(p1-p2)))
    d=dsrc(m,x,b)
    # source: +/- /(rhot-rho \mp i eps). wrong control flips only denominator displacement.
    imsign=1 if sgn==1 else -1
    if wrong: imsign*=-1
    z=r+1j*imsign*eps
    a=(sgn*p1*d/(x-z)/(2j*np.pi))*H
    direct=complex(np.sum(a)); comp=kahan_complex(a)
    return direct,comp,poly_err

def normerr(a,b): return abs(a-b)/max(1.0,abs(b))

def lane(ms):
    rec=[]; polymax=0.; accummax=0.; allfinite=True; cauchy_ok=True; target_ok=True; add_ok=True; trend_ok=True; wrong_hits=wrong_total=0
    for m in ms:
      for rho in RHOS:
       for beta in BETAS:
        d0=complex(dsrc(m,np.array([rho]),beta)[0]); tp,tm=branches(m,rho,beta)
        errs={1:[], -1:[]}; vals={}
        for eps in EPS:
          vals[eps]={}
          for R in RS:
            vals[eps][R]={}
            for sgn,target in ((1,tp),(-1,tm)):
              v,c,pe=integ(m,rho,beta,eps,R,sgn); polymax=max(polymax,pe); accummax=max(accummax,abs(v-c)/max(1.,abs(c)))
              allfinite &= bool(np.isfinite(v.real) and np.isfinite(v.imag) and np.isfinite(c.real) and np.isfinite(c.imag))
              vals[eps][R][sgn]=c
          for sgn,target in ((1,tp),(-1,tm)):
            errs[sgn].append(normerr(vals[eps][400.][sgn],target))
            cauchy_ok &= normerr(vals[eps][400.][sgn],vals[eps][200.][sgn])<=0.02
        for sgn,target in ((1,tp),(-1,tm)):
          target_ok &= errs[sgn][-1] <= 0.05
          trend_ok &= errs[sgn][-1] <= errs[sgn][0] + 0.10
          w,_,_=integ(m,rho,beta,EPS[-1],400.,sgn,wrong=True); wrong_total+=1; wrong_hits += int(normerr(w,target)>0.05)
        add_err=normerr(vals[EPS[-1]][400.][1]+vals[EPS[-1]][400.][-1],d0); add_ok &= add_err<=0.05
        rec.append({'m':m,'rho':rho,'beta':beta,'plus_err_eps':errs[1],'minus_err_eps':errs[-1],'final_add_err':add_err,
                    'cauchy_plus':normerr(vals[EPS[-1]][400.][1],vals[EPS[-1]][200.][1]),'cauchy_minus':normerr(vals[EPS[-1]][400.][-1],vals[EPS[-1]][200.][-1])})
    tests={'source_poly_route_agreement':polymax<=1e-12,'finite_complete':allfinite,'accumulation_agreement':accummax<=2e-9,
           'final_window_cauchy':cauchy_ok,'closed_branch_target':target_ok,'additive_recovery':add_ok,
           'wrong_sign_negative':wrong_total>0 and wrong_hits/wrong_total>=0.75,'epsilon_trend':trend_ok}
    return {'tests':tests,'poly_route_max':polymax,'accumulation_relative_max':accummax,'wrong_sign_hit_fraction':wrong_hits/max(1,wrong_total),'records':rec,'valid':allfinite,'pass':all(tests.values())}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    mapping={'L0':[-1],'L1':[0],'L2':[1],'L3':[-1,0,1]}
    try:
      q=lane(mapping[a.lane]); q['lane']=a.lane; q['classification']='ITER458_TOLLER_FEYNMAN_IEPSILON_ORDINARY_TRUNCATION_SUPPORTED_SCOPED' if q['pass'] else 'SCIENTIFIC_FAIL_ITER458_TOLLER_FEYNMAN_IEPSILON_ORDINARY_TRUNCATION'
    except Exception as e:
      q={'lane':a.lane,'valid':False,'pass':False,'classification':'INFRASTRUCTURE_OR_NUMERICAL_FAIL','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True); json.dump(q,open(a.out,'w'),indent=2); print(json.dumps(q,indent=2))
if __name__=='__main__': main()
