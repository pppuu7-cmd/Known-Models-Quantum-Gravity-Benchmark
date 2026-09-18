#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

GATE = 'ITER504V_SENTINEL_LOCAL_D_COUNTEREXAMPLE_FIRST'
PREREG = 'c162f23df45a58c567fa04fcdf99035497e482f2'
PARENT_TERMINAL = 'a31db0d6b9f98448977a6fcdde80a45e3e7195fe'
POSTCLOSURE_AUDIT = 'dd32ae2616f4cbe3826f73c7a1d2f51818b4954c'
CAMPAIGN_DESIGN = '6a789730833120a5e3037fdc11fe03b28ed5b9cb'
MANIFEST_BLOB = 'd3b8821e08243016bd475f3faf9f2161deed13d8'
SENTINEL_SHA256 = 'b56a2a32cd96b28c14aaaa86f1062d1f2f2a167a2295ed99f904a99fd8371e82'
MAX_DEPTH = 3
PASS = 'ITER504V_SENTINEL_LOCAL_D_NO_COUNTEREXAMPLE_SCOPED'
INC = 'ITER504V_SENTINEL_LOCAL_D_COUNTEREXAMPLE_TO_UNIFORM_CERTIFICATION_SCOPED'
INVALID = 'ITER504V_SENTINEL_INVALID'
RGRID = (6, 8, 10, 12)
RHOS = (0.35, 0.9, 1.6, 2.7)
SENTINELS = (
    '0to5|b0|p0|x00', '1to4|b0|p1|x01', '2to3|b0|p2|x02', '0to5|b0|p3|x03',
    '1to4|b1|p0|x04', '2to3|b1|p1|x05', '0to5|b1|p2|x06', '1to4|b1|p3|x07',
    '2to3|b2|p0|x08', '0to5|b2|p1|x09', '1to4|b2|p2|x10', '2to3|b2|p3|x11',
    '0to5|b3|p0|x12', '1to4|b3|p1|x13', '2to3|b3|p2|x14', '0to5|b3|p3|x15',
)


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def sha_json(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def sequence_sha(ids):
    return hashlib.sha256(('\n'.join(ids) + '\n').encode()).hexdigest()


def box_interval(k):
    return Fraction(16 + k, 12800), Fraction(17 + k, 12800)


def parse_state(state_id):
    causal, b, p, x = state_id.split('|')
    return causal, int(b[1:]), int(p[1:]), int(x[1:])


def expected_map():
    if sequence_sha(SENTINELS) != SENTINEL_SHA256:
        raise RuntimeError('embedded sentinel hash mismatch')
    manifest = json.loads(Path('inputs/iter504v_broader_domain_campaign_manifest.json').read_text())
    ids = tuple(manifest['phase_a_sentinel']['state_ids'])
    if ids != SENTINELS:
        raise RuntimeError('manifest sentinel sequence mismatch')
    if manifest['phase_a_sentinel']['newline_terminated_state_id_sha256'] != SENTINEL_SHA256:
        raise RuntimeError('manifest sentinel declared hash mismatch')
    if sequence_sha(ids) != SENTINEL_SHA256:
        raise RuntimeError('manifest sentinel computed hash mismatch')
    pm = {(int(x['block']), int(x['path'])): (list(x['direction']), int(x['sign'])) for x in manifest['domain']['path_map']}
    out = {}
    for sid in SENTINELS:
        causal, block, path, box = parse_state(sid)
        if box != 4 * block + path:
            raise RuntimeError('selection rule mismatch')
        if causal != ('0to5', '1to4', '2to3')[(block + path) % 3]:
            raise RuntimeError('causal selection mismatch')
        direction, sign = pm[(block, path)]
        out[sid] = (causal, block, path, box, direction, sign)
    return out


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


def validate_case(o, state_id, expected):
    errors = []
    causal, block, path, box, direction, sign = expected[state_id]
    exact = {
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
    if o.get('parent_amp_lower_q') != f'{lo.numerator}/{lo.denominator}' or o.get('parent_amp_upper_q') != f'{hi.numerator}/{hi.denominator}':
        errors.append('parent_amp_interval')

    leaves = o.get('leaves', [])
    if len(leaves) != o.get('terminal_leaf_count'):
        errors.append('terminal_leaf_count')
    unresolved = sum(not bool(x.get('certified')) for x in leaves)
    if unresolved != o.get('unresolved_leaf_count'):
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
                errors.append('non_dyadic_leaf')
        except Exception:
            errors.append('dyadic_parse')
        if leaf.get('validated_local_derivative') is not True or leaf.get('local_derivative_recomputed_here') is not True:
            errors.append('local_derivative')
        if leaf.get('leaf_certification_binding') != 'all_per_rho_exact':
            errors.append('leaf_binding_tag')
        if leaf.get('scientific_decision_transport') != 'exact_arb_booleans_float_bounds_display_only':
            errors.append('decision_transport')
        prs = leaf.get('per_rho', [])
        if tuple(float(r.get('rho')) for r in prs) != RHOS:
            errors.append('rho_rows')
        for r in prs:
            if r.get('certified') is not bool(r.get('slope_floor_satisfied') and r.get('drift_within_tolerance')):
                errors.append('per_rho_boolean_binding')
        if leaf.get('certified') is not all(r.get('certified') is True for r in prs):
            errors.append('leaf_per_rho_binding')
        if leaf.get('certified') is not True and int(leaf.get('depth', -1)) != MAX_DEPTH:
            errors.append('premature_unresolved_leaf_depth')
        pm = leaf.get('possible_max', [])
        if {(int(x.get('R')), float(x.get('rho'))) for x in pm} != expected_pm or len(pm) != 16:
            errors.append('possible_max_grid')
        for x in pm:
            inds = x.get('indices', [])
            if len(inds) != len(set(inds)) or any(not isinstance(i, int) or i < 0 or i >= 243 for i in inds):
                errors.append('possible_max_indices')

    inclusions = o.get('componentwise_parent_inclusion_records', [])
    if len(inclusions) != o.get('componentwise_parent_inclusion_record_count'):
        errors.append('inclusion_count')
    if len(inclusions) != max(0, int(o.get('visited_node_count', 0)) - 1):
        errors.append('inclusion_visited_binding')
    for rec in inclusions:
        if set(rec.get('haar_log_inclusion_by_R', {})) != {str(x) for x in RGRID}:
            errors.append('inclusion_haar_grid')
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
                'per_rho': [(float(r['rho']), r['slope_floor_satisfied'], r['drift_within_tolerance'], r['certified']) for r in x['per_rho']],
                'possible_max': [(p['R'], float(p['rho']), tuple(p['indices'])) for p in x['possible_max']],
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
                'rows': [(r['R'], float(r['rho']), tuple(r['componentwise_inclusion'])) for r in x['channel_inclusion_rows']],
                'all_componentwise_parent_inclusion': x['all_componentwise_parent_inclusion'],
            }
            for x in o['componentwise_parent_inclusion_records']
        ],
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--case-file', action='append', required=True)
    p.add_argument('--out', required=True)
    a = p.parse_args()
    errors = []
    cases = {}
    file_sha = {}
    try:
        expected = expected_map()
    except Exception as e:
        expected = {}
        errors.append(f'cohort_manifest:{e!r}')
    for path in a.case_file:
        o, h = load(path)
        sid = o.get('state_id')
        if sid not in expected:
            errors.append(f'unknown_state:{sid}')
            continue
        if sid in cases:
            errors.append(f'duplicate_state:{sid}')
            continue
        cases[sid] = o
        file_sha[sid] = h
    if tuple(cases) != SENTINELS and set(cases) != set(SENTINELS):
        errors.append('case_set')
    for sid in SENTINELS:
        if sid in cases:
            errors += [f'{sid}:{e}' for e in validate_case(cases[sid], sid, expected)]

    unresolved = sum(cases[sid].get('unresolved_leaf_count', 0) for sid in SENTINELS if sid in cases)
    classification = INVALID if errors else (PASS if unresolved == 0 else INC)
    projection = [case_projection(cases[sid]) for sid in SENTINELS if sid in cases]
    out = {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'parent_terminal_authority_commit': PARENT_TERMINAL,
        'postclosure_audit_commit': POSTCLOSURE_AUDIT,
        'campaign_design_commit': CAMPAIGN_DESIGN,
        'campaign_manifest_blob': MANIFEST_BLOB,
        'sentinel_sequence_sha256': SENTINEL_SHA256,
        'classification': classification,
        'errors': errors,
        'state_ids': list(SENTINELS),
        'case_file_sha256': file_sha,
        'total_cases': len(cases),
        'total_visited_nodes': sum(cases[sid].get('visited_node_count', 0) for sid in SENTINELS if sid in cases),
        'total_terminal_leaves': sum(cases[sid].get('terminal_leaf_count', 0) for sid in SENTINELS if sid in cases),
        'total_unresolved_leaves': unresolved,
        'counterexample_state_ids': [sid for sid in SENTINELS if sid in cases and cases[sid].get('unresolved_leaf_count', 0) > 0],
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'max_depth': MAX_DEPTH,
        'channels': 243,
        'r_cohort': list(RGRID),
        'rho_cohort': list(RHOS),
        'decision_projection_sha256': sha_json(projection),
        'decision_projection': projection,
        'claim_ceiling': 'Frozen 16-state Iter504V sentinel only; current certification procedure scope',
    }
    payload = dict(out)
    out['payload_sha256'] = sha_json(payload)
    q = Path(a.out)
    q.parent.mkdir(parents=True, exist_ok=True)
    q.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k not in ('decision_projection', 'counterexample_state_ids')}, indent=2, sort_keys=True))
    return 2 if classification == INVALID else 0


if __name__ == '__main__':
    raise SystemExit(main())
