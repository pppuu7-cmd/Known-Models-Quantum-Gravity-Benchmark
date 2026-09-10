# Paper IV — Frozen-Core Decision Ledger

**KMQGB iteration:** 184  
**RQIR standard:** **Core v1.0 FROZEN**  
**Current global decision:** **`NOT_YET_AUTHORIZED`**  
**Allowed future terminal decisions:** `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED`.

## Core discipline

A scoped benchmark result is not automatically a verdict on its entire research school. `BLOCKED`, `NOT_YET_BENCHMARKED`, `PARTIAL_SUBFAMILY_ONLY` and unresolved classification all contribute zero family-level exclusion evidence toward `NEW_REQUIRED`.

No semantic defect in RQIR Core v1.0 has been found.

## Global gates

`D2 = D2A_framework_set_coverage AND D2B_complete_objects`.

- D1 frozen-judge integrity — `PASS`.
- D2A framework-set coverage — `NOT_CLOSED`.
- D2B complete same-realization objects — `NOT_CLOSED`.
- D2 combined — `NOT_CLOSED_COVERAGE_AND_OBJECTS`.
- D3 common-domain comparability — `PARTIAL`.
- D4 comparator-subtracted residual matrix — `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`.
- D5 missing-object quarantine — `PASS`.
- D6 same-realization composition discipline — `PASS_RULE_TARGETS_OPEN`.
- D7 global terminal proof obligation — `NOT_CLOSED`.

## Tier-1 census after PF2-01A

| Family / role | Coverage state | Current strongest authority |
|---|---|---|
| GR + controlled low-energy EFT | `BENCHMARKED_COMPLETE_REALIZATION` | baseline/comparator pass |
| Perturbative/higher-derivative QG | `NOT_YET_BENCHMARKED` | PF2 pending |
| Hořava-Lifshitz QG | `NOT_YET_BENCHMARKED` | PF2 pending |
| Asymptotic Safety | `BLOCKED_MISSING_REQUIRED_OBJECT` | mediated scattering + separate contact sector |
| Nonlocal / infinite-derivative QG | **`PARTIAL_SUBFAMILY_ONLY`** | Ricci/EOM-squared tree S-matrix exact GR identity |
| String / M-theory / holographic QG | `PARTIAL_SUBFAMILY_ONLY` | dual-resonance/Virasoro-Shapiro scoped child pass |
| Causal sets | `NOT_YET_BENCHMARKED` | PF2 pending |
| CDT/EDT | `NOT_YET_BENCHMARKED` | PF2 pending |
| LQG / EPRL-spinfoam | `BLOCKED_MISSING_REQUIRED_OBJECT` | scoped EPRL->Regge + area-metric downstream controls |
| GFT / tensor models | `NOT_YET_BENCHMARKED` | independence/reduction audit pending |
| Causal Fermion Systems | `BLOCKED_MISSING_REQUIRED_OBJECT` | Einstein-Dirac continuum + correction generator |

Tier-2 unresolved watchlist remains five programs.

## PF2-01A — first omitted-family benchmark result

For the declared weakly-nonlocal Ricci/EOM-squared gravity subclass, the published field-redefinition theorem and explicit amplitude calculations give

`A_n^NLQG(tree) = A_n^GR(tree)`

for on-shell tree-level scattering in the theorem domain. Therefore

`R_NLQG(tree) = 0`

is a genuine exact comparator identity, not a missing-data zero-fill.

Scoped classification:

**`PASS_RQIR_GATE__EXACT_COMPARATOR_IDENTITY__TREE_S_MATRIX`**.

Authority:

- `post_freeze_paper_iv_wave_02/PF2_01_NONLOCAL_QG/audit.md`
- `post_freeze_paper_iv_wave_02/PF2_01_NONLOCAL_QG/result.json`

This result does not mean nonlocal QG is wrong; it means tree scattering cannot distinguish this particular class from its Einstein comparator.

## Why NONLOCAL_QG remains partial

An independent Riemann/Weyl-sector form factor is outside the Ricci field-redefinition identity and can alter scattering amplitudes. Published eikonal causality work also distinguishes form-factor realizations: a Weyl-basis `H_K` choice admits a Shapiro time advance, while an `H_T` choice supplies a matched causality-preserving control in the stated regime.

In addition, 2026 exact-vacuum work exhibits a form-factor subclass admitting Gödel-type vacuum solutions with closed timelike curves. Thus perturbative unitarity/renormalizability cannot be silently promoted to universal causality.

Front authority:

`paper_iv/O_NONLOCAL_RIEMANN_WEYL_CAUSALITY_FRONT_2026-09-10.md`.

## D4 evidence status

At the required Tier-1 family level only GR/EFT has a defined complete-row residual.

Two additional scoped child residuals are now defined:

1. string/dual-resonance — scoped rigidity pass;
2. nonlocal Ricci/EOM-squared — exact zero after GR subtraction.

Neither child result can by itself terminally classify its parent family.

## Existing CW2 blockers remain open

- O-AS — `STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`.
- O-LQG — `EPRL_REGGE_TO_AREA_REGGE_PARITY_COUPLING_MATCHING_CERTIFICATE`.
- O-CFS — `FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR`.

## Next active gate

**`PF2_01B_NONLOCAL_RIEMANN_WEYL_SCATTERING_CAUSALITY_CERTIFICATE`**

Prospectively split into:

- `PF2_01B1_WEYL_HK_EIKONAL_CAUSALITY`;
- `PF2_01B2_WEYL_HT_EIKONAL_CAUSALITY`;
- `PF2_01B3_RIEMANN_WEYL_AMPLITUDE_RESIDUAL`;
- `PF2_01B4_GODEL_VACUUM_CAUSALITY`.

A scoped causality FAIL for one form factor cannot exclude the family while an independently admissible branch remains causal or untested.

## Candidate Gravity firewall

Candidate Gravity remains inactive at R3 = 24%. It activates only if the completed D7 decision is exactly `NEW_REQUIRED`; if activated it must pass the same unchanged frozen RQIR funnel.

## Compute triage

Heavy compute remains IDLE. The current blocker is exact realization/domain/comparator matching, not numerical sensitivity.

## Current verdict

**`NOT_YET_AUTHORIZED`**

Reason:

`PF2-01A supplies a new exact scoped comparator identity + NONLOCAL_QG parent remains partial + major-school coverage and family-level residual matrix remain incomplete + D7 has no terminal proof`.
