# Iter495 Result — Multivariate q=1 Taylor stress

Date: 2026-09-14

## Authority
- prereg: `1b73918e53663186eb4811a62922cd4402220958`
- evaluator: `7ab222baf9fede2e5ff39a07d770c0f5544c1f61`
- aggregate implementation: `1a2f6974156dc4e6a1eaae7f4b95e3258f5c5ebe`
- production head: `49a4695e2ecc43391d3477d0ff9554b910e425ee`
- run: `34804409129`
- aggregate job: `103854581566`
- aggregate artifact: `10333052075`
- digest: `sha256:6d0cf4c19a3735d4509772ab43e246ab58da3d408534cbd09578348e3ed44a77`

All 12 scientific jobs and source-lock completed successfully. Aggregate reports `job_count=12`, `missing_jobs=0`, `invalid_jobs=[]`, `valid=true`.

## Frozen classification
`ITER495_MULTIVARIATE_TAYLOR_STRESS_QUALIFIED_SCOPED`.

## Measured envelope
- max absolute quadratic remainder: `2.1820206151890176e-4`
- median absolute remainder: `1.6141497027888363e-9`
- max `|r|/a^2`: `10.173351908946415`
- max `|r|/a^3`: `4069.3407635785657`
- cubic expected small/large ratio: `0.125`
- observed small/large ratio median: `0.22654674656585128`
- observed small/large ratio max: `9.533261802575108`

A consumed raw lane (`0to5-b0`) exhibits one of the severe cases: at rho `2.7`, direction `[1,1,1,-1,-1,-1]`, sign `-1`, `a=0.005`, the absolute remainder is `1.729638565208802e-4`; at `a=0.0025` the same block also contains `|r|/a^3` up to `4069.3407635785657`.

## Scientific interpretation
Iter495 is a valid finite-set audit, but it does not support a stable cubic remainder assumption for the quadratic Taylor model over the frozen simultaneous perturbations. This is a new scientific blocker, not infrastructure failure and not a reason to relax thresholds.

Before attributing the non-cubic remainder to genuine third/higher-order angular structure, finite-difference truncation in the Iter493/494 local coefficients must be separated from physical/nonlinear higher-order structure. Iter496 is prospectively frozen for exactly that coefficient-stencil convergence question.

## Scope guards
No interval/uniform certificate, no positive-measure/Haar theorem, no D7-S2 closure, no terminal D7 classifier, and no Candidate Gravity authorization follows from Iter495.