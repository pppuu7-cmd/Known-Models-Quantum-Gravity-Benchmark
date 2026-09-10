# KMQGB Recovery Delta 185

**Date:** 2026-09-10  
**Scope:** PF2-01B1/B2 nonlocal Weyl-basis eikonal causality under RQIR Core v1.0 FROZEN.

## New scientific result

Two matched form-factor realizations inside the nonlocal Weyl family were frozen separately rather than merged by label.

### PF2-01B1 — Weyl `H_K`

Published eikonal/Shapiro-delay authority gives a time advance for the declared `H_2=H_0=H_K` Weyl-basis realization in the stated weak-coupling high-energy regime.

Classification:

`FAIL_RQIR_GATE__SCOPED_EIKONAL_CAUSALITY_TIME_ADVANCE`.

This is a genuine scoped scientific FAIL.

### PF2-01B2 — Weyl `H_T`

For the matched `H_2=H_0=H_T` realization, the same source finds no dangerous Shapiro time advance in the stated regime.

Classification:

`PASS_RQIR_GATE__SCOPED_EIKONAL_CAUSALITY_CONTROL`.

This is a scoped causality control, not a complete theory PASS.

Authorities:

- `post_freeze_paper_iv_wave_02/PF2_01B_NONLOCAL_WEYL_CAUSALITY/audit.md`
- `.../result_hk.json`
- `.../result_ht.json`

## Methodological significance

The opposite outcomes prove that the nonlocal causality verdict is realization/form-factor dependent. Therefore a child FAIL cannot be promoted to parent-family FAIL and a child PASS cannot be promoted to parent-family sufficiency.

`code/paper_iv_framework_coverage_validator.py` was strengthened to fail-close either type of silent child-to-parent promotion.

## NONLOCAL_QG parent status

Remains:

`PARTIAL_SUBFAMILY_ONLY`.

Closed scoped children now include:

1. Ricci/EOM-squared weakly-nonlocal tree S-matrix — exact GR comparator identity;
2. Weyl `H_K` eikonal causality — scoped scientific FAIL;
3. Weyl `H_T` eikonal causality — scoped PASS control.

## D4 evidence growth

The global Tier-1 family matrix remains nonterminal. At required-row level only GR/EFT has a complete defined residual.

However, defined scoped child rows increase to four total:

- string/dual-resonance rigidity;
- nonlocal Ricci/EOM-squared exact identity;
- nonlocal Weyl `H_K` causality FAIL;
- nonlocal Weyl `H_T` causality control.

The scoped scientific-FAIL count is now 1, but it contributes zero family-level exclusion evidence.

## Exact next gate

`PF2_01B3_RIEMANN_WEYL_AMPLITUDE_RESIDUAL`

Required payload:

`{fixed Riemann/Weyl form factor, external states/helicities, normalized amplitude vector, identical-order GR plus local higher-curvature EFT comparator basis, form-factor parameter incidence, unitarity/pole prescription, causality status, approximation/error ledger, comparator-orthogonal residual}`.

The key scientific question is whether the known non-GR Riemann/Weyl amplitude dependence survives the **full local higher-curvature EFT quotient**, rather than merely differing from pure Einstein gravity.

PF2-01B4 Gödel/CTC scope classification remains downstream/parallel.

## Stable global state

- R1 = 100%.
- R2 = 100%.
- R3 Candidate Gravity = 24% unchanged.
- Candidate Gravity inactive.
- Tier-1 = 11: 1 terminal coverage row / 10 nonterminal.
- Tier-2 unresolved = 5.
- D2A = NOT_CLOSED.
- D2B = NOT_CLOSED.
- D2 = NOT_CLOSED_COVERAGE_AND_OBJECTS.
- D4 = PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED.
- D7 = NOT_CLOSED.
- Paper IV = NOT_YET_AUTHORIZED.
- NEW_REQUIRED forbidden.
- AS/LQG/CFS Closure Wave 02 remains 0/3.

## Compute policy

Heavy compute remains IDLE. PF2-01B3 is primarily an analytic comparator-basis and amplitude-attribution problem; numerical work is not yet the bottleneck.
