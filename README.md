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
| 1 | 4D Einstein–Hilbert GR, Lambda=0, weak-field Minkowski sector | null control C0 | **CLOSED — EXACT_COMPARATOR_IDENTITY** |
| 2 | `ANSATZ-PQG-EFT-001` v0.1, perturbative low-energy quantum GR EFT | EFT/comparator control C5 | **CLOSED — EXACT_COMPARATOR_IDENTITY** |
| 3 | `SCG-MINK-SCALAR-LR-001`, renormalized semiclassical Einstein gravity with conformal scalar / Minkowski linear response | source/backreaction control C1 | **CLOSED — EXACT_COMPARATOR_IDENTITY** |
| 4 | `SG-MINK-CONFORMAL-EL-001`, Einstein–Langevin/noise-kernel stochastic gravity | fluctuation control C2 | **CLOSED — EXACT_COMPARATOR_IDENTITY** |
| 5 | `FR-R2-MINK-001`, metric `R+R^2/(6M^2)` gravity | extra-DOF control | **active audit** |
| 6 | concrete Brans-Dicke/scalar–tensor | extra-scalar control | queued |
| 7 | Stelle quadratic gravity | pathological-pole control | queued |
| 8 | concrete higher-curvature EFT/action | EFT positive control | queued |
| 9 | concrete string low-energy/scattering realization | QG/EFT control | queued |

Terminal queue coverage: **4/9 = 44.44%**. This is exact queue coverage, not a probability that quantum gravity is 44.44% solved.

## Status vocabulary

`PASS_RQIR_GATE`, `FAIL_RQIR_CONSISTENCY`, `EXACT_COMPARATOR_IDENTITY`, `OPERATIONALLY_DEGENERATE`, `ROBUST_NONZERO_RESIDUAL`, `BLOCKED_MISSING_REQUIRED_OBJECT`, `BLOCKED_PROTOCOL_MISMATCH`, `OPERATIONAL_FAILURE`.

`BLOCKED` is never scientific invalidation. Exact comparator identity is a retained control/negative result, not a consistency failure.

## Current lesson from controls M01–M04

The first four controls validate the benchmark semantics rather than falsify their source theories:

- C0 correctly recognizes ordinary GR as the null classical baseline;
- C5 correctly recognizes perturbative quantum GR EFT as the standard low-energy quantum reference;
- C1 correctly recognizes mean semiclassical backreaction while retaining its mean-only hierarchy limitation;
- C2 correctly recognizes stochastic gravity as a stronger classical-stochastic fluctuation/noise comparator.

Therefore noise or symmetrized metric fluctuations alone are not sufficient evidence for a quantum gravitational mediator. A stronger discriminator must survive C2 and the rest of the comparator/nuisance quotient.

## Mandatory output table

Every concrete realization must ultimately populate: exact realization/paper; action/equations; regime; DOF; GR limit; poles/cuts; ghosts/tachyons; gauge/Ward; causal/retarded structure; source rule; nonlinear vertices; Q1–Q7 fingerprint; frozen-observable mapping; comparator span; quotient residual; degeneracies; missing objects; first blocking/failing gate; final status.

## Repository firewall

This repository may read the frozen RQIR protocol and current Candidate Gravity authority as external inputs, but benchmark writes belong here only. It must not modify Candidate Gravity readiness, recovery state, iteration numbering, workflows, active runner state, or scientific authority files in `Relativity-Quantum-Interface-Reconstruction`.

Prior RQIR comparator/model audits may be imported here as explicitly provenance-tagged evidence snapshots. Such imports never change the source RQIR repository.
