#!/usr/bin/env python3
import argparse, math
from lqg_entropy_observable_common import HAN_ENTROPY_2026,bh_ratio,write_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); a=ap.parse_args()
    gammas=[0.05,0.10,0.25,0.50]
    rows=[]
    ok=True
    for g in gammas:
        beta=math.pi*g
        ratio=bh_ratio(g,beta)
        err=abs(ratio-0.25)
        rows.append({'gamma':g,'beta_required':beta,'S_over_A_lP2':ratio,'abs_error':err})
        ok &= err < 1e-15
    ok &= HAN_ENTROPY_2026['bh_formula_reproduced_with_coupling_gamma_relation']
    write_json(a.output,{
      'probe':'lqg_entropy_bh_normalization_probe','pass':bool(ok),'rows':rows,
      'classification':'PASS_SCOPED_BH_NORMALIZATION_IDENTITY_BETA_EQUALS_PI_GAMMA' if ok else 'FAIL_BH_NORMALIZATION_IDENTITY',
      'boundary':'Algebraic normalization check only; it does not derive the coupling-to-gamma selection rule.'})
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()
