# ITER504V Phase-B assembly reachability under cancelled shards — terminal provenance result

Date: 2026-09-19

## Gate

`ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_PROVENANCE_GATE`

Prospective preregistration: `97b4251fbcf690cedbfc475232ec607e90044b75`.

## Exact object

Only orchestration/provenance of authoritative source run `35405065903`, attempt 1, immutable launch head `31fcdacffcc394e96b73917083281edb90d6753c`, exact workflow blob `a34f23eaab9b7fec0a1da2b0b684031a24cfa360`, and GitHub run/job/step metadata.

No artifact ZIP bytes were opened. No case/leaf/slope/drift/certification/assembly/aggregate/counterexample scientific payload was consumed.

## Terminal classification

`ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_CANCELLED_SHARD_BLOCK_VERIFIED_SCOPED`

This is an exact-run orchestration/provenance result only. It is not Phase-B scientific PASS, INCONCLUSIVE, or FAIL.

## Frozen controls

Positive controls pass:

- source-lock job `105792998164` remains `completed/success`;
- case job `105793032770` is `completed/success` and its frozen `Execute frozen quartile shard` step is `success`;
- immutable workflow contains explicit `assemble-311`, `assemble-313`, and `aggregate` downstream jobs.

Negative controls pass:

- the fresh first-page metadata snapshot contains 12 terminal cancelled case jobs, including 7 Python 3.11 and 5 Python 3.13 jobs;
- each cancelled execution is terminal for attempt 1 and cannot count as a successful-complete shard under the already-frozen authority semantics;
- no uploaded artifact from a cancelled execution is promoted to successful-complete merely because upload may have succeeded.

## Key workflow fact

The immutable workflow deliberately uses:

- `assemble-311: needs: cases-311; if: always()`;
- `assemble-313: needs: cases-313; if: always()`;
- `aggregate: needs: [assemble-311, assemble-313]; if: always()`.

Therefore cancelled matrix children do **not** necessarily make the downstream GitHub jobs scheduler-unreachable. The assembly and aggregate jobs may still execute after the matrices settle.

The verified block is stronger and narrower: **valid authority reachability**, not scheduler reachability.

The frozen Phase-B execution contract requires exactly 192 successful-complete quartile shards per Python environment. At least one required shard is already terminal-cancelled in each environment, and the same attempt has no in-attempt retry mechanism that can turn those terminal cancelled matrix jobs into successful-complete shards. A GitHub re-run would be a distinct attempt and is not part of this exact object.

Hence attempt 1 can no longer reach the required valid-completion inventory of 192 successful-complete shards in Python 3.11 plus 192 in Python 3.13, even if `if: always()` lets nominal assembly/aggregate jobs run and even if cancelled jobs emitted artifact metadata.

## Result snapshot

Fresh run state at the gate read: `queued / conclusion=null`.

Fresh first-page job counts:

- 30 jobs visible;
- 8 `completed/success`;
- 12 `completed/cancelled`;
- 8 `in_progress`;
- 2 `queued`.

Cancelled jobs by environment in the frozen first-page snapshot:

- Python 3.11: 7;
- Python 3.13: 5.

Decision projection SHA256:

`e07665be4a044f7abfe8e09ebc79d6cd87db9c5aa9611df8669b2349e7960c67`.

Raw metadata snapshot:
`research/results/ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_RAW_2026-09-19.json`.

Canonical result:
`research/results/ITER504V_PHASE_B_ASSEMBLY_REACHABILITY_UNDER_CANCELLED_SHARDS_RESULT_2026-09-19.json`.

## New fact

The current Phase-B source attempt is already irreversibly incomplete as a **valid-completion authority attempt** because required case-matrix jobs have terminal-cancelled in both Python environments. Downstream `if: always()` means the workflow may still manufacture nominal assembly/aggregate artifacts, so green or present downstream artifacts cannot repair the missing successful-complete shard provenance.

Any future terminal Critic must therefore distinguish:

1. scheduler reachability of assembly/aggregate jobs;
2. semantic validity of their inputs;
3. exact 192-successful-shard completion in each environment;
4. exclusion of all cancelled/time-limited shard artifacts from the valid inventory.

## Claim ceiling

`TIMEOUT/CANCELLATION/INCOMPLETE_EXECUTION != SCIENTIFIC_FAIL`.

This result does not classify any physical case, does not assert any substantive value is wrong, does not authorize an adaptive producer rerun, and does not close all-Iter504, any model/family obligation, D7, Candidate Gravity, Paper IV, or any global quantum-gravity claim.

## Next admissible action

While run `35405065903` remains nonterminal, only status/provenance monitoring is admissible. After natural terminalization, prospectively freeze the exact terminal run/job/step/artifact inventory before opening substantive payload. Because attempt 1 already lacks a valid 192+192 successful shard inventory, terminal classification must preserve implementation/provenance incompleteness rather than reinterpret it as scientific FAIL.
