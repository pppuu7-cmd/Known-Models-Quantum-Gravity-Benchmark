#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

GATE = 'ITER504S_ROOT_DERIVATIVE_VS_CHANNEL_COMPETITION_DISCRIMINATOR'
PREREG = 'f6367456aa715fe6282ab70c1b2005971a4568c7'
REPAIR_DERIVATIVE = '88c92f86a765e9d8b441152674fc2c303f3f1ff3'
REPAIR_DRIFT = '4ef41c0f4ceed3082fd4d80930ef5d848f18802b'
ROOTS = (13, 14, 15)
RHOS = (0.35, 0.9, 1.6, 2.7)
LOCS = ('LOW', 'MID', 'HIGH')
TOL = 0.05
FLOOR = 1.0
CL_DERIV = 'ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED'
CL_COMP = 'ITER504S_CHANNEL_COMPETITION_NECESSARY_SCOPED'
CL_FIXED = 'ITER504S_FIXED_CHANNEL_NONSTATIONARITY_REMAINS_SCOPED'
CL_MIX = 'ITER504S_MIXED_MECHANISM_SCOPED'
INVALID = 'ITER504S_INVALID'


def read_one(p):
    raw = Path(p).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def root_points(k):
    lo = Fraction(16 + k, 12800)
    hi = Fraction(17 + k, 12800)
    mid = (lo + hi) / 2
    return {'LOW': lo, 'MID': mid, 'HIGH': hi}


def row_by_rho(rows, rho):
    hits = [x for x in rows if float(x.get('rho')) == rho]
    if len(hits) != 1:
        raise ValueError(f'rho {rho} count {len(hits)}')
    return hits[0]


def fixed_drift_all_within(row):
    cand = row.get('candidate_union', [])
    inc = row.get('ineligible_candidates', [])
    complete = bool(not inc and int(row.get('eligible_count', -1)) == len(cand))
    mx = row.get('max_fixed_channel_drift_upper')
    return bool(complete and len(cand) > 0 and mx is not None and float(mx) <= TOL)


def validate_fixed_row(rr, tag, errors):
    cand = rr.get('candidate_union', [])
    if len(cand) != len(set(cand)) or any(not isinstance(i, int) or i < 0 or i >= 243 for i in cand):
        errors.append(tag + ':candidate_union')
    inc = rr.get('ineligible_candidates', [])
    if any(i not in cand for i in inc):
        errors.append(tag + ':ineligible_not_candidate')
    complete = bool(not inc and int(rr.get('eligible_count', -1)) == len(cand))
    if rr.get('competition_test_complete') is not complete:
        errors.append(tag + ':competition_complete')
    derived = fixed_drift_all_within(rr)
    if rr.get('all_candidate_fixed_channel_drifts_within_tolerance') is not derived:
        errors.append(tag + ':drift_only_predicate')
    wit = rr.get('max_fixed_channel_witness')
    mx = rr.get('max_fixed_channel_drift_upper')
    if (mx is None) != (wit is None):
        errors.append(tag + ':max_witness_presence')
    if wit is not None:
        if float(wit.get('drift_upper')) != float(mx):
            errors.append(tag + ':max_witness_drift')
        if bool(wit.get('drift_within_tolerance')) is not bool(float(mx) <= TOL):
            errors.append(tag + ':witness_drift_predicate')


def validate_root(obj, k):
    errors = []
    if obj.get('invalid'):
        errors.append('producer_invalid')
    if obj.get('gate') != GATE:
        errors.append('gate')
    if obj.get('preregistration_commit') != PREREG:
        errors.append('prereg')
    if obj.get('repair_preregistrations') != [REPAIR_DERIVATIVE, REPAIR_DRIFT]:
        errors.append('repair_preregistrations')
    if obj.get('root_box') != k:
        errors.append('root_box')
    if obj.get('causal') != '0to5' or obj.get('block') != 0 or obj.get('path') != 2:
        errors.append('lane')
    if obj.get('direction') != [1, 1, 1, -1, -1, -1] or obj.get('sign') != 1:
        errors.append('path_sign')
    if obj.get('precision_bits') != 384:
        errors.append('precision')
    if obj.get('full_channel_count') != 243:
        errors.append('channels')
    if obj.get('channel_pruning_used') is not False:
        errors.append('pruning')
    if obj.get('root_model_build_count') != 1:
        errors.append('model_count')
    if obj.get('derivative_recomputed_at_points') is not False:
        errors.append('derivative_recompute')
    if obj.get('derivative_channel_representation') != 'ad.as_c(z).d':
        errors.append('derivative_representation')
    if obj.get('full_D_derivative_treatment') != 'unchanged_full_root_acb_derivative_ball':
        errors.append('full_D_derivative_treatment')
    if obj.get('center_D_derivative_treatment') != 'deterministic_midpoint_of_same_full_root_acb_derivative_ball':
        errors.append('center_D_derivative_treatment')
    if not obj.get('root_controls') or not all(obj['root_controls'].values()):
        errors.append('controls')
    cases = obj.get('cases', [])
    if [x.get('location') for x in cases] != list(LOCS):
        errors.append('locations')
    pts = root_points(k)
    out = []
    for c in cases:
        loc = c.get('location')
        if loc not in pts:
            continue
        try:
            if Fraction(c.get('amp_q', '0')) != pts[loc]:
                errors.append(f'amp:{loc}')
            if Fraction(c.get('delta_q', '0')) != pts[loc] - pts['MID']:
                errors.append(f'delta:{loc}')
        except Exception:
            errors.append(f'rational_parse:{loc}')
        for treat in ('full_D', 'center_D_sensitivity'):
            q = c.get(treat, {})
            pr = q.get('per_rho', [])
            fc = q.get('fixed_channel', [])
            perR = q.get('per_R', [])
            if tuple(float(x.get('rho')) for x in pr) != RHOS:
                errors.append(f'{loc}:{treat}:rho')
            if tuple(float(x.get('rho')) for x in fc) != RHOS:
                errors.append(f'{loc}:{treat}:fixedrho')
            if [x.get('R') for x in perR] != [6, 8, 10, 12]:
                errors.append(f'{loc}:{treat}:R')
            for rr in pr:
                calc = bool(float(rr['S_lower']) >= FLOOR and float(rr['drift_upper']) <= TOL)
                if rr.get('within_tolerance') is not calc:
                    errors.append(f'{loc}:{treat}:within:{rr.get("rho")}')
            for rr in fc:
                validate_fixed_row(rr, f'{loc}:{treat}:fixed:{rr.get("rho")}', errors)
            for Rrow in perR:
                if tuple(float(x.get('rho')) for x in Rrow.get('rho', [])) != RHOS:
                    errors.append(f'{loc}:{treat}:Rrho:{Rrow.get("R")}')
                for z in Rrow.get('rho', []):
                    inds = z.get('possible_indices', [])
                    if z.get('possible_count') != len(inds) or len(inds) != len(set(inds)) or any(i < 0 or i >= 243 for i in inds):
                        errors.append(f'{loc}:{treat}:possible')
        flags = []
        for rho in RHOS:
            F = row_by_rho(c['full_D']['per_rho'], rho)
            C = row_by_rho(c['center_D_sensitivity']['per_rho'], rho)
            FF = row_by_rho(c['full_D']['fixed_channel'], rho)
            CF = row_by_rho(c['center_D_sensitivity']['fixed_channel'], rho)
            ff_all = fixed_drift_all_within(FF)
            cf_all = fixed_drift_all_within(CF)
            flags.append({
                'rho': rho,
                'full_D_within_tolerance': bool(float(F['S_lower']) >= FLOOR and float(F['drift_upper']) <= TOL),
                'derivative_radius_sensitivity': bool(float(F['drift_upper']) > TOL and float(C['drift_upper']) <= TOL),
                'competition_necessary_full_D': bool(float(F['drift_upper']) > TOL and FF['competition_test_complete'] and ff_all),
                'competition_necessary_center_D': bool(float(C['drift_upper']) > TOL and CF['competition_test_complete'] and cf_all),
                'fixed_channel_nonstationarity_center_D': bool(float(C['drift_upper']) > TOL and CF['competition_test_complete'] and not cf_all),
            })
        if c.get('mechanism_flags') != flags:
            errors.append(f'{loc}:flags_mismatch')
        out.append({
            'location': loc,
            'amp_q': c.get('amp_q'),
            'flags': flags,
            'full_D': c['full_D'],
            'center_D_sensitivity': c['center_D_sensitivity'],
        })
    return errors, out


def classify(roots):
    cases = []
    for r in roots:
        cases += r['cases']
    mids = []
    endpoints = []
    center_viol = []
    for c in cases:
        for rho in RHOS:
            F = row_by_rho(c['full_D']['per_rho'], rho)
            C = row_by_rho(c['center_D_sensitivity']['per_rho'], rho)
            FF = row_by_rho(c['full_D']['fixed_channel'], rho)
            CF = row_by_rho(c['center_D_sensitivity']['fixed_channel'], rho)
            cf_all = fixed_drift_all_within(CF)
            rec = {
                'root_box': c['root_box'],
                'location': c['location'],
                'amp_q': c['amp_q'],
                'rho': rho,
                'full_S_lower': F['S_lower'],
                'full_drift_upper': F['drift_upper'],
                'full_within': bool(float(F['S_lower']) >= FLOOR and float(F['drift_upper']) <= TOL),
                'center_S_lower': C['S_lower'],
                'center_drift_upper': C['drift_upper'],
                'center_within': bool(float(C['S_lower']) >= FLOOR and float(C['drift_upper']) <= TOL),
                'derivative_radius_sensitivity': bool(float(F['drift_upper']) > TOL and float(C['drift_upper']) <= TOL),
                'competition_necessary_center_D': bool(float(C['drift_upper']) > TOL and CF['competition_test_complete'] and cf_all),
                'fixed_channel_nonstationarity_center_D': bool(float(C['drift_upper']) > TOL and CF['competition_test_complete'] and not cf_all),
                'center_competition_test_complete': bool(CF['competition_test_complete']),
                'full_competition_test_complete': bool(FF['competition_test_complete']),
            }
            if c['location'] == 'MID':
                mids.append(rec)
            else:
                endpoints.append(rec)
            if float(C['drift_upper']) > TOL:
                center_viol.append(rec)
    endpoint_viol = [x for x in endpoints if float(x['full_drift_upper']) > TOL]
    deriv = bool(
        mids
        and all(x['full_within'] for x in mids)
        and endpoint_viol
        and all(x['derivative_radius_sensitivity'] for x in endpoint_viol)
        and not center_viol
    )
    if deriv:
        cls = CL_DERIV
    elif center_viol and all(
        x['center_competition_test_complete']
        and x['competition_necessary_center_D']
        and not x['fixed_channel_nonstationarity_center_D']
        for x in center_viol
    ):
        cls = CL_COMP
    elif center_viol and all(x['center_competition_test_complete'] for x in center_viol) and any(
        x['fixed_channel_nonstationarity_center_D'] for x in center_viol
    ):
        cls = CL_FIXED
    else:
        cls = CL_MIX
    return cls, cases, mids, endpoints, endpoint_viol, center_viol


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root13', required=True)
    ap.add_argument('--root14', required=True)
    ap.add_argument('--root15', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    inputs = []
    errors = []
    for k, p in ((13, a.root13), (14, a.root14), (15, a.root15)):
        obj, h = read_one(p)
        ee, cases = validate_root(obj, k)
        errors += [f'{k}:{x}' for x in ee]
        inputs.append({'root_box': k, 'sha256': h, 'obj': obj, 'cases': cases})
    roots = []
    for x in inputs:
        roots.append({'root_box': x['root_box'], 'cases': [dict(c, root_box=x['root_box']) for c in x['cases']]})
    cls = INVALID
    cases = []
    mids = []
    endpoints = []
    endpoint_viol = []
    center_viol = []
    if not errors:
        cls, cases, mids, endpoints, endpoint_viol, center_viol = classify(roots)
    max_full = max((float(row_by_rho(c['full_D']['per_rho'], rho)['drift_upper']) for c in cases for rho in RHOS), default=None)
    max_center = max((float(row_by_rho(c['center_D_sensitivity']['per_rho'], rho)['drift_upper']) for c in cases for rho in RHOS), default=None)
    min_full_S = min((float(row_by_rho(c['full_D']['per_rho'], rho)['S_lower']) for c in cases for rho in RHOS), default=None)
    max_possible = max((z['possible_count'] for c in cases for t in ('full_D', 'center_D_sensitivity') for rr in c[t]['per_R'] for z in rr['rho']), default=None)
    strict = sum(bool(z['strict_unique_max']) for c in cases for t in ('full_D', 'center_D_sensitivity') for rr in c[t]['per_R'] for z in rr['rho'])
    out = {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'repair_preregistrations': [REPAIR_DERIVATIVE, REPAIR_DRIFT],
        'classification': cls,
        'errors': errors,
        'root_input_sha256': {str(x['root_box']): x['sha256'] for x in inputs},
        'case_count': len(cases) * 4,
        'root_location_count': len(cases),
        'mid_case_count': len(mids),
        'endpoint_case_count': len(endpoints),
        'endpoint_full_D_violation_count': len(endpoint_viol),
        'center_D_violation_count': len(center_viol),
        'maximum_full_D_drift_upper': max_full,
        'maximum_center_D_drift_upper': max_center,
        'minimum_full_D_S_lower': min_full_S,
        'maximum_possible_count': max_possible,
        'strict_unique_max_certificate_count': strict,
        'cases': cases,
        'threshold': TOL,
        'robust_floor': FLOOR,
        'center_D_is_control_only': True,
        'fixed_channel_competition_semantics': 'drift_only',
        'claim_ceiling': 'Iter504S nine-point mechanism diagnostic only; no full Iter504 reclassification or global theorem',
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
