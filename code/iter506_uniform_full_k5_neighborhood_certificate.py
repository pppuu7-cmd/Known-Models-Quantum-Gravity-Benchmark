#!/usr/bin/env python3
import argparse, json, math, os
import numpy as np
import iter505_finite_t_asymptotic_regression_repair as prev

base = prev.base
ETAS = (1e-12, 1e-10, 1e-8, 1e-6)
PASS = 'ITER506_UNIFORM_FULL_K5_NEIGHBORHOOD_CERTIFIED_SCOPED'
FAIL = 'SCIENTIFIC_FAIL_ITER506_NO_CERTIFIED_OPEN_NEIGHBORHOOD_AT_FROZEN_RADII'
BLOCK = 'BLOCKED_OR_INFRASTRUCTURE_ITER506'


def edge_variation_bound(panel, causal, rho, eta, lead):
    sig = base.ctrl.SIGMAS[causal]
    deltas = []
    coeff_controls = []
    geom_ok = True
    for ei, ((a,b), w, r, n) in enumerate(lead['data']):
        d = 2.0 * eta
        rminus = r - d
        if not (rminus > 0.0):
            geom_ok = False
            deltas.append(float('inf'))
            coeff_controls.append(False)
            continue
        plus = bool(sig[a] * sig[b] > 0)
        bm = base.beta_coeff(-1, rho, plus)
        b0 = base.beta_coeff(0, rho, plus)
        bp = base.beta_coeff(1, rho, plus)
        aa = b0
        bb = (bp - bm) / 2.0
        cc = (bp + bm) / 2.0 - b0
        finite_coeffs = all(np.isfinite(abs(z)) for z in (aa,bb,cc))
        coeff_controls.append(bool(finite_coeffs))
        dn = 2.0 * d / rminus
        directional = abs(bb) * math.sqrt(2.0) * dn + abs(cc) * (2.0 * math.sqrt(2.0) * dn + 2.0 * dn * dn)
        center_frob = float(np.linalg.norm(lead['mats'][ei], ord='fro'))
        magnetic_frob_bound = (r ** 3) * center_frob
        radial = (rminus ** -3 - r ** -3) * magnetic_frob_bound
        delta = radial + (rminus ** -3) * directional
        deltas.append(float(delta))
    return deltas, bool(geom_ok and all(coeff_controls))


def evaluate(panel, causal, rho):
    rho = int(rho)
    upstream = prev.evaluate(panel, causal, rho)
    lead = base.leading_mats(panel, causal, rho)
    ts = [base.ctrl.intertwiner(i) for i in range(3)]
    path = base.ctrl.contraction_path(ts)
    vals = base.contraction_values(ts, path, lead['mats'])
    absvals = np.abs(vals)
    imax = int(np.argmax(absvals))
    channel = base.CHANNELS[imax]
    center_amp = float(absvals[imax])
    tensor_prefactor = float(np.prod([np.linalg.norm(ts[channel[v]], ord='fro') for v in range(5)]))
    center_edge_frob = [float(np.linalg.norm(M, ord='fro')) for M in lead['mats']]
    center_prod = float(np.prod(center_edge_frob))
    scale_maxabs = float(np.prod([base.src.maxabs(M) for M in lead['mats']]))

    radii = []
    analytic_ok = True
    for eta in ETAS:
        deltas, edge_ok = edge_variation_bound(panel, causal, rho, eta, lead)
        if edge_ok and all(np.isfinite(d) and d >= 0.0 for d in deltas):
            enlarged_prod = float(np.prod([b+d for b,d in zip(center_edge_frob, deltas)]))
            variation = tensor_prefactor * max(0.0, enlarged_prod - center_prod)
            margin = center_amp - variation
            normalized_margin = margin / max(scale_maxabs, 1e-300)
            certified = bool(np.isfinite(variation) and variation >= 0.0 and margin > 0.0)
        else:
            variation = float('inf')
            margin = float('-inf')
            normalized_margin = float('-inf')
            certified = False
            analytic_ok = False
        radii.append({
            'eta': eta,
            'certified_variation_bound': variation,
            'center_amplitude': center_amp,
            'margin': margin,
            'normalized_margin': normalized_margin,
            'certified': certified,
            'max_edge_delta_frobenius': max(deltas) if deltas else float('nan'),
        })

    certified_etas = [x['eta'] for x in radii if x['certified']]
    checks = {
        'iter505_lane_valid': bool(upstream.get('valid', False) and upstream.get('pass', False)),
        'center_contraction_finite_nonzero': bool(np.isfinite(center_amp) and center_amp > 0.0),
        'center_edge_norms_finite_positive': bool(all(np.isfinite(x) and x > 0.0 for x in center_edge_frob)),
        'tensor_prefactor_finite_positive': bool(np.isfinite(tensor_prefactor) and tensor_prefactor > 0.0),
        'analytic_edge_bounds_valid': bool(analytic_ok),
        'frozen_max_eta_geometrically_admissible': bool(all(2.0*max(ETAS) < float(r) for _,_,r,_ in lead['data'])),
        'center_channel_fixed_before_eta_scan': True,
    }
    controls_valid = bool(all(checks.values()))
    if not controls_valid:
        cls, passed = BLOCK, False
    elif ETAS[0] in certified_etas:
        cls, passed = PASS, True
    else:
        cls, passed = FAIL, False

    return {
        'iteration': 506,
        'lane': f'{panel}-{causal}-rho{rho}',
        'panel': panel,
        'causal': causal,
        'rho': rho,
        'valid': controls_valid,
        'pass': passed,
        'classification': cls,
        'checks': checks,
        'center_channel_index': imax,
        'center_channel': list(channel),
        'center_amplitude': center_amp,
        'center_normalized_witness_ratio': float(upstream.get('max_ratio', 0.0)),
        'tensor_prefactor': tensor_prefactor,
        'center_edge_frobenius_product': center_prod,
        'center_scale_maxabs_product': scale_maxabs,
        'frozen_etas': list(ETAS),
        'radii': radii,
        'largest_certified_eta': max(certified_etas) if certified_etas else 0.0,
        'smallest_certified_eta': min(certified_etas) if certified_etas else 0.0,
        'scope': 'fixed-causal j=1 full-K5 leading contraction; analytic open coordinate-neighborhood certificate only; no Haar, spectral pairing, physical-vertex, D7-S2 closure, or terminal-classifier claim',
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--panel', required=True, choices=sorted(base.PANELS))
    ap.add_argument('--causal', required=True, choices=sorted(base.ctrl.SIGMAS))
    ap.add_argument('--rho', required=True, type=int, choices=base.RHOS)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    try:
        out = evaluate(a.panel, a.causal, a.rho)
    except Exception as e:
        out = {'iteration':506,'lane':f'{a.panel}-{a.causal}-rho{a.rho}','panel':a.panel,'causal':a.causal,'rho':a.rho,'valid':False,'pass':False,'classification':BLOCK,'error':repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    with open(a.out, 'w') as f:
        json.dump(out, f, indent=2, sort_keys=True)
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
