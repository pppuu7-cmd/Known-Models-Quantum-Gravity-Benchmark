# KMQGB Migration Provenance

Migration date: 2026-09-08
Destination: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`, branch `main`.
Source: `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction`, branch `rqir7-known-models-benchmark`.
Source benchmark HEAD: `782df9af3af1ca55ca4f9bf143e2723a7a8f18bc`.
Source branch base: `02ad31e89f1df0d5515779e6b7526e8eb5505667`.
External RQIR authority observed at migration checkpoint: `5fed1f52c013e9e469be73596e2c80932289c725`, authoritative research Iteration 563.

## Migrated artifact ledger

| Source path | Destination path | Treatment |
|---|---|---|
| `known_models_benchmark/README.md` | `README.md` | migrated; standalone repository metadata added |
| `known_models_benchmark/models/gr/audit.md` | `models/gr/audit.md` | migrated scientifically unchanged in scope |
| `known_models_benchmark/models/gr/result.json` | `models/gr/result.json` | migrated scientifically unchanged in scope |
| `known_models_benchmark/protocol/BACKUP_AND_RECOVERY_METHOD.md` | `protocol/BACKUP_AND_RECOVERY_METHOD.md` | migrated; recovery references rewritten for standalone repo |
| `known_models_benchmark/protocol/FROZEN_RQIR_PROTOCOL_REFERENCE.md` | `protocol/FROZEN_RQIR_PROTOCOL_REFERENCE.md` | migrated; RQIR marked read-only external authority |
| `known_models_benchmark/protocol/KMQGB_CANDIDATE_GRAVITY_SEPARATION.md` | `protocol/KMQGB_CANDIDATE_GRAVITY_SEPARATION.md` | migrated and hardened into repository firewall |
| `known_models_benchmark/recovery/RESTORE_FROM_NEW_CHAT.md` | `recovery/RESTORE_FROM_NEW_CHAT.md` | migrated; standalone recovery entrypoint |

## Preservation rule

The source RQIR branch and `main` were not modified or deleted during migration. The old branch remains historical provenance. New benchmark writes are authorized only in this repository. Reads from RQIR are permitted solely to consume frozen protocol/Candidate Gravity authority.

## Scientific continuity

Migration changes repository location and recovery plumbing only. It does not convert provisional GR conclusions into terminal conclusions and does not alter frozen RQIR gates. GR remains nonterminal until literal Q1–Q7/comparator/quotient authority is recovered and mapped.
