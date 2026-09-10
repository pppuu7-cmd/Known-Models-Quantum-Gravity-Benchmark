# Paper IV — Frozen-Core Decision Ledger

**KMQGB iteration:** 183  
**RQIR standard:** **Core v1.0 FROZEN**  
**Current global decision:** **`NOT_YET_AUTHORIZED`**  
**Allowed future terminal decisions:** `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED`.

## Core discipline

A scoped benchmark result is not automatically a verdict on its entire research school. `BLOCKED`, `NOT_YET_BENCHMARKED`, `PARTIAL_SUBFAMILY_ONLY` and unresolved classification all contribute **zero** exclusion evidence toward `NEW_REQUIRED`.

Cross-authority composition remains governed by `protocol/PAPER_IV_SAME_REALIZATION_COMPOSITION_GATE.md`. Major-school completeness is governed by `protocol/PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json`.

No semantic defect in RQIR Core v1.0 has been found.

## D2 now has two obligations

`D2 = D2A_framework_set_coverage AND D2B_complete_objects`.

- **D2A** asks whether the materially distinct major known schools have been admitted, explicitly reduced/merged by a derived map, or excluded from Paper-IV scope by proof.
- **D2B** asks whether every admitted school has a complete same-realization physical object suitable for comparator subtraction.

At Iter183 both are `NOT_CLOSED`.

## Tier-1 major-school census

| Family / role | Coverage state | Current strongest authority |
|---|---|---|
| GR + controlled low-energy EFT | `BENCHMARKED_COMPLETE_REALIZATION` | baseline/comparator pass |
| Perturbative renormalizable / higher-derivative QG | `NOT_YET_BENCHMARKED` | PF2 pending |
| Hořava-Lifshitz QG | `NOT_YET_BENCHMARKED` | PF2 pending |
| Asymptotic Safety | `BLOCKED_MISSING_REQUIRED_OBJECT` | mediated scattering + separate contact sector |
| Nonlocal / infinite-derivative QG | `NOT_YET_BENCHMARKED` | **next active PF2 target** |
| String / M-theory / holographic QG | `PARTIAL_SUBFAMILY_ONLY` | dual-resonance/Virasoro-Shapiro scoped child pass |
| Causal sets | `NOT_YET_BENCHMARKED` | PF2 pending |
| CDT/EDT | `NOT_YET_BENCHMARKED` | PF2 pending |
| LQG / EPRL-spinfoam | `BLOCKED_MISSING_REQUIRED_OBJECT` | scoped EPRL->Regge + area-metric downstream controls |
| GFT / tensor models | `NOT_YET_BENCHMARKED` | independence/reduction audit pending |
| Causal Fermion Systems | `BLOCKED_MISSING_REQUIRED_OBJECT` | Einstein-Dirac continuum + correction generator |

A five-entry Tier-2 watchlist remains unresolved and must be dispositioned before D7: supergravity/double-copy, noncommutative/spectral geometry, twistor/amplitude programs, canonical Wheeler-DeWitt geometrodynamics, and emergent/induced/graph-based gravity.

## Global gates after Iter183

- **D1 Frozen-judge integrity:** `PASS`.
- **D2A Framework-set coverage:** `NOT_CLOSED`.
- **D2B Complete same-realization objects:** `NOT_CLOSED`.
- **D2 combined:** `NOT_CLOSED_COVERAGE_AND_OBJECTS`.
- **D3 Common-domain comparability:** `PARTIAL`.
- **D4 Comparator-subtracted residual matrix:** `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`.
- **D5 Missing-object quarantine:** `PASS`.
- **D6 Same-realization composition discipline:** `PASS_RULE_TARGETS_OPEN`.
- **D7 Global terminal proof obligation:** `NOT_CLOSED`.

Machine authorities:

- `code/paper_iv_framework_coverage_validator.py`
- `code/paper_iv_global_gate_validator.py`
- `paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_2026-09-10.json`

## Scope correction to Iter182

The Iter182 five-row residual matrix was correct for its declared active set, but it was not a complete census of major known quantum-gravity schools. Iter183 preserves every scoped result while expanding the coverage obligation.

In particular, `STRING_DUAL_RESONANCE` remains a valid `PASS_RQIR_GATE__SCOPED_RIGIDITY_CONTROL`, but it is now a child benchmark under the broader `STRING_MTHEORY_HOLOGRAPHY` family. It cannot alone establish whole-family sufficiency or exclusion.

## Existing CW2 blockers remain open

### O-AS

`STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`

The `A_s+A_t+A_u` Lorentzian mediated object and a separate contact `A4` sector cannot be added across unmatched realization vectors.

### O-LQG

`EPRL_REGGE_TO_AREA_REGGE_PARITY_COUPLING_MATCHING_CERTIFICATE`

The open issue is controlled ancestry from microscopic EPRL dynamics through Area-Regge/area-metric couplings and `gamma_EPRL -> gamma_AM(mu)`, not absence of all downstream observables.

### O-CFS

`FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR`

The correction generator exists, but the first normalized comparator-ready non-Einstein tensor is still missing.

## Terminal proof obligations

### `EXISTING_SUFFICIENT`

Requires at least one complete family/equivalence class to close the target RQIR hierarchy across Paper-IV scope. Not authorized.

### `ADAPT_EXISTING`

Requires a complete known family whose remaining gap is demonstrably adapter/interface-only rather than missing physics. Not authorized.

### `HYBRID_REQUIRED`

Requires complete constituent rows, a derived interface law and no-double-counting certificate. Not authorized.

### `NEW_REQUIRED`

Requires resolved major-school coverage plus family-level exclusion/inadequacy evidence for every relevant existing/adapted/hybrid route. One failed representative realization is insufficient. Not authorized.

## New active PF2 gate

**`PF2_01_NONLOCAL_QG_SCATTERING_REALIZATION_CERTIFICATE`**

Required payload:

`{declared nonlocal action/form factors, pole/ghost/unitarity prescription, normalized physical scattering or propagation observable, IR GR map, causality/domain assumptions, approximation/error ledger, full local GR/EFT comparator quotient, alternative-QG comparators}`.

After nonlocal QG the planned omitted-family sequence is CDT/EDT, Hořava-Lifshitz, causal sets, perturbative higher-derivative QG, then GFT/tensor after its independence/reduction audit.

## Candidate Gravity firewall

Candidate Gravity remains inactive at R3 = 24%. It is activated only if the completed D7 decision is exactly `NEW_REQUIRED`. If activated, it must pass the unchanged frozen RQIR funnel used for known schools.

## Compute triage

Heavy computation remains IDLE. PF2-01 begins with literature, realization selection, normalized observable construction and comparator mapping; numerical work is allowed only after a prospective physical gate justifies it.

## Current verdict

**`NOT_YET_AUTHORIZED`**

Reason:

`frozen judge valid + major-school census expanded + D2A/D2B open + D4 only partial active-set authority + multiple major families not yet benchmarked + no terminal D7 proof`.

Primary Iter183 audit: `paper_iv/PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_AUDIT_2026-09-10.md`.
