# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **191**  
**Phase:** **RQIR Core v1.0 FROZEN / Hořava projectable 3+1 AF marginal RG trajectory admitted / family-level D7 blockers active**.

## Stable metrics

- R1 repository readiness: **100%**.
- R2 methodology/material readiness: **100%**.
- Candidate Gravity R3: **24%**, inactive.
- Candidate activation condition: D7=`NEW_REQUIRED` only.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.

No readiness promotion in Iter191.

## Paper-IV global gates

- D1: PASS.
- D2A framework-set/family coverage: NOT_CLOSED.
- D2B complete same-realization objects: NOT_CLOSED.
- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`.
- D3: PARTIAL.
- D4: `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`.
- D5: PASS.
- D6: `PASS_RULE_TARGETS_OPEN`.
- D7: NOT_CLOSED.
- Global decision: **`NOT_YET_AUTHORIZED`**.

## Coverage status

- Tier-1 required rows: **14**.
- terminal family-level rows: **1/14**.
- nonterminal family rows: **13/14**.
- untouched Tier-1 rows: **0/14**.
- Tier-2 unresolved classifications: **0**.
- scoped child residual count remains **9**; Iter190–191 add scoped structural/RG PASS results but no family-level residual.
- scoped scientific FAIL rows: **2**.

## Iter190 — material Hořava branch fork

Projectable and non-projectable/BPS Hořava are frozen as materially distinct branches because projectability changes the physical constraint/scalar sector. A scoped result in one branch cannot be promoted to the family without branch-by-branch terminal disposition or a reduction/equivalence theorem.

Authority: `paper_iv/O_HORAVA_PROJECTABLE_NONPROJECTABLE_FAMILY_FORK_AUDIT_2026-09-10.md`.

Classification:
`PASS_RQIR_GATE__HORAVA_MATERIAL_PROJECTABILITY_FORK_AND_EXTRA_MODE_OBJECT_IDENTIFIED`.

## Iter191 — projectable 3+1 AF RG authority

Primary literature now closes the narrower claim that no 3+1 projectable UV trajectory is known:

- arXiv:2110.14688 derives the complete one-loop beta functions for marginal essential couplings and identifies candidate asymptotically free fixed points.
- arXiv:2411.13574 follows the 3+1 projectable RG flow numerically and finds asymptotically free trajectories spanning the unitarity-compatible lambda range, including `0 < lambda - 1 << 1`.

Classification:

**`PASS_RQIR_GATE__HORAVA_PROJECTABLE_3P1_ASYMPTOTICALLY_FREE_MARGINAL_RG_TRAJECTORY_AUTHORITY`**.

Authority:
`paper_iv/O_HORAVA_PROJECTABLE_3P1_RG_TRAJECTORY_SCOPE_AUDIT_2026-09-10.md`.

This is **not** a complete same-realization UV->IR certificate. The remaining missing object is the crossover/matching from the marginal z=3 trajectory through relevant lower-derivative couplings into a normalized IR extra-scalar observable with propagated loop/truncation/matching remainder and a same-domain GR/EFT comparator.

## Hořava parent status

`HORAVA_LIFSHITZ = PARTIAL_SUBFAMILY_ONLY`.

Projectable next gate:

**`HORAVA_PROJECTABLE_AF_RG_TO_IR_RELEVANT_COUPLING_CROSSOVER_PLUS_EXTRA_SCALAR_OBSERVABLE_MATCHING_CERTIFICATE`**.

Non-projectable next gate:

**`HORAVA_NONPROJECTABLE_BPS_UV_TO_IR_TRAJECTORY_PLUS_SCALAR_TENSOR_COMPARATOR_CERTIFICATE`**.

A phenomenological IR lambda scan is explicitly not a substitute for transporting one UV realization into the observable regime.

## Validation authority carried forward

Iter189 methodology CI run `34431893468`, job `102728958236`: validated SUCCESS, including frozen-core governance, executable registry, independent readiness recomputation, methodology orchestrator and repository-completion checks.

Iter190/191 changes require their own latest-head methodology validation before they are called repository-validated.

## D7 after Iter191

No family-level row became terminal:

- D2 = NOT_CLOSED;
- D4 = NOT_CLOSED;
- D7 = NOT_CLOSED;
- global decision = **`NOT_YET_AUTHORIZED`**;
- `NEW_REQUIRED=false`;
- Candidate Gravity activation=false, R3=24%.

## Heavy compute

**IDLE.** The live blocker is RG-to-IR matching/provenance and controlled remainder, not a free numerical scan.

## Exact next order

1. Validate the latest Iter191 head with methodology CI/reproducibility chain.
2. Search primary literature for a same-realization projectable crossover from the AF marginal trajectory to the relevant IR couplings and scalar mode normalization.
3. If no such object exists, freeze the projectable H1 subgate as `BLOCKED_MISSING_REQUIRED_OBJECT` with exact missing fields; do not infer scientific FAIL.
4. Then attack the non-projectable/BPS UV->IR trajectory independently.
5. Rerun D7 only after a family-level terminal change or other material decision-ledger change.
