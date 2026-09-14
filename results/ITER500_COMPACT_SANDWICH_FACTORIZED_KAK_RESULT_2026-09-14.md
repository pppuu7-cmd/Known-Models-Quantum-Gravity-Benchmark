# Iter500 — compact-sandwich / factorized KAK enabling result

Date: 2026-09-14
Status: TERMINAL SCOPED QUALIFICATION; ENABLING GATE ONLY

## Authority
- prereg: `04b6f01f603e7b37ed4b0e380eedbdff6b44fe50`
- evaluator: `5e4054b105cdfc646b85f4e52926dc4dd87c6d50`
- regression-semantics repair: `4964bb8a882ee840e30c45b71e90bd9edebedf21`
- aggregate: `0e95a580645aeca467139bcdb2b43e3131ab889b`
- production head: `aeda66ac6d80a1ac85f43f21fe300194042313bb`
- workflow run: `34819282062`
- source-lock job: `103896861477`
- aggregate job: `103897145400`
- aggregate artifact: `10338155232`
- aggregate digest: `sha256:f687ee7bcd1cb4afc8404171c3834a321c061b74c56cce8d475d6b60b018f950`

## Terminal classification
`ITER500_COMPACT_SANDWICH_FACTORIZED_KAK_QUALIFIED_SCOPED`

All four matrix blocks are present exactly once and qualified. Each block evaluates 256 frozen states, for 1024/1024 states total. There are no missing blocks, no duplicate blocks, no method-blocker blocks and no covariance-fail blocks.

Aggregate numerical controls:
- global max midpoint matrix relative error: `1.506093027251261e-16`
- global max midpoint beta absolute error: `2.220446049250313e-16`
- global max midpoint Toller relative error: `1.2412085474744689e-15`
- global minimum certified beta lower bound: `0.5011445004474808`
- old generic interval-KAK limitation negative control: reproduced as expected.

## Scientific interpretation
The Iter499 validated-arithmetic method blocker is removed on the prospectively frozen 16-box state space by the source-faithful compact-sandwich / dependency-preserving factorized KAK construction:
- outer amplitude-dependent SU(2) factors are stripped before interval KAK and restored afterward;
- `0b` edges use the fixed middle `G_b^{-1} B^{-1}`;
- internal `ab` edges retain the dependency-preserving middle factorization;
- midpoint source regression against the independent high-precision geometry/Toller construction passes at margins far inside the frozen tolerances.

This result authorizes a fresh prospectively frozen direct continuous max-envelope interval science gate that allows intertwiner-channel crossings. It does **not** itself classify NONDECAY, Haar convergence/divergence, positive measure, the ten-spectral correlated kernel, or D7-S2 closure.

## Guards
D7-S2 remains open. D7-S3 remains open. D7-S4 remains partial/global-not-closed. Terminal D7 classification and `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` remain forbidden. Candidate Gravity remains inactive.
