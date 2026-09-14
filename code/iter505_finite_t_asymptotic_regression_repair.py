#!/usr/bin/env python3
import argparse, json, os
import iter504_fixed_causal_k5_full_collision_leading as base

base.T_COARSE = 1.25e-4
base.T_FINE = 6.25e-5

PASS='ITER505_FINITE_T_ASYMPTOTIC_REGRESSION_REPAIR_QUALIFIED_SCOPED'
FAIL='SCIENTIFIC_FAIL_ITER505_UNIFORM_FROZEN_FULL_COLLISION_LEADING_SURVIVAL'
BLOCK='BLOCKED_OR_INFRASTRUCTURE_ITER505'


def evaluate(panel, causal, rho):
    out = base.evaluate(panel, causal, rho)
    out['iteration'] = 505
    out['lane'] = f'{panel}-{causal}-rho{int(rho)}'
    out['t_coarse'] = base.T_COARSE
    out['t_fine'] = base.T_FINE
    out['scope'] = 'Iter504 fixed-causal j=1 full-K5 common-node full-collision leading coefficient with prospectively frozen smaller-t source regression only; no remainder, positive-measure, local-integrability, Haar, spectral-pairing or physical-vertex theorem'
    if not out.get('valid', False):
        out['classification'] = BLOCK
        out['pass'] = False
    elif float(out.get('max_ratio', 0.0)) > base.WITNESS_TOL:
        out['classification'] = PASS
        out['pass'] = True
    else:
        out['classification'] = FAIL
        out['pass'] = False
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--panel',required=True,choices=sorted(base.PANELS))
    ap.add_argument('--causal',required=True,choices=sorted(base.ctrl.SIGMAS))
    ap.add_argument('--rho',required=True,type=int,choices=base.RHOS)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    try:
        out=evaluate(a.panel,a.causal,a.rho)
    except Exception as e:
        out={'iteration':505,'lane':f'{a.panel}-{a.causal}-rho{a.rho}','panel':a.panel,'causal':a.causal,'rho':a.rho,'valid':False,'pass':False,'classification':BLOCK,'error':repr(e),'t_coarse':base.T_COARSE,'t_fine':base.T_FINE}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
