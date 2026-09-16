#!/usr/bin/env python3
import argparse,hashlib,json,sys
p=argparse.ArgumentParser(); p.add_argument('--source',required=True); p.add_argument('--manifest',required=True); p.add_argument('--out',required=True); a=p.parse_args()
s=json.load(open(a.source)); m=json.load(open(a.manifest)); f=s['required_field_assessment']
required=m['frozen_required_fields']
missing=[k for k in required if k not in f]
invalid=bool(missing) or not all(s['negative_controls'].values())
def authorized(status):
    return isinstance(status,str) and not status.startswith('NOT_ESTABLISHED')
blocked_fields=[]
for k in ('source_authorized_group_only_restriction_dz_zero','source_authorized_conditioning_on_fixed_z_for_contact_distribution','ten_wedge_group_only_contact_covectors'):
    if not authorized(f.get(k)): blocked_fields.append(k)
present_ok=all(authorized(f.get(k)) for k in required)
if invalid: classification='INVALID'
elif present_ok: classification='D7_S2_EQ4_K5_SIMULTANEOUS_CONTACT_COVECTOR_OBJECT_PASS_SCOPED'
else: classification='D7_S2_EQ4_K5_SIMULTANEOUS_CONTACT_COVECTOR_OBJECT_BLOCKED_SCOPED'
scientific={
 'gate':m['gate'],
 'classification':classification,
 'source_id':s['source_id'],
 'locked_pdf_sha256':s['locked_pdf_sha256'],
 'explicit_B_formula_present':f['exact_scalar_contact_function']=='PRESENT',
 'contact_distribution_full_B_z_g_present':s['facts']['contact_distribution']['assessment']=='SOURCE_DISTRIBUTION_IS_COMPOSED_WITH_FULL_B_Z_G_OBJECT',
 'joint_group_cp1_integration_domain_present':s['facts']['coherent_state_domain']['assessment']=='GROUP_AND_AUXILIARY_SPINOR_VARIABLES_ARE_SIMULTANEOUS_INTEGRATION_VARIABLES',
 'full_first_differential_defined':f['exact_full_first_differential']=='ALGEBRAICALLY_DEFINED_FROM_EXPLICIT_B_FORMULA_ON_CP1_X_SL2C',
 'group_only_dz_zero_restriction_authorized':authorized(f['source_authorized_group_only_restriction_dz_zero']),
 'fixed_z_conditioning_authorized':authorized(f['source_authorized_conditioning_on_fixed_z_for_contact_distribution']),
 'ten_wedge_group_only_contact_covectors_authorized':authorized(f['ten_wedge_group_only_contact_covectors']),
 'blocked_fields':blocked_fields,
 'minimal_missing_object':s['minimal_missing_object'],
 'negative_controls':s['negative_controls'],
 'physical_transverse_rank':None,
 'contact_covector_rank':None,
 'claim_ceiling':m['claim_ceiling']
}
b=json.dumps(scientific,sort_keys=True,separators=(',',':')).encode(); out={'scientific':scientific,'scientific_sha256':hashlib.sha256(b).hexdigest(),'valid_terminal':classification!='INVALID'}
with open(a.out,'w') as h: json.dump(out,h,sort_keys=True,indent=2); h.write('\n')
print(json.dumps(out,sort_keys=True)); sys.exit(0 if classification!='INVALID' else 2)
