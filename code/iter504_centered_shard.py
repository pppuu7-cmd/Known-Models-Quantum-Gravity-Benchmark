#!/usr/bin/env python3
"""Frozen Iter504 centered full-science box-shard evaluator."""
import argparse, json, os
from flint import arb, ctx

import iter499_arb_core as core
import iter500_compact_sandwich_kak as enable
import iter501_direct_max_envelope_interval as prev
import iter503_ad_core as ad

ctx.prec = 384
DRIFT_TOL = arb('0.05')
ROBUST_FLOOR = arb('1.0')
NONDECAY_FLOOR = arb('0.0')
DECAY_CEIL = arb('-0.10')
CAUSALS = ['0to5', '1to4', '2to3']


def path_spec(block, path):
    if block not in range(4) or path not in range(4):
        raise ValueError((block, path))
    direction = list(core.BLOCKS[block][path // 2])
    sign = 1 if path % 2 == 0 else -1
    return direction, sign


def _bf(x, side):
    return core.bound_float(x, side)


def centered_box(causal, direction, sign, k):
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
    center_regression = []
    min_beta = None

    for R in core.R_GRID:
        ds = ad.construct_dual_state(R, direction, sign, dual_amp)
        controls['construction'] = controls['construction'] and all(x[2] for x in ds['checks'])
        controls['cycle'] = controls['cycle'] and prev.cycle_contains(
            {e: ad.value_matrix(M) for e, M in ds['edges'].items()}
        )

        raw = enable.construct_state(R, direction, sign, mid)
        reg = enable.source_regression(R, direction, sign, mid, raw)
        controls['center_regression'] = controls['center_regression'] and bool(reg['pass'])
        center_regression.append({'R': R, **reg})

        dlogH = ad.RD(0, 0)
        raw_logH = arb(0)
        for kk in ds['node_kak'].values():
            dlogH += 2 * kk['beta'].sinh().log()
            bl = kk['beta'].v.lower()
            min_beta = bl if min_beta is None or bl < min_beta else min_beta
        for kk in ds['edge_kak'].values():
            bl = kk['beta'].v.lower()
            min_beta = bl if min_beta is None or bl < min_beta else min_beta
        for kk in raw['node_kak'].values():
            raw_logH += 2 * kk['beta'].sinh().log()
        centered_logH = raw_logH + delta * dlogH.d

        rhorows = []
        for rho in core.RHOS:
            dmats, rmats = [], []
            addok = True
            for e in core.EDGES:
                branch = 'p' if sig[e[0]] * sig[e[1]] > 0 else 'm'
                dM, dok = ad.dfull_toller(ds['edge_kak'][e], rho, branch)
                rM, rok = core.full_toller(raw['edge_kak'][e], rho, branch)
                dmats.append(dM)
                rmats.append(rM)
                addok = addok and dok and rok
            controls['source_additive'] = controls['source_additive'] and addok
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
            rhorows.append({
                'rho': rho,
                '_ylo': ylo,
                '_yhi': yhi,
                'envelope_lower': L,
                'envelope_upper': U,
                'possible_max': list(possible),
            })
        perR[R] = rhorows

    if not all(controls.values()):
        raise ArithmeticError(f'centered controls failed: {controls}')

    per_rho = []
    for ir, rho in enumerate(core.RHOS):
        y6l, y6u = perR[6][ir]['_ylo'], perR[6][ir]['_yhi']
        y8l, y8u = perR[8][ir]['_ylo'], perR[8][ir]['_yhi']
        y10l, y10u = perR[10][ir]['_ylo'], perR[10][ir]['_yhi']
        y12l, y12u = perR[12][ir]['_ylo'], perR[12][ir]['_yhi']
        slo = (y12l - y8u) / 4
        shi = (y12u - y8l) / 4
        elo = (y10l - y6u) / 4
        ehi = (y10u - y6l) / 4
        du = max(abs(slo - ehi), abs(shi - elo))
        if bool(slo >= ROBUST_FLOOR and du <= DRIFT_TOL):
            cls = 'INTERVAL_ROBUST_NONDECAY'
        elif bool(slo >= NONDECAY_FLOOR and du <= DRIFT_TOL):
            cls = 'INTERVAL_NONDECAY'
        elif bool(shi <= DECAY_CEIL and du <= DRIFT_TOL):
            cls = 'INTERVAL_UNIFORM_DECAY_WITNESS'
        else:
            cls = 'INTERVAL_INCONCLUSIVE'
        per_rho.append({
            'rho': rho,
            'classification': cls,
            'S_lower': _bf(slo, 'lower'),
            'S_upper': _bf(shi, 'upper'),
            'E_lower': _bf(elo, 'lower'),
            'E_upper': _bf(ehi, 'upper'),
            'drift_upper': _bf(du, 'upper'),
        })

    per_R = []
    for R in core.R_GRID:
        rows = []
        for q in perR[R]:
            rows.append({
                'rho': q['rho'],
                'Y_lower': _bf(q['_ylo'], 'lower'),
                'Y_upper': _bf(q['_yhi'], 'upper'),
                'envelope_lower': _bf(q['envelope_lower'], 'lower'),
                'envelope_upper': _bf(q['envelope_upper'], 'upper'),
                'possible_max_indices': q['possible_max'],
                'possible_max_count': len(q['possible_max']),
            })
        per_R.append({'R': R, 'rho': rows})

    return {
        'box': k,
        'amp_lower': _bf(lo, 'lower'),
        'amp_upper': _bf(hi, 'upper'),
        'controls': controls,
        'center_regression': center_regression,
        'min_beta_lower': None if min_beta is None else _bf(min_beta, 'lower'),
        'per_rho': per_rho,
        'per_R': per_R,
    }


def evaluate(causal, block, path, half):
    direction, sign = path_spec(block, path)
    box_ids = list(range(0, 8)) if half == 0 else list(range(8, 16))
    boxes = []
    valid = True
    for k in box_ids:
        try:
            boxes.append(centered_box(causal, direction, sign, k))
        except Exception as e:
            valid = False
            boxes.append({'box': k, 'error': repr(e)})
    return {
        'iteration': 504,
        'kind': 'centered_box_shard',
        'shard_id': f'{causal}-b{block}-p{path}-h{half}',
        'causal': causal,
        'block': block,
        'path': path,
        'half': half,
        'direction': direction,
        'sign': sign,
        'box_ids': box_ids,
        'precision_bits': 384,
        'valid': bool(valid and len(boxes) == 8 and all('error' not in b for b in boxes)),
        'boxes': boxes,
        'scope': 'Iter504 frozen centered 243-channel box shard; orchestration fragment of one causal x block logical science lane',
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--causal', required=True, choices=CAUSALS)
    ap.add_argument('--block', required=True, type=int, choices=range(4))
    ap.add_argument('--path', required=True, type=int, choices=range(4))
    ap.add_argument('--half', required=True, type=int, choices=(0, 1))
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    try:
        out = evaluate(a.causal, a.block, a.path, a.half)
    except Exception as e:
        out = {
            'iteration': 504,
            'kind': 'centered_box_shard',
            'shard_id': f'{a.causal}-b{a.block}-p{a.path}-h{a.half}',
            'causal': a.causal,
            'block': a.block,
            'path': a.path,
            'half': a.half,
            'valid': False,
            'error': repr(e),
        }
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    with open(a.out, 'w') as f:
        json.dump(out, f, indent=2, sort_keys=True)
    print(json.dumps({k: v for k, v in out.items() if k != 'boxes'}, indent=2, sort_keys=True))
    raise SystemExit(0)


if __name__ == '__main__':
    main()
