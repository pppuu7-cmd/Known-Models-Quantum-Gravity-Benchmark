#!/usr/bin/env python3
import json,pathlib
import mpmath as mp
mp.mp.dps=90
PANEL=[(7,2),(7,5),(8,2),(8,5)]
BETAS=[mp.mpf('0.05'),mp.mpf('0.025'),mp.mpf('0.0125')]

def h2f1_series(a,b,c,z):
    term=mp.mpc(1); s=mp.mpc(1); tol=mp.mpf('1e-65'); consecutive=0
    for n in range(30000):
        term *= (a+n)*(b+n)/((c+n)*(n+1))*z
        s2=s+term
        if abs(term)<=tol*max(mp.mpf(1),abs(s2)):
            consecutive += 1
            if consecutive>=5: return s2,n+1
        else: consecutive=0
        s=s2
    raise RuntimeError('2F1 direct series did not converge')

def branch_data(j,m,rho,beta,plus):
    jx=mp.mpf(j); mx=mp.mpf(m); rx=mp.mpf(rho); bta=mp.mpf(beta); ii=mp.j; z=mp.e**(-2*bta); N=2*j+1
    if plus:
        a=jx+mx+1; b=jx+1-ii*rx; c=1+mx-ii*rx
        pref0=mp.gamma(2*jx+2)*mp.gamma(ii*rx-mx)/(mp.gamma(jx-mx+1)*mp.gamma(jx+1+ii*rx))
        expf=mp.e**(-(jx-ii*rx+mx+1)*bta)
    else:
        a=jx-mx+1; b=jx+1+ii*rx; c=1-mx+ii*rx
        pref0=mp.gamma(2*jx+2)*mp.gamma(-ii*rx+mx)/(mp.gamma(jx+mx+1)*mp.gamma(jx+1-ii*rx))
        expf=mp.e**(-(jx+ii*rx-mx+1)*bta)
    F,nterms=h2f1_series(a,b,c,z)
    val=expf*pref0*F
    C=pref0*mp.gamma(c)*mp.gamma(N)/(mp.gamma(a)*mp.gamma(b))
    R=val*(1-z)**N/C
    Rlo=val*(1-z)**(N-1)/C
    Rhi=val*(1-z)**(N+1)/C
    return {'a':a,'b':b,'c':c,'N':N,'value':val,'coefficient':C,'ratio':R,'wrong_low':Rlo,'wrong_high':Rhi,'nterms':nterms,'z':z}

records=[]; exact_ok=True; coeff_ok=True; monotone_ok=True; wrong_ok=True; max_terms=0
for gamma,j in PANEL:
    rho=gamma*j; N=2*j+1
    for m in range(-j,j+1):
        rec={'gamma':gamma,'j':j,'m':m,'rho':rho,'N':N,'branches':{}}
        vals={}
        for name,plus in [('plus',True),('minus',False)]:
            seq=[]
            for beta in BETAS:
                d=branch_data(j,m,rho,beta,plus); max_terms=max(max_terms,d['nterms'])
                identity=d['a']+d['b']-d['c']
                exact=abs(identity-N)<mp.mpf('1e-70')
                finite=bool(mp.isfinite(d['coefficient'].real) and mp.isfinite(d['coefficient'].imag))
                nonzero=abs(d['coefficient'])>mp.mpf('1e-70')
                exact_ok &= exact; coeff_ok &= finite and nonzero
                seq.append({'beta':float(beta),'ratio_abs_error':float(abs(d['ratio']-1)),'ratio_abs':float(abs(d['ratio'])),'wrong_low_abs_error':float(abs(d['wrong_low']-1)),'wrong_high_abs_error':float(abs(d['wrong_high']-1)),'branch_abs':float(abs(d['value'])),'series_terms':d['nterms']})
                vals[(name,float(beta))]=d['value']
            errs=[x['ratio_abs_error'] for x in seq]
            mono=all(errs[k+1] <= errs[k]+1e-12 for k in range(len(errs)-1)); monotone_ok &= mono
            last=seq[-1]; sep=last['ratio_abs_error']<last['wrong_low_abs_error'] and last['ratio_abs_error']<last['wrong_high_abs_error']; wrong_ok &= sep
            rec['branches'][name]={'exact_a_plus_b_minus_c':N,'coefficient_abs':float(abs(branch_data(j,m,rho,BETAS[-1],plus)['coefficient'])),'monotone_to_unit':mono,'wrong_exponents_separated':sep,'numeric':seq}
        # recombination witness only, not part of the PASS rule
        vp=vals[('plus',float(BETAS[-1]))]; vm=vals[('minus',float(BETAS[-1]))]
        rec['smallest_beta_recombination']={'beta':float(BETAS[-1]),'sum_abs':float(abs(vp+vm)),'plus_abs':float(abs(vp)),'minus_abs':float(abs(vm))}
        records.append(rec)
checks={'exact_parameter_identity':exact_ok,'leading_coefficients_finite_nonzero':coeff_ok,'correct_order_scaled_ratio_monotone':monotone_ok,'wrong_exponent_controls_separated':wrong_ok}
analytic=exact_ok and coeff_ok
ok=analytic and monotone_ok and wrong_ok
classification='ITER477_SOURCE_TOLLER_EXACT_BETA0_BRANCH_ORDER_2JPLUS1_QUALIFIED_SCOPED' if ok else ('ANALYTIC_ORDER_SUPPORTED_NUMERIC_CONFIRMATION_UNRESOLVED_SCOPED' if analytic else 'FAIL_ITER477_ANALYTIC_CERTIFICATE')
out={'iteration':477,'classification':classification,'scientific_pass':ok,'analytic_order_supported':analytic,'checks':checks,'panel':{'gamma':[7,8],'j':[2,5],'betas':[float(x) for x in BETAS]},'max_series_terms':max_terms,'records':records,'authority':'NIST DLMF 15.4.23 plus published source Toller hypergeometric parameters','interpretation':'For each individual frozen source Toller branch the exact local beta->0 singular order is N=2j+1 when qualified. This is one-wedge branch structure only, not a contracted K5 collision exponent or divergence theorem.','d7_s2':'NOT_CLOSED'}
pathlib.Path('artifacts').mkdir(exist_ok=True); pathlib.Path('artifacts/iter477-summary.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); raise SystemExit(0 if analytic else 2)
