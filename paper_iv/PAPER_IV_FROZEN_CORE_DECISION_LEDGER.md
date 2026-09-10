# Paper IV — Frozen-Core Decision Ledger

**KMQGB iteration:** 182  
**RQIR standard:** **Core v1.0 FROZEN**  
**Current global decision:** **`NOT_YET_AUTHORIZED`**  
**Allowed future terminal decisions:** `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED`.

## Core discipline

A framework may be terminal for a scoped benchmark while Paper IV remains non-terminal. `BLOCKED_MISSING_REQUIRED_OBJECT` contributes zero exclusion evidence to `NEW_REQUIRED` until the missing physical object is supplied and tested in the common domain.

Cross-authority composition remains governed by `protocol/PAPER_IV_SAME_REALIZATION_COMPOSITION_GATE.md`: papers from one school are not one RQIR observable unless their realization vectors match or an explicit map is derived.

## Current framework evidence

| Framework | Current state | Strongest accepted progress | Exact open object |
|---|---|---|---|
| GR + low-energy EFT | `PASS_RQIR_GATE__BASELINE_CONTROL` | controlled low-energy sufficiency and universal QG-EFT predictions | UV/strong-gravity completion outside EFT authority |
| String / dual resonance | `PASS_RQIR_GATE__SCOPED_RIGIDITY_CONTROL` | rich Regge/bootstrap package gives scoped Virasoro–Shapiro rigidity | common-domain attribution of the full useful UV invariant vector |
| Asymptotic safety | `BLOCKED_MISSING_REQUIRED_OBJECT` | mediated Lorentzian scattering exists; explicit contact sector exists in a separate simplified realization | **same-realization `A_s+A_t+A_u+A4` certificate with crossing, trajectory, normalisation, full error and comparator map** |
| LQG / spinfoam | `BLOCKED_MISSING_REQUIRED_OBJECT` | Lorentzian EPRL->Regge asymptotic dynamics plus area-metric continuum/parity/RG structures | **controlled EPRL/Regge -> Area-Regge/area-metric coupling ancestry and `gamma_EPRL -> gamma_AM(mu)` map** |
| Causal Fermion Systems | `BLOCKED_MISSING_REQUIRED_OBJECT` | Einstein–Dirac continuum identity and systematic microscopic correction generator | **first explicit normalized non-Einstein gravity correction tensor/coefficient vector + full C5/GR/QFT comparator** |

## Global gates after Iter182

- **D1 Frozen-judge integrity:** `PASS`.
- **D2 Major-framework complete-object coverage:** `NOT_CLOSED`.
- **D3 Common-domain comparability:** `PARTIAL`.
- **D4 Comparator-subtracted residual matrix:** `PARTIAL_MATRIX_FROZEN__NOT_CLOSED`.
- **D5 Missing-object quarantine:** `PASS`.
- **D6 Same-realization composition discipline:** `PASS_RULE_TARGETS_OPEN`.
- **D7 Global terminal proof obligation:** `NOT_CLOSED`.

Iter182 adds a frozen machine-readable residual matrix:

`paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_2026-09-10.json`

and fail-closed global logic validator:

`code/paper_iv_global_gate_validator.py`.

The validator makes the D2 -> D4 -> D7 dependency executable. Undefined/BLOCKED residual rows cannot be zero-filled and cannot count as exclusion evidence.

## Terminal proof obligations

### `EXISTING_SUFFICIENT` — NOT AUTHORIZED

Requires one complete framework/equivalence class to close the target RQIR hierarchy across the declared Paper-IV domains. GR/EFT closes only its controlled low-energy domain and string theory currently gives scoped hard-amplitude rigidity, not global coverage.

### `ADAPT_EXISTING` — NOT AUTHORIZED

Requires an existing framework whose complete residual object exists and whose remaining mismatch is demonstrated to be adapter/interface-only. AS, LQG and CFS remain physically promising but still lack one required same-realization object each.

### `HYBRID_REQUIRED` — NOT AUTHORIZED

Requires complete constituent rows plus an explicit interface law and no-double-counting certificate. No such globally complete pair/set exists yet.

### `NEW_REQUIRED` — NOT AUTHORIZED

Requires broad inadequacy/exclusion evidence on **complete** known-framework realizations. Three mandatory rows are still `BLOCKED_MISSING_REQUIRED_OBJECT`, so `NEW_REQUIRED` remains logically and scientifically forbidden.

## Closure Wave 02 — 0/3 terminal

### CW2-01 / O-AS

Published authority now establishes both a Lorentzian mediated scattering object and, separately, an explicit momentum-dependent contact sector. This is meaningful progress but **not** a same-realization sum. The contact calculation itself states that a more complete momentum-dependent propagator/all-vertex treatment is required before a final amplitude-level verdict.

Target remains:

`STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`.

### CW2-02 / O-LQG

Iter181 closed a scoped Lorentzian EPRL -> Regge asymptotic step. Iter182 verifies that Area-Regge/area-metric continuum, parity-sensitive couplings and an Immirzi beta function exist. However the area-metric RG construction explicitly treats non-metric masses as independent because they are not currently computable from spin foams and assumes an intermediate EFT regime. Therefore the microscopic EPRL Immirzi parameter cannot be equated to the running area-metric parameter by notation alone.

Target remains:

`EPRL_REGGE_TO_AREA_REGGE_PARITY_COUPLING_MATCHING_CERTIFICATE`.

### CW2-03 / O-CFS

The 2026 geometric derivation supplies Einstein gravity plus a systematic regularization-length correction architecture. The currents construction supplies a tensor hierarchy, but states that the rank-two equations are **expected** to encode Einstein equations. No first explicit normalized non-Einstein gravity correction tensor/coefficient vector is presently frozen.

Target remains:

`FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR`.

## D4 residual semantics

The frozen matrix currently contains:

- GR/EFT: defined baseline/comparator row;
- string/dual resonance: defined scoped-rigidity row;
- AS: undefined residual pending complete same-realization amplitude;
- LQG: undefined residual pending micro-to-area-metric parameter ancestry;
- CFS: undefined residual pending normalized correction tensor.

Thus D4 has materially progressed from an unspecified missing matrix to a **frozen partial matrix**, but it cannot pass until all required rows are defined in a common comparator domain.

## Compute triage

Heavy computation remains unauthorized for these blockers. The current missing objects are analytic/ancestry/normalization/composition objects, not sensitivity scans.

## Current verdict

**`NOT_YET_AUTHORIZED`**

Reason:

`frozen judge valid + D4 matrix now explicit + three required residual rows remain undefined because complete same-realization physical objects are missing + no terminal D7 proof`.

Primary Iter182 audit: `paper_iv/PAPER_IV_D2_D4_D7_CLOSURE_AUDIT_2026-09-10.md`.
