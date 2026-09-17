# Current Benchmark Front
Updated: 2026-09-17

Fresh repository `main` and fresh Actions state always outrank this navigation document if they diverge.

## Latest terminal closure authority

Gate: `ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_GATE`.

Terminal classification:

`ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`

This is an exact-run authority validation PASS for completed repair run `35205054496`; it is not a universal validation of the immutable launch-head workflow.

Authority / execution chain:

- prospective terminal-review preregistration `a4be2171d5d325ba25b805603a2e9e30e542520b`;
- frozen review authority `525cea7c03dfae45c668f9fb57b23ad30ac15010`;
- reviewer `cd30ab36e61f4668a73214f603dd018eeb503825`;
- aggregate reviewer `de9596f9fc1297e31ff9f11bbf1d3f30a2f79926`;
- workflow head `8cf5aefa4b15b5a6c7dfaf7f08d1884ba8363658`;
- authoritative review Actions run `35225818354`, terminal `completed/success`;
- jobs: source-lock `105217007869`, Python 3.11 `105217073486`, Python 3.13 `105217073481`, aggregate `105217171182`;
- artifacts: Python 3.11 `10498984379` / `sha256:ecaa42b702fb6e823a90862adca0c6da9869774aa7de673abb8b9c186d6c49f9`; Python 3.13 `10499010539` / `sha256:01ac6aa3746a4b3ada66080188e634fcc116f76b96cbfef9b737fa6ac30d4a24`; aggregate `10499190200` / `sha256:7d2c7181896f396ad476fba2e073d91b04ee776d81d5efb1ebda0f368a278338`;
- lane decision SHA256 `7db8327005022341541ef0b62df9a87a02e8741d5716ddf2deb397fb1b95e989`;
- aggregate decision SHA256 `6e764ea10206959a755914279a4dfa67adfcbe0935762377a38606a0b24be9c4`.

## Exact validated run

The validated scientific execution is `ITER504T_IMPLEMENTATION_CONTROL_REPAIR_RERUN_GATE`, Actions run `35205054496`, head `10ae6bcc8447d14cecc6e550065504b23f792953`.

The terminal review independently opened the frozen terminal assemblies after review preregistration and did not trust launch-head top-level certification. Both assembly payloads are byte-identical with SHA256 `dfaa14d7b07708b9cc59d04413a86661aed37dab662705499893e601ffcb9c24`.

For each environment the review independently recomputed the original frozen certification predicate:

- roots `13,14,15`;
- 12 terminal leaves total;
- all 48 per-rho boolean identities are exact;
- all 12 actual terminal leaves satisfy `leaf.certified == all(rho.certified for rho in leaf.per_rho)`;
- independently recomputed unresolved leaves = `0`;
- independently recomputed scientific class = `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`;
- C1 parent-inclusion: 18 records / 70,056 component booleans per lane / 0 false;
- exact R cohort `[6,8,10,12]` is independently bound;
- all seven outcome-sensitive terminal-review controls pass;
- review errors = `[]`; independent review lanes agree exactly.

The frozen repair result `ITER504T_IMPLEMENTATION_CONTROLS_REPAIRED_AND_RERUN_VALID_SCOPED` is consistent with the independently rebound actual terminal data.

## C4 retained

`ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED` remains independently `CONFIRMED_SCOPED` for the immutable launch-head validator path.

The present review does not erase C4. It establishes that this exact terminal execution happens to satisfy the missing leaf-to-rho conjunction on every actual terminal leaf and independently reconstructs the same scientific PASS. Therefore exact-run authority is restored for run `35205054496`, while the unchanged launch-head validators remain generally unsafe for future executions unless C4 is repaired or independently rebound again.

## Historical state retained

- Original Iter504T run `35181094204` remains historically `INVALID_IMPLEMENTATION`, not scientific FAIL.
- C1 VERIFIED, C2 REFUTED, C3 VERIFIED historical closure remains immutable.
- Parent results remain `ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED`, `ITER504R_ROOT_AFFINE_REUSE_INCONCLUSIVE_SCOPED`, and `ITER504P_POINT_GRID_DRIFT_WITHIN_FROZEN_TOLERANCE_SCOPED`.
- The validated Iter504T result is only three-root bounded local-D authority; it is not all-1888-state closure.

## Next admissible work

No competing same-object execution was launched in this closure run.

For reusable validator correctness, highest-information next implementation gate is a prospectively frozen same-science C4 repair: explicitly enforce in assembler and independent Critic

`leaf.certified == all(rho.certified for rho in leaf.per_rho)`

and include the terminal adversarial C4 mutation. Preserve roots/rhos/R/channels/local-D construction/threshold/floor/MAX_DEPTH/scientific classifier/claim ceiling exactly.

Because exact run `35205054496` is independently validated, a C4 rerun is a pipeline-reusability obligation rather than a prerequisite to retain this exact-run three-root authority.

## Governance lock

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors remain forbidden.
- Candidate Gravity remains inactive; Paper IV remains `NOT_YET_AUTHORIZED`.
- `INCONCLUSIVE != FAIL`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`.
- missing object/rank/certificate != zero; scoped child result != family closure; green CI != science.
- no authority exists for `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.
