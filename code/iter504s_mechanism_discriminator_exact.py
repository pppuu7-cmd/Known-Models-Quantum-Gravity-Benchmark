#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
from flint import arb, acb, ctx

import iter499_arb_core as core
import iter503_ad_core as ad
import iter504_centered_shard as parent
import iter504r_root_affine_reuse as rgate

ctx.prec = 384

GATE = 'ITER504S_ROOT_DERIVATIVE_VS_CHANNEL_COMPETITION_DISCRIMINATOR'
PREREG = 'f6367456aa715fe6282ab70c1b2005971a4568c7'
REPAIR_DERIVATIVE = '88c92f86a765e9d8b441152674fc2c303f3f1ff3'
REPAIR_DRIFT = '4ef41c0f4ceed3082fd4d80930ef5d848f18802b'
REPAIR_EXACT = '77d42eb58c03eef2356aed7a25795562760de4e3'
ROOTS = (13, 14, 15)
RHOS = tuple(core.RHOS)
RGRID = tuple(core.R_GRID)
TOL = arb('0.05')
FLOOR = arb('1.0')


def af(q: Fraction):
    return arb(q.numerator) / arb(q.denominator)


def qt(q: Fraction):
    return f'{q.numerator}/{q.denominator}'


def bf(x, side):
    return core.bound_float(x, side)


def amid(x: arb):
    return arb(x.mid())


def cmid(z: acb):
    return acb(arb(z.real.mid()), arb(z.imag.mid()))


def derivative_array(dual_arr):
    a = np.asarray(dual_arr, dtype=object)
    out = np.empty(a.shape, dtype=object)
    for idx in np.ndindex(a.shape):
        out[idx] = ad.as_c(a[idx]).d
    return out


def center_acb_array(arr):
    a = np.asarray(arr, dtype=object)
    out = np.empty(a.shape, dtype=object)
    for idx in np.ndindex(a.shape):
        out[idx] = cmid(acb(a[idx]))
    return out


def point_locations(root_box: int):
    lo, hi = rgate.root_interval(root_box)
    mid = (lo + hi) / 2
    return [('LOW', lo), ('MID', mid), ('HIGH', hi)]


def envelope_details(vals):
    a = np.asarray(vals, dtype=object)
    lows, ups = [], []
    for z in a.flat:
        zz = acb(z)
        lo = zz.abs_lower()
        up = zz.abs_upper()
        if not (lo.is_finite() and up.is_finite()):
            raise ArithmeticError('nonfinite channel magnitude')
        lows.append(lo)
        ups.append(up)
    L = lows[0]
    U = ups[0]
    best = 0
    for i in range(1, len(lows)):
        if lows[i] > L:
            L = lows[i]
            best = i
        if ups[i] > U:
            U = ups[i]
    if not L > arb(0):
        raise ArithmeticError('nonpositive envelope lower bound')
    possible = [i for i, u in enumerate(ups) if u >= L]
    other_u = None
    for i, u in enumerate(ups):
        if i == best:
            continue
        other_u = u if other_u is None or u > other_u else other_u
    gap = L - other_u if other_u is not None else L
    return {
        'L': L, 'U': U, 'possible': possible, 'best_lower_index': best,
        'dominance_gap': gap, 'lows': lows, 'ups': ups,
    }


def slope_rows(perR):
    rows = []
    for ir, rho in enumerate(RHOS):
        y6l, y6u = perR[6][ir]['ylo'], perR[6][ir]['yhi']
        y8l, y8u = perR[8][ir]['ylo'], perR[8][ir]['yhi']
        y10l, y10u = perR[10][ir]['ylo'], perR[10][ir]['yhi']
        y12l, y12u = perR[12][ir]['ylo'], perR[12][ir]['yhi']
        slo = (y12l - y8u) / 4
        shi = (y12u - y8l) / 4
        elo = (y10l - y6u) / 4
        ehi = (y10u - y6l) / 4
        du = max(abs(slo - ehi), abs(shi - elo))
        slope_ok = bool(slo >= FLOOR)
        drift_ok = bool(du <= TOL)
        rows.append({
            'rho': rho,
            'S_lower': bf(slo, 'lower'),
            'S_upper': bf(shi, 'upper'),
            'E_lower': bf(elo, 'lower'),
            'E_upper': bf(ehi, 'upper'),
            'drift_upper': bf(du, 'upper'),
            'slope_floor_satisfied': slope_ok,
            'drift_within_tolerance': drift_ok,
            'within_tolerance': bool(slope_ok and drift_ok),
            'decision_arithmetic': 'arb_exact_predicates_before_float_serialization',
        })
    return rows


def fixed_channel_rows(perR_channels, candidate_unions):
    out = []
    for ir, rho in enumerate(RHOS):
        candidates = sorted(candidate_unions[ir])
        rows = []
        incomplete = []
        for ch in candidates:
            ys = {}
            eligible = True
            for R in RGRID:
                q = perR_channels[R][ir]
                lo = q['lows'][ch]
                up = q['ups'][ch]
                if not (lo > arb(0) and up.is_finite()):
                    eligible = False
                    break
                ys[R] = (
                    q['hlog'].lower() + lo.log().lower(),
                    q['hlog'].upper() + up.log().upper(),
                )
            if not eligible:
                incomplete.append(ch)
                continue
            y6l, y6u = ys[6]
            y8l, y8u = ys[8]
            y10l, y10u = ys[10]
            y12l, y12u = ys[12]
            slo = (y12l - y8u) / 4
            shi = (y12u - y8l) / 4
            elo = (y10l - y6u) / 4
            ehi = (y10u - y6l) / 4
            du = max(abs(slo - ehi), abs(shi - elo))
            rows.append({
                'channel': ch,
                'drift_upper': bf(du, 'upper'),
                'S_lower': bf(slo, 'lower'),
                'drift_within_tolerance': bool(du <= TOL),
            })
        complete = bool(not incomplete and len(rows) == len(candidates))
        violating = sorted(r['channel'] for r in rows if not r['drift_within_tolerance'])
        all_drift_within = bool(rows and complete and not violating)
        mx = max(rows, key=lambda z: z['drift_upper']) if rows else None
        out.append({
            'rho': rho,
            'candidate_union': candidates,
            'candidate_count': len(candidates),
            'eligible_count': len(rows),
            'ineligible_candidates': incomplete,
            'competition_test_complete': complete,
            'all_candidate_fixed_channel_drifts_within_tolerance': all_drift_within,
            'violating_channel_indices': violating,
            'max_fixed_channel_drift_upper': None if mx is None else mx['drift_upper'],
            'max_fixed_channel_witness': None if mx is None else mx,
            'decision_arithmetic': 'arb_exact_per_channel_predicates_before_float_serialization',
        })
    return out


def fixed_drift_all_within(row):
    return bool(
        row.get('competition_test_complete')
        and row.get('candidate_count', 0) > 0
        and not row.get('violating_channel_indices', [])
        and row.get('all_candidate_fixed_channel_drifts_within_tolerance') is True
    )


def evaluate_treatment(root, delta, collapse_derivative=False):
    perR = {}
    perR_channels = {}
    candidate_unions = [set() for _ in RHOS]
    for R in RGRID:
        mr = root['model'][R]
        dlog = amid(mr['dlogH'].d) if collapse_derivative else mr['dlogH'].d
        hlog = mr['raw_logH'] + delta * dlog
        rows = []
        chans = []
        for ir, rr in enumerate(mr['rho']):
            extracted = derivative_array(rr['dvals'])
            dvals = center_acb_array(extracted) if collapse_derivative else extracted
            vals = np.asarray(rr['rvals'], dtype=object) + np.asarray(dvals, dtype=object) * delta
            ed = envelope_details(vals)
            candidate_unions[ir].update(ed['possible'])
            ylo = hlog.lower() + ed['L'].log().lower()
            yhi = hlog.upper() + ed['U'].log().upper()
            rows.append({
                'rho': rr['rho'], 'ylo': ylo, 'yhi': yhi,
                'envelope_lower': bf(ed['L'], 'lower'),
                'envelope_upper': bf(ed['U'], 'upper'),
                'possible_count': len(ed['possible']),
                'possible_indices': ed['possible'],
                'best_lower_index': ed['best_lower_index'],
                'dominance_gap_lower': bf(ed['dominance_gap'], 'lower'),
                'strict_unique_max': bool(ed['dominance_gap'] > arb(0)),
            })
            chans.append({'hlog': hlog, 'lows': ed['lows'], 'ups': ed['ups']})
        perR[R] = rows
        perR_channels[R] = chans
    slopes = slope_rows(perR)
    fixed = fixed_channel_rows(perR_channels, candidate_unions)
    compact = []
    for R in RGRID:
        compact.append({
            'R': R,
            'rho': [{
                'rho': q['rho'],
                'envelope_lower': q['envelope_lower'],
                'envelope_upper': q['envelope_upper'],
                'possible_count': q['possible_count'],
                'possible_indices': q['possible_indices'],
                'best_lower_index': q['best_lower_index'],
                'dominance_gap_lower': q['dominance_gap_lower'],
                'strict_unique_max': q['strict_unique_max'],
            } for q in perR[R]],
        })
    return {'per_rho': slopes, 'per_R': compact, 'fixed_channel': fixed}


def evaluate_root(root_box: int):
    direction, sign = parent.path_spec(0, 2)
    if direction != [1, 1, 1, -1, -1, -1] or sign != 1:
        raise RuntimeError('frozen path mismatch')
    root = rgate.build_root_model(root_box, direction, sign)
    if not all(root['controls'].values()):
        raise ArithmeticError('root controls')
    cases = []
    for loc, aq in point_locations(root_box):
        delta = af(aq - root['midq'])
        full = evaluate_treatment(root, delta, False)
        center = evaluate_treatment(root, delta, True)
        mech = []
        for ir, rho in enumerate(RHOS):
            F = full['per_rho'][ir]
            C = center['per_rho'][ir]
            FF = full['fixed_channel'][ir]
            CF = center['fixed_channel'][ir]
            ff_all = fixed_drift_all_within(FF)
            cf_all = fixed_drift_all_within(CF)
            full_viol = not F['drift_within_tolerance']
            center_viol = not C['drift_within_tolerance']
            deriv = bool(full_viol and C['drift_within_tolerance'])
            compF = bool(full_viol and FF['competition_test_complete'] and ff_all)
            compC = bool(center_viol and CF['competition_test_complete'] and cf_all)
            fixedC = bool(center_viol and CF['competition_test_complete'] and not cf_all)
            mech.append({
                'rho': rho,
                'full_D_within_tolerance': F['within_tolerance'],
                'derivative_radius_sensitivity': deriv,
                'competition_necessary_full_D': compF,
                'competition_necessary_center_D': compC,
                'fixed_channel_nonstationarity_center_D': fixedC,
                'decision_arithmetic': 'producer_exact_arb_booleans',
            })
        cases.append({
            'location': loc,
            'amp_q': qt(aq),
            'delta_q': qt(aq - root['midq']),
            'full_D': full,
            'center_D_sensitivity': center,
            'mechanism_flags': mech,
        })
    return {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'repair_preregistrations': [REPAIR_DERIVATIVE, REPAIR_DRIFT, REPAIR_EXACT],
        'root_box': root_box,
        'causal': '0to5', 'block': 0, 'path': 2,
        'direction': direction, 'sign': sign,
        'precision_bits': 384,
        'full_channel_count': 243,
        'channel_pruning_used': False,
        'root_model_build_count': 1,
        'derivative_recomputed_at_points': False,
        'derivative_channel_representation': 'ad.as_c(z).d',
        'full_D_derivative_treatment': 'unchanged_full_root_acb_derivative_ball',
        'center_D_derivative_treatment': 'deterministic_midpoint_of_same_full_root_acb_derivative_ball',
        'scientific_decision_transport': 'exact_arb_booleans_float_bounds_display_only',
        'root_controls': root['controls'],
        'min_beta_lower': root['min_beta_lower'],
        'cases': cases,
        'claim_ceiling': 'Iter504S nine-point mechanism diagnostic only; center-D treatment is control-only sensitivity, not validated enclosure',
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root-box', type=int, required=True, choices=ROOTS)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    try:
        out = evaluate_root(a.root_box)
    except Exception as e:
        out = {
            'gate': GATE,
            'preregistration_commit': PREREG,
            'repair_preregistrations': [REPAIR_DERIVATIVE, REPAIR_DRIFT, REPAIR_EXACT],
            'root_box': a.root_box,
            'invalid': True,
            'error': repr(e),
        }
    p = Path(a.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'cases'}, indent=2, sort_keys=True))
    return 2 if out.get('invalid') else 0


if __name__ == '__main__':
    raise SystemExit(main())
