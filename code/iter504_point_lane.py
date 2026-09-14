#!/usr/bin/env python3
"""Frozen Iter504 source-point regression evaluator for one logical causal x block lane."""
import argparse, json, os
import iter499_arb_core as core
import iter501_direct_max_envelope_interval as prev

CAUSALS = ['0to5', '1to4', '2to3']


def path_spec(block, path):
    direction = list(core.BLOCKS[block][path // 2])
    sign = 1 if path % 2 == 0 else -1
    return direction, sign


def evaluate(causal, block):
    paths = []
    valid = True
    for path in range(4):
        direction, sign = path_spec(block, path)
        amplitudes = []
        for amp in prev.POINT_AMPS:
            try:
                rows = prev.point_eval(causal, direction, sign, amp)
                amplitudes.append({'amplitude': amp, 'rho': rows})
            except Exception as e:
                valid = False
                amplitudes.append({'amplitude': amp, 'error': repr(e)})
        paths.append({
            'path': path,
            'direction': direction,
            'sign': sign,
            'amplitudes': amplitudes,
        })
    return {
        'iteration': 504,
        'kind': 'point_lane',
        'lane_id': f'{causal}-b{block}',
        'causal': causal,
        'block': block,
        'valid': bool(valid),
        'paths': paths,
        'scope': 'unchanged Iter492 source point evaluator at the nine frozen Iter501 amplitudes for Iter504 containment regression',
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--causal', required=True, choices=CAUSALS)
    ap.add_argument('--block', required=True, type=int, choices=range(4))
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    try:
        out = evaluate(a.causal, a.block)
    except Exception as e:
        out = {
            'iteration': 504,
            'kind': 'point_lane',
            'lane_id': f'{a.causal}-b{a.block}',
            'causal': a.causal,
            'block': a.block,
            'valid': False,
            'error': repr(e),
        }
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    with open(a.out, 'w') as f:
        json.dump(out, f, indent=2, sort_keys=True)
    print(json.dumps({k: v for k, v in out.items() if k != 'paths'}, indent=2, sort_keys=True))
    raise SystemExit(0)


if __name__ == '__main__':
    main()
