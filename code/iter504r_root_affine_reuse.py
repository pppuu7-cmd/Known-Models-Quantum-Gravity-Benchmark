#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

from flint import arb, ctx

import iter499_arb_core as core
import iter500_compact_sandwich_kak as enable
import iter501_direct_max_envelope_interval as prev
import iter503_ad_core as ad
import iter504_centered_shard as parent

ctx.prec = 384

GATE = 'ITER504R_ROOT_AFFINE_REUSE_CONTINUOUS_DRIFT_DIAGNOSTIC_GATE'
PREREG = '147d68f26ed3a14ce3cd1fd77fcd96d5fb329ec8'
CAUSAL = '0to5'
BLOCK = 0
PATH = 2
ROOT_BOXES = (13, 14, 15)
MAX_DEPTH = 10
DRIFT_TOL = arb('0.05')
ROBUST_FLOOR = arb('1.0')


def af(q: Fraction):
    return arb(q.numerator) / arb(q.denominator)


def qt(q: Fraction):
    return f'{q.numerator}/{q.denominator}'


def bf(x, side):
    return core.bound_float(x, side)


def root_interval(k: int):
    if k not in ROOT_BOXES:
        raise ValueError(k)
    return Fraction(16 + k, 12800), Fraction(17 + k, 12800)


def build_root_model(root_box: int, direction, sign):
    loq, hiq = root_interval(root_box)
    lo, hi = af(loq), af(hiq)
    amp = lo.union(hi)
    midq = (loq + hiq) / 2
    mid = af(midq)
    dual_amp = ad.RD(amp, 1)
    sig = core.SIGMAS[CAUSAL]

    controls = {
        'construction': True,
        'cycle': True,
        'source_additive': True,
        'finite_root_envelope': True,
        'center_regression': True,
    }
    min_beta = None
    model = {}

    for R in core.R_GRID:
        ds = ad.construct_dual_state(R, direction, sign, dual_amp)
        controls['construction'] = controls['construction'] and all(x[2] for x in ds['checks'])
        controls['cycle'] = controls['cycle'] and prev.cycle_contains(
            {e: ad.value_matrix(M) for e, M in ds['edges'].items()}
        )
        raw = enable.construct_state(R, direction, sign, mid)
        reg = enable.source_regression(R, direction, sign, mid, raw)
        controls['center_regression'] = controls['center_regression'] and bool(reg['pass'])

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

        rrows = []
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
            # Root-envelope finiteness is a frozen control only; descendants reuse these values/derivatives.
            root_delta = (-(hi - lo) / 2).union((hi - lo) / 2)
            vals = ad.centered_channels(rvals, dvals, root_delta)
            L, U, _ = core.envelope_bounds(vals)
            controls['finite_root_envelope'] = controls['finite_root_envelope'] and bool(L > arb(0) and U.is_finite())
            rrows.append({
                'rho': rho,
                'dvals': dvals,
                'rvals': rvals,
            })
        model[R] = {
            'raw_logH': raw_logH,
            'dlogH': dlogH,
            'rho': rrows,
        }

    if not all(controls.values()):
        raise ArithmeticError(f'root controls failed: {controls}')

    return {
        'root_box': root_box,
        'loq': loq,
        'hiq': hiq,
        'midq': midq,
        'controls': controls,
        'min_beta_lower': None if min_beta is None else bf(min_beta, 'lower'),
        'model': model,
    }


def evaluate_child(root, loq: Fraction, hiq: Fraction, depth: int):
    delta = af(loq - root['midq']).union(af(hiq - root['midq']))
    perR = {}
    finite = True
    for R in core.R_GRID:
        mr = root['model'][R]
        centered_logH = mr['raw_logH'] + delta * mr['dlogH'].d
        rows = []
        for rr in mr['rho']:
            vals = ad.centered_channels(rr['rvals'], rr['dvals'], delta)
            L, U, possible = core.envelope_bounds(vals)
            ok = bool(L > arb(0) and U.is_finite())
            finite = finite and ok
            if not ok:
                raise ArithmeticError('child nonfinite/nonpositive max envelope')
            rows.append({
                'rho': rr['rho'],
                '_ylo': centered_logH.lower() + L.log().lower(),
                '_yhi': centered_logH.upper() + U.log().upper(),
                'possible_count': len(possible),
                'possible_indices': list(possible),
            })
        perR[R] = rows

    per_rho = []
    certified = True
    max_drift = None
    min_s = None
    for i, rho in enumerate(core.RHOS):
        y6l, y6u = perR[6][i]['_ylo'], perR[6][i]['_yhi']
        y8l, y8u = perR[8][i]['_ylo'], perR[8][i]['_yhi']
        y10l, y10u = perR[10][i]['_ylo'], perR[10][i]['_yhi']
        y12l, y12u = perR[12][i]['_ylo'], perR[12][i]['_yhi']
        slo = (y12l - y8u) / 4
        shi = (y12u - y8l) / 4
        elo = (y10l - y6u) / 4
        ehi = (y10u - y6l) / 4
        du = max(abs(slo - ehi), abs(shi - elo))
        rho_cert = bool(slo >= ROBUST_FLOOR and du <= DRIFT_TOL)
        certified = certified and rho_cert
        dul = du.upper()
        sl = slo.lower()
        max_drift = dul if max_drift is None or dul > max_drift else max_drift
        min_s = sl if min_s is None or sl < min_s else min_s
        per_rho.append({
            'rho': rho,
            'certified': rho_cert,
            'S_lower': bf(slo, 'lower'),
            'S_upper': bf(shi, 'upper'),
            'E_lower': bf(elo, 'lower'),
            'E_upper': bf(ehi, 'upper'),
            'drift_upper': bf(du, 'upper'),
        })

    possible = []
    for R in core.R_GRID:
        for row in perR[R]:
            possible.append({'R': R, 'rho': row['rho'], 'count': row['possible_count'], 'indices': row['possible_indices']})

    return {
        'root_box': root['root_box'],
        'depth': depth,
        'amp_lower_q': qt(loq),
        'amp_upper_q': qt(hiq),
        'delta_lower_q': qt(loq - root['midq']),
        'delta_upper_q': qt(hiq - root['midq']),
        'finite_envelope': finite,
        'certified': certified,
        'max_drift_upper': bf(max_drift, 'upper'),
        'min_S_lower': bf(min_s, 'lower'),
        'max_possible_count': max(x['count'] for x in possible),
        'possible_max': possible,
        'per_rho': per_rho,
    }


def cover(root_box: int, leaves):
    lo0, hi0 = root_interval(root_box)
    spans = sorted((Fraction(x['amp_lower_q']), Fraction(x['amp_upper_q'])) for x in leaves)
    valid = bool(spans and spans[0][0] == lo0 and spans[-1][1] == hi0)
    gaps, overlaps = [], []
    for i in range(len(spans) - 1):
        if spans[i][1] < spans[i + 1][0]:
            gaps.append([qt(spans[i][1]), qt(spans[i + 1][0])])
        if spans[i][1] > spans[i + 1][0]:
            overlaps.append([qt(spans[i + 1][0]), qt(spans[i][1])])
        valid = valid and spans[i][1] == spans[i + 1][0]
    return {
        'valid': bool(valid and not gaps and not overlaps),
        'root_lower_q': qt(lo0),
        'root_upper_q': qt(hi0),
        'leaf_count': len(spans),
        'gaps': gaps,
        'interior_overlaps': overlaps,
    }


def run_root(root_box: int):
    direction, sign = parent.path_spec(BLOCK, PATH)
    if direction != [1, 1, 1, -1, -1, -1] or sign != 1:
        raise RuntimeError('frozen path mismatch')
    root = build_root_model(root_box, direction, sign)
    stack = [(root['loq'], root['hiq'], 0)]
    leaves = []
    nodes = 0
    root_diag = None
    while stack:
        loq, hiq, depth = stack.pop()
        node = evaluate_child(root, loq, hiq, depth)
        nodes += 1
        if depth == 0:
            root_diag = {
                'max_drift_upper': node['max_drift_upper'],
                'min_S_lower': node['min_S_lower'],
                'max_possible_count': node['max_possible_count'],
            }
        if node['certified']:
            node['leaf_status'] = 'CERTIFIED'
            leaves.append(node)
        elif depth >= MAX_DEPTH:
            node['leaf_status'] = 'UNRESOLVED_DEPTH10'
            leaves.append(node)
        else:
            m = (loq + hiq) / 2
            stack.append((m, hiq, depth + 1))
            stack.append((loq, m, depth + 1))
    leaves.sort(key=lambda x: Fraction(x['amp_lower_q']))
    return {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'root_box': root_box,
        'causal': CAUSAL,
        'block': BLOCK,
        'path': PATH,
        'direction': direction,
        'sign': sign,
        'precision_bits': 384,
        'max_depth': MAX_DEPTH,
        'full_channel_count': 243,
        'root_model_build_count': 1,
        'derivative_recomputed_on_descendants': False,
        'channel_pruning_used_for_decision': False,
        'root_controls': root['controls'],
        'min_beta_lower': root['min_beta_lower'],
        'node_count': nodes,
        'leaf_count': len(leaves),
        'certified_leaf_count': sum(x['leaf_status'] == 'CERTIFIED' for x in leaves),
        'unresolved_leaf_count': sum(x['leaf_status'] != 'CERTIFIED' for x in leaves),
        'leaf_depth_histogram': dict(sorted(Counter(str(x['depth']) for x in leaves).items())),
        'root_diagnostic': root_diag,
        'cover': cover(root_box, leaves),
        'max_terminal_leaf_possible_count': max(x['max_possible_count'] for x in leaves),
        'max_terminal_leaf_drift_upper': max(x['max_drift_upper'] for x in leaves),
        'minimum_terminal_leaf_S_lower': min(x['min_S_lower'] for x in leaves),
        'leaves': leaves,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root-box', type=int, choices=ROOT_BOXES, required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    try:
        out = run_root(a.root_box)
    except Exception as exc:
        out = {'gate': GATE, 'preregistration_commit': PREREG, 'root_box': a.root_box, 'invalid': True, 'error': repr(exc)}
    p = Path(a.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'leaves'}, indent=2, sort_keys=True))
    return 2 if out.get('invalid') else 0


if __name__ == '__main__':
    raise SystemExit(main())
