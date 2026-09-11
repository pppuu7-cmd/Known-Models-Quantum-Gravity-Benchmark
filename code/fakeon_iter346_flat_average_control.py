#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path

# Independent constant-coefficient control for the source definition used in
# Piva EPJ Plus 138 (2023), eq. (5.28): fakeon tree prescription is the
# arithmetic average of retarded and advanced Green functions.

def g_ret(omega: float, t: float, tp: float) -> float:
    d=t-tp
    return math.sin(omega*d)/omega if d>0 else 0.0

def g_adv(omega: float, t: float, tp: float) -> float:
    d=t-tp
    return -math.sin(omega*d)/omega if d<0 else 0.0

def g_fakeon(omega: float, t: float, tp: float) -> float:
    return 0.5*(g_ret(omega,t,tp)+g_adv(omega,t,tp))

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--omega',type=float,required=True)
    ap.add_argument('--output',required=True)
    a=ap.parse_args()
    if a.omega<=0: raise ValueError('omega must be positive')
    dts=[0.137,0.431,0.773]
    rows=[]
    min_future=1e300
    max_average_identity=0.0
    max_time_symmetry=0.0
    for dt in dts:
        past=g_fakeon(a.omega,0.0,-dt)
        future=g_fakeon(a.omega,0.0,+dt)
        ret_future=g_ret(a.omega,0.0,+dt)
        adv_future=g_adv(a.omega,0.0,+dt)
        identity=abs(future-0.5*(ret_future+adv_future))
        symmetry=abs(future-past)
        min_future=min(min_future,abs(future))
        max_average_identity=max(max_average_identity,identity)
        max_time_symmetry=max(max_time_symmetry,symmetry)
        rows.append({'delta_t':dt,'fakeon_past':past,'fakeon_future':future,'retarded_future':ret_future,'advanced_future':adv_future,'average_identity_residual':identity,'time_symmetric_residual':symmetry})
    assert min_future>1e-8,min_future
    assert max_average_identity<1e-15,max_average_identity
    assert max_time_symmetry<1e-15,max_time_symmetry
    assert all(r['retarded_future']==0.0 for r in rows)
    out={
      'iteration':346,'omega':a.omega,'probe_count':len(rows),'probes':rows,
      'minimum_fakeon_future_abs':min_future,
      'maximum_average_identity_residual':max_average_identity,
      'maximum_time_symmetric_residual':max_time_symmetry,
      'classification':'PASS_SCOPED_FLAT_CONSTANT_COEFFICIENT_CONTROL__FAKEON_HALF_RETARDED_PLUS_HALF_ADVANCED_RESPONSE_IS_TIME_SYMMETRIC_AND_HAS_NONZERO_FUTURE_SUPPORT',
      'scope_guard':['CONTROL_PROBLEM_FOR_TREE_LEVEL_FAKEON_PRESCRIPTION','NOT_FULL_GRAVITY','NOT_PARENT_FAMILY_TERMINAL','NO_D7_PROMOTION']
    }
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))

if __name__=='__main__': main()
