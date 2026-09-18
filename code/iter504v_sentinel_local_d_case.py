#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

from flint import ctx

import iter504_centered_shard as parent
import iter504u_heldout_local_d_case as base

ctx.prec = 384

GATE = 'ITER504V_SENTINEL_LOCAL_D_COUNTEREXAMPLE_FIRST'
PREREG = 'c162f23df45a58c567fa04fcdf99035497e482f2'
PARENT_TERMINAL = 'a31db0d6b9f98448977a6fcdde80a45e3e7195fe'
POSTCLOSURE_AUDIT = 'dd32ae2616f4cbe3826f73c7a1d2f51818b4954c'
CAMPAIGN_DESIGN = '6a789730833120a5e3037fdc11fe03b28ed5b9cb'
MANIFEST_BLOB = 'd3b8821e08243016bd475f3faf9f2161deed13d8'
SENTINEL_SHA256 = 'b56a2a32cd96b28c14aaaa86f1062d1f2f2a167a2295ed99f904a99fd8371e82'
MAX_DEPTH = 3
SENTINELS = (
    '0to5|b0|p0|x00',
    '1to4|b0|p1|x01',
    '2to3|b0|p2|x02',
    '0to5|b0|p3|x03',
    '1to4|b1|p0|x04',
    '2to3|b1|p1|x05',
    '0to5|b1|p2|x06',
    '1to4|b1|p3|x07',
    '2to3|b2|p0|x08',
    '0to5|b2|p1|x09',
    '1to4|b2|p2|x10',
    '2to3|b2|p3|x11',
    '0to5|b3|p0|x12',
    '1to4|b3|p1|x13',
    '2to3|b3|p2|x14',
    '0to5|b3|p3|x15',
)


def sentinel_sha256() -> str:
    raw = ('\n'.join(SENTINELS) + '\n').encode()
    return hashlib.sha256(raw).hexdigest()


def parse_state_id(state_id: str):
    if state_id not in SENTINELS:
        raise ValueError(f'unknown sentinel {state_id}')
    causal, b, p, x = state_id.split('|')
    return causal, int(b[1:]), int(p[1:]), int(x[1:])


def case_run(state_id: str):
    if sentinel_sha256() != SENTINEL_SHA256:
        raise RuntimeError('sentinel cohort hash mismatch')
    causal, block, path, box = parse_state_id(state_id)
    if box != 4 * block + path:
        raise RuntimeError('sentinel selection rule mismatch')
    causal_expected = ('0to5', '1to4', '2to3')[(block + path) % 3]
    if causal != causal_expected:
        raise RuntimeError('sentinel causal rule mismatch')
    if base.R_COHORT != (6, 8, 10, 12):
        raise RuntimeError(f'R cohort {base.R_COHORT}')
    if base.RHO_COHORT != (0.35, 0.9, 1.6, 2.7):
        raise RuntimeError(f'rho cohort {base.RHO_COHORT}')
    if MAX_DEPTH != base.MAX_DEPTH:
        raise RuntimeError('MAX_DEPTH mismatch with frozen Iter504U evaluator')

    direction, sign = parent.path_spec(block, path)
    lo, hi = base.box_interval(box)
    stack = [(lo, hi, 0, None, None, None)]
    leaves = []
    inclusions = []
    visited = 0
    while stack:
        a, b, d, parent_snap, parent_bounds, parent_depth = stack.pop()
        row, snap = base.evaluate(a, b, d, causal, direction, sign)
        visited += 1
        if parent_snap is not None:
            pa, pb = parent_bounds
            inclusions.append(base._inclusion_record(snap, parent_snap, a, b, d, pa, pb, parent_depth))
        if row['certified'] or d == MAX_DEPTH:
            leaves.append(row)
        else:
            m = (a + b) / 2
            stack.append((m, b, d + 1, snap, (a, b), d))
            stack.append((a, m, d + 1, snap, (a, b), d))

    spans = sorted((Fraction(x['amp_lower_q']), Fraction(x['amp_upper_q'])) for x in leaves)
    cover = bool(
        spans
        and spans[0][0] == lo
        and spans[-1][1] == hi
        and all(spans[i][1] == spans[i + 1][0] for i in range(len(spans) - 1))
    )
    unresolved = [x for x in leaves if not x['certified']]
    if any(int(x['depth']) != MAX_DEPTH for x in unresolved):
        raise RuntimeError('premature unresolved terminal leaf')

    return {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'parent_terminal_authority_commit': PARENT_TERMINAL,
        'postclosure_audit_commit': POSTCLOSURE_AUDIT,
        'campaign_design_commit': CAMPAIGN_DESIGN,
        'campaign_manifest_blob': MANIFEST_BLOB,
        'sentinel_sequence_sha256': SENTINEL_SHA256,
        'case_id': state_id,
        'state_id': state_id,
        'causal': causal,
        'block': block,
        'path': path,
        'box': box,
        'direction': direction,
        'sign': sign,
        'parent_amp_lower_q': base.qt(lo),
        'parent_amp_upper_q': base.qt(hi),
        'precision_bits': 384,
        'python_flint': '0.9.0',
        'full_channel_count': 243,
        'channel_pruning_used': False,
        'max_depth': MAX_DEPTH,
        'partition_rule': 'deterministic_dyadic_midpoint',
        'local_derivative_recomputed_each_visited_node': True,
        'leaf_certification_binding': 'all_per_rho_exact',
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'r_cohort_consumed': list(base.R_COHORT),
        'rho_cohort_consumed': list(base.RHO_COHORT),
        'componentwise_parent_inclusion_record_count': len(inclusions),
        'componentwise_parent_inclusion_records': inclusions,
        'cover_valid': cover,
        'visited_node_count': visited,
        'terminal_leaf_count': len(leaves),
        'unresolved_leaf_count': len(unresolved),
        'leaves': leaves,
        'claim_ceiling': 'One frozen Iter504V sentinel record; certification-procedure scope only',
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--index', type=int, choices=range(len(SENTINELS)), required=True)
    p.add_argument('--out', required=True)
    a = p.parse_args()
    state_id = SENTINELS[a.index]
    try:
        out = case_run(state_id)
    except Exception as e:
        out = {
            'gate': GATE,
            'preregistration_commit': PREREG,
            'parent_terminal_authority_commit': PARENT_TERMINAL,
            'postclosure_audit_commit': POSTCLOSURE_AUDIT,
            'campaign_design_commit': CAMPAIGN_DESIGN,
            'campaign_manifest_blob': MANIFEST_BLOB,
            'sentinel_sequence_sha256': SENTINEL_SHA256,
            'case_id': state_id,
            'state_id': state_id,
            'invalid': True,
            'error': repr(e),
        }
    q = Path(a.out)
    q.parent.mkdir(parents=True, exist_ok=True)
    q.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'state_id': state_id, 'artifact_written': True, 'invalid': bool(out.get('invalid'))}, sort_keys=True))
    return 2 if out.get('invalid') else 0


if __name__ == '__main__':
    raise SystemExit(main())
