#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

ap=argparse.ArgumentParser()
ap.add_argument('--a', required=True)
ap.add_argument('--b', required=True)
ap.add_argument('--out', required=True)
args=ap.parse_args()
a=json.loads(Path(args.a).read_text())
b=json.loads(Path(args.b).read_text())
match=(a['decision_projection']==b['decision_projection'] and a['decision_sha256']==b['decision_sha256'])
classification=a['decision_projection']['classification'] if match else 'INVALID_IMPLEMENTATION'
out={
  'gate':'SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_PRIMARY_SOURCE_EXPANSION_V10_GATE',
  'classification':classification,
  'lane_decision_agreement':match,
  'decision_projection':a['decision_projection'] if match else None,
  'decision_sha256':a['decision_sha256'] if match else None,
  'lane_a_controls_pass':a['decision_projection']['controls_pass'],
  'lane_b_controls_pass':b['decision_projection']['controls_pass'],
  'source_records':a['source_records'] if match else None,
  'candidate_checks':a['candidate_checks'] if match else None,
  'claim_ceiling':a['claim_ceiling'],
}
raw=json.dumps(out, indent=2, sort_keys=True)+'\n'
Path(args.out).parent.mkdir(parents=True, exist_ok=True)
Path(args.out).write_text(raw)
print(json.dumps({'classification':classification,'lane_decision_agreement':match,'decision_sha256':out['decision_sha256'],'pdf_sha256': None if not match else out['decision_projection']['pdf_sha256']}, sort_keys=True))
print('aggregate_sha256='+hashlib.sha256(raw.encode()).hexdigest())
