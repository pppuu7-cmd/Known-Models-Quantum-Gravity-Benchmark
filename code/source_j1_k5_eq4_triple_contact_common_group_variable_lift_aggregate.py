#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path
ap=argparse.ArgumentParser(); ap.add_argument('--a',required=True); ap.add_argument('--b',required=True); ap.add_argument('--out',required=True); x=ap.parse_args()
a=json.loads(Path(x.a).read_text()); b=json.loads(Path(x.b).read_text())
keys=['classification','target_triangle','required_fields','missing_fields','common_gauge_fixed_group_tuple_present','three_wedge_group_argument_maps_present','common_local_group_lie_lift_present','transverse_rank','jacobian_haar_contact_normalization_transport_present','s3_orientation_coordinate_transport_present','controls','source_facts','claim_ceiling']
pa={k:a[k] for k in keys}; pb={k:b[k] for k in keys}; lanes_agree=pa==pb
classification=a['classification'] if lanes_agree else 'INVALID_IMPLEMENTATION'
out={'gate':a['gate'],'classification':classification,'lanes_agree':lanes_agree,'decision':pa}
canon=json.dumps(out,sort_keys=True,separators=(',',':')); out['aggregate_decision_sha256']=hashlib.sha256(canon.encode()).hexdigest()
Path(x.out).parent.mkdir(parents=True,exist_ok=True); Path(x.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
