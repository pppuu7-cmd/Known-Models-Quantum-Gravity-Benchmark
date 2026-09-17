# ITER504U_CRITIC_C4_FIXTURE_REPAIR_GATE — terminal record

Date: 2026-09-17
Formal preregistration: `662e1b40c4584a5b1989b821cd7a5c334ef8fc44`
Authoritative methodology run: `35250717944`
Workflow head: `9793843843b53c1616af6fbfc72f7a8fa56a28ef`
Terminal workflow state: `completed/success`

## Terminal classification

`INVALID_IMPLEMENTATION`

This is **not** a scientific failure and does not classify held-out source run `35246605860`.

## Why green CI is not formal PASS

The formal preregistration prospectively required the C4 repair self-test to exercise the **same shared Critic validation path** used for production structure validation, and declared bypass of that shared validation path to be `INVALID_IMPLEMENTATION`.

The authoritative workflow logs show that step `Syntax and isolated outcome-independent C4 fixture self-test` executed:

`python code/iter504u_heldout_critic_c4_fixture_repair.py --self-test`

followed by static `grep` checks.

That self-test checks local Boolean relations inside a synthetic carrier, but it does not call `iter504u_heldout_critic.validate_all` or `validate_case`. It therefore does not establish the formal gate's required positive control that the intentionally contradictory fixture is rejected by the shared Critic validator, nor the complementary negative control that a coherent non-contradictory full structural fixture is accepted by that same validator.

The workflow's successful exit status proves the local assertions and frozen blob checks passed. It does not satisfy the stronger formal decision contract frozen while the run was nonterminal.

## What remains valid

The following facts remain valid methodology evidence:

- producer evaluator blob remained `bf457eef08f7df32523c9e22ce3b3713f10d97a0`;
- assembler blob remained `5c3b04f25c5fb2523c3788b725ccf84ca23a07f1`;
- aggregate classifier blob remained `23165f9d99ff9a2f90c27a51cb889d5920327f92`;
- original Critic blob remained `c2a7ea31ddc151bf02a3995d761cae95bdabd0db`;
- isolated wrapper blob remained `bcea2946a0f9676b50897dc4bbe74fa1122a9965`;
- the wrapper's local outcome-independent carrier self-test passed;
- no held-out scientific value was required to identify this defect.

## Minimal defect localization

The remaining defect is narrow: **formal validation-path coverage**, not synthetic-constructor logic and not production science.

A minimal successor may construct a completely synthetic six-case structurally valid Iter504U payload, verify that `base.validate_all` accepts it, apply the already-frozen `force_c4_contradiction`, and verify that the same `base.validate_all` rejects it for exactly `H0_AMP_LOW:C4_leaf_binding`, including a carrier whose initial leaf/rho state is false.

No source-run science payload is needed or authorized for that successor methodology test.

## Claim ceiling

`INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`.

This record does not modify or classify source run `35246605860`, does not alter its cohort or criteria, and authorizes no all-Iter504, D7, model/family, selector, Candidate Gravity, Paper IV or global quantum-gravity conclusion.
