# Iter504V Phase-B full job inventory provenance — terminal record

Date: 2026-09-19
Gate: `ITER504V_PHASE_B_FULL_JOB_INVENTORY_PROVENANCE_GATE`
Prospective preregistration: `cb69a9057a0b74cf8680e57f2d810d72ccdc6f93`
Source run: `35405065903`, attempt 1
Immutable source head: `31fcdacffcc394e96b73917083281edb90d6753c`
Workflow blob: `a34f23eaab9b7fec0a1da2b0b684031a24cfa360`

## Terminal classification

`ITER504V_PHASE_B_FULL_JOB_INVENTORY_AUTHORITY_INCOMPLETE_VERIFIED_SCOPED`

This is an implementation/provenance authority result only. It is not a Phase-B scientific PASS, INCONCLUSIVE, INVALID or scientific FAIL.

## Frozen-object result

Fresh GitHub Actions metadata for the exact run/attempt/head was read without opening any artifact ZIP or scientific payload.

The complete paginated job endpoint reports `total_count = 385`. The immutable workflow contains exactly:

- one `source-lock` job;
- a 192-job Python 3.11 matrix;
- a 192-job Python 3.13 matrix;
- downstream `assemble-311`, `assemble-313`, and `aggregate` jobs that depend on completion of the matrix jobs.

All four current job pages were inspected. No `assemble-*` or `aggregate` job name is yet present. Therefore the current instantiated job inventory is exactly the source-lock plus all 384 required matrix jobs; downstream jobs have not yet been instantiated in the job list.

The first page now contains 29 matrix jobs plus source-lock. Matrix status on that page is:

- success: 8;
- cancelled: 12;
- in progress: 9;
- queued: 0.

Source-lock `105792998164` remains `completed/success`.

Positive execution control remains valid:

- Python 3.13 job `105793032770`, `cases (3.13, 0to5, b0, p0, q1)`;
- job conclusion `success`;
- frozen `Execute frozen quartile shard` step `success`.

Required terminal non-success controls exist independently in both environments:

- Python 3.13 job `105793032797`, `cases (3.13, 0to5, b0, p1, q1)`: job `cancelled`, frozen execution step `cancelled`, upload step `success`;
- Python 3.11 job `105793033008`, `cases (3.11, 0to5, b0, p2, q0)`: job `cancelled`, frozen execution step `cancelled`, upload step `success`.

Because the frozen execution authority requires exactly 192 successful-complete matrix shards in each environment, and terminal cancelled matrix children cannot become successful-complete jobs within the same Actions attempt, attempt 1 cannot reach the required 192+192 successful-complete scientific-authority inventory. Later `if: always()` assembly/aggregate scheduler execution or artifact upload cannot repair that execution provenance.

## Artifact metadata snapshot

Fresh metadata-only artifact count: `25`.

All observed artifacts are bound to run `35405065903` and head `31fcdacffcc394e96b73917083281edb90d6753c` and expose GitHub SHA256 digests. No artifact bytes were downloaded or opened.

Raw snapshot:
`research/results/ITER504V_PHASE_B_FULL_JOB_INVENTORY_PROVENANCE_RAW_2026-09-19.json`

Raw snapshot SHA256:
`1a3f18c9a33f9966f99e7d82a6095e266e54ccf74234033af44b51dfafd8a2d6`

Canonical result:
`research/results/ITER504V_PHASE_B_FULL_JOB_INVENTORY_PROVENANCE_RESULT_2026-09-19.json`

Canonical result SHA256:
`a478bb8f8b0f15641ddf1d46eebed00345a61aaa29d69642041a33f3fbd8154c`

## New fact

The full current job graph is not missing matrix scheduling identities: all 384 required matrix jobs are instantiated. The authority defect is execution completeness, not failure to instantiate the matrix. At the same time, downstream assembly/aggregate jobs are not yet present in the current job inventory.

This sharpens the closure distinction:

`complete matrix instantiation != successful-complete matrix authority`.

## Science firewall

The source run remains nonterminal at this record (`queued / conclusion=null`). No case, leaf, slope, drift, certification, assembly, aggregate or counterexample value was consumed. `source_run_classified=false` and Phase-B science remains `IN_PROGRESS_NOT_CLASSIFIED`.

## Claim ceiling

This result is scoped to execution/provenance authority completeness for exact source run `35405065903`, attempt 1. It does not classify any physical value, does not create a scientific FAIL, does not authorize a producer rerun, and does not advance D7, Candidate Gravity, Paper IV, model/family/global quantum-gravity claims, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, or `NEW_PHYSICS_FOUND`.

## Next admissible action

While source run `35405065903` remains nonterminal: status/provenance monitoring only. After natural terminalization, prospectively freeze the exact terminal run/job/step/artifact inventory and digests before substantive payload access, classify terminal execution completeness under the frozen authority, and preserve all independently established assembler/aggregate binding obligations. Any repair or re-execution requires a separate prospective authority and must not rewrite attempt-1 history.
