#!/usr/bin/env python3
import argparse
import glob
import json
import os

EXPECTED = {0, 7, 15}


def load_all(root):
    rows = []
    for p in sorted(glob.glob(os.path.join(root, '**', 'iter503-box*.json'), recursive=True)):
        with open(p) as f:
            rows.append(json.load(f))
    return rows


def aggregate(root):
    rows = load_all(root)
    by_box = {}
    duplicates = []
    for r in rows:
        k = r.get('box')
        if k in by_box:
            duplicates.append(k)
        else:
            by_box[k] = r
    got = {k for k in by_box if k in EXPECTED}
    missing = sorted(EXPECTED - got)
    valid_structure = (not missing and not duplicates and len(got) == len(EXPECTED))
    method = (not valid_structure) or any(bool(by_box[k].get('method_blocker', True)) for k in got)
    centered_all = bool(valid_structure and all(bool(by_box[k].get('centered_containment_all')) for k in EXPECTED))
    negative_any = bool(valid_structure and any(bool(by_box[k].get('negative_control_reproduced')) for k in EXPECTED))
    if method or not centered_all:
        cls = 'ITER503_NUMERICAL_METHOD_BLOCKER'
    elif negative_any:
        cls = 'ITER503_CENTERED_DEPENDENCY_REPAIR_ENABLED_SCOPED'
    else:
        cls = 'ITER503_CENTERED_DEPENDENCY_REPAIR_INCONCLUSIVE'
    return {
        'iteration': 503,
        'classification': cls,
        'valid_structure': bool(valid_structure),
        'method_blocker': bool(method or not centered_all),
        'centered_containment_all': centered_all,
        'negative_control_reproduced_any': negative_any,
        'boxes_present': sorted(got),
        'missing_boxes': missing,
        'duplicate_boxes': sorted(set(duplicates)),
        'lane_classifications': {str(k): by_box[k].get('classification') for k in sorted(got)},
        'scope': 'Iter503 centered single-common-amplitude dependency-repair enabling subset only; PASS authorizes only a separately preregistered full 12-lane centered/correlated science gate.'
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
    raise SystemExit(0)


if __name__ == '__main__':
    main()
