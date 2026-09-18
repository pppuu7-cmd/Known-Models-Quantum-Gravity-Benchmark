#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

GATE = 'ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE'
PREREG = 'e42caf47f9201d79cd89b79dc72b90f696e3ec5d'
DESIGN_AUTHORITY = 'a4006f336a49f655534a2f76a443a3d60a47cd85'
DESIGN_STATIC_CRITIC = '722c7e09bf077c0cb29c3ac0ac2ed724b99290f4'
IMPLEMENTATION_AUTHORITY = '42a2f035a80c474ebc7e5f57934ad9ba78ce9937'
TERMINAL_PARENT = 'd03cae09c04638cb02412435a284cfd9acdf8406'
CAMPAIGN_DESIGN = '6a789730833120a5e3037fdc11fe03b28ed5b9cb'
MANIFEST_BLOB = 'd3b8821e08243016bd475f3faf9f2161deed13d8'
CANONICAL_SHA256 = '3cac282175830e795394dca5202f5368b27120817f2d4abd9eba54fc6c9f1e6f'
PASS = 'ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED'
INC = 'ITER504V_BROADER_DOMAIN_LOCAL_D_INCONCLUSIVE_SCOPED'
INVALID = 'ITER504V_BROADER_DOMAIN_INVALID'
MAX_DEPTH = 3
RGRID = (6, 8, 10, 12)
RHOS = (0.35, 0.9, 1.6, 2.7)
CAUSALS = ('0to5', '1to4', '2to3')
BLOCKS = (0, 1, 2, 3)
PATHS = (0, 1, 2, 3)
BOXES = tuple(range(16))


def sha_json(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


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


def parse_state(sid):
    causal, b, p, x = sid.split('|')
    return causal, int(b[1:]), int(p[1:]), int(x[1:])


def box_interval(k):
    return Fraction(16 + k, 12800), Fraction(17 + k, 12800)


def expected_map():
    ids = canonical_state_ids()
    if len(ids) != 768 or len(set(ids)) != 768:
        raise RuntimeError('canonical state cardinality mismatch')
    if sequence_sha(ids) != CANONICAL_SHA256:
        raise RuntimeError('canonical state hash mismatch')
    m = json.loads(Path('inputs/iter504v_broader_domain_campaign_manifest.json').read_text())
    c = m['canonical_state_identity']
    if c['record_count'] != 768 or c['newline_terminated_enumeration_sha256'] != CANONICAL_SHA256:
        raise RuntimeError('manifest canonical identity mismatch')
    d = m['domain']
    if tuple(d['causals']) != CAUSALS or tuple(d['blocks']) != BLOCKS or tuple(d['paths']) != PATHS or tuple(d['boxes']) != BOXES:
        raise RuntimeError('manifest domain mismatch')
    pm = {
        (int(x['block']), int(x['path'])): (list(x['direction']), int(x['sign']))
        for x in d['path_map']
    }
    if set(pm) != {(b, p) for b in BLOCKS for p in PATHS}:
        raise RuntimeError('manifest path map mismatch')
    out = {}
    for sid in ids:
        causal, block, path, box = parse_state(sid)
        direction, sign = pm[(block, path)]
        out[sid] = (causal, block, path, box, direction, sign)
    return ids, out


def dyadic_cell_valid(box, leaf):
    d = int(leaf.get('depth', -1))
    a = Fraction(leaf['amp_lower_q'])
    b = Fraction(leaf['amp_upper_q'])
    lo, hi = box_interval(box)
    if d < 0 or d > MAX_DEPTH:
        return False
    w = (hi - lo) / (2 ** d)
    if b - a != w:
        return False
    q = (a - lo) / w
    return q.denominator == 1 and 0 <= q.numerator < 2 ** d


def validate_case(o, sid, expected):
    errors = []
    causal, block, path, box, direction, sign = expected[sid]
    exact = {
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
        'r_cohort_consumed': list(RGRID),
        'rho_cohort_consumed': list(RHOS),
        'cover_valid': True,
    }
    for k, v in exact.items():
        if o.get(k) != v:
            errors.append(k)
    if o.get('invalid'):
        errors.append('producer_invalid')

    lo, hi = box_interval(box)
    try:
        if Fraction(o.get('parent_amp_lower_q', '0')) != lo or Fraction(o.get('parent_amp_upper_q', '0')) != hi:
            errors.append('parent_interval')
    except Exception:
        errors.append('parent_interval_parse')

    leaves = o.get('leaves', [])
    if len(leaves) != o.get('terminal_leaf_count'):
        errors.append('terminal_leaf_count')
    if sum(not bool(x.get('certified')) for x in leaves) != o.get('unresolved_leaf_count'):
        errors.append('unresolved_leaf_count')
    try:
        spans = sorted((Fraction(x['amp_lower_q']), Fraction(x['amp_upper_q'])) for x in leaves)
        if not spans or spans[0][0] != lo or spans[-1][1] != hi or any(spans[i][1] != spans[i + 1][0] for i in range(len(spans) - 1)):
            errors.append('cover')
    except Exception:
        errors.append('cover_parse')

    expected_pm = {(R, rho) for R in RGRID for rho in RHOS}
    for leaf in leaves:
        try:
            if not dyadic_cell_valid(box, leaf):
                errors.append('dyadic_leaf')
            if Fraction(leaf['local_mid_q']) != (Fraction(leaf['amp_lower_q']) + Fraction(leaf['amp_upper_q'])) / 2:
                errors.append('local_midpoint')
        except Exception:
            errors.append('dyadic_parse')
        if leaf.get('validated_local_derivative') is not True or leaf.get('local_derivative_recomputed_here') is not True:
            errors.append('local_derivative')
        if leaf.get('leaf_certification_binding') != 'all_per_rho_exact':
            errors.append('leaf_binding_tag')
        if leaf.get('scientific_decision_transport') != 'exact_arb_booleans_float_bounds_display_only':
            errors.append('decision_transport')
        prs = leaf.get('per_rho', [])
        if tuple(float(x.get('rho')) for x in prs) != RHOS:
            errors.append('rho_rows')
        for row in prs:
            if row.get('certified') is not bool(row.get('slope_floor_satisfied') and row.get('drift_within_tolerance')):
                errors.append('per_rho_binding')
        if leaf.get('certified') is not all(row.get('certified') is True for row in prs):
            errors.append('leaf_per_rho_binding')
        if not leaf.get('certified') and int(leaf.get('depth', -1)) != MAX_DEPTH:
            errors.append('premature_unresolved_leaf_depth')
        pm = leaf.get('possible_max', [])
        if len(pm) != 16 or {(int(x.get('R')), float(x.get('rho'))) for x in pm} != expected_pm:
            errors.append('possible_max_grid')
        for row in pm:
            inds = row.get('indices', [])
            if len(inds) != len(set(inds)) or any(not isinstance(i, int) or not 0 <= i < 243 for i in inds):
                errors.append('possible_max_indices')

    incs = o.get('componentwise_parent_inclusion_records', [])
    if len(incs) != o.get('componentwise_parent_inclusion_record_count'):
        errors.append('inclusion_count')
    if len(incs) != max(0, int(o.get('visited_node_count', 0)) - 1):
        errors.append('inclusion_visited_binding')
    for rec in incs:
        if set(rec.get('haar_log_inclusion_by_R', {})) != {str(R) for R in RGRID}:
            errors.append('inclusion_haar')
        rows = rec.get('channel_inclusion_rows', [])
        if len(rows) != 16 or {(int(x.get('R')), float(x.get('rho'))) for x in rows} != expected_pm:
            errors.append('inclusion_grid')
        for row in rows:
            bits = row.get('componentwise_inclusion', [])
            if len(bits) != 243 or any(type(b) is not bool for b in bits):
                errors.append('inclusion_bits')
    return errors


def case_projection(o):
    return {
        'state_id': o['state_id'],
        'causal': o['causal'],
        'block': o['block'],
        'path': o['path'],
        'box': o['box'],
        'direction': o['direction'],
        'sign': o['sign'],
        'parent_amp_lower_q': o['parent_amp_lower_q'],
        'parent_amp_upper_q': o['parent_amp_upper_q'],
        'visited_node_count': o['visited_node_count'],
        'terminal_leaf_count': o['terminal_leaf_count'],
        'unresolved_leaf_count': o['unresolved_leaf_count'],
        'leaves': [
            {
                'depth': x['depth'],
                'amp_lower_q': x['amp_lower_q'],
                'amp_upper_q': x['amp_upper_q'],
                'local_mid_q': x['local_mid_q'],
                'certified': x['certified'],
                'per_rho': [
                    (
                        float(r['rho']),
                        r['slope_floor_satisfied'],
                        r['drift_within_tolerance'],
                        r['certified'],
                    )
                    for r in x['per_rho']
                ],
                'possible_max': [
                    (p['R'], float(p['rho']), tuple(p['indices']))
                    for p in x['possible_max']
                ],
            }
            for x in o['leaves']
        ],
        'parent_inclusion': [
            {
                'depth': x['depth'],
                'amp_lower_q': x['amp_lower_q'],
                'amp_upper_q': x['amp_upper_q'],
                'parent_depth': x['parent_depth'],
                'parent_amp_lower_q': x['parent_amp_lower_q'],
                'parent_amp_upper_q': x['parent_amp_upper_q'],
                'haar': x['haar_log_inclusion_by_R'],
                'rows': [
                    (r['R'], float(r['rho']), tuple(r['componentwise_inclusion']))
                    for r in x['channel_inclusion_rows']
                ],
                'all_componentwise_parent_inclusion': x['all_componentwise_parent_inclusion'],
            }
            for x in o['componentwise_parent_inclusion_records']
        ],
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--cases-root', required=True)
    p.add_argument('--out', required=True)
    a = p.parse_args()

    errors = []
    try:
        ids, expected = expected_map()
    except Exception as e:
        ids, expected = canonical_state_ids(), {}
        errors.append(f'cohort_manifest:{e!r}')

    cases = {}
    case_file_sha256 = {}
    duplicates = []
    for path in sorted(Path(a.cases_root).rglob('case-*.json')):
        o, h = load(path)
        sid = o.get('state_id')
        if sid in cases:
            duplicates.append(sid)
        else:
            cases[sid] = o
            case_file_sha256[sid] = h
    if duplicates:
        errors.append('duplicate_states')
    if set(cases) != set(ids):
        errors.append('case_set')
    if len(cases) != 768:
        errors.append('case_count')

    for sid in ids:
        if sid in cases and sid in expected:
            errors += [f'{sid}:{x}' for x in validate_case(cases[sid], sid, expected)]

    projection_sha_by_state = {}
    unresolved_by_state = {}
    visited_by_state = {}
    terminal_leaves_by_state = {}
    for sid in ids:
        if sid in cases and not cases[sid].get('invalid'):
            projection_sha_by_state[sid] = sha_json(case_projection(cases[sid]))
            unresolved_by_state[sid] = int(cases[sid].get('unresolved_leaf_count', 0))
            visited_by_state[sid] = int(cases[sid].get('visited_node_count', 0))
            terminal_leaves_by_state[sid] = int(cases[sid].get('terminal_leaf_count', 0))

    complete_projection = len(projection_sha_by_state) == 768
    if not complete_projection:
        errors.append('projection_count')

    total_unresolved = sum(unresolved_by_state.values()) if complete_projection else None
    counterexamples = [
        sid for sid in ids if unresolved_by_state.get(sid, 0) > 0
    ] if complete_projection else None
    classification = (
        INVALID
        if errors
        else (PASS if total_unresolved == 0 else INC)
    )
    projection_sequence_sha256 = (
        sha_json([[sid, projection_sha_by_state[sid]] for sid in ids])
        if complete_projection
        else None
    )

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
        'classification': classification,
        'errors': errors,
        'state_ids': list(ids),
        'total_cases': len(cases),
        'case_file_sha256': case_file_sha256,
        'decision_projection_sha256_by_state': projection_sha_by_state,
        'decision_projection_sequence_sha256': projection_sequence_sha256,
        'unresolved_leaf_count_by_state': unresolved_by_state if complete_projection else None,
        'total_visited_nodes': sum(visited_by_state.values()) if complete_projection else None,
        'total_terminal_leaves': sum(terminal_leaves_by_state.values()) if complete_projection else None,
        'total_unresolved_leaves': total_unresolved,
        'counterexample_state_ids': counterexamples,
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'max_depth': 3,
        'channels': 243,
        'r_cohort': list(RGRID),
        'rho_cohort': list(RHOS),
        'claim_ceiling': 'One Python-environment complete 768-record q=1 Phase-B assembly only',
    }
    payload = dict(out)
    out['assembly_payload_sha256'] = sha_json(payload)
    q = Path(a.out)
    q.parent.mkdir(parents=True, exist_ok=True)
    q.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({
        'classification': classification,
        'errors': errors,
        'total_cases': len(cases),
        'projection_count': len(projection_sha_by_state),
        'artifact_written': True,
    }, sort_keys=True))
    return 2 if classification == INVALID else 0


if __name__ == '__main__':
    raise SystemExit(main())
