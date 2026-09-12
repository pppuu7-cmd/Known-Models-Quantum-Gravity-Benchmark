#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path

FACTS={
 'erg_contact': {
  'date':'2026-09-03','linked_paper':'2603.10168','same_lead_author':True,'contact_resummed_lorentzian_claim':True,
  'cross_section_gr_ir_claim':True,'cross_section_uv_unitarity_claim':True,'formula_payload_machine_retrieved':False
 },
 'march_v1': {
  'source':'2603.10168v1','submitted':'2026-03-10','identical_scalar':True,'mediated_stu_present':True,
  'direct_A4_included':False,'direct_A4_explicit_future_work':True
 },
 'spectral': {
  'source':'2606.19321v1','submitted':'2026-06-17','lorentzian_KL':True,'normalisable_spectral_functions':True,
  'IR_EFT_match':True,'effective_action_R2':True,'explicit_map_to_contact_scattering_realization':False
 },
 'distinct_contact': {
  'source':'2602.21285','two_species_process':True,'process':'phi phi -> chi chi',
  'same_as_identical_scalar_2603_10168':False
 }
}

def dump(x,p):
 Path(p).parent.mkdir(parents=True,exist_ok=True); Path(p).write_text(json.dumps(x,indent=2,sort_keys=True)+'\n',encoding='utf-8'); print(json.dumps(x,sort_keys=True))
 if not x.get('pass',False): raise SystemExit(2)

def evidence(name):
 if name=='contact_claim':
  f=FACTS['erg_contact']; ok=f['contact_resummed_lorentzian_claim'] and f['same_lead_author'] and f['linked_paper']=='2603.10168'
  c='PASS_PUBLIC_ERG2026_CONTACT_RESUMMATION_CLAIM_ADMITTED__FORMULA_PAYLOAD_PENDING'
 elif name=='observable_claim':
  f=FACTS['erg_contact']; ok=f['cross_section_gr_ir_claim'] and f['cross_section_uv_unitarity_claim']
  c='PASS_PUBLIC_ERG2026_IR_GR_AND_UV_UNITARITY_OBSERVABLE_CLAIM_ADMITTED__NUMERIC_LEDGER_PENDING'
 elif name=='preprint_delta':
  a=FACTS['march_v1']; b=FACTS['erg_contact']; f={'march_v1':a,'erg2026':b}
  ok=a['direct_A4_explicit_future_work'] and b['contact_resummed_lorentzian_claim'] and b['date']>'2026-03-10'
  c='PASS_MATERIAL_POST_V1_CONTACT_PROGRESS_DETECTED'
 elif name=='spectral_authority':
  f=FACTS['spectral']; ok=f['lorentzian_KL'] and f['normalisable_spectral_functions'] and f['IR_EFT_match'] and f['effective_action_R2']
  c='PASS_INDEPENDENT_LORENTZIAN_SPECTRAL_AUTHORITY_ADMITTED'
 elif name=='payload_guard':
  f=FACTS['erg_contact']; ok=(f['formula_payload_machine_retrieved'] is False)
  c='PASS_FAIL_CLOSED_CONTACT_FORMULA_PAYLOAD_GUARD'
 else: raise ValueError(name)
 return {'iteration':409,'stream':'ASYMPTOTIC_SAFETY','probe':name,'pass':ok,'classification':c,'facts':f,
         'terminal':False,'d7_promotion':False}

def composition():
 a=FACTS['erg_contact']; s=FACTS['spectral']; d=FACTS['distinct_contact']
 ok=(not a['formula_payload_machine_retrieved']) and (not s['explicit_map_to_contact_scattering_realization']) and (not d['same_as_identical_scalar_2603_10168'])
 return {'iteration':410,'stream':'ASYMPTOTIC_SAFETY','probe':'same_realization_composition_guard','pass':ok,
  'classification':'PASS_FAIL_CLOSED_COMPOSITION__ERG_CONTACT_REOPENS_FRONT_BUT_SPECTRAL_AND_DISTINCT_CONTACT_AUTHORITIES_NOT_SILENTLY_SPLICED',
  'guards':{'erg_formula_payload_missing':not a['formula_payload_machine_retrieved'],
            'spectral_to_scattering_explicit_map_missing':not s['explicit_map_to_contact_scattering_realization'],
            'knorr_contact_process_distinct':not d['same_as_identical_scalar_2603_10168']},
  'terminal':False,'d7_promotion':False}

def aggregate(root):
 rows=[json.loads(p.read_text()) for p in Path(root).rglob('*.json')]
 names=sorted(r['probe'] for r in rows)
 expected=sorted(['contact_claim','observable_claim','preprint_delta','spectral_authority','payload_guard','same_realization_composition_guard'])
 ok=len(rows)==6 and names==expected and all(r.get('pass') for r in rows)
 return {'iteration_bundle':'409-411','pass':ok,'independent_result_count':len(rows),'probes':names,
  'classification':'PASS_AS_ERG2026_CONTACT_FRONT_REOPENED__MATERIAL_PUBLIC_PROGRESS__FORMULA_ERROR_LEDGER_AND_SAME_REALIZATION_COMPOSITION_STILL_OPEN',
  'contact_front_reopened':True,'contact_complete_terminal_certificate':False,
  'required_next_object':'MACHINE_READABLE_ERG2026_CONTACT_AMPLITUDE_FORMULA_OR_UPDATED_PUBLICATION_PLUS_SAME_REALIZATION_PARAMETER_APPROXIMATION_AND_ERROR_LEDGER',
  'D2':'NOT_CLOSED_COVERAGE_AND_OBJECTS','D4':'PARTIAL_GLOBAL_NOT_CLOSED','D7':'NOT_CLOSED_NOT_YET_AUTHORIZED',
  'candidate_gravity_activation':False,'new_required_authorized':False}

def main():
 p=argparse.ArgumentParser(); p.add_argument('--mode',choices=['evidence','composition','aggregate'],required=True); p.add_argument('--probe'); p.add_argument('--input-dir'); p.add_argument('--output',required=True); a=p.parse_args()
 if a.mode=='evidence': out=evidence(a.probe)
 elif a.mode=='composition': out=composition()
 else: out=aggregate(a.input_dir)
 dump(out,a.output)
if __name__=='__main__': main()
