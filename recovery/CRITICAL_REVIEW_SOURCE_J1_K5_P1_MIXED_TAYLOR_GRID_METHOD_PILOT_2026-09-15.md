# KMQGB Critical Review — P1 mixed Taylor grid method pilot

Date: 2026-09-15
Lane: independent Critical Review / Verification

## RESULT_REVIEWED

Exactly one latest terminal substantive Research result was reviewed at the Actions layer:

- gate `SOURCE_J1_K5_P1_MIXED_TAYLOR_GRID_METHOD_PILOT`;
- preregistration commit `aca376c7933c20bb5cbea1f95c6fc601a82af070`;
- implementation commit `4f73b7822ba910ea0904c9add0d5a1c52c206bbf`;
- workflow / aggregate head `49a0dab06356fd81f9943364e73acb11e7c0d9e3`;
- authoritative run `35002079183`, terminal `completed/success` at 2026-09-15T18:14:02Z;
- source-lock job `104492642126` success;
- LOW job `104492696982` success;
- HIGH job `104492697029` success;
- aggregate job `104506337435` success;
- LOW artifact `10410881419`, digest `sha256:a1cd661cf23e201ef788cda6ef5123e38051f0e6996651c2551b27e4a2dabd2d`;
- HIGH artifact `10411856350`, digest `sha256:b621f9d11a52d972ac75219ded87f31072662c73c2bb16ed031e415890bdd235`;
- aggregate artifact `10411547872`, digest `sha256:e5e74cd932d86021f8881ea842926b02de2c0688404040f5051fef92a7b062b7`;
- terminal Actions aggregate classification `INVALID_IMPLEMENTATION`.

No separate Research terminal-result commit existed on current `main` at review start; fresh Actions state is authoritative and outranks stale recovery navigation.

## PREREG_CHECK

PASS.

The preregistration was prospectively frozen before implementation and workflow launch. Source-lock explicitly verifies ancestry of both preregistration `aca376c7...` and implementation `4f73b782...`, and checks the frozen PASS / PRECISION_BLOCKED / INVALID_IMPLEMENTATION branches and operator-digest marker.

Frozen scientific/method contract includes exact P1 object `alpha=0.55`, `k=5`, P1 exponents `(1,1,1,1,2,2,2,2,2,2)`, four fixed laminar forests, scalar Taylor orders `(2,7,15)`, LOW `dps=1100`, HIGH `dps=1500`, fixed step scales `2^-100` and `2^-140`, raw parent lock tolerance `1e-65`, precision/refinement controls, negative controls, and a method-only interpretation ceiling.

The frozen INVALID branch explicitly includes a wrong P1 object.

## OBJECT_IDENTITY_CHECK

FAIL — implementation uses the wrong numerical realization of the frozen `alpha=0.55` object.

The implementation defines at module import time:

`ALPHA = mp.mpf("0.55")`

before `main()` raises `mp.mp.dps` to 1100 or 1500. Under mpmath default initialization this stores approximately

`0.5500000000000000444089209850062616169452667236328125`

rather than parsing decimal `0.55` at the active high precision. Later precision increases do not recover the lost bits.

This exact defect was identified prospectively in the preterminal Critic audit before LOW/HIGH outputs were consumed.

## SOURCE/REALIZATION_CHECK

FAIL only for the alpha realization; other inspected frozen realization fields are consistent.

The implementation uses the frozen P1 exponent pattern, `k=5`, the four preregistered forest boxes, scalar orders `(2,7,15)`, barycentric collapse realization, nonlaminar negative control, historical-order-9 rejection, exact polynomial fixtures, tensor reduction replay, and the expected operator digest marker.

The operator-digest control remains weaker than ideal because it checks for the expected digest string in the historical terminal result rather than cryptographically recomputing/binding the currently imported operator source. No concrete operator-source mismatch was found in this review, so that point is a hardening qualification rather than an independent invalidity.

## PROVENANCE_CHECK

PASS.

Run `35002079183` is terminal. All four jobs completed successfully and all three artifacts are present with recorded digests. The aggregate job downloaded the exact LOW/HIGH artifacts by ID/digest, pinned `mpmath==1.3.0`, and emitted the terminal aggregate artifact.

Green workflow status is not interpreted as scientific/method PASS: the aggregate scientific/method classification is `INVALID_IMPLEMENTATION`.

Current recovery/front navigation is stale relative to the terminal Actions state and must not be used to overwrite this terminal classification.

## SAME_REALIZATION_CHECK

FAIL.

The validated parent numerical kernel parses `"0.55"` only after working precision is set. The mixed-Taylor implementation instead reuses a prematurely rounded module-level `ALPHA` in both the parent raw lock and every actual-Gaussian forest evaluation.

The frozen parent-raw control independently detects the realization mismatch. Both LOW and HIGH report the identical normalized raw-lock error

`2.722451999499224874738459741907942144132691567392430481003687026923784910146776298687742615255977491e-20`,

far above the frozen `1e-65` tolerance. Because the error is precision-independent across 1100 and 1500 digits, increasing working precision cannot repair the already-rounded object.

## NUMERICAL/STATISTICAL_CHECK

The terminal invalidity is confirmed; this is not a precision blocker.

Both lanes self-classify `INVALID_IMPLEMENTATION` only because `historical_parent_raw_lock=false`; all other recorded lane controls pass. In particular:

- all forest-structure controls pass;
- exact polynomial fixtures pass;
- nonlaminar rejection passes;
- historical order-9 rejection passes;
- tensor-order/direct-sum replay passes;
- all actual values are finite;
- measured cancellation margin is at least 180 decimal digits;
- the degree-`r+1` adversarial step-sensitivity control passes.

The aggregate reports:

- `invalid_controls_pass=false`;
- `lane_precision_controls_pass=true`;
- LOW and HIGH lane classifications both `INVALID_IMPLEMENTATION`;
- same-step precision replay errors are exactly `0.0` for all four forests;
- HIGH refinement errors are about `4.17e-37` for the multi-axis cases and `2.47e-53` for `SINGLE15`, all well inside the frozen `1e-18` threshold.

Therefore the method is not BLOCKED by precision/refinement; it is invalid because the object/source control fails.

## COUNTEREXAMPLE_ATTEMPTS

1. **Wrong P1 object / alpha realization.** Confirmed. Import-time `mp.mpf("0.55")` produces the wrong high-precision object and the raw-parent lock fails by roughly 45 decimal orders relative to tolerance.
2. **Could higher working precision rescue the object?** Refuted: LOW and HIGH produce the same raw-lock error, proving the discrepancy is fixed before precision is raised.
3. **Wrong forest/order boxes.** Not found; frozen boxes and orders match preregistration.
4. **Precision/refinement failure promoted to scientific FAIL.** Rejected: precision controls pass; invalidity is object identity.
5. **Green CI promoted to science.** Rejected: workflow success only establishes execution provenance; aggregate classification is INVALID_IMPLEMENTATION.
6. **Finite method pilot promoted to forest-subtracted science.** Rejected by the frozen interpretation ceiling.
7. **P3 imported into this P1 gate.** No historical P3 use was found in the production classifier.
8. **Operator marker promoted to cryptographic source lock.** Hardening issue remains, but no actual source mismatch was established.

## OVERCLAIM_CHECK

No PASS authority exists for `P1_MIXED_TAYLOR_GRID_METHOD_CONFIRMED_SCOPED` from this run.

Accordingly this run does not authorize the separately frozen 29-orbit P1 production diagnostic. It also says nothing about forest-subtracted stabilization/divergence, Eq. (4) existence/nonexistence, physical model/family failure, D7 closure, terminal selectors, or Candidate Gravity.

The invalid result is methodological/implementation-only and must not be promoted to scientific FAIL.

## VERDICT

`INVALID_IMPLEMENTATION`

The terminal Actions classification is independently confirmed. The decisive defect is wrong-object realization of frozen decimal `alpha=0.55` through premature import-time mpmath conversion. The preregistered raw-parent control correctly detects the defect in both LOW and HIGH lanes.

## QUALIFICATIONS

1. Historical run `35002079183` remains immutable terminal provenance with aggregate classification `INVALID_IMPLEMENTATION`.
2. All observed precision/refinement/method controls besides the raw object lock passed; this does not convert the invalid run into a method PASS.
3. Repairing `ALPHA` to remain a string/exact decimal until after `mp.mp.dps` is set preserves the frozen scientific contract and is an implementation repair, not a new scientific hypothesis.
4. A new prospective scientific gate is required only if alpha, forests, orders, steps, tolerances, classifier, dependency, object, or interpretation ceiling are changed.
5. The 29-orbit production diagnostic remains unauthorized until a repaired mixed-Taylor run terminally passes the same frozen gate.
6. Iter504 run `34907349374` and Iter461 run `34748503239` were freshly rechecked and remain `queued / conclusion=null`; no partial substantive values were consumed.
7. `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; terminal selectors remain forbidden; Candidate Gravity remains inactive.

## UPDATED_STATE

- `SOURCE_J1_K5_P1_MIXED_TAYLOR_GRID_METHOD_PILOT = INVALID_IMPLEMENTATION` for run `35002079183`.
- exact failure: frozen `alpha=0.55` object is instantiated before high precision and fails the parent raw lock.
- LOW/HIGH precision agreement and HIGH step refinement are numerically stable but non-authoritative for PASS because object identity fails first.
- no method PASS; no 29-orbit production authorization.
- recovery/front navigation on current main is stale relative to terminal Actions and should be reconciled by the next Research/recovery update.
- governance unchanged.

## NEXT_ADMISSIBLE_GATE

Perform an implementation-only repair under the same prospectively frozen gate:

- keep `ALPHA` as the literal string `"0.55"` or construct `mp.mpf("0.55")` only after setting the lane precision;
- rerun the frozen parent raw lock and require normalized error `<=1e-65` in both LOW and HIGH;
- preserve all frozen P1 exponents, forest boxes, scalar orders, step scales, tolerances, mpmath version, classifier and interpretation ceiling;
- rerun LOW/HIGH/aggregate and record new artifacts/digests;
- do not rewrite or relabel historical run `35002079183`.

Only a terminal PASS from a repaired run of this same frozen contract can authorize the separately prospectively frozen 29-orbit P1 proper-forest production diagnostic.
