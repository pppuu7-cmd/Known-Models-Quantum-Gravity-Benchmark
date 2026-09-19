# Iter504V Phase-B source aggregate binding adversarial gate — prospective preregistration

Date: 2026-09-19
Status: **FROZEN_BEFORE_IMPLEMENTATION_AND_EXECUTION**

## Gate

`ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_ADVERSARIAL_GATE`

This is a bounded verifier/authority-path closure gate only. It consumes no production Phase-B scientific payload and does not classify source run `35405065903`.

## HYPOTHESIS

The exact immutable Phase-B source aggregate `code/iter504v_phase_b_aggregate.py` at source launch head `31fcdacffcc394e96b73917083281edb90d6753c` may accept one or more structurally/provenance-invalid synthetic assembly pairs as nominal complete-q1 PASS because it validates agreement/counts without independently rebinding all frozen semantic relations.

The gate tests exactly three outcome-independent candidates:

A. **classification-to-unresolved semantic binding** — both assembly lanes claim `ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED` while the same assemblies contain one unresolved state, `total_unresolved_leaves=1`, and the matching counterexample state;

B. **canonical decision-projection key binding** — both lanes retain the exact canonical `state_ids` list and unchanged projection-sequence scalar but replace one canonical key in `decision_projection_sha256_by_state` by a foreign noncanonical key while preserving cardinality 768 and exact cross-environment equality;

C. **case-provenance key binding** — both lanes replace one canonical key in `case_file_sha256` by a foreign noncanonical key while preserving cardinality 768 and exact cross-environment equality.

Each candidate is invalid under the frozen Phase-B source contract. Acceptance by the exact source aggregate is a verifier-binding defect, not a statement that the active producer emitted such an object.

## exact OBJECT

Only synthetic assembly JSON objects presented to the exact source aggregate blob from the immutable Phase-B source launch.

Bound source object:

- source run: `35405065903` (nonterminal at preregistration; payload forbidden);
- source launch head: `31fcdacffcc394e96b73917083281edb90d6753c`;
- source aggregate path: `code/iter504v_phase_b_aggregate.py`;
- expected aggregate blob: `ae1932a7cdd98a1cc74f1b2f07bc295e0c097274`;
- Phase-B design preregistration: `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
- Phase-B execution authority: `caf67585a9fad990dd90948df51839e6ed7cf891`.

No source case, leaf, slope, drift, certification, assembly or aggregate payload is part of this gate object.

## DEPENDENCY

Depends only on the frozen Phase-B taxonomy and the immutable aggregate implementation. It does not depend on any active source outcome.

## SOURCE / REALIZATION AUTHORITY

Use exactly the repository aggregate implementation above. The gate must call that file as an external subprocess. Reimplementation of its decision logic inside the test harness is not source authority.

## FROZEN INPUTS

Synthetic assembly baseline must bind exactly:

- gate `ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE`;
- preregistration `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
- design authority `a4006f336a49f655534a2f76a443a3d60a47cd85`;
- design static Critic `722c7e09bf077c0cb29c3ac0ac2ed724b99290f4`;
- implementation authority `42a2f035a80c474ebc7e5f57934ad9ba78ce9937`;
- canonical 768-record sequence SHA256 `3cac282175830e795394dca5202f5368b27120817f2d4abd9eba54fc6c9f1e6f`;
- exact canonical 768 state IDs in causal/block/path/box order;
- threshold `1/20`, robust floor `1`, `MAX_DEPTH=3`, channels `243`, R `[6,8,10,12]`, rho `[0.35,0.9,1.6,2.7]`.

Synthetic hash values are deterministic SHA256 strings generated from state identity and are not physical data.

## POSITIVE CONTROLS

1. Coherent zero-unresolved pair with PASS classification must be accepted as PASS by the exact aggregate.
2. Coherent one-unresolved pair with INCONCLUSIVE classification, matching unresolved map/total/counterexample set, must be accepted as INCONCLUSIVE.

## NEGATIVE CONTROLS

The exact aggregate must reject as `ITER504V_BROADER_DOMAIN_INVALID`:

1. cross-environment classification disagreement;
2. cross-environment canonical `state_ids` disagreement;
3. cross-environment decision-projection map disagreement.

These controls establish that the aggregate is live and not universally accepting.

## Independent oracles

Before interpreting aggregate output, the harness independently checks:

- taxonomy oracle: PASS iff total unresolved is zero; INCONCLUSIVE iff total unresolved is positive and counterexample/unresolved maps agree;
- canonical projection-key oracle: keys of `decision_projection_sha256_by_state` equal exactly the canonical state set;
- canonical provenance-key oracle: keys of `case_file_sha256` equal exactly the canonical state set.

The oracles do not reuse the source aggregate implementation.

## PASS

`ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_DEFECTS_VERIFIED_SCOPED`

iff both positive controls are accepted correctly, all three negative controls are rejected, all three independent candidate oracles identify their candidate as invalid, and the exact source aggregate nevertheless accepts candidates A, B and C without source-invalid classification.

## FAIL

`ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_DEFECTS_NOT_REPRODUCED_SCOPED`

iff the harness/controls are valid but at least one preregistered candidate is correctly rejected by the exact aggregate, so the exact three-defect hypothesis is not fully reproduced.

This is methodology FAIL only, never scientific/physics FAIL.

## BLOCKED

`ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_GATE_BLOCKED_SCOPED`

iff the exact frozen aggregate object cannot be source-locked or executed for reasons independent of candidate outcome.

## INVALID

`INVALID_IMPLEMENTATION`

iff preregistration/source identity is violated, the harness/oracles are internally inconsistent, a positive control fails, a required negative sensitivity control fails to reject, environments disagree on canonical result, production science is consumed, or frozen criteria are changed after execution.

## Execution

Run independently under Python 3.11 and 3.13 with `fail-fast:false`. Require byte-identical canonical `result.json` across environments before terminal interpretation.

The workflow must source-lock this preregistration, gate implementation, workflow, execution authority, exact source aggregate blob, and must not download any artifact from source run `35405065903`.

## INTERPRETATION CEILING

Any PASS means only that the exact Phase-B source aggregate has the three preregistered verifier/authority-path binding omissions on synthetic assembly inputs. It does not show that active source run `35405065903` emitted invalid assemblies and does not classify that run. It does not alter the frozen Phase-B PASS/INCONCLUSIVE/INVALID taxonomy.

No all-domain beyond q=1, model-family, D7, Candidate Gravity, Paper IV or global quantum-gravity conclusion follows.
