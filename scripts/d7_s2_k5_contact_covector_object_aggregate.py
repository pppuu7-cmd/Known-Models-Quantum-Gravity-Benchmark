#!/usr/bin/env python3
import argparse,hashlib,json,sys
p=argparse.ArgumentParser(); p.add_argument('--a',required=True); p.add_argument('--b',required=True); p.add_argument('--out',required=True); x=p.parse_args()
a=json.load(open(x.a)); b=json.load(open(x.b))
sa=a['scientific']; sb=b['scientific']; keys=['classification','source_id','locked_pdf_sha256','explicit_B_formula_present','contact_distribution_full_B_z_g_present','joint_group_cp1_integration_domain_present','full_first_differential_defined','group_only_dz_zero_restriction_authorized','fixed_z_conditioning_authorized','ten_wedge_group_only_contact_covectors_authorized','blocked_fields','minimal_missing_object','physical_transverse_rank','contact_covector_rank','claim_ceiling']
agree=all(sa[k]==sb[k] for k in keys) and a['scientific_sha256']==b['scientific_sha256']
valid=agree and a['valid_terminal'] and b['valid_terminal']
scientific={k:sa[k] for k in keys}; scientific['lanes_agree']=agree; scientific['negative_controls']=sa['negative_controls']
payload=json.dumps(scientific,sort_keys=True,separators=(',',':')).encode(); out={'valid':valid,'scientific':scientific,'scientific_sha256':hashlib.sha256(payload).hexdigest(),'lane_scientific_sha256':[a['scientific_sha256'],b['scientific_sha256']]}
with open(x.out,'w') as h: json.dump(out,h,sort_keys=True,indent=2); h.write('\n')
print(json.dumps(out,sort_keys=True)); sys.exit(0 if valid else 2)
