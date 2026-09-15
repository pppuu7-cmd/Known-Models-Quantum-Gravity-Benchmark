# KMQGB Critical Review preterminal audit — P1 mixed Taylor grid method

Date: 2026-09-15
Lane: independent Critical Review / Verification
Status: `NONTERMINAL_AUDIT_ONLY`

## RESULT_REVIEWED

No terminal scientific/method result is reviewed in this note.

The current authoritative Research workflow is:

- gate `SOURCE_J1_K5_P1_MIXED_TAYLOR_GRID_METHOD_PILOT`;
- preregistration commit `aca376c7933c20bb5cbea1f95c6fc601a82af070`;
- implementation commit `4f73b7822ba910ea0904c9add0d5a1c52c206bbf`;
- workflow/aggregate head `49a0dab06356fd81f9943364e73acb11e7c0d9e3`;
- authoritative run `35002079183`;
- source-lock job `104492642126` completed success;
- LOW job `104492696982` in progress at audit time;
- HIGH job `104492697029` in progress at audit time;
- aggregate not yet authoritative;
- no partial substantive lane values were read or consumed.

Per governance, this note creates no competing scientific/method verdict. It is limited to chronology, frozen-contract, provenance, code inspection, and outcome-independent counterexample preparation.

## PREREG_CHECK

Chronology is prospective. Commit ancestry is

`aca376c7...` (prereg) -> `368ccf1e...` (independent Critic note) -> `4f73b782...` (implementation) -> later workflow head `49a0dab...`.

The preregistration freezes, before implementation/result:

- exact object `alpha=0.55`, `k=5`, P1 exponents `(1,1,1,1,2,2,2,2,2,2)`;
- barycentric `Gamma_S(lambda)=C_S+lambda(I-C_S)`;
- scalar orders `r_2=2`, `r_3=7`, `r_4=15`;
- operator digest `sha256:c3e0ca0c5a5357887db79b7b0a1c5a0a1042c450ca13f7e2599c7e3801ef8a9c`;
- four exact test forests;
- LOW `dps=1100, h=2^-100`;
- HIGH `dps=1500, h=2^-100,2^-140`;
- same-step, refinement, tensor-order, polynomial-fixture, finiteness, cancellation-margin and negative controls;
- terminal branches PASS / PRECISION_BLOCKED / INVALID_IMPLEMENTATION;
- method-only interpretation ceiling.

No evidence of a post-hoc scientific-contract edit was found before launch.

## OBJECT_IDENTITY_CHECK

A code-level object-identity defect candidate is present **before any terminal output is consumed**.

The frozen object requires decimal `alpha=0.55` at the active high precision. The validated predecessor numerical kernel stores

`ALPHA = "0.55"`

and converts it with `mp.mpf(ALPHA)` only inside evaluation, after `mp.mp.dps` has been set by `main()`.

The new mixed-Taylor implementation instead defines at module import time:

`ALPHA = mp.mpf("0.55")`

and only later, inside `main()`, sets `mp.mp.dps = 1100` or `1500`.

With standard mpmath initialization this constructs `ALPHA` at the default ~15-decimal-digit context and later precision increases do not restore the lost digits. An independent reviewer replay of exactly this initialization order gives the stored value

`0.5500000000000000444089209850062616169452667236328125`

rather than the prospectively frozen high-precision decimal `0.55`.

This is an outcome-independent wrong-object counterexample candidate, not a statement about partial workflow values.

## SOURCE/REALIZATION_CHECK

The P1 exponent pattern, `k=5`, frozen forests, scalar order boxes and barycentric collapse implementation are visibly aligned with the preregistration.

The operator digest control is weaker than an executable digest recomputation: `structural_controls()` checks that the expected digest string occurs in the historical terminal result, while the numerical lane imports the current `source_j1_k5_scalar_forest_operator_pilot` module. At the inspected workflow head the imported operator source appears consistent with the terminal operator implementation, so no actual mismatch is asserted here. Hardening should nevertheless prefer a current-spec recomputation or source/blob lock rather than a marker-string presence test.

## PROVENANCE_CHECK

Run `35002079183` is authoritative for the launched gate and remains nonterminal at audit time. Source-lock completed success; LOW/HIGH are still executing and the aggregate has not run. Therefore:

- no lane projection values are scientific/method evidence yet;
- no artifact digest is consumed as a terminal authority;
- green source-lock is chronology/provenance only.

The workflow pins `mpmath==1.3.0`, uses independent LOW/HIGH matrix lanes with `fail-fast:false`, hashes lane outputs, and aggregates only if the lane matrix succeeds.

## SAME_REALIZATION_CHECK

Pending terminalization, but the `ALPHA` initialization defect candidate already breaks exact same-object identity at source level unless repaired or shown not to affect the frozen object.

The predecessor kernel's parent raw authority uses high-precision parsing of the string `"0.55"`. The mixed-Taylor lane's `raw_parent_lock()` uses the prematurely rounded module-level `ALPHA`.

Independent reviewer control on the same P1 raw pairing at `k=5` gives:

- high-precision `alpha=0.55`: parent raw normalized error approximately `3.39e-81`;
- import-time rounded `ALPHA`: parent raw normalized error approximately `2.72e-20`.

The frozen parent-raw tolerance is `1e-65`. Thus the wrong-alpha construction is large enough to be detected by the preregistered raw lock by about 45 decimal orders. This control is prepared independently of the still-running lane and does not consume a partial Action value.

## NUMERICAL/STATISTICAL_CHECK

No terminal numerical result is evaluated.

Code-level observations only:

1. Tensor Lagrange weights implement evaluation of the unique degree-box interpolant at physical point 1 and are consistent with the frozen Newton-forward objective.
2. Exact polynomial fixtures are structurally appropriate.
3. The degree-`r+1` adversarial fixture is outcome-sensitive to the frozen step scales.
4. Cancellation condition-number accounting is present.
5. The module-level `ALPHA` construction occurs before the lane raises `mp.mp.dps`, so all actual-Gaussian calculations and the raw parent lock use the prematurely rounded value.

## COUNTEREXAMPLE_ATTEMPTS

1. **Wrong P1 object via alpha precision.** Explicit code-level counterexample prepared: import-time `mp.mpf("0.55")` is not the same high-precision decimal object frozen by the contract; independent raw-pairing replay changes the parent-lock error from ~`3.39e-81` to ~`2.72e-20`.
2. **Wrong forest/order boxes.** Not found in code inspection; the four boxes match the preregistration.
3. **Nonlaminar acceptance.** A negative control exists and rejects `{0,1}` / `{1,2}` before scientific classification.
4. **Historical 3D order promoted into scalar gate.** A negative order-9 control exists; frozen SINGLE15 uses 15.
5. **Operator digest marker promoted to actual source lock.** Hardening issue identified: marker-string presence does not by itself cryptographically bind the imported current module. No current mismatch is asserted.
6. **Partial values promoted to science.** Explicitly avoided.
7. **Green CI promoted to science.** Explicitly avoided.

## OVERCLAIM_CHECK

No scientific/method result exists yet. In particular there is no authority for:

- `P1_MIXED_TAYLOR_GRID_METHOD_CONFIRMED_SCOPED`;
- a precision blocker classification;
- any forest-subtracted stabilization/divergence statement;
- Eq. (4) existence/nonexistence;
- model/family failure;
- D7 closure or terminal selectors;
- Candidate Gravity activation.

## VERDICT

`NO_TERMINAL_VERDICT — AUTHORITATIVE WORKFLOW NONTERMINAL`

This string is a review-state marker, not one of the terminal scientific verdicts.

## QUALIFICATIONS

- The implementation has a concrete wrong-object defect candidate in `ALPHA` initialization.
- Because the frozen raw parent lock should detect it, the still-running workflow may eventually self-classify the lane as invalid; no prediction is promoted to a terminal result here.
- If a later terminal aggregate were to report PASS without correcting/explaining this object mismatch, the independent Critic must treat the alpha construction as a direct frozen-contract implementation challenge rather than accepting green CI.
- Repairing the code to retain `ALPHA` as string/exact decimal until after `mp.mp.dps` is set is an implementation repair that preserves the frozen scientific object; changing alpha, steps, tolerances, forest boxes, or classifier would require prospective scientific-contract treatment as applicable.

## UPDATED_STATE

- authoritative gate remains nonterminal;
- no partial substantive values consumed;
- P1 forest numerical-kernel predecessor remains the latest reviewed terminal predecessor;
- mixed-Taylor code audit has a prepared explicit alpha-precision counterexample;
- governance unchanged: `RQIR Core v1.0 = FROZEN`, `D7-S2 = NOT_CLOSED`, `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`, terminal selectors forbidden, Candidate Gravity inactive.

## NEXT_ADMISSIBLE_GATE

Do not launch a competing mixed-Taylor gate and do not classify the current run before terminalization.

On terminalization, first audit the final run status, LOW/HIGH/aggregate artifacts and digests, then apply the frozen decision contract. Independently verify that the actual numerical object is exactly the frozen `alpha=0.55` realization. If the existing source remains unchanged, the import-time-alpha issue must be resolved as an implementation matter before any PASS can be independently confirmed.
