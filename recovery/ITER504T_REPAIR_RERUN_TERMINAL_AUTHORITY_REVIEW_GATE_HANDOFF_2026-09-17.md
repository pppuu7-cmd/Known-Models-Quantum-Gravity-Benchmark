# KMQGB Research / Closure handoff — Iter504T repair rerun terminal authority review

Date: 2026-09-17
Status: TERMINAL_HANDOFF

## STATE_READ

- Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark` only.
- Starting fresh main before this run: `142ef1d7e149e19752ec52e6b797f0e618cccea6`.
- Both `CURRENT_BENCHMARK_FRONT.md` and `CURRENT_ACTIVE_FRONT_INDEX_2026-09-15.md` were stale because they still described repair run `35205054496` as nonterminal.
- Fresh GitHub Actions showed repair run `35205054496` had terminalized `completed/success` at immutable head `10ae6bcc8447d14cecc6e550065504b23f792953`.
- Recovery was reconciled before terminal substantive artifact consumption: commits `e7fcaa46301dfcc01f6db3db0a259b12abcce4a0` and `76a306f78052c5227b2b3c136b09d50aa4697b2f`.
- Terminal C4 authority was read and retained: `ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED`, independent Critic `CONFIRMED_SCOPED`, exact missing validator binding `leaf.certified == all(rho.certified for rho in leaf.per_rho)`.
- Governance retained: `RQIR Core v1.0 = FROZEN`; D7-S2/D7-S3 NOT_CLOSED; D7-S4 PARTIAL_GLOBAL_NOT_CLOSED; terminal selectors forbidden; Candidate Gravity inactive; Paper IV not authorized.

## TARGET_GATE

`ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_GATE`

## WHY_THIS_GATE

The repair execution had become terminal, so the highest-information admissible question was no longer another rerun. C4 had already proven that green CI and launch-head PASS transport could not independently bind the original leaf predicate. The exact completed terminal assemblies, however, could prospectively be reviewed and independently rebound to the original scientific predicate. This gate therefore tested whether exact-run authority could be restored without changing the science and without erasing the general C4 defect.

## PREREG

- Protocol: `research/prereg/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_GATE_2026-09-17.md`.
- Prospective freeze commit: `a4be2171d5d325ba25b805603a2e9e30e542520b`.
- Authority ledger: `inputs/iter504t_repair_rerun_terminal_authority_review_authority.json`.
- Authority commit: `525cea7c03dfae45c668f9fb57b23ad30ac15010`.
- Frozen PASS: `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`.
- Frozen FAIL: `ITER504T_REPAIR_RERUN_AUTHORITY_RESTORATION_FAILED_SCOPED`.
- Frozen BLOCKED: `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`.
- Frozen INVALID: `INVALID_IMPLEMENTATION`.
- Criteria and interpretation ceiling were not changed after terminal artifacts were opened.

## WORK_PERFORMED

- Frozen the exact terminal run/head and five required repair artifacts by ID/digest before payload inspection.
- Frozen C4 as retained authority rather than treating the launch-head validators as sufficient.
- Implemented an independent reviewer that recomputes every actual per-rho certification, every leaf conjunction, unresolved counts and the original scientific classification from the terminal assembly payloads.
- Added independent C1 record/cardinality checks, exact-R cohort checks, aggregate/Critic/repair-verdict consistency, artifact-internal hashes and cross-environment identity checks.
- Added seven outcome-sensitive negative controls: both C4 mismatch directions, per-rho boolean inconsistency, R `6 -> 7`, missing C1 record, artifact identity mutation, and serialized unresolved-count mismatch.
- Ran independent Python 3.11/3.13 review lanes with `fail-fast:false` and a terminal aggregate.
- Consumed the review result only after Actions run `35225818354` terminalized.
- Saved canonical result, exact aggregate raw log, hash/artifact manifest, terminal result, current-front/index and this handoff.
- No competing same-object scientific execution was launched.

## RESULT

Authoritative review Actions run `35225818354` is terminal `completed/success` at workflow head `8cf5aefa4b15b5a6c7dfaf7f08d1884ba8363658`.

Jobs:

- source-lock `105217007869` — success;
- Python 3.11 `105217073486` — success;
- Python 3.13 `105217073481` — success;
- aggregate `105217171182` — success.

Artifacts:

- Python 3.11 `10498984379`, digest `sha256:ecaa42b702fb6e823a90862adca0c6da9869774aa7de673abb8b9c186d6c49f9`;
- Python 3.13 `10499010539`, digest `sha256:01ac6aa3746a4b3ada66080188e634fcc116f76b96cbfef9b737fa6ac30d4a24`;
- aggregate `10499190200`, digest `sha256:7d2c7181896f396ad476fba2e073d91b04ee776d81d5efb1ebda0f368a278338`.

The independently verified ZIP hashes equal the GitHub digests.

Terminal review hashes:

- lane JSON SHA256 `bab61981843310ed204caea2b81ef461a402c0e02bfd9df09593788e7772a15d` in both environments;
- lane log SHA256 `0e6ab4be6ddb1085c180fce271db80528a52c816bb1d47e369deaad0203c5d33` in both environments;
- lane decision SHA256 `7db8327005022341541ef0b62df9a87a02e8741d5716ddf2deb397fb1b95e989`;
- aggregate JSON SHA256 `5cd809948846750e51096ab19a23d8710915859a9f8afcca84bfb6ee32827dc1`;
- aggregate log SHA256 `0c08257847b686994f8782ad89a3d49d62a074f54d0b78d225a480efc692630e`;
- aggregate decision SHA256 `6e764ea10206959a755914279a4dfa67adfcbe0935762377a38606a0b24be9c4`.

Actual terminal data, independently recomputed in both review lanes:

- assembly JSON SHA256 `dfaa14d7b07708b9cc59d04413a86661aed37dab662705499893e601ffcb9c24` in both environments; byte-identical;
- root count `3` and terminal leaf count `12`;
- all 48 per-rho serialized certifications equal their frozen slope/drift conjunction;
- all 12 terminal leaves satisfy `leaf.certified == all(rho.certified for rho in leaf.per_rho)`;
- recomputed unresolved leaves `0`;
- recomputed scientific class `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`;
- C1 record count `18`, component count `70056`, false component count `0` per lane;
- exact R cohort `[6,8,10,12]` bound;
- seven frozen review controls all pass;
- review errors empty;
- review lanes agree exactly.

Underlying repair output is also consistent: `ITER504T_IMPLEMENTATION_CONTROLS_REPAIRED_AND_RERUN_VALID_SCOPED`; underlying launch aggregate and Critic both report the same original scientific class and Critic errors are empty.

## CLASSIFICATION

`ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`

PASS for exact completed-run authority restoration.

This is not a universal PASS for the unchanged launch-head validator path.

## NEW_FACT

The terminal C4 defect and the exact-run scientific authority can consistently coexist.

C4 remains true: launch-head validators do not independently enforce the leaf-to-rho conjunction. But the actual terminal payloads of run `35205054496` satisfy that missing conjunction on every terminal leaf. A stronger, prospectively frozen post-terminal review independently recomputed the original predicate and recovered the same scientific PASS in both environments.

Therefore run `35205054496` is now admissible as scoped scientific authority for the original three-root bounded local-D claim even though future executions of the unchanged validator path cannot inherit authority automatically.

## CLAIM_CEILING

Only exact run `35205054496` and the original Iter504T three-root bounded local-D claim for roots `13,14,15` are validated.

No all-1888-state closure; no D7 closure; no model/family failure; no terminal D7 selector; no Candidate Gravity; no Paper IV authorization; no `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

C4 `CONFIRMED_SCOPED` is preserved.

## FILES/ARTIFACTS

- `research/prereg/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_GATE_2026-09-17.md`;
- `inputs/iter504t_repair_rerun_terminal_authority_review_authority.json`;
- `code/iter504t_repair_rerun_terminal_authority_review.py`;
- `code/iter504t_repair_rerun_terminal_authority_review_aggregate.py`;
- `.github/workflows/iter504t-repair-rerun-terminal-authority-review.yml`;
- `results/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_CANONICAL_2026-09-17.json`;
- `results/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ACTIONS_AGGREGATE_RAW_2026-09-17.log`;
- `results/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_HASHES_2026-09-17.json`;
- `results/ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_TERMINAL_2026-09-17.md`;
- review Actions run `35225818354` and review artifacts `10498984379`, `10499010539`, `10499190200`;
- reviewed repair run `35205054496` and frozen reviewed artifacts `10498265422`, `10497554745`, `10497359984`, `10498490034`, `10498015467`.

## COMMITS

- recovery reconciliation before artifact consumption: `e7fcaa46301dfcc01f6db3db0a259b12abcce4a0`, `76a306f78052c5227b2b3c136b09d50aa4697b2f`;
- preregistration: `a4be2171d5d325ba25b805603a2e9e30e542520b`;
- authority: `525cea7c03dfae45c668f9fb57b23ad30ac15010`;
- reviewer: `cd30ab36e61f4668a73214f603dd018eeb503825`;
- aggregate reviewer: `de9596f9fc1297e31ff9f11bbf1d3f30a2f79926`;
- workflow head: `8cf5aefa4b15b5a6c7dfaf7f08d1884ba8363658`;
- canonical result: `876274b2290d0f54cf851110116c3fc4e14f211c`;
- raw aggregate log: `c721a5e2871b4e13ea683d5534fe68ea0f83534e`;
- hashes/artifact provenance: `e61e16bc934a15aa17048f37e7ce553cfebadca7`;
- terminal result: `a8221ae57ea9afa74fa897793c89998c44074bd0`;
- current-front update: `d2c7ab7056f2d54165deb79d65fd89d9360223bd`;
- active-index update: `170c9824c3be19e33e999b3b171c0757750a6768`.

## OPEN_BLOCKERS

1. The immutable launch-head validator still has terminally confirmed C4 and is not generally safe for future execution without repair or another independent terminal rebinding.
2. Iter504T remains a three-root bounded result only; extension to the broader state/family obligations is open.
3. D7-S2/D7-S3 remain NOT_CLOSED; D7-S4 remains PARTIAL_GLOBAL_NOT_CLOSED.
4. Parallel K5 physical transverse quotient/measure/observable pushforward obligations remain open/blocked as recorded in current recovery state.
5. Candidate Gravity and Paper IV remain unauthorized.

## NEXT_RECOMMENDED_GATE

At the next fresh-state run, compare downstream scientific unlocks against reusable-validator repair cost.

If Iter504T machinery will be reused or extended, prospectively freeze a same-science `ITER504T_C4_LEAF_CERTIFICATION_BINDING_REPAIR_GATE` that adds explicit assembler and independent-Critic enforcement of

`leaf.certified == all(rho.certified for rho in leaf.per_rho)`

plus the already-terminal adversarial C4 mutation, while preserving roots, rhos, R cohort, 243 channels, local-D construction, threshold `1/20`, floor `1`, `MAX_DEPTH=3`, classifier and claim ceiling.

If a different DAG frontier has higher information gain and does not rely on the defective reusable validator, it may outrank this implementation repair. Do not infer family/D7/global closure from the present exact-run validation.
