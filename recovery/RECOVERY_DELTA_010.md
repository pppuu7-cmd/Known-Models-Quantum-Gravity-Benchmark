# KMQGB Recovery Delta 010 — First Queue Terminal Completion

**Date:** 2026-09-08  
**Iteration:** KMQGB-010  
**Repository:** `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`

## What changed

1. Closed M06 Brans-Dicke as `OPERATIONALLY_DEGENERATE` against the broader massless scalar-tensor parent class. The frozen static and dipole signal remains nonzero against C0 but cannot uniquely identify the nested BD submodel.
2. Instantiated and closed M07 standard fundamental Stelle quadratic gravity as `FAIL_RQIR_CONSISTENCY` at F2 because the massive spin-2 pole has the opposite residue under the frozen conventional Feynman/Hilbert-space physical-state interpretation.
3. Instantiated and closed M08 perturbative `Riemann^3` gravity EFT as `EXACT_COMPARATOR_IDENTITY` with C5. Its higher-curvature operator is a Wilson insertion below cutoff, not a new resummed ghost spectrum.
4. Froze M09 as the type-II tree-level four-graviton Virasoro-Shapiro amplitude with six dimensions compactified on flat `T^6` and four-dimensional zero-mode external gravitons.
5. Used the compactified zero-slope result to anchor the 4D GR limit.
6. Derived/froze normalized string form factor `F_VS=Π Gamma(1-alpha' x/4)/Gamma(1+alpha' x/4)` and low-energy onset `ln F_VS=[zeta(3) alpha'^3/32]stu+...` in the declared Mandelstam convention.
7. Closed M09 under current protocol as `BLOCKED_PROTOCOL_MISMATCH`: its sub-string-threshold analytic slice is C5-EFT-degenerate, while the massive string pole domain lacks a valid frozen UV comparator in the current registry.
8. First frozen queue now has terminal classifications for all 9/9 models.

## First-queue rollup

- `EXACT_COMPARATOR_IDENTITY`: 5
- `OPERATIONALLY_DEGENERATE`: 2
- `FAIL_RQIR_CONSISTENCY`: 1
- `BLOCKED_PROTOCOL_MISMATCH`: 1
- `ROBUST_NONZERO_RESIDUAL`: 0

Terminal queue coverage: **9/9 = 100%**.

This 100% is classification coverage, not a probability of correctness and not a claim that quantum gravity is solved.

## Critical scientific semantics

- M07 is the only first-queue mandatory consistency failure.
- M05 and M06 are not failed theories; they lose unique model identification after broader comparator profiling.
- M08 demonstrates why the M07 ghost result must not be transferred blindly to a low-energy higher-curvature EFT.
- M09 is not rejected: low-energy string effects are EFT-matchable, while high-energy string-specific structure requires a comparator valid at the same energy.
- No first-queue target produced an authorized robust unique QG residual after the applicable comparator/validity-domain quotient.

## External RQIR state

KMQGB did not write to RQIR. Last observed external authority:

- Candidate Gravity research Iteration 566;
- MODEL_READINESS 24%;
- rank11 run `34168897005`, job `101885271903`, coordinate `(+2.5e-6,-1.25e-6)` directly verified `in_progress` during the cycle.

No KMQGB heavy job was dispatched on the shared runner.

## Exact restore instruction

On recovery, read in this order:

1. `recovery/CURRENT_BENCHMARK_FRONT.md`
2. `recovery/state.json`
3. `matrices/benchmark_matrix.csv`
4. this delta
5. `logs/research_log.md`
6. per-model audits/results as needed

Do not reopen the historical first-queue denominator. The next research action is to freeze a **separate second-wave queue** and only then create a new coverage percentage for that wave.

Priority second-wave candidates:

1. concrete ghost-free nonlocal/form-factor gravity;
2. concrete asymptotic-safety trajectory/truncation with Lorentzian observable kernel;
3. classical-channel / measurement-feedback gravity;
4. modern postquantum classical gravity;
5. explicit UV-completion comparator for the M09 string-threshold branch;
6. additional loop/canonical/discrete QG models only if one concrete observable realization can be frozen.
