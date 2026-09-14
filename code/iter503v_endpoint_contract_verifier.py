#!/usr/bin/env python3
"""Iter503V outcome-blind raw endpoint-contract verifier.

Independently compares high-precision point Y(R,rho,a) values from the established
Iter491/492 point path against Iter503 centered per-R Y enclosures.
"""
import argparse
import json
import math
import os

import mpmath as mp
import numpy as np
from flint import arb, ctx

import iter486_shared_node_haar_escape as base
import iter490_angular_neighborhood_thickening as parent
import iter491_high_precision_angular_thickening as hp
import iter499_arb_core as core
import iter500_compact_sandwich_kak as enable
import iter501_direct_max_envelope_interval as prev
import iter503_ad_core as ad

ctx.prec = 384
mp.mp.dps = 130

DIRECTION = [1, 1, 1, -1, -1, -1]
SIGN = 1
BOXES = [0, 7, 15]
CAUSALS = ['0to5', '1to4', '2to3']


def centered_raw(causal, k):
    amp, lo, hi = core.box_amp(k)
    mid = (lo + hi) / 2
    h = (hi - lo) / 2
    delta = (-h).union(h)
    dual_amp = ad.RD(amp, 1)
    sig = core.SIGMAS[causal]
    controls = {
        'construction': True,
        'cycle': True,
        'source_additive': True,
        'finite_envelope': True,
        'center_regression': True,
    }
    perR = {}
    for R in core.R_GRID:
        ds = ad.construct_dual_state(R, DIRECTION, SIGN, dual_amp)
        controls['construction'] = controls['construction'] and all(x[2] for x in ds['checks'])
        controls['cycle'] = controls['cycle'] and prev.cycle_contains(
            {e: ad.value_matrix(M) for e, M in ds['edges'].items()}
        )

        raw = enable.construct_state(R, DIRECTION, SIGN, mid)
        reg = enable.source_regression(R, DIRECTION, SIGN, mid, raw)
        controls['center_regression'] = controls['center_regression'] and bool(reg['pass'])

        dlogH = ad.RD(0, 0)
        raw_logH = arb(0)
        for kk in ds['node_kak'].values():
            dlogH += 2 * kk['beta'].sinh().log()
        for kk in raw['node_kak'].values():
            raw_logH += 2 * kk['beta'].sinh().log()
        centered_logH = raw_logH + delta * dlogH.d

        rows = []
        for rho in core.RHOS:
            dmats = []
            rmats = []
            add_ok = True
            for e in core.EDGES:
                branch = 'p' if sig[e[0]] * sig[e[1]] > 0 else 'm'
                dM, dok = ad.dfull_toller(ds['edge_kak'][e], rho, branch)
                rM, rok = core.full_toller(raw['edge_kak'][e], rho, branch)
                dmats.append(dM)
                rmats.append(rM)
                add_ok = add_ok and dok and rok
            controls['source_additive'] = controls['source_additive'] and add_ok
            dvals = ad.dcontract_all(dmats)
            rvals = core.contract_all(rmats)
            vals = ad.centered_channels(rvals, dvals, delta)
            L, U, possible = core.envelope_bounds(vals)
            finite = bool(L > arb(0) and U.is_finite())
            controls['finite_envelope'] = controls['finite_envelope'] and finite
            if not finite:
                raise ArithmeticError('centered nonfinite/nonpositive max envelope')
            ylo = centered_logH.lower() + L.log().lower()
            yhi = centered_logH.upper() + U.log().upper()
            rows.append({'rho': float(rho), '_ylo': ylo, '_yhi': yhi,
                         'possible_max_count': len(possible)})
        perR[int(R)] = rows

    if not all(controls.values()):
        raise ArithmeticError(f'centered controls failed: {controls}')
    return {'lo': lo, 'hi': hi, 'mid': mid, 'controls': controls, 'perR': perR}


def high_precision_point_raw(causal, amplitude):
    """Established Iter491/492 point geometry/KAK/Toller/contraction, exposing raw Y."""
    sig = base.SIGMAS[causal]
    d = np.zeros(20, dtype=float)
    for j, c in enumerate(core.COORDS):
        d[c] = float(DIRECTION[j])
    v = float(SIGN) * d

    node_det = mp.mpf('0')
    edge_det = mp.mpf('0')
    cycle = mp.mpf('0')
    kak_recon = mp.mpf('0')
    kak_unit = mp.mpf('0')
    kak_det = mp.mpf('0')
    identity = 0.0
    additive = 0.0
    all_positive = True
    perR = {}

    for R in base.R_GRID:
        eps = float(float(amplitude) * math.exp(-float(R)))
        gs, rs = hp.geometry_bundle(float(R), v, eps, dps=hp.PRIMARY_DPS)
        node_det = max(node_det, max(abs(hp.det2(g) - 1) for g in gs))
        edge_det = max(edge_det, max(abs(hp.det2(h) - 1) for h in rs.values()))
        cycle = max(cycle, hp.hp_cycle_residual(rs))

        old_gs = parent.perturb(base.escaped_nodes('C', 4, float(R)), v, eps)
        old_rs = base.relatives(old_gs)
        for e in hp.EDGES:
            identity = max(identity, hp.source_identity_residual(rs[e], old_rs[e]))

        logH = mp.mpf('0')
        for a in range(1, 5):
            _, beta_node, _, rec, uu, dd = hp.hp_kak(gs[a], dps=hp.PRIMARY_DPS)
            kak_recon = max(kak_recon, rec)
            kak_unit = max(kak_unit, uu)
            kak_det = max(kak_det, dd)
            logH += 2 * mp.log(mp.sinh(beta_node))

        edge_kak = {}
        for e in hp.EDGES:
            U1, beta, U2, rec, uu, dd = hp.hp_kak(rs[e], dps=hp.PRIMARY_DPS)
            kak_recon = max(kak_recon, rec)
            kak_unit = max(kak_unit, uu)
            kak_det = max(kak_det, dd)
            edge_kak[e] = (hp.to_np(U1), float(beta), hp.to_np(U2))

        rows = []
        for rho in base.RHOS:
            mats = []
            lognorm = 0.0
            for e in hp.EDGES:
                U1, beta, U2 = edge_kak[e]
                D, Tp, Tm = base.full_from_kak(U1, beta, U2, rho)
                additive = max(additive, base.maxabs(Tp + Tm - D))
                M = Tp if sig[e[0]] * sig[e[1]] > 0 else Tm
                n = base.maxabs(M)
                if not np.isfinite(n) or n <= 0:
                    all_positive = False
                    mats.append(M)
                else:
                    mats.append(M / n)
                    lognorm += math.log(n)
            vals = np.asarray(
                [base.contract(ch, hp.TS, mats, hp.PATH) for ch in hp.CHANNELS],
                dtype=np.complex128,
            )
            finite = bool(np.all(np.isfinite(vals.real)) and np.all(np.isfinite(vals.imag)))
            m = float(np.max(np.abs(vals))) if finite else float('nan')
            positive = bool(finite and np.isfinite(m) and m > 0)
            all_positive = all_positive and positive
            y = float(logH) + lognorm + math.log(m) if positive else float('nan')
            rows.append({'rho': float(rho), 'Y': y})
        perR[int(R)] = rows

    controls = {
        'hp_node_det': bool(node_det < hp.HP_GROUP_TOL),
        'hp_edge_det': bool(edge_det < hp.HP_GROUP_TOL),
        'hp_kak_reconstruction': bool(kak_recon < hp.HP_GROUP_TOL),
        'hp_kak_su2_unitarity': bool(kak_unit < hp.HP_GROUP_TOL),
        'hp_kak_su2_det': bool(kak_det < hp.HP_GROUP_TOL),
        'hp_cycle': bool(cycle < hp.HP_GROUP_TOL),
        'source_object_identity': bool(identity < float(hp.EDGE_ID_REL_TOL)),
        'finite_positive': bool(all_positive),
        'source_additive': bool(additive < 1e-9),
    }
    # The raw-Y verifier does not form a slope difference, so the Iter492
    # Haar-bookkeeping identity is not a separate numerical observable here.
    if not all(controls.values()):
        raise ArithmeticError(f'point controls failed: {controls}')
    return {'controls': controls, 'perR': perR}


def evaluate_box(k):
    if k not in BOXES:
        raise ValueError(k)
    rows = []
    all_ok = True
    total_checks = 0
    for causal in CAUSALS:
        try:
            centered = centered_raw(causal, k)
            endpoints = [
                ('lo', float(centered['lo'].mid())),
                ('hi', float(centered['hi'].mid())),
            ]
            point_controls = []
            checks = []
            for label, a in endpoints:
                point = high_precision_point_raw(causal, a)
                point_controls.append({'endpoint': label, 'amplitude': a,
                                       'controls': point['controls']})
                for R in core.R_GRID:
                    for ir, rho in enumerate(core.RHOS):
                        y = float(point['perR'][int(R)][ir]['Y'])
                        yy = arb(repr(y))
                        q = centered['perR'][int(R)][ir]
                        hit = bool(q['_ylo'] <= yy <= q['_yhi'])
                        all_ok = all_ok and hit
                        total_checks += 1
                        checks.append({
                            'endpoint': label,
                            'amplitude': a,
                            'R': int(R),
                            'rho': float(rho),
                            'Y_point': y,
                            'Y_lower': core.bound_float(q['_ylo'], 'lower'),
                            'Y_upper': core.bound_float(q['_yhi'], 'upper'),
                            'contained': hit,
                            'possible_max_count': q['possible_max_count'],
                        })
            rows.append({'causal': causal, 'centered_controls': centered['controls'],
                         'point_controls': point_controls, 'checks': checks,
                         'all_contained': bool(all(x['contained'] for x in checks))})
        except Exception as e:
            all_ok = False
            rows.append({'causal': causal, 'error': repr(e)})

    complete = bool(total_checks == 96 and len(rows) == 3 and all('error' not in x for x in rows))
    if complete and all_ok:
        cls = 'ITER503V_ENDPOINT_CONTRACT_CONFIRMED'
    elif complete:
        cls = 'ITER503V_ENDPOINT_CONTRACT_VIOLATION'
    else:
        cls = 'ITER503V_INVALID_OR_BLOCKED'
    return {
        'iteration': '503V',
        'box': k,
        'expected_checks': 96,
        'completed_checks': total_checks,
        'complete': complete,
        'all_contained': bool(complete and all_ok),
        'classification': cls,
        'rows': rows,
        'scope': 'raw per-R endpoint contract verifier only; no DECAY/NONDECAY, Haar, spectral-integral, D7 or selector claim',
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--box', type=int, required=True, choices=BOXES)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    try:
        out = evaluate_box(a.box)
    except Exception as e:
        out = {'iteration': '503V', 'box': a.box, 'complete': False,
               'classification': 'ITER503V_INVALID_OR_BLOCKED', 'error': repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    with open(a.out, 'w') as f:
        json.dump(out, f, indent=2, sort_keys=True)
    print(json.dumps({k: v for k, v in out.items() if k != 'rows'}, indent=2, sort_keys=True))
    raise SystemExit(0)


if __name__ == '__main__':
    main()
