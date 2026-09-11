# Paper IV LQG Toller Finiteness-Theorem Transfer Audit — Iter304

Date: 2026-09-11

## Authority and frozen scope

Primary objects: Kamiński, *All 3-edge-connected relativistic BC and EPRL spin-networks are integrable* (arXiv:1010.5384); Bianchi–Chen–Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, PRD 114, 046014 (2026); and Bianchi–Chen–Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, PRD 113, 126020 (2026).

The prospectively frozen contract is `benchmarks/lqg_iter304_toller_finiteness_transfer.json`. The question is intentionally narrow: does the already-published 3-edge-connected standard-EPRL integrability theorem automatically certify the sign-selected Toller causal vertex from the presently frozen source properties?

## Machine result

Scientific run `34622448515` on exact scientific head `b6365b863fea2e6c61c7bcd0848deac0c81f4dc9`: four independent probes ran with `fail-fast:false`, `max-parallel:4`; aggregate executed only after all probes succeeded.

Independent jobs:
- `103339444457` — `source_theorem_scope` — SUCCESS;
- `103339444326` — `polynomial_bound_nonintegrability_witness` — SUCCESS;
- `103339444484` — `transfer_fail_closed_guard` — SUCCESS;
- `103339444563` — `scope_guard` — SUCCESS;
- aggregate `103339561820` — SUCCESS.

Summary artifact `10272398533`; artifact digest `sha256:ad9072614d42f6f004b9fae8d3225c678e67315af84c7c3cf2a3ffb700e2280a`; raw summary digest `sha256:233709ebaceee04857e04b8b2de89aa84a7d9982e80657e3e4d0af331d428c80`.

Exact-head methodology CI `34622448482` = SUCCESS.

## Frozen classification

`PASS_SCOPED_STANDARD_EPRL_3_EDGE_CONNECTED_FINITENESS_THEOREM_NOT_AUTOMATICALLY_TRANSFERABLE_TO_FIXED_CAUSAL_TOLLER_VERTEX_FROM_POLYNOMIAL_BOUNDEDNESS_ALONE__EXPLICIT_TOLLER_INTEGRABILITY_BOUND_OR_EXTENSION_THEOREM_REQUIRED__NO_DIVERGENCE_NO_GO_OR_FAMILY_PROMOTION`

## Interpretation

The standard theorem is a genuine positive finiteness result for its stated SL(2,C) spin-network/invariant class. Iter302-303 established that a fixed Toller branch is not itself an SL(2,C) representation even though its finite-spin SU(2)-Haar boundary contraction is compatible with Han's half-link gluing. Iter304 therefore audits theorem applicability rather than repeating the glue calculation.

The independent analytic witness uses `f(r)=1`: it is polynomially bounded, but against the noncompact radial volume factor `sinh(r)^2 dr`,

`integral_0^R sinh(r)^2 dr = sinh(2R)/4 - R/2`,

which diverges as `R -> infinity`. This proves only the logical point that polynomial boundedness alone does not imply noncompact Haar/radial integrability. It is **not** a calculation of the causal spinfoam vertex and is **not** evidence that that vertex diverges.

Accordingly:
- automatic transfer of the standard EPRL theorem = not established;
- causal-vertex finiteness = not established;
- causal-vertex divergence = not established;
- family terminality = false;
- D7 authorization = false.

## Publication impact

Paper III: `NOT_NEEDED` — no new general methodology rule beyond the already-frozen same-realization/resource-closure semantics.

Paper IV: `READY` — state the theorem-applicability gap explicitly and require either an explicit Toller-kernel integrability/decay estimate, a theorem extending the relevant EPRL integrability class, or a direct finite normalized causal-vertex certificate before claiming vertex finiteness.

## Current blocker

`BLOCKED_MISSING_EXPLICIT_TOLLER_CAUSAL_VERTEX_INTEGRABILITY_DECAY_BOUND_OR_EXTENSION_THEOREM_OR_DIRECT_FINITE_NORMALIZED_VERTEX_CERTIFICATE_PLUS_LAMBDA_F_WEIGHTED_COMPLETE_STACK_FINITE_NORMALIZATION_AREA_CUTOFF_REMOVAL_PLUS_SAME_REALIZATION_UV_TO_CAUSAL_LARGE_SPIN_REGGE_GR_TRANSPORT_WITH_PARAMETER_IDENTITY_NORMALIZED_OBSERVABLE_COMMON_DOMAIN_COMPARATOR_AND_PROPAGATED_ERROR`

No terminal D7 classifier is authorized while D7-S2, D7-S3, or D7-S4 remains open.
