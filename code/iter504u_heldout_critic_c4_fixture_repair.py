#!/usr/bin/env python3
from __future__ import annotations

import copy
import sys
from fractions import Fraction

import iter504u_heldout_critic as base

REPAIR_PREREG = '5ad9664e88e517cd64bd9971bac5c4c239ba4672'
FROZEN_PARENT_CRITIC_BLOB = 'c2a7ea31ddc151bf02a3995d761cae95bdabd0db'


def force_c4_contradiction(cases):
    leaf = cases['H0_AMP_LOW']['leaves'][0]
    rows = leaf['per_rho']
    if not rows:
        raise ValueError('C4 fixture requires at least one rho row')
    for row in rows:
        row['slope_floor_satisfied'] = True
        row['drift_within_tolerance'] = True
        row['certified'] = True
    rows[0]['drift_within_tolerance'] = False
    rows[0]['certified'] = False
    leaf['certified'] = True


def negative_controls(base_cases):
    tests = {}

    def reject(name, mut):
        x = copy.deepcopy(base_cases)
        mut(x)
        tests[name] = bool(base.validate_all(x))

    reject('wrong_case_identity', lambda x: x['H0_AMP_LOW'].__setitem__('causal', '1to4'))
    reject('development_box_inserted', lambda x: x['H0_AMP_LOW'].__setitem__('box', 13))
    reject('missing_heldout_case', lambda x: x.pop('H5_SIGN'))
    reject('changed_threshold', lambda x: x['H0_AMP_LOW'].__setitem__('threshold_exact', '1/19'))
    reject('changed_floor', lambda x: x['H0_AMP_LOW'].__setitem__('robust_floor_exact', '0.9'))
    reject('changed_depth', lambda x: x['H0_AMP_LOW'].__setitem__('max_depth', 4))
    reject('channel_pruning', lambda x: x['H0_AMP_LOW'].__setitem__('full_channel_count', 242))
    reject('wrong_R_cohort', lambda x: x['H0_AMP_LOW'].__setitem__('r_cohort_consumed', [7, 8, 10, 12]))
    reject('wrong_rho_cohort', lambda x: x['H0_AMP_LOW'].__setitem__('rho_cohort_consumed', [0.36, 0.9, 1.6, 2.7]))
    reject('root_derivative_reuse', lambda x: x['H0_AMP_LOW'].__setitem__('local_derivative_recomputed_each_visited_node', False))
    reject('float_decision_transport', lambda x: x['H0_AMP_LOW']['leaves'][0].__setitem__('scientific_decision_transport', 'float_threshold'))
    reject(
        'non_dyadic_partition',
        lambda x: x['H0_AMP_LOW']['leaves'][0].__setitem__(
            'amp_upper_q',
            str(Fraction(x['H0_AMP_LOW']['leaves'][0]['amp_upper_q']) + Fraction(1, 10**12)),
        ),
    )
    reject('C4_true_leaf_false_rho', force_c4_contradiction)
    reject('leaf_binding_tag_removed', lambda x: x['H0_AMP_LOW']['leaves'][0].__setitem__('leaf_certification_binding', 'unbound'))
    return tests


def self_test_fixture():
    def carrier(certified, row0):
        rows = []
        for i in range(4):
            value = row0 if i == 0 else certified
            rows.append({
                'rho': base.RHOS[i],
                'slope_floor_satisfied': bool(value),
                'drift_within_tolerance': bool(value),
                'certified': bool(value),
            })
        return {'H0_AMP_LOW': {'leaves': [{'certified': bool(certified), 'per_rho': rows}]}}

    for initial_leaf in (False, True):
        for initial_row0 in (False, True):
            x = carrier(initial_leaf, initial_row0)
            force_c4_contradiction(x)
            leaf = x['H0_AMP_LOW']['leaves'][0]
            rows = leaf['per_rho']
            assert leaf['certified'] is True
            assert rows[0]['certified'] is False
            assert rows[0]['drift_within_tolerance'] is False
            assert all(r['certified'] is bool(r['slope_floor_satisfied'] and r['drift_within_tolerance']) for r in rows)
            assert all(r['certified'] is True for r in rows) is False
            assert leaf['certified'] is not all(r['certified'] is True for r in rows)
    print('ITER504U_C4_FIXTURE_SELF_TEST_PASS')
    return 0


def main():
    if sys.argv[1:] == ['--self-test']:
        return self_test_fixture()
    base.negative_controls = negative_controls
    return base.main()


if __name__ == '__main__':
    raise SystemExit(main())
