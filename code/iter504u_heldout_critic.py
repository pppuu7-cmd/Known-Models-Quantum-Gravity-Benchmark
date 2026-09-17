#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path

GATE = 'ITER504U_HELDOUT_LOCAL_D_GENERALIZATION_FIREWALL'
PREREG = '05b8e9354c9a7805f0fce18b904346a986a0787f'
PARENT_CRITIC = '8624532254981fbea6f8fcfac09cd538e2066aa4'
EXACT_REPAIR_HEAD = '10ae6bcc8447d14cecc6e550065504b23f792953'
PASS = 'ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED'
INC = 'ITER504U_HELDOUT_LOCAL_D_INCONCLUSIVE_SCOPED'
INVALID = 'ITER504U_INVALID'
MAX_DEPTH = 3
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


def sha_json(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


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


def validate_case(o, cid):
    e = []
    causal, block, path, box, direction, sign = EXPECTED[cid]
    checks = {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'parent_critic_commit': PARENT_CRITIC,
        'exact_repair_head': EXACT_REPAIR_HEAD,
        'case_id': cid,
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
        'max_depth': 3,
        'partition_rule': 'deterministic_dyadic_midpoint',
        'local_derivative_recomputed_each_visited_node': True,
        'leaf_certification_binding': 'all_per_rho_exact',
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'r_cohort_consumed': list(RGRID),
        'rho_cohort_consumed': list(RHOS),
        'cover_valid': True,
    }
    for k, v in checks.items():
        if o.get(k) != v:
            e.append(k)
    if o.get('invalid'):
        e.append('producer_invalid')
    if o.get('box') in (13, 14, 15):
        e.append('development_box_forbidden')
    lo, hi = box_interval(box)
    if o.get('parent_amp_lower_q') != f'{lo.numerator}/{lo.denominator}' or o.get('parent_amp_upper_q') != f'{hi.numerator}/{hi.denominator}':
        e.append('parent_interval')

    leaves = o.get('leaves', [])
    if len(leaves) != o.get('terminal_leaf_count'):
        e.append('terminal_leaf_count')
    if sum(not bool(x.get('certified')) for x in leaves) != o.get('unresolved_leaf_count'):
        e.append('unresolved_leaf_count')
    try:
        spans = sorted((Fraction(x['amp_lower_q']), Fraction(x['amp_upper_q'])) for x in leaves)
        if not spans or spans[0][0] != lo or spans[-1][1] != hi or any(spans[i][1] != spans[i + 1][0] for i in range(len(spans) - 1)):
            e.append('cover')
    except Exception:
        e.append('cover_parse')

    expected_pm = {(R, rho) for R in RGRID for rho in RHOS}
    for leaf in leaves:
        try:
            if not dyadic_cell_valid(box, leaf):
                e.append('dyadic_leaf')
        except Exception:
            e.append('dyadic_parse')
        if leaf.get('validated_local_derivative') is not True or leaf.get('local_derivative_recomputed_here') is not True:
            e.append('local_derivative')
        if leaf.get('leaf_certification_binding') != 'all_per_rho_exact':
            e.append('leaf_binding_tag')
        if leaf.get('scientific_decision_transport') != 'exact_arb_booleans_float_bounds_display_only':
            e.append('decision_transport')
        prs = leaf.get('per_rho', [])
        if tuple(float(x.get('rho')) for x in prs) != RHOS:
            e.append('rho_rows')
        for row in prs:
            if row.get('certified') is not bool(row.get('slope_floor_satisfied') and row.get('drift_within_tolerance')):
                e.append('per_rho_binding')
        if leaf.get('certified') is not all(row.get('certified') is True for row in prs):
            e.append('C4_leaf_binding')
        pm = leaf.get('possible_max', [])
        if len(pm) != 16 or {(int(x.get('R')), float(x.get('rho'))) for x in pm} != expected_pm:
            e.append('possible_max_grid')
        for row in pm:
            inds = row.get('indices', [])
            if len(inds) != len(set(inds)) or any(not isinstance(i, int) or not 0 <= i < 243 for i in inds):
                e.append('possible_max_indices')

    incs = o.get('componentwise_parent_inclusion_records', [])
    if len(incs) != o.get('componentwise_parent_inclusion_record_count') or len(incs) != max(0, int(o.get('visited_node_count', 0)) - 1):
        e.append('inclusion_count')
    for rec in incs:
        if set(rec.get('haar_log_inclusion_by_R', {})) != {str(R) for R in RGRID}:
            e.append('inclusion_haar')
        rows = rec.get('channel_inclusion_rows', [])
        if len(rows) != 16 or {(int(x.get('R')), float(x.get('rho'))) for x in rows} != expected_pm:
            e.append('inclusion_grid')
        for row in rows:
            bits = row.get('componentwise_inclusion', [])
            if len(bits) != 243 or any(type(b) is not bool for b in bits):
                e.append('inclusion_bits')
    return e


def projection(cases):
    out = []
    for cid in EXPECTED:
        o = cases[cid]
        out.append({
            'case_id': o['case_id'], 'causal': o['causal'], 'block': o['block'], 'path': o['path'], 'box': o['box'],
            'direction': o['direction'], 'sign': o['sign'], 'parent_amp_lower_q': o['parent_amp_lower_q'], 'parent_amp_upper_q': o['parent_amp_upper_q'],
            'visited_node_count': o['visited_node_count'], 'terminal_leaf_count': o['terminal_leaf_count'], 'unresolved_leaf_count': o['unresolved_leaf_count'],
            'leaves': [{
                'depth': x['depth'], 'amp_lower_q': x['amp_lower_q'], 'amp_upper_q': x['amp_upper_q'], 'local_mid_q': x['local_mid_q'], 'certified': x['certified'],
                'per_rho': [(float(r['rho']), r['slope_floor_satisfied'], r['drift_within_tolerance'], r['certified']) for r in x['per_rho']],
                'possible_max': [(p['R'], float(p['rho']), tuple(p['indices'])) for p in x['possible_max']],
            } for x in o['leaves']],
            'parent_inclusion': [{
                'depth': x['depth'], 'amp_lower_q': x['amp_lower_q'], 'amp_upper_q': x['amp_upper_q'], 'parent_depth': x['parent_depth'],
                'parent_amp_lower_q': x['parent_amp_lower_q'], 'parent_amp_upper_q': x['parent_amp_upper_q'], 'haar': x['haar_log_inclusion_by_R'],
                'rows': [(r['R'], float(r['rho']), tuple(r['componentwise_inclusion'])) for r in x['channel_inclusion_rows']],
                'all_componentwise_parent_inclusion': x['all_componentwise_parent_inclusion'],
            } for x in o['componentwise_parent_inclusion_records']],
        })
    return out


def discover(directory):
    cases = {}
    hashes = {}
    duplicates = []
    for path in sorted(Path(directory).rglob('case.json')):
        o, h = load(path)
        cid = o.get('case_id')
        if cid in cases:
            duplicates.append(cid)
        else:
            cases[cid] = o
            hashes[cid] = h
    return cases, hashes, duplicates


def validate_all(cases):
    errs = []
    if set(cases) != set(EXPECTED):
        errs.append('case_set')
    for cid in EXPECTED:
        if cid in cases:
            errs += [f'{cid}:{x}' for x in validate_case(cases[cid], cid)]
    return errs


def classification(cases):
    return PASS if sum(cases[cid]['unresolved_leaf_count'] for cid in EXPECTED) == 0 else INC


def negative_controls(base):
    tests = {}

    def reject(name, mut):
        x = copy.deepcopy(base)
        mut(x)
        tests[name] = bool(validate_all(x))

    reject('wrong_case_identity', lambda x: x['H0_AMP_LOW'].__setitem__('causal', '1to4'))
    reject('development_box_inserted', lambda x: x['H0_AMP_LOW'].__setitem__('box', 13))
    reject('missing_heldout_case', lambda x: x.pop('H5_SIGN'))
    reject('changed_threshold', lambda x: x['H0_AMP_LOW'].__setitem__('threshold_exact', '1/19'))
    reject('changed_floor', lambda x: x['H0_AMP_LOW'].__setitem__('robust_floor_exact', '0.9'))
    reject('changed_depth', lambda x: x['H0_AMP_LOW'].__setitem__('max_depth', 4))
    reject('channel_pruning', lambda x: x['H0_AMP_LOW'].__setitem__('full_channel_count', 242))
    reject('wrong_R_cohort', lambda x: x['H0_AMP_LOW'].__setitem__('r_cohort_consumed', [7, 8, 10, 12]))
    reject('wrong_rho_cohort', lambda x: x['H0_AMP_LOW'].__setitem__('rho_cohort_consumed', [0.36, 0.9, 1.6, 2.7]))
    reject('root_derivative_reuse', lambda x: x['H0_AMP_LOW'].__setitem__('local_derivative_recomputed_each_visited_node', False))
    reject('float_decision_transport', lambda x: x['H0_AMP_LOW']['leaves'][0].__setitem__('scientific_decision_transport', 'float_threshold'))
    reject('non_dyadic_partition', lambda x: x['H0_AMP_LOW']['leaves'][0].__setitem__('amp_upper_q', str(Fraction(x['H0_AMP_LOW']['leaves'][0]['amp_upper_q']) + Fraction(1, 10**12))))
    reject('C4_true_leaf_false_rho', lambda x: x['H0_AMP_LOW']['leaves'][0]['per_rho'][0].__setitem__('certified', False))
    reject('leaf_binding_tag_removed', lambda x: x['H0_AMP_LOW']['leaves'][0].__setitem__('leaf_certification_binding', 'unbound'))
    return tests


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--a-dir', required=True)
    p.add_argument('--b-dir', required=True)
    p.add_argument('--a-assembled', required=True)
    p.add_argument('--b-assembled', required=True)
    p.add_argument('--aggregate', required=True)
    p.add_argument('--out', required=True)
    a = p.parse_args()

    A, Ah, adup = discover(a.a_dir)
    B, Bh, bdup = discover(a.b_dir)
    errors = []
    if adup:
        errors.append('a_duplicate_cases')
    if bdup:
        errors.append('b_duplicate_cases')
    errors += [f'a:{x}' for x in validate_all(A)]
    errors += [f'b:{x}' for x in validate_all(B)]

    aa, aah = load(a.a_assembled)
    bb, bbh = load(a.b_assembled)
    agg, aggh = load(a.aggregate)

    ca = classification(A) if not [e for e in errors if e.startswith('a:')] and set(A) == set(EXPECTED) else INVALID
    cb = classification(B) if not [e for e in errors if e.startswith('b:')] and set(B) == set(EXPECTED) else INVALID
    pa = projection(A) if ca != INVALID else None
    pb = projection(B) if cb != INVALID else None
    cross = pa == pb and ca == cb and ca != INVALID

    if aa.get('classification') != ca or aa.get('decision_projection_sha256') != (sha_json(pa) if pa is not None else None):
        errors.append('assembled_a')
    if bb.get('classification') != cb or bb.get('decision_projection_sha256') != (sha_json(pb) if pb is not None else None):
        errors.append('assembled_b')
    if not cross:
        errors.append('cross_environment_exact_projection')
    if agg.get('classification') != ca or agg.get('cross_environment_exact_decision_agreement') is not True:
        errors.append('aggregate_authority')

    neg = negative_controls(A) if set(A) == set(EXPECTED) and not [e for e in errors if e.startswith('a:')] else {}
    if not neg or not all(neg.values()):
        errors.append('negative_controls')

    final = ca if not errors else INVALID
    out = {
        'gate': GATE,
        'preregistration_commit': PREREG,
        'parent_critic_commit': PARENT_CRITIC,
        'classification': final,
        'critic_errors': errors,
        'cross_environment_exact_decision_agreement': cross,
        'lane_a_case_sha256': Ah,
        'lane_b_case_sha256': Bh,
        'lane_a_assembled_sha256': aah,
        'lane_b_assembled_sha256': bbh,
        'aggregate_sha256': aggh,
        'decision_projection_sha256': sha_json(pa) if cross else None,
        'negative_controls': neg,
        'total_cases': 6 if final != INVALID else None,
        'total_terminal_leaves': sum(A[cid]['terminal_leaf_count'] for cid in EXPECTED) if final != INVALID else None,
        'total_unresolved_leaves': sum(A[cid]['unresolved_leaf_count'] for cid in EXPECTED) if final != INVALID else None,
        'threshold_exact': '1/20',
        'robust_floor_exact': '1',
        'max_depth': 3,
        'channels': 243,
        'claim_ceiling': 'Independent six-case Iter504U held-out Critic only; not all Iter504 states',
    }
    payload = dict(out)
    out['critic_payload_sha256'] = sha_json(payload)
    q = Path(a.out)
    q.parent.mkdir(parents=True, exist_ok=True)
    q.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps(out, indent=2, sort_keys=True))
    return 2 if final == INVALID else 0


if __name__ == '__main__':
    raise SystemExit(main())
