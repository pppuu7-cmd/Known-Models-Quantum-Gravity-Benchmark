# ITER504V_PHASE_B_FULL_JOB_INVENTORY_PROVENANCE_GATE — prospective preregistration

Date: 2026-09-19
Status: PROSPECTIVELY FROZEN BEFORE RESULT
Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
Lane: KMQGB Research / Closure

## HYPOTHESIS

For authoritative Phase-B source run `35405065903`, attempt 1, immutable launch head `31fcdacffcc394e96b73917083281edb90d6753c`, the complete GitHub Actions job inventory can be used as a metadata-only authority-completeness object. The frozen Phase-B authority requires exactly 192 successful-complete matrix shards in Python 3.11 and exactly 192 in Python 3.13. A terminal non-success required matrix job cannot be repaired within the same Actions attempt and therefore prevents this exact attempt from reaching a valid 192+192 successful-complete source inventory, regardless of artifact upload or downstream `if: always()` scheduler reachability.

## exact OBJECT

Only GitHub Actions metadata for run `35405065903`, attempt 1:

- run status/conclusion/head/attempt;
- complete paginated job inventory and job names/status/conclusion;
- step summaries, only where needed to distinguish frozen execution-step success from job non-success;
- artifact metadata only: IDs, names, sizes, expiry, digests, run/head binding.

Forbidden in this gate:

- downloading/opening artifact ZIP bytes;
- reading case/leaf/slope/drift/certification/assembly/aggregate/counterexample scientific payload;
- changing producer code, scientific thresholds, source realization, cohort, classifier or interpretation.

## DEPENDENCY

- Phase-B preregistration `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
- static implementation Critic `eaa2d1ef84fe8370f33cec360233f60571f9bcd0 = PASS_SCOPED`;
- execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`;
- source launch/head `31fcdacffcc394e96b73917083281edb90d6753c`;
- prior timeout/cancelled-artifact/assembly-reachability closures, including independent review `cceb3d66e164f86f4cb56a47a0a52791b039e862`.

## SOURCE/REALIZATION AUTHORITY

Frozen Phase-B source object:

- complete q=1 domain = 768 canonical records;
- 192 deterministic quartile shards per environment;
- Python 3.11 and 3.13;
- 384 source compute shards total;
- four canonical physical records per shard;
- `fail-fast:false`, `max-parallel:12`, case-job timeout 360 minutes;
- exact workflow `.github/workflows/iter504v-phase-b-science.yml` at launch head.

## FROZEN INPUTS

Expected matrix identity is the Cartesian product, separately for each Python environment:

`causal in {0to5,1to4,2to3}` x `block in {0,1,2,3}` x `path in {0,1,2,3}` x `quartile in {0,1,2,3}` = 192 jobs.

Expected total matrix jobs = 384. `source-lock` is distinct from these matrix jobs. Downstream assembly/aggregate jobs are not successful-complete source shards and cannot substitute for missing/non-success matrix jobs.

## POSITIVE CONTROLS

1. Exact source-lock job must remain `completed/success`.
2. At least one normal matrix job must have `job.conclusion == success` and frozen `Execute frozen quartile shard == success`.
3. Run/head/attempt metadata must match the frozen source authority.

## NEGATIVE CONTROLS

1. A matrix job with terminal `cancelled`, `failure`, `timed_out`, or another non-success conclusion is not a successful-complete shard even if an artifact exists.
2. Artifact ID/digest alone is insufficient completion evidence.
3. A downstream `if: always()` assembly/aggregate job, if present, does not repair or replace a non-success required matrix shard.
4. Missing or duplicate expected matrix identity is an authority-inventory defect.

## PASS

Classify `ITER504V_PHASE_B_FULL_JOB_INVENTORY_AUTHORITY_INCOMPLETE_VERIFIED_SCOPED` if the complete paginated metadata establishes the exact matrix inventory and at least one required terminal non-success matrix job in either environment, with the stronger conclusion for both environments only if each environment independently contains at least one terminal non-success required matrix job. This is an implementation/provenance authority result only.

## FAIL

Classify `ITER504V_PHASE_B_FULL_JOB_INVENTORY_DEFECT_NOT_VERIFIED_SCOPED` only if complete metadata contradicts the hypothesis, e.g. all expected required matrix jobs are successful-complete and no inventory defect exists.

## BLOCKED/INVALID

- `BLOCKED_SCOPED` if complete job metadata cannot be obtained or paginated identity cannot be established without scientific payload access.
- `INVALID_IMPLEMENTATION` if this gate opens substantive artifact/science payload, changes frozen criteria after observation, uses a different run/attempt/head, or conflates artifact presence with successful execution.

## INTERPRETATION CEILING

This gate can classify only Phase-B execution/provenance authority completeness for exact run `35405065903` attempt 1. It cannot classify Phase-B scientific PASS/INCONCLUSIVE/INVALID, cannot issue a scientific FAIL, cannot authorize a producer rerun, and cannot advance D7, Candidate Gravity, Paper IV, model-family/global quantum-gravity claims, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, or `NEW_PHYSICS_FOUND`.
