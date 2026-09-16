#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

PASS='ITER504R_ROOT_AFFINE_REUSE_NARROWED_WITHIN_TOLERANCE_SCOPED'
INCONCLUSIVE='ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED'
INVALID='ITER504R_ROOT_AFFINE_REUSE_INVALID'
GATE='ITER504R_ROOT_AFFINE_REUSE_CONTINUOUS_DRIFT_DIAGNOSTIC_GATE'
PREREG='147d68f26ed3a14ce3cd1fd77fcd96d5fb329ec8'


def load(p): return json.loads(Path(p).read_text())


def main():
    ap=argparse.ArgumentParser()
    for k in (13,14,15): ap.add_argument(f'--box{k}', required=True)
    ap.add_argument('--out', required=True)
    a=ap.parse_args()
    roots=[load(getattr(a,f'box{k}')) for k in (13,14,15)]
    roots.sort(key=lambda x:x.get('root_box',-1))
    invalid = [x.get('root_box') for x in roots if x.get('invalid')]
    identity_ok=[x.get('root_box') for x in roots]==[13,14,15]
    covers_ok=identity_ok and all(x.get('cover',{}).get('valid') for x in roots)
    controls_ok=identity_ok and all(all(x.get('root_controls',{}).values()) for x in roots)
    model_count_ok=identity_ok and all(x.get('root_model_build_count')==1 and x.get('derivative_recomputed_on_descendants') is False for x in roots)
    channels_ok=identity_ok and all(x.get('full_channel_count')==243 and x.get('channel_pruning_used_for_decision') is False for x in roots)
    unresolved=sum(int(x.get('unresolved_leaf_count',0)) for x in roots) if identity_ok else None
    if invalid or not (covers_ok and controls_ok and model_count_ok and channels_ok): cls=INVALID
    elif unresolved: cls=INCONCLUSIVE
    else: cls=PASS
    leaves=[leaf for r in roots for leaf in r.get('leaves',[])]
    worst=max(leaves,key=lambda x:x['max_drift_upper']) if leaves else None
    hist=Counter()
    for r in roots:
        for k,v in r.get('leaf_depth_histogram',{}).items(): hist[k]+=v
    per_rho={}
    for rho in ('0.35','0.9','1.6','2.7'):
        rows=[]
        for r in roots:
            for leaf in r.get('leaves',[]):
                for rr in leaf.get('per_rho',[]):
                    if str(rr['rho'])==rho:
                        rows.append((rr['drift_upper'],r['root_box'],leaf,rr))
        if rows:
            d,rb,leaf,rr=max(rows,key=lambda z:z[0])
            per_rho[rho]={
                'max_drift_upper':d,'root_box':rb,'depth':leaf['depth'],
                'amp_lower_q':leaf['amp_lower_q'],'amp_upper_q':leaf['amp_upper_q'],
                'S_lower':rr['S_lower'],'certified':rr['certified']}
    out={
        'gate':GATE,'preregistration_commit':PREREG,'classification':cls,
        'root_identity_ok':identity_ok,'exact_covers_valid':covers_ok,
        'root_controls_valid':controls_ok,'root_model_build_count_valid':model_count_ok,
        'all_243_channels_retained':channels_ok,
        'total_node_count':sum(x.get('node_count',0) for x in roots),
        'total_leaf_count':sum(x.get('leaf_count',0) for x in roots),
        'certified_leaf_count':sum(x.get('certified_leaf_count',0) for x in roots),
        'unresolved_leaf_count':unresolved,
        'leaf_depth_histogram':dict(sorted(hist.items(),key=lambda z:int(z[0]))),
        'per_root_leaf_count':{str(x['root_box']):x.get('leaf_count') for x in roots if 'root_box' in x},
        'root_max_drift':{str(x['root_box']):x.get('root_diagnostic',{}).get('max_drift_upper') for x in roots if 'root_box' in x},
        'root_max_possible_counts':{str(x['root_box']):x.get('root_diagnostic',{}).get('max_possible_count') for x in roots if 'root_box' in x},
        'max_terminal_leaf_possible_count':max((x.get('max_terminal_leaf_possible_count',0) for x in roots),default=None),
        'max_terminal_leaf_drift_upper':None if worst is None else worst['max_drift_upper'],
        'max_terminal_leaf_drift_witness':None if worst is None else {
            'root_box':worst['root_box'],'depth':worst['depth'],
            'amp_lower_q':worst['amp_lower_q'],'amp_upper_q':worst['amp_upper_q'],
            'delta_lower_q':worst['delta_lower_q'],'delta_upper_q':worst['delta_upper_q'],
            'leaf_status':worst['leaf_status'],'max_possible_count':worst['max_possible_count']},
        'minimum_terminal_leaf_S_lower':min((x.get('minimum_terminal_leaf_S_lower') for x in roots if x.get('minimum_terminal_leaf_S_lower') is not None),default=None),
        'per_rho_worst':per_rho,
        'covers':{str(x['root_box']):x.get('cover') for x in roots if 'root_box' in x},
        'roots':roots,
        'claim_ceiling':'three-root-box continuous diagnostic only; no full-domain theorem, Haar/divergence theorem, D7 closure, selector, model/family or new-physics conclusion'
    }
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='roots'},indent=2,sort_keys=True))
    return 0 if cls!=INVALID else 2

if __name__=='__main__': raise SystemExit(main())
