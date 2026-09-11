#!/usr/bin/env python3
import json, pathlib
p=json.load(open('benchmarks/lqg_iter314_cplus_cminus_noncausal_cancellation.json'))
c=p['prospectively_frozen_claims']
ok=(c['cplus_plus_cminus_k3_sum']==0 and c['cplus_plus_cminus_k4_sum']==0 and c['cplus_plus_cminus_k5_sum']==32 and
    c['unrestricted_eprl_k5_sum']==0 and c['noncausal_k5_sum']==-32 and
    not c['cplus_plus_cminus_restores_full_k5_leading_cancellation'] and
    c['noncausal_sector_is_required_for_full_k5_scalar_sign_cancellation'] and
    not c['full_tensor_residue_cancellation_proven'] and not c['family_terminal'] and not c['d7_authorized'])
out={'probe':'scope_guard','pass':bool(ok),'iteration':314,
     'proven_scope':'at scalar minimal-spin leading-sign level, C+ plus C- cancels K3 but leaves K5 +32; the 992 noncausal sectors supply -32 in the unrestricted EPRL sum',
     'not_proven':['full angular/intertwiner K3 residue cancellation','full tensor K5 cancellation or divergence','nonexistence of a renormalized causal+co-causal model','family terminality','D7 authorization'],
     'next_required':'compute exact contracted partial-diagonal residues and determine whether a causal-only renormalization can be fixed without reintroducing the noncausal EPRL sector'}
pathlib.Path('build/lqg-iter314').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter314/scope_guard.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
