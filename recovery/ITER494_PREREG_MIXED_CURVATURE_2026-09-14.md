# Iter494 Preregistration — Critical q=1 mixed-curvature audit

Date: 2026-09-14
Status: prospectively frozen before implementation.

## Authority
Iter493 terminal classification is `ITER493_CRITICAL_Q1_LOCAL_VARIATION_QUALIFIED_SCOPED`. Its aggregate shows a strongly anisotropic response, max |Q| about 1.978, and a large two-step Q discrepancy. Therefore a scalar/diagonal-only Lipschitz or Taylor surrogate is not authorized.

## Scientific question
On the already-qualified q=1 shrinking boundary layer, are mixed angular second derivatives among the dominant local-response coordinates finite and numerically stable enough to support the next validated Taylor-envelope design, or do cross-coordinate couplings expose a new blocker?

## Frozen coordinate set
Using only terminal Iter493 outputs, freeze coordinates `[0,1,3,5,6,11]` before implementation:
- 0,1,5,6 are among the largest Iter493 coordinate response norms;
- 11 contains the largest measured diagonal second variation;
- 3 is a prospectively fixed low-response control coordinate.
All 15 unordered pairs are tested; no pair may be dropped after seeing results.

## Frozen design
- causal classes: `0to5`, `1to4`, `2to3`;
- q = 1.00 only;
- pair steps h in `{0.005,0.010}`;
- all four rho witnesses;
- for every pair `(i,j)` and rho, compute the symmetric mixed finite difference
  `M_h=[s(+i,+j)-s(+i,-j)-s(-i,+j)+s(-i,-j)]/(4h^2)`;
- center/source geometry, R grid, KAK convention, intertwiner channels, Haar bookkeeping, HP precision and source controls are inherited unchanged from Iter493/492;
- partition the 15 pairs into 3 fixed blocks of 5 pairs; 3 causal × 3 blocks = 9 independent Actions jobs;
- `fail-fast:false`; `max-parallel:9`.

## Frozen validity controls
A job is valid only if every corner evaluation passes inherited source/HP controls and every returned slope/M_h is finite. No scientific threshold may be relaxed to make CI green.

For each pair/rho record both M_0.005 and M_0.010, absolute discrepancy, scale-normalized discrepancy, and sign stability. Aggregate reports max/median |M|, extremum location, discrepancy maxima, sign-stability count, and per-coordinate mixed-response norm.

## Interpretation rule
If all 9 jobs are valid, classify `ITER494_CRITICAL_Q1_MIXED_CURVATURE_QUALIFIED_SCOPED` and report the measured cross-coordinate curvature regardless of magnitude. If an inherited numerical/source control fails, classify `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER494` and identify the first causal failure; do not weaken thresholds.

Even a valid result is only a finite-grid mixed-curvature prerequisite for a later interval/validated-uniform Taylor certificate. It is not itself an interval proof, open-neighborhood/positive-measure theorem, Haar convergence/divergence theorem, D7-S2 closure, terminal D7 label, or Candidate Gravity authorization.

## Locks
D7-S2 `NOT_CLOSED`; D7-S3 `NOT_CLOSED`; D7-S4 `PARTIAL_GLOBAL_NOT_CLOSED`. `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` forbidden. Candidate Gravity inactive.
