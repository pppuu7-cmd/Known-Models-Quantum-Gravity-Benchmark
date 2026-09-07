# KMQGB Current Benchmark Front

**Updated:** 2026-09-08
**KMQGB iteration:** 002
**Repository:** `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
**Branch:** `main`
**Migration:** COMPLETE — all 7 source benchmark artifacts migrated from RQIR branch `rqir7-known-models-benchmark`; source RQIR remains unchanged/read-only for KMQGB.

## Current benchmark state

- Terminal queue coverage: **2/9 = 22.22%**.
- M01 GR null control: **`EXACT_COMPARATOR_IDENTITY`** with C0 in declared classical weak-field domain.
- M02 `ANSATZ-PQG-EFT-001` v0.1: **`EXACT_COMPARATOR_IDENTITY`** with C5 at declared theory-class level.
- Active realization: **KMQGB-M03-SEMICLASSICAL / SCG-MINK-SCALAR-LR-001**.
- M03 current state: **ACTIVE / NONTERMINAL**.
- M03 first blocker: **`SCG_REALIZATION_FREEZE`** — pin exact scalar mass/coupling, state, renormalization/counterterm convention and observable domain.

## Literal RQIR authority recovered

- Q1–Q7 + base residual: external `README.md`, blob `e431df35d929aa8b06b1b1369a2dc80352efe9e9`.
- Comparator C0–C6 registry: `candidate_gravity/BASELINE_COMPARATORS.md`, blob `a2b45188710c885f979123f77fa7aad2273b9983`.
- F0–F7 known-model funnel semantics: `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`, blob `2757e8fe1004b5c0caef51d6d9fee6f982ac81d4`.
- Fixed-comparator fail-closed preflight semantics: Iteration-504 commit `9af20b657eb89114a954b55b75b59bb3cf284777`.

## Migration / provenance authority

- Source repository: `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction`.
- Source benchmark branch: `rqir7-known-models-benchmark`.
- Source benchmark HEAD: `782df9af3af1ca55ca4f9bf143e2723a7a8f18bc`.
- Source branch base: `02ad31e89f1df0d5515779e6b7526e8eb5505667`.
- External RQIR `main` observed: `5fed1f52c013e9e469be73596e2c80932289c725`.
- External RQIR Candidate Gravity authority observed: Iteration 563, MODEL_READINESS 24%.

## Repository firewall

All benchmark writes go here only. RQIR is read-only external protocol/Candidate Gravity authority. KMQGB does not modify Candidate Gravity readiness, recovery files, iteration numbering, workflows, active runner state, or scientific authority.

Prior RQIR model/control work may be imported here only as provenance-tagged evidence. The original RQIR artifact remains unchanged.

## Heavy compute

External RQIR current front reports rank10 heavy computation active. KMQGB dispatches no competing heavy work to the shared runner. Current M03 work is literature/protocol mapping and lightweight analytic audit.

## Exact next gate

For `SCG-MINK-SCALAR-LR-001`:
1. freeze one explicit free-scalar mass/coupling choice and Minkowski-vacuum state;
2. freeze the renormalized curvature-counterterm convention/domain;
3. map F0–F7 and Q1–Q7 literally;
4. determine whether terminal relation is exact C1 identity, operational degeneracy, or a scoped blocker;
5. preserve mean-only F3 limitation as a model-interface limitation, not a generic theory consistency FAIL.

## Following gate

After M03 closure, instantiate M04 stochastic gravity as a concrete Einstein–Langevin/noise-kernel realization and test it as the stronger C2 fluctuation control.
