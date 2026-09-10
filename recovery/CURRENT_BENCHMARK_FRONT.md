# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **190**  
**Phase:** **RQIR Core v1.0 FROZEN / all known-school first-pass audits complete / Hořava material branch fork frozen / family-level D7 blockers active**.

## Stable metrics

- R1 repository readiness: **100%**.
- R2 methodology/material readiness: **100%**.
- Candidate Gravity R3: **24%**, inactive.
- Candidate activation condition: D7=`NEW_REQUIRED` only.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.

No readiness promotion in Iter190.

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
- terminal family-level rows: **1/14** (GR/EFT baseline).
- nonterminal family rows: **13/14**.
- untouched Tier-1 rows: **0/14**.
- Tier-2 unresolved classifications: **0**.
- defined scoped child residuals remain **9**; Iter190 adds a family-structure PASS but no new comparator residual.
- scoped scientific FAIL rows: **2**.

No scoped child result is promoted to family exclusion or sufficiency.

## Iter190 — Hořava projectability fork and extra-mode object

Primary-source audit establishes that projectability changes the constraint/scalar sector materially. The projectable theory has a dynamical extra scalar in cosmological perturbations and documented ghost/tachyon/strong-coupling issues in relevant regimes; the BPS non-projectable extension changes the scalar quadratic action and has a distinct Lorentz-violating scalar-tensor IR limit.

Classification:

**`PASS_RQIR_GATE__HORAVA_MATERIAL_PROJECTABILITY_FORK_AND_EXTRA_MODE_OBJECT_IDENTIFIED`**.

This is a scoped family-structure PASS, not a terminal Hořava-family result.

Authority:

- `paper_iv/O_HORAVA_PROJECTABLE_NONPROJECTABLE_FAMILY_FORK_AUDIT_2026-09-10.md`
- Cerioni & Brandenberger, arXiv:1007.1006
- Koyama & Arroja, arXiv:0910.1998
- Blas, Pujolas & Sibiryakov, arXiv:0909.3525
- Papazoglou & Sotiriou, arXiv:0911.1299; BPS comment arXiv:0912.0550

## Hořava family status

Parent status remains:

`HORAVA_LIFSHITZ = PARTIAL_SUBFAMILY_ONLY`.

The family is now explicitly forked into two material branches that cannot inherit one another's terminal status without an equivalence/reduction theorem:

1. `PROJECTABLE_HORAVA` — concrete target is the normalized extra-scalar observable/dispersion carried along one same-realization UV->IR trajectory with stability/strong-coupling domain and controlled remainder.
2. `NONPROJECTABLE_HORAVA/BPS` — concrete target is its distinct low-energy scalar-tensor observable carried from a frozen UV realization with controlled matching/remainder.

No family-level comparator residual is yet defined because neither complete same-realization UV->IR certificate is in hand.

Next exact gates:

**`HORAVA_PROJECTABLE_UV_TO_IR_TRAJECTORY_PLUS_EXTRA_SCALAR_NORMALIZED_OBSERVABLE_CERTIFICATE`**

and

**`HORAVA_NONPROJECTABLE_BPS_UV_TO_IR_TRAJECTORY_PLUS_SCALAR_TENSOR_COMPARATOR_CERTIFICATE`**.

## Iter189 validation

Iter189 methodology CI run `34431893468`, job `102728958236`, is now validated SUCCESS. All methodology self-test steps completed successfully, including frozen-core governance, executable registry, independent R1/R2 recomputation, methodology orchestrator and repository-completion validation.

## D7 after Iter190

No family-level row changed terminal status:

- D2 = false / NOT_CLOSED;
- D4 = false / NOT_CLOSED;
- D7 = false / NOT_CLOSED;
- `EXISTING_SUFFICIENT = false`;
- `ADAPT_EXISTING = false`;
- `HYBRID_REQUIRED = false`;
- `NEW_REQUIRED = false`;
- global decision = **`NOT_YET_AUTHORIZED`**;
- Candidate Gravity activation = false.

## Heavy compute

**IDLE.** Current Hořava blockers are structural/provenance/RG ancestry. IR parameter scans cannot manufacture a missing same-realization UV->IR map.

## Next order

1. Validate Iter190 methodology CI/reproducibility chain.
2. Attack the projectable Hořava UV->IR trajectory certificate first, because the extra scalar already supplies a concrete observable target.
3. Require exact action/operator basis, running/trajectory authority, IR scalar normalization and stability/strong-coupling domain, error/remainder and same-domain GR/EFT comparator.
4. Then disposition the non-projectable/BPS branch independently.
5. If primary literature does not supply a same-realization UV->IR object, mark the exact branch gate BLOCKED and switch to the next high-probability family blocker; do not weaken RQIR.
6. Rerun executable D7 only after a family-level terminal change or a material decision-ledger update.
