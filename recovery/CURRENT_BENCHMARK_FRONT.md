# KMQGB Current Benchmark Front

**Updated:** 2026-09-09  
**KMQGB iteration:** **152**  
**Phase:** **RQIR Core v1.0 FROZEN / PF1 regression closed / Paper-IV decision closure ACTIVE**.

## Stable metrics

- **R1 Repository readiness: 92%.**
- **R2 KMQGB methodology/material readiness: 90%.**
- **R3 external Candidate Gravity readiness: 24%.**
- **Legacy parent-search R4: 45% — PAUSED / CONDITIONAL ON PAPER IV.**
- **Post-freeze Paper-IV Wave 01: 5/5 = 100% terminal.**

Last readiness change: Iter145, `R2 89 -> 90`, when `residual/identifiability/rigidity` closed `19/20 -> 20/20` after methodology-ci run `34397157673` passed the independent nonlinear detector-facing regression.

## Frozen RQIR authority

RQIR Core **v1.0 is FROZEN** and Papers I–III are **100% scientific/material CLOSED**. KMQGB owns model-specific adapters and Paper-IV benchmark writes. Future Candidate Gravity remains separate and cannot tune the frozen judge.

Governance:

- external `RQIR_VERSION.json`;
- external `docs/RQIR_CORE_CHANGE_CONTROL.md`;
- `protocol/RQIR_CORE_V1_BENCHMARK_FIREWALL.md`.

## Completed post-freeze regression

Authority: `post_freeze_paper_iv_wave_01/README.md`.

- **PF1-01 CFS:** `BLOCKED_MISSING_REQUIRED_OBJECT`; controlled continuum theorem gives scoped Einstein–Dirac comparator identity.
- **PF1-02 GR/EFT:** `PASS_RQIR_GATE__BASELINE_CONTROL`; existing sufficient in the declared low-energy EFT domain only.
- **PF1-03 string/dual resonance:** `PASS_RQIR_GATE__SCOPED_RIGIDITY_CONTROL`; low-dimensional fingerprints are non-unique, stronger overconstrained Virasoro–Shapiro package is rigid in its stated scope.
- **PF1-04 LQG/spinfoam:** `BLOCKED_MISSING_REQUIRED_OBJECT`; 2026 UV-fixed-point and causal-vertex results retire stale triangulation/causal-phase blockers, leaving a continuum-normalized Lorentzian observable package open.
- **PF1-05 asymptotic safety:** `BLOCKED_MISSING_REQUIRED_OBJECT`; direct Lorentzian spectral/form-factor progress is accepted, leaving a scheme/truncation/gauge-controlled full physical crossover package open.

The frozen judge required **no semantic change** across all five regressions.

## Paper-IV global decision

Authority:

- `paper_iv/PAPER_IV_FROZEN_CORE_DECISION_LEDGER.md`;
- `paper_iv/PAPER_IV_FROZEN_CORE_DECISION_LEDGER.json`.

Current global result:

**`NOT_YET_AUTHORIZED`**.

None of `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` has met its proof obligation.

In particular, `NEW_REQUIRED` is currently forbidden because CFS, LQG and asymptotic safety remain missing-object blocked rather than excluded on complete same-domain observables.

## Exact high-value open objects

### O-CFS

Normalized beyond-continuum CFS relational/detector/asymptotic observable with fixed state/regularization and an identical-domain Einstein–Dirac/QFT comparator.

### O-LQG

Continuum-normalized Lorentzian LQG/spinfoam physical observable with regulator/triangulation authority and same-domain GR/EFT/QG comparators.

### O-AS

Lorentzian asymptotic-safety physical crossover observable with frozen renormalization/trajectory prescription, controlled truncation/gauge dependence and same-domain comparator completion; contact/crossing-complete `4g`/higher authority is preferred for scattering claims.

## Governance enforcement

`code/post_freeze_paper_iv_governance_validator.py` makes the anti-retrofitting rule executable. In particular, a `BLOCKED` result cannot be marked as `NEW_REQUIRED` evidence, and a core change cannot be requested without an explicit core defect.

## Heavy compute

**IDLE.**

Compute becomes justified only after one of O-CFS/O-LQG/O-AS is frozen sufficiently that a numerical result can change its model-level terminal classification.

## Next research move

Audit O-CFS, O-LQG and O-AS against current literature/repository authority and select the one closest to a complete same-domain observable. Do not expand to another broad taxonomy wave until one of these three blockers is materially advanced.