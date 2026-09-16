#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import iter504q_adaptive_subbox_diagnostic as q


def load_one(path: str):
    p = Path(path)
    obj = json.loads(p.read_text())
    return obj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--box13', required=True)
    ap.add_argument('--box14', required=True)
    ap.add_argument('--box15', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    boxes = [load_one(a.box13), load_one(a.box14), load_one(a.box15)]
    boxes.sort(key=lambda x: x['root_box'])
    if [x['root_box'] for x in boxes] != list(q.ROOT_BOXES):
        raise SystemExit('root-box identity mismatch')
    out = q.summarize(boxes)
    p = Path(a.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'boxes'}, indent=2, sort_keys=True))
    return 0 if out.get('classification') != q.INVALID else 2


if __name__ == '__main__':
    raise SystemExit(main())
