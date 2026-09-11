# Current Benchmark Front
Updated: 2026-09-11
Iteration: Iter304 Toller causal-vertex finiteness-theorem transfer applicability gap validated; Iter303 SU(2)-Haar glue compatibility retained
Authoritative operational-saturation milestone: Iter270
Authoritative D7 infrastructure milestone: Iter272
Authoritative 15-row census synchronization milestone: Iter276

## Global lock
- RQIR Core v1.0 remains FROZEN.
- Tier-1 census = 15 families.
- Strict terminal coverage = 1/15; strict nonterminal = 14/15.
- Candidate-family terminal coverage = 0/14.
- Tier-2 unresolved = 0.
- D1 = PASS.
- D2 = NOT_CLOSED_COVERAGE_AND_OBJECTS.
- D3 = PARTIAL.
- D4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D5 = PASS.
- D6 = PASS_RULE_TARGETS_OPEN.
- D7 = NOT_CLOSED / NOT_YET_AUTHORIZED.
- D7-S0 = PASS; D7-S1 = PASS; D7-S2 = NOT_CLOSED; D7-S3 = NOT_CLOSED; D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED; D7-S5 = NOT_AUTHORIZED; D7-S6 = INACTIVE.
- `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, and `NEW_REQUIRED` are forbidden while S2-S4 remain open.
- Candidate Gravity remains inactive at canonical R3 = 24%.

## Authoritative LQG/spinfoam progression
The validated Iter281-297 chain established: a complete-stack/refinement architecture, scoped physical-continuum/physical-state components, small-spin UV and large-spin Einstein/Regge endpoints, a Lorentzian entropy observable anchor, a causal generalized-EPRL/KKL endpoint, a nonempty conditional Han/generalized-causal per-complex overlap, orientation-level lift through positive face multiplicities, and a formal memberwise causal-vertex substitution. None of these proves the required family-level same-realization complete-stack transport.

### Iter298 — fixed causal sector versus full standard EPRL product
Contract: `benchmarks/lqg_iter298_causal_sector_decomposition.json`.
Scoped result: one fixed causal Toller-sign assignment is one component of the formal expansion of the full standard EPRL `D`-product; generic algebraic identity with the full product is unavailable without additional vanishing, an admissible sector sum, or a new causal factorization theorem.
Classification: `PASS_SCOPED_ALGEBRAIC_NONIDENTITY_OF_ONE_FIXED_CAUSAL_TOLLER_SECTOR_WITH_FULL_STANDARD_EPRL_D_PRODUCT__HAN_HALF_LINK_EQUIVALENCE_REQUIRES_EXPLICIT_SECTOR_SUM_OR_NEW_CAUSAL_FACTORIZATION_PROOF`.
Scientific run `34598197609`; summary artifact `10263221608`; artifact digest `sha256:393effdb28a73118e587c9ba49e5caf07cde78e108de6478c4bdc8c384805c56`; raw digest `sha256:c1d445802eb484457526355e99a252a67448a935c0e012e724001f1fec3713ee`.
Boundary: scoped formal result only; no no-go and no family promotion.

### Iter299 — unrestricted sector-sum recovery
Contract: `benchmarks/lqg_iter299_causal_sector_sum_recovery.json`.
Exact formal result: summing every local Toller-sign sector with unit weight reconstructs the standard `D`-product by distributivity.
Classification: `PASS_SCOPED_EXACT_UNRESTRICTED_TOLLER_SECTOR_SUM_RECONSTRUCTS_STANDARD_D_PRODUCT__CAUSALLY_ADMISSIBLE_WEIGHTED_SECTOR_MEASURE_HAN_GLUE_FACTORIZATION_AND_UV_IR_TRANSPORT_REMAIN_UNPROVEN`.
Scientific run `34601894692`; scientific head `e0ec53785f312871b91307f8df854b4a8edd66c5`; summary artifact `10264955714`; artifact digest `sha256:7db47f3b76568e8de11832c6447c4cb27779bceec41318934a435e12ea178f34`; raw digest `sha256:5101d4ffce7b2307e035a1a5b64402527712ec90746d6ed47eb6ed1236f96f95`.
Boundary: the unrestricted unit-weight algebraic identity is not a theorem that the physical causal measure has unrestricted support or those weights.

### Iter300 — generic sector-weight uniqueness
Contract: `benchmarks/lqg_iter300_sector_weight_uniqueness.json`.
In a generic algebraically independent sector-monomial basis, exact standard-`D` recovery requires full support and `w_sigma=1`; recovery up to nonzero global normalization `C` requires full support and uniform `w_sigma=C`.
Classification: `PASS_SCOPED_GENERIC_COEFFICIENT_MATCHING_REQUIRES_FULL_SECTOR_SUPPORT_AND_UNIFORM_WEIGHTS_UP_TO_GLOBAL_NORMALIZATION_FOR_STANDARD_D_PRODUCT_RECOVERY__PHYSICAL_CAUSAL_MEASURE_HAN_GLUE_AND_UV_IR_TRANSPORT_REMAIN_UNPROVEN`.
Scientific run `34602793992`; scientific head `f8e661a6ff52fd9ee00a2a21cac4528485a7b8a3`; summary artifact `10265255466`; artifact digest `sha256:65d443d95a63376f9454bafc47a87ad71c8014eb78bf50b1628935acd83e9809`; raw digest `sha256:74210a18880ce7e202bc7703fc31fb472b4b65246464c5413adfd5c335a42e91`.
Boundary: source-specific relations, cancellations, and alternative causal factorization remain open.

### Iter301 — source-specific causal sector support
Contract: `benchmarks/lqg_iter301_causal_sector_support.json`.
The `sigma_a` construction induces `kappa_ab=sigma_a sigma_b`. On a connected graph its kernel is the global flip and the induced support has `2^(V-1)` sectors; equivalent edge signs obey positive cycle product. On K5 this gives exactly 16 induced causal sectors versus 1024 unrestricted wedge-sign sectors.
Classification: `PASS_SCOPED_SOURCE_SPECIFIC_SIGMA_INDUCED_CAUSAL_SECTOR_SUPPORT_IS_EXACT_CYCLE_EVEN_CUT_SPACE_AND_STRICTLY_SMALLER_THAN_UNRESTRICTED_TOLLER_SUPPORT_ON_CYCLIC_VERTEX_GRAPHS__NO_GENERIC_FULL_D_PRODUCT_RECOVERY_FROM_CAUSAL_SUPPORT_ALONE__NO_NO_GO_AND_HAN_GLUE_STACK_UV_IR_TRANSPORT_REMAIN_OPEN`.
Scientific run `34608395886`; scientific head `e2f6ea37e1bfcfcc90347e2366b0233fd56d18c1`; methodology `34608395856`; summary artifact `10267280795`; artifact digest `sha256:61f8c98a77a45b2cdd7806f44903ab187aa58f632612db052e9a6098853ffa3a`; raw digest `sha256:701a568536a1f1581878c78e1b0d7df2f45e4dec5c6dea0d1d729a65bd81ca74`.
Boundary: support mismatch is not scientific FAIL; post-Haar identities, source-specific cancellations, extended physically justified causal sums, or a new factorization remain admissible.

### Iter302 — Toller branch representation-composition audit
Primary authority: Bianchi–Chen–Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, Physical Review D 114, 046014 (published 13 August 2026), DOI `10.1103/v3kc-4n3n`, arXiv:2604.24945. The Iter302 scientific run prospectively froze the arXiv-identified source object; Iter302A records the later checked peer-reviewed provenance without changing the frozen claims.
Contract: `benchmarks/lqg_iter302_toller_half_link_composition.json`.
Source-grounded result: `T^(+)+T^(-)=D`, while a fixed individual Toller branch is not itself a group representation. Therefore ordinary Wigner-`D` representation composition/half-link factorization cannot be silently inherited branchwise. Additive completion before composition recovers the standard `D` object; cross-branch or post-integration identities remain open.
Classification: `PASS_SCOPED_SOURCE_GROUNDED_TOLLER_BRANCH_NONREPRESENTATION_SHARPENS_HALF_LINK_GLUE_BLOCKER__NAIVE_FIXED_BRANCH_STANDARD_REPRESENTATION_FACTORIZATION_NOT_AVAILABLE__ADDITIVE_COMPLETION_OR_SOURCE_SPECIFIC_CROSS_BRANCH_POST_INTEGRATION_GLUE_REMAINS_OPEN__NO_NO_GO`.
Scientific run `34614044780` on head `3453a20e48ff7ca859d2fcaa8175b6fbe7cdca90`; 4/4 independent guards plus aggregate SUCCESS; methodology `34614044721` SUCCESS; reproducibility `34614177446` SUCCESS. Summary artifact `10269636788`; artifact digest `sha256:23fa9439b92fd815f07a10ee01e9ed47ab1aedf928dee460d13664b7bdd2f0b4`; raw summary digest `sha256:7b5f42e0e9b98bd4ffbac58a367107e77c9105aa4b57bdd22e89f679b6c2c273`.
Boundary: no causal-spinfoam no-go, no Han half-link/Haar-glue equivalence, no causal-stack finiteness/normalization/cutoff certificate, no same-realization UV→Regge/GR transport, no family promotion, and D7 remains unauthorized.
Audit: `paper_iv/P_LQG_TOLLER_HALF_LINK_COMPOSITION_SCOPE_AUDIT_ITER302_2026-09-11.md`.
Peer-reviewed authority delta: `paper_iv/P_LQG_TOLLER_AUTHORITY_DELTA_ITER302A_2026-09-11.md`.

### Iter303 — fixed-spin Toller SU(2)-Haar half-link glue
Contract: `benchmarks/lqg_iter303_toller_su2_haar_glue.json`.
Scientific run `34614776339` on exact head `d2238ee1e3e43b16ec550a49317c2aab459fdc01`: five independent probes in parallel plus aggregate SUCCESS. Methodology `34614776311`: SUCCESS. Summary artifact `10269418152`; artifact digest `sha256:0cf3f16acf0a00211ef4cb55f009a5eaff296903b6ed6b38d2718bbedc4a662f`; raw summary digest `sha256:b638c92c7790f660a14d64410eda2c699a7589a73aebc12e5ce3058061095acf`.

Machine result: fixed-spin Toller SU(2)-Haar half-link glue compatibility = PASS; exact Schur contraction dimensions `1..6`; 49 spin channels checked with 42 mismatched channels zero; branch bilinearity dimensions `2..5`; fixed Toller branch remains not an `SL(2,C)` representation.

Classification: `PASS_SCOPED_FIXED_SPIN_TOLLER_BLOCK_SU2_HAAR_HALF_LINK_GLUE_COMPATIBILITY__SCHUR_CONTRACTION_SURVIVES_WITHOUT_SL2C_BRANCH_REPRESENTATION_LAW__CAUSAL_VERTEX_FINITE_NORMALIZATION_STACK_CUTOFF_AND_UV_IR_TRANSPORT_REMAIN_OPEN`.

Boundary: causal-vertex finiteness, `lambda_f`-weighted complete-stack finite normalization/cutoff removal, and same-realization UV→causal-Regge/GR transport remain open. No family promotion; D7 remains unauthorized.

### Iter304 — Toller causal-vertex finiteness-theorem transfer
Contract: `benchmarks/lqg_iter304_toller_finiteness_transfer.json`.
Scientific run `34622448515` on exact head `b6365b863fea2e6c61c7bcd0848deac0c81f4dc9`: four independent probes in parallel plus aggregate SUCCESS. Methodology `34622448482`: SUCCESS. Summary artifact `10272398533`; artifact digest `sha256:ad9072614d42f6f004b9fae8d3225c678e67315af84c7c3cf2a3ffb700e2280a`; raw summary digest `sha256:233709ebaceee04857e04b8b2de89aa84a7d9982e80657e3e4d0af331d428c80`.

Machine result: Kamiński's positive 3-edge-connected standard-EPRL integrability theorem is not automatically transferable to a sign-selected fixed-causal Toller vertex from polynomial boundedness alone. Polynomial boundedness is logically insufficient for noncompact Haar/radial integrability; no explicit source extension theorem was found in the frozen contract.

Classification: `PASS_SCOPED_STANDARD_EPRL_3_EDGE_CONNECTED_FINITENESS_THEOREM_NOT_AUTOMATICALLY_TRANSFERABLE_TO_FIXED_CAUSAL_TOLLER_VERTEX_FROM_POLYNOMIAL_BOUNDEDNESS_ALONE__EXPLICIT_TOLLER_INTEGRABILITY_BOUND_OR_EXTENSION_THEOREM_REQUIRED__NO_DIVERGENCE_NO_GO_OR_FAMILY_PROMOTION`.

Boundary: this is an applicability gap, not a divergence result or no-go. Causal-vertex finiteness remains unproven; `lambda_f`-weighted complete-stack finite normalization/cutoff removal and same-realization UV→causal-Regge/GR transport remain open. No family promotion; D7 remains unauthorized.

## Infrastructure note
The old `iter299-recovery-integration` workflow can fire and fail on later heads because its recovery preconditions are stale. This is an infrastructure/synchronization defect only. It must not be interpreted as a scientific failure; the current scientific and methodology workflows remain authoritative.

## Publication handoff
`recovery/PUBLICATION_IMPACT_LEDGER.md` is the manuscript-impact authority. Iter298-302 require Paper-IV scoped wording only; Paper III receives no new general rule. The ledger must preserve the distinction between formal algebra/support/composition results and family-level evidence.

## Current blocker and next permitted gate
LQG/spinfoam remains `PARTIAL/BLOCKED`, not FAIL and not family-level PASS.

Current blocker:
`BLOCKED_MISSING_EXPLICIT_TOLLER_CAUSAL_VERTEX_INTEGRABILITY_DECAY_BOUND_OR_EXTENSION_THEOREM_OR_DIRECT_FINITE_NORMALIZED_VERTEX_CERTIFICATE_PLUS_LAMBDA_F_WEIGHTED_COMPLETE_STACK_FINITE_NORMALIZATION_AREA_CUTOFF_REMOVAL_PLUS_SAME_REALIZATION_UV_TO_CAUSAL_LARGE_SPIN_REGGE_GR_TRANSPORT_WITH_PARAMETER_IDENTITY_NORMALIZED_OBSERVABLE_COMMON_DOMAIN_COMPARATOR_AND_PROPAGATED_ERROR`

Exact next permitted gate:
`D7_S2_LQG_EXPLICIT_TOLLER_CAUSAL_VERTEX_INTEGRABILITY_THEOREM_OR_DIRECT_FINITE_NORMALIZED_VERTEX_CERTIFICATE__THEN_LAMBDA_F_WEIGHTED_COMPLETE_STACK_CUTOFF_CONTROL__THEN_SAME_REALIZATION_UV_TO_CAUSAL_REGGE_GR_TRANSPORT`

Do not launch the terminal D7 classifier while D7-S2, D7-S3, or D7-S4 remains open. Missing published objects remain blockers, not evidence of impossibility.
