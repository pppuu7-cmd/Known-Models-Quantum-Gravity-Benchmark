#!/usr/bin/env python3
import argparse, json, math, os
import numpy as np
from flint import arb, acb, ctx

import iter499_arb_core as core
import iter491_high_precision_angular_thickening as hp
import iter486_shared_node_haar_escape as base

ctx.prec=384
MATRIX_REL_TOL=1e-9
BETA_ABS_TOL=1e-10
TOLLER_REL_TOL=1e-8


def build_factors(R,direction,sign,amp):
    d20=[0]*20
    for k,c in enumerate(core.COORDS): d20[c]=int(sign)*int(direction[k])
    B=core.boost(R); Binv=core.boost(-R)
    L=[core.eye2() for _ in range(5)]; RR=[core.eye2() for _ in range(5)]
    G=[core.eye2() for _ in range(5)]; Gi=[core.eye2() for _ in range(5)]
    eps=amp*((-core.A(R)).exp())
    for a in range(1,5):
        aa,t,g=core.gb.PANELS['C'][a]; eta=core.gb.BOOSTS['strong'][a]
        UL=core.su2(repr(float(aa)),repr(float(t)),repr(float(g)))
        ur_a=float(-.37*g); ur_t=float(.73*t); ur_g=float(.41*aa)
        UR=core.su2(repr(ur_a),repr(ur_t),repr(ur_g))
        G[a]=core.mm(core.mm(UL,core.boost(repr(float(eta)))),UR)
        Gi[a]=core.mm(core.mm(core.dagger(UR),core.boost(repr(float(-eta)))),core.dagger(UL))
        q=[eps*d20[(a-1)*5+j] for j in range(5)]
        L[a]=core.mm(core.mm(core.rx(q[0]),core.ry(q[1])),core.rz(q[2]))
        RR[a]=core.mm(core.rx(q[3]),core.ry(q[4]))
    return B,Binv,L,RR,G,Gi


def with_outer(km,left,right):
    return {'U1':core.mm(left,km['U1']),'beta':km['beta'],'U2':core.mm(km['U2'],right)}


def validate_full(h,k):
    beta=k['beta']
    AA=core.diag2((beta/2).exp(),(-beta/2).exp())
    recon=core.residual_contains_zero(core.madd(core.mm(core.mm(k['U1'],AA),k['U2']),h,-1))
    u1=core.unitary_contains(k['U1']); u2=core.unitary_contains(k['U2'])
    d1=core.det_contains_one(k['U1']); d2=core.det_contains_one(k['U2'])
    positive=bool(beta.lower()>arb(0))
    return bool(recon and u1 and u2 and d1 and d2 and positive),{'reconstruction':bool(recon),'u1_unitary':bool(u1),'u2_unitary':bool(u2),'u1_det':bool(d1),'u2_det':bool(d2),'positive_beta':positive}


def construct_state(R,direction,sign,amp):
    B,Binv,L,RR,G,Gi=build_factors(R,direction,sign,amp)
    nodes={}; nk={}; edges={}; ek={}; checks=[]
    for a in range(1,5):
        middle=core.mm(B,G[a])
        km=core.kak_ball(middle)
        h=core.mm(core.mm(L[a],middle),RR[a])
        k=with_outer(km,L[a],RR[a])
        ok,detail=validate_full(h,k); checks.append(('node',a,ok,detail)); nodes[a]=h; nk[a]=k
    for a,b in core.EDGES:
        if a==0:
            middle=core.mm(Gi[b],Binv)
            km=core.kak_ball(middle)
            left=core.dagger(RR[b]); right=core.dagger(L[b])
            h=core.mm(core.mm(left,middle),right)
            k=with_outer(km,left,right)
        else:
            middle=core.mm(Gi[b],Binv)
            middle=core.mm(middle,core.dagger(L[b])); middle=core.mm(middle,L[a])
            middle=core.mm(middle,B); middle=core.mm(middle,G[a])
            km=core.kak_ball(middle)
            left=core.dagger(RR[b]); right=RR[a]
            h=core.mm(core.mm(left,middle),right)
            k=with_outer(km,left,right)
        ok,detail=validate_full(h,k); checks.append(('edge',[a,b],ok,detail)); edges[(a,b)]=h; ek[(a,b)]=k
    return {'nodes':nodes,'node_kak':nk,'edges':edges,'edge_kak':ek,'checks':checks}


def acb_mid(z):
    z=core.C(z)
    return complex(float(z.real.mid()),float(z.imag.mid()))


def np_mid(M):
    return np.array([[acb_mid(M[i][j]) for j in range(len(M[0]))] for i in range(len(M))],dtype=np.complex128)


def rel_matrix_error(M,hpM):
    A=np_mid(M); B=hp.to_np(hpM)
    den=max(1.0,float(np.max(np.abs(B))))
    return float(np.max(np.abs(A-B))/den)


def source_regression(R,direction,sign,mid,state):
    v=np.zeros(20,dtype=float)
    for k,c in enumerate(core.COORDS): v[c]=float(sign*direction[k])
    eps=float(mid)*math.exp(-float(R))
    gs,rs=hp.geometry_bundle(float(R),v,eps,dps=100)
    matrix_max=0.0; beta_max=0.0; toller_max=0.0; additive=True
    for e in core.EDGES:
        matrix_max=max(matrix_max,rel_matrix_error(state['edges'][e],rs[e]))
        U1,beta,U2,rec,uu,dd=hp.hp_kak(rs[e],dps=100)
        beta_max=max(beta_max,abs(float(state['edge_kak'][e]['beta'].mid())-float(beta)))
        refU1=hp.to_np(U1); refU2=hp.to_np(U2); refb=float(beta)
        for rho in core.RHOS:
            D,Tp,Tm=base.full_from_kak(refU1,refb,refU2,rho)
            for branch,ref in [('p',Tp),('m',Tm)]:
                M,addok=core.full_toller(state['edge_kak'][e],rho,branch); additive=additive and addok
                X=np_mid(M); den=max(1.0,float(np.max(np.abs(ref))))
                toller_max=max(toller_max,float(np.max(np.abs(X-ref))/den))
    passed=bool(matrix_max<MATRIX_REL_TOL and beta_max<BETA_ABS_TOL and toller_max<TOLLER_REL_TOL and additive)
    return {'matrix_relative_max':matrix_max,'beta_absolute_max':beta_max,'toller_relative_max':toller_max,'source_additive':bool(additive),'pass':passed}


def old_negative_control():
    amp,_,_=core.box_amp(0); direction=core.DIRS[0]; rows=[]; failed_large=False
    for R in core.R_GRID:
        try:
            gs,_=core.geometry(R,direction,1,amp); core.kak_ball(gs[1]); ok=True; err=None
        except Exception as e:
            ok=False; err=repr(e)
        if R in (10,12) and not ok: failed_large=True
        rows.append({'R':R,'old_generic_node1_pass':ok,'error':err})
    return {'rows':rows,'reproduces_old_limitation':bool(failed_large)}


def evaluate(block):
    dirs=core.BLOCKS[block]; method_blocker=False; covariance_fail=False; regress_fail=False
    states=0; min_beta=None; max_matrix=0.0; max_beta=0.0; max_toller=0.0; source_add=True; records=[]
    for direction in dirs:
        for sign in (1,-1):
            for k in range(16):
                amp,lo,hi=core.box_amp(k); mid=(lo+hi)/2
                for R in core.R_GRID:
                    states+=1
                    try:
                        st=construct_state(R,direction,sign,amp)
                    except Exception as e:
                        method_blocker=True; records.append({'direction':direction,'sign':sign,'box':k,'R':R,'error':repr(e)}); continue
                    allid=all(x[2] for x in st['checks'])
                    if not allid: covariance_fail=True
                    for kk in list(st['node_kak'].values())+list(st['edge_kak'].values()):
                        b=kk['beta'].lower(); min_beta=b if min_beta is None or b<min_beta else min_beta
                    try:
                        reg=source_regression(R,direction,sign,mid,construct_state(R,direction,sign,mid))
                    except Exception as e:
                        method_blocker=True; records.append({'direction':direction,'sign':sign,'box':k,'R':R,'identity_pass':allid,'regression_error':repr(e)}); continue
                    regress_fail=regress_fail or (not reg['pass']); source_add=source_add and reg['source_additive']
                    max_matrix=max(max_matrix,reg['matrix_relative_max']); max_beta=max(max_beta,reg['beta_absolute_max']); max_toller=max(max_toller,reg['toller_relative_max'])
                    records.append({'direction':direction,'sign':sign,'box':k,'R':R,'identity_pass':bool(allid),'regression':reg})
    neg=old_negative_control() if block==0 else None
    if method_blocker or regress_fail or not source_add:
        cls='ITER500_NUMERICAL_METHOD_BLOCKER'
    elif covariance_fail:
        cls='SCIENTIFIC_FAIL_ITER500_COMPACT_KAK_COVARIANCE'
    else:
        cls='ITER500_COMPACT_SANDWICH_FACTORIZED_KAK_LANE_QUALIFIED_SCOPED'
    return {'iteration':500,'block':block,'valid':bool(not method_blocker and not regress_fail and source_add),'method_blocker':bool(method_blocker or regress_fail or not source_add),'covariance_fail':bool(covariance_fail),'regression_fail':bool(regress_fail),
            'classification':cls,'states_expected':256,'states_evaluated':states,'min_beta_lower':None if min_beta is None else float(min_beta),
            'max_midpoint_matrix_relative_error':max_matrix,'max_midpoint_beta_absolute_error':max_beta,'max_midpoint_toller_relative_error':max_toller,
            'source_additive_all':bool(source_add),'negative_control':neg,'records':records,
            'scope':'validated compact-sandwich/factorized KAK/Toller enabling gate only; no NONDECAY, envelope, Haar or spectral-integration claim'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--block',type=int,required=True,choices=range(4)); ap.add_argument('--out',required=True); a=ap.parse_args()
    try: out=evaluate(a.block)
    except Exception as e: out={'iteration':500,'block':a.block,'valid':False,'method_blocker':True,'classification':'ITER500_NUMERICAL_METHOD_BLOCKER','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2,sort_keys=True)); raise SystemExit(0)
if __name__=='__main__': main()
