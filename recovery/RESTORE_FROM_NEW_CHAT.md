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
10. Read `third_wave/README.md` and the active third-wave model `audit.md` / `result.json` if present.
11. Fetch external repository `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction` `main` and `candidate_gravity/recovery/CURRENT_QG_FRONT.md` separately and read-only; do not confuse moving Candidate Gravity authority with KMQGB authority.
12. Resume from `next_actions` in `state.json`.

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
- Every final status must be one of the allowed status strings documented in `protocol/BACKUP_AND_RECOVERY_METHOD.md`.

## Candidate Gravity design layer

Benchmark results may generate reusable design lessons for a future KG model. Those lessons are stored in:

- `protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md`;
- `recovery/CANDIDATE_GRAVITY_RESEARCH_HANDOFF.md`.

They are design evidence only. They must not change RQIR Candidate Gravity readiness or promote an ansatz without an independent derivation.

## Migration provenance

The standalone repository was initialized from source branch `rqir7-known-models-benchmark` at source HEAD `782df9af3af1ca55ca4f9bf143e2723a7a8f18bc`, with original branch base `02ad31e89f1df0d5515779e6b7526e8eb5505667`.

## Minimal new-chat instruction

`Продолжай исследование KMQGB и полезные наработки для будущей Candidate Gravity. Восстанови состояние по recovery/RESTORE_FROM_NEW_CHAT.md и recovery/CANDIDATE_GRAVITY_RESEARCH_HANDOFF.md, затем читай protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md. Не меняй исторические 9/9 и 5/5 и не записывай benchmark-изменения в основной RQIR.`
