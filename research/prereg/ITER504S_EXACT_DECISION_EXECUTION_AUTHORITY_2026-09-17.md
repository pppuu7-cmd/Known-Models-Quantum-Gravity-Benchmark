# Iter504S exact-decision single scientific execution authority

Date: 2026-09-17
Status: PROSPECTIVELY FROZEN BEFORE EXACT-DECISION SCIENTIFIC OUTPUT

Gate:

`ITER504S_ROOT_DERIVATIVE_VS_CHANNEL_COMPETITION_DISCRIMINATOR`

This record authorizes exactly one new scientific workflow identity. It does not authorize a rerun of historical Iter504S run `35175533159` and does not change that run's diagnostic-only status.

## Immutable science authority

scientific_preregistration: `f6367456aa715fe6282ab70c1b2005971a4568c7`

derivative_extraction_repair: `88c92f86a765e9d8b441152674fc2c303f3f1ff3`

fixed_channel_drift_semantics_repair: `4ef41c0f4ceed3082fd4d80930ef5d848f18802b`

exact_threshold_firewall: `77d42eb58c03eef2356aed7a25795562760de4e3`

parent_Iter504R_source: `f846820bae39963a48272deccb2e4a539100fce1`

parent_Iter504R_terminal_result: `598ede26e0db448411537e9d5f813aa344f88d0f`

parent_Iter504R_independent_critic: `6e300294e6c9a470099776d1c30357eed3fa4b93`

## Exact-decision implementation identities

discriminator_commit: `d6fab0d6a42e79e0d9843c08c453cc0e283cc190`

assembler_commit: `2acf07c0ac5b27e55c90f88a9ffc3af05264cf23`

aggregate_commit: `d8fac6d451f266df238bd6814eea7ec29fa27dc7`

critic_commit: `ecd40392d16f2c936d3d0ff9655a3ff6d390e26d`

final_source_diff_audit: `be7b6adf13dc987f58c8179a6e230ec4a58d76fc`

exact_methodology_workflow_commit: `932866e4be11f0ced241f5e3a1a854bb74dfb637`

exact_methodology_run: `35178027196` completed/success

general_methodology_run: `35178027113` completed/success

## New scientific workflow identity

workflow_path: `.github/workflows/iter504s-exact-decision-science.yml`

workflow_creation_commit: `8b15b76f88aa0a4a7e966af589c5fc08bbc43a96`

workflow_git_blob: `8a4cf650b126d4e943d82b0014d08b6758e80c16`

The workflow is intentionally triggered only by creation of the one-shot file:

`research/notes/ITER504S_EXACT_DECISION_SINGLE_EXECUTION_TRIGGER_2026-09-17.md`

No `workflow_dispatch` trigger is present. The source-lock requires the launch commit to change exactly that one file, requires this authority record to be an ancestor, verifies this workflow blob, verifies all frozen scientific source blobs, and reruns the synthetic exact-decision adversarial self-test before scientific computation.

## Frozen environment/cohort

- runner family: GitHub-hosted Ubuntu;
- independent Python cohorts: `3.11` and `3.13`;
- `python-flint==0.9.0`;
- Arb/Acb precision: `384` bits;
- roots: `13,14,15`;
- locations: exact preregistered `LOW/MID/HIGH` only;
- rhos: `[0.35,0.9,1.6,2.7]`;
- R grid: `[6,8,10,12]`;
- all `243` channels retained;
- channel pruning forbidden;
- exact threshold: `1/20`;
- exact robust floor: `+1`.

Each root job must capture Python version, installed dependency set, platform identity, python-flint version and declared Arb precision before scientific output.

## Exact-decision transport

Scientifically active inequalities are producer-level Arb decisions. Binary64 numeric summaries are display/diagnostic only and may not determine mechanism flags or the terminal classifier.

The assembler, aggregate, and Critic consume exact producer booleans, exact rational identities and structural/provenance identities. Cross-environment agreement is required for every frozen scientific boolean and discrete identity relevant to classification.

## Frozen classifier

Allowed terminal classes remain exactly:

- `ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED`;
- `ITER504S_CHANNEL_COMPETITION_NECESSARY_SCOPED`;
- `ITER504S_FIXED_CHANNEL_NONSTATIONARITY_REMAINS_SCOPED`;
- `ITER504S_MIXED_MECHANISM_SCOPED`;
- `ITER504S_INVALID`.

No fifth class is authorized.

## Execution-only declaration

execution_only_repair: `true`

science_changed: `false`

threshold_changed: `false`

cohort_changed: `false`

classifier_changed: `false`

source_physics_changed: `false`

decision_transport_verification_changed: `true`

single_scientific_execution_authorized: `true`

The new exact execution is explicitly allowed to disagree with the historical provisional diagnostic classification. Any such disagreement must be accepted if the exact run satisfies the frozen authority.

## Launch rule

Exactly one trigger-file creation is authorized after this authority commit. Do not update the trigger afterward. Do not rerun the workflow. Do not use GitHub rerun. Do not dispatch manually.

After terminalization, persist workflow head/run identity/jobs/artifacts/digests/environment/source hashes/exact-decision payload and Critic result before updating the benchmark front.

This authority makes no mechanism claim by itself.
