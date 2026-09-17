#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

GATE = 'ITER504U_HELDOUT_LOCAL_D_GENERALIZATION_FIREWALL'
PREREG = '05b8e9354c9a7805f0fce18b904346a986a0787f'
PARENT_CRITIC = '8624532254981fbea6f8fcfac09cd538e2066aa4'
EXACT_REPAIR_HEAD = '10ae6bcc8447d14cecc6e550065504b23f792953'
MAX_DEPTH = 3
PASS = 'ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED'
INC = 'ITER504U_HELDOUT_LOCAL_D_INCONCLUSIVE_SCOPED'
INVALID = 'ITER504U_INVALID'
RGRID = (6, 8, 10, 12)
RHOS = (0.35, 0.9, 1.6, 2.7)
D1 = [1, 1, 1, -1, -1, -1]
D7 = [1, -1, -1, -1, -1, 1]

EXPECTED = {
    'H0_AMP_LOW': ('0to5', 0, 2, 0, D1, 1),
    'H1_AMP_MID': ('0to5', 0, 2, 8, D1, 1),
    'H2_CAUSAL_1': ('1to4', 0, 2, 8, D1, 1),
    'H3_CAUSAL_2': ('2to3', 0, 2, 8, D1, 1),
    'H4_DIRECTION': ('0to5', 3, 2, 8, D7, 1),
    'H5_SIGN': ('0to5', 0, 3, 8, D1, -1),
}


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def sha_json(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def box_interval(k):
    return Fraction(16 + k, 12800), Fraction(17 + k, 12800)


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


def validate_case(o, case_id):
    errors = []
    causal, block, path, box, direction, sign = EXPECTED[case_id]
    expected = {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'parent_critic_commit': PARENT_CRITIC,
        'exact_repair_head': EXACT_REPAIR_HEAD,
        'case_id': case_id,
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
    for k, v in expected.items():
        if o.get(k) != v:
            errors.append(k)
    if o.get('invalid'):
        errors.append('producer_invalid')
    if box in (13, 14, 15):
        errors.append('development_box_forbidden')
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
        'case_id': o['case_id'],
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
    for path in a.case_file:
        o, h = load(path)
        cid = o.get('case_id')
        if cid not in EXPECTED:
            errors.append(f'unknown_case:{cid}')
            continue
        if cid in cases:
            errors.append(f'duplicate_case:{cid}')
            continue
        cases[cid] = o
        file_sha[cid] = h
    if set(cases) != set(EXPECTED):
        errors.append('case_set')
    for cid in EXPECTED:
        if cid in cases:
            errors += [f'{cid}:{e}' for e in validate_case(cases[cid], cid)]

    unresolved = sum(cases[cid].get('unresolved_leaf_count', 0) for cid in EXPECTED if cid in cases)
    classification = INVALID if errors else (PASS if unresolved == 0 else INC)
    projection = [case_projection(cases[cid]) for cid in EXPECTED if cid in cases]
    out = {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'parent_critic_commit': PARENT_CRITIC,
        'exact_repair_head': EXACT_REPAIR_HEAD,
        'classification': classification,
        'errors': errors,
        'case_ids': list(EXPECTED),
        'case_file_sha256': file_sha,
        'total_cases': len(cases),
        'total_visited_nodes': sum(cases[cid].get('visited_node_count', 0) for cid in EXPECTED if cid in cases),
        'total_terminal_leaves': sum(cases[cid].get('terminal_leaf_count', 0) for cid in EXPECTED if cid in cases),
        'total_unresolved_leaves': unresolved,
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'max_depth': MAX_DEPTH,
        'channels': 243,
        'r_cohort': list(RGRID),
        'rho_cohort': list(RHOS),
        'decision_projection_sha256': sha_json(projection),
        'decision_projection': projection,
        'claim_ceiling': 'Prospectively frozen six-case Iter504U held-out cohort only; not all Iter504 states',
    }
    payload = dict(out)
    out['payload_sha256'] = sha_json(payload)
    q = Path(a.out)
    q.parent.mkdir(parents=True, exist_ok=True)
    q.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'decision_projection'}, indent=2, sort_keys=True))
    return 2 if classification == INVALID else 0


if __name__ == '__main__':
    raise SystemExit(main())
