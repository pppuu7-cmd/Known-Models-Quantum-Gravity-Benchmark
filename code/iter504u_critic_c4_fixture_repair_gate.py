#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import iter504u_heldout_critic as base
import iter504u_heldout_critic_c4_fixture_repair as repair

GATE = 'ITER504U_CRITIC_C4_FIXTURE_REPAIR_GATE'
PREREG = '662e1b40c4584a5b1989b821cd7a5c334ef8fc44'
PASS = 'ITER504U_CRITIC_C4_FIXTURE_REPAIR_VALIDATED_SCOPED'
FAIL = 'ITER504U_CRITIC_C4_FIXTURE_REPAIR_FAIL_SCOPED'
INVALID = 'INVALID_IMPLEMENTATION'


def sha_json(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def qstr(q: Fraction) -> str:
    return f'{q.numerator}/{q.denominator}'


def coherent_case(case_id: str):
    causal, block, path, box, direction, sign = base.EXPECTED[case_id]
    lo, hi = base.box_interval(box)
    mid = (lo + hi) / 2
    per_rho = [
        {
            'rho': rho,
            'slope_floor_satisfied': True,
            'drift_within_tolerance': True,
            'certified': True,
            'S_lower': 2.0,
            'S_upper': 2.1,
            'E_lower': 2.0,
            'E_upper': 2.1,
            'drift_upper': 0.01,
        }
        for rho in base.RHOS
    ]
    possible_max = [
        {'R': R, 'rho': rho, 'indices': [0]}
        for R in base.RGRID
        for rho in base.RHOS
    ]
    leaf = {
        'depth': 0,
        'amp_lower_q': qstr(lo),
        'amp_upper_q': qstr(hi),
        'local_mid_q': qstr(mid),
        'validated_local_derivative': True,
        'local_derivative_recomputed_here': True,
        'leaf_certification_binding': 'all_per_rho_exact',
        'scientific_decision_transport': 'exact_arb_booleans_float_bounds_display_only',
        'certified': True,
        'per_rho': per_rho,
        'possible_max': possible_max,
        'max_drift_upper': 0.01,
        'min_S_lower': 2.0,
    }
    return {
        'gate': base.GATE,
        'preregistration_commit': base.PREREG,
        'parent_critic_commit': base.PARENT_CRITIC,
        'exact_repair_head': base.EXACT_REPAIR_HEAD,
        'case_id': case_id,
        'causal': causal,
        'block': block,
        'path': path,
        'box': box,
        'direction': direction,
        'sign': sign,
        'parent_amp_lower_q': qstr(lo),
        'parent_amp_upper_q': qstr(hi),
        'precision_bits': 384,
        'python_flint': '0.9.0',
        'full_channel_count': 243,
        'channel_pruning_used': False,
        'max_depth': 3,
        'partition_rule': 'deterministic_dyadic_midpoint',
        'local_derivative_recomputed_each_visited_node': True,
        'leaf_certification_binding': 'all_per_rho_exact',
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'r_cohort_consumed': list(base.RGRID),
        'rho_cohort_consumed': list(base.RHOS),
        'componentwise_parent_inclusion_record_count': 0,
        'componentwise_parent_inclusion_records': [],
        'cover_valid': True,
        'visited_node_count': 1,
        'terminal_leaf_count': 1,
        'unresolved_leaf_count': 0,
        'leaves': [leaf],
        'claim_ceiling': 'synthetic methodology fixture only',
    }


def coherent_cases():
    return {cid: coherent_case(cid) for cid in base.EXPECTED}


def main():
    controls = {}
    errors = []

    baseline = coherent_cases()
    baseline_errors = base.validate_all(baseline)
    controls['coherent_noncontradictory_fixture_accepted'] = baseline_errors == []

    contradicted = copy.deepcopy(baseline)
    repair.force_c4_contradiction(contradicted)
    contradiction_errors = base.validate_all(contradicted)
    controls['contradictory_fixture_rejected_shared_validator'] = bool(contradiction_errors)
    controls['contradiction_hits_exact_c4_binding'] = contradiction_errors == ['H0_AMP_LOW:C4_leaf_binding']

    carrier_false = copy.deepcopy(baseline)
    leaf = carrier_false['H0_AMP_LOW']['leaves'][0]
    leaf['certified'] = False
    leaf['per_rho'][0]['slope_floor_satisfied'] = False
    leaf['per_rho'][0]['drift_within_tolerance'] = False
    leaf['per_rho'][0]['certified'] = False
    carrier_false['H0_AMP_LOW']['unresolved_leaf_count'] = 1
    # The baseline carrier may be scientifically unresolved; after deterministic repair it must still create only C4.
    repair.force_c4_contradiction(carrier_false)
    carrier_errors = base.validate_all(carrier_false)
    controls['outcome_independent_false_carrier_rejected_exact_c4'] = carrier_errors == ['H0_AMP_LOW:C4_leaf_binding']

    repaired_negative_controls = repair.negative_controls(baseline)
    controls['full_repaired_negative_control_suite_passes_on_coherent_fixture'] = bool(repaired_negative_controls) and all(repaired_negative_controls.values())

    frozen_identity_controls = {
        'original_critic_blob': repair.FROZEN_PARENT_CRITIC_BLOB == 'c2a7ea31ddc151bf02a3995d761cae95bdabd0db',
        'repair_prereg': repair.REPAIR_PREREG == '5ad9664e88e517cd64bd9971bac5c4c239ba4672',
        'production_gate_unchanged': base.GATE == 'ITER504U_HELDOUT_LOCAL_D_GENERALIZATION_FIREWALL',
        'production_prereg_unchanged': base.PREREG == '05b8e9354c9a7805f0fce18b904346a986a0787f',
    }
    controls.update(frozen_identity_controls)

    if not all(controls.values()):
        errors.append('formal_control_failure')
    classification = PASS if not errors else FAIL
    result = {
        'gate': GATE,
        'formal_preregistration_commit': PREREG,
        'classification': classification,
        'errors': errors,
        'controls': controls,
        'baseline_validation_errors': baseline_errors,
        'contradiction_validation_errors': contradiction_errors,
        'false_carrier_validation_errors': carrier_errors,
        'repaired_negative_controls': repaired_negative_controls,
        'production_science_consumed': False,
        'source_run_classified': False,
        'claim_ceiling': 'Critic C4 synthetic fixture repair only; no Iter504U science classification',
    }
    result['payload_sha256'] = sha_json(result)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if classification == PASS else 2


if __name__ == '__main__':
    raise SystemExit(main())
