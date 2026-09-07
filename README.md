# Known Models / Quantum Gravity Benchmark (KMQGB)

Purpose: audit concrete gravity and quantum-gravity realizations through the same frozen RQIR funnel used for Candidate Gravity, while keeping benchmark work physically separated from the main RQIR development repository.

Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`  
Default branch: `main`  
Recovery entrypoint: `recovery/RESTORE_FROM_NEW_CHAT.md`.

## First queue — terminally classified

| # | Concrete target | Control role | Terminal state |
|---|---|---|---|
| 1 | 4D Einstein–Hilbert GR, weak-field Minkowski | C0 null control | **EXACT_COMPARATOR_IDENTITY** |
| 2 | `ANSATZ-PQG-EFT-001` perturbative low-energy QG EFT | C5 control | **EXACT_COMPARATOR_IDENTITY** |
| 3 | `SCG-MINK-SCALAR-LR-001` semiclassical Einstein gravity | C1 mean control | **EXACT_COMPARATOR_IDENTITY** |
| 4 | `SG-MINK-CONFORMAL-EL-001` stochastic Einstein–Langevin gravity | C2 fluctuation control | **EXACT_COMPARATOR_IDENTITY** |
| 5 | `FR-R2-MINK-001` metric `R+R^2/(6M^2)` | extra scalar | **OPERATIONALLY_DEGENERATE** |
| 6 | `BD-MASSLESS-OMEGA200000-MINK-001` Brans–Dicke | long-range scalar | **OPERATIONALLY_DEGENERATE** |
| 7 | `STELLE-MINK-STANDARD-FEYNMAN-001` standard fundamental Stelle gravity | pathological spin-2 pole | **FAIL_RQIR_CONSISTENCY** |
| 8 | `GR-EFT-RIEMANN3-MINK-001` perturbative higher-curvature EFT | EFT positive/boundary control | **EXACT_COMPARATOR_IDENTITY** |
| 9 | `TYPEII-T6-GRAV4-TREE-001` type-II tree four-graviton string amplitude | UV/string scattering control | **BLOCKED_PROTOCOL_MISMATCH** |

**First-queue terminal coverage: 9/9 = 100%.**

This 100% means only that every member of the frozen first queue has a terminal classification under the current benchmark protocol. It does **not** mean quantum gravity is solved, that every known school has been exhausted, or that the Candidate Gravity model is complete.

## First-queue rollup

- `EXACT_COMPARATOR_IDENTITY`: 5
- `OPERATIONALLY_DEGENERATE`: 2
- `FAIL_RQIR_CONSISTENCY`: 1
- `BLOCKED_PROTOCOL_MISMATCH`: 1
- `ROBUST_NONZERO_RESIDUAL`: 0

## Main scientific lessons

1. **The funnel does not automatically reject known theories.** GR, semiclassical gravity, stochastic gravity and standard low-energy QG EFT are recognized as their own comparator/control classes.
2. **Different from GR is not the same as uniquely identified.** `R+R^2` has a real nonzero GR residual in the frozen weak-field slip observable, but a broader one-scalar Yukawa family reproduces the whole curve exactly.
3. **Even linked multi-channel signatures can identify only a parent class.** Brans–Dicke links the weak-field PPN shift and scalar dipole radiation, but the exact BD point is nested in general massless scalar-tensor gravity.
4. **M07 is the first genuine consistency failure.** In standard fundamental Stelle quadratic gravity the UV-improving massive spin-2 pole has the opposite residue and fails the frozen positivity/unitarity gate under the standard physical-state interpretation.
5. **That failure must not be overgeneralized to EFT.** A higher-curvature Wilson operator treated perturbatively below a cutoff does not inherit the M07 verdict merely because a resummed truncated equation has extra formal roots. M08 is a C5 EFT slice, not a new fundamental ghost spectrum.
6. **String theory exposes a comparator-domain boundary.** In the sub-string-threshold domain its analytic corrections are ordinary gravitational EFT Wilson data and hence not uniquely string-identifying versus C5. At string thresholds the full Virasoro–Shapiro pole tower becomes relevant, but C5 is no longer a valid high-energy comparator. The current protocol lacks a frozen UV-completion comparator class, so M09 is blocked rather than falsely promoted or rejected.

## Status vocabulary

`PASS_RQIR_GATE`, `FAIL_RQIR_CONSISTENCY`, `EXACT_COMPARATOR_IDENTITY`, `OPERATIONALLY_DEGENERATE`, `ROBUST_NONZERO_RESIDUAL`, `BLOCKED_MISSING_REQUIRED_OBJECT`, `BLOCKED_PROTOCOL_MISMATCH`, `OPERATIONAL_FAILURE`.

`BLOCKED` is not scientific invalidation. `EXACT_COMPARATOR_IDENTITY` is a control/non-novelty result. `OPERATIONALLY_DEGENERATE` is an observable/model-identification limitation. `FAIL_RQIR_CONSISTENCY` is reserved for a mandatory consistency failure.

## Second wave

The first 9-model denominator is frozen historically and will not be retroactively changed. A separate second-wave queue will be frozen before its own percentage is reported. Priority candidates currently retained are:

- a concrete ghost-free nonlocal/form-factor gravity model;
- a concrete asymptotic-safety trajectory/truncation with a Lorentzian observable kernel;
- classical-channel / measurement-feedback gravity;
- a modern postquantum classical-gravity realization;
- a genuine UV comparator for the M09 string-threshold branch;
- additional loop/canonical/discrete QG programs only after a concrete observable realization can be frozen.

## Repository firewall

KMQGB may read frozen RQIR protocol and current Candidate Gravity authority as external inputs, but all benchmark writes belong here only. It must not modify Candidate Gravity readiness, recovery state, iteration numbering, workflows, active runner state, or scientific authority in `Relativity-Quantum-Interface-Reconstruction`.
