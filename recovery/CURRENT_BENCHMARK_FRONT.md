# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **193**  
**Phase:** **RQIR Core v1.0 FROZEN / projectable + non-projectable Hořava UV→IR blockers localized / family branch-exhaustion next**.

## Stable metrics

- R1 repository readiness: **100%**.
- R2 methodology/material readiness: **100%**.
- Candidate Gravity R3: **24%**, inactive.
- Candidate activation condition: D7=`NEW_REQUIRED` only.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.
- No readiness promotion in Iter193.

## Paper-IV global gates

- D1: PASS.
- D2A: NOT_CLOSED.
- D2B: NOT_CLOSED.
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
- scoped child residual count: **9**.
- scoped scientific FAIL rows: **2**.

## Iter193 — non-projectable/BPS Hořava 3+1 UV→IR audit

Primary literature establishes a healthy non-projectable IR theory with a physical khronon/extra-scalar sector and comparator-facing PPN/phenomenology. Separate quantum work establishes cancellation of dangerous nonlocal subdivergences, and the 2025/2026 Lagrangian-path-integral program gives explicit one-loop beta functions only in 2+1 dimensions.

What is still absent is one authenticated **3+1 same-realization** object connecting the microscopic non-projectable action to a UV fixed-point/asymptotically-free domain, a complete essential beta-function system and integrated RG trajectory, then through relevant lower-derivative operators into normalized IR khronometric couplings and a GR/EFT comparator with loop/truncation/matching remainder.

Therefore the non-projectable branch is frozen as:

**`BLOCKED_MISSING_REQUIRED_OBJECT__HORAVA_NONPROJECTABLE_3P1_UV_RG_TRAJECTORY_TO_IR_KHRONOMETRIC_OBSERVABLE_SAME_REALIZATION_MAP`**.

This is BLOCKED, not FAIL, defines no family-level residual, and does not authorize NEW_REQUIRED.

Authority: `paper_iv/O_HORAVA_NONPROJECTABLE_3P1_UV_IR_GAP_AUDIT_2026-09-10.md`.

## Hořava parent status

`HORAVA_LIFSHITZ = PARTIAL_SUBFAMILY_ONLY`.

Projectable branch:
`BLOCKED_MISSING_REQUIRED_OBJECT__HORAVA_PROJECTABLE_AF_MARGINAL_TRAJECTORY_TO_RELEVANT_IR_COUPLINGS_AND_NORMALIZED_EXTRA_SCALAR_SAME_REALIZATION_MAP`.

Non-projectable/BPS branch:
`BLOCKED_MISSING_REQUIRED_OBJECT__HORAVA_NONPROJECTABLE_3P1_UV_RG_TRAJECTORY_TO_IR_KHRONOMETRIC_OBSERVABLE_SAME_REALIZATION_MAP`.

Exact next family gate:

**`HORAVA_FAMILY_MATERIAL_BRANCH_EXHAUSTION_AND_TERMINAL_DISPOSITION_CERTIFICATE`**.

Audit whether other material Hořava realizations, especially U(1)-extended variants, are independent Paper-IV families/subfamilies or reduce to the tracked branches by an explicit physical map. Only after material-branch exhaustion may a family terminal disposition be considered.

## Validation / CI

Iter192 methodology run `34439484092` failed at generic JSON parsing with `recovery/state.json: Extra data`. The exact same scientific head was re-run after source inspection to determine whether this was a transient/check-out synchronization problem; no science criterion was modified. Iter193 itself triggers fresh methodology CI via the new commits and must be consumed before repository-validation is claimed.

## D7 after Iter193

No family-level row became terminal:

- D2 = NOT_CLOSED;
- D4 = NOT_CLOSED;
- D7 = NOT_CLOSED;
- global decision = **`NOT_YET_AUTHORIZED`**;
- `NEW_REQUIRED=false`;
- Candidate Gravity activation=false, R3=24%.

## Heavy compute

**IDLE.** Both Hořava blockers are structural/provenance/matching blockers; free numerical scans cannot construct the missing same-realization UV→IR ancestry.

## Exact next order

1. Consume Iter192 re-run and Iter193 methodology CI; repair only exact infrastructure/synchronization defects.
2. Execute `HORAVA_FAMILY_MATERIAL_BRANCH_EXHAUSTION_AND_TERMINAL_DISPOSITION_CERTIFICATE`.
3. If no additional independent material branch changes coverage, freeze Hořava family as nonterminal BLOCKED with explicit branch-exhaustion authority rather than promoting child results.
4. Move to the next analytically closable Tier-1 blocker.
5. Rerun D7 only after a family-level terminal change or material decision-ledger change.
