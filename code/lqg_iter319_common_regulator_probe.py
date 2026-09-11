#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--subset', required=True)
a = p.parse_args()
S = tuple(sorted(int(x) for x in a.subset))
s = len(S)
if s not in (3, 4, 5) or len(set(S)) != s:
    raise SystemExit('expected a distinct K3/K4/K5 subset')
sd = s * (s - 1)
d = 3 * (s - 1)
omega = sd - d

def softplus(z):
    if z > 40:
        return z
    if z < -40:
        return math.exp(z)
    return math.log1p(math.exp(z))

def radial_integral(eps, n=24000):
    lo = -20.0
    hi = math.log(1.0 / eps)
    h = (hi - lo) / n
    total = 0.0
    for i in range(n + 1):
        y = lo + i * h
        logf = d * y - 0.5 * sd * softplus(2 * y)
        f = math.exp(logf)
        total += f * (0.5 if i in (0, n) else 1.0)
    return (eps ** (d - sd)) * total * h

eps_values = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]
vals = [radial_integral(e) for e in eps_values]
if omega == 0:
    increments = [vals[i+1] - vals[i] for i in range(len(vals)-1)]
    observed = sum(increments[-2:]) / 2.0 / math.log(10.0)
    assert abs(observed - 1.0) < 2e-3, (observed, vals)
    diagnostic = {
        'kind': 'logarithmic',
        'observed_log_coefficient': observed,
        'expected_log_coefficient': 1.0,
        'last_decade_increment': increments[-1]
    }
else:
    scaled = [v * (e ** omega) for e, v in zip(eps_values, vals)]
    asymptotic = 0.5 * math.gamma(d/2.0) * math.gamma(omega/2.0) / math.gamma(sd/2.0)
    rel = abs(scaled[-1] - asymptotic) / asymptotic
    lx = [math.log(e) for e in eps_values[-3:]]
    ly = [math.log(v) for v in vals[-3:]]
    mx = sum(lx) / 3.0
    my = sum(ly) / 3.0
    slope = sum((x-mx)*(y-my) for x,y in zip(lx,ly)) / sum((x-mx)**2 for x in lx)
    assert rel < 2e-3, (scaled[-1], asymptotic, rel)
    assert abs(slope + omega) < 2e-3, (slope, omega)
    diagnostic = {
        'kind': 'power',
        'observed_loglog_slope': slope,
        'expected_loglog_slope': -omega,
        'scaled_limit_numeric': scaled[-1],
        'scaled_limit_exact': asymptotic,
        'relative_error': rel
    }

out = {
    'iteration': 319,
    'subset': ''.join(map(str, S)),
    'size': s,
    'scaling_degree': sd,
    'relative_dimension': d,
    'omega': omega,
    'regulator': 'radial smooth proxy (r^2+eps^2)^(-sd/2)',
    'eps_values': eps_values,
    'integrals': vals,
    'diagnostic': diagnostic,
    'ordinary_eps_to_zero_limit': 'diverges',
    'prior_nonzero_witness': 'Iter317' if s in (3,4) else 'Iter307',
    'scope_guard': 'tests the local homogeneous scaling implied by the witnessed residue under a common smooth radial regulator; it does not prove equivalence to the full source spectral i-epsilon product and does not rule out a renormalized/distributional extension'
}
path = Path('build/lqg-iter319') / f"subset_{out['subset']}.json"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
print(json.dumps(out, sort_keys=True))
