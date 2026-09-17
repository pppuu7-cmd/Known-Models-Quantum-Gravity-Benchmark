#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--a', required=True)
ap.add_argument('--b', required=True)
ap.add_argument('--out', required=True)
x = ap.parse_args()
a = json.loads(Path(x.a).read_text())
b = json.loads(Path(x.b).read_text())
keys = [
    'gate','classification','controls','authority_files','target_c4_exact_path_accepted','target_c4',
    'positive_full_path_classifications','per_rho_control_errors','r_cohort_control_errors','new_fact',
    'claim_ceiling','active_scientific_run_classified'
]
pa = {k: a.get(k) for k in keys}
pb = {k: b.get(k) for k in keys}
lanes_agree = pa == pb
classification = a.get('classification') if lanes_agree else 'INVALID_IMPLEMENTATION'
out = {
    'gate': a.get('gate'),
    'classification': classification,
    'lanes_agree': lanes_agree,
    'decision': pa,
    'lane_a_decision_sha256': a.get('decision_sha256'),
    'lane_b_decision_sha256': b.get('decision_sha256'),
}
canon = json.dumps(out, sort_keys=True, separators=(',', ':'))
out['aggregate_decision_sha256'] = hashlib.sha256(canon.encode()).hexdigest()
Path(x.out).parent.mkdir(parents=True, exist_ok=True)
Path(x.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
print(json.dumps(out, sort_keys=True))
raise SystemExit(0 if classification != 'INVALID_IMPLEMENTATION' else 2)
