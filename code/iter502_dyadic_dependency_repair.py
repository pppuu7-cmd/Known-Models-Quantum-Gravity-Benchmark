#!/usr/bin/env python3
import argparse, json, os
from flint import arb, ctx

import iter499_arb_core as core
import iter501_direct_max_envelope_interval as prev

ctx.prec=384
SUBDIV=8


def sub_bounds(k,s):
    if k not in range(16) or s not in range(SUBDIV): raise ValueError((k,s))
    den=12800*SUBDIV
    lo=arb(f'{SUBDIV*(16+k)+s}/{den}')
    hi=arb(f'{SUBDIV*(16+k)+s+1}/{den}')
    return lo.union(hi),lo,hi


def eval_subbox(causal,direction,sign,k,s):
    amp,lo,hi=sub_bounds(k,s)
    old=core.box_amp
    try:
        core.box_amp=lambda kk:(amp,lo,hi)
        b=prev.box_eval(causal,direction,sign,k)
    finally:
        core.box_amp=old
    b['parent_box']=k; b['subbox']=s; b['_alo']=lo; b['_ahi']=hi
    return b


def eligible(b,a):
    aa=arb(repr(float(a)))
    return bool(b['_alo'] <= aa and aa <= b['_ahi'])


def point_containment(boxes,causal,direction,sign):
    checks=[]; ok=True
    for a in prev.POINT_AMPS:
        pp=prev.point_eval(causal,direction,sign,a)
        cand=[b for b in boxes if not b.get('error') and eligible(b,a)]
        for ir,r in enumerate(pp):
            sv=arb(repr(r['actual_slope'])); ev=arb(repr(r['early_actual_slope']))
            hit=False; ids=[]
            for b in cand:
                q=b['per_rho'][ir]
                if q['_slo']<=sv<=q['_shi'] and q['_elo']<=ev<=q['_ehi']:
                    hit=True; ids.append([b['parent_box'],b['subbox']])
            ok=ok and hit
            checks.append({'amplitude':a,'rho':r['rho'],'eligible_subboxes':len(cand),'contained':bool(hit),'containing_subboxes':ids})
    return bool(ok),checks


def bf(x,side): return core.bound_float(x,side)


def compact_box(b):
    if b.get('error'): return b
    return {'parent_box':b['parent_box'],'subbox':b['subbox'],
            'amp_lower':bf(b['_alo'],'lower'),'amp_upper':bf(b['_ahi'],'upper'),
            'controls':b['controls'],'min_beta_lower':bf(b['_min_beta'],'lower'),
            'per_rho':[{'rho':q['rho'],'classification':q['classification'],
                        'S_lower':bf(q['_slo'],'lower'),'S_upper':bf(q['_shi'],'upper'),
                        'E_lower':bf(q['_elo'],'lower'),'E_upper':bf(q['_ehi'],'upper'),
                        'drift_upper':bf(q['_du'],'upper')} for q in b['per_rho']]}


def evaluate(causal,block):
    paths=[]; method=False; all_classes=[]; point_all=True; global_min_beta=None
    for direction in core.BLOCKS[block]:
        for sign in (1,-1):
            boxes=[]
            for k in range(16):
                for s in range(SUBDIV):
                    try:
                        b=eval_subbox(causal,direction,sign,k,s)
                        mb=b['_min_beta']; global_min_beta=mb if global_min_beta is None or mb<global_min_beta else global_min_beta
                        all_classes += [q['classification'] for q in b['per_rho']]
                        boxes.append(b)
                    except Exception as e:
                        method=True; boxes.append({'parent_box':k,'subbox':s,'error':repr(e)})
            try: pok,pchecks=point_containment(boxes,causal,direction,sign)
            except Exception as e: pok=False; pchecks=[{'error':repr(e)}]
            point_all=point_all and pok; method=method or (not pok)
            paths.append({'direction':direction,'sign':sign,'point_regression_pass':bool(pok),
                          'point_regression':pchecks,'subboxes':[compact_box(b) for b in boxes]})
    if method: cls='ITER502_NUMERICAL_METHOD_BLOCKER'
    elif all_classes and all(c=='INTERVAL_ROBUST_NONDECAY' for c in all_classes): cls='ITER502_DYADIC_DIRECT_MAX_ENVELOPE_INTERVAL_ROBUST_QUALIFIED_SCOPED'
    elif all_classes and all(c in ('INTERVAL_ROBUST_NONDECAY','INTERVAL_NONDECAY') for c in all_classes): cls='ITER502_DYADIC_DIRECT_MAX_ENVELOPE_INTERVAL_NONDECAY_QUALIFIED_SCOPED'
    elif any(c=='INTERVAL_UNIFORM_DECAY_WITNESS' for c in all_classes): cls='SCIENTIFIC_FAIL_ITER502_UNIFORM_NONDECAY_INTERVAL'
    else: cls='ITER502_VALIDATED_INTERVAL_INCONCLUSIVE_SCOPED'
    return {'iteration':502,'job':f'{causal}-b{block}','causal':causal,'block':block,
            'precision_bits':384,'subdivisions_per_iter501_box':SUBDIV,'subboxes_per_signed_direction':128,
            'valid':bool(not method),'method_blocker':bool(method),'classification':cls,
            'point_regression_all_pass':bool(point_all),'min_beta_lower':None if global_min_beta is None else bf(global_min_beta,'lower'),
            'interval_classes_count':len(all_classes),'paths':paths,
            'scope':'prospectively frozen exact 8-way cover of each Iter501 amplitude box; same 243-channel direct max-envelope and same scientific thresholds; numerical dependency-repair prerequisite only'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--causal',required=True,choices=['0to5','1to4','2to3']); ap.add_argument('--block',required=True,type=int,choices=range(4)); ap.add_argument('--out',required=True); a=ap.parse_args()
    try: out=evaluate(a.causal,a.block)
    except Exception as e: out={'iteration':502,'job':f'{a.causal}-b{a.block}','causal':a.causal,'block':a.block,'valid':False,'method_blocker':True,'classification':'ITER502_NUMERICAL_METHOD_BLOCKER','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps({k:v for k,v in out.items() if k!='paths'},indent=2,sort_keys=True))
    raise SystemExit(0)
if __name__=='__main__': main()
