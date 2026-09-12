#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TERMINAL={'BENCHMARKED_COMPLETE_REALIZATION','EQUIVALENCE_CLASS_CLOSED_BY_THEOREM','MERGED_INTO_OTHER_ROW_WITH_EXPLICIT_REDUCTION_MAP','OUTSIDE_PAPER_IV_TARGET_WITH_SCOPE_PROOF'}

def branch_map():
    p=json.loads((ROOT/'paper_iv/HIGHER_DERIVATIVE_QUANTIZATION_BRANCH_MAP_V2_ITER399.json').read_text())
    branches=p['material_branches']; ids=[b['id'] for b in branches]
    iho=next(b for b in branches if b['id']=='IHO_DQFT_SPACELIKE_PV')
    full=iho['full_minimum_payload_slots']; partial=iho['partial_or_open_minimum_payload_slots']
    ok=(len(branches)==6 and len(ids)==len(set(ids)) and len(full)==5 and len(partial)==5 and not iho['terminal'] and not p['family_effect']['family_terminal'])
    return {
      'mode':'branch_map_v2','iteration':399,'material_branch_count':len(branches),'unique_branch_ids':len(set(ids)),
      'iho_present':True,'iho_full_slots':len(full),'iho_partial_open_slots':len(partial),
      'family_terminal':p['family_effect']['family_terminal'],'pass':ok,
      'classification':'PASS_HIGHER_DERIVATIVE_SIX_BRANCH_COHERENCE__IHO_EXPLICIT__FAMILY_REMAINS_PARTIAL' if ok else 'FAIL_BRANCH_MAP_V2_COHERENCE'
    }

def source_family(family):
    a=json.loads((ROOT/'paper_iv/PARALLEL_SOURCE_CLOSURE_AUTHORITY_ITER400_403.json').read_text())
    f=a['families'][family]
    cov=json.loads((ROOT/'protocol/PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json').read_text())
    row=next(r for r in cov['tier1_required_rows'] if r['id']==family)
    terminal_before=row['coverage_status'] in TERMINAL
    terminal_found=bool(f['terminal_object_found'])
    status=f['status']
    if family=='HORAVA_LIFSHITZ': route='MIXED_SOURCE_AND_REDUCTION__PROJECTABLE_RELEVANT_IR_BRIDGE_PLUS_NONPROJECTABLE_3P1_DISPOSITION'
    elif family=='CDT_EDT': route='EXTERNAL_DATA_AND_COMPUTE_CAPSULE__MULTICOUPLING_CONTINUUM_SCALE_SETTING_ERRORS'
    elif family=='GFT_TENSOR_MODELS': route='REDUCTION_OR_INDEPENDENT_OBSERVABLE__TGFT_REMAINDER'
    elif family=='STRING_MTHEORY_HOLOGRAPHY': route='SOURCE_CENSUS_AND_EQUIVALENCE__COMPACTIFICATION_SUBFAMILY_EXHAUSTION'
    else: raise ValueError(family)
    return {
      'mode':'source_family','iteration':400,'family':family,'coverage_status_before':row['coverage_status'],
      'terminal_before':terminal_before,'terminal_object_found_in_new_authority':terminal_found,
      'source_update_status':status,'next_route':route,'required_gate':f['required_gate'],
      'terminal_after':terminal_before or terminal_found,'scientific_fail':False,'pass':not terminal_found and not terminal_before,
      'classification':'PASS_SOURCE_REAUDIT__NO_TERMINAL_PROMOTION__BLOCKER_REFINED'
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',required=True,choices=['branch','family']); ap.add_argument('--family'); ap.add_argument('--output',required=True); x=ap.parse_args()
    out=branch_map() if x.mode=='branch' else source_family(x.family)
    p=Path(x.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))
    if not out['pass']: raise SystemExit(2)
if __name__=='__main__': main()
