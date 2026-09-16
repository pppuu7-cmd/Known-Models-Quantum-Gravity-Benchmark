#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, itertools, json
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import source_j1_k5_highest_contact_magnetic_leading_transfer_v4 as base

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/'inputs/source_j1_k5_highest_contact_magnetic_leading_transfer_v4.json'
PREREG='d30274a74e206287b5dc3cf9cba02fa66e13c74b'

def canon(x):
    if isinstance(x,F): return f'{x.numerator}/{x.denominator}'
    return str(x)

def main(out):
    data=json.loads(INPUT.read_text())
    cart=base.cartesian_intertwiners()
    X=[tuple(F(x) for x in p) for p in data['tangent_points_zero_based']]
    mats=[]
    for a,b in base.EDGES:
        v=tuple(X[a][q]-X[b][q] for q in range(3))
        mats.append(base.Q(v))
    path=base.contraction_path(cart)
    channels=list(itertools.product(range(3), repeat=5))
    complete=(len(channels)==243 and len(set(channels))==243 and channels==sorted(channels))
    vals={''.join(map(str,c)):canon(base.contract(cart,mats,c,path)) for c in channels}
    lock=(vals['00000']=='11/24')
    nonzero=[k for k,v in vals.items() if v not in ('0','0/1')]
    z=np.empty((3,3),dtype=object)
    for idx in np.ndindex(z.shape): z[idx]=F(0)
    zm=list(mats); zm[0]=z
    neg={''.join(map(str,c)):canon(base.contract(cart,zm,c,path)) for c in channels}
    negative_ok=all(v in ('0','0/1') for v in neg.values())
    payload='\n'.join(f'{k}={vals[k]}' for k in sorted(vals))
    digest=hashlib.sha256(payload.encode()).hexdigest()
    controls={'channel_00000_lock':lock,'enumeration_complete':complete,'zero_edge_negative':negative_ok}
    classification='CHANNEL_COVERAGE_NONZERO_SCOPED' if all(controls.values()) and nonzero else 'INVALID_IMPLEMENTATION'
    result={'gate':'SOURCE_J1_K5_CHANNEL_COVERAGE_V5','prereg_commit':PREREG,'classification':classification,'controls':controls,'total_channels':243,'nonzero_count':len(nonzero),'zero_count':243-len(nonzero),'channel_map_sha256':digest,'channel_00000':vals['00000'],'nonzero_channels':nonzero,'channel_map':vals,'claim_ceiling':'finite same-tangent j=1 channel coverage only; no D7 closure or terminal selector'}
    Path(out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:result[k] for k in ('classification','nonzero_count','zero_count','channel_map_sha256','channel_00000')},indent=2))
    return 0 if classification!='INVALID_IMPLEMENTATION' else 2

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); a=ap.parse_args(); raise SystemExit(main(a.out))
