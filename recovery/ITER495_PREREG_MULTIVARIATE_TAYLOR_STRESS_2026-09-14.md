# Iter495 Preregistration — Multivariate q=1 Taylor-envelope stress audit

Date: 2026-09-14
Status: prospectively frozen before implementation.

## Authority
Iter493 qualified the full-basis q=1 first/diagonal-second response. Iter494 terminal classification is `ITER494_CRITICAL_Q1_MIXED_CURVATURE_QUALIFIED_SCOPED`; it shows finite but strongly anisotropic mixed curvature, max |M| about 1.966, so diagonal/separable Taylor control is not authorized.

## Scientific question
Does a full local quadratic model including first, diagonal-second and mixed-second terms predict the actual q=1 shrinking-layer radial slopes on prospectively frozen simultaneous multi-coordinate perturbations with a stable remainder, or do higher-order/cross-coordinate effects expose a new blocker before any interval/uniform certificate?

## Frozen active chart
Use exactly coordinates `[0,1,3,5,6,11]`, inherited from Iter494. No coordinate may be added/dropped after seeing Iter495 output.

## Frozen multi-coordinate directions
Use the following 8 six-dimensional sign directions and both signs (16 directed perturbations total):
`[+,+,+,+,+,+]`, `[+,+,+,-,-,-]`, `[+,-,-,+,+,-]`, `[+,-,+,-,+,-]`, `[+,+,-,+,-,-]`, `[+,-,+,+,-,+]`, `[+,+,-,-,+,+]`, `[+,-,-,-,-,+]`.
These are fixed before implementation to mix dominant and low-response coordinates without post-hoc steering.

## Frozen scales and objects
- causal classes: `0to5`, `1to4`, `2to3`;
- q=`1.00` only;
- all four inherited rho witnesses;
- reference finite-difference step `h0=0.005` for local coefficients;
- target simultaneous amplitudes `a in {0.0025,0.0050}`;
- inherit center geometry, R grid, source Toller/KAK convention, intertwiner channels, Haar bookkeeping, HP precision and source controls unchanged from Iter492-494.

For each causal/rho state, compute at h0:
- center slope `s0`;
- six symmetric first derivatives D_i;
- six symmetric diagonal second derivatives Q_ii;
- all 15 symmetric mixed derivatives M_ij.
For every frozen target vector x=a*d, form
`T2(x)=s0 + D.x + 0.5 * sum_i Q_ii x_i^2 + sum_{i<j} M_ij x_i x_j`
and evaluate the actual slope `s(x)` from the source-locked q=1 network.
Record remainder `r=s(x)-T2(x)`, `|r|`, `|r|/a^2`, `|r|/a^3`, sign-pair symmetry residuals, and the ratio of remainders between the two amplitudes.

## Parallelization
Partition the 8 undirected directions into 4 fixed blocks of 2. Matrix = 3 causal classes × 4 blocks = 12 independent jobs; `fail-fast:false`; `max-parallel:12`.

## Frozen validity controls
A job is valid only if every center, coefficient stencil and target evaluation passes inherited source/HP controls and every slope/derivative/remainder is finite. No threshold may be relaxed to make CI green.

## Interpretation rule
If all 12 jobs are valid, classify `ITER495_MULTIVARIATE_TAYLOR_STRESS_QUALIFIED_SCOPED` and report the measured remainder envelope regardless of magnitude. Large or non-cubic remainder is a scientific blocker, not an infrastructure failure. If inherited source/HP controls fail, classify `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER495` and identify the first causal failure.

A valid Iter495 is only a prospectively frozen finite-set multivariate Taylor stress audit. It is not an interval proof, not a uniform open-neighborhood certificate, not a positive-measure/Haar theorem, not D7-S2 closure, and does not authorize a terminal D7 label or Candidate Gravity.

## Locks
D7-S2 `NOT_CLOSED`; D7-S3 `NOT_CLOSED`; D7-S4 `PARTIAL_GLOBAL_NOT_CLOSED`. `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` forbidden. Candidate Gravity inactive.
