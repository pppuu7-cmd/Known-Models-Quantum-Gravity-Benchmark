#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path

GATE = 'ITER504S_ROOT_DERIVATIVE_VS_CHANNEL_COMPETITION_DISCRIMINATOR'
PREREG = 'f6367456aa715fe6282ab70c1b2005971a4568c7'
REPAIR_DERIVATIVE = '88c92f86a765e9d8b441152674fc2c303f3f1ff3'
REPAIR_DRIFT = '4ef41c0f4ceed3082fd4d80930ef5d848f18802b'
ROOTS = (13, 14, 15)
LOCS = ('LOW', 'MID', 'HIGH')
RHOS = (0.35, 0.9, 1.6, 2.7)
RGRID = (6, 8, 10, 12)
TOL = 0.05
FLOOR = 1.0
CL_DERIV = 'ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED'
CL_COMP = 'ITER504S_CHANNEL_COMPETITION_NECESSARY_SCOPED'
CL_FIXED = 'ITER504S_FIXED_CHANNEL_NONSTATIONARITY_REMAINS_SCOPED'
CL_MIX = 'ITER504S_MIXED_MECHANISM_SCOPED'
INVALID = 'ITER504S_INVALID'


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def expected_points(k):
    lo = Fraction(16 + k, 12800)
    hi = Fraction(17 + k, 12800)
    mid = (lo + hi) / 2
    return {'LOW': lo, 'MID': mid, 'HIGH': hi}


def one_rho(rows, rho):
    hits = [x for x in rows if float(x.get('rho')) == rho]
    if len(hits) != 1:
        raise ValueError(f'rho={rho} count={len(hits)}')
    return hits[0]


def fixed_drift_all_within(row):
    cand = row.get('candidate_union', [])
    inc = row.get('ineligible_candidates', [])
    complete = bool(not inc and int(row.get('eligible_count', -1)) == len(cand))
    mx = row.get('max_fixed_channel_drift_upper')
    return bool(complete and len(cand) > 0 and mx is not None and float(mx) <= TOL)


def validate_fixed_row(rr, tag, errors):
    cand = rr.get('candidate_union', [])
    inc = rr.get('ineligible_candidates', [])
    if len(cand) != len(set(cand)) or any(not isinstance(i, int) or i < 0 or i >= 243 for i in cand):
        errors.append(tag + ':candidate_union')
    if any(i not in cand for i in inc):
        errors.append(tag + ':ineligible_not_candidate')
    complete = bool(not inc and int(rr.get('eligible_count', -1)) == len(cand))
    if rr.get('competition_test_complete') is not complete:
        errors.append(tag + ':competition_complete')
    derived = fixed_drift_all_within(rr)
    if rr.get('all_candidate_fixed_channel_drifts_within_tolerance') is not derived:
        errors.append(tag + ':drift_only_predicate')
    mx = rr.get('max_fixed_channel_drift_upper')
    wit = rr.get('max_fixed_channel_witness')
    if (mx is None) != (wit is None):
        errors.append(tag + ':max_witness_presence')
    if wit is not None:
        try:
            if int(wit.get('channel')) not in cand:
                errors.append(tag + ':witness_not_candidate')
            if float(wit.get('drift_upper')) != float(mx):
                errors.append(tag + ':witness_drift')
            if bool(wit.get('drift_within_tolerance')) is not bool(float(mx) <= TOL):
                errors.append(tag + ':witness_drift_predicate')
        except Exception:
            errors.append(tag + ':witness_parse')


def validate_treatment(t, tag, errors):
    perrho = t.get('per_rho', [])
    fixed = t.get('fixed_channel', [])
    perR = t.get('per_R', [])
    if tuple(float(x.get('rho')) for x in perrho) != RHOS:
        errors.append(tag + ':rho_grid')
    if tuple(float(x.get('rho')) for x in fixed) != RHOS:
        errors.append(tag + ':fixed_rho_grid')
    if tuple(x.get('R') for x in perR) != RGRID:
        errors.append(tag + ':R_grid')
    for rr in perrho:
        calc = bool(float(rr.get('S_lower')) >= FLOOR and float(rr.get('drift_upper')) <= TOL)
        if rr.get('within_tolerance') is not calc:
            errors.append(tag + ':within:' + str(rr.get('rho')))
    for rr in fixed:
        validate_fixed_row(rr, tag + ':fixed:' + str(rr.get('rho')), errors)
    for rrow in perR:
        if tuple(float(x.get('rho')) for x in rrow.get('rho', [])) != RHOS:
            errors.append(tag + ':R_rho_grid:' + str(rrow.get('R')))
        for q in rrow.get('rho', []):
            inds = q.get('possible_indices', [])
            if q.get('possible_count') != len(inds):
                errors.append(tag + ':possible_count')
            if len(inds) != len(set(inds)) or any(not isinstance(i, int) or i < 0 or i >= 243 for i in inds):
                errors.append(tag + ':possible_indices')


def validate_root(obj, k):
    e = []
    if obj.get('invalid'):
        e.append('producer_invalid')
    if obj.get('gate') != GATE:
        e.append('gate')
    if obj.get('preregistration_commit') != PREREG:
        e.append('prereg')
    if obj.get('repair_preregistrations') != [REPAIR_DERIVATIVE, REPAIR_DRIFT]:
        e.append('repair_preregistrations')
    if obj.get('root_box') != k:
        e.append('root_box')
    if obj.get('causal') != '0to5' or obj.get('block') != 0 or obj.get('path') != 2:
        e.append('lane')
    if obj.get('direction') != [1, 1, 1, -1, -1, -1] or obj.get('sign') != 1:
        e.append('path_sign')
    if obj.get('precision_bits') != 384:
        e.append('precision')
    if obj.get('full_channel_count') != 243:
        e.append('full_channel_count')
    if obj.get('channel_pruning_used') is not False:
        e.append('channel_pruning')
    if obj.get('root_model_build_count') != 1:
        e.append('root_model_build_count')
    if obj.get('derivative_recomputed_at_points') is not False:
        e.append('point_derivative_recompute')
    if obj.get('derivative_channel_representation') != 'ad.as_c(z).d':
        e.append('derivative_representation')
    if obj.get('full_D_derivative_treatment') != 'unchanged_full_root_acb_derivative_ball':
        e.append('full_D_derivative_treatment')
    if obj.get('center_D_derivative_treatment') != 'deterministic_midpoint_of_same_full_root_acb_derivative_ball':
        e.append('center_D_derivative_treatment')
    controls = obj.get('root_controls')
    if not isinstance(controls, dict) or not controls or not all(controls.values()):
        e.append('root_controls')
    cases = obj.get('cases', [])
    if tuple(c.get('location') for c in cases) != LOCS:
        e.append('locations')
    pts = expected_points(k)
    for c in cases:
        loc = c.get('location')
        if loc not in pts:
            continue
        try:
            if Fraction(c.get('amp_q')) != pts[loc]:
                e.append(loc + ':amp')
            if Fraction(c.get('delta_q')) != pts[loc] - pts['MID']:
                e.append(loc + ':delta')
        except Exception:
            e.append(loc + ':rational_parse')
        validate_treatment(c.get('full_D', {}), loc + ':full_D', e)
        validate_treatment(c.get('center_D_sensitivity', {}), loc + ':center_D', e)
        flags = c.get('mechanism_flags', [])
        if tuple(float(x.get('rho')) for x in flags) != RHOS:
            e.append(loc + ':flag_rhos')
        recomputed = []
        try:
            for rho in RHOS:
                F = one_rho(c['full_D']['per_rho'], rho)
                C = one_rho(c['center_D_sensitivity']['per_rho'], rho)
                FF = one_rho(c['full_D']['fixed_channel'], rho)
                CF = one_rho(c['center_D_sensitivity']['fixed_channel'], rho)
                ff_all = fixed_drift_all_within(FF)
                cf_all = fixed_drift_all_within(CF)
                recomputed.append({
                    'rho': rho,
                    'full_D_within_tolerance': bool(float(F['S_lower']) >= FLOOR and float(F['drift_upper']) <= TOL),
                    'derivative_radius_sensitivity': bool(float(F['drift_upper']) > TOL and float(C['drift_upper']) <= TOL),
                    'competition_necessary_full_D': bool(float(F['drift_upper']) > TOL and FF['competition_test_complete'] and ff_all),
                    'competition_necessary_center_D': bool(float(C['drift_upper']) > TOL and CF['competition_test_complete'] and cf_all),
                    'fixed_channel_nonstationarity_center_D': bool(float(C['drift_upper']) > TOL and CF['competition_test_complete'] and not cf_all),
                })
        except Exception as ex:
            e.append(loc + ':flag_recompute:' + repr(ex))
            recomputed = []
        if flags != recomputed:
            e.append(loc + ':mechanism_flags')
    return e


def cases_from_roots(roots):
    out = []
    for k in ROOTS:
        for c in roots[k]['cases']:
            z = copy.deepcopy(c)
            z['root_box'] = k
            out.append(z)
    return out


def independent_classify(roots):
    cases = cases_from_roots(roots)
    mids = []
    endpoints = []
    center_viol = []
    for c in cases:
        for rho in RHOS:
            F = one_rho(c['full_D']['per_rho'], rho)
            C = one_rho(c['center_D_sensitivity']['per_rho'], rho)
            CF = one_rho(c['center_D_sensitivity']['fixed_channel'], rho)
            cf_all = fixed_drift_all_within(CF)
            rec = {
                'root_box': c['root_box'],
                'location': c['location'],
                'rho': rho,
                'full_within': bool(float(F['S_lower']) >= FLOOR and float(F['drift_upper']) <= TOL),
                'full_violate': bool(float(F['drift_upper']) > TOL),
                'center_violate': bool(float(C['drift_upper']) > TOL),
                'derivative_radius_sensitivity': bool(float(F['drift_upper']) > TOL and float(C['drift_upper']) <= TOL),
                'center_complete': bool(CF['competition_test_complete']),
                'competition_center': bool(float(C['drift_upper']) > TOL and CF['competition_test_complete'] and cf_all),
                'fixed_nonstationarity_center': bool(float(C['drift_upper']) > TOL and CF['competition_test_complete'] and not cf_all),
            }
            if c['location'] == 'MID':
                mids.append(rec)
            else:
                endpoints.append(rec)
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
        return CL_DERIV
    if center_viol and all(
        x['center_complete'] and x['competition_center'] and not x['fixed_nonstationarity_center']
        for x in center_viol
    ):
        return CL_COMP
    if center_viol and all(x['center_complete'] for x in center_viol) and any(
        x['fixed_nonstationarity_center'] for x in center_viol
    ):
        return CL_FIXED
    return CL_MIX


def discrete_projection(roots):
    p = []
    for k in ROOTS:
        for c in roots[k]['cases']:
            row = {'root_box': k, 'location': c['location'], 'amp_q': c['amp_q'], 'rho': [], 'R': []}
            for rho in RHOS:
                F = one_rho(c['full_D']['per_rho'], rho)
                C = one_rho(c['center_D_sensitivity']['per_rho'], rho)
                FF = one_rho(c['full_D']['fixed_channel'], rho)
                CF = one_rho(c['center_D_sensitivity']['fixed_channel'], rho)
                row['rho'].append((
                    rho,
                    F['within_tolerance'],
                    float(F['drift_upper']) > TOL,
                    C['within_tolerance'],
                    float(C['drift_upper']) > TOL,
                    tuple(FF['candidate_union']),
                    FF['competition_test_complete'],
                    fixed_drift_all_within(FF),
                    tuple(CF['candidate_union']),
                    CF['competition_test_complete'],
                    fixed_drift_all_within(CF),
                ))
            for treatment in ('full_D', 'center_D_sensitivity'):
                for rr in c[treatment]['per_R']:
                    row['R'].append((
                        treatment,
                        rr['R'],
                        tuple((float(q['rho']), tuple(q['possible_indices']), bool(q['strict_unique_max'])) for q in rr['rho']),
                    ))
            p.append(row)
    return p


def validate_assembled(obj, roots, cls):
    e = []
    if obj.get('gate') != GATE:
        e.append('gate')
    if obj.get('preregistration_commit') != PREREG:
        e.append('prereg')
    if obj.get('repair_preregistrations') != [REPAIR_DERIVATIVE, REPAIR_DRIFT]:
        e.append('repair_preregistrations')
    if obj.get('threshold') != TOL:
        e.append('threshold')
    if obj.get('robust_floor') != FLOOR:
        e.append('floor')
    if obj.get('center_D_is_control_only') is not True:
        e.append('center_D_control_label')
    if obj.get('fixed_channel_competition_semantics') != 'drift_only':
        e.append('fixed_channel_semantics')
    if obj.get('errors') not in ([], None):
        e.append('producer_errors')
    if obj.get('classification') != cls:
        e.append('classification')
    if obj.get('root_location_count') != 9 or obj.get('case_count') != 36:
        e.append('case_counts')
    got = {(c.get('root_box'), c.get('location'), c.get('amp_q')) for c in obj.get('cases', [])}
    exp = {(k, c['location'], c['amp_q']) for k in ROOTS for c in roots[k]['cases']}
    if got != exp:
        e.append('case_identity_set')
    return e


def negative_controls(base_roots, base_assembled):
    tests = {}

    def rejected(name, mutate_roots=None, mutate_assembled=None):
        roots = copy.deepcopy(base_roots)
        asm = copy.deepcopy(base_assembled)
        if mutate_roots:
            mutate_roots(roots)
        if mutate_assembled:
            mutate_assembled(asm)
        errs = []
        for k in ROOTS:
            if k not in roots:
                errs.append('missing_root:' + str(k))
                continue
            errs += [f'{k}:{x}' for x in validate_root(roots[k], k)]
        if not errs and all(k in roots for k in ROOTS):
            try:
                cls = independent_classify(roots)
                errs += validate_assembled(asm, roots, cls)
            except Exception as ex:
                errs.append('exception:' + repr(ex))
        tests[name] = bool(errs)

    rejected('missing_root', lambda r: r.pop(15))
    rejected('missing_location', lambda r: r[13]['cases'].pop())
    rejected('missing_rho', lambda r: r[13]['cases'][0]['full_D']['per_rho'].pop())
    rejected('wrong_exact_amplitude', lambda r: r[13]['cases'][0].__setitem__('amp_q', '1/2'))
    rejected('threshold_changed', mutate_assembled=lambda a: a.__setitem__('threshold', 0.051))
    rejected('floor_changed', mutate_assembled=lambda a: a.__setitem__('robust_floor', 0.99))
    rejected('omitted_channel', lambda r: r[13].__setitem__('full_channel_count', 242))
    rejected('active_channel_pruning', lambda r: r[13].__setitem__('channel_pruning_used', True))
    rejected('point_derivative_recompute', lambda r: r[13].__setitem__('derivative_recomputed_at_points', True))
    rejected('wrong_derivative_representation', lambda r: r[13].__setitem__('derivative_channel_representation', 'dual_CD'))
    rejected('center_D_mislabeled_rigorous', lambda r: r[13].__setitem__('center_D_derivative_treatment', 'validated_enclosure'))
    rejected('wrong_root', lambda r: r[13].__setitem__('root_box', 14))
    rejected('wrong_path_sign', lambda r: r[13].__setitem__('sign', -1))
    rejected('wrong_rho', lambda r: r[13]['cases'][0]['full_D']['per_rho'][0].__setitem__('rho', 0.36))
    rejected('wrong_R_grid', lambda r: r[13]['cases'][0]['full_D']['per_R'][0].__setitem__('R', 7))

    def exclude_ineligible(r):
        q = r[13]['cases'][0]['full_D']['fixed_channel'][0]
        q['candidate_union'] = [0]
        q['eligible_count'] = 0
        q['ineligible_candidates'] = []
        q['competition_test_complete'] = True
        q['max_fixed_channel_drift_upper'] = None
        q['max_fixed_channel_witness'] = None
        q['all_candidate_fixed_channel_drifts_within_tolerance'] = False

    rejected('silently_excluded_ineligible_candidate', exclude_ineligible)

    def corrupt_drift_boolean(r):
        q = r[13]['cases'][0]['full_D']['fixed_channel'][0]
        q['all_candidate_fixed_channel_drifts_within_tolerance'] = not bool(q['all_candidate_fixed_channel_drifts_within_tolerance'])

    rejected('trusted_corrupted_fixed_drift_boolean', corrupt_drift_boolean)

    def slope_floor_cannot_define_competition(r):
        q = r[13]['cases'][0]['full_D']['fixed_channel'][0]
        if q.get('max_fixed_channel_witness') is not None:
            q['max_fixed_channel_witness']['S_lower'] = -999.0

    # This mutation must NOT be rejected solely by competition semantics. It is a diagnostic control
    # proving the critic no longer uses fixed-channel S_lower in the drift-only competition predicate.
    roots = copy.deepcopy(base_roots)
    asm = copy.deepcopy(base_assembled)
    slope_floor_cannot_define_competition(roots)
    errs = []
    for k in ROOTS:
        errs += [f'{k}:{x}' for x in validate_root(roots[k], k)]
    if not errs:
        try:
            cls = independent_classify(roots)
            errs += validate_assembled(asm, roots, cls)
        except Exception as ex:
            errs.append('exception:' + repr(ex))
    tests['fixed_channel_slope_floor_ignored_by_competition'] = not bool(errs)
    return tests


def main():
    ap = argparse.ArgumentParser()
    for lane in ('a', 'b'):
        for k in ROOTS:
            ap.add_argument(f'--{lane}-root{k}', required=True)
        ap.add_argument(f'--{lane}-assembled', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    lanes = {}
    errors = []
    for lane in ('a', 'b'):
        roots = {}
        hashes = {}
        lane_errors = []
        for k in ROOTS:
            obj, h = load(getattr(a, f'{lane}_root{k}'))
            roots[k] = obj
            hashes[str(k)] = h
            lane_errors += [f'{lane}:{k}:{x}' for x in validate_root(obj, k)]
        asm, ah = load(getattr(a, f'{lane}_assembled'))
        cls = INVALID if lane_errors else independent_classify(roots)
        lane_errors += [f'{lane}:assembled:{x}' for x in validate_assembled(asm, roots, cls)]
        errors += lane_errors
        lanes[lane] = {
            'roots': roots,
            'root_sha256': hashes,
            'assembled': asm,
            'assembled_sha256': ah,
            'recomputed_classification': cls,
        }
    if not errors:
        if lanes['a']['recomputed_classification'] != lanes['b']['recomputed_classification']:
            errors.append('cross_env_classification')
        if discrete_projection(lanes['a']['roots']) != discrete_projection(lanes['b']['roots']):
            errors.append('cross_env_discrete_projection')
    neg = negative_controls(lanes['a']['roots'], lanes['a']['assembled'])
    if not all(neg.values()):
        errors.append('negative_control_not_rejected_or_positive_control_failed')
    cls = INVALID if errors else lanes['a']['recomputed_classification']
    summary = {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'repair_preregistrations': [REPAIR_DERIVATIVE, REPAIR_DRIFT],
        'classification': cls,
        'critic_errors': errors,
        'lane_a_root_sha256': lanes['a']['root_sha256'],
        'lane_b_root_sha256': lanes['b']['root_sha256'],
        'lane_a_assembled_sha256': lanes['a']['assembled_sha256'],
        'lane_b_assembled_sha256': lanes['b']['assembled_sha256'],
        'cross_environment_discrete_agreement': bool(not errors and discrete_projection(lanes['a']['roots']) == discrete_projection(lanes['b']['roots'])),
        'fixed_channel_competition_semantics': 'drift_only_reconstructed_from_max_fixed_channel_drift_upper',
        'negative_and_semantic_controls': neg,
        'claim_ceiling': 'Independent Iter504S adversarial verification only; no full-domain theorem',
    }
    payload = json.dumps(summary, sort_keys=True, separators=(',', ':')).encode()
    summary['critic_payload_sha256'] = hashlib.sha256(payload).hexdigest()
    p = Path(a.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 2 if cls == INVALID else 0


if __name__ == '__main__':
    raise SystemExit(main())
