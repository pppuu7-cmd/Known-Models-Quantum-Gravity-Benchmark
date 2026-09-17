# ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_GATE — prospective freeze

Date: 2026-09-17
Status: PROSPECTIVELY_FROZEN_BEFORE_TERMINAL_SUBSTANTIVE_ARTIFACT_CONSUMPTION

## HYPOTHESIS

The completed same-science execution of `ITER504T_IMPLEMENTATION_CONTROL_REPAIR_RERUN_GATE`, Actions run `35205054496`, may or may not be recoverable as exact-run scientific authority despite the independently confirmed C4 validator-path defect. A green workflow or launch-head repair-verdict is insufficient. This gate asks whether one prospectively frozen independent terminal review can bind the actual terminal data back to the original frozen scientific predicate, including the missing leaf-to-rho conjunction, without changing the scientific object or recomputing new physics.

## exact OBJECT

Exactly one terminal authority/admissibility review of the already-completed Actions run `35205054496` at immutable launch head `10ae6bcc8447d14cecc6e550065504b23f792953`.

The review consumes only terminal artifacts from that execution after this preregistration is committed. It independently checks:

1. terminal execution/provenance and exact artifact identities;
2. original unchanged Iter504T science/numerics and the C1/C3 repair contract;
3. launch-head aggregate, independent-Critic and repair-verdict outputs;
4. every terminal leaf represented in both terminal assembly artifacts, recomputing `rho_certified := slope_floor_satisfied AND drift_within_tolerance` and `leaf_certified_recomputed := all(rho_certified for rho in leaf.per_rho)` independently of serialized top-level `leaf.certified`;
5. equality of serialized `leaf.certified` and independently recomputed leaf certification for every terminal leaf;
6. recomputation of unresolved-leaf counts and the terminal three-root scientific class from the independently bound leaf predicate, rather than trusting serialized `unresolved_leaf_count` alone;
7. cross-environment identity/agreement for the reviewed scientific decision.

This is an exact-run terminal review, not a repair of the general launch-head validator. Terminal C4 remains historically true even if all actual terminal leaves happen to satisfy the missing conjunction.

## DEPENDENCY

- original Iter504T scientific preregistration commit `aa2b0256ce60d605574a18ec86c0bad5b5df1512`;
- implementation-control repair preregistration commit `adc7bfb9df77a90455cac1b0f0cb7255d80c44d5`;
- repair authority commit `a47a9140cf10f2f0f912943133a01238ff1b5653`;
- immutable repair launch head `10ae6bcc8447d14cecc6e550065504b23f792953`;
- terminal repair Actions run `35205054496`, `completed/success`;
- terminal C4 closure preregistration `aa421bd0b1aec1cbcc7a381fb00e947798d1b084` and authority `9aa9f77093bd34e058641bb141c8f95a4794d841`;
- terminal C4 classification `ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED`;
- independent C4 Critical Review on current repository state: `CONFIRMED_SCOPED`;
- reconciled starting main `76a306f78052c5227b2b3c136b09d50aa4697b2f`.

## SOURCE/REALIZATION AUTHORITY

Only the prospectively committed ledger `inputs/iter504t_repair_rerun_terminal_authority_review_authority.json`, the immutable repository objects it locks, and terminal GitHub Actions artifacts of run `35205054496` are authoritative.

No web source, partial/nonterminal value, synthetic replacement for production data, changed threshold, changed scientific classifier, guessed missing field, or data from another run may enter the terminal decision.

C4 is applied as already-terminal authority: the launch-head validators themselves do not prove the leaf-to-rho conjunction. Therefore this review may restore authority for this exact completed run only if it independently recomputes and verifies that conjunction on the actual terminal data and recomputes the scientific decision from the bound predicate.

## FROZEN INPUTS

Scientific/numerical identity remains exactly the original Iter504T contract:

- roots `[13,14,15]`;
- rhos `[0.35,0.9,1.6,2.7]`;
- exact R cohort `[6,8,10,12]`;
- all 243 channels;
- Arb/Acb precision 384 bits;
- exact threshold `1/20`;
- exact robust slope floor `1`;
- deterministic rational dyadic subdivision;
- `MAX_DEPTH=3`;
- direct local derivative recomputation on visited intervals;
- original PASS / INCONCLUSIVE / INVALID scientific labels and claim ceiling.

Repair-contract identity remains C1/C3 only as prospectively frozen by the repair gate. C2 remains REFUTED. C4 is a separately terminally confirmed decision-binding defect and must not be erased.

Required terminal artifacts, all conjunctive for an unblocked review:

- `iter504t-repair-assembled-3.11`;
- `iter504t-repair-assembled-3.13`;
- `iter504t-repair-aggregate`;
- `iter504t-repair-critic`;
- `iter504t-repair-verdict`.

The artifact IDs/digests are frozen in the authority ledger from terminal GitHub metadata before any artifact payload is opened.

## POSITIVE CONTROLS

1. Both assembly artifacts must expose the same frozen roots/rhos/R cohort and a parseable complete terminal leaf structure.
2. For every per-rho row, serialized `rho.certified` must equal exact boolean conjunction `slope_floor_satisfied AND drift_within_tolerance`.
3. For every terminal leaf, independently recomputed `all(per_rho.certified)` must be compared to serialized top-level `leaf.certified`; no fallback to serialized `unresolved_leaf_count` is allowed.
4. Independently recomputed unresolved-leaf counts and scientific class must agree between Python 3.11 and 3.13 terminal assemblies.
5. Aggregate/Critic/repair-verdict must refer to the same run/head/scientific realization and must not contradict the independently recomputed terminal decision.
6. C1 parent-inclusion and C3 exact-R repair evidence required by the frozen repair contract must remain present/valid; false parent-inclusion booleans remain diagnostic-only as originally frozen.

## NEGATIVE CONTROLS

The review logic must distinguish and reject at least:

1. a leaf with top-level `leaf.certified=true` while one actual per-rho certification is false;
2. a leaf with top-level `leaf.certified=false` while all actual per-rho certifications are true;
3. any per-rho serialized `certified` inconsistent with its slope/drift booleans;
4. a wrong/missing/extra R entry, including `6 -> 7`;
5. missing/incomplete C1 parent-inclusion records where the repair contract requires them;
6. artifact ID/digest/head/run mismatch or cross-run substitution;
7. a scientific class transported solely from serialized `unresolved_leaf_count` when independently recomputed leaf bindings disagree.

These controls are review predicates; no synthetic fixture may replace production terminal data in the substantive decision.

## PASS

`ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED` iff all required terminal artifacts/provenance match frozen authority, C1/C3 repair obligations are satisfied, every actual terminal per-rho and leaf certification relation is independently recomputed and exact, independently recomputed unresolved counts and scientific class agree across both environments, and aggregate/Critic/repair-verdict are consistent with that independently bound decision.

PASS validates only this exact completed run by an independent post-terminal gate. It does NOT erase or refute C4 as a launch-head validator defect and does not make the unchanged workflow generally valid for future executions.

## FAIL

`ITER504T_REPAIR_RERUN_AUTHORITY_RESTORATION_FAILED_SCOPED` iff provenance and terminal artifacts are complete/valid but the actual terminal data fail the independently frozen leaf-to-rho binding or the independently recomputed scientific decision disagrees with the transported aggregate/Critic/verdict decision. This is failure of exact-run authority restoration, not a scientific/model falsification.

If the independently recomputed original Iter504T scientific outcome is an originally preregistered INCONCLUSIVE label with otherwise valid implementation/binding, record that scientific INCONCLUSIVE separately; do not relabel it as FAIL.

## BLOCKED / INVALID

`ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED` iff one or more required terminal artifacts/fields are unavailable, corrupted, expired, or structurally insufficient to independently recompute the frozen leaf predicate without guessing. Missing data remain missing, never false/zero.

`INVALID_IMPLEMENTATION` iff authority/provenance identity fails, data from another run or nonterminal state are mixed in, frozen review criteria are changed after artifact inspection, the scientific object/threshold/classifier is changed, or synthetic production substitution occurs.

## INTERPRETATION CEILING

No outcome of this review establishes all 1888 states, D7 closure, model/family failure, terminal D7 selector, Candidate Gravity, Paper IV authorization, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

PASS, if obtained, is exact-run validation only and coexists with historical C4 `CONFIRMED_SCOPED` for the launch-head validator path. FAIL is only failure to restore exact-run authority. BLOCKED is missing terminal review object. `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`.
