#!/usr/bin/env python3
import json,math,pathlib
import mpmath as mp
BETAS=[mp.mpf('0.4'),mp.mpf('0.2'),mp.mpf('0.1'),mp.mpf('0.05'),mp.mpf('0.025'),mp.mpf('0.0125')]
PANEL=[(7,2),(7,5),(8,2),(8,5)]

def h2f1_series(a,b,c,z,dps):
    mp.mp.dps=dps
    term=mp.mpc(1); s=mp.mpc(1); tol=mp.power(10,-max(40,dps-20)); consecutive=0
    for n in range(200000):
        term *= (a+n)*(b+n)/((c+n)*(n+1))*z
        s2=s+term
        if abs(term) <= tol*max(mp.mpf(1),abs(s2)):
            consecutive += 1
            if consecutive>=5: return s2,n+1
        else: consecutive=0
        s=s2
    raise RuntimeError('direct 2F1 series did not converge')

def tvals(j,m,rho,beta,dps):
    mp.mp.dps=dps; jx=mp.mpf(j); mx=mp.mpf(m); rx=mp.mpf(rho); b=mp.mpf(beta); z=mp.e**(-2*b); ii=mp.j
    fp,np=h2f1_series(jx+mx+1,jx+1-ii*rx,1+mx-ii*rx,z,dps)
    fm,nm=h2f1_series(jx-mx+1,jx+1+ii*rx,1-mx+ii*rx,z,dps)
    tp=(mp.e**(-(jx-ii*rx+mx+1)*b)*mp.gamma(2*jx+2)*mp.gamma(ii*rx-mx)/(mp.gamma(jx-mx+1)*mp.gamma(jx+1+ii*rx))*fp)
    tm=(mp.e**(-(jx+ii*rx-mx+1)*b)*mp.gamma(2*jx+2)*mp.gamma(-ii*rx+mx)/(mp.gamma(jx+mx+1)*mp.gamma(jx+1-ii*rx))*fm)
    return tp,tm,max(np,nm)

def relerr(a,b):
    den=max(abs(b),mp.mpf('1e-100')); return abs(a-b)/den

def slope(xs,ys):
    x=[math.log(float(v)) for v in xs]; y=[math.log(float(v)) for v in ys]
    xm=sum(x)/len(x); ym=sum(y)/len(y); return sum((a-xm)*(b-ym) for a,b in zip(x,y))/sum((a-xm)**2 for a in x)

records=[]; precision_ok=True; stability_ok=True; neg_sep=False; finite=True; max_terms=0
for gamma,j in PANEL:
    rho=gamma*j
    for m in range(-j,j+1):
        routes={80:[],120:[]}
        for dps in (80,120):
            for b in BETAS:
                tp,tm,nterms=tvals(j,m,rho,b,dps); max_terms=max(max_terms,nterms); routes[dps].append((tp,tm,tp+tm,tp-tm))
        for i,b in enumerate(BETAS):
            for q in range(4):
                a=routes[80][i][q]; c=routes[120][i][q]
                finite &= bool(mp.isfinite(a.real) and mp.isfinite(a.imag) and mp.isfinite(c.real) and mp.isfinite(c.imag))
                if abs(c)>mp.mpf('1e-40'): precision_ok &= bool(relerr(a,c)<=mp.mpf('1e-18'))
                else: precision_ok &= bool(abs(a-c)<=mp.mpf('1e-40'))
            if abs(routes[120][i][2]-routes[120][i][3])>mp.mpf('1e-30'): neg_sep=True
        labels=('plus','minus','sum'); powers={}
        for q,label in enumerate(labels):
            mags=[abs(x[q]) for x in routes[120]]; nonneg=all(v>mp.mpf('1e-30') for v in mags[-4:])
            if nonneg:
                p4=-slope(BETAS[-4:],mags[-4:]); p3=-slope(BETAS[-3:],mags[-3:]); stab=abs(p4-p3); stability_ok &= stab<=0.35
                powers[label]={'power_last4':p4,'power_last3':p3,'stability':stab,'status':'CHARACTERIZED'}
            else: powers[label]={'status':'NEAR_ZERO_UNRESOLVED'}
        records.append({'gamma':gamma,'j':j,'m':m,'rho':rho,'powers':powers,'last_beta_magnitudes':{'plus':float(abs(routes[120][-1][0])),'minus':float(abs(routes[120][-1][1])),'sum':float(abs(routes[120][-1][2]))}})
checks={'all_finite':finite,'precision_agreement':precision_ok,'nested_power_stability':stability_ok,'wrong_recombination_separates':neg_sep}
ok=all(checks.values())
out={'iteration':474,'classification':'ITER474_SOURCE_TOLLER_BETA0_LOCAL_ASYMPTOTICS_CHARACTERIZED_SCOPED' if ok else 'UNRESOLVED_ITER474_ON_FROZEN_GRID','scientific_pass':ok,'checks':checks,'beta_grid':[float(x) for x in BETAS],'max_series_terms':max_terms,'records':records,'scope':'one-wedge source Toller beta->0 diagnostic only; direct 2F1 power series is the same source hypergeometric function for |z|<1; no contracted K5 exponent and no convergence/divergence theorem','d7_s2':'NOT_CLOSED'}
pathlib.Path('artifacts').mkdir(exist_ok=True); pathlib.Path('artifacts/iter474-summary.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); raise SystemExit(0 if ok else 2)
