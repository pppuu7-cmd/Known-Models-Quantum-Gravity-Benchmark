# KMQGB Critical Review — Iter504T repair-rerun terminal authority review

Date: 2026-09-17
Lane: independent KMQGB Critical Review / Verification
Status: TERMINAL CRITIC REVIEW
Review-start main: `8100820b07d57cfce8899bab43c25936ee841a90`

## RESULT_REVIEWED

Exactly one latest terminal substantive closure result was reviewed:

- gate: `ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_GATE`;
- prospective preregistration: `a4be2171d5d325ba25b805603a2e9e30e542520b`;
- frozen terminal-review authority: `525cea7c03dfae45c668f9fb57b23ad30ac15010`;
- reviewer implementation: `cd30ab36e61f4668a73214f603dd018eeb503825`;
- aggregate reviewer: `de9596f9fc1297e31ff9f11bbf1d3f30a2f79926`;
- workflow head: `8cf5aefa4b15b5a6c7dfaf7f08d1884ba8363658`;
- authoritative Actions run: `35225818354`, terminal `completed/success`;
- historical Research/Closure classification: `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`.

The historical result is not rewritten by this review.

## PREREG_CHECK

PASS for chronology.

The terminal-review preregistration was committed after the underlying repair execution `35205054496` terminalized but before the terminal substantive artifacts were opened by this review gate. The authority ledger was then frozen before the reviewer implementation/workflow. The review is therefore a legitimate prospectively frozen post-terminal authority-restoration gate.

The frozen contract explicitly preserves the original Iter504T scientific labels and semantics, including original scientific INCONCLUSIVE `ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED`, and states that a valid recomputed INCONCLUSIVE must be recorded separately rather than relabeled as authority-restoration FAIL. It also freezes BLOCKED for required terminal artifacts/fields that are unavailable, corrupted, expired, or structurally insufficient to recompute the predicate without guessing.

## OBJECT_IDENTITY_CHECK

PASS_SCOPED for the actual exact-run data inspected.

The underlying immutable execution is repair run `35205054496` at head `10ae6bcc8447d14cecc6e550065504b23f792953`, with unchanged Iter504T roots `[13,14,15]`, rhos `[0.35,0.9,1.6,2.7]`, R cohort `[6,8,10,12]`, 243 channels, `python-flint==0.9.0`, Arb/Acb precision 384, threshold `1/20`, slope floor `1`, deterministic dyadic partition and `MAX_DEPTH=3`.

Independent download and direct inspection of the two frozen assembly artifacts reproduced byte-identical payload SHA256

`dfaa14d7b07708b9cc59d04413a86661aed37dab662705499893e601ffcb9c24`.

The actual terminal payload contains 12 leaves and 48 per-rho rows. Independent replay finds:

- all 48 serialized `rho.certified` values are exact booleans equal to `slope_floor_satisfied AND drift_within_tolerance`;
- all 12 serialized `leaf.certified` values are exact booleans equal to `all(per_rho.certified)`;
- all 12 terminal leaves have `validated_local_derivative=true`;
- all three exact rational terminal covers are contiguous and cover their frozen roots;
- all 12 leaves are scientifically certified, giving independently recomputed unresolved count `0` and the original PASS label `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`;
- C1 has 18 non-root inclusion records, 70,056 boolean components per lane, and 0 false components in this exact execution.

Thus the actual exact-run scientific PASS is arithmetically/structurally consistent with the frozen predicate. The Critic defect below is in the new terminal-review implementation contract, not evidence that these actual terminal leaves fail the scientific predicate.

## SOURCE/REALIZATION_CHECK

PASS_SCOPED.

The authority ledger correctly pins underlying run `35205054496`, launch head `10ae6bcc8447d14cecc6e550065504b23f792953`, prior C4 terminal authority, and the five required underlying terminal artifacts. The workflow source-lock checks the exact run/head and artifact IDs/digests before either review lane runs.

No source/version substitution or cross-run mixing was found.

## PROVENANCE_CHECK

PASS.

Review run `35225818354` is terminal `completed/success` at exact head `8cf5aefa4b15b5a6c7dfaf7f08d1884ba8363658`.

Jobs:

- source-lock `105217007869`, success;
- Python 3.11 review `105217073486`, success;
- Python 3.13 review `105217073481`, success;
- aggregate `105217171182`, success.

Artifacts:

- Python 3.11 `10498984379`, digest `sha256:ecaa42b702fb6e823a90862adca0c6da9869774aa7de673abb8b9c186d6c49f9`;
- Python 3.13 `10499010539`, digest `sha256:01ac6aa3746a4b3ada66080188e634fcc116f76b96cbfef9b737fa6ac30d4a24`;
- aggregate `10499190200`, digest `sha256:7d2c7181896f396ad476fba2e073d91b04ee776d81d5efb1ebda0f368a278338`.

The aggregate artifact was independently downloaded and rehashed to the same GitHub digest. Its terminal aggregate decision SHA256 is `6e764ea10206959a755914279a4dfa67adfcbe0935762377a38606a0b24be9c4`.

The underlying repair artifacts were also independently downloaded and rehashed against the frozen authority ledger:

- assembled 3.11 `10498265422`: `sha256:3e6739a93cd6e467ea4d1929c37bf68a830fabcd10e415bf2d08388ee4dc0075`;
- assembled 3.13 `10497554745`: `sha256:fee046299dee740c4a85df00eb8e6c21628ad98b7bf812a0518f8a423e6df2ff`;
- aggregate `10497359984`: `sha256:dee8780bb093f8dfe35419a1e4749127cebf730972ed1a395bc894ebfb7d0d47`;
- Critic `10498490034`: `sha256:cbe6e8856f16850f5c4ecefe07a9c64aa6a7c2c0d035383f385da99c264078a1`;
- repair verdict `10498015467`: `sha256:888edcf687b1c6705d32cd2aae3f03637732376f2eb2eadd8818690fd00cad49`.

There is no `INVALID_PROVENANCE` basis. Green CI is used only as provenance.

## SAME_REALIZATION_CHECK

PASS_SCOPED for the actual exact run.

The post-terminal review consumes the exact frozen assemblies from the same immutable repair execution and preserves C4 as a defect of the general launch-head validator path. It does not substitute another run, another root/rho/R cohort, another classifier, or synthetic production data into the substantive exact-run decision.

## NUMERICAL/STATISTICAL_CHECK

PASS_EXACT_NONSTATISTICAL for the actual terminal data.

The exact-run authority reviewer correctly rebinds the actual PASS-path leaf relation: every actual per-rho row is true/true/true, every actual leaf has all four rhos certified, and unresolved count recomputes to zero in both byte-identical environments.

However, this successful observed branch is not sufficient to validate the implementation of the entire prospectively frozen terminal-review gate, because the frozen alternate decision semantics are implemented incorrectly as detailed below.

## COUNTEREXAMPLE_ATTEMPTS

### 1. Frozen INCONCLUSIVE-label preservation — explicit counterexample succeeds

Original Iter504T prospectively freezes scientific INCONCLUSIVE as

`ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED`.

The terminal-authority-review preregistration explicitly preserves the original PASS / INCONCLUSIVE / INVALID scientific labels and further requires that an independently recomputed valid scientific INCONCLUSIVE be recorded separately, not relabeled as authority-restoration FAIL.

But the reviewer implementation defines

`EXPECTED_SCIENCE_INCONCLUSIVE = "ITER504T_LOCAL_D_THREE_ROOT_CONTINUOUS_DRIFT_INCONCLUSIVE_SCOPED"`,

which is not the original preregistered label.

Explicit contract counterexample: take a structurally/provenance-valid terminal assembly with one scientifically uncertified depth-3 leaf, set the serialized leaf/rho relations consistently, set `total_unresolved_leaves=1`, and use the correct original classification `ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED` in both environments/aggregate/Critic. The reviewer recomputes its invented label instead, records `science_classification` mismatches, and therefore routes the valid original INCONCLUSIVE case to `ITER504T_REPAIR_RERUN_AUTHORITY_RESTORATION_FAILED_SCOPED`.

This violates a prospectively frozen decision branch. The defect is outcome-independent and is present in the immutable reviewer source even though the actual observed run happened to take the PASS branch.

### 2. Frozen BLOCKED semantics for structurally insufficient fields — explicit counterexample succeeds

The frozen terminal-review contract requires `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED` when required terminal fields are structurally insufficient to independently recompute the leaf predicate without guessing.

`validate_lane()` itself returns `blocked=True` when `roots` is missing, but `main()` never consumes either lane's `blocked` flag. It concatenates the lane errors and maps any nonempty `review_errors` to `ITER504T_REPAIR_RERUN_AUTHORITY_RESTORATION_FAILED_SCOPED` unless the separately defined authority identity fails.

Explicit counterexample: keep the required artifact file present and provenance-valid but remove the `roots` field. The implementation has enough information to know the review object is structurally insufficient (`blocked=True`), yet the terminal classifier ignores that flag and emits restoration FAIL rather than the prospectively frozen BLOCKED label.

This is a second direct frozen-semantics mismatch.

### 3. C4 exact-run binding

Refutation attempt against the actual exact-run PASS failed: the downloaded actual assemblies contain no C4 violation. All 12 actual leaf-to-rho conjunctions are exact and independently recompute to true.

Therefore C4 remains a general validator-path defect but does not by itself refute the underlying exact execution.

### 4. Artifact/provenance substitution

Refutation attempt failed: frozen IDs/digests, run/head identity, downloaded ZIP SHA256 values, and byte-identical assemblies agree.

## OVERCLAIM_CHECK

PASS after qualification.

The exact downloaded data support only the frozen three-root bounded local-D PASS. Nothing here closes all 1888 states, D7, a model/family, a terminal selector, Candidate Gravity, Paper IV, or any global quantum-gravity claim.

The historical terminal-review PASS may remain recorded exactly as emitted, but because its implementation does not implement all frozen decision semantics, it cannot be promoted as a fully valid terminal-review gate result without qualification.

## VERDICT

`INVALID_IMPLEMENTATION`

The latest terminal authority-review implementation does not satisfy its prospectively frozen contract:

1. it changes the original frozen scientific INCONCLUSIVE label and therefore misroutes a legitimate original INCONCLUSIVE case into restoration FAIL;
2. it defines but ignores lane-level `blocked` state, causing structurally insufficient terminal fields to be classified as restoration FAIL instead of frozen BLOCKED.

These are implementation/decision-semantics defects, not scientific FAIL and not provenance failure.

## QUALIFICATIONS

1. The actual exact repair-run payload independently satisfies the missing C4 conjunction on all 12 terminal leaves and independently recomputes the scientific PASS with zero unresolved leaves.
2. C1/C3 evidence in the actual payload is consistent: 18 inclusion records, 70,056 booleans, exact R cohort, no observed inclusion false in this run.
3. The historical closure classification `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED` remains immutable history.
4. This Critic does not assert that the actual underlying Iter504T three-root PASS is numerically false; it rejects the new terminal-review implementation as a complete frozen gate.
5. C4 remains `CONFIRMED_SCOPED` for the reusable launch-head validator path.

## UPDATED_STATE

- latest terminal closure gate `ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_GATE = INVALID_IMPLEMENTATION` by independent Critic;
- historical terminal-review PASS remains preserved but is not independently accepted as a fully contract-valid authority-restoration gate;
- actual run `35205054496` has independently consistent exact terminal PASS data, but downstream authority remains qualified until a contract-correct authority review/repair addresses the two decision-semantic defects above;
- C4 remains true for the reusable launch-head validation path;
- `RQIR Core v1.0 = FROZEN`;
- D7-S2/S3 remain not closed; D7-S4 remains partial-global-not-closed;
- terminal selectors remain forbidden; Candidate Gravity remains inactive; Paper IV remains not authorized.

## NEXT_ADMISSIBLE_GATE

A same-object, prospectively frozen terminal-review implementation repair is admissible without changing the scientific object:

1. use the exact original scientific INCONCLUSIVE label `ITER504T_LOCAL_D_INCONCLUSIVE_SCOPED` and add an adversarial/positive fixture proving a valid unresolved exact run is retained as scientific INCONCLUSIVE rather than restoration FAIL;
2. propagate lane `blocked` state into the top-level terminal classifier and add a fixture where a required terminal field is structurally missing, requiring `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`;
3. retain the already-correct actual-run C4 leaf-to-rho recomputation, artifact ID/digest source lock, C1/C3 checks, exact R cohort, roots/rhos/channels/precision/threshold/floor/MAX_DEPTH, and interpretation ceiling;
4. rerun two independent review lanes plus aggregate with fresh artifacts/digests.

No new physics execution is required to fix these review semantics. Any change to the underlying scientific object, thresholds, source realization, scientific classifier meaning, or interpretation ceiling requires a new prospectively frozen scientific gate instead of rewriting history.