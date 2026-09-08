# KMQGB — Restore from a New Chat

This file is the shortest recovery entrypoint. It intentionally assumes no usable chat memory.

## Required order

1. Use repository `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`, branch `main`.
2. Read `protocol/BACKUP_AND_RECOVERY_METHOD.md` completely.
3. Read `protocol/KMQGB_CANDIDATE_GRAVITY_SEPARATION.md`.
4. Read `recovery/CURRENT_BENCHMARK_FRONT.md`.
5. Read `recovery/state.json`.
6. Read `recovery/CANDIDATE_GRAVITY_RESEARCH_HANDOFF.md`.
7. Read `protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md` completely.
8. Read the highest-numbered immutable `recovery/RECOVERY_DELTA_NNN.md`.
9. Read `protocol/FROZEN_RQIR_PROTOCOL_REFERENCE.md`.
10. Read `third_wave/README.md` and all active third-wave audit/preflight files listed in the handoff.
11. Read `fourth_wave/PREFLIGHT.md` for candidate-pool context only. **Do not infer or freeze a fourth-wave denominator from this preflight file.**
12. Fetch external repository `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction` `main` and `candidate_gravity/recovery/CURRENT_QG_FRONT.md` separately and read-only.
13. Resume from `next_actions` in `recovery/state.json`.

## Hard constraints

- All KMQGB writes go only to `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`.
- The RQIR repository is read-only for benchmark work.
- Never reconstruct frozen gates/Q1–Q7/comparator rules from chat memory.
- Never silently change a frozen gate.
- Never equate BLOCKED with FAIL.
- Never generalize a concrete realization to a whole model family.
- Never invent missing published objects.
- Never use benchmark coverage percentages as Candidate Gravity readiness.
- Historical first-wave `9/9` and second-wave `5/5` denominators are immutable.
- Third-wave denominator is frozen at `5`; operational task percentages are not terminal coverage.
- Fourth wave remains preflight-only until third wave reaches terminal `5/5`; do not invent a fourth-wave percentage before formal freeze.
- Every final status must be one of the allowed status strings documented in `protocol/BACKUP_AND_RECOVERY_METHOD.md`.

## Candidate Gravity design layer

Benchmark results may generate reusable design lessons for a future KG model. Those lessons are stored in:

- `protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md`;
- `recovery/CANDIDATE_GRAVITY_RESEARCH_HANDOFF.md`.

They are design evidence only. They must not change RQIR Candidate Gravity readiness or promote an ansatz without an independent derivation.

Current high-level KG rule: seek a **rigid multi-channel gravitational interface** whose mean/noise/retarded/ordered/higher-statistics/quantum-channel/causal and Ward/constraint relations come from one parent dynamics and survive mediator, geometry, comparator and regulator/continuum attribution tests.

## Heavy compute guardrail

Before any KMQGB heavy job, refresh external RQIR authority. If an RQIR heavy rank or authorized successor chain is active, continue only literature/algebra/protocol/lightweight KMQGB work on the shared resources.

## Migration provenance

The standalone repository was initialized from source branch `rqir7-known-models-benchmark` at source HEAD `782df9af3af1ca55ca4f9bf143e2723a7a8f18bc`, with original branch base `02ad31e89f1df0d5515779e6b7526e8eb5505667`.

## Minimal new-chat instruction

`Продолжай KMQGB и полезные наработки для будущей Candidate Gravity. Восстанови состояние по recovery/RESTORE_FROM_NEW_CHAT.md и recovery/CANDIDATE_GRAVITY_RESEARCH_HANDOFF.md, затем читай protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md, third_wave/README.md и fourth_wave/PREFLIGHT.md. Не меняй исторические 9/9 и 5/5, не замораживай 4-ю волну до terminal 5/5 третьей и не записывай benchmark-изменения в основной RQIR.`
