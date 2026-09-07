# KMQGB Research Log

## 2026-09-08 — KMQGB-001 — standalone migration and authority isolation

- Created standalone benchmark authority in `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`.
- Identified the exact source as RQIR branch `rqir7-known-models-benchmark`, source HEAD `782df9af3af1ca55ca4f9bf143e2723a7a8f18bc`, base `02ad31e89f1df0d5515779e6b7526e8eb5505667`.
- Migrated all seven benchmark artifacts from `known_models_benchmark/` into root-level standalone paths.
- Rewrote recovery plumbing so future KMQGB work cannot accidentally write benchmark state into the main RQIR repository.
- Preserved RQIR source branch and `main` unchanged.
- Observed external RQIR authority at SHA `5fed1f52c013e9e469be73596e2c80932289c725`, authoritative research Iteration 563, MODEL_READINESS 24%, with rank10 heavy computation active.
- KMQGB heavy-compute policy therefore remains lightweight/read-only with respect to the shared runner until RQIR heavy work is no longer active or a separate runner is explicitly available.
- Current benchmark realization remains GR Einstein–Hilbert, Lambda=0, weak-field Minkowski.
- Current scientific blocker remains literal recovery of frozen Q1–Q7, comparator span, quotient/residual rule, and exact source/Ward/contact/K2 target contract. No scientific FAIL is inferred from this blocker.

Next: recover literal frozen protocol authority directly from RQIR repository paths; then complete GR null-control classification.
