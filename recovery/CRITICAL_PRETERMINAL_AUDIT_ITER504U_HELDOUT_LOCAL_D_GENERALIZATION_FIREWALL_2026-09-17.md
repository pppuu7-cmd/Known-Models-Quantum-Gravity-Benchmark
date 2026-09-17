# KMQGB Critical Preterminal Audit — Iter504U held-out local-D generalization firewall

Date: 2026-09-17
Lane: independent KMQGB Critical Review / Verification
Status: PRETERMINAL / NO SCIENTIFIC VERDICT
Review-start main: `1ba205138e92851e48702248e5151f112bcd2f63`

## RESULT_REVIEWED

No terminal Iter504U scientific result exists at this review point.

Authoritative scientific workflow:

- gate: `ITER504U_HELDOUT_LOCAL_D_GENERALIZATION_FIREWALL`;
- launch head: `102c7f9cafec956f3bc7bed4384ae755c98f761a`;
- Actions run: `35246605860`;
- fresh state at review: `in_progress / conclusion=null`;
- source-lock job `105288277610`: terminal `success`;
- all twelve case jobs were still `in_progress` at the fresh check.

No partial case artifact, held-out slope/drift value, leaf-certification value, assembly value, aggregate value or Critic outcome was consumed in this audit.

The latest prior independently closed authority remains the Iter504T decision-canonicalization repair, run `35245037403`, terminal `completed/success`, independently `CONFIRMED_SCOPED` by commit `8624532254981fbea6f8fcfac09cd538e2066aa4`.

## PREREG_CHECK

PASS for chronology.

Prospective sequence is clean:

- Iter504U preregistration `05b8e9354c9a7805f0fce18b904346a986a0787f`;
- evaluator `8053039c48f5fc876180c10d4ca0769182b3c871`;
- assembler `beca5c425f7adcf9f381885034df35991b747c84`;
- aggregate `f5f3ef40c17d685c50771143058c461f2ad77e27`;
- adversarial Critic `396dd6fdadf261a0ca33e3b4415fd79626d500b4`;
- methodology CI / pre-execution audit;
- frozen execution authority `7b446398c97dc849f6f4ecbcd493058d9889d0cf`;
- prepared workflow `65246c144675d656ab434b306816fd99459f753d`;
- one launch marker `102c7f9cafec956f3bc7bed4384ae755c98f761a`.

The later successor-policy commit `1ba205138e92851e48702248e5151f112bcd2f63` was frozen while the scientific run was still non-terminal and does not alter the launch-head scientific contract.

## FROZEN CONTRACT CHECK

The preregistration freezes, among other fields:

- exact six-case held-out cohort;
- no development boxes 13–15;
- precision 384 bits;
- all 243 channels, no pruning;
- R `[6,8,10,12]` and rho `[0.35,0.9,1.6,2.7]`;
- exact threshold `1/20`, floor `1`, `MAX_DEPTH=3`;
- deterministic rational dyadic midpoint subdivision;
- direct local-D recomputation on every visited node;
- exact-Arb decision booleans;
- C4 `leaf.certified = all(per_rho.certified)`;
- PASS only with zero unresolved leaves across all six valid cases;
- valid unresolved terminal leaves at frozen depth 3 -> INCONCLUSIVE;
- implementation/provenance/cohort/decision defects -> INVALID;
- no scientific FAIL label.

Critically, the case-evaluator contract requires: if a node is not certified, bisect it exactly until `MAX_DEPTH=3`; only at depth 3 may an unresolved valid leaf be preserved unresolved.

## OBJECT_IDENTITY_CHECK

Static PASS_SCOPED for the launch-head producer object.

The frozen producer source itself implements the intended recursion correctly:

`if row['certified'] or d == MAX_DEPTH: leaves.append(row) else: split at exact midpoint`.

It therefore does not intentionally terminate an uncertified node at depth 0, 1 or 2.

A separate verification-binding defect candidate exists downstream, described below. It is a validator/authority-path issue, not evidence that the currently running producer has emitted such a leaf.

## SOURCE / REALIZATION CHECK

Static PASS_SCOPED.

The workflow source-lock pins the preregistration, evaluator, assembler, aggregate, Critic and workflow blobs and verifies the Iter499/500/501/503/504 base source files byte-identical to exact repair head `10ae6bcc8447d14cecc6e550065504b23f792953`.

The fresh source-lock job completed successfully. No source/version mismatch was found in the bounded audit.

## PROVENANCE_CHECK

PRETERMINAL PASS only.

The authoritative run is non-terminal, so terminal artifacts/digests do not yet exist as a complete scientific authority chain. Only source-lock chronology/status was consumed.

The prior independently closed Iter504T authority run `35245037403` was freshly confirmed terminal `completed/success`; its four Actions artifact digests remain present and unexpired.

## SAME_REALIZATION_CHECK

Static PASS_SCOPED.

The launch workflow pins the no-refit base realization and the six prospectively frozen held-out identities. No development case substitution is visible in source.

## NUMERICAL / STATISTICAL CHECK

Not performed on active scientific outputs because the workflow is non-terminal.

No partial substantive values were consumed.

## COUNTEREXAMPLE_ATTEMPTS

### C1 — premature unresolved terminal leaf accepted as valid INCONCLUSIVE: SUCCESS

Frozen algorithm rule:

- certify a node -> it may terminate at any depth;
- uncertified node with depth `< 3` -> it must be bisected;
- only an uncertified node at depth `3` may remain as an unresolved terminal leaf.

The environment assembler and independent Critic do **not** enforce this implication. Their leaf validation checks:

- depth is in `[0,3]`;
- the leaf is an exact dyadic cell of that depth;
- cover is complete;
- per-rho boolean binding is coherent;
- top-level leaf C4 binding is coherent;
- local-D / exact-decision tags and cohort fields are present.

But neither validator rejects `leaf.certified == false` at depth `0`, `1` or `2`.

Explicit outcome-independent mutation fixture:

1. Start from a structurally valid case object.
2. Replace its terminal tree by the single exact parent-box cell at `depth=0`.
3. Give the leaf four internally coherent per-rho rows with at least one `rho.certified=false`, hence `leaf.certified=false` by the frozen C4 relation.
4. Set `terminal_leaf_count=1`, `unresolved_leaf_count=1`, `visited_node_count=1`, full exact parent cover, empty parent-inclusion records, and retain all frozen cohort/constants/tags.
5. Apply the same mutation in both Python environments.

Current `validate_case()` accepts the depth-0 unresolved leaf because `dyadic_cell_valid()` allows any depth `0..3`, the cover is exact, and no rule requires `depth == MAX_DEPTH` when `certified == false`.

The assembler therefore maps the case to a valid environment payload and, with any unresolved count, to `ITER504U_HELDOUT_LOCAL_D_INCONCLUSIVE_SCOPED`. The independent Critic repeats the same omission, and cross-environment agreement can remain exact.

Thus the current authority path can accept **premature stopping** of an uncertified held-out case as scientific INCONCLUSIVE instead of classifying the execution implementation-invalid.

This counterexample is independent of all active held-out outcomes. It does not assert that the immutable producer code actually emitted a shallow unresolved leaf; source inspection shows the producer recursion itself is correct.

### Other attempted defects

- development-case insertion: statically rejected;
- wrong R/rho cohort: statically rejected;
- threshold/floor/depth/channel-count changes: statically rejected;
- C4 true-leaf/false-rho inconsistency: statically rejected;
- non-dyadic leaf identity: statically rejected;
- root/development derivative-reuse flag: statically rejected;
- float decision-transport tag: statically rejected.

No active-run outcome was used in any attempt.

## OVERCLAIM_CHECK

PASS.

No Iter504U PASS/INCONCLUSIVE/INVALID scientific result is issued here. No all-1888, D7, model/family, selector, Candidate Gravity, Paper IV or global quantum-gravity claim follows.

`INCONCLUSIVE != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; green source-lock CI is provenance, not science.

## VERDICT

None while run `35246605860` is non-terminal.

Prepared terminal-review defect candidate: **premature unresolved leaf depth binding is missing from assembler/Critic validation**.

If the launch-head implementation remains unchanged and the terminal authority chain relies on these validators, this candidate must be adjudicated before accepting any terminal Iter504U classification as fully contract-valid.

## QUALIFICATIONS

1. The immutable producer recursion itself appears correct and splits uncertified nodes until depth 3.
2. The defect candidate concerns independent validation/authority binding, not an observed active producer error.
3. No partial scientific value or artifact was inspected.
4. Parent-child derivative inclusion remains diagnostic-only under the pre-execution methodology; this audit does not promote inclusion=true to a new scientific requirement.

## UPDATED_STATE

- Iter504U scientific run `35246605860` = ACTIVE / NON-TERMINAL.
- No scientific Critic verdict exists for Iter504U in this audit.
- One outcome-independent terminal-review counterexample is durably frozen: shallow unresolved leaf accepted as valid INCONCLUSIVE.
- Latest prior independently closed Iter504T authority remains unchanged.
- RQIR Core v1.0 remains FROZEN; D7 required subgates remain unclosed; terminal selectors remain forbidden; Candidate Gravity inactive.

## NEXT_ADMISSIBLE_GATE

Only terminal review of this same Iter504U run once all case jobs, both assemblies, aggregate, Critic and artifact digests are terminal.

At terminal review, before accepting PASS/INCONCLUSIVE/INVALID authority, explicitly test the launch-head assembler/Critic against the frozen recursion implication:

`not leaf.certified  =>  leaf.depth == MAX_DEPTH`.

A same-contract implementation repair may add this exact validator rule and an adversarial shallow-unresolved-leaf fixture without changing any scientific object, case cohort, threshold, floor, depth, R/rho grid, channel count, partition rule or interpretation ceiling. Changing any of those scientific fields requires a new prospectively frozen gate.