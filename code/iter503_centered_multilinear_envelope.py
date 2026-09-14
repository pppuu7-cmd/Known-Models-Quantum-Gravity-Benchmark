#!/usr/bin/env python3
import argparse, json, os
import numpy as np
from flint import arb, acb, ctx

import iter499_arb_core as core
import iter500_compact_sandwich_kak as enable
import iter501_direct_max_envelope_interval as parent

ctx.prec = 384

TABS = np.empty(core.TSTACK.shape, dtype=object)
for idx in np.ndindex(core.TSTACK.shape):
    TABS[idx] = abs(core.TSTACK[idx])


def contract_abs_all(mats):
    args=[]; outlabels=list(range(20,25))
    for node in range(5):
        args += [TABS,[20+node]+core.ctrl.NODE_LABELS[node]]
    for ei,M in enumerate(mats):
        args += [np.asarray(M,dtype=object),core.ctrl.EDGE_LABELS[ei]]
    args += [outlabels]
    return np.einsum(*args,optimize=core.BALL_PATH)


def edge_mats(causal,direction,sign,R,amp):
    sig=core.SIGMAS[causal]
    st=enable.construct_state(R,direction,sign,amp)
    construction=all(x[2] for x in st['checks'])
    cycle=parent.cycle_contains(st['edges'])
    mats=[]; additive=True
    for e in core.EDGES:
        branch='p' if sig[e[0]]*sig[e[1]]>0 else 'm'
        M,ok=core.full_toller(st['edge_kak'][e],rho=edge_mats.rho,branch=branch)
        mats.append(M); additive=additive and ok
    return st,mats,bool(construction and cycle and additive)
edge_mats.rho = None


def generic_midpoint_vals(causal,direction,sign,R,rho,a0):
    sig=core.SIGMAS[causal]
    _,rs=core.geometry(R,direction,sign,a0)
    mats=[]; additive=True
    for e in core.EDGES:
        k=core.kak_ball(rs[e])
        branch='p' if sig[e[0]]*sig[e[1]]>0 else 'm'
        M,ok=core.full_toller(k,rho,branch)
        mats.append(M); additive=additive and ok
    return core.contract_all(mats),bool(additive)


def midpoint_regression(factorized_vals,generic_vals):
    ok=True; max_rel=0.0
    for z,w in zip(factorized_vals.flat,generic_vals.flat):
        z=core.C(z); w=core.C(w)
        wr=arb(w.real.mid()); wi=arb(w.imag.mid())
        contains=bool(z.real.contains(wr) and z.imag.contains(wi))
        ok=ok and contains
        zr=float(z.real.mid()); zi=float(z.imag.mid())
        gr=float(w.real.mid()); gi=float(w.imag.mid())
        den=max(1.0,abs(complex(gr,gi)))
        max_rel=max(max_rel,abs(complex(zr-gr,zi-gi))/den)
    return bool(ok),float(max_rel)


def centered_bounds(mats_box,mats0):
    B=[]; BP=[]
    for Mb,M0 in zip(mats_box,mats0):
        bmat=[]; pmat=[]
        for i in range(3):
            brow=[]; prow=[]
            for j in range(3):
                z0=core.C(M0[i][j]); zb=core.C(Mb[i][j])
                b=z0.abs_upper()
                r=(zb-z0).abs_upper()
                if not (b.is_finite() and r.is_finite()):
                    raise ArithmeticError('nonfinite centered edge radius')
                brow.append(b); prow.append(b+r)
            bmat.append(brow); pmat.append(prow)
        B.append(bmat); BP.append(pmat)
    vals0=core.contract_all(mats0)
    abase=contract_abs_all(B); ainfl=contract_abs_all(BP)
    lows=[]; ups=[]; delta_max=arb(0)
    for z,b,p in zip(vals0.flat,abase.flat,ainfl.flat):
        z=core.C(z); d=(p-b).upper()
        if d < arb(0):
            raise ArithmeticError('negative centered variation upper bound')
        if d>delta_max: delta_max=d
        lo=z.abs_lower()-d
        if lo<arb(0): lo=arb(0)
        up=z.abs_upper()+d
        if not (lo.is_finite() and up.is_finite()):
            raise ArithmeticError('nonfinite centered channel bound')
        lows.append(lo); ups.append(up)
    L=lows[0]; U=ups[0]
    for x in lows[1:]:
        if x>L: L=x
    for x in ups[1:]:
        if x>U: U=x
    possible=[i for i,u in enumerate(ups) if u>=L]
    return L,U,possible,delta_max,vals0


def eval_box(causal,direction,sign,k):
    amp,alo,ahi=core.box_amp(k); a0=(alo+ahi)/2
    perR={}; controls={'construction_cycle_additive':True,'midpoint_channel_regression':True}
    max_mid_rel=0.0; min_beta=None; all_positive=True
    for R in core.R_GRID:
        stb=enable.construct_state(R,direction,sign,amp)
        controls['construction_cycle_additive']=controls['construction_cycle_additive'] and all(x[2] for x in stb['checks']) and parent.cycle_contains(stb['edges'])
        st0=enable.construct_state(R,direction,sign,a0)
        controls['construction_cycle_additive']=controls['construction_cycle_additive'] and all(x[2] for x in st0['checks']) and parent.cycle_contains(st0['edges'])
        logH=arb(0)
        for kk in stb['node_kak'].values():
            b=kk['beta']; logH += 2*b.sinh().log()
            bl=b.lower(); min_beta=bl if min_beta is None or bl<min_beta else min_beta
        for kk in stb['edge_kak'].values():
            bl=kk['beta'].lower(); min_beta=bl if min_beta is None or bl<min_beta else min_beta
        rows=[]
        sig=core.SIGMAS[causal]
        for rho in core.RHOS:
            matsb=[]; mats0=[]; additive=True
            for e in core.EDGES:
                branch='p' if sig[e[0]]*sig[e[1]]>0 else 'm'
                Mb,okb=core.full_toller(stb['edge_kak'][e],rho,branch)
                M0,ok0=core.full_toller(st0['edge_kak'][e],rho,branch)
                matsb.append(Mb); mats0.append(M0); additive=additive and okb and ok0
            controls['construction_cycle_additive']=controls['construction_cycle_additive'] and additive
            L,U,possible,dmax,vals0=centered_bounds(matsb,mats0)
            gvals,gadd=generic_midpoint_vals(causal,direction,sign,R,rho,a0)
            mok,mrel=midpoint_regression(vals0,gvals)
            controls['midpoint_channel_regression']=controls['midpoint_channel_regression'] and mok and gadd
            max_mid_rel=max(max_mid_rel,mrel)
            positive=bool(L>arb(0)); all_positive=all_positive and positive
            row={'rho':rho,'positive':positive,'L':L,'U':U,'possible':possible,'delta_max':dmax}
            if positive:
                row['_ylo']=logH.lower()+L.log().lower(); row['_yhi']=logH.upper()+U.log().upper()
            rows.append(row)
        perR[R]={'logH':logH,'rho':rows}
    valid_controls=bool(all(controls.values()))
    eligible=bool(valid_controls and all_positive)
    per=[]
    if eligible:
        for ir,rho in enumerate(core.RHOS):
            y6l=perR[6]['rho'][ir]['_ylo']; y6u=perR[6]['rho'][ir]['_yhi']
            y8l=perR[8]['rho'][ir]['_ylo']; y8u=perR[8]['rho'][ir]['_yhi']
            y10l=perR[10]['rho'][ir]['_ylo']; y10u=perR[10]['rho'][ir]['_yhi']
            y12l=perR[12]['rho'][ir]['_ylo']; y12u=perR[12]['rho'][ir]['_yhi']
            per.append({'rho':rho,'_slo':(y12l-y8u)/4,'_shi':(y12u-y8l)/4,
                        '_elo':(y10l-y6u)/4,'_ehi':(y10u-y6l)/4})
    return {'box':k,'_alo':alo,'_ahi':ahi,'eligible':eligible,'controls':controls,'_min_beta':min_beta,
            'max_midpoint_channel_relative_residual':max_mid_rel,'_perR':perR,'per_rho':per}


def point_containment(boxes,causal,direction,sign):
    checks=[]; ok=True
    for j,a in enumerate(parent.POINT_AMPS):
        endpoint=2*j
        candidates=[0] if endpoint==0 else ([15] if endpoint==16 else [endpoint-1,endpoint])
        pp=parent.point_eval(causal,direction,sign,a)
        for ir,r in enumerate(pp):
            sv=arb(repr(r['actual_slope'])); ev=arb(repr(r['early_actual_slope']))
            hit=False
            for k in candidates:
                b=boxes[k]
                if not b.get('eligible'): continue
                q=b['per_rho'][ir]
                if q['_slo']<=sv<=q['_shi'] and q['_elo']<=ev<=q['_ehi']:
                    hit=True; break
            ok=ok and hit
            checks.append({'amplitude':a,'rho':r['rho'],'candidate_boxes':candidates,'contained':bool(hit)})
    return bool(ok),checks


def bf(x,side): return core.bound_float(x,side)


def serialize_box(b):
    rows=[]
    for R in core.R_GRID:
        rr=[]
        for q in b['_perR'][R]['rho']:
            rr.append({'rho':q['rho'],'positive':q['positive'],'envelope_lower':bf(q['L'],'lower'),
                       'envelope_upper':bf(q['U'],'upper'),'possible_max_count':len(q['possible']),
                       'delta_max_upper':bf(q['delta_max'],'upper')})
        rows.append({'R':R,'rho':rr})
    return {'box':b['box'],'amp_lower':bf(b['_alo'],'lower'),'amp_upper':bf(b['_ahi'],'upper'),
            'eligible':b['eligible'],'controls':b['controls'],
            'min_beta_lower':None if b['_min_beta'] is None else bf(b['_min_beta'],'lower'),
            'max_midpoint_channel_relative_residual':b['max_midpoint_channel_relative_residual'],
            'per_rho':[{'rho':q['rho'],'S_lower':bf(q['_slo'],'lower'),'S_upper':bf(q['_shi'],'upper'),
                        'E_lower':bf(q['_elo'],'lower'),'E_upper':bf(q['_ehi'],'upper')} for q in b['per_rho']],
            'per_R':rows}


def evaluate(causal):
    paths=[]; validation_fail=False; insufficient=False; point_all=True
    min_beta=None; max_mid_rel=0.0; positive_states=0; total_states=0
    for direction in core.BLOCKS[0]:
        for sign in (1,-1):
            boxes=[]
            for k in range(16):
                try:
                    b=eval_box(causal,direction,sign,k)
                except Exception as e:
                    validation_fail=True
                    boxes.append({'box':k,'error':repr(e),'eligible':False})
                    continue
                if not all(b['controls'].values()): validation_fail=True
                if not b['eligible']: insufficient=True
                if b['_min_beta'] is not None:
                    min_beta=b['_min_beta'] if min_beta is None or b['_min_beta']<min_beta else min_beta
                max_mid_rel=max(max_mid_rel,b['max_midpoint_channel_relative_residual'])
                for R in core.R_GRID:
                    for q in b['_perR'][R]['rho']:
                        total_states+=1; positive_states+=int(q['positive'])
                boxes.append(b)
            pok=False; pchecks=[]
            if len(boxes)==16 and all('error' not in b for b in boxes) and all(b.get('eligible') for b in boxes):
                try: pok,pchecks=point_containment(boxes,causal,direction,sign)
                except Exception as e:
                    validation_fail=True; pchecks=[{'error':repr(e)}]
                if not pok: validation_fail=True
            else:
                pchecks=[{'skipped':'at least one box is not eligible; method-insufficient path'}]
            point_all=point_all and (pok if all(b.get('eligible',False) for b in boxes) else True)
            paths.append({'direction':direction,'sign':sign,'point_regression_pass':bool(pok),'point_regression':pchecks,'boxes':boxes})
    if validation_fail:
        cls='INFRASTRUCTURE_OR_VALIDATION_FAIL_ITER503'
    elif insufficient:
        cls='ITER503_CENTERED_MULTILINEAR_METHOD_INSUFFICIENT_SCOPED'
    else:
        cls='ITER503_CENTERED_MULTILINEAR_METHOD_QUALIFIED_SCOPED'
    return {'iteration':503,'job':f'{causal}-b0','causal':causal,'block':0,'precision_bits':384,
            'valid':bool(not validation_fail),'method_insufficient':bool(insufficient),'classification':cls,
            'positive_envelope_states':int(positive_states),'total_envelope_states':int(total_states),
            'point_regression_all_pass':bool(point_all and not insufficient),
            'min_beta_lower':None if min_beta is None else bf(min_beta,'lower'),
            'max_midpoint_channel_relative_residual':float(max_mid_rel),
            'paths':[{'direction':p['direction'],'sign':p['sign'],'point_regression_pass':p['point_regression_pass'],
                      'point_regression':p['point_regression'],
                      'boxes':[({'box':b.get('box'),'error':b.get('error'),'eligible':False} if 'error' in b else serialize_box(b)) for b in p['boxes']]} for p in paths],
            'scope':'centered multilinear enclosure method diagnostic on frozen block 0 only; no NONDECAY/DECAY, multidimensional Haar, spectral, or physical-vertex theorem'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--causal',required=True,choices=['0to5','1to4','2to3']); ap.add_argument('--out',required=True); a=ap.parse_args()
    try: out=evaluate(a.causal)
    except Exception as e: out={'iteration':503,'job':f'{a.causal}-b0','causal':a.causal,'valid':False,'classification':'INFRASTRUCTURE_OR_VALIDATION_FAIL_ITER503','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps({k:v for k,v in out.items() if k!='paths'},indent=2,sort_keys=True))
    raise SystemExit(0)

if __name__=='__main__': main()
