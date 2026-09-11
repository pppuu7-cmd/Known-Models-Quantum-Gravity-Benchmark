# RECOVERY DELTA 272 — D7 staged decision wrapper

Date: 2026-09-11

## Purpose

Start the global D7 decision campaign conservatively, preserving all frozen RQIR/Paper-IV scientific rules while making the remaining decision path explicit and auditable.

## Added artifacts

1. `protocol/PAPER_IV_D7_GLOBAL_DECISION_CONTRACT.json`
   - commit `ed0412aace9e1c76af1f18022e4aa9a1f0ad7989`
   - additive/non-redefining D7 wrapper;
   - defines D7-S0 through D7-S6;
   - defines only four authorized terminal outcomes after prerequisites close: `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED`;
   - mandates `NOT_AUTHORIZED` before D7-S0..S4 close;
   - explicitly forbids BLOCKED→FAIL, scoped→family promotion without proof, and operational-saturation→NEW_REQUIRED shortcuts.

2. `paper_iv/PAPER_IV_D7_READINESS_STATE.json`
   - commit `0da2294b49a1b7ec9ec2b723ff4bf8f72bc43613`
   - machine-readable stage state and separated readiness metrics.

3. `paper_iv/PAPER_IV_D7_STAGE0_DECISION_CONTRACT_AUDIT_ITER272_2026-09-11.md`
   - commit `9c706f0a1a363daee51d9787b06f0a20edc32182`
   - D7-S0 audit and explicit inheritance of Iter270 D7-S1 operational saturation.

4. `paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_272.json`
   - commit `0fa09c0cd3b2a77c0200154f2834e825d2b4058a`
   - records that no scientific status was promoted and all global D2/D4/D7 restrictions remain intact.

## Stage state after Iter272

- D7-S0 Frozen judge integrity: **PASS**.
- D7-S1 Internal saturation: **PASS**.
- D7-S2 Strict Tier-1 terminal coverage / D2A: **NOT_CLOSED**.
- D7-S3 Same-realization object completeness / D2B: **NOT_CLOSED**.
- D7-S4 Common-domain global comparability / D3-D4: **PARTIAL_GLOBAL_NOT_CLOSED**.
- D7-S5 Global outcome classifier: **NOT_AUTHORIZED**.
- D7-S6 Candidate Gravity activation/export: **INACTIVE**.

## Metrics that remain separate

- operational proving-ground readiness: **100%**;
- strict Tier-1 terminal rows: **1/14**;
- internally saturated/parked candidate rows: **13/13**;
- Tier-2 unresolved: **0**;
- internal actionable fronts: **0**;
- Candidate Gravity R3: **24%**;
- Candidate Gravity active: **false**;
- D2: **NOT_CLOSED_COVERAGE_AND_OBJECTS**;
- D4: **PARTIAL_GLOBAL_NOT_CLOSED**;
- D7: **NOT_CLOSED_NOT_YET_AUTHORIZED**;
- heavy compute: **IDLE**.

## Interpretation

Iter272 completes the *definition* of the ecological D7 path. It does not solve the missing external scientific objects. Therefore no known family is newly excluded, no Candidate Gravity model is activated, and `NEW_REQUIRED` remains forbidden.

The next scientific stage is D7-S2. Reopen a parked family only when a new authoritative object or explicit reduction/equivalence map can change the strict family-level status. Repeating already exhausted scans is not a valid D7 step.

## Validation

The pre-Iter272 authority head `963e3a1440fb067fc3f447852d749edec01ee111` was already green under repository methodology/reproducibility validation. Post-Iter272 validation must be checked on the newest head before D7 protocol infrastructure is certified at 100%.
