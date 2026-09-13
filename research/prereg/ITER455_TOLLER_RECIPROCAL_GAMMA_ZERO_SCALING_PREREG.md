# Iter455 — Toller reciprocal-Gamma simple-zero replacement qualification

Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION
Date: 2026-09-13

## Motivation and authority
Iter454 is immutable and remains a frozen aggregate FAIL. Its causal audit showed that the only failing predicate required `|1/Gamma|<=1e-50` at finite displacement `delta=1e-30`, although the reciprocal Gamma function has a simple zero and therefore must scale linearly in `delta`. Iter455 is a new replacement prerequisite; it does not alter any Iter454 artifact, threshold, or classification.

## Goal
Test the mathematically correct local zero law of the reciprocal-Gamma factor used by the source-defined Toller Feynman projector, while independently repeating the unaffected Iter454 projector/branch controls.

For a nonnegative integer m,
`1/Gamma(-m+epsilon) = (-1)^m m! epsilon + O(epsilon^2)`.
For the source-pole parameterization used here, the magnitude coefficient is therefore `m!`.

## Frozen lanes
Same source-independent numerical tuples as Iter454:
- L0=(j,l,rho)=(0,0,0.37)
- L1=(1,1,0.73)
- L2=(1,2,1.11)
- L3=(2,2,1.57)
All use 80 decimal digits.

## Frozen simple-zero probes
For every source pole n=-j,...,l, define m=j+n and evaluate at
`delta = [1e-10,1e-15,1e-20,1e-25,1e-30]`.

Required per pole:
1. `R(delta)=|1/Gamma(-m-i*delta)|/delta` at the two smallest deltas agrees with exact `m!` to relative error <=1e-8.
2. Log-log slopes of `|1/Gamma|` versus delta for the final three adjacent intervals each satisfy `|slope-1|<=1e-6`.
3. Magnitudes strictly decrease with delta.
4. Deliberately wrong quadratic-zero hypothesis is rejected: at delta=1e-30, `|1/Gamma|/delta^2 > 1e20`.

## Frozen repeated controls
Per lane:
5. `P_jl(rho;rho)=1` within 1e-60.
6. Source pole enumeration exactly equals `n=-j,...,l`.
7. Same regulated Sokhotski-Plemelj branch-difference Gaussian control as Iter454, epsilon=[0.2,0.1,0.05,0.025]: last absolute error <0.03 and lower than first.
8. Same deliberately wrong same-sign branch control: last absolute error >0.2.

## Frozen aggregate
PASS only if all four lanes are valid and all eight predicates pass:
`ITER455_TOLLER_RECIPROCAL_GAMMA_SIMPLE_ZERO_QUALIFIED_SCOPED`.
Valid execution with any failed scientific predicate:
`SCIENTIFIC_FAIL_ITER455_TOLLER_RECIPROCAL_GAMMA_SIMPLE_ZERO`.
Execution/precision/integration invalidity:
`INFRASTRUCTURE_OR_NUMERICAL_FAIL`.

## Interpretation lock
A PASS supersedes only the malformed Iter454 local-zero prerequisite. Together with the repeated projector/branch controls it permits a later, separately preregistered reduced Toller t-matrix / Ruhl-phase / Eq.(7) reconstruction gate. It does not establish the full Toller matrix element, vertex convergence, regulator removal, absolute integrability, D7-S2 closure, terminal D7, or any model-family classifier.
