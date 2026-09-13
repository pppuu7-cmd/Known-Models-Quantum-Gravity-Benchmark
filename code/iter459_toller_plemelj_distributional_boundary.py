import argparse, json, math, os
import numpy as np
from scipy.integrate import quad

R = 12.0
EPS = (0.20, 0.10, 0.05, 0.025, 0.0125)
PANEL = {
    "R035_G0": (0.35, 0),
    "R035_G1": (0.35, 1),
    "R035_G2": (0.35, 2),
    "R160_G0": (1.60, 0),
    "R160_G1": (1.60, 1),
    "R160_G2": (1.60, 2),
}

def phi(k, x):
    if k == 0:
        return math.exp(-x*x)
    if k == 1:
        return (1.0 + 0.3*x) * math.exp(-0.7*x*x)
    if k == 2:
        return math.cos(1.1*x) * math.exp(-0.4*x*x)
    raise ValueError(k)

def relerr(a, b):
    return abs(a-b) / max(1.0, abs(b))

def finite_eps(rho, k, eps, s):
    # Published displacement object: 1/(x-rho-i*s*eps).
    def re(x):
        y = x-rho
        p = phi(k, x)
        return p*y/(y*y+eps*eps)
    def im(x):
        y = x-rho
        p = phi(k, x)
        return p*s*eps/(y*y+eps*eps)
    rv = quad(re, -R, R, epsabs=2e-11, epsrel=2e-11, limit=600, points=[rho])[0]
    iv = quad(im, -R, R, epsabs=2e-11, epsrel=2e-11, limit=600, points=[rho])[0]
    return complex(rv, iv)

def pv_weighted(rho, k):
    return quad(lambda x: phi(k, x), -R, R, weight='cauchy', wvar=rho,
                epsabs=2e-11, epsrel=2e-11, limit=600)[0]

def pv_subtracted(rho, k):
    p0 = phi(k, rho)
    def f(x):
        y = x-rho
        if abs(y) < 1e-8:
            h = 2e-6
            return (phi(k, rho+h)-phi(k, rho-h))/(2*h)
        return (phi(k, x)-p0)/y
    regular = quad(f, -R, R, epsabs=2e-11, epsrel=2e-11, limit=600, points=[rho])[0]
    const = p0 * math.log((R-rho)/(R+rho))
    return regular + const

def lane(name):
    rho, k = PANEL[name]
    p0 = phi(k, rho)
    pva = pv_weighted(rho, k)
    pvb = pv_subtracted(rho, k)
    pv_agreement = abs(pva-pvb)
    records = []
    finite_ok = True
    boundary_ok = True
    trend_ok = True
    cauchy_ok = True
    pref_ok = True
    wrong_ok = True
    for s in (+1, -1):
        target = complex(pva, s*math.pi*p0)
        vals = [finite_eps(rho, k, e, s) for e in EPS]
        finite_ok &= all(np.isfinite(v.real) and np.isfinite(v.imag) for v in vals)
        errs = [relerr(v, target) for v in vals]
        final_err = errs[-1]
        ratio = final_err / max(errs[0], 1e-300)
        last_change = relerr(vals[-1], vals[-2])
        boundary_ok &= final_err <= 3e-2
        trend_ok &= ratio <= 0.35
        cauchy_ok &= last_change <= 3e-2
        source_from_raw = s*target/(2j*math.pi)
        source_split = s*pva/(2j*math.pi) + 0.5*p0
        pref_resid = abs(source_from_raw-source_split)
        pref_ok &= pref_resid <= 1e-12
        wrong = complex(pva, -s*math.pi*p0)
        wrong_sep = relerr(wrong, target)
        wrong_ok &= wrong_sep >= 5e-2
        records.append({
            'sign': s,
            'errors': errs,
            'final_error': final_err,
            'final_to_initial_ratio': ratio,
            'last_halving_change': last_change,
            'source_prefactor_residual': pref_resid,
            'wrong_delta_sign_separation': wrong_sep,
            'final_value': [vals[-1].real, vals[-1].imag],
            'target': [target.real, target.imag],
        })
    tests = {
        'finite_complete': bool(finite_ok),
        'independent_pv_agreement': bool(pv_agreement <= 2e-9),
        'boundary_value_final_error': bool(boundary_ok),
        'clear_epsilon_approach': bool(trend_ok),
        'last_halving_cauchy': bool(cauchy_ok),
        'source_prefactor_consistency': bool(pref_ok),
        'wrong_delta_sign_negative_control': bool(wrong_ok),
    }
    passed = all(tests.values())
    return {
        'lane': name,
        'rho': rho,
        'test_function': k,
        'pv_weighted': pva,
        'pv_subtracted': pvb,
        'pv_route_abs_difference': pv_agreement,
        'phi_at_rho': p0,
        'records': records,
        'tests': tests,
        'valid': bool(finite_ok and np.isfinite(pva) and np.isfinite(pvb)),
        'pass': bool(passed),
        'classification': ('ITER459_TOLLER_PLEMELJ_DISTRIBUTIONAL_KERNEL_QUALIFIED_SCOPED'
                           if passed else 'SCIENTIFIC_FAIL_ITER459_TOLLER_PLEMELJ_DISTRIBUTIONAL_PANEL')
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lane', required=True, choices=sorted(PANEL))
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    try:
        q = lane(a.lane)
    except Exception as e:
        q = {'lane': a.lane, 'valid': False, 'pass': False,
             'classification': 'INFRASTRUCTURE_OR_NUMERICAL_FAIL', 'error': repr(e)}
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    with open(a.out, 'w') as f:
        json.dump(q, f, indent=2)
    print(json.dumps(q, indent=2))

if __name__ == '__main__':
    main()
