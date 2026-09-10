# KMQGB Current Benchmark Front

**Updated:** 2026-09-10  
**KMQGB iteration:** **185**  
**Phase:** **RQIR Core v1.0 FROZEN / Paper-IV major-school coverage / PF2 nonlocal-QG**.

## Stable metrics

- R1 Repository readiness: **100%**.
- R2 KMQGB methodology/material readiness: **100%**.
- R3 Candidate Gravity scientific readiness: **24%**.
- Candidate Gravity: **inactive**; activation requires D7=`NEW_REQUIRED`.
- Historical PF1: 5/5 terminal in scoped records.
- AS/LQG/CFS Closure Wave 02: **0/3 terminal**.

No R1/R2/R3 promotion in Iter185. RQIR Core v1.0 remains FROZEN.

## Paper-IV global state

- D1 — PASS.
- D2A framework-set coverage — NOT_CLOSED.
- D2B complete objects — NOT_CLOSED.
- D2 — `NOT_CLOSED_COVERAGE_AND_OBJECTS`.
- D3 — PARTIAL.
- D4 — `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`.
- D5 — PASS.
- D6 — `PASS_RULE_TARGETS_OPEN`.
- D7 — NOT_CLOSED.
- Global decision — **`NOT_YET_AUTHORIZED`**.
- `NEW_REQUIRED` — forbidden.

## PF2 nonlocal-QG progress

Parent family:

**`NONLOCAL_QG = PARTIAL_SUBFAMILY_ONLY`**.

### PF2-01A — Ricci/EOM-squared tree S-matrix

`PASS_RQIR_GATE__EXACT_COMPARATOR_IDENTITY__TREE_S_MATRIX`

`A_n^NLQG(tree)=A_n^GR(tree)` in the declared field-redefinition-equivalent class. Exact zero residual after GR subtraction; not zero-fill and not FAIL.

### PF2-01B1 — Weyl `H_K` eikonal causality

**`FAIL_RQIR_GATE__SCOPED_EIKONAL_CAUSALITY_TIME_ADVANCE`**.

The frozen source calculation yields a Shapiro time advance in the stated high-energy weak-coupling eikonal regime. This is the first explicit scoped scientific FAIL in the PF2 coverage wave.

### PF2-01B2 — Weyl `H_T` matched control

**`PASS_RQIR_GATE__SCOPED_EIKONAL_CAUSALITY_CONTROL`**.

The dangerous time advance is absent in the source analysis for this distinct form-factor realization.

The B1/B2 pair demonstrates form-factor dependence. No child PASS or FAIL is promoted to the parent family.

Authorities:

- `post_freeze_paper_iv_wave_02/PF2_01B_NONLOCAL_WEYL_CAUSALITY/audit.md`
- `.../result_hk.json`
- `.../result_ht.json`

## Executable scope firewall

`code/paper_iv_framework_coverage_validator.py` now enforces for every scoped child row:

- a valid Tier-1 parent;
- complete declared child-domain object;
- defined child result;
- `counts_as_new_required_exclusion=false`;
- `global_sufficiency=false`.

Thus a local scientific FAIL cannot silently become family-level exclusion.

## D4 evidence status

Required Tier-1 rows with defined complete residual: **1/11** (GR/EFT baseline).

Defined scoped child results: **4**:

1. string/dual-resonance rigidity;
2. nonlocal Ricci/EOM-squared exact GR identity;
3. nonlocal Weyl `H_K` causality FAIL;
4. nonlocal Weyl `H_T` causality PASS control.

Scoped child scientific FAILs: **1**.

## Exact active gate

**`PF2_01B3_RIEMANN_WEYL_AMPLITUDE_RESIDUAL`**

Published authority already shows that adding an independent nonlocal Riemann-sector form factor can alter tree-level graviton amplitudes. The unresolved RQIR question is stronger:

> does a fixed normalized nonlocal Riemann/Weyl amplitude retain a comparator-orthogonal residual after quotienting the full allowed local higher-curvature EFT basis at the same order/domain?

Required payload:

`{fixed Riemann/Weyl form factor, external states/helicities, normalized amplitude vector, identical-order GR+local higher-curvature EFT comparator basis, form-factor parameter incidence, pole/unitarity prescription, causality status, approximation/error ledger, comparator-orthogonal residual}`.

## Parallel PF2-01B4

2026 Gödel/CTC exact-vacuum evidence remains a scope-classification object. It must not be combined with B1/B2 unless realization/domain mapping is explicit.

## Other major-school queue

After the nonlocal parent reaches a justified stopping/terminal point:

1. CDT/EDT;
2. Hořava-Lifshitz;
3. causal sets;
4. perturbative/higher-derivative QG;
5. GFT/tensor independence/reduction audit.

AS/LQG/CFS blockers remain open unchanged.

## Heavy compute

**IDLE.** The current front is analytic comparator-basis/attribution work.

## Exact continuation order

1. Build PF2-01B3 local-EFT comparator quotient for a fixed Riemann/Weyl nonlocal realization.
2. Classify PF2-01B4 Gödel/CTC scope separately.
3. Keep NONLOCAL_QG partial until materially independent branches are exhausted/reduced.
4. Proceed through the omitted-family queue.
5. Only after D2A+D2B and global D4 close may D7 choose EXISTING/ADAPT/HYBRID/NEW.
6. Build Candidate Gravity only if D7 returns exactly `NEW_REQUIRED`, then run it through unchanged RQIR.
