#!/usr/bin/env python3
from __future__ import annotations

import copy
from fractions import Fraction

import iter504u_heldout_critic as base
import iter504u_heldout_critic_c4_fixture_repair as c4

REPAIR_PREREG = 'a2dc229c849f5b15668e984b5947eb45386757f3'
FROZEN_PARENT_CRITIC_BLOB = 'c2a7ea31ddc151bf02a3995d761cae95bdabd0db'
FROZEN_C4_WRAPPER_BLOB = 'bcea2946a0f9676b50897dc4bbe74fa1122a9965'
ORIGINAL_VALIDATE_CASE = base.validate_case


def _qstr(q: Fraction) -> str:
    return f'{q.numerator}/{q.denominator}'


def validate_case(o, cid):
    errors = list(ORIGINAL_VALIDATE_CASE(o, cid))
    for leaf in o.get('leaves', []):
        if leaf.get('certified') is False:
            try:
                depth = int(leaf.get('depth', -1))
            except Exception:
                continue
            if depth != base.MAX_DEPTH:
                errors.append('premature_unresolved_leaf_depth')
    return errors


def force_shallow_unresolved(cases):
    case = cases['H0_AMP_LOW']
    leaves = case.get('leaves', [])
    if not leaves:
        raise ValueError('shallow-unresolved fixture requires at least one leaf')
    leaf = copy.deepcopy(leaves[0])
    rows = leaf.get('per_rho', [])
    if len(rows) != len(base.RHOS):
        raise ValueError('shallow-unresolved fixture requires frozen rho rows')

    lo, hi = base.box_interval(case['box'])
    mid = (lo + hi) / 2
    leaf['depth'] = 0
    leaf['amp_lower_q'] = _qstr(lo)
    leaf['amp_upper_q'] = _qstr(hi)
    leaf['local_mid_q'] = _qstr(mid)
    for row in rows:
        row['slope_floor_satisfied'] = True
        row['drift_within_tolerance'] = True
        row['certified'] = True
    rows[0]['slope_floor_satisfied'] = False
    rows[0]['drift_within_tolerance'] = False
    rows[0]['certified'] = False
    leaf['certified'] = False

    case['leaves'] = [leaf]
    case['visited_node_count'] = 1
    case['terminal_leaf_count'] = 1
    case['unresolved_leaf_count'] = 1
    case['componentwise_parent_inclusion_record_count'] = 0
    case['componentwise_parent_inclusion_records'] = []
    case['cover_valid'] = True


def negative_controls(base_cases):
    tests = dict(c4.negative_controls(base_cases))
    x = copy.deepcopy(base_cases)
    force_shallow_unresolved(x)
    tests['premature_unresolved_leaf_depth'] = bool(base.validate_all(x))
    return tests


def install():
    base.validate_case = validate_case
    base.negative_controls = negative_controls


def main():
    install()
    return base.main()


if __name__ == '__main__':
    raise SystemExit(main())
