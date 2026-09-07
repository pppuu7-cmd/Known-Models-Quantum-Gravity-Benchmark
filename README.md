# Known Models / Quantum Gravity Benchmark (KMQGB)

Purpose: audit concrete gravity and quantum-gravity realizations through the same frozen RQIR funnel used for Candidate Gravity, while keeping benchmark work physically separated from the main RQIR development repository.

Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
Default branch: `main`
Source migration: `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction`, branch `rqir7-known-models-benchmark`, source HEAD `782df9af3af1ca55ca4f9bf143e2723a7a8f18bc`.
Recovery entrypoint: `recovery/RESTORE_FROM_NEW_CHAT.md`.

## First queue

| # | Concrete target | Control role | State |
|---|---|---|---|
| 1 | 4D Einstein–Hilbert GR, Lambda=0, weak-field Minkowski | null control C0 | **CLOSED — EXACT_COMPARATOR_IDENTITY** |
| 2 | `ANSATZ-PQG-EFT-001` v0.1, perturbative low-energy quantum GR EFT | C5 EFT control | **CLOSED — EXACT_COMPARATOR_IDENTITY** |
| 3 | `SCG-MINK-SCALAR-LR-001` semiclassical Einstein gravity | C1 mean-backreaction control | **CLOSED — EXACT_COMPARATOR_IDENTITY** |
| 4 | `SG-MINK-CONFORMAL-EL-001` Einstein–Langevin stochastic gravity | C2 fluctuation control | **CLOSED — EXACT_COMPARATOR_IDENTITY** |
| 5 | `FR-R2-MINK-001`, metric `R+R^2/(6M^2)` | extra-scalar modified gravity | **CLOSED — OPERATIONALLY_DEGENERATE** |
| 6 | `BD-MASSLESS-OMEGA200000-MINK-001`, massless Brans–Dicke | long-range scalar control | **CLOSED — OPERATIONALLY_DEGENERATE** |
| 7 | `STELLE-MINK-STANDARD-FEYNMAN-001`, standard fundamental Stelle quadratic gravity | pathological-pole control | **CLOSED — FAIL_RQIR_CONSISTENCY** |
| 8 | `GR-EFT-RIEMANN3-MINK-001`, perturbative higher-curvature EFT | EFT boundary/positive control | **CLOSED — EXACT_COMPARATOR_IDENTITY** |
| 9 | `TYPEII-T6-GRAV4-TREE-001` provisional, type-II string four-graviton scattering with intended 4D projection | string/QG scattering control | **active audit** |

Terminal queue coverage: **8/9 = 88.89%**. This is exact queue coverage, not a probability that quantum gravity is 88.89% solved.

## Status vocabulary

`PASS_RQIR_GATE`, `FAIL_RQIR_CONSISTENCY`, `EXACT_COMPARATOR_IDENTITY`, `OPERATIONALLY_DEGENERATE`, `ROBUST_NONZERO_RESIDUAL`, `BLOCKED_MISSING_REQUIRED_OBJECT`, `BLOCKED_PROTOCOL_MISMATCH`, `OPERATIONAL_FAILURE`.

`BLOCKED` is never scientific invalidation. `EXACT_COMPARATOR_IDENTITY` is a control/non-novelty result. `OPERATIONALLY_DEGENERATE` means a frozen observable/model-identification residual is exactly absorbed by an allowed broader comparator even though the theories need not be globally equivalent. `FAIL_RQIR_CONSISTENCY` is reserved for a mandatory physical consistency gate such as the standard massive spin-2 ghost in M07.

## Current lessons

1. GR, semiclassical gravity, stochastic gravity and perturbative QG EFT are correctly recognized as their own comparator/control classes rather than falsely rejected.
2. A nonzero deviation from GR is not enough for theory identification: M05 `R+R^2` is exactly absorbed in its frozen `gamma(r)` observable by a broader one-scalar Yukawa family.
3. A linked multi-channel signal still may not identify a nested submodel: M06 Brans–Dicke has a nonzero static PPN shift and linked scalar dipole channel, but the general massless scalar-tensor parent family contains the exact BD point.
4. M07 is the first true consistency failure: standard fundamental Stelle quadratic gravity retains the UV-improving opposite-residue massive spin-2 pole, which fails the frozen positivity/unitarity gate under the standard physical-state interpretation.
5. M08 prevents overgeneralization of M07: a higher-curvature term used as a perturbative EFT Wilson insertion below a cutoff is not the same object as a resummed fundamental higher-derivative theory. The concrete `Riemann^3` EFT slice belongs to C5.
6. M09 must compare string theory only in a common validity domain: finite-order low-energy string corrections may be absorbed by C5 Wilson coefficients, whereas genuinely string-specific massive pole structure appears when the string threshold is resolved, where a finite low-energy C5 truncation is no longer the proper comparator.

## Mandatory output table

Every concrete realization must ultimately populate: exact realization/paper; action/equations; regime; DOF; GR limit; poles/cuts; ghosts/tachyons; gauge/Ward; causal/retarded structure; source rule; nonlinear vertices; Q1–Q7 fingerprint; frozen-observable mapping; comparator span; quotient residual; degeneracies; missing objects; first blocking/failing gate; final status.

## Repository firewall

KMQGB may read frozen RQIR protocol and current Candidate Gravity authority as external inputs, but all benchmark writes belong here only. It must not modify Candidate Gravity readiness, recovery state, iteration numbering, workflows, active runner state, or scientific authority in `Relativity-Quantum-Interface-Reconstruction`.
