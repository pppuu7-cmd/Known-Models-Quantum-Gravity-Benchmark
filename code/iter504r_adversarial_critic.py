#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

PASS='ITER504R_ROOT_AFFINE_REUSE_NARROWED_WITHIN_TOLERANCE_SCOPED'
INC='ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED'
VERDICT_PASS='CRITIC_CONFIRMS_ITER504R_ROOT_AFFINE_REUSE_PASS_SCOPED'
VERDICT_INC='CRITIC_CONFIRMS_ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED'
VERDICT_FAIL='CRITIC_REJECTS_ITER504R_TERMINALIZATION'
ROOTS=(13,14,15)
RHOS=('0.35','0.9','1.6','2.7')
TOL=0.05
FLOOR=1.0
EPS=1e-12


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()


def fq(s): return Fraction(s)


def root_interval(k): return Fraction(16+k,12800),Fraction(17+k,12800)


def check_env(obj,parent):
    errors=[]
    roots=obj.get('roots',[])
    if [x.get('root_box') for x in roots] != list(ROOTS): errors.append('root_identity')
    all_leaves=[]
    unresolved=0
    certified=0
    total_nodes=0
    hist={}
    for root in roots:
        rb=root.get('root_box')
        if rb not in ROOTS:
            errors.append(f'bad_root:{rb}'); continue
        if root.get('root_model_build_count') != 1: errors.append(f'root_model_count:{rb}')
        if root.get('derivative_recomputed_on_descendants') is not False: errors.append(f'derivative_recompute:{rb}')
        if root.get('full_channel_count') != 243: errors.append(f'channel_count:{rb}')
        if root.get('channel_pruning_used_for_decision') is not False: errors.append(f'channel_pruning:{rb}')
        if not all(root.get('root_controls',{}).values()): errors.append(f'root_controls:{rb}')
        leaves=root.get('leaves',[])
        L=len(leaves)
        if root.get('leaf_count') != L: errors.append(f'leaf_count:{rb}')
        if root.get('node_count') != 2*L-1: errors.append(f'full_binary_node_invariant:{rb}')
        total_nodes += root.get('node_count',0)
        lo0,hi0=root_interval(rb)
        spans=[]
        for leaf in leaves:
            d=leaf.get('depth')
            if not isinstance(d,int) or d<0 or d>10: errors.append(f'depth:{rb}')
            lo,hi=fq(leaf['amp_lower_q']),fq(leaf['amp_upper_q'])
            spans.append((lo,hi,d,leaf))
            # exact dyadic descendant certificate
            width=hi0-lo0
            unit=width/(2**d)
            if hi-lo != unit: errors.append(f'dyadic_width:{rb}:{d}:{lo}')
            if (lo-lo0)/unit != int((lo-lo0)/unit): errors.append(f'dyadic_alignment:{rb}:{d}:{lo}')
            rows=leaf.get('per_rho',[])
            if [str(x.get('rho')) for x in rows] != list(RHOS): errors.append(f'rho_identity:{rb}:{d}:{lo}')
            row_cert=[]
            for rr in rows:
                calc=bool(float(rr['S_lower']) >= FLOOR and float(rr['drift_upper']) <= TOL)
                if bool(rr.get('certified')) != calc: errors.append(f'rho_cert_mismatch:{rb}:{d}:{lo}:{rr.get("rho")}')
                row_cert.append(calc)
            calc_leaf=all(row_cert)
            if bool(leaf.get('certified')) != calc_leaf: errors.append(f'leaf_cert_mismatch:{rb}:{d}:{lo}')
            st=leaf.get('leaf_status')
            if calc_leaf:
                certified+=1
                if st!='CERTIFIED': errors.append(f'certified_status:{rb}:{d}:{lo}')
            else:
                unresolved+=1
                if not (d==10 and st=='UNRESOLVED_DEPTH10'): errors.append(f'unresolved_status:{rb}:{d}:{lo}')
            hist[str(d)]=hist.get(str(d),0)+1
            all_leaves.append(leaf)
        spans.sort(key=lambda z:z[0])
        if not spans or spans[0][0]!=lo0 or spans[-1][1]!=hi0: errors.append(f'cover_endpoints:{rb}')
        for i in range(len(spans)-1):
            if spans[i][1]!=spans[i+1][0]: errors.append(f'cover_gap_overlap:{rb}:{i}')
        cov=root.get('cover',{})
        if cov.get('valid') is not True: errors.append(f'cover_flag:{rb}')
        # depth-zero regression to terminal Iter504 parent values
        p=parent['boxes'][str(rb)]
        rd=root.get('root_diagnostic',{})
        p_max=max(float(v['drift_upper']) for v in p['per_rho'].values())
        p_min=min(float(v['S_lower']) for v in p['per_rho'].values())
        if abs(float(rd.get('max_drift_upper'))-p_max)>EPS: errors.append(f'parent_max_drift_regression:{rb}')
        if abs(float(rd.get('min_S_lower'))-p_min)>EPS: errors.append(f'parent_min_S_regression:{rb}')
        if int(rd.get('max_possible_count')) != int(p['max_possible_count']): errors.append(f'parent_possible_regression:{rb}')
    expected_class = PASS if unresolved==0 and not errors else INC if not errors else None
    if expected_class and obj.get('classification') != expected_class: errors.append('classification_mismatch')
    if obj.get('total_node_count') != total_nodes: errors.append('aggregate_node_count')
    if obj.get('total_leaf_count') != len(all_leaves): errors.append('aggregate_leaf_count')
    if obj.get('certified_leaf_count') != certified: errors.append('aggregate_certified_count')
    if obj.get('unresolved_leaf_count') != unresolved: errors.append('aggregate_unresolved_count')
    if obj.get('leaf_depth_histogram') != dict(sorted(hist.items(),key=lambda z:int(z[0]))): errors.append('depth_histogram')
    if all_leaves:
        worst=max(all_leaves,key=lambda x:float(x['max_drift_upper']))
        if abs(float(obj.get('max_terminal_leaf_drift_upper'))-float(worst['max_drift_upper']))>EPS: errors.append('max_leaf_drift')
        mins=min(float(x['min_S_lower']) for x in all_leaves)
        if abs(float(obj.get('minimum_terminal_leaf_S_lower'))-mins)>EPS: errors.append('min_leaf_S')
    return {
        'errors':errors,
        'unresolved':unresolved,
        'certified':certified,
        'leaf_count':len(all_leaves),
        'node_count':total_nodes,
        'expected_classification':expected_class,
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--a',required=True);ap.add_argument('--b',required=True);ap.add_argument('--parent',required=True);ap.add_argument('--out',required=True)
    a=ap.parse_args()
    A,Ah=read(a.a);B,Bh=read(a.b);P,_=read(a.parent)
    ca=check_env(A,P);cb=check_env(B,P)
    errors=[]
    if ca['errors']: errors += ['A:'+x for x in ca['errors']]
    if cb['errors']: errors += ['B:'+x for x in cb['errors']]
    byte_identical=Ah==Bh
    if not byte_identical: errors.append('assembled_outputs_not_byte_identical')
    if A.get('classification')!=B.get('classification'): errors.append('cross_environment_classification')
    cls=A.get('classification') if not errors else None
    if cls==PASS: verdict=VERDICT_PASS
    elif cls==INC: verdict=VERDICT_INC
    else: verdict=VERDICT_FAIL
    out={
      'verdict':verdict,'terminal_classification':cls,
      'assembled_a_sha256':Ah,'assembled_b_sha256':Bh,
      'assembled_outputs_byte_identical':byte_identical,
      'environment_a':ca,'environment_b':cb,'errors':errors,
      'parent_depth_zero_regression_checked':True,
      'exact_dyadic_cover_checked':True,
      'full_binary_tree_node_invariant_checked':True,
      'all_243_channels_no_pruning_checked':True,
      'threshold':TOL,'robust_floor':FLOOR,
      'claim_ceiling':'Critic of three-box Iter504R diagnostic only; no full-domain theorem or global D7 conclusion'
    }
    core=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['critic_sha256']=hashlib.sha256(core).hexdigest()
    p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));return 0 if not errors else 2
if __name__=='__main__': raise SystemExit(main())
