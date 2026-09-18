#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

GATE = 'ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE'
PREREG = 'e42caf47f9201d79cd89b79dc72b90f696e3ec5d'
DESIGN_AUTHORITY = 'a4006f336a49f655534a2f76a443a3d60a47cd85'
DESIGN_STATIC_CRITIC = '722c7e09bf077c0cb29c3ac0ac2ed724b99290f4'
IMPLEMENTATION_AUTHORITY = '42a2f035a80c474ebc7e5f57934ad9ba78ce9937'
CANONICAL_SHA256 = '3cac282175830e795394dca5202f5368b27120817f2d4abd9eba54fc6c9f1e6f'
PASS = 'ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED'
INC = 'ITER504V_BROADER_DOMAIN_LOCAL_D_INCONCLUSIVE_SCOPED'
INVALID = 'ITER504V_BROADER_DOMAIN_INVALID'


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def sha_json(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--a', required=True)
    p.add_argument('--b', required=True)
    p.add_argument('--out', required=True)
    a = p.parse_args()

    A, Ah = load(a.a)
    B, Bh = load(a.b)
    errors = []
    for tag, obj in (('a', A), ('b', B)):
        exact = {
            'gate': GATE,
            'preregistration_commit': PREREG,
            'design_authority_commit': DESIGN_AUTHORITY,
            'design_static_critic_commit': DESIGN_STATIC_CRITIC,
            'implementation_authority_commit': IMPLEMENTATION_AUTHORITY,
            'canonical_768_record_sequence_sha256': CANONICAL_SHA256,
            'total_cases': 768,
            'threshold_exact': '1/20',
            'robust_floor_exact': '1',
            'max_depth': 3,
            'channels': 243,
            'r_cohort': [6, 8, 10, 12],
            'rho_cohort': [0.35, 0.9, 1.6, 2.7],
        }
        for k, v in exact.items():
            if obj.get(k) != v:
                errors.append(f'{tag}:{k}')
        if obj.get('errors'):
            errors.append(f'{tag}:assembly_errors')
        if obj.get('classification') not in (PASS, INC):
            errors.append(f'{tag}:classification')
        if len(obj.get('state_ids', [])) != 768 or len(set(obj.get('state_ids', []))) != 768:
            errors.append(f'{tag}:state_set')
        if len(obj.get('decision_projection_sha256_by_state', {})) != 768:
            errors.append(f'{tag}:projection_count')
        if len(obj.get('case_file_sha256', {})) != 768:
            errors.append(f'{tag}:case_provenance_count')

    class_agree = A.get('classification') == B.get('classification')
    state_agree = A.get('state_ids') == B.get('state_ids')
    projection_map_agree = (
        A.get('decision_projection_sha256_by_state')
        == B.get('decision_projection_sha256_by_state')
    )
    projection_sequence_agree = (
        A.get('decision_projection_sequence_sha256')
        == B.get('decision_projection_sequence_sha256')
        and A.get('decision_projection_sequence_sha256') is not None
    )
    unresolved_map_agree = (
        A.get('unresolved_leaf_count_by_state')
        == B.get('unresolved_leaf_count_by_state')
    )
    unresolved_total_agree = (
        A.get('total_unresolved_leaves') == B.get('total_unresolved_leaves')
    )
    counterexample_agree = (
        A.get('counterexample_state_ids') == B.get('counterexample_state_ids')
    )
    visited_agree = A.get('total_visited_nodes') == B.get('total_visited_nodes')
    terminal_leaf_agree = (
        A.get('total_terminal_leaves') == B.get('total_terminal_leaves')
    )

    checks = {
        'cross_environment_classification': class_agree,
        'cross_environment_state_identity': state_agree,
        'cross_environment_projection_map': projection_map_agree,
        'cross_environment_projection_sequence': projection_sequence_agree,
        'cross_environment_unresolved_map': unresolved_map_agree,
        'cross_environment_unresolved_total': unresolved_total_agree,
        'cross_environment_counterexample_set': counterexample_agree,
        'cross_environment_visited_count': visited_agree,
        'cross_environment_terminal_leaf_count': terminal_leaf_agree,
    }
    for name, ok in checks.items():
        if not ok:
            errors.append(name)

    classification = A.get('classification') if not errors else INVALID
    out = {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'design_authority_commit': DESIGN_AUTHORITY,
        'design_static_critic_commit': DESIGN_STATIC_CRITIC,
        'implementation_authority_commit': IMPLEMENTATION_AUTHORITY,
        'canonical_768_record_sequence_sha256': CANONICAL_SHA256,
        'classification': classification,
        'errors': errors,
        'cross_environment_exact_decision_agreement': bool(
            not errors
            and class_agree
            and state_agree
            and projection_map_agree
            and projection_sequence_agree
            and unresolved_map_agree
            and unresolved_total_agree
            and counterexample_agree
            and visited_agree
            and terminal_leaf_agree
        ),
        'lane_3_11_sha256': Ah,
        'lane_3_13_sha256': Bh,
        'decision_projection_sequence_sha256': (
            A.get('decision_projection_sequence_sha256') if not errors else None
        ),
        'decision_projection_sha256_by_state': (
            A.get('decision_projection_sha256_by_state') if not errors else None
        ),
        'total_cases': 768 if not errors else None,
        'total_visited_nodes': A.get('total_visited_nodes') if not errors else None,
        'total_terminal_leaves': A.get('total_terminal_leaves') if not errors else None,
        'total_unresolved_leaves': A.get('total_unresolved_leaves') if not errors else None,
        'counterexample_state_ids': A.get('counterexample_state_ids') if not errors else None,
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'max_depth': 3,
        'channels': 243,
        'r_cohort': [6, 8, 10, 12],
        'rho_cohort': [0.35, 0.9, 1.6, 2.7],
        'claim_ceiling': 'Complete frozen 768-record q=1 certificate domain only; no model-level physics claim',
    }
    payload = dict(out)
    out['aggregate_payload_sha256'] = sha_json(payload)
    q = Path(a.out)
    q.parent.mkdir(parents=True, exist_ok=True)
    q.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({
        'classification': classification,
        'errors': errors,
        'cross_environment_exact_decision_agreement': out['cross_environment_exact_decision_agreement'],
        'artifact_written': True,
    }, sort_keys=True))
    return 2 if classification == INVALID else 0


if __name__ == '__main__':
    raise SystemExit(main())
