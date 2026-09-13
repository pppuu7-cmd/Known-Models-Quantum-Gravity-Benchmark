# Iter459 preregistration — Toller/Plemelj distributional boundary-value audit

Frozen before implementation/production: 2026-09-13.

## Motivation
Iter458 terminally rejected ordinary symmetric truncation as an adequate realization of the published Feynman `i epsilon` kernel on its frozen source panel. The next admissible question is whether the *published denominator displacement itself* exhibits the expected distributional boundary value when paired with well-controlled Schwartz tests, before inserting the non-Schwartz source-specific `P_11*d` object.

## Frozen mathematical object
For `s in {+1,-1}` test

`K_{s,epsilon}(x;r) = 1 / (x-r - i*s*epsilon)`

against real Schwartz test functions. The target is the Sokhotski-Plemelj boundary value

`PV ∫ phi(x)/(x-r) dx + i*s*pi*phi(r)`.

A source-prefactor consistency control also applies the published branch prefactor `s/(2 i pi)` without modifying the denominator prescription.

## Frozen panel
Six independent lanes, each testing both signs:
- rho `0.35` with `phi0=exp(-x^2)`, `phi1=(1+0.3x)exp(-0.7x^2)`, `phi2=cos(1.1x)exp(-0.4x^2)`;
- rho `1.60` with the same three tests.

Integration window `[-12,12]`; epsilon ladder `[0.20,0.10,0.05,0.025,0.0125]`.

## Independent routes
1. Finite-epsilon complex quadrature with adaptive real/imaginary integration.
2. PV target route A: Cauchy-weight quadrature.
3. PV target route B: exact singularity subtraction `(phi(x)-phi(rho))/(x-rho)` plus the analytic constant PV logarithm.

The two PV routes must agree independently.

## Frozen criteria
A lane is scientifically supportive only if all conditions hold for both signs:
1. all finite-epsilon and target values are finite;
2. independent PV routes agree to absolute error `<= 2e-9`;
3. the smallest-epsilon boundary-value relative error is `<= 3e-2`;
4. the final error is no larger than `0.35` times the first-epsilon error (clear approach to the boundary value);
5. the last epsilon-halving changes the finite-epsilon value by relative `<= 3e-2`;
6. source-prefactor reconstruction from the raw Plemelj target is algebraically consistent to `<= 1e-12`;
7. wrong-delta-sign control must differ from the correct target by relative `>= 5e-2` in every sign/test case.

Aggregate PASS requires 6/6 valid and 6/6 supportive lanes. `fail-fast:false`; no post-result threshold changes.

## Frozen interpretations
- PASS: `ITER459_TOLLER_PLEMELJ_DISTRIBUTIONAL_KERNEL_QUALIFIED_SCOPED` — qualifies only the universal distributional realization of the source denominator on this Schwartz panel. It does not reconstruct the full Toller branch, does not close D7-S2, and does not imply causal-vertex convergence.
- Valid scientific failure: `SCIENTIFIC_FAIL_ITER459_TOLLER_PLEMELJ_DISTRIBUTIONAL_PANEL` — preserve the result and investigate the failed mathematical/numerical premise without retuning thresholds.
- Invalid execution: `INFRASTRUCTURE_OR_NUMERICAL_FAIL`.

## Claim locks
No physical causal-vertex finiteness/divergence theorem; no terminal D7 classifier; no Candidate Gravity activation; no replacement regulator; no fitted subtraction; no `beta+i epsilon`.
