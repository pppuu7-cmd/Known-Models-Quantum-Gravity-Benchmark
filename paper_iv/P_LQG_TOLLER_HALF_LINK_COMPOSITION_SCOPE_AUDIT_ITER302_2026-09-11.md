# Paper IV LQG Toller Half-Link Composition Scope Audit — Iter302

Date: 2026-09-11

## Authority and frozen scope

Primary source object: Bianchi–Chen–Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, arXiv:2604.24945 (2026). The source relation used by this audit is `T^(+) + T^(-) = D`, together with the source statement that individual Toller matrices are functions on `SL(2,C)` rather than group representations. The audit asks only whether standard Wigner-`D` representation composition may be inherited branchwise after a fixed causal Toller replacement.

Prospective contract: `benchmarks/lqg_iter302_toller_half_link_composition.json`.

## Machine result

Scientific run: `34614044780` on head `3453a20e48ff7ca859d2fcaa8175b6fbe7cdca90`.

Four independent guards (`source_contract`, `branch_nonrepresentation`, `additive_completion`, `scope_boundary`) ran with `fail-fast:false`, `max-parallel:4`; aggregate executed only after the dependency barrier. All guards and aggregate passed.

Summary artifact: `10269636788` (`lqg-iter302-summary`).
Artifact digest: `sha256:23fa9439b92fd815f07a10ee01e9ed47ab1aedf928dee460d13664b7bdd2f0b4`.
Raw summary digest: `sha256:7b5f42e0e9b98bd4ffbac58a367107e77c9105aa4b57bdd22e89f679b6c2c273`.
Exact-head methodology CI: `34614044721` = SUCCESS. Reproducibility release `34614177446` = SUCCESS.

Frozen machine classification:

`PASS_SCOPED_SOURCE_GROUNDED_TOLLER_BRANCH_NONREPRESENTATION_SHARPENS_HALF_LINK_GLUE_BLOCKER__NAIVE_FIXED_BRANCH_STANDARD_REPRESENTATION_FACTORIZATION_NOT_AVAILABLE__ADDITIVE_COMPLETION_OR_SOURCE_SPECIFIC_CROSS_BRANCH_POST_INTEGRATION_GLUE_REMAINS_OPEN__NO_NO_GO`

Raw aggregate facts:
- `toller_additive_completion_recovers_D=true`;
- `fixed_toller_branch_representation_composition_available=false`;
- `naive_fixed_branch_standard_half_link_factorization_authorized=false`;
- generic two-half-link additive expansion contains four branch combinations, including two cross-branch terms;
- `post_integration_or_cross_branch_glue_identity_excluded=false`;
- `scientific_no_go_claim=false`;
- `han_half_link_haar_glue_equivalence_proven=false`;
- `causal_stack_finiteness_normalization_cutoff_control_proven=false`;
- `same_realization_uv_to_regge_gr_transport_proven=false`;
- `family_terminal=false`; `d7_authorized=false`.

## Scientific disposition

This is a scoped formal/source-grounded obstruction to silently inheriting ordinary representation composition branchwise. It is not a scientific FAIL of causal spinfoams and not a family-level result. Additive completion, cross-branch convolution, a Haar-integrated identity/cancellation, or a new causal factorization theorem remain admissible closure routes. Missing objects remain BLOCKED/undefined rather than evidence of impossibility.

The stale `iter299-recovery-integration` workflow failure on the same head is infrastructure-only; methodology CI and the Iter302 scientific workflow both passed and the stale workflow does not alter the scientific classification.

## Paper impact

Paper III: `NOT_NEEDED` — no new general methodology rule beyond already frozen same-realization/resource-closure semantics.

Paper IV: `READY` — distinguish fixed-branch Toller nonrepresentation and the resulting half-link inheritance restriction from a no-go claim; preserve the still-open cross-branch/post-integration/new-factorization routes and the downstream `lambda_f` stack-cutoff plus UV→causal-Regge/GR transport obligations.

## Global lock

No global promotion follows. Strict Tier-1 terminal coverage remains `1/15`; D2 remains `NOT_CLOSED_COVERAGE_AND_OBJECTS`; D4 remains `PARTIAL_GLOBAL_NOT_CLOSED`; D7 remains `NOT_CLOSED_NOT_YET_AUTHORIZED`; Candidate Gravity remains inactive at R3=24%.

## Next permitted LQG gate

`D7_S2_LQG_SOURCE_SPECIFIC_CROSS_BRANCH_OR_HAAR_INTEGRATED_CAUSAL_GLUE_IDENTITY_COMPATIBLE_WITH_HAN_HALF_LINKS_AND_FACE_FACTORIZATION__THEN_LAMBDA_F_WEIGHTED_STACK_NORMALIZATION_CUTOFF_AND_SAME_REALIZATION_UV_TO_CAUSAL_REGGE_GR_TRANSPORT`
