#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
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
D = 'ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED'
C = 'ITER504S_CHANNEL_COMPETITION_NECESSARY_SCOPED'
F = 'ITER504S_FIXED_CHANNEL_NONSTATIONARITY_REMAINS_SCOPED'
M = 'ITER504S_MIXED_MECHANISM_SCOPED'
INVALID = 'ITER504S_INVALID'
TRANSPORT = 'exact_arb_booleans_float_bounds_display_only'
ROW_ARITH = 'arb_exact_predicates_before_float_serialization'
FIXED_ARITH = 'arb_exact_per_channel_predicates_before_float_serialization'


def load(p):
    raw = Path(p).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def one(rows, rho):
    hits = [x for x in rows if float(x.get('rho')) == rho]
    if len(hits) != 1:
        raise ValueError(f'rho={rho} count={len(hits)}')
    return hits[0]


def expected_points(k):
    lo = Fraction(16 + k, 12800)
    hi = Fraction(17 + k, 12800)
    mid = (lo + hi) / 2
    return {'LOW': lo, 'MID': mid, 'HIGH': hi}


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


def validate_fixed_row(rr, tag, errors):
    cand = rr.get('candidate_union', [])
    inc = rr.get('ineligible_candidates', [])
    viol = rr.get('violating_channel_indices', [])
    if rr.get('decision_arithmetic') != FIXED_ARITH:
        errors.append(tag + ':decision_arithmetic')
    if rr.get('candidate_count') != len(cand):
        errors.append(tag + ':candidate_count')
    if len(cand) != len(set(cand)) or any(not isinstance(i, int) or i < 0 or i >= 243 for i in cand):
        errors.append(tag + ':candidate_union')
    if len(inc) != len(set(inc)) or any(i not in cand for i in inc):
        errors.append(tag + ':ineligible_candidates')
    if len(viol) != len(set(viol)) or any(i not in cand for i in viol):
        errors.append(tag + ':violating_channel_indices')
    if set(inc) & set(viol):
        errors.append(tag + ':ineligible_violating_overlap')
    eligible = rr.get('eligible_count')
    if not isinstance(eligible, int) or eligible < 0 or eligible > len(cand):
        errors.append(tag + ':eligible_count')
    complete = bool(not inc and eligible == len(cand))
    if rr.get('competition_test_complete') is not complete:
        errors.append(tag + ':competition_complete')
    exact_all = bool(complete and len(cand) > 0 and not viol)
    if rr.get('all_candidate_fixed_channel_drifts_within_tolerance') is not exact_all:
        errors.append(tag + ':all_within_vs_violating')
    witness = rr.get('max_fixed_channel_witness')
    mx = rr.get('max_fixed_channel_drift_upper')
    if (witness is None) != (mx is None):
        errors.append(tag + ':display_max_presence')
    if witness is not None:
        try:
            if int(witness.get('channel')) not in cand:
                errors.append(tag + ':display_witness_not_candidate')
            if not isinstance(witness.get('drift_within_tolerance'), bool):
                errors.append(tag + ':display_witness_exact_bool_missing')
        except Exception:
            errors.append(tag + ':display_witness_parse')


def validate_treatment(t, tag, errors):
    per_rho = t.get('per_rho', [])
    fixed = t.get('fixed_channel', [])
    per_R = t.get('per_R', [])
    if tuple(float(x.get('rho')) for x in per_rho) != RHOS:
        errors.append(tag + ':rho_grid')
    if tuple(float(x.get('rho')) for x in fixed) != RHOS:
        errors.append(tag + ':fixed_rho_grid')
    if tuple(x.get('R') for x in per_R) != RGRID:
        errors.append(tag + ':R_grid')

    for rr in per_rho:
        if rr.get('decision_arithmetic') != ROW_ARITH:
            errors.append(tag + ':row_decision_arithmetic:' + str(rr.get('rho')))
        if not isinstance(rr.get('slope_floor_satisfied'), bool):
            errors.append(tag + ':exact_floor_bool_missing:' + str(rr.get('rho')))
        if not isinstance(rr.get('drift_within_tolerance'), bool):
            errors.append(tag + ':exact_drift_bool_missing:' + str(rr.get('rho')))
        if not isinstance(rr.get('within_tolerance'), bool):
            errors.append(tag + ':within_bool_missing:' + str(rr.get('rho')))
        if rr.get('within_tolerance') is not bool(
            rr.get('slope_floor_satisfied') and rr.get('drift_within_tolerance')
        ):
            errors.append(tag + ':within_composite:' + str(rr.get('rho')))

    for rr in fixed:
        validate_fixed_row(rr, tag + ':fixed:' + str(rr.get('rho')), errors)

    for rrow in per_R:
        if tuple(float(x.get('rho')) for x in rrow.get('rho', [])) != RHOS:
            errors.append(tag + ':R_rho_grid:' + str(rrow.get('R')))
        for q in rrow.get('rho', []):
            inds = q.get('possible_indices', [])
            if q.get('possible_count') != len(inds):
                errors.append(tag + ':possible_count:' + str(rrow.get('R')))
            if len(inds) != len(set(inds)) or any(not isinstance(i, int) or i < 0 or i >= 243 for i in inds):
                errors.append(tag + ':possible_indices:' + str(rrow.get('R')))
            if not isinstance(q.get('strict_unique_max'), bool):
                errors.append(tag + ':dominance_bool:' + str(rrow.get('R')))


def validate_root(obj, k):
    errors = []
    checks = [
        (obj.get('gate') == GATE, 'gate'),
        (obj.get('preregistration_commit') == PREREG, 'prereg'),
        (obj.get('repair_preregistrations') == REPAIRS, 'repairs'),
        (obj.get('root_box') == k, 'root_box'),
        (obj.get('causal') == '0to5' and obj.get('block') == 0 and obj.get('path') == 2, 'lane'),
        (obj.get('direction') == [1, 1, 1, -1, -1, -1] and obj.get('sign') == 1, 'path_sign'),
        (obj.get('precision_bits') == 384, 'precision'),
        (obj.get('full_channel_count') == 243, 'full_channel_count'),
        (obj.get('channel_pruning_used') is False, 'channel_pruning'),
        (obj.get('root_model_build_count') == 1, 'root_model_build_count'),
        (obj.get('derivative_recomputed_at_points') is False, 'point_derivative_recompute'),
        (obj.get('derivative_channel_representation') == 'ad.as_c(z).d', 'derivative_representation'),
        (obj.get('full_D_derivative_treatment') == 'unchanged_full_root_acb_derivative_ball', 'full_D_derivative_treatment'),
        (obj.get('center_D_derivative_treatment') == 'deterministic_midpoint_of_same_full_root_acb_derivative_ball', 'center_D_control_only'),
        (obj.get('scientific_decision_transport') == TRANSPORT, 'scientific_decision_transport'),
    ]
    for ok, name in checks:
        if not ok:
            errors.append(name)
    if obj.get('invalid'):
        errors.append('producer_invalid')
    controls = obj.get('root_controls')
    if not isinstance(controls, dict) or not controls or not all(controls.values()):
        errors.append('root_controls')

    cases = obj.get('cases', [])
    if tuple(c.get('location') for c in cases) != LOCS:
        errors.append('locations')
    pts = expected_points(k)

    for c in cases:
        loc = c.get('location')
        if loc not in pts:
            continue
        try:
            if Fraction(c.get('amp_q')) != pts[loc]:
                errors.append(loc + ':amp')
            if Fraction(c.get('delta_q')) != pts[loc] - pts['MID']:
                errors.append(loc + ':delta')
        except Exception:
            errors.append(loc + ':rational_parse')

        validate_treatment(c.get('full_D', {}), loc + ':full_D', errors)
        validate_treatment(c.get('center_D_sensitivity', {}), loc + ':center_D', errors)

        flags = c.get('mechanism_flags', [])
        if tuple(float(x.get('rho')) for x in flags) != RHOS:
            errors.append(loc + ':flag_rhos')
        recomputed = []
        try:
            for rho in RHOS:
                full = one(c['full_D']['per_rho'], rho)
                center = one(c['center_D_sensitivity']['per_rho'], rho)
                full_fixed = one(c['full_D']['fixed_channel'], rho)
                center_fixed = one(c['center_D_sensitivity']['fixed_channel'], rho)
                full_viol = not full['drift_within_tolerance']
                center_viol = not center['drift_within_tolerance']
                recomputed.append({
                    'rho': rho,
                    'full_D_within_tolerance': full['within_tolerance'],
                    'derivative_radius_sensitivity': bool(full_viol and center['drift_within_tolerance']),
                    'competition_necessary_full_D': bool(full_viol and full_fixed['competition_test_complete'] and fixed_all(full_fixed)),
                    'competition_necessary_center_D': bool(center_viol and center_fixed['competition_test_complete'] and fixed_all(center_fixed)),
                    'fixed_channel_nonstationarity_center_D': bool(center_viol and center_fixed['competition_test_complete'] and not fixed_all(center_fixed)),
                    'decision_arithmetic': 'producer_exact_arb_booleans',
                })
        except Exception as ex:
            errors.append(loc + ':flag_recompute:' + repr(ex))
            recomputed = []
        if flags != recomputed:
            errors.append(loc + ':mechanism_flags')

    return errors


def cases_from_roots(roots):
    out = []
    for k in ROOTS:
        for c in roots[k]['cases']:
            z = copy.deepcopy(c)
            z['root_box'] = k
            out.append(z)
    return out


def classify(roots):
    cases = cases_from_roots(roots)
    mids = []
    endpoints = []
    center_viol = []
    for c in cases:
        for rho in RHOS:
            full = one(c['full_D']['per_rho'], rho)
            center = one(c['center_D_sensitivity']['per_rho'], rho)
            center_fixed = one(c['center_D_sensitivity']['fixed_channel'], rho)
            rec = {
                'root_box': c['root_box'],
                'location': c['location'],
                'rho': rho,
                'full_within': full['within_tolerance'],
                'full_violate': not full['drift_within_tolerance'],
                'center_violate': not center['drift_within_tolerance'],
                'derivative_radius_sensitivity': bool(
                    (not full['drift_within_tolerance']) and center['drift_within_tolerance']
                ),
                'center_complete': center_fixed['competition_test_complete'],
                'competition_center': bool(
                    (not center['drift_within_tolerance'])
                    and center_fixed['competition_test_complete']
                    and fixed_all(center_fixed)
                ),
                'fixed_center': bool(
                    (not center['drift_within_tolerance'])
                    and center_fixed['competition_test_complete']
                    and not fixed_all(center_fixed)
                ),
            }
            (mids if c['location'] == 'MID' else endpoints).append(rec)
            if rec['center_violate']:
                center_viol.append(rec)

    endpoint_viol = [x for x in endpoints if x['full_violate']]
    derivative = bool(
        mids
        and all(x['full_within'] for x in mids)
        and endpoint_viol
        and all(x['derivative_radius_sensitivity'] for x in endpoint_viol)
        and not center_viol
    )
    if derivative:
        return D
    if center_viol and all(
        x['center_complete'] and x['competition_center'] and not x['fixed_center']
        for x in center_viol
    ):
        return C
    if center_viol and all(x['center_complete'] for x in center_viol) and any(
        x['fixed_center'] for x in center_viol
    ):
        return F
    return M


def exact_projection(roots):
    projection = []
    for k in ROOTS:
        for c in roots[k]['cases']:
            row = {'root_box': k, 'location': c['location'], 'amp_q': c['amp_q'], 'rho': [], 'R': []}
            for rho in RHOS:
                full = one(c['full_D']['per_rho'], rho)
                center = one(c['center_D_sensitivity']['per_rho'], rho)
                full_fixed = one(c['full_D']['fixed_channel'], rho)
                center_fixed = one(c['center_D_sensitivity']['fixed_channel'], rho)
                row['rho'].append((
                    rho,
                    full['slope_floor_satisfied'],
                    full['drift_within_tolerance'],
                    full['within_tolerance'],
                    center['slope_floor_satisfied'],
                    center['drift_within_tolerance'],
                    center['within_tolerance'],
                    tuple(full_fixed['candidate_union']),
                    tuple(full_fixed['ineligible_candidates']),
                    tuple(full_fixed['violating_channel_indices']),
                    full_fixed['competition_test_complete'],
                    full_fixed['all_candidate_fixed_channel_drifts_within_tolerance'],
                    tuple(center_fixed['candidate_union']),
                    tuple(center_fixed['ineligible_candidates']),
                    tuple(center_fixed['violating_channel_indices']),
                    center_fixed['competition_test_complete'],
                    center_fixed['all_candidate_fixed_channel_drifts_within_tolerance'],
                    tuple(sorted((x, str(v)) for x, v in c['mechanism_flags'][RHOS.index(rho)].items())),
                ))
            for treatment in ('full_D', 'center_D_sensitivity'):
                for rrow in c[treatment]['per_R']:
                    row['R'].append((
                        treatment,
                        rrow['R'],
                        tuple((
                            float(q['rho']),
                            tuple(q['possible_indices']),
                            bool(q['strict_unique_max']),
                        ) for q in rrow['rho']),
                    ))
            projection.append(row)
    return projection


def validate_assembled(obj, roots, cls, tag):
    errors = []
    checks = [
        (obj.get('gate') == GATE, 'gate'),
        (obj.get('preregistration_commit') == PREREG, 'prereg'),
        (obj.get('repair_preregistrations') == REPAIRS, 'repairs'),
        (obj.get('threshold_exact') == '1/20', 'threshold_exact'),
        (obj.get('robust_floor_exact') == '1', 'robust_floor_exact'),
        (obj.get('scientific_decision_transport') == TRANSPORT, 'transport'),
        (obj.get('fixed_channel_competition_semantics') == 'drift_only_exact_producer_booleans', 'fixed_semantics'),
        (obj.get('center_D_is_control_only') is True, 'center_D_control_only'),
        (obj.get('classification') == cls, 'classification'),
        (obj.get('root_location_count') == 9 and obj.get('case_count') == 36, 'case_counts'),
        (obj.get('errors') in ([], None), 'producer_errors'),
    ]
    for ok, name in checks:
        if not ok:
            errors.append(tag + ':' + name)
    got = {(c.get('root_box'), c.get('location'), c.get('amp_q')) for c in obj.get('cases', [])}
    expected = {
        (k, c['location'], c['amp_q'])
        for k in ROOTS
        for c in roots[k]['cases']
    }
    if got != expected:
        errors.append(tag + ':case_identity_set')
    return errors


def validate_aggregate(obj, cls):
    errors = []
    checks = [
        (obj.get('classification') == cls, 'aggregate:classification'),
        (obj.get('errors') in ([], None), 'aggregate:errors'),
        (obj.get('threshold_exact') == '1/20', 'aggregate:threshold_exact'),
        (obj.get('robust_floor_exact') == '1', 'aggregate:robust_floor_exact'),
        (obj.get('scientific_decision_transport') == TRANSPORT, 'aggregate:transport'),
        (obj.get('fixed_channel_competition_semantics') == 'drift_only_exact_producer_booleans', 'aggregate:fixed_semantics'),
        (obj.get('exact_discrete_projection_identical') is True, 'aggregate:cross_environment_projection'),
        (obj.get('root_location_count') == 9 and obj.get('case_count') == 36, 'aggregate:case_counts'),
    ]
    for ok, name in checks:
        if not ok:
            errors.append(name)
    return errors


def negative_controls(base_roots, base_assembled, base_aggregate):
    tests = {}

    def reject_root(name, mutate):
        roots = copy.deepcopy(base_roots)
        mutate(roots)
        errors = []
        for k in ROOTS:
            if k not in roots:
                errors.append('missing_root:' + str(k))
            else:
                errors += [f'{k}:{e}' for e in validate_root(roots[k], k)]
        tests[name] = bool(errors)

    def reject_assembled(name, mutate):
        roots = copy.deepcopy(base_roots)
        assembled = copy.deepcopy(base_assembled)
        mutate(assembled)
        cls = classify(roots)
        tests[name] = bool(validate_assembled(assembled, roots, cls, 'negative'))

    reject_root(
        'threshold_comparison_after_arb_to_float_conversion',
        lambda x: x[13]['cases'][0]['full_D']['per_rho'][0].__setitem__('decision_arithmetic', 'binary64_threshold_after_serialization'),
    )
    reject_root(
        'floor_comparison_from_serialized_float',
        lambda x: x[13]['cases'][0]['center_D_sensitivity']['per_rho'][0].__setitem__('decision_arithmetic', 'binary64_floor_after_serialization'),
    )
    reject_root(
        'fixed_channel_maximum_used_as_threshold_authority',
        lambda x: x[13]['cases'][0]['full_D']['fixed_channel'][0].__setitem__('decision_arithmetic', 'binary64_max_fixed_channel_threshold_authority'),
    )

    def missing_exact_bool(x):
        del x[13]['cases'][0]['full_D']['per_rho'][0]['drift_within_tolerance']
    reject_root('missing_exact_decision_boolean', missing_exact_bool)

    reject_root(
        'inconsistent_all_within_vs_violating_channel_list',
        lambda x: x[13]['cases'][0]['full_D']['fixed_channel'][0].__setitem__(
            'all_candidate_fixed_channel_drifts_within_tolerance',
            not x[13]['cases'][0]['full_D']['fixed_channel'][0]['all_candidate_fixed_channel_drifts_within_tolerance'],
        ),
    )
    reject_root('omitted_channel', lambda x: x[13].__setitem__('full_channel_count', 242))

    def incomplete_candidate_mislabeled(x):
        rr = x[13]['cases'][0]['full_D']['fixed_channel'][0]
        rr['ineligible_candidates'] = [rr['candidate_union'][0]]
        rr['competition_test_complete'] = True
    reject_root('candidate_set_incompleteness_mislabeled_complete', incomplete_candidate_mislabeled)

    reject_root('channel_pruning', lambda x: x[13].__setitem__('channel_pruning_used', True))
    reject_assembled('changed_threshold', lambda a: a.__setitem__('threshold_exact', '1/19'))
    reject_assembled('changed_floor', lambda a: a.__setitem__('robust_floor_exact', '2'))

    def changed_cohort(x):
        x[13]['cases'][0]['full_D']['per_R'][0]['R'] = 7
    reject_root('changed_root_rho_R_cohort', changed_cohort)

    reject_root(
        'changed_exact_LOW_MID_HIGH_amplitude',
        lambda x: x[13]['cases'][0].__setitem__('amp_q', '1/2'),
    )
    reject_root(
        'center_D_treated_as_rigorous_enclosure',
        lambda x: x[13].__setitem__('center_D_derivative_treatment', 'rigorous_replacement_enclosure'),
    )

    def delete_case(x):
        x[13]['cases'].pop()
    reject_root('result_dependent_case_deletion', delete_case)

    # Additional provenance/identity controls beyond the mandatory fourteen.
    reject_root('wrong_derivative_representation', lambda x: x[13].__setitem__('derivative_channel_representation', 'raw_CD'))
    reject_root('wrong_path_sign', lambda x: x[13].__setitem__('sign', -1))
    reject_root('wrong_repair_authority', lambda x: x[13].__setitem__('repair_preregistrations', REPAIRS[:-1]))

    aggregate = copy.deepcopy(base_aggregate)
    aggregate['exact_discrete_projection_identical'] = False
    tests['aggregate_cross_environment_disagreement'] = bool(validate_aggregate(aggregate, base_assembled['classification']))

    return tests


def synthetic_root(k):
    pts = expected_points(k)
    cases = []
    for loc in LOCS:
        per_rho = []
        fixed = []
        per_R = []
        for rho in RHOS:
            per_rho.append({
                'rho': rho,
                'S_lower': 2.0,
                'S_upper': 2.0,
                'E_lower': 2.0,
                'E_upper': 2.0,
                'drift_upper': 0.0,
                'slope_floor_satisfied': True,
                'drift_within_tolerance': True,
                'within_tolerance': True,
                'decision_arithmetic': ROW_ARITH,
            })
            fixed.append({
                'rho': rho,
                'candidate_union': [0],
                'candidate_count': 1,
                'eligible_count': 1,
                'ineligible_candidates': [],
                'competition_test_complete': True,
                'all_candidate_fixed_channel_drifts_within_tolerance': True,
                'violating_channel_indices': [],
                'max_fixed_channel_drift_upper': 0.0,
                'max_fixed_channel_witness': {'channel': 0, 'drift_upper': 0.0, 'S_lower': 2.0, 'drift_within_tolerance': True},
                'decision_arithmetic': FIXED_ARITH,
            })
        for R in RGRID:
            per_R.append({
                'R': R,
                'rho': [
                    {
                        'rho': rho,
                        'envelope_lower': 1.0,
                        'envelope_upper': 1.0,
                        'possible_count': 1,
                        'possible_indices': [0],
                        'best_lower_index': 0,
                        'dominance_gap_lower': 1.0,
                        'strict_unique_max': True,
                    }
                    for rho in RHOS
                ],
            })
        treatment = {'per_rho': copy.deepcopy(per_rho), 'fixed_channel': copy.deepcopy(fixed), 'per_R': copy.deepcopy(per_R)}
        cases.append({
            'location': loc,
            'amp_q': str(pts[loc].numerator) + '/' + str(pts[loc].denominator),
            'delta_q': str((pts[loc] - pts['MID']).numerator) + '/' + str((pts[loc] - pts['MID']).denominator),
            'full_D': copy.deepcopy(treatment),
            'center_D_sensitivity': copy.deepcopy(treatment),
            'mechanism_flags': [
                {
                    'rho': rho,
                    'full_D_within_tolerance': True,
                    'derivative_radius_sensitivity': False,
                    'competition_necessary_full_D': False,
                    'competition_necessary_center_D': False,
                    'fixed_channel_nonstationarity_center_D': False,
                    'decision_arithmetic': 'producer_exact_arb_booleans',
                }
                for rho in RHOS
            ],
        })
    return {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'repair_preregistrations': list(REPAIRS),
        'root_box': k,
        'causal': '0to5',
        'block': 0,
        'path': 2,
        'direction': [1, 1, 1, -1, -1, -1],
        'sign': 1,
        'precision_bits': 384,
        'full_channel_count': 243,
        'channel_pruning_used': False,
        'root_model_build_count': 1,
        'derivative_recomputed_at_points': False,
        'derivative_channel_representation': 'ad.as_c(z).d',
        'full_D_derivative_treatment': 'unchanged_full_root_acb_derivative_ball',
        'center_D_derivative_treatment': 'deterministic_midpoint_of_same_full_root_acb_derivative_ball',
        'scientific_decision_transport': TRANSPORT,
        'root_controls': {'synthetic_control': True},
        'min_beta_lower': 1.0,
        'cases': cases,
        'claim_ceiling': 'synthetic methodology self-test only; center-D is control-only sensitivity',
    }


def synthetic_assembled(roots):
    cls = classify(roots)
    cases = cases_from_roots(roots)
    return {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'repair_preregistrations': list(REPAIRS),
        'classification': cls,
        'errors': [],
        'root_location_count': 9,
        'case_count': 36,
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'scientific_decision_transport': TRANSPORT,
        'fixed_channel_competition_semantics': 'drift_only_exact_producer_booleans',
        'center_D_is_control_only': True,
        'cases': cases,
    }


def synthetic_aggregate(cls):
    return {
        'classification': cls,
        'errors': [],
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'scientific_decision_transport': TRANSPORT,
        'fixed_channel_competition_semantics': 'drift_only_exact_producer_booleans',
        'exact_discrete_projection_identical': True,
        'root_location_count': 9,
        'case_count': 36,
    }


def run_self_test():
    roots = {k: synthetic_root(k) for k in ROOTS}
    base_errors = []
    for k in ROOTS:
        base_errors += [f'{k}:{e}' for e in validate_root(roots[k], k)]
    assembled = synthetic_assembled(roots)
    cls = assembled['classification']
    base_errors += validate_assembled(assembled, roots, cls, 'selftest_assembled')
    aggregate = synthetic_aggregate(cls)
    base_errors += validate_aggregate(aggregate, cls)
    controls = negative_controls(roots, assembled, aggregate)
    if base_errors or not all(controls.values()):
        print(json.dumps({'base_errors': base_errors, 'negative_controls': controls}, indent=2, sort_keys=True))
        return 2
    print(json.dumps({'base_errors': [], 'negative_controls': controls, 'status': 'PASS'}, indent=2, sort_keys=True))
    return 0


def main():
    ap = argparse.ArgumentParser()
    for lane in ('a', 'b'):
        for k in ROOTS:
            ap.add_argument(f'--{lane}-root{k}', required=True)
        ap.add_argument(f'--{lane}-assembled', required=True)
    ap.add_argument('--aggregate', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    roots_a = {}
    roots_b = {}
    hash_a = {}
    hash_b = {}
    errors = []

    for lane, roots, hashes in (('a', roots_a, hash_a), ('b', roots_b, hash_b)):
        for k in ROOTS:
            obj, h = load(getattr(args, f'{lane}_root{k}'))
            roots[k] = obj
            hashes[str(k)] = h
            errors += [f'{lane}:{k}:{e}' for e in validate_root(obj, k)]

    assembled_a, assembled_a_hash = load(args.a_assembled)
    assembled_b, assembled_b_hash = load(args.b_assembled)
    aggregate, aggregate_hash = load(args.aggregate)

    cls_a = classify(roots_a) if not [x for x in errors if x.startswith('a:')] else INVALID
    cls_b = classify(roots_b) if not [x for x in errors if x.startswith('b:')] else INVALID
    errors += validate_assembled(assembled_a, roots_a, cls_a, 'assembled_a')
    errors += validate_assembled(assembled_b, roots_b, cls_b, 'assembled_b')
    if cls_a != cls_b:
        errors.append('cross_environment_classification')

    cross = exact_projection(roots_a) == exact_projection(roots_b)
    if not cross:
        errors.append('cross_environment_exact_projection')

    errors += validate_aggregate(aggregate, cls_a)
    if aggregate.get('classification') != cls_b:
        errors.append('aggregate_vs_lane_b_classification')

    controls = negative_controls(roots_a, assembled_a, aggregate)
    if not all(controls.values()):
        errors.append('negative_control_failure')

    cls = cls_a if not errors and cls_a != INVALID else INVALID
    out = {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'repair_preregistrations': REPAIRS,
        'classification': cls,
        'critic_errors': errors,
        'cross_environment_exact_decision_agreement': cross,
        'lane_a_root_sha256': hash_a,
        'lane_b_root_sha256': hash_b,
        'lane_a_assembled_sha256': assembled_a_hash,
        'lane_b_assembled_sha256': assembled_b_hash,
        'aggregate_sha256': aggregate_hash,
        'negative_controls': controls,
        'scientific_decision_transport': TRANSPORT,
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'claim_ceiling': 'Independent exact-decision Iter504S verification only; no full-domain theorem',
    }
    payload = json.dumps(out, sort_keys=True, separators=(',', ':')).encode()
    out['critic_payload_sha256'] = hashlib.sha256(payload).hexdigest()
    p = Path(args.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps(out, indent=2, sort_keys=True))
    return 2 if cls == INVALID else 0


if __name__ == '__main__':
    if '--self-test' in sys.argv:
        raise SystemExit(run_self_test())
    raise SystemExit(main())
