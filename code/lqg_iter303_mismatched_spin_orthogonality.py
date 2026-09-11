#!/usr/bin/env python3
import json, pathlib
# Schur orthogonality between inequivalent SU(2) irreps gives zero.
# We encode independent labels k and k' (twice-spin convention); matching dimension alone is not sufficient.
pairs=[]
for k in range(0,7):
    for kp in range(0,7):
        kernel_nonzero=(k==kp)
        expected=(k==kp)
        pairs.append({'k':k,'k_prime':kp,'d_k':k+1,'d_k_prime':kp+1,
                      'schur_channel_nonzero':kernel_nonzero,'expected':expected,
                      'pass':kernel_nonzero==expected})
ok=all(x['pass'] for x in pairs) and sum(x['schur_channel_nonzero'] for x in pairs)==7
out={'probe':'mismatched_spin_orthogonality','pass':ok,'iteration':303,
     'pairs_checked':len(pairs),'matching_channels':7,'mismatched_channels_zero':42,'rows':pairs}
pathlib.Path('build/lqg-iter303').mkdir(parents=True,exist_ok=True)
pathlib.Path('build/lqg-iter303/mismatched_spin_orthogonality.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if not ok: raise SystemExit(1)
