# Paper IV LQG Toller SU(2)-Haar Half-Link Glue Audit — Iter303

Date: 2026-09-11

## Authority and frozen scope
Primary objects: Han, *Summation and triangulation independence of Lorentzian spinfoam amplitudes for all LQG*, PRD 113, 084034 (2026); Bianchi–Chen–Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, arXiv:2604.24945 (2026); and the causal gamma-simple Toller vertex construction of arXiv:2601.23162 (2026).

The prospectively frozen contract is `benchmarks/lqg_iter303_toller_su2_haar_glue.json`. The question is narrower than Iter302: although a fixed Toller branch is not an `SL(2,C)` representation, does Han's *SU(2) boundary Haar/Schur contraction* still act on the matching finite magnetic-index spaces?

## Machine result
Scientific run `34614776339` on exact head `d2238ee1e3e43b16ec550a49317c2aab459fdc01`: five independent probes ran with `fail-fast:false`, `max-parallel:5`; aggregate executed only after all probes succeeded.

Independent probes:
1. source/covariance contract;
2. exact Schur-Haar contraction;
3. mismatched-spin orthogonality;
4. branch bilinearity/cross-term contraction;
5. fail-closed scope guard.

All five probes plus aggregate = SUCCESS. Methodology run `34614776311` = preflight + 4/4 shards + aggregate/bundle SUCCESS.

Summary artifact `10269418152`; artifact digest `sha256:0cf3f16acf0a00211ef4cb55f009a5eaff296903b6ed6b38d2718bbedc4a662f`; raw summary digest `sha256:b638c92c7790f660a14d64410eda2c699a7589a73aebc12e5ce3058061095acf`.

Exact machine facts:
- fixed-spin Toller SU(2)-Haar half-link glue compatibility = true;
- exact Schur contraction checked for dimensions `d=1..6`;
- 49 spin channels checked; all 42 mismatched channels vanish;
- branch bilinearity checked independently for `d=2,3,4,5`;
- a fixed Toller branch remains *not* an `SL(2,C)` group representation;
- generalized causal-vertex finiteness = not proven;
- `lambda_f`-weighted causal complete-stack finiteness/normalization/cutoff control = not proven;
- same-realization UV→causal-Regge/GR transport = not proven;
- family terminal = false; D7 authorized = false.

## Frozen classification
`PASS_SCOPED_FIXED_SPIN_TOLLER_BLOCK_SU2_HAAR_HALF_LINK_GLUE_COMPATIBILITY__SCHUR_CONTRACTION_SURVIVES_WITHOUT_SL2C_BRANCH_REPRESENTATION_LAW__CAUSAL_VERTEX_FINITE_NORMALIZATION_STACK_CUTOFF_AND_UV_IR_TRANSPORT_REMAIN_OPEN`

## Interpretation
Iter302 correctly forbade silently inheriting the ordinary `SL(2,C)` representation-composition law branchwise. Iter303 shows that this does **not** obstruct the separate SU(2)-Haar/Schur boundary contraction used in Han's half-link gluing: the contraction is an index-space orthogonality identity and survives at fixed matched spin without requiring the Toller branch itself to be an `SL(2,C)` representation.

This removes one sub-blocker only. It is not a finiteness proof for the generalized causal vertex, not a proof of the finite normalized `lambda_f`-weighted complete-stack amplitude or cutoff removal, and not the same-realization UV→IR observable/error certificate.

## Current blocker
`BLOCKED_MISSING_FINITE_NORMALIZED_GENERALIZED_CAUSAL_VERTEX_AND_LAMBDA_F_WEIGHTED_COMPLETE_STACK_FINITE_NORMALIZATION_AREA_CUTOFF_REMOVAL_PLUS_SAME_REALIZATION_UV_TO_CAUSAL_LARGE_SPIN_REGGE_GR_TRANSPORT_WITH_PARAMETER_IDENTITY_NORMALIZED_OBSERVABLE_COMMON_DOMAIN_COMPARATOR_AND_PROPAGATED_ERROR`
