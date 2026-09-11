#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

root = Path('build/lqg-iter320-results')
files = sorted(root.glob('chain_*.json'))
if len(files) != 20:
    raise SystemExit(f'expected 20 maximal-chain artifacts, got {len(files)}')
rows = [json.loads(p.read_text()) for p in files]
chains = {r['chain'] for r in rows}
expected = set()
verts = set(range(5))
import itertools
for k4 in itertools.combinations(range(5),4):
    for k3 in itertools.combinations(k4,3):
        expected.add(''.join(map(str,k3)) + '_' + ''.join(map(str,k4)))
assert chains == expected, (len(chains), len(expected), sorted(expected-chains), sorted(chains-expected))
assert all(r['all_positive_joint_cutoff_paths_tested_diverge'] for r in rows)
assert all(r['shell_exponents'] == {'lambda':-9,'mu':-4,'nu':-1} for r in rows)
max_err = 0.0
for r in rows:
    for v in r['path_results'].values():
        max_err=max(max_err,abs(v['observed_power_after_log_removal']-v['expected_power_after_log_removal']))
assert max_err < 2e-3
summary = {
    'iteration': 320,
    'maximal_nested_chains_K3_K4_K5': 20,
    'all_chains_passed': True,
    'tested_joint_cutoff_paths_per_chain': 5,
    'total_path_probes': 100,
    'nested_shell_density': 'lambda^-9 * mu^-4 * nu^-1 d(lambda)d(mu)d(nu)',
    'cumulative_divergence_degrees': {'K3':0,'K4':3,'K5':8},
    'maximum_power_fit_error_after_log_removal': max_err,
    'classification': 'all 20 maximal K3<K4<K5 forests retain simultaneous multiscale divergence under all five positive common-cutoff paths; a finite ordinary joint cutoff limit is not obtained',
    'source_prescription_gap': 'Eq.(3) defines individual Toller boundary values and Eq.(4) multiplies them; Iter320 does not identify an explicit forest subtraction/extension condition that would fix all nested/overlap extensions',
    'scope_guard': 'The result is a nested-sector scaling theorem/probe for already witnessed nonzero residues. It does not exclude a mathematically well-defined source-consistent distributional extension and is not a family-level FAIL or D7 authorization.'
}
out=Path('build/lqg-iter320-summary.json')
out.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
h=hashlib.sha256(out.read_bytes()).hexdigest()
Path('build/lqg-iter320-summary.sha256').write_text(h+'  '+out.name+'\n')
print(json.dumps(summary,sort_keys=True))
