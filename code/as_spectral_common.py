#!/usr/bin/env python3
"""Common source-anchored constants for Iter280 Asymptotic-Safety spectral audit."""
import json, math
from pathlib import Path

SOURCE={
 "title":"Self-consistent graviton spectral function in Lorentzian quantum gravity",
 "authors":["Jan M. Pawlowski","Manuel Reichert","Jonas Wessely"],
 "arxiv":"2507.22169v1",
 "journal":"Physics Letters B 880 (2026) 140844",
 "doi":"10.1016/j.physletb.2026.140844",
 "published":"2026-08-13"
}
A=2499.0/(380.0*math.pi)
GSTAR=760.0*math.pi/2499.0
ZSPEC=1.486
IR_A=61.0/(60.0*math.pi)
IR_TAIL=61.0/30.0

def beta(g): return 2.0*g-A*g*g

def trajectory(k,mpl=1.0):
    return GSTAR*k*k/(k*k+GSTAR*mpl*mpl)

def write_json(path,payload):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")
