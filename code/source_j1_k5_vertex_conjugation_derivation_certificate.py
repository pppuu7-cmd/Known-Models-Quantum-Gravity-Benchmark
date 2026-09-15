#!/usr/bin/env python3
import argparse
import itertools
import json
import os
from pathlib import Path

import mpmath as mp
import sympy as sp

mp.mp.dps = 80

MS = [1, 0, -1]
RHOS = [mp.mpf(x) for x in ['-2.3', '-1.7', '-0.6', '0.35', '0.9', '1.6', '2.7']]
BETAS = [mp.mpf('0.35'), mp.mpf('0.8'), mp.mpf('1.2'), mp.pi/2, mp.mpf('2.1')]
PHASES = [1, -1, 1j, -1j]
TOL = mp.mpf('1e-35')

LANES = {
    'L0': ((mp.mpf('.17'),mp.mpf('.43'),mp.mpf('-.29')),(mp.mpf('-.38'),mp.mpf('.71'),mp.mpf('.52'))),
    'L1': ((mp.mpf('-.61'),mp.mpf('.84'),mp.mpf('.33')),(mp.mpf('.47'),mp.mpf('.58'),mp.mpf('-.76'))),
    'L2': ((mp.mpf('.93'),mp.mpf('.52'),mp.mpf('-.41')),(mp.mpf('-.74'),mp.mpf('1.03'),mp.mpf('.26'))),
    'L3': ((mp.mpf('-1.11'),mp.mpf('.67'),mp.mpf('.89')),(mp.mpf('.68'),mp.mpf('.92'),mp.mpf('-1.02'))),
}

C_MP = mp.matrix([[0,0,1],[0,-1,0],[1,0,0]])

FROZEN_BLOBS = {
    'research/SOURCE_J1_K5_PUBLISHED_IEPSILON_SCOPE_RESULT_2026-09-15.md': '9a5531b6dbecc367c2869c6e9d873071a6444a66',
    'research/SOURCE_J1_K5_CAUSAL_COCAUSAL_CONJUGATION_AMBIGUITY_PREREG_2026-09-15.md': 'de8916bb0444d54249ffa7ffc33553ff39d5db0f',
    'research/SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_AUTHORITY_RESULT_2026-09-15.md': '839f0ed038b60eb73dfbdc4738872d13fea2a352',
    'recovery/CRITICAL_REVIEW_SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_AUTHORITY_2026-09-15.md': '87a95edccb41ca2115ad0918b590d948bf4b9338',
    'code/iter456_reduced_toller_appendixb.py': '9626d52307763bc84c348110ed26db4a2b57b211',
    'code/iter457_toller_eq7_magnetic_reconstruction.py': '23d7108cd697012b2d9bb9ce3b2651d36b561e2b',
}


def csch(x): return 1/mp.sinh(x)
def coth(x): return mp.cosh(x)/mp.sinh(x)
def den(r): return r+r**3


def source(m,r,b):
    if m == 0:
        d=-12*mp.e**(2*b)*(((mp.e**(2*b)-1)*r*mp.cos(b*r)-(mp.e**(2*b)+1)*mp.sin(b*r)))/((mp.e**(2*b)-1)**3*den(r))
        tp=-3*mp.e**(1j*b*r)*(r+1j*coth(b))*csch(b)**2/(2*den(r))
        tm=-3*mp.e**(-1j*b*r)*(r-1j*coth(b))*csch(b)**2/(2*den(r))
    elif m == -1:
        d=12*mp.e**(3*b)*(-mp.sin(b*r)+mp.e**(1j*b*r)*r*mp.sinh(b)*(mp.cosh(b)-1j*r*mp.sinh(b)))/((mp.e**(2*b)-1)**3*den(r))
        tp=3*mp.e**(1j*b*r)*csch(b)**3*(1j*(1+r**2)+r*(mp.sinh(2*b)-1j*r*mp.cosh(2*b)))/(4*den(r))
        tm=-3j*mp.e**(-1j*b*r)*csch(b)**3/(4*den(r))
    elif m == 1:
        d=6*mp.e**(b*(3-1j*r))*(1j*(mp.e**(2j*b*r)-r**2-1)+r*(1j*r*mp.cosh(2*b)+mp.sinh(2*b)))/((mp.e**(2*b)-1)**3*den(r))
        tp=3j*mp.e**(1j*b*r)*csch(b)**3/(4*den(r))
        tm=3*csch(b)**3*(1j*mp.cos(b*r)+mp.sin(b*r))*(-r**2+r**2*mp.cosh(2*b)-1j*r*mp.sinh(2*b)-1)/(4*den(r))
    else:
        raise ValueError(m)
    return d,tp,tm


def symbolic_source(m, r, b):
    I=sp.I
    de=r+r**3
    if m == 0:
        tp=-3*sp.exp(I*b*r)*(r+I*sp.coth(b))*sp.csch(b)**2/(2*de)
        tm=-3*sp.exp(-I*b*r)*(r-I*sp.coth(b))*sp.csch(b)**2/(2*de)
    elif m == -1:
        tp=3*sp.exp(I*b*r)*sp.csch(b)**3*(I*(1+r**2)+r*(sp.sinh(2*b)-I*r*sp.cosh(2*b)))/(4*de)
        tm=-3*I*sp.exp(-I*b*r)*sp.csch(b)**3/(4*de)
    elif m == 1:
        tp=3*I*sp.exp(I*b*r)*sp.csch(b)**3/(4*de)
        tm=3*sp.csch(b)**3*(I*sp.cos(b*r)+sp.sin(b*r))*(-r**2+r**2*sp.cosh(2*b)-I*r*sp.sinh(2*b)-1)/(4*de)
    else:
        raise ValueError(m)
    return tp,tm


def wigner_closed(a,t,g):
    c=mp.cos(t); s=mp.sin(t); q=mp.sqrt(2)
    d=mp.matrix([[(1+c)/2,-s/q,(1-c)/2],[s/q,c,-s/q],[(1-c)/2,s/q,(1+c)/2]])
    D=mp.matrix(3)
    for i,m in enumerate(MS):
        for j,n in enumerate(MS):
            D[i,j]=mp.e**(-1j*m*a)*d[i,j]*mp.e**(-1j*n*g)
    return D


def maxentry(A):
    return max(abs(A[i,j]) for i in range(A.rows) for j in range(A.cols))


def enc(z):
    if isinstance(z,(bool,int,str)) or z is None: return z
    if isinstance(z,dict): return {k:enc(v) for k,v in z.items()}
    if isinstance(z,(list,tuple)): return [enc(v) for v in z]
    if isinstance(z,complex) or isinstance(z,mp.mpc):
        return {'re':mp.nstr(mp.re(z),50),'im':mp.nstr(mp.im(z),50)}
    try: return mp.nstr(z,50)
    except Exception: return str(z)


def candidate_search():
    survivors=[]
    tested=0
    best_wrong=None
    for s_r in (1,-1):
        for s_m in (1,-1):
            for qs in itertools.product(PHASES, repeat=3):
                tested += 1
                mx=mp.mpf('0')
                ok=True
                for m,q in zip(MS,qs):
                    mm=s_m*m
                    for rho in RHOS:
                        for beta in BETAS:
                            lhs=mp.conj(source(m,rho,beta)[1])
                            rhs=q*source(mm,s_r*rho,beta)[2]
                            err=abs(lhs-rhs)/max(mp.mpf('1'),abs(lhs),abs(rhs))
                            mx=max(mx,err)
                            if err>TOL:
                                ok=False
                                break
                        if not ok: break
                    if not ok: break
                if ok:
                    survivors.append({'s_r':s_r,'s_m':s_m,'q':list(qs),'max_relative_residual':mx})
                elif best_wrong is None or mx < best_wrong['residual']:
                    best_wrong={'s_r':s_r,'s_m':s_m,'q':list(qs),'residual':mx}
    return tested,survivors,best_wrong


def symbolic_reduced_check():
    r,b=sp.symbols('r b', real=True, nonzero=True)
    rows=[]
    all_ok=True
    for m in MS:
        tp,_=symbolic_source(m,r,b)
        _,tm= symbolic_source(-m,r,b)
        expr=sp.simplify(sp.expand_complex(sp.conjugate(tp)-tm))
        ok=(expr==0)
        rows.append({'m':m,'identity':'conj(t_plus_m(rho,beta)) = t_minus_-m(rho,beta)','symbolic_zero':bool(ok)})
        all_ok &= bool(ok)
    return all_ok,rows


def symbolic_wigner_check():
    a,t,g=sp.symbols('a t g', real=True)
    I=sp.I; q=sp.sqrt(2); c=sp.cos(t); s=sp.sin(t)
    d=sp.Matrix([[(1+c)/2,-s/q,(1-c)/2],[s/q,c,-s/q],[(1-c)/2,s/q,(1+c)/2]])
    D=sp.Matrix(3,3,lambda i,j: sp.exp(-I*MS[i]*a)*d[i,j]*sp.exp(-I*MS[j]*g))
    C=sp.Matrix([[0,0,1],[0,-1,0],[1,0,0]])
    R=sp.simplify(sp.conjugate(D)-C*D*C)
    ok=all(sp.simplify(R[i,j])==0 for i in range(3) for j in range(3))
    return bool(ok)


def full_matrix_check():
    mx=mp.mpf('0'); wmx=mp.mpf('0'); n=0
    for lane,(u1a,u2a) in LANES.items():
        U1=wigner_closed(*u1a); U2=wigner_closed(*u2a)
        wmx=max(wmx,maxentry(U1.apply(lambda x:mp.conj(x))-C_MP*U1*C_MP))
        wmx=max(wmx,maxentry(U2.apply(lambda x:mp.conj(x))-C_MP*U2*C_MP))
        for rho in RHOS:
            for beta in BETAS:
                pv=[]; mv=[]
                for m in MS:
                    _,tp,tm=source(m,rho,beta); pv.append(tp); mv.append(tm)
                TP=U1*mp.diag(pv)*U2
                TM=U1*mp.diag(mv)*U2
                lhs=TP.apply(lambda x:mp.conj(x))
                rhs=C_MP*TM*C_MP
                err=maxentry(lhs-rhs)/max(mp.mpf('1'),maxentry(lhs),maxentry(rhs))
                mx=max(mx,err); n+=1
    return {'n_matrix_points':n,'max_relative_residual':mx,'max_wigner_residual':wmx,'pass':mx<=TOL and wmx<=TOL}


def coefficient_control():
    nodes=range(5); edges=list(itertools.combinations(nodes,2))
    cplus=set()
    for sig in itertools.product((-1,1),repeat=5):
        cplus.add(tuple(sig[a]*sig[b] for a,b in edges))
    cminus={tuple(-x for x in k) for k in cplus}
    all_patterns=list(itertools.product((-1,1),repeat=10))
    def coeff(k):
        if k in cplus: return 1j
        if k in cminus: return -1j
        return 0j
    conj_ok=all(coeff(tuple(-x for x in k))==complex(coeff(k)).conjugate() for k in all_patterns)
    total=sum((coeff(k) for k in all_patterns),0j)
    return {
        'n_patterns':len(all_patterns),'n_cplus':len(cplus),'n_cminus':len(cminus),
        'intersection':len(cplus & cminus),'conjugation_covariance':conj_ok,
        'eprl_counterterm_sum_re':total.real,'eprl_counterterm_sum_im':total.imag,
        'pass':len(cplus)==16 and len(cminus)==16 and not (cplus & cminus) and conj_ok and total==0j,
    }


def joint_authority_audit(repo_root):
    p=Path(repo_root)/'research/SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_AUTHORITY_RESULT_2026-09-15.md'
    txt=p.read_text()
    frozen_class='SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_NORMALIZATION_AUTHORITY_NOT_YET_PINNED_SCOPED'
    has_class=frozen_class in txt
    has_joint_gap=('collision-supported action' in txt and 'source chain contains no already-pinned joint vertex-level conjugation or collision-normalization law' in txt)
    return {
        'frozen_authority_classification_present':has_class,
        'joint_collision_action_gap_present':has_joint_gap,
        'unique_joint_extension_action_derived_from_frozen_chain':False,
        'reason':'The frozen authority result states that no joint collision-supported selection law is pinned; this gate derives the one-wedge representation-valued anti-linear map but introduces no new joint regulator/normalization data.',
        'pass_for_blocker':bool(has_class and has_joint_gap),
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',required=True)
    ap.add_argument('--repo-root',default='.')
    args=ap.parse_args()

    tested,survivors,best_wrong=candidate_search()
    sym_ok,sym_rows=symbolic_reduced_check()
    wig_sym=symbolic_wigner_check()
    matrix=full_matrix_check()
    coeff=coefficient_control()
    joint=joint_authority_audit(args.repo_root)

    unique=(len(survivors)==1 and survivors[0]['s_r']==1 and survivors[0]['s_m']==-1 and survivors[0]['q']==[1,1,1])
    positive=unique and sym_ok and wig_sym and matrix['pass'] and coeff['pass']
    if positive and joint['pass_for_blocker'] and not joint['unique_joint_extension_action_derived_from_frozen_chain']:
        classification='SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_JOINT_EXTENSION_ACTION_BLOCKED_SCOPED'
        outcome='BLOCKED_SCOPED'
    elif positive and joint['unique_joint_extension_action_derived_from_frozen_chain']:
        classification='SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_DERIVED_AND_COUNTERTERM_DECIDED_SCOPED'
        outcome='PASS'
    else:
        classification='INVALID_DERIVATION_GATE' if not positive else 'SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_DERIVATION_CONTRADICTS_FROZEN_SOURCE_SCOPED'
        outcome='INVALID' if not positive else 'FAIL'

    payload={
        'gate':'SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_DERIVATION_AND_COUNTERTERM_ELIMINATION_GATE',
        'frozen_blob_contract':FROZEN_BLOBS,
        'candidate_family_size':tested,
        'candidate_survivor_count':len(survivors),
        'candidate_survivors':survivors,
        'best_rejected_candidate':best_wrong,
        'derived_reduced_map':'conj(t_plus_m(rho,beta)) = t_minus_-m(rho,beta)',
        'derived_rho_map':'rho -> rho',
        'derived_magnetic_map':'m -> -m',
        'derived_component_phase':'q_m = +1 for m=+1,0,-1',
        'symbolic_reduced_checks':sym_rows,
        'symbolic_reduced_all_pass':sym_ok,
        'symbolic_wigner_identity':'conj(D^1(U)) = C D^1(U) C',
        'symbolic_wigner_pass':wig_sym,
        'C_matrix':[[0,0,1],[0,-1,0],[1,0,0]],
        'derived_full_one_wedge_map':'conj(T_plus(U1,beta,U2;rho)) = C T_minus(U1,beta,U2;rho) C',
        'full_matrix_control':matrix,
        'coefficient_witness_control':coeff,
        'joint_extension_decision_audit':joint,
        'positive_controls_pass':positive,
        'outcome':outcome,
        'classification':classification,
        'claim_ceiling':'The exact one-wedge representation-valued conjugation map is derived for the frozen j=1 realization. The frozen source chain still does not uniquely define the action on collision-supported joint K5 extension terms; BLOCKED_SCOPED is not physical nonuniqueness or model falsification.',
    }
    os.makedirs(os.path.dirname(args.out) or '.',exist_ok=True)
    with open(args.out,'w') as f: json.dump(enc(payload),f,indent=2,sort_keys=True)
    print(json.dumps(enc(payload),indent=2,sort_keys=True))
    if classification=='INVALID_DERIVATION_GATE':
        raise SystemExit(2)

if __name__=='__main__':
    main()
