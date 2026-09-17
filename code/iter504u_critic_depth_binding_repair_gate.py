#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction

import iter504u_heldout_critic as base
import iter504u_heldout_critic_c4_fixture_repair as c4
import iter504u_critic_c4_fixture_repair_gate as carrier
import iter504u_heldout_critic_depth_binding_repair as repair

GATE = 'ITER504U_CRITIC_SHALLOW_UNRESOLVED_DEPTH_BINDING_REPAIR_GATE'
PREREG = 'a2dc229c849f5b15668e984b5947eb45386757f3'
PASS = 'ITER504U_CRITIC_SHALLOW_UNRESOLVED_DEPTH_BINDING_REPAIR_VALIDATED_SCOPED'
FAIL = 'ITER504U_CRITIC_SHALLOW_UNRESOLVED_DEPTH_BINDING_REPAIR_FAIL_SCOPED'


def sha_json(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def qstr(q: Fraction) -> str:
    return f'{q.numerator}/{q.denominator}'


def coherent_depth3_unresolved_case(case_id: str):
    case = carrier.coherent_case(case_id)
    lo, hi = base.box_interval(case['box'])
    width = (hi - lo) / 8
    template = case['leaves'][0]
    leaves = []
    for i in range(8):
        a = lo + i * width
        b = a + width
        leaf = copy.deepcopy(template)
        leaf['depth'] = base.MAX_DEPTH
        leaf['amp_lower_q'] = qstr(a)
        leaf['amp_upper_q'] = qstr(b)
        leaf['local_mid_q'] = qstr((a + b) / 2)
        if i == 0:
            for row in leaf['per_rho']:
                row['slope_floor_satisfied'] = True
                row['drift_within_tolerance'] = True
                row['certified'] = True
            leaf['per_rho'][0]['slope_floor_satisfied'] = False
            leaf['per_rho'][0]['drift_within_tolerance'] = False
            leaf['per_rho'][0]['certified'] = False
            leaf['certified'] = False
        leaves.append(leaf)

    inclusion_rows = [
        {'R': R, 'rho': rho, 'componentwise_inclusion': [True] * 243}
        for R in base.RGRID
        for rho in base.RHOS
    ]
    inclusion = {
        'depth': 1,
        'amp_lower_q': qstr(lo),
        'amp_upper_q': qstr(hi),
        'parent_depth': 0,
        'parent_amp_lower_q': qstr(lo),
        'parent_amp_upper_q': qstr(hi),
        'haar_log_inclusion_by_R': {str(R): True for R in base.RGRID},
        'channel_inclusion_rows': inclusion_rows,
        'all_componentwise_parent_inclusion': True,
    }
    case['leaves'] = leaves
    case['visited_node_count'] = 15
    case['terminal_leaf_count'] = 8
    case['unresolved_leaf_count'] = 1
    case['componentwise_parent_inclusion_record_count'] = 14
    case['componentwise_parent_inclusion_records'] = [copy.deepcopy(inclusion) for _ in range(14)]
    case['cover_valid'] = True
    return case


def main():
    controls = {}
    errors = []

    baseline = carrier.coherent_cases()
    baseline_pre_errors = base.validate_all(baseline)
    controls['coherent_baseline_accepted_pre_repair'] = baseline_pre_errors == []

    shallow = copy.deepcopy(baseline)
    repair.force_shallow_unresolved(shallow)
    shallow_pre_errors = base.validate_all(shallow)
    controls['pre_repair_validator_accepts_shallow_counterexample'] = shallow_pre_errors == []

    depth3 = carrier.coherent_cases()
    depth3['H0_AMP_LOW'] = coherent_depth3_unresolved_case('H0_AMP_LOW')
    depth3_pre_errors = base.validate_all(depth3)
    controls['depth3_unresolved_fixture_structurally_valid_pre_repair'] = depth3_pre_errors == []

    repair.install()

    baseline_post_errors = base.validate_all(baseline)
    controls['coherent_baseline_accepted_repaired'] = baseline_post_errors == []

    shallow_post_errors = base.validate_all(shallow)
    controls['shallow_counterexample_rejected_exact_binding'] = shallow_post_errors == [
        'H0_AMP_LOW:premature_unresolved_leaf_depth'
    ]

    depth3_post_errors = base.validate_all(depth3)
    controls['depth3_unresolved_terminal_leaf_accepted_repaired'] = depth3_post_errors == []

    c4_case = copy.deepcopy(baseline)
    c4.force_c4_contradiction(c4_case)
    c4_errors = base.validate_all(c4_case)
    controls['c4_regression_rejected_exact_binding'] = c4_errors == ['H0_AMP_LOW:C4_leaf_binding']

    c4_negative_controls = c4.negative_controls(baseline)
    controls['validated_c4_negative_control_suite_preserved'] = bool(c4_negative_controls) and all(c4_negative_controls.values())

    successor_negative_controls = repair.negative_controls(baseline)
    controls['successor_negative_control_suite_passes'] = bool(successor_negative_controls) and all(successor_negative_controls.values())
    controls['successor_contains_depth_binding_control'] = successor_negative_controls.get('premature_unresolved_leaf_depth') is True

    controls.update({
        'repair_prereg_frozen': repair.REPAIR_PREREG == PREREG,
        'original_critic_blob_frozen': repair.FROZEN_PARENT_CRITIC_BLOB == 'c2a7ea31ddc151bf02a3995d761cae95bdabd0db',
        'c4_wrapper_blob_frozen': repair.FROZEN_C4_WRAPPER_BLOB == 'bcea2946a0f9676b50897dc4bbe74fa1122a9965',
        'production_gate_unchanged': base.GATE == 'ITER504U_HELDOUT_LOCAL_D_GENERALIZATION_FIREWALL',
        'production_prereg_unchanged': base.PREREG == '05b8e9354c9a7805f0fce18b904346a986a0787f',
        'max_depth_unchanged': base.MAX_DEPTH == 3,
    })

    if not all(controls.values()):
        errors.append('formal_control_failure')
    classification = PASS if not errors else FAIL
    result = {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'classification': classification,
        'errors': errors,
        'controls': controls,
        'baseline_pre_validation_errors': baseline_pre_errors,
        'shallow_pre_validation_errors': shallow_pre_errors,
        'depth3_pre_validation_errors': depth3_pre_errors,
        'baseline_repaired_validation_errors': baseline_post_errors,
        'shallow_repaired_validation_errors': shallow_post_errors,
        'depth3_repaired_validation_errors': depth3_post_errors,
        'c4_regression_validation_errors': c4_errors,
        'c4_negative_controls': c4_negative_controls,
        'successor_negative_controls': successor_negative_controls,
        'production_science_consumed': False,
        'source_run_classified': False,
        'claim_ceiling': 'Independent Critic depth-binding methodology only; no Iter504U science classification',
    }
    result['payload_sha256'] = sha_json(result)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if classification == PASS else 2


if __name__ == '__main__':
    raise SystemExit(main())
