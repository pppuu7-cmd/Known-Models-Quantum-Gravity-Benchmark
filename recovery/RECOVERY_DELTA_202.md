# KMQGB recovery delta — Iteration 202

**Date:** 2026-09-10  
**Base canonical main:** `ef0ca4b3bc50addc0577a4528c8f2dafe3e4f21a` (Iter201)  
**RQIR Core:** v1.0 FROZEN.

## Auto-research reconciliation

Before starting Iter202, the hourly `KMQGB Research Loop` was checked. Its latest run had already repaired the malformed Iter201 recovery JSON and merged validated Iter201 to `main`; therefore no manual duplicate repair was performed. No Iter202 branch/PR existed at the start of this iteration.

## New GFT result

The old GFT blocker mixed microscopic relation-to-spin-foam questions with continuum/observable questions. Iter202 separates them.

### Microscopic relation

Oriti–Ryan–Thürigen provide an explicit GFT formulation of the KKL spin-foam model and formulate GFT as a second-quantized reformulation/completion of the LQG/spin-foam state/amplitude framework.

Frozen scoped status:

`PASS_STRUCTURAL_GATE__SELECTED_KKL_COMPATIBLE_GFT_HAS_EXPLICIT_SPINFOAM_REDUCTION_MAP_AT_THE_MICROSCOPIC_AMPLITUDE_LEVEL`.

This is not family-wide equivalence. GFT/TGFT includes graph-changing/Feynman-complex sums, tensorial interactions, RG/phase structure and condensate collective dynamics that are not exhausted by a fixed spin-foam amplitude.

### Relational continuum/effective observables

Lorentzian Barrett-Crane GFT constructions produce relational scalar cosmological perturbation dynamics with a sub-Planckian GR regime and trans-Planckian corrections. A 2025 Landau-Ginzburg analysis supports a nontrivial condensate phase in the causally complete Lorentzian Barrett-Crane TGFT at mean-field level. The 2026 Dekhil–Greco–Liberati–Oriti construction derives an effective scalar field on emergent FLRW geometry from GFT hydrodynamics and obtains dispersive/dissipative modified-dispersion corrections in the early-universe regime.

Frozen scoped status:

`PASS_STRUCTURAL_GATE__GFT_RELATIONAL_CONDENSATE_DYNAMICS_SUPPLIES_EXPLICIT_GR_LIMIT_AND_QUANTUM_CORRECTION_CHANNELS`.

No new comparator-ready gravity residual row is added because a nonperturbatively controlled continuum trajectory, one normalized physical observation operator, full GR/EFT/alternative-QG comparator set and propagated approximation/error ledger are not jointly frozen in one realization.

## Refined blocker

`GFT_MATERIAL_BRANCH_REDUCTION_OR_INDEPENDENCE_MAP_PLUS_CONTROLLED_CONTINUUM_TRAJECTORY_AND_NORMALIZED_RELATIONAL_GRAVITY_OBSERVABLE_COMPARATOR_ERROR_CERTIFICATE`

Required next object:

1. material GFT/TGFT branch census;
2. explicit reduction-to-named-spin-foam or independent-collective-dynamics classification per branch;
3. fixed Lorentzian gravity realization with controlled continuum/thermodynamic trajectory;
4. relational gravitational observable transported through that trajectory;
5. common physical normalization/observation operator;
6. GR/EFT and alternative-QG comparators;
7. continuum/mean-field/condensate/interaction/truncation/numerical error ledger;
8. family-level disposition without promoting one cosmology child to the whole family.

## Global status

No promotion:

- Tier-1: `1/14` terminal; `13/14` nonterminal;
- scoped comparator-ready gravity residual/control rows: **10**;
- D2: NOT_CLOSED;
- D4: NOT_CLOSED;
- D7: NOT_CLOSED;
- Paper IV: `NOT_YET_AUTHORIZED`;
- Candidate Gravity R3: **24%**, inactive;
- Closure Wave 02: **0/3 terminal**;
- heavy compute: IDLE.

## Authorities added

- `paper_iv/O_GFT_SPINFOAM_REDUCTION_AND_RELATIONAL_OBSERVABLE_SCOPE_AUDIT_2026-09-10.md`
- `paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_DELTA_202.json`
- `paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_202.json`

## Next operation

1. synchronize `recovery/state.json` and `recovery/CURRENT_BENCHMARK_FRONT.md`;
2. exact-head CI validate Iter202;
3. recheck hourly auto-research before integration;
4. if no competing newer front exists, merge Iter202 and then inspect whether the GFT material-branch census itself can be made terminal from existing literature, or rotate to the next family if that census remains too broad for a single valid closure.