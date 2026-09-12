# Iter431-432 Recovery / Front / Publication-Ledger Delta

Date: 2026-09-12

## Iter431 — causal-branch Hessian transport assay
Authoritative compute head: `35f3d5865ac0992ab39bd1311d4aa05c5e706894`
Authoritative run: `34695479100` (`lqg-iter431-causal-branch-hessian-transport`)
Aggregate job: `103558653903`
Aggregate artifact: `10297574053`
Aggregate artifact digest: `sha256:903d0d1cd4840d71459363994a0589f91988c1cc9ffff634627c90eb238d7318`

All 24 profile artifacts were produced, but only 8/24 passed the frozen profile gate. The common-branch covariance test itself had zero worst relative error; the failing discriminator was the preregistered negative-control sensitivity requirement. The minimum negative-control covariance shift was `7.027283697271206e-06`, below the frozen `1e-3` sensitivity threshold used by the audit. This is therefore a scientific assay FAIL, not an infrastructure failure and not evidence that the source-backed common-Hessian statement is false. No threshold is relaxed post hoc.

Classification: `FAIL_CAUSAL_BRANCH_HESSIAN_TRANSPORT_STRUCTURE` with interpretation `NEGATIVE_CONTROL_SENSITIVITY_NOT_UNIFORM`; D7-S4 remains `PARTIAL_GLOBAL_NOT_CLOSED`.

## Iter432 — source-faithful gamma-simple Toller kernel
Authoritative compute head: `d7632eeae116686ca3f11bd70d605a8ddd506596`
Authoritative run: `34695643583` (`lqg-iter432-gamma-simple-toller-kernel`)
Aggregate job: `103558812669`
Aggregate artifact: `10299155196`
Aggregate artifact digest: `sha256:307012c0ac8b8e4c50ed41a7d15e1bad1dc6c6bde93a819bdab7ca13139945a7`

All 24/24 profiles passed the prospectively frozen one-wedge kernel gate. Worst forward relative `T+ + T- = D` error was `8.838635530945528e-76`; worst backward relative error was `5.8471560999073846e-80`; worst large-boost tail-slope error was `2.8166100215675864e-05` against the unchanged `2e-4` bound. Worst cancellation condition was `472717.53442256706`, so the high-precision backward-error control is material.

Classification: `PASS_SOURCE_FAITHFUL_GAMMA_SIMPLE_TOLLER_KERNEL`.

This closes only the exact published gamma-simple one-wedge kernel prerequisite. It does not establish fixed-causal-sector vertex integrability, multi-wedge contraction finiteness, a normalized causal vertex, complete-stack cutoff removal, or same-realization UV-to-GR transport.

## Global locks after Iter432
- D2 = `NOT_CLOSED_COVERAGE_AND_OBJECTS`.
- D4 = `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7 = `NOT_CLOSED / NOT_YET_AUTHORIZED`.
- D7-S2 = `NOT_CLOSED`.
- D7-S3 = `NOT_CLOSED`.
- D7-S4 = `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7-S5 = `NOT_AUTHORIZED`; D7-S6 = `INACTIVE`.
- `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, and `NEW_REQUIRED` remain forbidden.
- Candidate Gravity remains inactive.

## Next permitted frontier
The direct S2 route is now allowed to use the validated Iter432 one-wedge kernels. The next independent pre-gate is a prospectively frozen large-boost radial-envelope audit for the four wedges incident on one tetrahedral group integration: combine the published branch-specific tail exponents with the Lorentz-group radial Haar growth, include the worst branch/magnetic assignments, and test the exact kernels numerically at high precision. A PASS may close only the single-group large-boost tail obstruction. Finite-boost pole/collision structure, angular correlations, simultaneous multi-group escape directions, full boundary contraction, and normalized causal-vertex finiteness remain open and must be addressed separately before D7-S2 can close.
