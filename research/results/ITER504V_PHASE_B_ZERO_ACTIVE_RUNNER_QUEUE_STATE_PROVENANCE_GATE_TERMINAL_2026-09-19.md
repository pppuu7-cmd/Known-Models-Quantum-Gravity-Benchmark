# Iter504V Phase-B zero-active-runner queue-state provenance gate — terminal record

Date: 2026-09-19
Gate: `ITER504V_PHASE_B_ZERO_ACTIVE_RUNNER_QUEUE_STATE_PROVENANCE_GATE`

## Preregistration

Prospectively frozen before the decisive snapshot at commit `499ae185c2cd2f27cc0ca2191ff73fe07b2aa50c`.

Frozen authority:

- repository `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`;
- source run `35405065903`, attempt 1;
- immutable head `31fcdacffcc394e96b73917083281edb90d6753c`;
- source workflow blob `a34f23eaab9b7fec0a1da2b0b684031a24cfa360`;
- complete job pagination pages 1..4 with `per_page=100`;
- no artifact ZIP bytes or scientific payload authorized.

## Result

Fresh post-freeze GitHub Actions reads establish:

- run endpoint: `queued / conclusion=null`;
- complete job inventory: `385`;
- `completed = 100`;
- `queued = 285`;
- `in_progress = 0`;
- source-lock job `105792998164 = completed/success`.

All positive controls passed. The run remained nonterminal, the full 385-job inventory was present, zero jobs were actively executing, and 285 jobs remained queued.

## Classification

`ITER504V_PHASE_B_QUEUE_ONLY_NONTERMINAL_STATE_VERIFIED_SCOPED`

Canonical result: `research/results/ITER504V_PHASE_B_ZERO_ACTIVE_RUNNER_QUEUE_STATE_PROVENANCE_GATE_2026-09-19.json`.
Canonical serialization SHA256: `5c4c021e4a645bd2e3acca7f22bc763a5f3d562af5cafd91434f4d5a96a06021`.
Canonical result commit: `05c71ac24fc9323b8f1c5830fdee4387e73aa0e9`.

## New fact

At the frozen post-preregistration snapshot, the exact source run had entered a queue-only nonterminal topology: every remaining nonterminal job was queued and no job was `in_progress`.

This is stronger than the preceding run/job coherence result because it removes active execution from the instantaneous topology. It does **not** establish why the jobs are queued.

## Retained authority incompleteness

This result does not repair the already verified successful-execution incompleteness of attempt 1. Required timeout/cancelled shards exist in both Python environments, so the attempt cannot satisfy the frozen requirement of exactly 192 successful-complete shards in Python 3.11 and exactly 192 successful-complete shards in Python 3.13.

## Claim ceiling

The result establishes only an instantaneous GitHub Actions execution-state topology. It does not attribute the queue state to billing, account limits, GitHub capacity, runner scarcity, policy, cancellation, or any other cause. It does not classify Phase-B science, consume partial science, authorize a rerun, alter historical results, or support any D7/Candidate-Gravity/global claim.

`queued != scientific BLOCKED`; `no active runner != scientific FAIL`; `TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`.
