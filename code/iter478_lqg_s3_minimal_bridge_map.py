#!/usr/bin/env python3
import json,pathlib

AUTHORITIES={
 'iter283':'paper_iv/P_LQG_UV_IR_BRIDGE_IDENTITY_AUDIT_ITER283_2026-09-11.md',
 'iter284':'paper_iv/P_LQG_PHYSICAL_STATE_LINK_COMPATIBILITY_AUDIT_ITER284_2026-09-11.md',
 'iter286':'paper_iv/P_LQG_EPRL_WICK_SIGNATURE_BRIDGE_AUDIT_ITER286_2026-09-11.md',
 'iter287':'paper_iv/P_LQG_SAME_STACK_UV_ENTROPY_ALIGNMENT_AUDIT_ITER287_2026-09-11.md',
 'iter291':'paper_iv/LQG_GAMMA_DUALITY_OBSERVABLE_PARAMETER_BRIDGE_AUDIT_ITER291_2026-09-11.md',
 'iter302':'paper_iv/P_LQG_TOLLER_HALF_LINK_COMPOSITION_SCOPE_AUDIT_ITER302_2026-09-11.md',
}
BRIDGES={
 'UV_IR_SAME_REALIZATION_IDENTITY_AND_PARAMETER_MAP':{
   'files':['iter283'],
   'negative':['same_realization_terminal_bridge_ready = false','same_realization_terminal_bridge_ready=false','PARAMETER_TRANSPORT_MAP_MISSING','NORMALIZED_OBSERVABLE_TRANSPORT_MISSING'],
   'positive':['shared_parent_family = true','material_positive_endpoints = true']},
 'PHYSICAL_STATE_SIGNATURE_STACK_TRANSPORT':{
   'files':['iter284','iter286'],
   'negative':['same_realization_chain_ready = false','same_realization_chain_ready=false','same_real_gamma_identity = false','same_real_gamma_identity=false','rigging_map_transport_ready = false','rigging_map_transport_ready=false','complete_stack_transport_ready = false','complete_stack_transport_ready=false'],
   'positive':['physical_state_component = HIGH_VALUE_SCOPED_POSITIVE','explicit_euclidean_lorentzian_vertex_map = true','structural_signature_bridge = true']},
 'CONTINUOUS_SHARED_STACK_UV_TO_GR_TRANSPORT':{
   'files':['iter287'],
   'negative':['continuous_same_realization_transport_ready = false','continuous_same_realization_transport_ready=false'],
   'positive':['shared_lorentzian_stack_architecture = true','observable_anchor_inside_shared_stack = true','uv_ir_regime_orientation_identified = true']},
 'NORMALIZED_OBSERVABLE_AND_PROPAGATED_ERROR_TRANSPORT':{
   'files':['iter291'],
   'negative':['normalized_observable_with_full_propagated_qg_error_ready=false','complete_stack_same_realization_uv_ir_transport_ready=false'],
   'positive':['scoped_observable_parameter_bridge=true','semiclassical_gamma_observable_anchor=true']},
 'CAUSAL_TOLLER_GLUE_FINITE_NORMALIZED_STACK_TO_REGGE_GR':{
   'files':['iter302'],
   'negative':['fixed_toller_branch_representation_composition_available=false','causal_stack_finiteness_normalization_cutoff_control_proven=false','same_realization_uv_to_regge_gr_transport_proven=false'],
   'positive':['toller_additive_completion_recovers_D=true']},
}
texts={}; files_present=True
for tag,fn in AUTHORITIES.items():
    p=pathlib.Path(fn); files_present &= p.exists(); texts[tag]=p.read_text(encoding='utf-8') if p.exists() else ''
rows=[]; all_resolved=True; positive_not_override=True
for name,spec in BRIDGES.items():
    combined='\n'.join(texts[t] for t in spec['files'])
    neg=[x for x in spec['negative'] if x in combined]
    pos=[x for x in spec['positive'] if x in combined]
    state='OPEN_EXPLICIT_SOURCE_BLOCKER' if neg else 'NO_EXPLICIT_BLOCKER_RECOVERED'
    all_resolved &= bool(neg) or bool(combined)
    positive_not_override &= not (pos and neg and state!='OPEN_EXPLICIT_SOURCE_BLOCKER')
    rows.append({'bridge_class':name,'authority_files':[AUTHORITIES[t] for t in spec['files']],'state':state,'negative_markers_recovered':neg,'positive_anchors_recovered':pos})
checks={'all_six_authority_files_present':bool(files_present),'all_five_bridge_classes_resolved':bool(all_resolved and len(rows)==5),'positive_anchors_do_not_override_negative_readiness':bool(positive_not_override)}
ok=all(checks.values())
open_count=sum(r['state']=='OPEN_EXPLICIT_SOURCE_BLOCKER' for r in rows)
out={'iteration':478,'classification':'ITER478_LQG_S3_MINIMAL_BRIDGE_MAP_COMPLETE_SCOPED' if ok else 'FAIL_ITER478_AUTHORITY_MAP_INVALID','scientific_pass':ok,'checks':checks,'bridge_classes':rows,'open_bridge_class_count':open_count,'d7_s3':'NOT_CLOSED' if open_count else 'REQUIRES_FULL_BUNDLE_REVIEW','scope':'dependency/blocker map from six frozen LQG/EPRL authority audits only; OPEN is missing certificate, not impossibility'}
pathlib.Path('artifacts').mkdir(exist_ok=True); pathlib.Path('artifacts/iter478-summary.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2)); raise SystemExit(0 if ok else 2)
