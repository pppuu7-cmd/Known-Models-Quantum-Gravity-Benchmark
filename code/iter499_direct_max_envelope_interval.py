#!/usr/bin/env python3
import argparse, itertools, json, math, os
import numpy as np
from flint import arb, ctx

import iter499_arb_core as core
import iter492_tangent_boundary_layer as point

ctx.prec=384
POINT_AMPS=[0.00125,0.00140625,0.0015625,0.00171875,0.001875,0.00203125,0.0021875,0.00234375,0.00250]
DRIFT_TOL=arb('0.05')
ROBUST_FLOOR=arb('1.0')
NONDECAY_FLOOR=arb('0.0')
DECAY_CEIL=arb('-0.10')


def cycle_contains(rs):
    for a,b,c in itertools.combinations(range(5),3):
        lhs=core.mm(rs[(b,c)],rs[(a,b)])
        if not core.residual_contains_zero(core.madd(lhs,rs[(a,c)],-1)):
            return False
    return True


def box_eval(causal,direction,sign,k):
    amp,alo,ahi=core.box_amp(k)
    sig=core.SIGMAS[causal]
    perR={}; min_beta=None; min_chart=None
    controls={'group_det':True,'cycle':True,'kak':True,'source_additive':True,'finite_envelope':True}
    for R in core.R_GRID:
        gs,rs=core.geometry(R,direction,sign,amp)
        controls['group_det']=controls['group_det'] and all(core.C(core.det2(g)).contains(1) for g in gs)
        controls['group_det']=controls['group_det'] and all(core.C(core.det2(h)).contains(1) for h in rs.values())
        controls['cycle']=controls['cycle'] and cycle_contains(rs)
        node_k=[]
        logH=arb(0)
        for node in range(1,5):
            kk=core.kak_ball(gs[node]); node_k.append(kk)
            b=kk['beta']; logH += 2*b.sinh().log()
            bl=b.lower(); cl=kk['chart_norm2_lower']
            min_beta=bl if min_beta is None or bl<min_beta else min_beta
            min_chart=cl if min_chart is None or cl<min_chart else min_chart
        edge_k={}
        for e in core.EDGES:
            kk=core.kak_ball(rs[e]); edge_k[e]=kk
            bl=kk['beta'].lower(); cl=kk['chart_norm2_lower']
            min_beta=bl if min_beta is None or bl<min_beta else min_beta
            min_chart=cl if min_chart is None or cl<min_chart else min_chart
        rhorows=[]
        for rho in core.RHOS:
            mats=[]; addok=True
            for e in core.EDGES:
                branch='p' if sig[e[0]]*sig[e[1]]>0 else 'm'
                M,ok=core.full_toller(edge_k[e],rho,branch)
                mats.append(M); addok=addok and ok
            controls['source_additive']=controls['source_additive'] and addok
            vals=core.contract_all(mats)
            L,U,possible=core.envelope_bounds(vals)
            controls['finite_envelope']=controls['finite_envelope'] and bool(L>arb(0) and U.is_finite())
            ylo=logH.lower()+L.log().lower()
            yhi=logH.upper()+U.log().upper()
            rhorows.append({'rho':rho,'_ylo':ylo,'_yhi':yhi,
                            'possible_max':possible,'envelope_lower':L,'envelope_upper':U})
        perR[R]={'logH':logH,'rho':rhorows}
    if not all(controls.values()): raise ArithmeticError(f'box controls failed: {controls}')
    per=[]
    for ir,rho in enumerate(core.RHOS):
        y6l=perR[6]['rho'][ir]['_ylo']; y6u=perR[6]['rho'][ir]['_yhi']
        y8l=perR[8]['rho'][ir]['_ylo']; y8u=perR[8]['rho'][ir]['_yhi']
        y10l=perR[10]['rho'][ir]['_ylo']; y10u=perR[10]['rho'][ir]['_yhi']
        y12l=perR[12]['rho'][ir]['_ylo']; y12u=perR[12]['rho'][ir]['_yhi']
        slo=(y12l-y8u)/4; shi=(y12u-y8l)/4
        elo=(y10l-y6u)/4; ehi=(y10u-y6l)/4
        d1=abs(slo-ehi); d2=abs(shi-elo); du=d1 if d1>=d2 else d2
        robust=bool(slo>=ROBUST_FLOOR and du<=DRIFT_TOL)
        nondecay=bool(slo>=NONDECAY_FLOOR and du<=DRIFT_TOL)
        decay=bool(shi<=DECAY_CEIL and du<=DRIFT_TOL)
        if robust: cls='INTERVAL_ROBUST_NONDECAY'
        elif nondecay: cls='INTERVAL_NONDECAY'
        elif decay: cls='INTERVAL_UNIFORM_DECAY_WITNESS'
        else: cls='INTERVAL_INCONCLUSIVE'
        per.append({'rho':rho,'classification':cls,'_slo':slo,'_shi':shi,'_elo':elo,'_ehi':ehi,'_du':du})
    return {'box':k,'_alo':alo,'_ahi':ahi,'controls':controls,'_min_beta':min_beta,'_min_chart':min_chart,
            '_perR':perR,'per_rho':per}


def point_eval(causal,direction,sign,amp):
    d=np.zeros(20,dtype=float)
    for j,c in enumerate(core.COORDS): d[c]=float(direction[j])
    old=point.KAPPA
    try:
        point.KAPPA=float(amp)
        out=point.dynamic_eval(causal,d,int(sign),1.0)
    finally:
        point.KAPPA=old
    if not all(out['controls'].values()): raise ArithmeticError('legacy point evaluator control failure')
    return [{'rho':float(r['rho']),'actual_slope':float(r['actual_slope']),
             'early_actual_slope':float(r['early_actual_slope'])} for r in out['results']]


def point_containment(boxes,causal,direction,sign):
    checks=[]; ok=True
    for j,a in enumerate(POINT_AMPS):
        endpoint=2*j
        candidates=[0] if endpoint==0 else ([15] if endpoint==16 else [endpoint-1,endpoint])
        pp=point_eval(causal,direction,sign,a)
        for ir,r in enumerate(pp):
            sv=arb(repr(r['actual_slope'])); ev=arb(repr(r['early_actual_slope']))
            hit=False
            for k in candidates:
                if k>=len(boxes) or boxes[k].get('error'): continue
                q=boxes[k]['per_rho'][ir]
                if q['_slo']<=sv<=q['_shi'] and q['_elo']<=ev<=q['_ehi']:
                    hit=True; break
            ok=ok and hit
            checks.append({'amplitude':a,'rho':r['rho'],'actual_slope':r['actual_slope'],
                           'early_actual_slope':r['early_actual_slope'],'candidate_boxes':candidates,'contained':bool(hit)})
    return bool(ok),checks


def _bf(x,side): return core.bound_float(x,side)

def serialize_box(b):
    if b.get('error'): return b
    perR=[]
    for R in core.R_GRID:
        rows=[]
        for q in b['_perR'][R]['rho']:
            rows.append({'rho':q['rho'],'Y_lower':_bf(q['_ylo'],'lower'),'Y_upper':_bf(q['_yhi'],'upper'),
                         'envelope_lower':_bf(q['envelope_lower'],'lower'),'envelope_upper':_bf(q['envelope_upper'],'upper'),
                         'possible_max_indices':q['possible_max'],'possible_max_count':len(q['possible_max'])})
        perR.append({'R':R,'logH_lower':_bf(b['_perR'][R]['logH'],'lower'),
                     'logH_upper':_bf(b['_perR'][R]['logH'],'upper'),'rho':rows})
    return {'box':b['box'],'amp_lower':_bf(b['_alo'],'lower'),'amp_upper':_bf(b['_ahi'],'upper'),
            'controls':b['controls'],'min_beta_lower':_bf(b['_min_beta'],'lower'),
            'min_chart_norm2_lower':_bf(b['_min_chart'],'lower'),
            'per_rho':[{'rho':q['rho'],'classification':q['classification'],
                        'S_lower':_bf(q['_slo'],'lower'),'S_upper':_bf(q['_shi'],'upper'),
                        'E_lower':_bf(q['_elo'],'lower'),'E_upper':_bf(q['_ehi'],'upper'),
                        'drift_upper':_bf(q['_du'],'upper')} for q in b['per_rho']],
            'per_R':perR}


def evaluate(causal,block):
    int_reg=core.intertwiner_regression()
    init_ok=bool(int_reg<1e-15)
    paths=[]; method_blocker=not init_ok; all_classes=[]; point_ok_all=True
    global_min_beta=None; global_min_chart=None
    for direction in core.BLOCKS[block]:
        for sign in (1,-1):
            boxes=[]
            for k in range(16):
                try:
                    b=box_eval(causal,direction,sign,k)
                    mb=b['_min_beta']; mc=b['_min_chart']
                    global_min_beta=mb if global_min_beta is None or mb<global_min_beta else global_min_beta
                    global_min_chart=mc if global_min_chart is None or mc<global_min_chart else global_min_chart
                    all_classes += [q['classification'] for q in b['per_rho']]
                    boxes.append(b)
                except Exception as e:
                    method_blocker=True
                    boxes.append({'box':k,'error':repr(e)})
            try:
                pok,pchecks=point_containment(boxes,causal,direction,sign)
            except Exception as e:
                pok=False; pchecks=[{'error':repr(e)}]
            point_ok_all=point_ok_all and pok
            method_blocker=method_blocker or (not pok)
            paths.append({'direction':direction,'sign':sign,'point_regression_pass':bool(pok),
                          'point_regression':pchecks,'boxes_internal':boxes})
    if method_blocker:
        cls='ITER499_NUMERICAL_METHOD_BLOCKER'
    elif all(c=='INTERVAL_ROBUST_NONDECAY' for c in all_classes):
        cls='ITER499_DIRECT_MAX_ENVELOPE_INTERVAL_ROBUST_QUALIFIED_SCOPED'
    elif all(c in ('INTERVAL_ROBUST_NONDECAY','INTERVAL_NONDECAY') for c in all_classes):
        cls='ITER499_DIRECT_MAX_ENVELOPE_INTERVAL_NONDECAY_QUALIFIED_SCOPED'
    elif any(c=='INTERVAL_UNIFORM_DECAY_WITNESS' for c in all_classes):
        cls='SCIENTIFIC_FAIL_ITER499_UNIFORM_NONDECAY_INTERVAL'
    else:
        cls='ITER499_VALIDATED_INTERVAL_INCONCLUSIVE_SCOPED'
    outpaths=[]
    for p in paths:
        outpaths.append({'direction':p['direction'],'sign':p['sign'],'point_regression_pass':p['point_regression_pass'],
                         'point_regression':p['point_regression'],'boxes':[serialize_box(b) for b in p['boxes_internal']]})
    return {'iteration':499,'job':f'{causal}-b{block}','causal':causal,'block':block,
            'precision_bits':384,'python_flint_required':'0.9.0','interval_boxes':16,
            'intertwiner_regression_max_abs':float(int_reg),'intertwiner_regression_pass':init_ok,
            'point_regression_all_pass':bool(point_ok_all),'method_blocker':bool(method_blocker),
            'classification':cls,'valid':bool(not method_blocker),
            'min_beta_lower':(core.bound_float(global_min_beta,'lower') if global_min_beta is not None else None),
            'min_chart_norm2_lower':(core.bound_float(global_min_chart,'lower') if global_min_chart is not None else None),
            'paths':outpaths,
            'scope':'validated direct 243-channel max-envelope on 16 q=1 amplitude subintervals along frozen signed directions only; not a 6-D/20-D neighborhood theorem'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--causal',required=True,choices=['0to5','1to4','2to3']); ap.add_argument('--block',required=True,type=int,choices=range(4)); ap.add_argument('--out',required=True); a=ap.parse_args()
    try:
        out=evaluate(a.causal,a.block)
    except Exception as e:
        out={'iteration':499,'job':f'{a.causal}-b{a.block}','causal':a.causal,'block':a.block,
             'valid':False,'method_blocker':True,'classification':'ITER499_NUMERICAL_METHOD_BLOCKER','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps({k:v for k,v in out.items() if k!='paths'},indent=2,sort_keys=True))
    raise SystemExit(0)
if __name__=='__main__': main()
