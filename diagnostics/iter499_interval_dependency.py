#!/usr/bin/env python3
import json, os
from flint import arb, ctx
import iter499_arb_core as core

ctx.prec=384
D=core.DIRS[0]
SIGN=1
BOX=0


def factors(R, amp):
    d20=[0]*20
    for k,c in enumerate(core.COORDS): d20[c]=D[k]
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
    nodes=[core.eye2()]
    for a in range(1,5): nodes.append(core.mm(core.mm(core.mm(L[a],B),G[a]),RR[a]))
    fac={}
    for a,b in core.EDGES:
        if a==0:
            fac[(a,b)]=core.mm(core.mm(core.mm(core.dagger(RR[b]),Gi[b]),Binv),core.dagger(L[b]))
        else:
            X=core.mm(core.dagger(RR[b]),Gi[b])
            X=core.mm(X,Binv); X=core.mm(X,core.dagger(L[b])); X=core.mm(X,L[a])
            X=core.mm(X,B); X=core.mm(X,G[a]); X=core.mm(X,RR[a])
            fac[(a,b)]=X
    return nodes,fac


def kak_ok(h):
    try:
        k=core.kak_ball(h)
        return True, float(k['beta'].lower())
    except Exception as e:
        return False, repr(e)


def midpoint_box():
    lo=arb('16/12800'); hi=arb('17/12800')
    return (lo+hi)/2


def evaluate():
    amp,lo,hi=core.box_amp(BOX)
    rows=[]; all_nodes=True; any_naive_fail=False; all_factor=True; all_equiv=True
    for R in core.R_GRID:
        nodesN,rsN=core.geometry(R,D,SIGN,amp)
        nodesF,rsF=factors(R,amp)
        node=[]
        for a in range(1,5):
            ok,detail=kak_ok(nodesN[a]); node.append({'node':a,'pass':ok,'detail':detail}); all_nodes &= ok
        naive=[]; fact=[]
        for e in core.EDGES:
            ok,detail=kak_ok(rsN[e]); naive.append({'edge':list(e),'pass':ok,'detail':detail}); any_naive_fail |= (not ok)
            ok2,detail2=kak_ok(rsF[e]); fact.append({'edge':list(e),'pass':ok2,'detail':detail2}); all_factor &= ok2
        # Exact-point algebraic equivalence at the frozen midpoint.
        mid=midpoint_box()
        _,nmid=core.geometry(R,D,SIGN,mid)
        _,fmid=factors(R,mid)
        equiv=[]
        for e in core.EDGES:
            ok=core.residual_contains_zero(core.madd(nmid[e],fmid[e],-1)); equiv.append({'edge':list(e),'pass':bool(ok)}); all_equiv &= bool(ok)
        rows.append({'R':R,'nodes':node,'naive_edges':naive,'factorized_edges':fact,'midpoint_equivalence':equiv})
    confirmed=bool(all_nodes and any_naive_fail and all_factor and all_equiv)
    return {'diagnostic':'iter499_interval_dependency','direction':D,'sign':SIGN,'box':BOX,
            'amp_lower':float(lo),'amp_upper':float(hi),'all_naive_nodes_kak_pass':bool(all_nodes),
            'any_naive_relative_kak_fail':bool(any_naive_fail),'all_factorized_relative_kak_pass':bool(all_factor),
            'all_midpoint_equivalence_pass':bool(all_equiv),
            'classification':'ITER499_INTERVAL_DEPENDENCY_BLOWUP_CONFIRMED_SCOPED' if confirmed else 'ITER499_DEPENDENCY_DIAGNOSTIC_UNRESOLVED',
            'scope':'diagnostic only; no Iter499 science verdict or repair','rows':rows}

if __name__=='__main__':
    out=evaluate(); os.makedirs('artifacts',exist_ok=True)
    with open('artifacts/iter499-dependency-diagnostic.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))
