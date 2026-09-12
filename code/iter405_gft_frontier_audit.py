#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def audit(lane):
    if lane=='reduction_scope':
        return {'iteration':405,'lane':lane,'pass':False,'terminal':False,'scientific_fail':False,'present':['scoped covariant GFT -> spin-foam amplitude correspondence'],'missing':['explicit maps for all material TGFT/GFT remainders','family-scope exhaustion proof'],'classification':'BLOCKED_SCOPED_REDUCTION_NOT_FAMILY_EQUIVALENCE'}
    if lane=='identity_doublecount':
        return {'iteration':405,'lane':lane,'pass':False,'terminal':False,'scientific_fail':False,'present':['selected amplitude-level correspondence'],'missing':['state/amplitude/observable identity map','parameter and normalization identity','double-counting control across represented and independent branches'],'classification':'BLOCKED_REDUCTION_IDENTITY_AND_DOUBLE_COUNTING_CONTROL'}
    if lane=='tgft_gravity_observable':
        return {'iteration':405,'lane':lane,'pass':False,'terminal':False,'scientific_fail':False,'present':['specific TGFT continuum/condensate evidence'],'missing':['frozen independent TGFT parent through Lorentzian gravity regime','normalized non-cosmology-only gravity observable','same-domain GR/EFT comparator','propagated errors'],'classification':'BLOCKED_TGFT_INDEPENDENT_GRAVITY_OBSERVABLE_COMPARATOR'}
    if lane=='continuum_transfer':
        return {'iteration':405,'lane':lane,'pass':False,'terminal':False,'scientific_fail':False,'present':['spin-foam continuum structural authority'],'missing':['explicit theorem transferring that continuum construction to the independent TGFT remainder'],'classification':'BLOCKED_SPINFOAM_CONTINUUM_RESULT_NOT_AUTOMATIC_TGFT_REDUCTION'}
    raise ValueError(lane)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--output',required=True); x=ap.parse_args()
    out=audit(x.lane); p=Path(x.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
