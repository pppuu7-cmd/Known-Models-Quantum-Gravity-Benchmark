# KMQGB Research Log

## 2026-09-08 — KMQGB-001 — standalone migration and authority isolation

- Created standalone benchmark authority in `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`.
- Identified the exact source as RQIR branch `rqir7-known-models-benchmark`, source HEAD `782df9af3af1ca55ca4f9bf143e2723a7a8f18bc`, base `02ad31e89f1df0d5515779e6b7526e8eb5505667`.
- Migrated all seven benchmark artifacts from `known_models_benchmark/` into root-level standalone paths.
- Rewrote recovery plumbing so future KMQGB work cannot accidentally write benchmark state into the main RQIR repository.
- Preserved RQIR source branch and `main` unchanged.
- Observed external RQIR authority at SHA `5fed1f52c013e9e469be73596e2c80932289c725`, authoritative research Iteration 563, MODEL_READINESS 24%, with rank10 heavy computation active.
- KMQGB heavy-compute policy therefore remains lightweight/read-only with respect to the shared runner until RQIR heavy work is no longer active or a separate runner is explicitly available.
- Current benchmark realization remained GR Einstein–Hilbert, Lambda=0, weak-field Minkowski.
- Initial scientific blocker was literal recovery of frozen Q1–Q7, comparator span, quotient/residual rule, and source/Ward/contact/K2 target contract.

## 2026-09-08 — KMQGB-002 — protocol recovery, two terminal controls, semiclassical start

### Literal protocol recovery

- Recovered Q1–Q7 and base residual authority from external RQIR `README.md`, blob `e431df35d929aa8b06b1b1369a2dc80352efe9e9`.
- Recovered comparator registry C0–C6 from `candidate_gravity/BASELINE_COMPARATORS.md`, blob `a2b45188710c885f979123f77fa7aad2273b9983`, introduction commit `fa841b0f5c4dc9a3f17af52f0ec5477c00b1502a`.
- Recovered F0–F7 existing-model funnel semantics from `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`, blob `2757e8fe1004b5c0caef51d6d9fee6f982ac81d4`.
- Recovered the fail-closed fixed-comparator preflight semantics from Iteration 504 commit `9af20b657eb89114a954b55b75b59bb3cf284777` and the current RQIR front.

### M01 — GR null control

- The declared classical Einstein–Hilbert weak-field realization is literally the C0 Classical GR comparator in its overlap domain.
- By the RQIR residual definition `Delta_A = O_A^model - O_A^baseline`, exact C0 identity gives analytic zero residual in the declared baseline domain.
- Terminal status: `EXACT_COMPARATOR_IDENTITY`.
- Interpretation: successful null-control recognition, not a consistency failure of GR.

### M02 — perturbative quantum GR EFT

- Located the existing RQIR concrete reference `ANSATZ-PQG-EFT-001` v0.1, instantiated at Iteration 133 commit `8f5051b8f9041ba0164b7e734be246188e664e62`.
- Imported provenance for MODEL, GATE_STATUS, ASSUMPTIONS_LEDGER and DERIVATION_MAP without modifying RQIR.
- Source RQIR explicitly states `ANSATZ-PQG-EFT-001 == C5`; D-008 marks this comparator identity `PROVED_BY_DEFINITION` and QG-007 records `REFERENCE_DEGENERACY_C5`.
- KMQGB terminal status: `EXACT_COMPARATOR_IDENTITY`.
- Interpretation: exact non-novelty relative to identical C5, not an inconsistency of perturbative quantum GR EFT.

### M03 — semiclassical gravity

- Activated concrete control `SCG-MINK-SCALAR-LR-001`: renormalized semiclassical Einstein equation with free scalar quantum matter and Minkowski linear-response control.
- Added initial audit using Hu–Verdaguer semiclassical equation/renormalization and Anderson–Molina-París–Mottola flat-space linear-response stability evidence.
- Current blocker: freeze exact scalar mass/coupling, state, renormalization/counterterm convention and observable domain before terminal comparator classification.

### Progress

- Terminal queue coverage: `2/9 = 22.22%`.
- Current active target: M03 semiclassical control.
- No heavy KMQGB job dispatched because external RQIR still reports shared-runner heavy rank10 work.
