#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--a', required=True)
ap.add_argument('--b', required=True)
ap.add_argument('--out', required=True)
args = ap.parse_args()
a = json.loads(Path(args.a).read_text())
b = json.loads(Path(args.b).read_text())

keys = [
    'classification', 'exact_run', 'terminal_c4_retained', 'authority_identity',
    'artifact_internal_file_sha256', 'assembly_byte_identical', 'lanes',
    'aggregate_observed', 'critic_observed', 'repair_verdict_observed',
    'negative_controls', 'review_errors', 'claim_ceiling'
]
pa = {k: a.get(k) for k in keys}
pb = {k: b.get(k) for k in keys}
lanes_agree = pa == pb
classification = a.get('classification') if lanes_agree else 'INVALID_IMPLEMENTATION'
out = {
    'gate': 'ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_GATE',
    'classification': classification,
    'lanes_agree': lanes_agree,
    'decision': pa if lanes_agree else {'lane_a': pa, 'lane_b': pb},
}
canon = json.dumps(out, sort_keys=True, separators=(',', ':'))
out['aggregate_decision_sha256'] = hashlib.sha256(canon.encode()).hexdigest()
Path(args.out).parent.mkdir(parents=True, exist_ok=True)
Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
print(json.dumps({'classification': classification, 'lanes_agree': lanes_agree, 'aggregate_decision_sha256': out['aggregate_decision_sha256']}, sort_keys=True))
