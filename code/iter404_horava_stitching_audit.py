#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AUTH=ROOT/'paper_iv/HORAVA_FRONTIER_AUTHORITY_ITER404.json'


def load():
    return json.loads(AUTH.read_text())


def audit(lane: str):
    a=load(); s=a['sources']; rules=a['prospective_rules']
    if lane=='projectable_dictionary':
        required=['explicit shared parameter dictionary','explicit common RG scale/normalization map']
        present=[]
        missing=list(required)
        return {'iteration':404,'lane':lane,'family':'HORAVA_LIFSHITZ','pass':False,'terminal':False,
                'scientific_fail':False,'present':present,'missing':missing,
                'classification':'BLOCKED_PROJECTABLE_CROSS_AUTHORITY_DICTIONARY_AND_SCALE_MAP'}
    if lane=='projectable_trajectory':
        required=['UV endpoint of IR authority matched to an allowed state of UV authority',
                  'relevant-coupling evolution attached to the same trajectory rather than spliced by analogy',
                  'uncertainty_or_truncation_error_transport']
        return {'iteration':404,'lane':lane,'family':'HORAVA_LIFSHITZ','pass':False,'terminal':False,
                'scientific_fail':False,'present':['separate UV marginal-flow authority','separate IR relevant-coupling FRG authority'],
                'missing':required,
                'classification':'BLOCKED_SAME_REALIZATION_UV_IR_STITCHING_NOT_ESTABLISHED'}
    if lane=='projectable_observable':
        return {'iteration':404,'lane':lane,'family':'HORAVA_LIFSHITZ','pass':False,'terminal':False,
                'scientific_fail':False,'present':[],
                'missing':['normalized physical extra-mode/tensor observable','identical-domain GR comparator','propagated theory/truncation errors'],
                'classification':'BLOCKED_NORMALIZED_OBSERVABLE_COMPARATOR_PACKAGE'}
    if lane=='nonprojectable_3p1':
        scope=s['nonprojectable_quantization']['scope']
        allowed=rules['nonprojectable_3p1_disposition_pass_requires_one_of']
        return {'iteration':404,'lane':lane,'family':'HORAVA_LIFSHITZ','pass':False,'terminal':False,
                'scientific_fail':False,'authority_scope':scope,'present':['non-projectable path-integral formulation','explicit 2+1 one-loop case study'],
                'missing':allowed,
                'classification':'BLOCKED_NONPROJECTABLE_3P1_DISPOSITION__2P1_CASE_STUDY_NOT_DIMENSION_TRANSFER'}
    raise ValueError(lane)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--output',required=True)
    x=ap.parse_args(); out=audit(x.lane)
    p=Path(x.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))
    # BLOCKED is a valid scientific classification, not workflow failure.

if __name__=='__main__': main()
