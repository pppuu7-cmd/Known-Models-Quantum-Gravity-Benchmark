#!/usr/bin/env python3
"""Frozen Iter504 aggregate: reconstruct 12 logical lanes, then classify science."""
import argparse, collections, glob, json, math, os

CAUSALS = ['0to5', '1to4', '2to3']
EXPECTED_LANES = [f'{c}-b{b}' for c in CAUSALS for b in range(4)]
EXPECTED_SHARDS = [f'{c}-b{b}-p{p}-h{h}' for c in CAUSALS for b in range(4) for p in range(4) for h in range(2)]
POINT_AMPS = [0.00125,0.00140625,0.0015625,0.00171875,0.001875,0.00203125,0.0021875,0.00234375,0.00250]


def load_rows(root):
    shards, points = [], []
    for p in sorted(glob.glob(os.path.join(root, '**', '*.json'), recursive=True)):
        try:
            with open(p) as f:
                x = json.load(f)
        except Exception:
            continue
        if x.get('iteration') != 504:
            continue
        if x.get('kind') == 'centered_box_shard':
            shards.append(x)
        elif x.get('kind') == 'point_lane':
            points.append(x)
    return shards, points


def point_containment(boxmap, point_path):
    checks = []
    ok = True
    amps = point_path.get('amplitudes', [])
    if len(amps) != 9:
        return False, [{'error': 'expected 9 amplitudes', 'observed': len(amps)}]
    for j, ar in enumerate(amps):
        a = float(ar.get('amplitude')) if ar.get('amplitude') is not None else math.nan
        if not math.isfinite(a) or abs(a - POINT_AMPS[j]) > 1e-15 or ar.get('error'):
            ok = False
            checks.append({'amplitude': a, 'error': ar.get('error', 'amplitude mismatch')})
            continue
        endpoint = 2 * j
        candidates = [0] if endpoint == 0 else ([15] if endpoint == 16 else [endpoint - 1, endpoint])
        rows = ar.get('rho', [])
        if len(rows) != 4:
            ok = False
            checks.append({'amplitude': a, 'candidate_boxes': candidates, 'error': 'expected 4 rho rows'})
            continue
        for ir, r in enumerate(rows):
            try:
                sv = float(r['actual_slope'])
                ev = float(r['early_actual_slope'])
                hit = False
                witnesses = []
                for k in candidates:
                    b = boxmap.get(k)
                    if not b or b.get('error'):
                        continue
                    q = b['per_rho'][ir]
                    s_hit = float(q['S_lower']) <= sv <= float(q['S_upper'])
                    e_hit = float(q['E_lower']) <= ev <= float(q['E_upper'])
                    if s_hit and e_hit:
                        hit = True
                        witnesses.append(k)
                ok = ok and hit
                checks.append({
                    'amplitude': a,
                    'rho': float(r['rho']),
                    'candidate_boxes': candidates,
                    'witness_boxes': witnesses,
                    'contained': bool(hit),
                })
            except Exception as e:
                ok = False
                checks.append({'amplitude': a, 'candidate_boxes': candidates, 'contained': False, 'error': repr(e)})
    return bool(ok), checks


def science_class(classes, blocker):
    if blocker:
        return 'ITER504_NUMERICAL_METHOD_BLOCKER'
    if classes and all(c == 'INTERVAL_ROBUST_NONDECAY' for c in classes):
        return 'ITER504_CENTERED_MAX_ENVELOPE_ROBUST_QUALIFIED_SCOPED'
    if classes and all(c in ('INTERVAL_ROBUST_NONDECAY', 'INTERVAL_NONDECAY') for c in classes):
        return 'ITER504_CENTERED_MAX_ENVELOPE_NONDECAY_QUALIFIED_SCOPED'
    if any(c == 'INTERVAL_UNIFORM_DECAY_WITNESS' for c in classes):
        return 'SCIENTIFIC_FAIL_ITER504_UNIFORM_NONDECAY_INTERVAL'
    return 'ITER504_VALIDATED_CENTERED_INTERVAL_INCONCLUSIVE_SCOPED'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    shards, points = load_rows(a.root)

    shard_ids = [x.get('shard_id') for x in shards]
    point_ids = [x.get('lane_id') for x in points]
    sc = collections.Counter(shard_ids)
    pc = collections.Counter(point_ids)
    missing_shards = sorted(set(EXPECTED_SHARDS) - set(shard_ids))
    duplicate_shards = sorted(k for k, v in sc.items() if v != 1)
    extra_shards = sorted(set(shard_ids) - set(EXPECTED_SHARDS))
    missing_points = sorted(set(EXPECTED_LANES) - set(point_ids))
    duplicate_points = sorted(k for k, v in pc.items() if v != 1)
    extra_points = sorted(set(point_ids) - set(EXPECTED_LANES))

    structure_ok = bool(
        len(shards) == 96 and len(points) == 12 and
        not missing_shards and not duplicate_shards and not extra_shards and
        not missing_points and not duplicate_points and not extra_points
    )

    shard_map = {x.get('shard_id'): x for x in shards if sc[x.get('shard_id')] == 1}
    point_map = {x.get('lane_id'): x for x in points if pc[x.get('lane_id')] == 1}

    logical = []
    all_classes = []
    all_point_checks = 0
    global_min_s = math.inf
    global_max_s = -math.inf
    global_max_drift = -math.inf
    global_min_beta = math.inf
    max_possible = 0
    nboxes = 0
    blocker = not structure_ok
    known_crossing = []

    for causal in CAUSALS:
        for block in range(4):
            lane_id = f'{causal}-b{block}'
            lane_valid = True
            lane_classes = []
            lane_paths = []
            pr = point_map.get(lane_id)
            if not pr or not pr.get('valid', False) or len(pr.get('paths', [])) != 4:
                lane_valid = False
            point_paths = {p.get('path'): p for p in pr.get('paths', [])} if pr else {}

            for path in range(4):
                sm = []
                for half in range(2):
                    sid = f'{lane_id}-p{path}-h{half}'
                    x = shard_map.get(sid)
                    if not x or not x.get('valid', False):
                        lane_valid = False
                    sm.append(x)

                boxmap = {}
                direction = None
                sign = None
                for x in sm:
                    if not x:
                        continue
                    if direction is None:
                        direction = x.get('direction')
                        sign = x.get('sign')
                    elif direction != x.get('direction') or sign != x.get('sign'):
                        lane_valid = False
                    for b in x.get('boxes', []):
                        k = b.get('box')
                        if k in boxmap:
                            lane_valid = False
                        boxmap[k] = b

                if sorted(boxmap) != list(range(16)):
                    lane_valid = False

                path_classes = []
                for k in range(16):
                    b = boxmap.get(k)
                    if not b or b.get('error'):
                        lane_valid = False
                        continue
                    if not all(bool(v) for v in b.get('controls', {}).values()):
                        lane_valid = False
                    nboxes += 1
                    mb = b.get('min_beta_lower')
                    if mb is not None:
                        global_min_beta = min(global_min_beta, float(mb))
                    for q in b.get('per_rho', []):
                        c = q.get('classification')
                        if c not in ('INTERVAL_ROBUST_NONDECAY','INTERVAL_NONDECAY','INTERVAL_UNIFORM_DECAY_WITNESS','INTERVAL_INCONCLUSIVE'):
                            lane_valid = False
                            continue
                        path_classes.append(c)
                        lane_classes.append(c)
                        all_classes.append(c)
                        global_min_s = min(global_min_s, float(q['S_lower']))
                        global_max_s = max(global_max_s, float(q['S_upper']))
                        global_max_drift = max(global_max_drift, float(q['drift_upper']))
                    for rr in b.get('per_R', []):
                        for q in rr.get('rho', []):
                            max_possible = max(max_possible, int(q.get('possible_max_count', 0)))
                            if causal == '0to5' and direction == [1,1,1,-1,-1,-1] and sign == 1 and b.get('amp_upper', 0) >= 0.00234375 and rr.get('R') in (10,12) and abs(float(q.get('rho',0))-2.7) < 1e-12:
                                known_crossing.append({
                                    'lane': lane_id, 'path': path, 'box': k, 'R': rr.get('R'),
                                    'possible_max_indices': q.get('possible_max_indices', []),
                                    'count': q.get('possible_max_count', 0),
                                })

                pp = point_paths.get(path)
                if not pp:
                    point_ok, checks = False, [{'error': 'missing point path'}]
                else:
                    if direction != pp.get('direction') or sign != pp.get('sign'):
                        lane_valid = False
                    point_ok, checks = point_containment(boxmap, pp)
                all_point_checks += sum(1 for c in checks if 'rho' in c)
                lane_valid = lane_valid and point_ok
                lane_paths.append({
                    'path': path,
                    'direction': direction,
                    'sign': sign,
                    'box_count': len(boxmap),
                    'rho_box_state_count': len(path_classes),
                    'point_regression_pass': bool(point_ok),
                    'point_checks': checks,
                })

            if len(lane_classes) != 256:
                lane_valid = False
            blocker = blocker or (not lane_valid)
            logical.append({
                'lane_id': lane_id,
                'causal': causal,
                'block': block,
                'valid': bool(lane_valid),
                'classification': science_class(lane_classes, not lane_valid),
                'rho_box_state_count': len(lane_classes),
                'paths': lane_paths,
            })

    complete_counts = bool(nboxes == 768 and len(all_classes) == 3072 and all_point_checks == 1728)
    blocker = blocker or (not complete_counts)
    cls = science_class(all_classes, blocker)
    cc = collections.Counter(all_classes)

    out = {
        'iteration': 504,
        'classification': cls,
        'valid_structure': bool(structure_ok and complete_counts),
        'method_blocker': bool(blocker),
        'centered_shard_count': len(shards),
        'point_artifact_count': len(points),
        'logical_lane_count': len(logical),
        'expected_logical_lane_count': 12,
        'missing_shards': missing_shards,
        'duplicate_shards': duplicate_shards,
        'extra_shards': extra_shards,
        'missing_point_lanes': missing_points,
        'duplicate_point_lanes': duplicate_points,
        'extra_point_lanes': extra_points,
        'n_direction_boxes': nboxes,
        'expected_direction_boxes': 768,
        'n_rho_box_states': len(all_classes),
        'expected_rho_box_states': 3072,
        'n_point_containment_checks': all_point_checks,
        'expected_point_containment_checks': 1728,
        'class_counts': dict(cc),
        'global_min_S_lower': None if not all_classes else global_min_s,
        'global_max_S_upper': None if not all_classes else global_max_s,
        'global_max_drift_upper': None if not all_classes else global_max_drift,
        'global_min_beta_lower': None if global_min_beta is math.inf else global_min_beta,
        'max_possible_max_channel_count': max_possible,
        'known_crossing_region': known_crossing,
        'logical_lanes': logical,
        'scope': 'full frozen q=1 signed-direction 243-channel centered max-envelope science campaign; no multidimensional positive-measure, absolute-Haar, spectral-removal, collision-removal, ten-spectral finiteness, D7 closure or selector claim',
    }
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    with open(a.out, 'w') as f:
        json.dump(out, f, indent=2, sort_keys=True)
    print(json.dumps({k: v for k, v in out.items() if k not in ('logical_lanes','known_crossing_region')}, indent=2, sort_keys=True))
    raise SystemExit(0)


if __name__ == '__main__':
    main()
