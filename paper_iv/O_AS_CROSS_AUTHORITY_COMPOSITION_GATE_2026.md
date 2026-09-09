# O-AS Cross-Authority Composition Gate — 2026-09-10

**KMQGB iteration:** 154  
**RQIR standard:** Core v1.0 FROZEN  
**Purpose:** prevent a false Paper-IV PASS obtained by splicing individually strong asymptotic-safety results that are not yet demonstrated to belong to one frozen realization.

## New authority accepted

Two 2026 AS lines materially strengthen the benchmark:

1. Chiesa–Pawlowski–Reichert, arXiv:2603.10168: non-perturbative momentum-dependent scalar–graviton vertex, Lorentzian reconstruction, graviton-mediated scalar `2->2` amplitude and cross section. The published/preprint calculation omits the direct gravitational contact contribution `A4` from its primary amplitude.
2. Ihssen–Knorr–Mezger–Pawlowski–Sprenger, arXiv:2609.07829: a physics-informed RG kernel preserving diffeomorphism invariance at every RG step, background-independent effective action, Reuter fixed-point application, explicit regularisation-dependence discussion and systematic approximation-error estimate.

ERG2026 conference authority additionally states that the scalar-scattering programme has been augmented by a gravitational contact contribution resummed directly in Lorentzian signature.

## Why the pieces cannot yet be added

The frozen RQIR benchmark requires a **same-realization** physical observable. Shared framework identity or overlapping authorship is insufficient.

Before combining scattering information from one calculation with error/gauge control from another, the following map must be explicit:

- identical or explicitly mapped effective-action/vertex basis;
- identical RG trajectory / fixed-point branch;
- compatible regulator/kernel and renormalisation conditions;
- compatible gauge or diffeomorphism-invariant construction;
- identical external-state and Lorentzian analytic prescription;
- contact vertex `A4` derived in the same normalization/convention as `A_s+A_t+A_u`;
- error/truncation budget propagated to the **combined** observable rather than borrowed from a neighbouring calculation.

Without this map, a synthetic object

`A_complete := A_mediated[paper A] + A4[paper/talk B]`

is not authorized.

## Classification

`BLOCKED_CROSS_AUTHORITY_COMPOSITION_NOT_YET_SAME_REALIZATION`.

This is **not** evidence against asymptotic safety and contributes zero evidence to `NEW_REQUIRED`.

## O-AS blocker after Iter154

The remaining high-value object is now:

`SAME_REALIZATION_CONTACT_COMPLETE_DIFFEO_ERROR_CONTROLLED_LORENTZIAN_SCALAR_SCATTERING_CERTIFICATE`.

Required contents:

1. `A_s+A_t+A_u+A4` from one declared AS realization;
2. one Lorentzian state/analytic prescription;
3. one physical normalization;
4. regulator/renormalisation/gauge or diffeomorphism-invariance authority for that realization;
5. approximation/truncation/reconstruction error budget propagated to the full amplitude/cross section;
6. GR/EFT same-domain comparator and robustness statement.

## Scientific lesson

A model school can close several difficult subproblems in separate papers without yet closing one RQIR observable. Paper IV scores the **composed physical object**, not the number or quality of neighbouring ingredients.
