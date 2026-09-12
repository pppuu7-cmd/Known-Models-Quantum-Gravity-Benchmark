# Iter430 Recovery / Front / Publication-Ledger Delta

Date: 2026-09-12
Authoritative compute head: `7c8a49d6c55007ac8f08d63efc53e6c308e3bfda`
Authoritative run: `34695267770` (`lqg-iter430-eprl-asymptotic-reach`)
Aggregate job: `103557667991`
Aggregate artifact: `10298254738`
Aggregate artifact digest: `sha256:ded1583f2d6171e25e5850b21f80d35ede7e1fd172a16a83167cc2ee50469b47`

## Proven result
Iter429 (`34694159992`) failed only the unchanged terminal scaled-limit criterion in profiles 21--23 at `j_max=1e6`; the three profiles still passed the scaling-slope, algebraic source-identity, and negative-control checks. The observed terminal relative errors were approximately `4.25e-5`, `1.21e-4`, and `1.50e-4`, respectively, versus the preregistered `2e-5` bound. This is recorded as a scientific finite-reach failure, not an infrastructure failure and not a reason to relax the gate.

Iter430 preserved the exact 24-fixture map and the original `2e-5` gate, extending only the asymptotic reach to `j=1e8` and adding explicit `O(1/j)` tail diagnostics. All 24/24 profiles and the strict aggregate passed. The worst terminal scaled-limit relative error was `1.5007917153323004e-06`; the latest first crossing of the original `2e-5` threshold occurred at `j=1e7`.

Classification: `PASS_FINITE_ASYMPTOTIC_REACH_CLOSURE`.

Interpretation: the Iter429 failures are resolved as insufficient asymptotic reach inside the controlled 44-dimensional EPRL/proper-vertex fixture, rather than a plateau/conditioning obstruction. No scientific threshold was loosened.

## Scope guard
This closes only the finite-reach question for the controlled source-backed asymptotic fixture. Numerical entries of the physical EPRL/proper-vertex Hessian, fixed-Toller causal-vertex integrability or a direct finite normalized vertex certificate, `lambda_f`-weighted complete-stack cutoff removal, and same-realization UV-to-causal-Regge/GR transport remain open.

## Global locks after Iter430
- D2 = `NOT_CLOSED_COVERAGE_AND_OBJECTS`.
- D4 = `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7 = `NOT_CLOSED / NOT_YET_AUTHORIZED`.
- D7-S2 = `NOT_CLOSED`.
- D7-S3 = `NOT_CLOSED`.
- D7-S4 = `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7-S5 = `NOT_AUTHORIZED`; D7-S6 = `INACTIVE`.
- `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, and `NEW_REQUIRED` remain forbidden.
- Candidate Gravity remains inactive.

## Publication impact
Permitted wording for Paper IV / benchmark reporting: the source-backed controlled EPRL/proper-vertex asymptotic fixture exhibits the predicted fixed-area `O(1/j)` approach and reaches the preregistered scaled-limit tolerance when the trajectory is extended sufficiently far.

Forbidden wording: this result is not a physical causal-spinfoam finiteness proof, not a physical Hessian/covariance ingestion, not a complete-stack continuum certificate, and not a family-level D7 classification. It creates no Paper-III general rule by itself.

## Next permitted frontier
Primary S2 blocker remains unchanged:
`D7_S2_LQG_EXPLICIT_TOLLER_CAUSAL_VERTEX_INTEGRABILITY_THEOREM_OR_DIRECT_FINITE_NORMALIZED_VERTEX_CERTIFICATE__THEN_LAMBDA_F_WEIGHTED_COMPLETE_STACK_CUTOFF_CONTROL__THEN_SAME_REALIZATION_UV_TO_CAUSAL_REGGE_GR_TRANSPORT`.

An independent S4 structural audit may proceed in parallel provided it preserves S2/S3 locks and does not authorize the terminal classifier; Iter431 is such a scoped audit.
