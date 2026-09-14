#!/usr/bin/env python3
"""Aggregate the prospectively frozen Iter503V endpoint-contract verifier."""
import argparse
import glob
import json
import os

EXPECTED = {0, 7, 15}


def load(root):
    out = []
    for p in glob.glob(os.path.join(root, '**', 'iter503v-box*.json'), recursive=True):
        with open(p) as f:
            x = json.load(f)
        x['_artifact_path'] = p
        out.append(x)
    return out


def aggregate(root):
    rows = load(root)
    boxes = {int(x['box']) for x in rows if 'box' in x}
    unique = len(rows) == len(boxes)
    complete_artifacts = unique and boxes == EXPECTED
    classifications = [x.get('classification') for x in rows]
    total = sum(int(x.get('completed_checks', 0)) for x in rows)
    lane_complete = bool(complete_artifacts and all(bool(x.get('complete')) for x in rows))

    if not lane_complete or total != 288:
        cls = 'ITER503V_INVALID_OR_BLOCKED'
    elif any(c == 'ITER503V_ENDPOINT_CONTRACT_VIOLATION' for c in classifications):
        cls = 'ITER503V_ENDPOINT_CONTRACT_VIOLATION'
    elif all(c == 'ITER503V_ENDPOINT_CONTRACT_CONFIRMED' for c in classifications):
        cls = 'ITER503V_ENDPOINT_CONTRACT_CONFIRMED'
    else:
        cls = 'ITER503V_INVALID_OR_BLOCKED'

    return {
        'iteration': '503V',
        'classification': cls,
        'expected_boxes': sorted(EXPECTED),
        'observed_boxes': sorted(boxes),
        'artifact_count': len(rows),
        'completed_checks': total,
        'expected_checks': 288,
        'all_288_contained': bool(cls == 'ITER503V_ENDPOINT_CONTRACT_CONFIRMED'),
        'lanes': [
            {
                'box': x.get('box'),
                'classification': x.get('classification'),
                'complete': x.get('complete'),
                'completed_checks': x.get('completed_checks', 0),
                'all_contained': x.get('all_contained'),
                'artifact_path': x.get('_artifact_path'),
            }
            for x in sorted(rows, key=lambda y: int(y.get('box', -1)))
        ],
        'promotion_rule': (
            'CONFIRMED can support promotion of an otherwise-green Iter503; '
            'VIOLATION forbids promotion of green Iter503; INVALID_OR_BLOCKED caps promotion pending repair.'
        ),
        'scope': 'Iter503 implementation/prereg endpoint-contract audit only; no scientific D7 or selector verdict',
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    out = aggregate(a.root)
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    with open(a.out, 'w') as f:
        json.dump(out, f, indent=2, sort_keys=True)
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
