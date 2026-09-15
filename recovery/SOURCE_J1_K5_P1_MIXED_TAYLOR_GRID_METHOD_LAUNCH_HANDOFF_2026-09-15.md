# KMQGB Research / Closure handoff — P1 mixed Taylor grid method gate

Date: 2026-09-15
Status: NONTERMINAL_ACTIVE_GATE

## STATE_READ
- Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark` only.
- Recovered current main before this gate: `db5ea6df79705ba90010b4787452ef32cb928f95` (`critic: verify P1 forest numerical kernel pilot`).
- Latest Critic handoff reviewed: `recovery/CRITICAL_REVIEW_SOURCE_J1_K5_P1_FOREST_NUMERICAL_KERNEL_PILOT_2026-09-15.md`, verdict `CONFIRMED_SCOPED` for the numerical kernel only.
- Critic explicitly identified the already prospectively frozen successor `SOURCE_J1_K5_P1_MIXED_TAYLOR_GRID_METHOD_PILOT` as the next admissible gate and forbade consuming nonterminal successor values.
- Historical P3 divergence remains invalidated/qualified and is not used in this gate.
- Governance remains: RQIR Core v1.0 FROZEN; D7-S2 NOT_CLOSED; D7-S3 NOT_CLOSED; D7-S4 PARTIAL_GLOBAL_NOT_CLOSED; terminal selectors forbidden; Candidate Gravity inactive.

## TARGET_GATE
`SOURCE_J1_K5_P1_MIXED_TAYLOR_GRID_METHOD_PILOT`

## WHY_THIS_GATE
This is the already-frozen direct successor of the confirmed P1 forest numerical-kernel pilot and is the required numerical-method prerequisite before any 29-orbit P1 proper-forest production subtraction. It has high downstream unlock value while remaining sharply falsifiable and scoped.

## PREREG
- Frozen preregistration: `research/prereg/SOURCE_J1_K5_P1_MIXED_TAYLOR_GRID_METHOD_PILOT_2026-09-15.md`
- Preregistration commit: `aca376c7933c20bb5cbea1f95c6fc601a82af070`
- Existing implementation commit: `4f73b7822ba910ea0904c9add0d5a1c52c206bbf`
- Frozen PASS: `P1_MIXED_TAYLOR_GRID_METHOD_CONFIRMED_SCOPED`
- Frozen BLOCKED: `P1_MIXED_TAYLOR_GRID_METHOD_PRECISION_BLOCKED`
- Frozen INVALID: `INVALID_IMPLEMENTATION`
- Interpretation ceiling unchanged: method validation only; no forest-subtracted stabilization/divergence, Eq. (4), model/family, D7, selector, or Candidate Gravity conclusion.

## WORK_PERFORMED
- Added frozen-decision aggregate implementation `code/source_j1_k5_p1_mixed_taylor_grid_method_aggregate.py`.
- Added GitHub Actions workflow `.github/workflows/source-j1-k5-p1-mixed-taylor-grid-method-pilot.yml` with source-lock plus independent LOW/HIGH lanes, `fail-fast:false`, pinned `mpmath==1.3.0`, artifact hashing, and terminal aggregate only after both lanes succeed.
- Workflow/code commit: `49a0dab06356fd81f9943364e73acb11e7c0d9e3` (`ci: run frozen P1 mixed Taylor grid method gate`).
- Authoritative Actions run created by that push: `35002079183`, workflow `source-j1-k5-p1-mixed-taylor-grid-method-pilot`, head `49a0dab06356fd81f9943364e73acb11e7c0d9e3`.
- Source-lock job `104492642126` completed success.
- LOW job `104492696982` and HIGH job `104492697029` are still `in_progress` at this handoff.

## RESULT
No terminal scientific/method result yet. Partial lane values are intentionally not read or consumed.

## CLASSIFICATION
`IN_PROGRESS_NOT_CLASSIFIED`

This is not PASS, FAIL, BLOCKED, or INVALID. Green source-lock/CI does not supply a scientific classification.

## NEW_FACT
The frozen mixed-Taylor method contract is now executable under a source-locked, independent-lane GitHub Actions workflow at authoritative run `35002079183`. No substantive method conclusion exists until the run terminalizes and the aggregate artifact is available.

## CLAIM_CEILING
No substantive mixed-Taylor method verdict; no forest-subtracted convergence/divergence claim; no Eq. (4) existence/nonexistence; no model/family failure; no D7 closure; no terminal selector; no Candidate Gravity activation.

## FILES/ARTIFACTS
- `.github/workflows/source-j1-k5-p1-mixed-taylor-grid-method-pilot.yml`
- `code/source_j1_k5_p1_mixed_taylor_grid_method_aggregate.py`
- existing `code/source_j1_k5_p1_mixed_taylor_grid_method_pilot.py`
- existing preregistration `research/prereg/SOURCE_J1_K5_P1_MIXED_TAYLOR_GRID_METHOD_PILOT_2026-09-15.md`
- Actions run `35002079183`
- source-lock job `104492642126`
- LOW job `104492696982`
- HIGH job `104492697029`
- no authoritative artifacts/digests consumed yet because the run is nonterminal.

## COMMITS
- preregistration: `aca376c7933c20bb5cbea1f95c6fc601a82af070`
- existing implementation: `4f73b7822ba910ea0904c9add0d5a1c52c206bbf`
- workflow + aggregate: `49a0dab06356fd81f9943364e73acb11e7c0d9e3`

## OPEN_BLOCKERS
1. Run `35002079183` must terminalize.
2. Both LOW/HIGH lanes must produce authoritative artifacts and digests.
3. Aggregate must apply the frozen same-step precision, step-refinement, tensor-order, exact-fixture, finiteness, cancellation-margin, structural, negative-control, and source/object locks.
4. Only then may the frozen PASS/BLOCKED/INVALID classification be recorded.

## NEXT_RECOMMENDED_GATE
First consume only the terminal aggregate of run `35002079183` under the frozen preregistration and record its result/provenance. If and only if it is `P1_MIXED_TAYLOR_GRID_METHOD_CONFIRMED_SCOPED`, the next separately prospectively frozen gate may be the 29-orbit P1 proper-forest production diagnostic. Do not launch a competing authoritative mixed-Taylor gate and do not consume partial lane values.
