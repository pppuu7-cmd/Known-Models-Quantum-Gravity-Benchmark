# KMQGB durable handoff — Iter504V Phase-B case-job timeout causality provenance

Date: 2026-09-19
Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
Lane: KMQGB Research / Closure

## STATE_READ

Fresh `main` at run start was `171d8ee9b0945de095ed9f5cbc1f9296aa2007fc`, whose latest independent Critical Review confirmed the prior cancelled-job artifact-provenance gate as `CONFIRMED_SCOPED`.

Active scientific source remains:
- gate `ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE`;
- execution gate `ITER504V_PHASE_B_SOURCE_EXECUTION`;
- prereg `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
- execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`;
- immutable launch/head `31fcdacffcc394e96b73917083281edb90d6753c`;
- source run `35405065903`, attempt 1.

Fresh run endpoint remained `queued / conclusion=null`; source-lock `105792998164` remained `completed/success`. Latest validated first-page job snapshot: 30 visible jobs = 8 completed/success, 12 completed/cancelled, 8 in progress, 2 queued. Latest validated artifact metadata count: 20. No artifact ZIP or substantive science payload was opened.

`recovery/state.json` contained an older time-local Phase-B snapshot. It was not destructively overwritten; validated newer state is reconciled through `recovery/ITER504V_PHASE_B_TIMEOUT_CAUSALITY_STATE_DELTA_2026-09-19.json`, updated current front, and updated active-front index.

## TARGET_GATE

`ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_PROVENANCE_GATE`.

## WHY_THIS_GATE

The immediately preceding independently confirmed closure established that cancelled numerical jobs can still upload artifacts, so artifact ID/digest does not imply completed science. The highest-information admissible non-science question while the source run remained nonterminal was therefore causal: why were the case jobs being cancelled? Resolving whether cancellation is a reproducible execution-time-limit effect materially changes the eventual terminal provenance classifier and valid-completion inventory without consuming any partial scientific value.

## PREREG

Prospective preregistration commit:
`2fc02a80c7d4db6f05813cbb571eb01cb4fb7c53`.

Frozen object: GitHub Actions metadata/logs only for exact run `35405065903`, attempt 1, head `31fcdacffcc394e96b73917083281edb90d6753c`; first six visible cancelled case jobs by ascending job id; first visible successful case job by ascending id; source-lock; immutable source workflow. Artifact ZIP bytes and all case/leaf/slope/drift/certification/assembly/aggregate/counterexample values were out of scope.

Frozen PASS/FAIL/BLOCKED/INVALID semantics were committed before log inspection and were not changed after the result.

## WORK_PERFORMED

1. Re-read exact source workflow at launch head. Workflow blob `a34f23eaab9b7fec0a1da2b0b684031a24cfa360` explicitly sets `timeout-minutes: 360` for both Python 3.11 and Python 3.13 case matrices and runs `actions/upload-artifact@v4` under `if: always()`.
2. Re-read fresh first-page jobs after preregistration.
3. Retrieved direct GitHub Actions logs for the first six cancelled case jobs selected prospectively by ascending job id: `105793032797`, `105793032807`, `105793032871`, `105793032873`, `105793032949`, `105793033008`.
4. Retrieved direct log for successful control job `105793032770`.
5. Compared frozen numerical-step start and cancellation/completion timestamps only. No artifact ZIPs were downloaded and no scientific payload was consumed.
6. Saved canonical result, terminal record, recovery state delta, current-front reconciliation, and active-front reconciliation.

## RESULT

All six prospectively selected cancelled jobs terminated the frozen numerical step at the workflow's exact six-hour boundary, within four seconds:

- `105793032797` Py3.13 `0to5|b0|p1|q1`: `21597.088928 s`, `-2.911072 s` from 360 min;
- `105793032807` Py3.13 `0to5|b0|p0|q2`: `21600.336255 s`, `+0.336255 s`;
- `105793032871` Py3.13 `0to5|b0|p2|q1`: `21596.493428 s`, `-3.506572 s`;
- `105793032873` Py3.13 `0to5|b0|p0|q3`: `21596.734158 s`, `-3.265842 s`;
- `105793032949` Py3.13 `0to5|b0|p0|q0`: `21597.890232 s`, `-2.109768 s`;
- `105793033008` Py3.11 `0to5|b0|p2|q0`: `21598.659739 s`, `-1.340261 s`.

Each direct log contains runner marker `The operation was canceled.`; each job and frozen execution step are `cancelled`; each subsequent `if: always()` upload step succeeded.

Successful positive control `105793032770`, Py3.13 `0to5|b0|p0|q1`, completed the frozen numerical step successfully in `16379.561743 s = 272.992696 min`, well before the same six-hour boundary, and the job/upload both succeeded.

Canonical result SHA256:
`471a8369cbfdb763ef5193984fe0f60d058d183e6f5bd5fb19e61bcb1e822504`.

## CLASSIFICATION

`ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_VERIFIED_SCOPED`.

This is a provenance/execution-causality PASS only. It is not a Phase-B scientific PASS, INCONCLUSIVE, FAIL, or source-run INVALID classification.

## NEW_FACT

For the frozen prospectively selected sample, Phase-B case cancellations are caused by the source workflow's explicit `timeout-minutes: 360` boundary. The pattern is reproduced across both Python 3.13 and 3.11. Because artifact upload runs under `if: always()`, a timeout-cancelled numerical shard can still leave a successfully uploaded, SHA256-digested artifact.

Consequently, timeout-cancelled artifacts are incomplete implementation/provenance objects. They cannot substitute for the required completed four-record shard and cannot enter terminal scientific authority.

## CLAIM_CEILING

`TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`.

No case value is classified or challenged by this gate. No producer rerun is authorized while the existing source run remains nonterminal. No Iter504V family/all-domain, D7, selector, Candidate Gravity, Paper IV, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, or `NEW_PHYSICS_FOUND` conclusion follows.

## FILES/ARTIFACTS

Created:
- `research/prereg/ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_PROVENANCE_PREREG_2026-09-19.md`
- `research/results/ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_PROVENANCE_RESULT_2026-09-19.json`
- `research/results/ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_PROVENANCE_TERMINAL_2026-09-19.md`
- `recovery/ITER504V_PHASE_B_TIMEOUT_CAUSALITY_STATE_DELTA_2026-09-19.json`
- this handoff.

Updated:
- `recovery/CURRENT_BENCHMARK_FRONT.md`
- `recovery/CURRENT_ACTIVE_FRONT_INDEX_2026-09-15.md`.

Representative artifact metadata inferred only from direct job logs after cancellation, without downloading ZIP bytes:
- job `105793032797` -> artifact `10578151776`, ZIP SHA256 `568b1de7db028d7374b9f96df3b105901a987d4f69550c49d425057139dcd412`;
- job `105793032807` -> artifact `10578511467`, ZIP SHA256 `d3afa37a445d2d0144eb75643ef7c4b438ede1edfe07c04b70345a56cb69e05d`;
- job `105793032871` -> artifact `10578476614`, ZIP SHA256 `fdf7a7208432559187ba3b1551d6c6895623072e545f5868d062198647bd0d47`;
- job `105793032873` -> artifact `10577986131`, ZIP SHA256 `b697adfb4384968a81dff57bae51eaefaaf38d008ed173aca266e31062bb281f`;
- job `105793032949` -> artifact `10578986244`, ZIP SHA256 `14af8253cc3585da5a795bc3ebde1e9b0c682564ffdabbb6ff206f95369ce294`;
- job `105793033008` -> artifact `10578026205`, ZIP SHA256 `73f9e0e0984209dcd2741d239e8c675d4d08ee79a34fa381dd2997c1706e9a2d`.

## COMMITS

- gate preregistration: `2fc02a80c7d4db6f05813cbb571eb01cb4fb7c53`
- canonical result: `558c02abd710812437f8616397d27cef7091af44`
- terminal record: `a1ca2288e774895ab6f77dedc2065299df8f2b89`
- recovery state delta: `2e01dd1f22cf7b9b767a5584163802893adeed35`
- current front reconciliation: `94599d121e354a30daa8660ae3831db1c2121c8b`
- active-front reconciliation: `fff612a5c7f7a2849058f3d7faccf17dcd867e88`

## OPEN_BLOCKERS

1. Source run `35405065903` remains nonterminal and scientifically unclassified.
2. Nominal Phase-B complete authority requires 384 successful-complete shard artifacts, but timeout-cancelled shard artifacts are now known not to qualify as complete shards.
3. Terminal independent Critic must still enforce all inherited obligations: exact shard/artifact -> `shard.json` -> four physical records; every dyadic parent-inclusion edge; unresolved evidence -> classification; exact canonical 768-state projection key/sequence; exact provenance key/content-hash binding; job success; frozen numerical-step success; timeout-completeness exclusion; source/cohort/channel/precision/R/rho/tree/leaf/per-rho/unresolved-depth/cross-environment controls.
4. No substantive source artifact may be opened before a prospectively frozen terminal inventory/digest authority exists after natural source terminalization.

## NEXT_RECOMMENDED_GATE

While source run `35405065903` remains nonterminal, only status/provenance checking is admissible. Do not rerun producer science and do not launch a competing same-object scientific gate.

After natural terminalization, prospectively freeze the exact terminal run/job/step/artifact inventory and digests **before** any substantive payload read. Partition inventory into successful-complete versus timeout-cancelled/incomplete shards. Then execute exactly one separately frozen independent terminal Critic closure against the immutable valid-completion inventory. If the source execution is terminal but incomplete, classify only under frozen implementation/provenance semantics; never convert execution timeout into scientific FAIL.
