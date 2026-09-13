import argparse, json, os
import mpmath as mp

mp.mp.dps = 80

BETAS=(mp.mpf('0.8'),mp.mpf('2.1'))
RHOS=(mp.mpf('0.35'),mp.mpf('1.6'))
XS=(mp.mpf('-7.3'),mp.mpf('-2.4'),mp.mpf('-0.7'),mp.mpf('0.45'),mp.mpf('1.9'),mp.mpf('5.6'),mp.mpf('11.2'))
EPS=(mp.mpf('0.2'),mp.mpf('0.1'),mp.mpf('0.05'),mp.mpf('0.025'))


def denrho(rho):
    i=mp.j
    return (i*rho+1)*(i*rho)*(i*rho-1)


def p11(x,rho):
    i=mp.j
    return ((i*x+1)*(i*x)*(i*x-1))/denrho(rho)


def dsrc(m,x,b):
    i=mp.j; e2=mp.e**(2*b); den=x+x**3; q=(e2-1)**3
    if m==0:
        return -12*e2*((e2-1)*x*mp.cos(b*x)-(e2+1)*mp.sin(b*x))/(q*den)
    if m==-1:
        return 12*mp.e**(3*b)*(-mp.sin(b*x)+mp.e**(i*b*x)*x*mp.sinh(b)*(mp.cosh(b)-i*x*mp.sinh(b)))/(q*den)
    return 6*mp.e**(b*(3-i*x))*(i*(mp.e**(2*i*b*x)-x*x-1)+x*(i*x*mp.cosh(2*b)+mp.sinh(2*b)))/(q*den)


def channels(m,b,rho):
    i=mp.j; D=denrho(rho); q=(mp.e**(2*b)-1)**3
    out={-1:{},1:{}}
    if m==0:
        A=mp.e**(2*b)-1; B=mp.e**(2*b)+1
        K=12*i*mp.e**(2*b)/(q*D)
        out[1]={1:K*A/2,0:K*i*B/2}
        out[-1]={1:K*A/2,0:-K*i*B/2}
    elif m==-1:
        S=mp.sinh(b); C=mp.cosh(b); K=-12*i*mp.e**(3*b)/(q*D)
        out[1]={0:K*i/2,1:K*S*C,2:K*(-i*S*S)}
        out[-1]={0:K*(-i/2)}
    else:
        S2=mp.sinh(2*b); C2=mp.cosh(2*b); K=-6*i*mp.e**(3*b)/(q*D)
        out[1]={0:K*i}
        out[-1]={0:K*(-i),1:K*S2,2:K*i*(C2-1)}
    return out


def reconstruct(m,x,b,rho):
    c=channels(m,b,rho); s=mp.mpc('0')
    for sig,terms in c.items():
        poly=sum(v*x**n for n,v in terms.items())
        s += poly*mp.e**(mp.j*sig*b*x)
    return s


def boundary_from_selector(m,b,rho,s):
    c=channels(m,b,rho)[s]
    poly=sum(v*rho**n for n,v in c.items())
    return 2*mp.pi*mp.j*s*mp.e**(mp.j*s*b*rho)*poly


def boundary_from_plemelj(m,b,rho,s):
    total=mp.mpc('0')
    for sig,terms in channels(m,b,rho).items():
        ksign=mp.mpf(sig)
        # PV Fourier boundary away from k=0 plus i*s*pi*delta term.
        factor=mp.j*mp.pi*(ksign+s)*mp.e**(mp.j*sig*b*rho)
        poly=sum(v*rho**n for n,v in terms.items())
        total += factor*poly
    return total


def finite_eps(m,b,rho,s,eps):
    z=rho+mp.j*s*eps
    terms=channels(m,b,rho)[s]
    poly=sum(v*z**n for n,v in terms.items())
    return 2*mp.pi*mp.j*s*mp.e**(mp.j*s*b*z)*poly


def rel(a,b):
    return abs(a-b)/max(mp.mpf('1e-70'),abs(a),abs(b))


def fstr(x):
    return mp.nstr(x,30)


def lane(m,beta):
    records=[]; ok=True
    for rho in RHOS:
        # exact cancellation tested numerically at high precision on held-out x; algebraic identity is direct.
        cancel_err=mp.mpf('0'); recon_err=mp.mpf('0')
        exact_const=-mp.j/denrho(rho)
        for x in XS:
            cancel_err=max(cancel_err,rel(p11(x,rho)/(x+x**3),exact_const))
            direct=p11(x,rho)*dsrc(m,x,beta)
            recon=reconstruct(m,x,beta,rho)
            recon_err=max(recon_err,rel(direct,recon))
        for s in (-1,1):
            sel=boundary_from_selector(m,beta,rho,s)
            plem=boundary_from_plemelj(m,beta,rho,s)
            plem_err=rel(sel,plem)
            ferr=[rel(finite_eps(m,beta,rho,s,e),sel) for e in EPS]
            mono=(ferr[1] <= ferr[0] and ferr[2] <= ferr[1] and ferr[3] <= ferr[2])
            wrong=boundary_from_selector(m,beta,rho,-s)
            wrong_diff=rel(sel,wrong)
            finite=all(mp.isfinite(z.real) and mp.isfinite(z.imag) for z in [sel,plem,wrong]+[finite_eps(m,beta,rho,s,e) for e in EPS])
            passed=(cancel_err <= mp.mpf('1e-40') and recon_err <= mp.mpf('1e-40') and plem_err <= mp.mpf('1e-40') and mono and ferr[-1] <= mp.mpf('0.12') and wrong_diff >= mp.mpf('1e-3') and finite)
            ok &= bool(passed)
            records.append({
                'm':m,'beta':fstr(beta),'rho':fstr(rho),'boundary_sign_s':s,
                'p11_denominator_cancellation_relative_error':fstr(cancel_err),
                'direct_vs_channel_relative_error_max':fstr(recon_err),
                'plemelj_vs_selector_relative_error':fstr(plem_err),
                'finite_epsilon_relative_errors':[fstr(x) for x in ferr],
                'finite_epsilon_last3_monotone':bool(mono),
                'wrong_boundary_sign_relative_difference':fstr(wrong_diff),
                'selector_value_real':fstr(sel.real),'selector_value_imag':fstr(sel.imag),
                'finite':bool(finite),'pass':bool(passed)
            })
    return {'iteration':464,'m':m,'beta':fstr(beta),'records':records,'pass':bool(ok),
            'classification':'ITER464_SOURCE_P11_D_DISTRIBUTIONAL_PAIRING_QUALIFIED_SCOPED' if ok else 'SCIENTIFIC_FAIL_ITER464_SOURCE_DISTRIBUTIONAL_PAIRING',
            'scope':'Exact one-dimensional source P11*d_source/Feynman-kernel distributional pairing only; no full causal-vertex convergence theorem; D7-S2 remains open pending multivariable/pullback closure.'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--m',type=int,required=True); ap.add_argument('--beta',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    out=lane(a.m,mp.mpf(a.beta)); os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2)); raise SystemExit(0 if out['pass'] else 1)

if __name__=='__main__': main()
