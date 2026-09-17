# ITER504T_PRETERMINAL_CRITIC_DEFECT_BINDING_VERIFICATION_GATE — prospective freeze

Date: 2026-09-17
Status: PROSPECTIVELY_FROZEN_BEFORE_GATE_RESULT

## HYPOTHESIS

All three outcome-independent implementation/verification defect candidates recorded by the latest Iter504T preterminal Critic audit are actually supported by the exact frozen launch-head producer/assembler/Critic code:

1. `FROZEN_COMPONENTWISE_PARENT_INCLUSION_CONTROL_NOT_IMPLEMENTED_OR_RECORDED`;
2. `FROZEN_DYADIC_SPLIT_LOCATION_NOT_INDEPENDENTLY_VERIFIED`;
3. `FROZEN_R_COHORT_NOT_INDEPENDENTLY_VERIFIED`.

This is a verifier/closure hypothesis only. It is not a hypothesis about the Iter504T scientific root outputs.

## exact OBJECT

Exactly one outcome-blind closure question: whether each of the three Critic defect candidates above is true for the exact code blobs frozen by the single-execution authority and used by active run `35181094204`.

The gate may inspect source code and run synthetic malformed-payload fixtures through the frozen assembler/Critic validators. It must not read, download, inspect, infer, or summarize any substantive Iter504T root artifact, leaf value, assembly, aggregate, or scientific classification from the active run.

## DEPENDENCY

- Iter504T scientific preregistration commit `aa2b0256ce60d605574a18ec86c0bad5b5df1512`;
- Iter504T single-execution authority `3a485d34efaa500bbd0276b397c1a2078d18905e`;
- scientific launch head `d23f34cba57b220dd29474c0651bc727d6d85eae`;
- latest preterminal Critic audit commit `d5ddeb699343c498b2c0a0640f21ac01529bf47d`;
- latest terminal scientific parent remains Iter504S commit `1b0004064575f046210383dc7b1ee22d4f25e66b`.

The active scientific run remains nonterminal when this closure gate is frozen. This gate is admissible only because it consumes no scientific output and does not compete for a physical/scientific classification.

## SOURCE/REALIZATION AUTHORITY

Only the authority ledger `inputs/iter504t_preterminal_critic_defect_binding_verification_authority.json` and exact repository blobs it locks are authoritative.

The scientific launch-head code identities to be locked are:

- producer `code/iter504t_local_derivative_contraction.py`, blob `1ae78fc309839da30d1c78fc25c8e5ea3d98693f`;
- assembler `code/iter504t_local_derivative_assemble.py`, blob `6a886bf6ce8c263e586a6cb25d7441df5273a72d`;
- Critic `code/iter504t_local_derivative_critic.py`, blob `950d22e97b1ca2a17b2bb08d4386de6d4fb39445`;
- scientific preregistration `research/prereg/ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION_2026-09-17.md`, blob `f648b0e0d6a960bf60c32d5c34694497a50b7e68`;
- latest preterminal audit `recovery/CRITICAL_PRETERMINAL_AUDIT_ITER504T_LOCAL_DERIVATIVE_ENCLOSURE_CONTRACTION_2026-09-17.md`, blob `9fffd4a3b755d0f6b10220390299d600e523e0b8`.

Fresh repository state outranks narrative summaries. A Critic prose assertion is not self-authenticating if an executable counterexample against the exact frozen validator refutes it.

## FROZEN INPUTS

Three claim tests, fixed before execution:

### C1 — parent-inclusion binding

Construct an otherwise valid synthetic root payload whose terminal leaves are exact dyadic children but contain no `componentwise_parent_inclusion` field, no per-channel/R/rho inclusion map, and no Haar/log inclusion record.

C1 is VERIFIED iff:

- the frozen producer source does not serialize such a certificate; and
- both frozen assembler and frozen Critic validators accept the synthetic child payload despite those fields being absent.

C1 is REFUTED iff the producer does serialize the required record or either validator rejects the missing certificate specifically as a contract violation.

### C2 — dyadic split-location binding

Construct a synthetic root-13 payload that keeps the expected metadata label `partition_rule=deterministic_dyadic_midpoint` and exact gap-free root cover but splits the root at one third rather than at its dyadic midpoint.

C2 is VERIFIED iff both frozen assembler and frozen Critic accept that non-dyadic payload.

C2 is REFUTED iff either frozen validator independently rejects it through exact interval/depth identity logic such as `non_dyadic_cell`, without relying only on the metadata label.

### C3 — R-cohort binding

Start from a valid synthetic dyadic payload with exactly 16 `possible_max` rows representing the frozen 4 rho x 4 R grid. Mutate every row with `R=6` to `R=7`, identically in both hypothetical environment payloads, while preserving all other fields and the expected top-level metadata.

C3 is VERIFIED iff both frozen assembler and frozen Critic validators accept the changed-R payload and the Critic cross-environment projection cannot distinguish the mutation when both lanes carry it.

C3 is REFUTED iff the frozen validation path rejects the changed R set as a cohort violation.

## POSITIVE CONTROLS

1. A valid synthetic root-13 payload consisting of the two exact depth-1 dyadic children, all exact top-level metadata, four frozen rhos and 16 possible-max rows, must be accepted by both frozen validators.
2. The exact source blob identities above must match the frozen authority ledger.
3. Loading the frozen assembler/Critic modules for validation must not require any Iter504T scientific artifact.

## NEGATIVE CONTROLS

1. Mutating `threshold_exact` from `1/20` to another value must be rejected by both validators.
2. Mutating `root_box` away from the expected root must be rejected.
3. A malformed interval identity that cannot be parsed as an exact rational cell must be rejected.
4. Any attempt by this closure gate to read active-run root artifacts or scientific values is `INVALID_IMPLEMENTATION`.

## PASS

`ITER504T_PRETERMINAL_CRITIC_DEFECT_CLAIMS_ALL_VERIFIED_SCOPED`

iff C1, C2 and C3 are all VERIFIED and all controls pass.

PASS means only that all three preterminal Critic defect candidates are supported by the exact frozen verifier implementation.

## FAIL

`ITER504T_PRETERMINAL_CRITIC_DEFECT_CLAIMS_NOT_ALL_VERIFIED_SCOPED`

iff all controls pass and at least one of C1/C2/C3 is REFUTED by the exact frozen implementation. The result must record each claim separately as VERIFIED or REFUTED.

This is failure of the all-three-defects closure hypothesis, not scientific failure of Iter504T.

## BLOCKED / INVALID

`ITER504T_PRETERMINAL_CRITIC_DEFECT_BINDING_BLOCKED_SCOPED` iff the exact frozen code/blob authority cannot be loaded or the synthetic claim tests cannot be evaluated without substantive scientific artifacts.

`INVALID_IMPLEMENTATION` iff any locked blob mismatches, the harness changes a frozen claim definition after observing results, consumes active scientific payloads, fails a frozen positive/negative control, or substitutes a different implementation for the launch-head validators.

## INTERPRETATION CEILING

This gate can only validate/refute the three named preterminal Critic implementation-defect candidates. It cannot classify the active Iter504T science, cannot consume partial root values, cannot repair or rerun the active scientific gate, cannot establish PASS/INCONCLUSIVE/INVALID for Iter504T itself, and cannot imply all-1888 closure, D7 closure, model/family failure, Candidate Gravity, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.
