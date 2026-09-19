# KMQGB durable handoff — Iter504V Phase-B assembly reachability under cancelled shards

Date: 2026-09-19
Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`

## STATE_READ

Fresh `main` at run start was `08e60368119cc3c06dd8d493eb3fdf955300d88e`, whose latest independent Critic record confirms the prior timeout-causality result as `CONFIRMED_SCOPED`.

Active science remains `ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE` / `ITER504V_PHASE_B_SOURCE_EXECUTION`, prereg `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`, execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`, immutable launch/head `31fcdacffcc394e96b73917083281edb90d6753c`, source run `35405065903`, attempt 1.

Fresh source status during this gate remained `queued / conclusion=null`; source-lock `105792998164 = success`. Frozen first-page snapshot used by the gate: 30 jobs = 8 completed/success, 12 completed/cancelled, 8 in progress, 2 queued. Cancelled visible required case jobs occur in both Python environments: 7 in Python 3.11 and 5 in Python 3.13. Latest post-result artifact metadata read shows 24 artifacts; artifact ZIP bytes were not opened.

Older `recovery/state.json` Phase-B counters are stale. Durable override for this run is `recovery/ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_STATE_DELTA_2026-09-19.json` plus fresh GitHub state.

## TARGET_GATE

`ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_PROVENANCE_GATE`.

## WHY_THIS_GATE

The active source run is still nonterminal, so no science-value consumption or competing scientific execution is admissible. Prior terminal provenance work established that required case jobs can timeout/cancel yet still upload SHA256-digested artifacts. The highest-value remaining outcome-independent question was whether the same exact attempt can still reach a *valid* two-environment assembly/aggregate authority after terminal cancellations, and whether workflow scheduler reachability must be distinguished from semantic authority validity.

## PREREG

Prospective freeze commit: `97b4251fbcf690cedbfc475232ec607e90044b75`.

Frozen before result:

- HYPOTHESIS;
- exact OBJECT = run `35405065903` attempt 1 + immutable launch-head workflow + run/job/step metadata only;
- DEPENDENCY and source/realization authority;
- no artifact ZIP reads and no science payload reads;
- positive/negative controls;
- PASS / FAIL / BLOCKED / INVALID;
- interpretation ceiling.

No frozen scientific or gate criterion was changed after observation.

## WORK_PERFORMED

1. Read fresh `main`, current front, active-front index, stale consolidated `state.json`, and latest independent Critic commit `08e60368119cc3c06dd8d493eb3fdf955300d88e`.
2. Read fresh source run `35405065903` and first-page job/step metadata without opening any source artifact payload.
3. Prospectively froze the gate.
4. Fetched immutable workflow `.github/workflows/iter504v-phase-b-science.yml` at exact launch head `31fcdacffcc394e96b73917083281edb90d6753c`; Git blob `a34f23eaab9b7fec0a1da2b0b684031a24cfa360`.
5. Verified workflow downstream graph: `assemble-311` needs `cases-311` with `if: always()`; `assemble-313` needs `cases-313` with `if: always()`; aggregate needs both assemblies with `if: always()`.
6. Verified positive controls: source-lock success and a normal successful case shard (`105793032770`, Python 3.13, execution step success).
7. Verified negative controls: 12 terminal-cancelled case jobs in the frozen first-page snapshot, including cancellations in both Python environments.
8. Saved raw snapshot, canonical result, terminal record, state delta, and this durable handoff.
9. Performed a fresh artifact-metadata-only read after terminalization of the gate; 24 source-run artifact metadata records are visible. No ZIP was opened.

## RESULT

The workflow's `if: always()` means cancelled matrix children do not necessarily prevent downstream assembly/aggregate *jobs* from executing. Therefore scheduler reachability remains possible.

However the frozen Phase-B authority requires exactly 192 successful-complete quartile shards in Python 3.11 and exactly 192 in Python 3.13. At least one required matrix child is already terminal-cancelled in each environment, and attempt 1 has no in-attempt retry mechanism that can convert those terminal cancelled jobs into successful-complete shards. A GitHub rerun would be a distinct attempt and is outside this exact object.

Therefore the same exact attempt can no longer reach a valid complete 192+192 shard authority inventory, even if downstream `if: always()` jobs later execute and emit nominal artifacts.

## CLASSIFICATION

`ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_CANCELLED_SHARD_BLOCK_VERIFIED_SCOPED`.

This is an orchestration/provenance closure only, not Phase-B science.

Decision projection SHA256: `e07665be4a044f7abfe8e09ebc79d6cd87db9c5aa9611df8669b2349e7960c67`.

## NEW_FACT

**Scheduler reachability != valid authority reachability.** In this exact Phase-B attempt, assemblies/aggregate are configured to run under `if: always()`, but terminal cancelled required shards in both Python environments make the frozen successful-complete 192+192 authority inventory irrecoverable within attempt 1. Nominal downstream artifacts cannot cure missing successful-execution provenance.

Terminal Critic must independently require the exact successful-complete shard inventory and reject nominal assemblies/aggregate as authority if any required input shard came from a cancelled/incomplete job, irrespective of artifact presence/digest.

## CLAIM_CEILING

`TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`.

No source-science payload was consumed. No Phase-B PASS, INCONCLUSIVE, INVALID science verdict, or scientific FAIL was issued. No physical case value is asserted wrong. No all-Iter504, model/family, D7, Candidate Gravity, Paper IV, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, or `NEW_PHYSICS_FOUND` claim follows.

## FILES / ARTIFACTS

Protocol/prereg:
- `research/prereg/ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_PROVENANCE_GATE_2026-09-19.md`

Raw result:
- `research/results/ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_RAW_2026-09-19.json`

Canonical result:
- `research/results/ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_RESULT_2026-09-19.json`

Terminal record:
- `research/results/ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_TERMINAL_2026-09-19.md`

Recovery delta:
- `recovery/ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_STATE_DELTA_2026-09-19.json`

No source artifact ZIP was downloaded or opened. The latest metadata-only source-run inventory contains 24 records at the final read in this handoff.

## COMMITS

- prereg freeze: `97b4251fbcf690cedbfc475232ec607e90044b75`
- raw snapshot: `ad0e4ae013746dcf9d69a2d164ffa2a3284ad14e`
- canonical result initial save: `96d0deb13cf819b51d7fced125c0824a3d3caff1`
- decision-hash field clarification: `7e35c657efca5423e88f4625a80f348c0388e9d1`
- terminal record: `85ef2b12dde45446db8f3524100303bb1882da14`
- recovery state delta: `4068b5f844cb25267eb80bc3a36e356ae48346ef`

Latest inherited independent Critic before this gate:
- timeout-causality review `08e60368119cc3c06dd8d493eb3fdf955300d88e = CONFIRMED_SCOPED`.

## OPEN_BLOCKERS

1. Source run `35405065903` remains nonterminal.
2. Attempt 1 is already authority-incomplete because terminal cancelled required shards exist in both environments.
3. Exact terminal run/job/step/artifact inventory is not yet frozen because the source run is not terminal.
4. No substantive source artifact may be opened before that terminal inventory freeze.
5. Independent terminal Critic remains required and must preserve all previously verified assembler/aggregate binding obligations plus job/step successful-completion binding and timeout/cancelled-shard exclusion.

## NEXT_RECOMMENDED_GATE

While source run `35405065903` remains nonterminal: only status/provenance monitoring.

After natural terminalization: prospectively freeze the exact terminal run/job/step/artifact inventory and digests **before** opening substantive payload. Because attempt 1 is already proven unable to satisfy the required 192+192 successful-complete shard inventory, the next terminal closure should classify exact execution completeness under frozen implementation/provenance semantics and must not reinterpret incomplete execution as scientific FAIL. Do not launch a competing same-object science run unless a separate future authority explicitly authorizes a repair/re-execution.
