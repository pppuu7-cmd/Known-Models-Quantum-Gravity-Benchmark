# Iter504U terminal repaired-Critic scientific authority

Date: 2026-09-17
Status: TERMINAL_SCIENTIFIC_AUTHORITY

## Gate

`ITER504U_HELDOUT_LOCAL_D_GENERALIZATION_FIREWALL`

Terminal closure gate: `ITER504U_REPAIRED_CRITIC_CLOSURE`.

## Terminal classification

`ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED`

This is the frozen scientific PASS label for the prospectively frozen six-case Iter504U held-out cohort only.

## Frozen source authority

- preregistration commit: `05b8e9354c9a7805f0fce18b904346a986a0787f`
- immutable source/launch head: `102c7f9cafec956f3bc7bed4384ae755c98f761a`
- source run: `35246605860`
- source attempt: `1`
- source terminal status/conclusion: `completed/success`
- source terminal updated_at: `2026-09-17T19:50:49Z`
- closure artifact-freeze authority commit: `3302f77593e668ab48fdff887801571fa46467b1`
- closure artifact-freeze authority blob: `6154f02e9e04c8c14c3b4433f1afddce37e4fb9f`
- science payload consumed before artifact freeze: `false`
- source run classified before repaired Critic: `false`

The prospective closure authority freezes the exact successful source-lock, 12 case jobs, two assembly jobs, aggregate job, and exact 15 upstream immutable artifact IDs/digests. The historical original source-workflow Critic job/artifact is explicitly excluded from repaired closure authority.

## Independent repaired Critic authority

Single closure launch commit/head:

`732b9a035472f3b67b00ce985f695c03d7e90bb8`

Actions run:

`35267499787` — `KMQGB Iter504U repaired Critic closure`, run number 1, attempt 1, `completed/success`.

Jobs:

- source-lock `105358214002`: success
- review Python 3.11 `105358279236`: success
- review Python 3.13 `105358279171`: success
- closure `105358414895`: success

The independent reviews downloaded only the prospectively frozen immutable 15 upstream artifacts, reconstructed the decision under the repaired Critic in both Python environments, and the closure required byte equality of `repaired-critic.json`, return code, and downloaded-content SHA256 list.

## Repaired Critic result

Both Python 3.11 and Python 3.13 independently returned exactly:

- classification: `ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED`
- critic errors: `[]`
- cross-environment exact decision agreement: `true`
- total cases: `6`
- total terminal leaves: `19`
- total unresolved leaves: `0`
- channels: `243`
- `MAX_DEPTH=3`
- exact threshold: `1/20`
- exact robust slope floor: `1`
- repaired Critic payload SHA256: `477c582cdf96c3211b84c2c5506cfa52debad409a0383841daccbde84d36adde`
- decision projection SHA256: `b44f7bd0711a45d5469c8c1ce968f9b7f7e4cbe773dd33e0fb1bcf5beb22d3e6`

All negative controls passed, including:

- `C4_true_leaf_false_rho`
- `changed_depth`
- `changed_floor`
- `changed_threshold`
- `channel_pruning`
- `development_box_inserted`
- `float_decision_transport`
- `leaf_binding_tag_removed`
- `missing_heldout_case`
- `non_dyadic_partition`
- `premature_unresolved_leaf_depth`
- `root_derivative_reuse`
- `wrong_R_cohort`
- `wrong_case_identity`
- `wrong_rho_cohort`

## Canonical closure payload

- repaired Critic SHA256: `5e81675fa60f344643675d45e3211e41406721fd96d53b1a5329755bda5956b2`
- closure payload SHA256: `56b86f4d8a8224544c55344cd08bfd8b9a6a05022059d1fb0af84e9e76439d6c`
- cross-Python repaired-review equality: `true`
- cross-environment exact decision agreement: `true`

Closure artifacts, all unexpired at terminal read:

- `iter504u-repaired-critic-review-3.11`: id `10517615531`, digest `sha256:1d5301cc8f6cd7609989af78d1141588773e2d7c230194263cde56fa87771f2a`
- `iter504u-repaired-critic-review-3.13`: id `10517600640`, digest `sha256:1eda7268243dfe6d2168e5063788582cf91023a5c80af0ac9004cfe76cfe271d`
- `iter504u-repaired-critic-closure`: id `10516579339`, digest `sha256:ee2399d5efdf58a829edfab57b30e31c2955663d538f89623bbba85c8390afdc`

## Critic-control repairs incorporated

C4 methodology authority remains terminal:

`ITER504U_CRITIC_C4_FIXTURE_REPAIR_VALIDATED_SCOPED`, run `35252175158`.

Shallow-unresolved depth-binding methodology authority remains terminal:

`ITER504U_CRITIC_SHALLOW_UNRESOLVED_DEPTH_BINDING_REPAIR_VALIDATED_SCOPED`, run `35266020916`.

These repairs modify only independent Critic/control validation. Producer evaluator, assembler, aggregate, source realization, held-out cohort, R/rho grids, threshold, floor, precision, channels, dyadic partition/local-D construction, depth, and frozen scientific taxonomy were not changed or refit after held-out outcomes.

## Scientific interpretation

Within the exact six prospectively frozen held-out cases H0–H5, the local-D certificate generalized without unresolved leaves under the frozen depth-3 decision procedure, and the result reproduced exactly across Python 3.11 and 3.13 under the repaired independent Critic.

This terminal PASS supports the scoped held-out generalization hypothesis tested by Iter504U. It does not establish all-1888-state coverage, an all-model-family theorem, D7 closure, Candidate Gravity authority, or a universal quantum-gravity mechanism.

## Claim ceiling

Exact frozen Iter504U six-case held-out run only.

This authority does **not** authorize `ALL_KNOWN_MODELS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `QUANTUM_GRAVITY_SOLVED`, `UNIQUE_MECHANISM`, `D7_FULLY_CLOSED`, `CANDIDATE_GRAVITY_ESTABLISHED`, `NEW_PHYSICS_FOUND`, all-domain Iter504 promotion, or equivalent global claims.

## Required successor

Before opening a new substantive science branch, perform exactly one bounded end-to-end infrastructure audit of:

`prereg -> single production -> immutable artifacts -> independent Critic -> terminal authority -> recovery -> next gate`.

After that audit, freeze infrastructure if no concrete blocker remains, rebuild the unresolved scientific DAG, and select the strongest counterexample-first discriminator by approximate `EIG × downstream unlocks × falsifiability / compute cost`, rather than mechanically advancing the iteration number.
