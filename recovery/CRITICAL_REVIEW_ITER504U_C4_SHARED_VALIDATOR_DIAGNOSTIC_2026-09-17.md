# Independent Critical Review — ITER504U C4 shared-validator diagnostic

Date: 2026-09-17
Lane: independent KMQGB Critical Review / Verification
Verdict: `CONFIRMED_SCOPED`

## Scope

This review covers exactly the bounded methodology object `ITER504U_C4_SHARED_VALIDATOR_DIAGNOSTIC`, authoritative Actions run `35252175158`, launch head `c0f45fb93a2298221fb0c60a2b2ee770a8bb8dc2`.

It does **not** consume or classify any substantive payload from the still-nonterminal Iter504U held-out science run `35246605860`. It does not create a competing scientific verdict.

## Recovered authority / chronology

Prospective diagnostic preregistration:

- commit `dd8ea4c0f6df3f0da6139e293d6b8fd5bea5d02a`;
- file `research/prereg/ITER504U_C4_SHARED_VALIDATOR_DIAGNOSTIC_2026-09-17.md`;
- status frozen before diagnostic replay.

Frozen diagnostic authority:

- authority commit `79e4a6a1e6ee100812f6247219fa79501c3720f3`;
- workflow commit `7cd6c8110077362d227b5ebf869887d44d473c97`;
- workflow blob `9675aa8176971cf13c03a6748a641eed2abece4f`;
- evaluator commit `151c4ea951c04278811e4c557847e01b32bbb97c`;
- evaluator blob `20a854869dbd0a61824b6c7e8a4f829507f5b126`;
- original Critic blob `c2a7ea31ddc151bf02a3995d761cae95bdabd0db`;
- repair-wrapper blob `bcea2946a0f9676b50897dc4bbe74fa1122a9965`;
- Python lanes `3.11` and `3.13`;
- science access forbidden.

The source-lock job binds these exact identities before replay. The diagnostic workflow only executes the frozen synthetic evaluator, preserves return code `0` or `2`, uploads the JSON in either case, and requires byte-identical JSON plus equal return code across the two Python environments.

## Terminal execution / provenance

Run `35252175158` is terminal `completed/success` at launch head `c0f45fb93a2298221fb0c60a2b2ee770a8bb8dc2`.

Fresh Actions artifacts:

- Python 3.11 artifact id `10510475771`, Actions digest `sha256:583c1935ee815b7d4ba80e0396212d725933f6eabe4ac1f8fb4279f3a16ad0a1`;
- Python 3.13 artifact id `10510765344`, Actions digest `sha256:f768f75cdc9794d70c4b5cced1ee8692c2fb8e38873094251baed9694c907cea`;
- aggregate artifact id `10509679536`, Actions digest `sha256:9df7eed7be9e89c0083d2cb6b0631f3d190b12085253b5786e8808ba70883880`.

Independent download and SHA256 recomputation matched all three current Actions digests exactly. The two lane `result.json` payloads are byte-identical; their SHA256, and the aggregate copy's SHA256, are all:

`fbc96994dd7ccc53325e415133993f056e08af45401567aa79670225c12e49de`.

Both evaluator return codes are `0`.

No provenance basis exists for `INVALID_PROVENANCE`.

## Frozen-contract review

### HYPOTHESIS / OBJECT

The diagnostic object is visibility/localization only: replay the already-frozen synthetic evaluator without altering evaluator, validator, fixture constructor, criteria or classification and without reading held-out science. That object was respected.

### DEPENDENCY / SOURCE / REALIZATION

The exact diagnostic workflow source-lock checks the frozen evaluator, original Critic, repair-wrapper and workflow blobs. Run `35252175158` executed that frozen object. No production/held-out artifact is downloaded by the diagnostic workflow.

Important scope boundary: the formal C4 repair preregistration `662e1b40c4584a5b1989b821cd7a5c334ef8fc44` gives its own source/realization authority to a different methodology workflow/head. The present diagnostic preregistration explicitly says this replay **cannot by itself convert the parent formal repair run to PASS**. Therefore the evaluator-emitted string `ITER504U_CRITIC_C4_FIXTURE_REPAIR_VALIDATED_SCOPED` is evidence about the frozen evaluator's deterministic output under this diagnostic; it is not promoted here into independent terminal authority for the distinct formal repair gate.

### CONTROLS / COUNTEREXAMPLE-FIRST CHECK

The recovered evaluator output is deterministic across Python 3.11/3.13 and reports:

- coherent non-contradictory synthetic baseline accepted;
- deterministic repaired C4 contradiction rejected by the shared Critic path;
- rejection hits exactly `H0_AMP_LOW:C4_leaf_binding`;
- the outcome-independent false-carrier variant, after the repair constructor is applied, is rejected by that same exact C4 binding;
- the repaired negative-control suite reports rejection of wrong case identity, development-box insertion, missing case, changed threshold/floor/depth/channel count, wrong R/rho cohort, derivative reuse, float-decision transport, non-dyadic partition, C4 contradiction and removed binding tag;
- `production_science_consumed=false` and `source_run_classified=false`.

This independently confirms the narrow proposition the diagnostic was allowed to test: the corrected synthetic constructor actually reaches the shared Critic's C4 leaf/per-rho binding check and is not a disconnected assertion.

## Surviving qualification: shallow unresolved leaves remain a separate open validator defect

The scientific Iter504U preregistration requires an uncertified node to bisect until `MAX_DEPTH=3`; only at depth 3 may an unresolved leaf remain terminal. The current shared Critic's `dyadic_cell_valid()` accepts terminal dyadic cells at any depth `0..3`, and `validate_case()` contains no implication `not leaf.certified => leaf.depth == MAX_DEPTH`.

The diagnostic's synthetic carrier starts from a depth-0 leaf and is deliberately a methodology carrier, not a production-science realization. Its use does not invalidate this bounded diagnostic because the diagnostic/formal fixture-repair object is expressly synthetic and science-independent. But it also **cannot** be used to claim that the full Iter504U validator contract is closed. The previously prepared shallow-unresolved counterexample remains open for eventual science-authority review.

## Overclaim check

PASS for this review only under the diagnostic claim ceiling. No held-out scientific value was consumed; no Iter504U PASS/INCONCLUSIVE result is issued; no all-Iter504, 1888-state, D7, model/family, selector, Candidate Gravity, Paper IV or global quantum-gravity conclusion follows.

`RQIR Core v1.0` remains FROZEN. `BLOCKED != FAIL`; `INCONCLUSIVE != FAIL`; finite certificate != universal theorem; scoped child result != family closure.

## Handoff

- `RESULT_REVIEWED = ITER504U_C4_SHARED_VALIDATOR_DIAGNOSTIC / run 35252175158`
- `PREREG_CHECK = PASS`
- `OBJECT_IDENTITY_CHECK = PASS_SCOPED` — exact synthetic diagnostic object only
- `SOURCE/REALIZATION_CHECK = PASS_SCOPED` — diagnostic authority only; formal repair-gate realization is not promoted
- `PROVENANCE_CHECK = PASS`
- `SAME_REALIZATION_CHECK = PASS_SCOPED` — lane JSON byte-identical, same frozen blobs and return code
- `NUMERICAL/STATISTICAL_CHECK = PASS_EXACT_NONSTATISTICAL` — no held-out numerical science consumed
- `COUNTEREXAMPLE_ATTEMPTS = corrected C4 contradiction rejected exactly; coherent baseline accepted; wrong-R and other frozen synthetic mutations rejected; shallow-unresolved science-validator counterexample remains OPEN and outside this diagnostic closure`
- `OVERCLAIM_CHECK = PASS_SCOPED`
- `VERDICT = CONFIRMED_SCOPED`
- `QUALIFICATIONS = confirms deterministic diagnostic visibility and real shared-validator C4 rejection only; does not independently terminalize the distinct formal repair gate; does not validate the full Iter504U science validator; source science run remains nonterminal`
- `UPDATED_STATE = diagnostic execution independently confirmed; formal/science authority unchanged; shallow-unresolved validator-binding defect remains open`
- `NEXT_ADMISSIBLE_GATE = while source run 35246605860 is nonterminal, only outcome-independent contract/code audit; after terminalization, review immutable terminal artifacts and require exact enforcement of not leaf.certified => leaf.depth == MAX_DEPTH before accepting full validator authority. A same-contract validator repair may add that implication plus an adversarial shallow-unresolved fixture without changing science criteria.`
