#!/usr/bin/env python3
"""Iter429: EPRL asymptotic scaling/resource-closure audit.

Source authority: Bianchi & Ding, arXiv:1109.6538v2, Sec. V.4,
especially Eqs. (98)-(100) and the preceding Hessian scaling:
  H_rest = j (H^epsilon + O(gamma)),
  H_rest^{-1} = j^{-1} ((H^epsilon)^{-1} + O(gamma)),
with gamma -> 0, j -> infinity and A = gamma*j fixed.
Metric-insertion derivatives in Eqs. (67)-(69) carry gamma^2*j^2,
so the rest-sector contribution scales as gamma^4*j^3 = A^4/j.

The dimension and scaling laws are source-backed. Numerical H^epsilon,
O(gamma) corrections and insertion directions are controlled fixtures.
"""

import argparse
import json
import math
import os
import numpy as np

N_REST = 44


def orthogonal(rng, n):
    q, r = np.linalg.qr(rng.normal(size=(n, n)))
    d = np.sign(np.diag(r)); d[d == 0.0] = 1.0
    return q @ np.diag(d)


def make_core(rng, cond_exp, imag_strength):
    q = orthogonal(rng, N_REST)
    eig = np.geomspace(1.0, 10.0 ** (-cond_exp), N_REST)
    real_spd = q @ np.diag(eig) @ q.T
    s = rng.normal(size=(N_REST, N_REST)); s = 0.5 * (s + s.T)
    s /= max(float(np.linalg.norm(s, ord=2)), 1.0e-300)
    h_eps = -(real_spd + 1j * imag_strength * math.sqrt(float(eig[-1])) * s)
    k = rng.normal(size=(N_REST, N_REST)) + 1j * rng.normal(size=(N_REST, N_REST))
    k = 0.5 * (k + k.T)
    k /= max(float(np.linalg.norm(k, ord=2)), 1.0e-300)
    return h_eps, k


def log_slope(xs, ys):
    lx = np.log(np.asarray(xs, dtype=float)); ly = np.log(np.asarray(ys, dtype=float))
    return float(np.polyfit(lx, ly, 1)[0])


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--index', type=int, required=True); a = ap.parse_args()
    idx = a.index
    if not 0 <= idx < 24: raise SystemExit('index must be 0..23')

    areas = [0.25, 0.5, 1.0, 2.0]
    cond_exps = [1, 2, 4]
    correction_strengths = [0.03, 0.10]
    area = areas[idx % 4]
    cond_exp = cond_exps[(idx // 4) % 3]
    corr_strength = correction_strengths[(idx // 12) % 2]
    imag_strength = [0.03, 0.10, 0.25][(idx // 2) % 3]

    rng = np.random.default_rng(429000 + idx)
    h_eps, k = make_core(rng, cond_exp, imag_strength)
    k *= corr_strength
    v = rng.normal(size=N_REST) + 1j * rng.normal(size=N_REST)
    v /= max(float(np.linalg.norm(v)), 1.0e-300)

    js = np.asarray([1e2, 3e2, 1e3, 3e3, 1e4, 3e4, 1e5, 3e5, 1e6], dtype=float)
    gammas = area / js
    rest_magnitudes = []
    inverse_errors = []
    scaled_limits = []

    h_eps_inv = np.linalg.inv(h_eps)
    # Source-backed leading fixed-area limit of j * G_rest / A^4.
    target = complex(v.T @ h_eps_inv @ v)
    if abs(target) < 1e-10:
        raise SystemExit('fixture target accidentally near zero')

    for j, gamma in zip(js, gammas):
        h_rest = j * (h_eps + gamma * k)
        h_inv = np.linalg.inv(h_rest)
        leading_inv = h_eps_inv / j
        inverse_errors.append(float(np.linalg.norm(h_inv - leading_inv, ord='fro') / max(np.linalg.norm(leading_inv, ord='fro'), 1e-300)))

        # Eqs. (67)-(69): derivative scale gamma^2 j^2 = A^2 at fixed A.
        d = (gamma ** 2) * (j ** 2) * v
        g_rest = complex(d.T @ h_inv @ d)
        rest_magnitudes.append(float(abs(g_rest)))
        scaled_limits.append(complex((j / (area ** 4)) * g_rest))

    # Use the asymptotic tail only; O(gamma) contamination is expected at finite j.
    tail = slice(-5, None)
    rest_slope = log_slope(js[tail], np.asarray(rest_magnitudes)[tail])
    inverse_error_slope = log_slope(js[tail], np.asarray(inverse_errors)[tail])
    final_scaled_relative_error = float(abs(scaled_limits[-1] - target) / abs(target))

    # Directly verify gamma^4 j^3 = A^4 / j, the source scaling in Eq. (98).
    source_scale = (gammas ** 4) * (js ** 3)
    algebraic_scale = (area ** 4) / js
    source_scaling_identity_error = float(np.max(np.abs(source_scale - algebraic_scale) / np.maximum(np.abs(algebraic_scale), 1e-300)))
    source_scale_slope = log_slope(js, source_scale)

    # Negative control: omit the source-required prefactor j in H_rest.
    bad_mags = []
    for j, gamma in zip(js, gammas):
        h_bad = h_eps + gamma * k
        d = (gamma ** 2) * (j ** 2) * v
        g_bad = complex(d.T @ np.linalg.inv(h_bad) @ d)
        bad_mags.append(abs(g_bad))
    bad_slope = log_slope(js[tail], np.asarray(bad_mags)[tail])
    missing_j_detected = abs(bad_slope + 1.0) > 0.5 and abs(bad_slope) < 0.15

    numerical_pass = bool(
        abs(rest_slope + 1.0) < 0.035
        and abs(inverse_error_slope + 1.0) < 0.08
        and final_scaled_relative_error < 2.0e-5
        and source_scaling_identity_error < 5.0e-14
        and abs(source_scale_slope + 1.0) < 1.0e-12
        and missing_j_detected
    )

    out = {
      'iteration':429,
      'profile_index':idx,
      'rest_dimension':N_REST,
      'fixed_area':area,
      'condition_exponent':cond_exp,
      'correction_strength':corr_strength,
      'imag_strength':imag_strength,
      'j_grid':js.tolist(),
      'gamma_grid':gammas.tolist(),
      'rest_sector_log_slope':rest_slope,
      'inverse_correction_log_slope':inverse_error_slope,
      'source_gamma4_j3_log_slope':source_scale_slope,
      'source_scaling_identity_relative_error':source_scaling_identity_error,
      'final_scaled_limit_relative_error':final_scaled_relative_error,
      'negative_control_missing_j_prefactor_log_slope':bad_slope,
      'negative_control_detected':bool(missing_j_detected),
      'numerical_pass':numerical_pass,
      'classification':'PASS_SOURCE_BACKED_ASYMPTOTIC_SCALING' if numerical_pass else 'FAIL_SOURCE_BACKED_ASYMPTOTIC_SCALING',
      'source_authority':'arXiv:1109.6538v2 Sec. V.4, Eqs. (98)-(100) and Hessian scaling immediately preceding them',
      'physical_input_status':'SOURCE_SCALING_LAWS_BACKED__NUMERICAL_HEPSILON_ENTRIES_CONTROLLED',
      'd7_status':'OPEN',
      'scope_guard':'This validates the published fixed-area asymptotic scaling and 44-dimensional rest-sector resource closure on controlled matrices. It does not supply a physical critical-point H^epsilon, boundary alpha, causal-measure transport, or close D7/NEW_REQUIRED.'
    }
    os.makedirs('build/lqg-iter429', exist_ok=True)
    with open(f'build/lqg-iter429/profile_{idx}.json','w',encoding='utf-8') as f:
        json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not numerical_pass: raise SystemExit(2)

if __name__ == '__main__': main()
