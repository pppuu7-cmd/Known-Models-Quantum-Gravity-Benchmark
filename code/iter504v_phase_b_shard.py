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

GATE = 'ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE'
PREREG = 'e42caf47f9201d79cd89b79dc72b90f696e3ec5d'
DESIGN_AUTHORITY = 'a4006f336a49f655534a2f76a443a3d60a47cd85'
DESIGN_STATIC_CRITIC = '722c7e09bf077c0cb29c3ac0ac2ed724b99290f4'
IMPLEMENTATION_AUTHORITY = '42a2f035a80c474ebc7e5f57934ad9ba78ce9937'
TERMINAL_PARENT = 'd03cae09c04638cb02412435a284cfd9acdf8406'
CAMPAIGN_DESIGN = '6a789730833120a5e3037fdc11fe03b28ed5b9cb'
MANIFEST_BLOB = 'd3b8821e08243016bd475f3faf9f2161deed13d8'
CANONICAL_SHA256 = '3cac282175830e795394dca5202f5368b27120817f2d4abd9eba54fc6c9f1e6f'
MAX_DEPTH = 3
CAUSALS = ('0to5', '1to4', '2to3')
BLOCKS = (0, 1, 2, 3)
PATHS = (0, 1, 2, 3)
BOXES = tuple(range(16))
QUARTILES = (
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (8, 9, 10, 11),
    (12, 13, 14, 15),
)


def canonical_state_ids():
    return tuple(
        f'{causal}|b{block}|p{path}|x{box:02d}'
        for causal in CAUSALS
        for block in BLOCKS
        for path in PATHS
        for box in BOXES
    )


def sequence_sha(ids):
    return hashlib.sha256(('\n'.join(ids) + '\n').encode()).hexdigest()


def load_manifest():
    p = Path('inputs/iter504v_broader_domain_campaign_manifest.json')
    m = json.loads(p.read_text())
    if m.get('gate') != 'ITER504V_BROADER_DOMAIN_CAMPAIGN_DESIGN':
        raise RuntimeError('campaign gate mismatch')
    if m['canonical_state_identity']['record_count'] != 768:
        raise RuntimeError('campaign record count mismatch')
    if m['canonical_state_identity']['newline_terminated_enumeration_sha256'] != CANONICAL_SHA256:
        raise RuntimeError('campaign canonical hash declaration mismatch')
    ids = canonical_state_ids()
    if len(ids) != 768 or len(set(ids)) != 768:
        raise RuntimeError('canonical identity cardinality mismatch')
    if sequence_sha(ids) != CANONICAL_SHA256:
        raise RuntimeError('canonical identity hash mismatch')
    domain = m['domain']
    if tuple(domain['causals']) != CAUSALS:
        raise RuntimeError('causal cohort mismatch')
    if tuple(domain['blocks']) != BLOCKS:
        raise RuntimeError('block cohort mismatch')
    if tuple(domain['paths']) != PATHS:
        raise RuntimeError('path cohort mismatch')
    if tuple(domain['boxes']) != BOXES:
        raise RuntimeError('box cohort mismatch')
    if tuple(domain['R']) != (6, 8, 10, 12):
        raise RuntimeError('R cohort mismatch')
    if tuple(domain['rhos']) != (0.35, 0.9, 1.6, 2.7):
        raise RuntimeError('rho cohort mismatch')
    if domain['channel_count'] != 243 or domain['precision_bits'] != 384 or domain['python_flint'] != '0.9.0':
        raise RuntimeError('numerical contract mismatch')
    pm = {
        (int(x['block']), int(x['path'])): (list(x['direction']), int(x['sign']))
        for x in domain['path_map']
    }
    if set(pm) != {(b, p) for b in BLOCKS for p in PATHS}:
        raise RuntimeError('path map mismatch')
    return m, pm


def state_id(causal, block, path, box):
    return f'{causal}|b{block}|p{path}|x{box:02d}'


def case_run(causal, block, path, box, path_map):
    sid = state_id(causal, block, path, box)
    if sid not in set(canonical_state_ids()):
        raise ValueError(f'unknown canonical state {sid}')
    if base.R_COHORT != (6, 8, 10, 12):
        raise RuntimeError(f'R cohort {base.R_COHORT}')
    if base.RHO_COHORT != (0.35, 0.9, 1.6, 2.7):
        raise RuntimeError(f'rho cohort {base.RHO_COHORT}')
    if MAX_DEPTH != base.MAX_DEPTH:
        raise RuntimeError('MAX_DEPTH mismatch with frozen Iter504U evaluator')

    direction_manifest, sign_manifest = path_map[(block, path)]
    direction_parent, sign_parent = parent.path_spec(block, path)
    if list(direction_parent) != direction_manifest or int(sign_parent) != sign_manifest:
        raise RuntimeError('path map differs from frozen centered-shard authority')
    direction = direction_manifest
    sign = sign_manifest

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
            inclusions.append(
                base._inclusion_record(snap, parent_snap, a, b, d, pa, pb, parent_depth)
            )
        if row['certified'] or d == MAX_DEPTH:
            leaves.append(row)
        else:
            m = (a + b) / 2
            stack.append((m, b, d + 1, snap, (a, b), d))
            stack.append((a, m, d + 1, snap, (a, b), d))

    spans = sorted(
        (Fraction(x['amp_lower_q']), Fraction(x['amp_upper_q']))
        for x in leaves
    )
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
        'design_authority_commit': DESIGN_AUTHORITY,
        'design_static_critic_commit': DESIGN_STATIC_CRITIC,
        'implementation_authority_commit': IMPLEMENTATION_AUTHORITY,
        'terminal_parent_commit': TERMINAL_PARENT,
        'campaign_design_commit': CAMPAIGN_DESIGN,
        'campaign_manifest_blob': MANIFEST_BLOB,
        'canonical_768_record_sequence_sha256': CANONICAL_SHA256,
        'case_id': sid,
        'state_id': sid,
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
        'claim_ceiling': 'One frozen Phase-B q=1 record; certification-procedure scope only',
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--causal', choices=CAUSALS, required=True)
    p.add_argument('--block', type=int, choices=BLOCKS, required=True)
    p.add_argument('--path', type=int, choices=PATHS, required=True)
    p.add_argument('--quartile', type=int, choices=range(4), required=True)
    p.add_argument('--out-dir', required=True)
    a = p.parse_args()

    out_dir = Path(a.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    invalid = []
    try:
        _, path_map = load_manifest()
    except Exception as e:
        path_map = None
        invalid.append({'state_id': None, 'error': repr(e)})

    boxes = QUARTILES[a.quartile]
    state_ids = []
    for box in boxes:
        sid = state_id(a.causal, a.block, a.path, box)
        state_ids.append(sid)
        if path_map is None:
            out = {
                'gate': GATE,
                'preregistration_commit': PREREG,
                'state_id': sid,
                'case_id': sid,
                'invalid': True,
                'error': invalid[0]['error'],
            }
        else:
            try:
                out = case_run(a.causal, a.block, a.path, box, path_map)
            except Exception as e:
                out = {
                    'gate': GATE,
                    'preregistration_commit': PREREG,
                    'design_authority_commit': DESIGN_AUTHORITY,
                    'design_static_critic_commit': DESIGN_STATIC_CRITIC,
                    'implementation_authority_commit': IMPLEMENTATION_AUTHORITY,
                    'terminal_parent_commit': TERMINAL_PARENT,
                    'campaign_design_commit': CAMPAIGN_DESIGN,
                    'campaign_manifest_blob': MANIFEST_BLOB,
                    'canonical_768_record_sequence_sha256': CANONICAL_SHA256,
                    'state_id': sid,
                    'case_id': sid,
                    'invalid': True,
                    'error': repr(e),
                }
                invalid.append({'state_id': sid, 'error': repr(e)})
        (out_dir / f'case-{box:02d}.json').write_text(
            json.dumps(out, indent=2, sort_keys=True) + '\n'
        )

    shard = {
        'gate': GATE,
        'python_environment_external': True,
        'causal': a.causal,
        'block': a.block,
        'path': a.path,
        'quartile': a.quartile,
        'boxes': list(boxes),
        'state_ids': state_ids,
        'record_count': 4,
        'invalid_count': len(invalid),
        'invalid_state_ids': [x['state_id'] for x in invalid if x['state_id'] is not None],
        'canonical_768_record_sequence_sha256': CANONICAL_SHA256,
    }
    (out_dir / 'shard.json').write_text(json.dumps(shard, indent=2, sort_keys=True) + '\n')
    print(json.dumps(shard, sort_keys=True))
    return 2 if invalid else 0


if __name__ == '__main__':
    raise SystemExit(main())
