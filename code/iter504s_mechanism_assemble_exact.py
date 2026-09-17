#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

GATE = 'ITER504S_ROOT_DERIVATIVE_VS_CHANNEL_COMPETITION_DISCRIMINATOR'
PREREG = 'f6367456aa715fe6282ab70c1b2005971a4568c7'
REPAIRS = [
    '88c92f86a765e9d8b441152674fc2c303f3f1ff3',
    '4ef41c0f4ceed3082fd4d80930ef5d848f18802b',
    '77d42eb58c03eef2356aed7a25795562760de4e3',
]
ROOTS = (13, 14, 15)
RHOS = (0.35, 0.9, 1.6, 2.7)
RGRID = (6, 8, 10, 12)
LOCS = ('LOW', 'MID', 'HIGH')
CL_DERIV = 'ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED'
CL_COMP = 'ITER504S_CHANNEL_COMPETITION_NECESSARY_SCOPED'
CL_FIXED = 'ITER504S_FIXED_CHANNEL_NONSTATIONARITY_REMAINS_SCOPED'
CL_MIX = 'ITER504S_MIXED_MECHANISM_SCOPED'
INVALID = 'ITER504S_INVALID'


def read_one(p):
    raw = Path(p).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def points(k):
    lo = Fraction(16 + k, 12800)
    hi = Fraction(17 + k, 12800)
    mid = (lo + hi) / 2
    return {'LOW': lo, 'MID': mid, 'HIGH': hi}


def one(rows, rho):
    hits = [x for x in rows if float(x.get('rho')) == rho]
    if len(hits) != 1:
        raise ValueError(f'rho {rho} count {len(hits)}')
    return hits[0]


def fixed_all(rr):
    cand = rr.get('candidate_union', [])
    inc = rr.get('ineligible_candidates', [])
    viol = rr.get('violating_channel_indices', [])
    complete = bool(
        not inc
        and rr.get('eligible_count') == len(cand)
        and rr.get('competition_test_complete') is True
    )
    return bool(
        complete
        and len(cand) > 0
        and not viol
        and rr.get('all_candidate_fixed_channel_drifts_within_tolerance') is True
    )


def validate_root(o, k):
    errors = []
    checks = [
        (o.get('gate') == GATE, 'gate'),
        (o.get('preregistration_commit') == PREREG, 'prereg'),
        (o.get('repair_preregistrations') == REPAIRS, 'repairs'),
        (o.get('root_box') == k, 'root'),
        (o.get('causal') == '0to5' and o.get('block') == 0 and o.get('path') == 2, 'lane'),
        (o.get('direction') == [1, 1, 1, -1, -1, -1] and o.get('sign') == 1, 'path_sign'),
        (o.get('precision_bits') == 384, 'precision'),
        (o.get('full_channel_count') == 243, 'channels'),
        (o.get('channel_pruning_used') is False, 'pruning'),
        (o.get('root_model_build_count') == 1, 'model_count'),
        (o.get('derivative_recomputed_at_points') is False, 'derivative_recompute'),
        (o.get('derivative_channel_representation') == 'ad.as_c(z).d', 'derivative_representation'),
        (o.get('full_D_derivative_treatment') == 'unchanged_full_root_acb_derivative_ball', 'full_D_treatment'),
        (o.get('center_D_derivative_treatment') == 'deterministic_midpoint_of_same_full_root_acb_derivative_ball', 'center_D_control_treatment'),
        (o.get('scientific_decision_transport') == 'exact_arb_booleans_float_bounds_display_only', 'transport'),
    ]
    for ok, name in checks:
        if not ok:
            errors.append(name)
    if o.get('invalid'):
        errors.append('producer_invalid')
    if not o.get('root_controls') or not all(o['root_controls'].values()):
        errors.append('controls')

    cases = o.get('cases', [])
    if tuple(c.get('location') for c in cases) != LOCS:
        errors.append('locations')
    exp = points(k)

    for c in cases:
        loc = c.get('location')
        if loc not in exp:
            continue
        try:
            if Fraction(c['amp_q']) != exp[loc]:
                errors.append(loc + ':amp')
            if Fraction(c['delta_q']) != exp[loc] - exp['MID']:
                errors.append(loc + ':delta')
        except Exception:
            errors.append(loc + ':rational')

        for tag in ('full_D', 'center_D_sensitivity'):
            t = c.get(tag, {})
            per_rho = t.get('per_rho', [])
            fixed = t.get('fixed_channel', [])
            per_R = t.get('per_R', [])
            if tuple(float(x.get('rho')) for x in per_rho) != RHOS:
                errors.append(loc + ':' + tag + ':rho')
            if tuple(float(x.get('rho')) for x in fixed) != RHOS:
                errors.append(loc + ':' + tag + ':fixedrho')
            if tuple(x.get('R') for x in per_R) != RGRID:
                errors.append(loc + ':' + tag + ':R')

            for rr in per_rho:
                if rr.get('decision_arithmetic') != 'arb_exact_predicates_before_float_serialization':
                    errors.append(loc + ':' + tag + ':decision')
                if not isinstance(rr.get('slope_floor_satisfied'), bool):
                    errors.append(loc + ':' + tag + ':floor_bool_missing')
                if not isinstance(rr.get('drift_within_tolerance'), bool):
                    errors.append(loc + ':' + tag + ':drift_bool_missing')
                if rr.get('within_tolerance') is not bool(
                    rr.get('slope_floor_satisfied') and rr.get('drift_within_tolerance')
                ):
                    errors.append(loc + ':' + tag + ':composite')

            for rr in fixed:
                cand = rr.get('candidate_union', [])
                inc = rr.get('ineligible_candidates', [])
                viol = rr.get('violating_channel_indices', [])
                if rr.get('decision_arithmetic') != 'arb_exact_per_channel_predicates_before_float_serialization':
                    errors.append(loc + ':' + tag + ':fixed_decision')
                if rr.get('candidate_count') != len(cand):
                    errors.append(loc + ':' + tag + ':candidate_count')
                if len(cand) != len(set(cand)) or any(not isinstance(i, int) or i < 0 or i >= 243 for i in cand):
                    errors.append(loc + ':' + tag + ':candidate')
                if any(i not in cand for i in inc + viol):
                    errors.append(loc + ':' + tag + ':fixed_identity')
                if set(inc) & set(viol):
                    errors.append(loc + ':' + tag + ':ineligible_violating_overlap')
                complete = bool(not inc and rr.get('eligible_count') == len(cand))
                if rr.get('competition_test_complete') is not complete:
                    errors.append(loc + ':' + tag + ':complete')
                derived = bool(complete and len(cand) > 0 and not viol)
                if rr.get('all_candidate_fixed_channel_drifts_within_tolerance') is not derived:
                    errors.append(loc + ':' + tag + ':fixed_bool')

            for Rrow in per_R:
                if tuple(float(q.get('rho')) for q in Rrow.get('rho', [])) != RHOS:
                    errors.append(loc + ':' + tag + ':Rrho:' + str(Rrow.get('R')))
                for q in Rrow.get('rho', []):
                    inds = q.get('possible_indices', [])
                    if q.get('possible_count') != len(inds):
                        errors.append(loc + ':' + tag + ':possible_count')
                    if len(inds) != len(set(inds)) or any(not isinstance(i, int) or i < 0 or i >= 243 for i in inds):
                        errors.append(loc + ':' + tag + ':possible_indices')
                    if not isinstance(q.get('strict_unique_max'), bool):
                        errors.append(loc + ':' + tag + ':dominance_bool')

        recomputed = []
        for rho in RHOS:
            F = one(c['full_D']['per_rho'], rho)
            C = one(c['center_D_sensitivity']['per_rho'], rho)
            FF = one(c['full_D']['fixed_channel'], rho)
            CF = one(c['center_D_sensitivity']['fixed_channel'], rho)
            full_viol = not F['drift_within_tolerance']
            center_viol = not C['drift_within_tolerance']
            recomputed.append({
                'rho': rho,
                'full_D_within_tolerance': F['within_tolerance'],
                'derivative_radius_sensitivity': bool(full_viol and C['drift_within_tolerance']),
                'competition_necessary_full_D': bool(full_viol and FF['competition_test_complete'] and fixed_all(FF)),
                'competition_necessary_center_D': bool(center_viol and CF['competition_test_complete'] and fixed_all(CF)),
                'fixed_channel_nonstationarity_center_D': bool(center_viol and CF['competition_test_complete'] and not fixed_all(CF)),
                'decision_arithmetic': 'producer_exact_arb_booleans',
            })
        if c.get('mechanism_flags') != recomputed:
            errors.append(loc + ':flags')

    return errors


def classify(cases):
    mids = []
    endpoints = []
    center_viol = []
    for c in cases:
        for rho in RHOS:
            F = one(c['full_D']['per_rho'], rho)
            C = one(c['center_D_sensitivity']['per_rho'], rho)
            CF = one(c['center_D_sensitivity']['fixed_channel'], rho)
            rec = {
                'root_box': c['root_box'],
                'location': c['location'],
                'rho': rho,
                'full_within': F['within_tolerance'],
                'full_violate': not F['drift_within_tolerance'],
                'center_violate': not C['drift_within_tolerance'],
                'derivative_radius_sensitivity': bool(
                    (not F['drift_within_tolerance']) and C['drift_within_tolerance']
                ),
                'center_complete': CF['competition_test_complete'],
                'competition_center': bool(
                    (not C['drift_within_tolerance'])
                    and CF['competition_test_complete']
                    and fixed_all(CF)
                ),
                'fixed_center': bool(
                    (not C['drift_within_tolerance'])
                    and CF['competition_test_complete']
                    and not fixed_all(CF)
                ),
            }
            (mids if c['location'] == 'MID' else endpoints).append(rec)
            if rec['center_violate']:
                center_viol.append(rec)

    endpoint_viol = [x for x in endpoints if x['full_violate']]
    deriv = bool(
        mids
        and all(x['full_within'] for x in mids)
        and endpoint_viol
        and all(x['derivative_radius_sensitivity'] for x in endpoint_viol)
        and not center_viol
    )
    if deriv:
        return CL_DERIV, mids, endpoints, endpoint_viol, center_viol
    if center_viol and all(
        x['center_complete'] and x['competition_center'] and not x['fixed_center']
        for x in center_viol
    ):
        return CL_COMP, mids, endpoints, endpoint_viol, center_viol
    if center_viol and all(x['center_complete'] for x in center_viol) and any(
        x['fixed_center'] for x in center_viol
    ):
        return CL_FIXED, mids, endpoints, endpoint_viol, center_viol
    return CL_MIX, mids, endpoints, endpoint_viol, center_viol


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root13', required=True)
    ap.add_argument('--root14', required=True)
    ap.add_argument('--root15', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    cases = []
    errors = []
    hashes = {}
    for k, p in ((13, a.root13), (14, a.root14), (15, a.root15)):
        obj, h = read_one(p)
        hashes[str(k)] = h
        errors += [f'{k}:{x}' for x in validate_root(obj, k)]
        cases += [dict(c, root_box=k) for c in obj.get('cases', [])]

    cls = INVALID
    mids = []
    endpoints = []
    endpoint_viol = []
    center_viol = []
    if not errors:
        cls, mids, endpoints, endpoint_viol, center_viol = classify(cases)

    out = {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'repair_preregistrations': REPAIRS,
        'classification': cls,
        'errors': errors,
        'root_input_sha256': hashes,
        'case_count': len(cases) * 4,
        'root_location_count': len(cases),
        'mid_case_count': len(mids),
        'endpoint_case_count': len(endpoints),
        'endpoint_full_D_violation_count': len(endpoint_viol),
        'center_D_violation_count': len(center_viol),
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'scientific_decision_transport': 'exact_arb_booleans_float_bounds_display_only',
        'fixed_channel_competition_semantics': 'drift_only_exact_producer_booleans',
        'center_D_is_control_only': True,
        'cases': cases,
        'claim_ceiling': 'Iter504S nine-point mechanism diagnostic only; no full-domain theorem',
    }
    payload = json.dumps(out, sort_keys=True, separators=(',', ':')).encode()
    out['payload_sha256'] = hashlib.sha256(payload).hexdigest()
    p = Path(a.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'cases'}, indent=2, sort_keys=True))
    return 2 if cls == INVALID else 0


if __name__ == '__main__':
    raise SystemExit(main())
