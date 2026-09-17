# ITER504T_PRETERMINAL_LEAF_CERTIFICATION_BINDING_VERIFICATION_GATE — prospective freeze

Date: 2026-09-17
Status: PROSPECTIVELY_FROZEN_BEFORE_SUBSTANTIVE_RESULT

## HYPOTHESIS

The active Iter504T repair launch may or may not contain a decision-binding implementation defect in which downstream validators independently verify each per-rho predicate but fail to bind the serialized top-level terminal-leaf `certified` flag to the conjunction of all four frozen per-rho certifications. This closure gate must verify or refute that C4 hypothesis without inspecting any substantive artifact from the nonterminal repair run.

## exact OBJECT

Exactly one implementation/provenance predicate-binding question at immutable repair launch head `10ae6bcc8447d14cecc6e550065504b23f792953`.

The frozen scientific predicate from the original Iter504T preregistration is:

- `rho_certified := slope_floor_satisfied AND drift_within_tolerance`;
- a node/terminal leaf is certified iff all four frozen rho predicates are certified;
- scientific PASS requires every terminal leaf to be scientifically certified.

The object is whether the launch-head assembler/Critic/aggregate decision path independently enforces the second implication rather than trusting the producer's serialized top-level `leaf.certified` flag.

No active numerical root, assembly, aggregate, Critic, or repair-verdict artifact is part of this object.

## DEPENDENCY

- original scientific preregistration commit `aa2b0256ce60d605574a18ec86c0bad5b5df1512`;
- active repair preregistration commit `adc7bfb9df77a90455cac1b0f0cb7255d80c44d5`;
- repair launch head `10ae6bcc8447d14cecc6e550065504b23f792953`;
- latest outcome-independent preterminal Critic refresh commit `009923a0806a4306925fd9fda56f7f489d6313f1`;
- active repair run `35205054496` remains scientifically nonterminal and its substantive artifacts are forbidden inputs.

## SOURCE/REALIZATION AUTHORITY

Only the prospectively committed authority ledger `inputs/iter504t_preterminal_leaf_certification_binding_verification_authority.json` and the immutable repository blobs it locks may determine this gate.

Authoritative implementation paths at launch head:

- `research/prereg/ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION_2026-09-17.md`;
- `code/iter504t_local_derivative_assemble.py`;
- `code/iter504t_local_derivative_critic.py`;
- `code/iter504t_local_derivative_aggregate.py`.

The active Actions artifacts/run outputs are explicitly excluded from scientific/closure authority for this gate.

## FROZEN INPUTS

1. Original scientific predicate identity exactly as frozen in the original preregistration.
2. Launch-head assembler `validate()` behavior.
3. Launch-head independent Critic `validate()` behavior.
4. Launch-head aggregate equality/classification path.
5. A synthetic outcome-independent root fixture satisfying all other launch-head structural/provenance validators.
6. Target adversarial mutation: one frozen rho row remains internally consistent but `certified=false`; top-level terminal-leaf `certified=true`; `unresolved_leaf_count` is updated consistently with that top-level flag; all other fields remain contract-valid.
7. Dual-lane version of the same malformed mutation to test whether cross-environment equality alone can mask it.

No real active scientific values may be copied into the fixture.

## POSITIVE CONTROLS

1. A fully compliant synthetic terminal leaf with all four rho certifications true and top-level `leaf.certified=true` must be accepted by assembler and Critic validators.
2. The exact frozen per-rho identity must be independently enforced: changing a rho row so `certified != (slope_floor_satisfied AND drift_within_tolerance)` must be rejected.
3. The repaired exact R-cohort binding remains live: a synthetic `R=6 -> 7` mutation in the possible-max cohort must be rejected.
4. Source/prereg/launch-head blob identities must match the prospectively frozen authority ledger.

## NEGATIVE / OUTCOME-SENSITIVE CONTROLS

1. Target C4 mutation described above.
2. The same target mutation applied identically to both synthetic environment lanes must not be rescued merely by cross-environment equality if the scientific predicate is independently bound.
3. Wrong blob/head/prereg identity, active scientific artifact use, or post-hoc contract mutation is `INVALID_IMPLEMENTATION`.

## PASS / C4 VERIFIED

`ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED`

iff the exact launch-head downstream validator path accepts the target malformed leaf (or otherwise fails to independently require `leaf.certified == all(rho.certified for rho in leaf.per_rho)`) while the positive controls demonstrate that the test actually exercises the relevant validators.

This is PASS for the defect hypothesis only. It is an implementation/provenance finding, not scientific FAIL.

## FAIL / C4 REFUTED

`ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_REFUTED_SCOPED`

iff the exact launch-head assembler/Critic/aggregate path rejects the target malformed leaf and independently binds every frozen conjunction needed for top-level leaf certification, with all controls passing.

This is scoped refutation of C4 only.

## BLOCKED

`ITER504T_LEAF_CERTIFICATION_BINDING_VERIFICATION_BLOCKED_SCOPED`

iff the preregistration-to-implementation mapping or exact launch-head validator path cannot be established from the frozen durable authority. Missing evidence is not evidence of correct binding.

## INVALID

`INVALID_IMPLEMENTATION`

for source/blob/head mismatch, non-faithful synthetic fixture that fails unrelated validators, use of active substantive artifacts, broken positive/negative controls, or any post-result change to this frozen contract.

## INTERPRETATION CEILING

This gate may establish or refute only C4 as a launch-head implementation/decision-binding defect. It says nothing about the actual numerical contents of active run `35205054496`, does not classify that repair rerun scientifically, does not establish scientific PASS/FAIL/INCONCLUSIVE for Iter504T, does not alter historical C1/C2/C3 findings, does not close all 1888 states or D7, and does not authorize Candidate Gravity, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.
