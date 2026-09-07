# Known Models / Quantum Gravity Benchmark (KMQGB)

Purpose: audit concrete gravity and quantum-gravity realizations through the same frozen RQIR funnel used for Candidate Gravity, while keeping benchmark work physically separated from the main RQIR development repository.

Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
Default branch: `main`
Source migration: `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction`, branch `rqir7-known-models-benchmark`, source HEAD `782df9af3af1ca55ca4f9bf143e2723a7a8f18bc`.
Original branch base SHA: `02ad31e89f1df0d5515779e6b7526e8eb5505667`.
Recovery entrypoint: `recovery/RESTORE_FROM_NEW_CHAT.md`.

## First queue

| # | Concrete target | Control role | State |
|---|---|---|---|
| 1 | 4D Einstein–Hilbert GR, Lambda=0, weak-field Minkowski sector | null control | active audit |
| 2 | GR + low-energy quantum-gravity EFT, concrete Donoghue/Burgess realization | EFT/comparator control | queued |
| 3 | Semiclassical gravity, concrete realization | source/backreaction control | queued |
| 4 | Stochastic gravity, Einstein–Langevin/noise-kernel realization | fluctuation control | queued |
| 5 | concrete f(R) gravity | extra-DOF control | queued |
| 6 | concrete Brans–Dicke/scalar–tensor | extra-scalar control | queued |
| 7 | Stelle quadratic gravity | pathological-pole control | queued |
| 8 | concrete higher-curvature EFT/action | EFT positive control | queued |
| 9 | concrete string low-energy/scattering realization | QG/EFT control | queued |

## Status vocabulary

`PASS_RQIR_GATE`, `FAIL_RQIR_CONSISTENCY`, `EXACT_COMPARATOR_IDENTITY`, `OPERATIONALLY_DEGENERATE`, `ROBUST_NONZERO_RESIDUAL`, `BLOCKED_MISSING_REQUIRED_OBJECT`, `BLOCKED_PROTOCOL_MISMATCH`, `OPERATIONAL_FAILURE`.

`BLOCKED` is never scientific invalidation.

## Mandatory output table

Every concrete realization must ultimately populate: exact realization/paper; action/equations; regime; DOF; GR limit; poles/cuts; ghosts/tachyons; gauge/Ward; causal/retarded structure; source rule; nonlinear vertices; Q1–Q7 fingerprint; frozen-observable mapping; comparator span; quotient residual; degeneracies; missing objects; first blocking/failing gate; final status.

## Repository firewall

This repository may read the frozen RQIR protocol and current Candidate Gravity authority as external inputs, but benchmark writes belong here only. It must not modify Candidate Gravity readiness, recovery state, iteration numbering, or scientific authority files in `Relativity-Quantum-Interface-Reconstruction`.
