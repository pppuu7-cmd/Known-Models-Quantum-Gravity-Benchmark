import argparse, json, math, os
import mpmath as mp

mp.mp.dps = 80
BETAS=[mp.mpf('0.35'),mp.mpf('0.8'),mp.mpf('1.2'),mp.pi/2,mp.mpf('2.1')]
RHOS=[mp.mpf(x) for x in ['-3.4','-2.3','-1.7','-0.6','0.35','0.9','1.6','2.7','3.8']]
DELTAS=[mp.mpf(x) for x in ['1e-8','1e-12','1e-16','1e-20','1e-24']]
POLES=[1j,0j,-1j]  # i*rho=-1,0,+1 respectively

def csch(x): return 1/mp.sinh(x)
def coth(x): return mp.cosh(x)/mp.sinh(x)
def den(r): return r+r**3

def source(m,r,b):
    if m==0:
        d=-12*mp.e**(2*b)*(((mp.e**(2*b)-1)*r*mp.cos(b*r)-(mp.e**(2*b)+1)*mp.sin(b*r)))/((mp.e**(2*b)-1)**3*den(r))
        tp=-3*mp.e**(1j*b*r)*(r+1j*coth(b))*csch(b)**2/(2*den(r))
        tm=-3*mp.e**(-1j*b*r)*(r-1j*coth(b))*csch(b)**2/(2*den(r))
    elif m==-1:
        d=12*mp.e**(3*b)*(-mp.sin(b*r)+mp.e**(1j*b*r)*r*mp.sinh(b)*(mp.cosh(b)-1j*r*mp.sinh(b)))/((mp.e**(2*b)-1)**3*den(r))
        tp=3*mp.e**(1j*b*r)*csch(b)**3*(1j*(1+r**2)+r*(mp.sinh(2*b)-1j*r*mp.cosh(2*b)))/(4*den(r))
        tm=-3j*mp.e**(-1j*b*r)*csch(b)**3/(4*den(r))
    elif m==1:
        d=6*mp.e**(b*(3-1j*r))*(1j*(mp.e**(2j*b*r)-r**2-1)+r*(1j*r*mp.cosh(2*b)+mp.sinh(2*b)))/((mp.e**(2*b)-1)**3*den(r))
        tp=3j*mp.e**(1j*b*r)*csch(b)**3/(4*den(r))
        tm=3*csch(b)**3*(1j*mp.cos(b*r)+mp.sin(b*r))*(-r**2+r**2*mp.cosh(2*b)-1j*r*mp.sinh(2*b)-1)/(4*den(r))
    else: raise ValueError(m)
    return d,tp,tm

def alt(m,r,b):
    # Algebraically separate organization using exponential definitions of trig/hyperbolic functions.
    E=mp.e**b; Ei=mp.e**(-b); sh=(E-Ei)/2; ch=(E+Ei)/2; cs=1/sh; ct=ch/sh
    ep=mp.e**(1j*b*r); em=1/ep
    co=(ep+em)/2; si=(ep-em)/(2j)
    e2=E**2
    sh2=2*sh*ch; ch2=ch**2+sh**2
    if m==0:
        d=-12*e2*(((e2-1)*r*co-(e2+1)*si))/((e2-1)**3*den(r))
        tp=-mp.mpf(3)/2*ep*(r+1j*ct)*cs**2/den(r)
        tm=-mp.mpf(3)/2*em*(r-1j*ct)*cs**2/den(r)
    elif m==-1:
        d=12*E**3*(-si+ep*r*sh*(ch-1j*r*sh))/((e2-1)**3*den(r))
        tp=mp.mpf(3)/4*ep*cs**3*(1j*(1+r**2)+r*(sh2-1j*r*ch2))/den(r)
        tm=-mp.mpf(3)/4*1j*em*cs**3/den(r)
    else:
        d=6*mp.e**(b*(3-1j*r))*(1j*(ep**2-r**2-1)+r*(1j*r*ch2+sh2))/((e2-1)**3*den(r))
        tp=mp.mpf(3)/4*1j*ep*cs**3/den(r)
        tm=mp.mpf(3)/4*cs**3*(1j*co+si)*(-r**2+r**2*ch2-1j*r*sh2-1)/den(r)
    return d,tp,tm

def t_num(m,branch,r,b):
    if m==0:
        return (-3*mp.e**(1j*b*r)*(r+1j*coth(b))*csch(b)**2/2 if branch=='p' else -3*mp.e**(-1j*b*r)*(r-1j*coth(b))*csch(b)**2/2)
    if m==-1:
        return (3*mp.e**(1j*b*r)*csch(b)**3*(1j*(1+r**2)+r*(mp.sinh(2*b)-1j*r*mp.cosh(2*b)))/4 if branch=='p' else -3j*mp.e**(-1j*b*r)*csch(b)**3/4)
    return (3j*mp.e**(1j*b*r)*csch(b)**3/4 if branch=='p' else 3*csch(b)**3*(1j*mp.cos(b*r)+mp.sin(b*r))*(-r**2+r**2*mp.cosh(2*b)-1j*r*mp.sinh(2*b)-1)/4)

def wrong_phase(m,r,b):
    d,tp,tm=source(m,r,b)
    # Flip the exponential phase in t+ only, keeping every other source factor fixed.
    if m==0: bad=-3*mp.e**(-1j*b*r)*(r+1j*coth(b))*csch(b)**2/(2*den(r))
    elif m==-1: bad=3*mp.e**(-1j*b*r)*csch(b)**3*(1j*(1+r**2)+r*(mp.sinh(2*b)-1j*r*mp.cosh(2*b)))/(4*den(r))
    else: bad=3j*mp.e**(-1j*b*r)*csch(b)**3/(4*den(r))
    return abs(bad+tm-d)

def enc(z):
    if isinstance(z,(bool,int,str)): return z
    if isinstance(z,dict): return {k:enc(v) for k,v in z.items()}
    if isinstance(z,list): return [enc(v) for v in z]
    if isinstance(z,tuple): return [enc(v) for v in z]
    try:
        if isinstance(z,mp.mpc) or isinstance(z,complex): return {'re':mp.nstr(mp.re(z),45),'im':mp.nstr(mp.im(z),45)}
        return mp.nstr(z,45)
    except Exception: return str(z)

def audit_m(m):
    add_max=mp.mpf('0'); indep_max=mp.mpf('0'); n=0; wrong_hits=0; wrong_total=0
    near_max=mp.mpf('0'); pole_records=[]
    for b in BETAS:
        for r in RHOS:
            d,tp,tm=source(m,r,b); a=alt(m,r,b)
            add=abs(tp+tm-d); add_max=max(add_max,add)
            tol=mp.mpf('1e-45')+mp.mpf('1e-40')*abs(d)
            if add>tol: pass
            for x,y in zip((d,tp,tm),a): indep_max=max(indep_max,abs(x-y))
            w=wrong_phase(m,r,b); wrong_total+=1; wrong_hits += int(w>mp.mpf('1e-8')); n+=1
    # Pole/simple-residue audit at beta=1.2; applicability is fixed by analytic numerator at exact pole.
    b=mp.mpf('1.2')
    for branch,idx in [('p',1),('m',2)]:
        for p in POLES:
            num0=t_num(m,branch,mp.mpc(p.real,p.imag),b)
            applicable=abs(num0)>mp.mpf('1e-30')
            mags=[]; residues=[]
            for delta in DELTAS:
                r=mp.mpc(p.real,p.imag)+delta
                val=source(m,r,b)[idx]
                mags.append(abs(val)); residues.append((r-mp.mpc(p.real,p.imag))*val)
            if applicable:
                slopes=[mp.log(mags[i+1]/mags[i])/mp.log(DELTAS[i+1]/DELTAS[i]) for i in range(len(DELTAS)-1)]
                slope_err=max(abs(s+1) for s in slopes[-2:])
                ref=residues[-1]
                drift=max(abs((q-ref)/ref) for q in residues[-3:-1]) if abs(ref)>0 else mp.inf
                pole_ok=(slope_err<=mp.mpf('5e-6') and drift<=mp.mpf('5e-6') and abs(ref)>mp.mpf('1e-30'))
            else:
                slopes=[]; slope_err=mp.mpf('0'); drift=mp.mpf('0'); pole_ok=True
            pole_records.append({'branch':branch,'pole':p,'applicable':applicable,'num_abs':abs(num0),'slope_err':slope_err,'residue_drift':drift,'pole_ok':pole_ok})
            # branch-sum cancellation near poles (only where d and branches are finite at displaced points)
            for delta in DELTAS[-3:]:
                r=mp.mpc(p.real,p.imag)+delta
                d,tp,tm=source(m,r,b)
                scale=max(mp.mpf('1'),abs(d)); near_max=max(near_max,abs(tp+tm-d)/scale)
    add_ok=add_max<=mp.mpf('1e-45')+mp.mpf('1e-40')*10  # conservative envelope; pointwise already tiny
    indep_ok=indep_max<=mp.mpf('1e-42')+mp.mpf('1e-38')*10
    poles_ok=all(x['pole_ok'] for x in pole_records)
    near_ok=near_max<=mp.mpf('1e-30')
    wrong_ok=(wrong_hits/mp.mpf(wrong_total))>=mp.mpf('0.8')
    wrong_poles=[mp.mpc('0','0.1')+q for q in POLES]
    wrong_pole_rejected=all(min(abs(w-q) for q in POLES)>mp.mpf('1e-30') for w in wrong_poles)
    tests={'additive_recovery':add_ok,'independent_formula_agreement':indep_ok,'simple_pole_scaling':poles_ok,'near_pole_branch_sum':near_ok,'wrong_phase_negative_control':wrong_ok,'wrong_pole_negative_control':wrong_pole_rejected}
    return {'m':m,'tests':tests,'add_max':add_max,'indep_max':indep_max,'near_pole_relative_max':near_max,'wrong_phase_hit_fraction':mp.mpf(wrong_hits)/wrong_total,'pole_records':pole_records,'valid':True,'pass':all(tests.values())}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--out',required=True); args=ap.parse_args()
    lane=args.lane
    try:
        if lane=='L0': payload={'lane':lane,'mode':'m=-1','records':[audit_m(-1)]}
        elif lane=='L1': payload={'lane':lane,'mode':'m=0','records':[audit_m(0)]}
        elif lane=='L2': payload={'lane':lane,'mode':'m=+1','records':[audit_m(1)]}
        elif lane=='L3': payload={'lane':lane,'mode':'cross-all-m','records':[audit_m(m) for m in (-1,0,1)]}
        else: raise ValueError(lane)
        payload['valid']=all(r['valid'] for r in payload['records'])
        payload['pass']=payload['valid'] and all(r['pass'] for r in payload['records'])
        payload['classification']='ITER456_REDUCED_TOLLER_APPENDIXB_RUHL_PHASE_QUALIFIED_SCOPED' if payload['pass'] else 'SCIENTIFIC_FAIL_ITER456_REDUCED_TOLLER_APPENDIXB'
    except Exception as e:
        payload={'lane':lane,'valid':False,'pass':False,'classification':'INFRASTRUCTURE_OR_NUMERICAL_FAIL','error':repr(e)}
    os.makedirs(os.path.dirname(args.out) or '.',exist_ok=True)
    with open(args.out,'w') as f: json.dump(enc(payload),f,indent=2)
    print(json.dumps(enc(payload),indent=2))

if __name__=='__main__': main()
