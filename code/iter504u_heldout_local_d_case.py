#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
from flint import arb, ctx

import iter499_arb_core as core
import iter500_compact_sandwich_kak as enable
import iter501_direct_max_envelope_interval as prev
import iter503_ad_core as ad
import iter504_centered_shard as parent

ctx.prec = 384

GATE = 'ITER504U_HELDOUT_LOCAL_D_GENERALIZATION_FIREWALL'
PREREG = '05b8e9354c9a7805f0fce18b904346a986a0787f'
PARENT_CRITIC = '8624532254981fbea6f8fcfac09cd538e2066aa4'
EXACT_REPAIR_HEAD = '10ae6bcc8447d14cecc6e550065504b23f792953'
MAX_DEPTH = 3
TOL = arb('0.05')
FLOOR = arb('1.0')
R_COHORT = tuple(int(x) for x in core.R_GRID)
RHO_COHORT = tuple(float(x) for x in core.RHOS)

CASES = {
    'H0_AMP_LOW': ('0to5', 0, 2, 0),
    'H1_AMP_MID': ('0to5', 0, 2, 8),
    'H2_CAUSAL_1': ('1to4', 0, 2, 8),
    'H3_CAUSAL_2': ('2to3', 0, 2, 8),
    'H4_DIRECTION': ('0to5', 3, 2, 8),
    'H5_SIGN': ('0to5', 0, 3, 8),
}
DEVELOPMENT_BOXES = (13, 14, 15)


def af(q: Fraction):
    return arb(q.numerator) / arb(q.denominator)


def qt(q: Fraction) -> str:
    return f'{q.numerator}/{q.denominator}'


def bf(x, side: str) -> float:
    return core.bound_float(x, side)


def box_interval(k: int) -> tuple[Fraction, Fraction]:
    if k not in range(16):
        raise ValueError(k)
    return Fraction(16 + k, 12800), Fraction(17 + k, 12800)


def _arb_subseteq(child, parent_ball) -> bool:
    return bool(child.lower() >= parent_ball.lower() and child.upper() <= parent_ball.upper())


def _acb_subseteq(child, parent_ball) -> bool:
    return _arb_subseteq(child.real, parent_ball.real) and _arb_subseteq(child.imag, parent_ball.imag)


def _derivative_snapshot(model):
    out = {'haar': {}, 'channels': {}}
    for R in R_COHORT:
        q = model['model'][R]
        out['haar'][R] = q['dlogH'].d
        rows = {}
        for rr in q['rho']:
            rho = float(rr['rho'])
            a = np.asarray(rr['dvals'], dtype=object)
            rows[rho] = [ad.as_c(a[idx]).d for idx in np.ndindex(a.shape)]
        out['channels'][R] = rows
    return out


def _inclusion_record(child, parent_snap, loq, hiq, depth, parent_loq, parent_hiq, parent_depth):
    if tuple(sorted(child['haar'])) != R_COHORT or tuple(sorted(parent_snap['haar'])) != R_COHORT:
        raise ArithmeticError('R cohort changed in inclusion snapshot')
    haar = {}
    rows = []
    all_ok = True
    for R in R_COHORT:
        hb = _arb_subseteq(child['haar'][R], parent_snap['haar'][R])
        haar[str(R)] = hb
        all_ok = all_ok and hb
        if tuple(sorted(child['channels'][R])) != RHO_COHORT or tuple(sorted(parent_snap['channels'][R])) != RHO_COHORT:
            raise ArithmeticError('rho cohort changed in inclusion snapshot')
        for rho in RHO_COHORT:
            cv = child['channels'][R][rho]
            pv = parent_snap['channels'][R][rho]
            if len(cv) != 243 or len(pv) != 243:
                raise ArithmeticError('channel count changed in inclusion snapshot')
            bits = [_acb_subseteq(c, p) for c, p in zip(cv, pv)]
            all_ok = all_ok and all(bits)
            rows.append({'R': R, 'rho': rho, 'componentwise_inclusion': bits})
    return {
        'depth': depth,
        'amp_lower_q': qt(loq),
        'amp_upper_q': qt(hiq),
        'parent_depth': parent_depth,
        'parent_amp_lower_q': qt(parent_loq),
        'parent_amp_upper_q': qt(parent_hiq),
        'haar_log_inclusion_by_R': haar,
        'channel_inclusion_rows': rows,
        'all_componentwise_parent_inclusion': bool(all_ok),
    }


def build_local(loq: Fraction, hiq: Fraction, causal: str, direction, sign: int):
    lo, hi = af(loq), af(hiq)
    amp = lo.union(hi)
    midq = (loq + hiq) / 2
    mid = af(midq)
    dual = ad.RD(amp, 1)
    sig = core.SIGMAS[causal]
    controls = {
        'construction': True,
        'cycle': True,
        'source_additive': True,
        'center_regression': True,
        'finite_local_envelope': True,
    }
    model = {}
    for R in R_COHORT:
        ds = ad.construct_dual_state(R, direction, sign, dual)
        controls['construction'] = controls['construction'] and all(x[2] for x in ds['checks'])
        controls['cycle'] = controls['cycle'] and prev.cycle_contains({e: ad.value_matrix(M) for e, M in ds['edges'].items()})
        raw = enable.construct_state(R, direction, sign, mid)
        reg = enable.source_regression(R, direction, sign, mid, raw)
        controls['center_regression'] = controls['center_regression'] and bool(reg['pass'])

        dlog = ad.RD(0, 0)
        rawlog = arb(0)
        for k in ds['node_kak'].values():
            dlog += 2 * k['beta'].sinh().log()
        for k in raw['node_kak'].values():
            rawlog += 2 * k['beta'].sinh().log()

        rr = []
        for rho in core.RHOS:
            dm, rm = [], []
            add = True
            for e in core.EDGES:
                branch = 'p' if sig[e[0]] * sig[e[1]] > 0 else 'm'
                dM, dok = ad.dfull_toller(ds['edge_kak'][e], rho, branch)
                rM, rok = core.full_toller(raw['edge_kak'][e], rho, branch)
                dm.append(dM)
                rm.append(rM)
                add = add and dok and rok
            controls['source_additive'] = controls['source_additive'] and add
            dv = ad.dcontract_all(dm)
            rv = core.contract_all(rm)
            delta = af(loq - midq).union(af(hiq - midq))
            vals = ad.centered_channels(rv, dv, delta)
            L, U, _ = core.envelope_bounds(vals)
            controls['finite_local_envelope'] = controls['finite_local_envelope'] and bool(L > arb(0) and U.is_finite())
            rr.append({'rho': rho, 'dvals': dv, 'rvals': rv})
        model[R] = {'raw_logH': rawlog, 'dlogH': dlog, 'rho': rr}

    if not all(controls.values()):
        raise ArithmeticError(f'local controls failed {controls}')
    return {'loq': loq, 'hiq': hiq, 'midq': midq, 'controls': controls, 'model': model}


def evaluate(loq: Fraction, hiq: Fraction, depth: int, causal: str, direction, sign: int):
    m = build_local(loq, hiq, causal, direction, sign)
    snap = _derivative_snapshot(m)
    delta = af(loq - m['midq']).union(af(hiq - m['midq']))
    perR = {}
    possible = []
    for R in R_COHORT:
        q = m['model'][R]
        h = q['raw_logH'] + delta * q['dlogH'].d
        rows = []
        for rr in q['rho']:
            vals = ad.centered_channels(rr['rvals'], rr['dvals'], delta)
            L, U, p = core.envelope_bounds(vals)
            if not bool(L > arb(0) and U.is_finite()):
                raise ArithmeticError('nonpositive/nonfinite local envelope')
            rows.append({'rho': rr['rho'], 'yl': h.lower() + L.log().lower(), 'yu': h.upper() + U.log().upper(), 'possible': list(p)})
            possible.append({'R': R, 'rho': rr['rho'], 'indices': list(p)})
        perR[R] = rows

    prs = []
    maxd = None
    mins = None
    for i, rho in enumerate(core.RHOS):
        y6l, y6u = perR[6][i]['yl'], perR[6][i]['yu']
        y8l, y8u = perR[8][i]['yl'], perR[8][i]['yu']
        y10l, y10u = perR[10][i]['yl'], perR[10][i]['yu']
        y12l, y12u = perR[12][i]['yl'], perR[12][i]['yu']
        sl = (y12l - y8u) / 4
        su = (y12u - y8l) / 4
        el = (y10l - y6u) / 4
        eu = (y10u - y6l) / 4
        du = max(abs(sl - eu), abs(su - el))
        sok = bool(sl >= FLOOR)
        dok = bool(du <= TOL)
        ok = sok and dok
        maxd = du.upper() if maxd is None or du.upper() > maxd else maxd
        mins = sl.lower() if mins is None or sl.lower() < mins else mins
        prs.append({
            'rho': rho,
            'slope_floor_satisfied': sok,
            'drift_within_tolerance': dok,
            'certified': ok,
            'S_lower': bf(sl, 'lower'),
            'S_upper': bf(su, 'upper'),
            'E_lower': bf(el, 'lower'),
            'E_upper': bf(eu, 'upper'),
            'drift_upper': bf(du, 'upper'),
        })

    certified = all(r['certified'] for r in prs)
    row = {
        'depth': depth,
        'amp_lower_q': qt(loq),
        'amp_upper_q': qt(hiq),
        'local_mid_q': qt(m['midq']),
        'validated_local_derivative': True,
        'local_derivative_recomputed_here': True,
        'leaf_certification_binding': 'all_per_rho_exact',
        'scientific_decision_transport': 'exact_arb_booleans_float_bounds_display_only',
        'certified': bool(certified),
        'per_rho': prs,
        'possible_max': possible,
        'max_drift_upper': bf(maxd, 'upper'),
        'min_S_lower': bf(mins, 'lower'),
    }
    return row, snap


def case_run(case_id: str):
    causal, block, path, box = CASES[case_id]
    if box in DEVELOPMENT_BOXES:
        raise RuntimeError('development box inserted into held-out cohort')
    if R_COHORT != (6, 8, 10, 12):
        raise RuntimeError(f'R cohort {R_COHORT}')
    if RHO_COHORT != (0.35, 0.9, 1.6, 2.7):
        raise RuntimeError(f'rho cohort {RHO_COHORT}')
    direction, sign = parent.path_spec(block, path)
    lo, hi = box_interval(box)
    stack = [(lo, hi, 0, None, None, None)]
    leaves = []
    inclusions = []
    visited = 0
    while stack:
        a, b, d, parent_snap, parent_bounds, parent_depth = stack.pop()
        row, snap = evaluate(a, b, d, causal, direction, sign)
        visited += 1
        if parent_snap is not None:
            pa, pb = parent_bounds
            inclusions.append(_inclusion_record(snap, parent_snap, a, b, d, pa, pb, parent_depth))
        if row['certified'] or d == MAX_DEPTH:
            leaves.append(row)
        else:
            m = (a + b) / 2
            stack.append((m, b, d + 1, snap, (a, b), d))
            stack.append((a, m, d + 1, snap, (a, b), d))

    spans = sorted((Fraction(x['amp_lower_q']), Fraction(x['amp_upper_q'])) for x in leaves)
    cover = bool(spans and spans[0][0] == lo and spans[-1][1] == hi and all(spans[i][1] == spans[i + 1][0] for i in range(len(spans) - 1)))
    unresolved = [x for x in leaves if not x['certified']]
    return {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'parent_critic_commit': PARENT_CRITIC,
        'exact_repair_head': EXACT_REPAIR_HEAD,
        'case_id': case_id,
        'causal': causal,
        'block': block,
        'path': path,
        'box': box,
        'direction': direction,
        'sign': sign,
        'parent_amp_lower_q': qt(lo),
        'parent_amp_upper_q': qt(hi),
        'precision_bits': 384,
        'python_flint': '0.9.0',
        'full_channel_count': 243,
        'channel_pruning_used': False,
        'max_depth': MAX_DEPTH,
        'partition_rule': 'deterministic_dyadic_midpoint',
        'local_derivative_recomputed_each_visited_node': True,
        'leaf_certification_binding': 'all_per_rho_exact',
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'r_cohort_consumed': list(R_COHORT),
        'rho_cohort_consumed': list(RHO_COHORT),
        'componentwise_parent_inclusion_record_count': len(inclusions),
        'componentwise_parent_inclusion_records': inclusions,
        'cover_valid': cover,
        'visited_node_count': visited,
        'terminal_leaf_count': len(leaves),
        'unresolved_leaf_count': len(unresolved),
        'leaves': leaves,
        'claim_ceiling': 'One prospectively frozen Iter504U held-out case only',
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--case-id', choices=tuple(CASES), required=True)
    p.add_argument('--out', required=True)
    a = p.parse_args()
    try:
        out = case_run(a.case_id)
    except Exception as e:
        out = {
            'gate': GATE,
            'preregistration_commit': PREREG,
            'parent_critic_commit': PARENT_CRITIC,
            'exact_repair_head': EXACT_REPAIR_HEAD,
            'case_id': a.case_id,
            'invalid': True,
            'error': repr(e),
        }
    q = Path(a.out)
    q.parent.mkdir(parents=True, exist_ok=True)
    q.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k not in ('leaves', 'componentwise_parent_inclusion_records')}, indent=2, sort_keys=True))
    return 2 if out.get('invalid') else 0


if __name__ == '__main__':
    raise SystemExit(main())
