#!/usr/bin/env python3
"""Iter503D outcome-blind dual source-identity verifier."""
import argparse, json, os
from flint import acb, ctx
import iter499_arb_core as core
import iter503_ad_core as ad

ctx.prec = 384
DIRECTION = [1,1,1,-1,-1,-1]
SIGN = 1
BOXES = [0,7,15]


def cfinite(z):
    z = acb(z)
    return bool(z.real.is_finite() and z.imag.is_finite())


def evaluate_box(k):
    if k not in BOXES:
        raise ValueError(k)
    amp, lo, hi = core.box_amp(k)
    checks = []
    construction_ok = True
    finite_ok = True
    value_ok = True
    derivative_ok = True
    for R in core.R_GRID:
        ds = ad.construct_dual_state(R, DIRECTION, SIGN, ad.RD(amp,1))
        construction_ok = construction_ok and all(bool(x[2]) for x in ds['checks'])
        for edge in core.EDGES:
            beta = ds['edge_kak'][edge]['beta']
            finite_ok = finite_ok and beta.v.is_finite() and beta.d.is_finite()
            for rho in core.RHOS:
                for m in (-1,0,1):
                    d,p,n = ad.dsource_coeffs(m,rho,beta)
                    rv = p.v + n.v - d.v
                    rd = p.d + n.d - d.d
                    vh = bool(rv.contains(0))
                    dh = bool(rd.contains(0))
                    fin = all(cfinite(z) for z in (d.v,d.d,p.v,p.d,n.v,n.d,rv,rd))
                    value_ok = value_ok and vh
                    derivative_ok = derivative_ok and dh
                    finite_ok = finite_ok and fin
                    checks.append({
                        'R': int(R), 'edge': list(edge), 'rho': float(rho), 'm': int(m),
                        'value_residual_contains_zero': vh,
                        'derivative_residual_contains_zero': dh,
                        'finite': fin,
                    })
    complete = len(checks) == 480
    controls = {'construction': bool(construction_ok), 'finite': bool(finite_ok), 'complete': bool(complete)}
    if not all(controls.values()):
        cls = 'ITER503D_INVALID_OR_BLOCKED'
    elif value_ok and derivative_ok:
        cls = 'ITER503D_DUAL_SOURCE_IDENTITY_CONFIRMED'
    else:
        cls = 'ITER503D_DUAL_SOURCE_IDENTITY_VIOLATION'
    return {
        'iteration':'503D', 'box':k,
        'amp_lower': core.bound_float(lo,'lower'), 'amp_upper': core.bound_float(hi,'upper'),
        'expected_identities':480, 'completed_identities':len(checks),
        'value_all_contain_zero':bool(value_ok),
        'derivative_all_contain_zero':bool(derivative_ok),
        'controls':controls, 'classification':cls, 'checks':checks,
        'scope':'dual source identity implementation audit only; no DECAY/NONDECAY, D7 or selector claim',
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--box',type=int,required=True,choices=BOXES); ap.add_argument('--out',required=True); a=ap.parse_args()
    try:
        out=evaluate_box(a.box)
    except Exception as e:
        out={'iteration':'503D','box':a.box,'classification':'ITER503D_INVALID_OR_BLOCKED','error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
    print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2,sort_keys=True))
    raise SystemExit(0)

if __name__=='__main__': main()
