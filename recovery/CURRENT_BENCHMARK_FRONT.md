# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **194**  
**Phase:** **RQIR Core v1.0 FROZEN / Hořava material branch census expanded / U(1)+mixed-derivative disposition next**.

## Stable metrics

- R1 repository readiness: **100%**.
- R2 methodology/material readiness: **100%**.
- Candidate Gravity R3: **24%**, inactive.
- Candidate activation condition: D7=`NEW_REQUIRED` only.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.
- No readiness promotion in Iter194.

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

## Validation consumed

Iter193 methodology CI run `34443342721` on exact head `c2cece01006a4d1bc915e46d45b9ab90fd5869c1` completed successfully. Iter193 is therefore validated repository authority.

## Iter194 — Hořava material-branch exhaustion audit

The previous two-branch representation (standard projectable + healthy non-projectable/BPS) is not exhaustive under the frozen Paper-IV rule that materially distinct constraint/DOF structures cannot be silently merged.

Minimum material branch census is now frozen as:

1. `H0_STANDARD_PROJECTABLE` — tracked, BLOCKED on AF marginal trajectory → relevant IR couplings → normalized extra-scalar same-realization map.
2. `H1_HEALTHY_NONPROJECTABLE_BPS` — tracked, BLOCKED on complete 3+1 UV RG trajectory → IR khronometric observable map.
3. `H2_PROJECTABLE_U1_EXTENDED` — material independent subbranch: enlarged local U(1) gauge symmetry changes the constraint/scalar sector; BLOCKED on its own 3+1 quantum UV→IR comparator certificate.
4. `H3_NONPROJECTABLE_U1_EXTENDED` — material independent subbranch: generic theory contains a scalar; scalar-free locus requires exact zeros of marginal couplings expected to be regenerated quantum mechanically; BLOCKED on generic same-realization UV→IR comparator certificate.
5. `H4_MIXED_DERIVATIVE` — material independent operator/kinetic class. Published minimal realization has an additional scalar degree of freedom unstable at low energy: scoped scientific negative result only, not yet a full mixed-derivative family FAIL.

Authority:
- `paper_iv/O_HORAVA_FAMILY_MATERIAL_BRANCH_EXHAUSTION_AUDIT_2026-09-10.md`
- `paper_iv/HORAVA_MATERIAL_BRANCH_MAP_2026-09-10.json`

Governance classification:

**`PASS_GOVERNANCE_GATE__HORAVA_MATERIAL_BRANCH_CENSUS_EXPANDED_AND_NONREDUCTION_CERTIFIED_FOR_U1_AND_MIXED_DERIVATIVE_CLASSES`**.

This is not a family scientific PASS/FAIL and defines no Hořava family residual.

## Hořava parent status

`HORAVA_LIFSHITZ = PARTIAL_SUBFAMILY_ONLY`.

The branch-exhaustion audit shrinks ambiguity about what must be dispositioned, but adds no license to promote scoped children to the parent.

Exact next family gate:

**`HORAVA_U1_PROJECTABLE_AND_NONPROJECTABLE_QUANTUM_IR_COMPARATOR_DISPOSITION_PLUS_MIXED_DERIVATIVE_COMPLETION_SCOPE_CERTIFICATE`**.

## D7 after Iter194

No family-level row became terminal:

- D2 = NOT_CLOSED;
- D4 = NOT_CLOSED;
- D7 = NOT_CLOSED;
- global decision = **`NOT_YET_AUTHORIZED`**;
- `NEW_REQUIRED=false`;
- Candidate Gravity activation=false, R3=24%.

## Heavy compute

**IDLE.** The next Hořava tasks are structural/provenance/matching questions. A numerical scan cannot manufacture the missing same-realization quantum ancestry or a theorem extending the mixed-derivative instability to the whole material class.

## Exact next order

1. Run/consume methodology CI for Iter194.
2. Audit H2/H3 for authenticated 3+1 quantum UV authority plus normalized IR observable/comparator map; if absent, freeze BLOCKED, not FAIL.
3. Audit whether H4 minimal low-energy instability extends to the full materially allowed mixed-derivative class or only the minimal realization.
4. If all Hořava material branches then have explicit terminal-or-BLOCKED dispositions, freeze a family-level nonterminal branch-exhaustion certificate and move to the next analytically closable Tier-1 blocker.
5. Rerun D7 only after a family-level terminal change or decision-ledger material change.
