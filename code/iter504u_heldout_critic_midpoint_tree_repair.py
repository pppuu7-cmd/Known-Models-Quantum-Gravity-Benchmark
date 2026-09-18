#!/usr/bin/env python3
from __future__ import annotations

import copy
from fractions import Fraction

import iter504u_heldout_critic as base
import iter504u_heldout_critic_depth_binding_repair as depth
from iter504u_midpoint_tree_binding import binding_errors

REPAIR_PREREG = '71403ec9a82106a7a2aa2d5bae37336ced25fcc5'
FROZEN_PARENT_CRITIC_BLOB = 'c2a7ea31ddc151bf02a3995d761cae95bdabd0db'
FROZEN_DEPTH_WRAPPER_BLOB = 'd10bb168e93b3e3b5496a4f40bb0f16a9bd59dd4'


def _first_case_with_inclusion(cases):
    for cid in base.EXPECTED:
        if cases[cid].get('componentwise_parent_inclusion_records'):
            return cases[cid]
    raise ValueError('fixture requires at least one parent-inclusion record')


def install():
    depth.install()
    prior_validate = base.validate_case
    prior_negative = base.negative_controls

    def validate_case(o, cid):
        errors = list(prior_validate(o, cid))
        errors += binding_errors(o)
        return errors

    base.validate_case = validate_case

    def negative_controls(base_cases):
        tests = dict(prior_negative(base_cases))

        x = copy.deepcopy(base_cases)
        leaf = x['H0_AMP_LOW']['leaves'][0]
        leaf['local_mid_q'] = str(Fraction(leaf['local_mid_q']) + Fraction(1, 10**12))
        tests['wrong_exact_local_midpoint'] = bool(base.validate_all(x))

        x = copy.deepcopy(base_cases)
        case = _first_case_with_inclusion(x)
        rec = case['componentwise_parent_inclusion_records'][0]
        rec['amp_lower_q'] = str(Fraction(rec['amp_lower_q']) + Fraction(1, 10**12))
        tests['wrong_parent_inclusion_child_interval'] = bool(base.validate_all(x))

        x = copy.deepcopy(base_cases)
        case = _first_case_with_inclusion(x)
        rec = case['componentwise_parent_inclusion_records'][0]
        rec['parent_amp_lower_q'] = str(Fraction(rec['parent_amp_lower_q']) + Fraction(1, 10**12))
        tests['wrong_parent_inclusion_parent_interval'] = bool(base.validate_all(x))

        return tests

    base.negative_controls = negative_controls


def main():
    install()
    return base.main()


if __name__ == '__main__':
    raise SystemExit(main())
