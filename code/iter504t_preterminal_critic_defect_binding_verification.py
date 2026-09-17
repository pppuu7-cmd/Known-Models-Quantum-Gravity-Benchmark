#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import subprocess
from fractions import Fraction
from pathlib import Path

GATE = 'ITER504T_PRETERMINAL_CRITIC_DEFECT_BINDING_VERIFICATION_GATE'
PASS = 'ITER504T_PRETERMINAL_CRITIC_DEFECT_CLAIMS_ALL_VERIFIED_SCOPED'
FAIL = 'ITER504T_PRETERMINAL_CRITIC_DEFECT_CLAIMS_NOT_ALL_VERIFIED_SCOPED'
BLOCKED = 'ITER504T_PRETERMINAL_CRITIC_DEFECT_BINDING_BLOCKED_SCOPED'
INVALID = 'INVALID_IMPLEMENTATION'


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'cannot load {path}')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def qtext(q: Fraction) -> str:
    return f'{q.numerator}/{q.denominator}'


def leaf(a: Fraction, b: Fraction, depth: int = 1):
    per_rho = [
        {
            'rho': rho,
            'slope_floor_satisfied': True,
            'drift_within_tolerance': True,
            'certified': True,
        }
        for rho in (0.35, 0.9, 1.6, 2.7)
    ]
    possible = [
        {'R': R, 'rho': rho, 'indices': [0]}
        for R in (6, 8, 10, 12)
        for rho in (0.35, 0.9, 1.6, 2.7)
    ]
    return {
        'depth': depth,
        'amp_lower_q': qtext(a),
        'amp_upper_q': qtext(b),
        'validated_local_derivative': True,
        'scientific_decision_transport': 'exact_arb_booleans_float_bounds_display_only',
        'certified': True,
        'per_rho': per_rho,
        'possible_max': possible,
    }


def base_payload():
    lo = Fraction(29, 12800)
    hi = Fraction(30, 12800)
    mid = (lo + hi) / 2
    return {
        'gate': 'ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION',
        'preregistration_commit': 'aa2b0256ce60d605574a18ec86c0bad5b5df1512',
        'root_box': 13,
        'precision_bits': 384,
        'python_flint': '0.9.0',
        'full_channel_count': 243,
        'channel_pruning_used': False,
        'max_depth': 3,
        'partition_rule': 'deterministic_dyadic_midpoint',
        'local_derivative_recomputed_each_visited_node': True,
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'cover_valid': True,
        'terminal_leaf_count': 2,
        'unresolved_leaf_count': 0,
        'leaves': [leaf(lo, mid), leaf(mid, hi)],
    }


def errors(mod, payload):
    return list(mod.validate(copy.deepcopy(payload), 13))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--authority', required=True)
    ap.add_argument('--repo-root', default='.')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    root = Path(a.repo_root)
    authority = json.loads(Path(a.authority).read_text())

    identities = {}
    identities_ok = True
    for rel, expected in authority['locked_files'].items():
        actual = subprocess.check_output(['git', 'hash-object', rel], cwd=root, text=True).strip()
        identities[rel] = {'expected': expected, 'actual': actual, 'match': actual == expected}
        identities_ok &= actual == expected

    blocked_reason = None
    try:
        assembler = load_module('iter504t_frozen_assembler', root / 'code/iter504t_local_derivative_assemble.py')
        critic = load_module('iter504t_frozen_critic', root / 'code/iter504t_local_derivative_critic.py')
    except Exception as exc:
        assembler = critic = None
        blocked_reason = repr(exc)

    claims = {}
    controls = {'blob_identity': identities_ok}

    if assembler is not None and critic is not None:
        base = base_payload()
        base_a = errors(assembler, base)
        base_c = errors(critic, base)
        controls['baseline_dyadic_payload_accepted_assembler'] = base_a == []
        controls['baseline_dyadic_payload_accepted_critic'] = base_c == []

        wrong_threshold = copy.deepcopy(base)
        wrong_threshold['threshold_exact'] = '1/19'
        wt_a = errors(assembler, wrong_threshold)
        wt_c = errors(critic, wrong_threshold)
        controls['wrong_threshold_rejected_assembler'] = 'threshold_exact' in wt_a
        controls['wrong_threshold_rejected_critic'] = 'threshold_exact' in wt_c

        wrong_root = copy.deepcopy(base)
        wrong_root['root_box'] = 99
        wr_a = errors(assembler, wrong_root)
        wr_c = errors(critic, wrong_root)
        controls['wrong_root_rejected_assembler'] = 'root_box' in wr_a
        controls['wrong_root_rejected_critic'] = 'root_box' in wr_c

        malformed = copy.deepcopy(base)
        malformed['leaves'][0]['amp_upper_q'] = 'not-a-rational'
        mf_a = errors(assembler, malformed)
        mf_c = errors(critic, malformed)
        controls['malformed_interval_rejected_assembler'] = bool(mf_a)
        controls['malformed_interval_rejected_critic'] = bool(mf_c)

        producer_text = (root / 'code/iter504t_local_derivative_contraction.py').read_text()
        assembler_text = (root / 'code/iter504t_local_derivative_assemble.py').read_text()
        critic_text = (root / 'code/iter504t_local_derivative_critic.py').read_text()
        c1_missing_record = 'componentwise_parent_inclusion' not in producer_text
        c1_assembler_accepts = base_a == [] and 'componentwise_parent_inclusion' not in assembler_text
        c1_critic_accepts = base_c == [] and 'componentwise_parent_inclusion' not in critic_text
        c1_verified = c1_missing_record and c1_assembler_accepts and c1_critic_accepts
        claims['FROZEN_COMPONENTWISE_PARENT_INCLUSION_CONTROL_NOT_IMPLEMENTED_OR_RECORDED'] = {
            'status': 'VERIFIED' if c1_verified else 'REFUTED',
            'producer_serializes_certificate': not c1_missing_record,
            'assembler_accepts_missing_certificate': c1_assembler_accepts,
            'critic_accepts_missing_certificate': c1_critic_accepts,
            'assembler_errors': base_a,
            'critic_errors': base_c,
        }

        nondyadic = copy.deepcopy(base)
        lo = Fraction(29, 12800)
        hi = Fraction(30, 12800)
        split = lo + (hi - lo) / 3
        nondyadic['leaves'][0]['amp_upper_q'] = qtext(split)
        nondyadic['leaves'][1]['amp_lower_q'] = qtext(split)
        nd_a = errors(assembler, nondyadic)
        nd_c = errors(critic, nondyadic)
        c2_verified = nd_a == [] and nd_c == []
        claims['FROZEN_DYADIC_SPLIT_LOCATION_NOT_INDEPENDENTLY_VERIFIED'] = {
            'status': 'VERIFIED' if c2_verified else 'REFUTED',
            'synthetic_split': qtext(split),
            'assembler_accepts_non_dyadic_split': nd_a == [],
            'critic_accepts_non_dyadic_split': nd_c == [],
            'assembler_errors': nd_a,
            'critic_errors': nd_c,
        }

        wrong_R = copy.deepcopy(base)
        for x in wrong_R['leaves']:
            for pm in x['possible_max']:
                if pm['R'] == 6:
                    pm['R'] = 7
        r_a = errors(assembler, wrong_R)
        r_c = errors(critic, wrong_R)
        projection_same_if_both_lanes_mutated = critic.projection({13: wrong_R, 14: wrong_R, 15: wrong_R}) == critic.projection({13: copy.deepcopy(wrong_R), 14: copy.deepcopy(wrong_R), 15: copy.deepcopy(wrong_R)})
        c3_verified = r_a == [] and r_c == [] and projection_same_if_both_lanes_mutated
        claims['FROZEN_R_COHORT_NOT_INDEPENDENTLY_VERIFIED'] = {
            'status': 'VERIFIED' if c3_verified else 'REFUTED',
            'assembler_accepts_changed_R': r_a == [],
            'critic_accepts_changed_R': r_c == [],
            'cross_environment_projection_same_if_both_lanes_changed': projection_same_if_both_lanes_mutated,
            'assembler_errors': r_a,
            'critic_errors': r_c,
        }

    controls_ok = all(controls.values())
    if not identities_ok or not controls_ok:
        classification = INVALID
    elif blocked_reason is not None:
        classification = BLOCKED
    else:
        all_verified = all(x['status'] == 'VERIFIED' for x in claims.values()) and len(claims) == 3
        classification = PASS if all_verified else FAIL

    decision = {
        'gate': GATE,
        'classification': classification,
        'claims': claims,
        'controls': controls,
        'locked_identities': identities,
        'blocked_reason': blocked_reason,
        'active_scientific_artifacts_consumed': False,
        'active_scientific_run_classified': False,
        'claim_ceiling': authority['claim_ceiling'],
    }
    canonical = json.dumps(decision, sort_keys=True, separators=(',', ':'))
    decision['decision_sha256'] = hashlib.sha256(canonical.encode()).hexdigest()
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(decision, indent=2, sort_keys=True) + '\n')
    print(json.dumps(decision, sort_keys=True))
    return 2 if classification == INVALID else 0


if __name__ == '__main__':
    raise SystemExit(main())
