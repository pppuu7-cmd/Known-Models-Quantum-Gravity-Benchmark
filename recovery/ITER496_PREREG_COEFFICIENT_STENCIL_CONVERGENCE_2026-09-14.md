# Iter496 Preregistration — q=1 Taylor coefficient-stencil convergence

Date: 2026-09-14
Status: prospectively frozen before implementation.

## Authority
Iter495 terminal aggregate classification is `ITER495_MULTIVARIATE_TAYLOR_STRESS_QUALIFIED_SCOPED` from run `34804409129`, head `49a4695e2ecc43391d3477d0ff9554b910e425ee`, aggregate artifact `10333052075`, digest `sha256:6d0cf4c19a3735d4509772ab43e246ab58da3d408534cbd09578348e3ed44a77`. All 12 jobs are valid, but the measured quadratic remainder is not uniformly cubic: `abs_remainder_max=2.1820206151890176e-4`, `r_over_a3_max=4069.3407635785657`, and the small/large remainder ratio has median `0.22654674656585128` and max `9.533261802575108` versus cubic expectation `0.125`.

## Scientific question
Before interpreting the Iter495 non-cubic remainder as genuine higher-order/cross-coordinate physics, determine whether it is dominated by finite-difference truncation in the locally estimated first/second/mixed Taylor coefficients. Does the coefficient tensor and the resulting multivariate remainder converge under a prospectively frozen halving sequence of coefficient-stencil widths?

## Frozen chart and directions
Use exactly the Iter495 active coordinates `[0,1,3,5,6,11]` and the same 8 six-dimensional sign directions, with both signs. No direction or coordinate may be changed after output is seen.

## Frozen coefficient stencils
Estimate the complete local coefficient set `(D_i,Q_ii,M_ij)` independently at
- `h = 0.0050`,
- `h = 0.0025`,
- `h = 0.00125`.
The center slope is common. Use the same symmetric formulas as Iter495 at each h.

Also construct a second-order Richardson extrapolation from the two finest stencils, coefficient by coefficient:
`C_R = (4*C_0.00125 - C_0.0025)/3`.
This extrapolation is a diagnostic object only; it does not alter any earlier gate.

## Frozen target amplitudes
Evaluate the actual source-locked q=1 slopes on the same simultaneous directions at `a in {0.00125,0.0025}`. For each coefficient stencil and for the Richardson tensor, form the same full quadratic predictor T2 and record remainder `r`, `|r|`, `|r|/a^2`, `|r|/a^3`, and small/large remainder ratio.

## Frozen convergence observables
For every causal/rho state record:
- max/median absolute changes in D, Qii, and M between successive h levels;
- observed halving ratios for coefficient changes;
- actual-predicted remainder envelopes for each h and Richardson coefficients;
- whether Richardson reduces the absolute remainder relative to the h=0.005 baseline on each prospectively frozen state.

## Matrix and parallelism
Partition the 8 undirected directions into the same 4 fixed blocks of 2. Matrix = 3 causal classes × 4 blocks = 12 independent jobs; `fail-fast:false`; `max-parallel:12`.

## Frozen validity controls
Every center, coefficient stencil, target evaluation and source/high-precision control inherited from Iter492–Iter495 must pass and all reported values must be finite. No numerical/source threshold may be relaxed to obtain green CI.

## Interpretation rule
If all 12 jobs are valid, classify `ITER496_COEFFICIENT_STENCIL_CONVERGENCE_QUALIFIED_SCOPED` and report the measured convergence/remainder envelopes regardless of whether convergence is good or bad.

Scientific interpretation is then frozen as follows:
- if coefficient refinement/Richardson materially suppresses the Iter495-style remainder envelope across the frozen states, the next blocker is a validated coefficient/remainder enclosure rather than adding higher polynomial order;
- if the remainder remains non-cubic and is not materially suppressed under coefficient refinement, the next blocker is genuine higher-order/nonlocal angular structure and a prospectively frozen third-order-or-direct interval treatment is required;
- mixed behavior must be reported as mixed and cannot be converted post hoc into either outcome.

This iteration is not an interval proof, not a uniform open-neighborhood certificate, not a positive-measure/Haar theorem, not D7-S2 closure, and does not authorize a terminal D7 label or Candidate Gravity.

## Locks
D7-S2 `NOT_CLOSED`; D7-S3 `NOT_CLOSED`; D7-S4 `PARTIAL_GLOBAL_NOT_CLOSED`. `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` forbidden. Candidate Gravity inactive.