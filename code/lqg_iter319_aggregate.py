#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

root = Path('build/lqg-iter319-results')
files = sorted(root.glob('subset_*.json'))
if len(files) != 16:
    raise SystemExit(f'expected 16 regulator artifacts, got {len(files)}')
rows = [json.loads(p.read_text()) for p in files]
counts = {s: sum(r['size'] == s for r in rows) for s in (3,4,5)}
assert counts == {3:10,4:5,5:1}
assert all(r['ordinary_eps_to_zero_limit'] == 'diverges' for r in rows)
assert all(r['omega'] == {3:0,4:3,5:8}[r['size']] for r in rows)

k3 = [r['diagnostic']['observed_log_coefficient'] for r in rows if r['size']==3]
k4 = [r['diagnostic']['observed_loglog_slope'] for r in rows if r['size']==4]
k5 = [r['diagnostic']['observed_loglog_slope'] for r in rows if r['size']==5]
summary = {
    'iteration':319,
    'jobs':16,
    'strata_by_size':counts,
    'common_radial_regulator_results': {
        'K3': {'expected':'log(1/eps)','mean_observed_log_coefficient':sum(k3)/len(k3)},
        'K4': {'expected':'eps^-3','mean_observed_loglog_slope':sum(k4)/len(k4)},
        'K5': {'expected':'eps^-8','mean_observed_loglog_slope':sum(k5)/len(k5)}
    },
    'classification':'the witnessed local homogeneous singularities do not acquire a finite ordinary epsilon-to-zero limit under this common smooth radial regulator; explicit extension/subtraction data remain necessary in this proxy test',
    'scope_guard':'this is a regulator stress test of scaling-degree behavior, not a proof that the exact source spectral i-epsilon product has no canonical distributional boundary value; a dedicated joint source-prescription audit remains required'
}
out = Path('build/lqg-iter319-summary.json')
out.write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
h = hashlib.sha256(out.read_bytes()).hexdigest()
Path('build/lqg-iter319-summary.sha256').write_text(h + '  ' + out.name + '\n')
print(json.dumps(summary, sort_keys=True))
