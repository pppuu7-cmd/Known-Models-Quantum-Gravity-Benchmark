#!/usr/bin/env python3
"""Frozen Iter503 centered dependency-repair enabling evaluator."""
import argparse
import json
import os
from flint import arb, ctx
import iter499_arb_core as core
import iter500_compact_sandwich_kak as enable
import iter501_direct_max_envelope_interval as prev
import iter503_ad_core as ad
ctx.prec = 384
DIRECTION = [1, 1, 1, -1, -1, -1]
SIGN = 1
BOXES = [0, 7, 15]
CAUSALS = ['0to5', '1to4', '2to3']

def point_contains(q, point_row):
    s = arb(repr(float(point_row['actual_slope'])))
    e = arb(repr(float(point_row['early_actual_slope'])))
    return bool(q['_slo'] <= s <= q['_shi'] and q['_elo'] <= e <= q['_ehi'])


def slopes_from_perR(perR):
    out = []
    for ir, rho in enumerate(core.RHOS):
        y6l, y6u = perR[6][ir]
        y8l, y8u = perR[8][ir]
        y10l, y10u = perR[10][ir]
        y12l, y12u = perR[12][ir]
        slo = (y12l - y8u) / 4; shi = (y12u - y8l) / 4
        elo = (y10l - y6u) / 4; ehi = (y10u - y6l) / 4
        out.append({'rho': rho, '_slo': slo, '_shi': shi, '_elo': elo, '_ehi': ehi})
    return out


def centered_box(causal, k):
    amp, lo, hi = core.box_amp(k); mid = (lo + hi) / 2; h = (hi - lo) / 2
    delta = (-h).union(h)
    dual_amp = ad.RD(amp, 1)
    sig = core.SIGMAS[causal]
    perR = {}; controls = {'construction': True, 'cycle': True, 'source_additive': True,
                            'finite_envelope': True, 'center_regression': True}
    center_regression = []
    for R in core.R_GRID:
        ds = ad.construct_dual_state(R, DIRECTION, SIGN, dual_amp)
        controls['construction'] = controls['construction'] and all(x[2] for x in ds['checks'])
        controls['cycle'] = controls['cycle'] and prev.cycle_contains({e: ad.value_matrix(M) for e, M in ds['edges'].items()})

        raw = enable.construct_state(R, DIRECTION, SIGN, mid)
        reg = enable.source_regression(R, DIRECTION, SIGN, mid, raw)
        controls['center_regression'] = controls['center_regression'] and bool(reg['pass'])
        center_regression.append({'R': R, **reg})

        dlogH = ad.RD(0, 0); raw_logH = arb(0)
        for kk in ds['node_kak'].values():
            dlogH += 2 * kk['beta'].sinh().log()
        for kk in raw['node_kak'].values():
            raw_logH += 2 * kk['beta'].sinh().log()
        centered_logH = raw_logH + delta * dlogH.d

        rhorows = []
        for rho in core.RHOS:
            dmats = []; rmats = []; add_rho = True
            for e in core.EDGES:
                branch = 'p' if sig[e[0]] * sig[e[1]] > 0 else 'm'
                dM, dok = ad.dfull_toller(ds['edge_kak'][e], rho, branch)
                rM, rok = core.full_toller(raw['edge_kak'][e], rho, branch)
                dmats.append(dM); rmats.append(rM); add_rho = add_rho and dok and rok
            controls['source_additive'] = controls['source_additive'] and add_rho
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
            rhorows.append((ylo, yhi, L, U, possible))
        perR[R] = rhorows
    if not all(controls.values()):
        raise ArithmeticError(f'centered controls failed: {controls}')

    compact = {R: [(row[0], row[1]) for row in perR[R]] for R in core.R_GRID}
    slopes = slopes_from_perR(compact)
    endpoint_checks = []
    centered_ok = True
    for a, label in [(float(lo.mid()), 'lo'), (float(hi.mid()), 'hi')]:
        pp = prev.point_eval(causal, DIRECTION, SIGN, a)
        for ir, row in enumerate(pp):
            hit = point_contains(slopes[ir], row)
            centered_ok = centered_ok and hit
            endpoint_checks.append({'endpoint': label, 'amplitude': a, 'rho': row['rho'], 'contained': bool(hit)})

    frozen_points = []
    point_ok = True
    for a in prev.POINT_AMPS:
        aa = arb(repr(float(a)))
        if lo <= aa <= hi:
            pp = prev.point_eval(causal, DIRECTION, SIGN, a)
            for ir, row in enumerate(pp):
                hit = point_contains(slopes[ir], row)
                point_ok = point_ok and hit
                frozen_points.append({'amplitude': a, 'rho': row['rho'], 'contained': bool(hit)})

    return {'controls': controls, 'center_regression': center_regression, 'slopes': slopes,
            'endpoint_checks': endpoint_checks, 'endpoint_containment': bool(centered_ok),
            'frozen_point_checks': frozen_points, 'frozen_point_containment': bool(point_ok)}


def natural_negative(causal, k):
    try:
        b = prev.box_eval(causal, DIRECTION, SIGN, k)
    except Exception as e:
        return {'reproduces_prior_blocker': True, 'reason': 'natural_interval_exception', 'error': repr(e)}
    checks = []; all_contained = True; eligible = 0
    lo = b['_alo']; hi = b['_ahi']
    for a in prev.POINT_AMPS:
        aa = arb(repr(float(a)))
        if not (lo <= aa <= hi):
            continue
        eligible += 1
        pp = prev.point_eval(causal, DIRECTION, SIGN, a)
        for ir, row in enumerate(pp):
            hit = point_contains(b['per_rho'][ir], row)
            all_contained = all_contained and hit
            checks.append({'amplitude': a, 'rho': row['rho'], 'contained': bool(hit)})
    return {'reproduces_prior_blocker': bool(eligible > 0 and not all_contained),
            'reason': 'unchanged_source_point_containment', 'eligible_point_amplitudes': eligible, 'checks': checks}


def _bf(x, side):
    return core.bound_float(x, side)


def serialize_centered(c):
    return {
        'controls': c['controls'],
        'center_regression': c['center_regression'],
        'endpoint_containment': c['endpoint_containment'],
        'frozen_point_containment': c['frozen_point_containment'],
        'endpoint_checks': c['endpoint_checks'],
        'frozen_point_checks': c['frozen_point_checks'],
        'slopes': [
            {'rho': q['rho'], 'S_lower': _bf(q['_slo'], 'lower'), 'S_upper': _bf(q['_shi'], 'upper'),
             'E_lower': _bf(q['_elo'], 'lower'), 'E_upper': _bf(q['_ehi'], 'upper')}
            for q in c['slopes']
        ],
    }


def evaluate_box(k):
    if k not in BOXES:
        raise ValueError(k)
    amp, lo, hi = core.box_amp(k)
    rows = []; method_blocker = False; negative_seen = False; all_centered = True
    for causal in CAUSALS:
        try:
            centered = centered_box(causal, k)
            neg = natural_negative(causal, k)
            negative_seen = negative_seen or bool(neg['reproduces_prior_blocker'])
            ok = centered['endpoint_containment'] and centered['frozen_point_containment'] and all(centered['controls'].values())
            all_centered = all_centered and ok
            if not ok:
                method_blocker = True
            rows.append({'causal': causal, 'centered': serialize_centered(centered), 'natural_negative': neg})
        except Exception as e:
            method_blocker = True; all_centered = False
            rows.append({'causal': causal, 'error': repr(e)})
    if method_blocker:
        cls = 'ITER503_NUMERICAL_METHOD_BLOCKER'
    elif all_centered and negative_seen:
        cls = 'ITER503_CENTERED_DEPENDENCY_REPAIR_ENABLED_SCOPED'
    else:
        cls = 'ITER503_CENTERED_DEPENDENCY_REPAIR_INCONCLUSIVE'
    return {'iteration': 503, 'box': k, 'amp_lower': _bf(lo, 'lower'), 'amp_upper': _bf(hi, 'upper'),
            'direction': DIRECTION, 'sign': SIGN, 'causals': CAUSALS, 'rho': core.RHOS, 'R_grid': core.R_GRID,
            'valid': bool(not method_blocker), 'method_blocker': bool(method_blocker),
            'negative_control_reproduced': bool(negative_seen), 'centered_containment_all': bool(all_centered),
            'classification': cls, 'rows': rows,
            'scope': 'Iter503 centered single-common-amplitude dependency-repair enabling subset only; no DECAY/NONDECAY, Haar, spectral-integral, or terminal-D7 claim'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--box', type=int, required=True, choices=BOXES)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    try:
        out = evaluate_box(a.box)
    except Exception as e:
        out = {'iteration': 503, 'box': a.box, 'valid': False, 'method_blocker': True,
               'classification': 'ITER503_NUMERICAL_METHOD_BLOCKER', 'error': repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    with open(a.out, 'w') as f:
        json.dump(out, f, indent=2, sort_keys=True)
    print(json.dumps({k: v for k, v in out.items() if k != 'rows'}, indent=2, sort_keys=True))
    raise SystemExit(0)


if __name__ == '__main__':
    main()
