#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

GATE = 'ITER504U_HELDOUT_LOCAL_D_GENERALIZATION_FIREWALL'
PREREG = '05b8e9354c9a7805f0fce18b904346a986a0787f'
PASS = 'ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED'
INC = 'ITER504U_HELDOUT_LOCAL_D_INCONCLUSIVE_SCOPED'
INVALID = 'ITER504U_INVALID'
EXPECTED_CASES = ['H0_AMP_LOW', 'H1_AMP_MID', 'H2_CAUSAL_1', 'H3_CAUSAL_2', 'H4_DIRECTION', 'H5_SIGN']


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def sha_json(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


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
        if obj.get('gate') != GATE:
            errors.append(f'{tag}:gate')
        if obj.get('preregistration_commit') != PREREG:
            errors.append(f'{tag}:prereg')
        if obj.get('errors'):
            errors.append(f'{tag}:assembly_errors')
        if obj.get('classification') not in (PASS, INC):
            errors.append(f'{tag}:classification')
        if obj.get('case_ids') != EXPECTED_CASES or obj.get('total_cases') != 6:
            errors.append(f'{tag}:case_set')
        if obj.get('threshold_exact') != '1/20' or obj.get('robust_floor_exact') != '1' or obj.get('max_depth') != 3 or obj.get('channels') != 243:
            errors.append(f'{tag}:science_constants')
    class_agree = A.get('classification') == B.get('classification')
    projection_agree = A.get('decision_projection_sha256') == B.get('decision_projection_sha256') and A.get('decision_projection') == B.get('decision_projection')
    unresolved_agree = A.get('total_unresolved_leaves') == B.get('total_unresolved_leaves')
    if not class_agree:
        errors.append('cross_environment_classification')
    if not projection_agree:
        errors.append('cross_environment_exact_projection')
    if not unresolved_agree:
        errors.append('cross_environment_unresolved_count')
    classification = A.get('classification') if not errors else INVALID
    out = {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'classification': classification,
        'errors': errors,
        'cross_environment_exact_decision_agreement': bool(projection_agree and class_agree and unresolved_agree),
        'lane_a_sha256': Ah,
        'lane_b_sha256': Bh,
        'lane_a_projection_sha256': A.get('decision_projection_sha256'),
        'lane_b_projection_sha256': B.get('decision_projection_sha256'),
        'total_cases': A.get('total_cases') if not errors else None,
        'total_visited_nodes': A.get('total_visited_nodes') if not errors else None,
        'total_terminal_leaves': A.get('total_terminal_leaves') if not errors else None,
        'total_unresolved_leaves': A.get('total_unresolved_leaves') if not errors else None,
        'case_ids': EXPECTED_CASES,
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'max_depth': 3,
        'channels': 243,
        'claim_ceiling': 'Cross-environment six-case Iter504U held-out aggregate only',
    }
    payload = dict(out)
    out['aggregate_payload_sha256'] = sha_json(payload)
    q = Path(a.out)
    q.parent.mkdir(parents=True, exist_ok=True)
    q.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps(out, indent=2, sort_keys=True))
    return 2 if classification == INVALID else 0


if __name__ == '__main__':
    raise SystemExit(main())
