#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import iter504q_adaptive_subbox_diagnostic as q


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root-box', required=True, type=int, choices=q.ROOT_BOXES)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    direction, sign = q.parent.path_spec(q.BLOCK, q.PATH)
    if direction != [1, 1, 1, -1, -1, -1] or sign != 1:
        raise SystemExit('frozen path identity mismatch')
    box = q.evaluate_box(a.root_box, direction, sign)
    p = Path(a.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(box, indent=2, sort_keys=True) + '\n')
    print(json.dumps({
        'root_box': box['root_box'],
        'node_count': box['node_count'],
        'leaf_count': len(box['leaves']),
        'cover_valid': box['cover']['valid'],
    }, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
