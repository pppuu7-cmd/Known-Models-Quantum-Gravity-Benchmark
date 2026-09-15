# V4 same-contract implementation repair protocol — 2026-09-16

Status: `FROZEN_BEFORE_REPAIR_IMPLEMENTATION_OR_RERUN`

Parent scientific contract: `research/prereg/SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_LEADING_TRANSFER_V4_2026-09-15.md`, commit `01ccbad09d4a413066b1bcfbf77861d386926e73`.
Frozen input: `inputs/source_j1_k5_highest_contact_magnetic_leading_transfer_v4.json`, commit `8b933f94b8eea1c6990b33f9f2f563f7fabae461`.
Latest independent Critic: `recovery/CRITICAL_REVIEW_SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_LEADING_TRANSFER_V4_2026-09-15.md`, commit `c0358e348bbb225719bb1617f905e38d91f33e21`, verdict `INVALID_IMPLEMENTATION`.
Accepted rotation-control repair: `f903669dd08c6ae6fa9ac4d140ff85f294dd36c1`.

This is an implementation-only repair. It does not alter the frozen HYPOTHESIS, OBJECT, source authority, source split, collision-scaling lemma, tangent witness, channel, PASS/FAIL/BLOCKED/INVALID semantics, or interpretation ceiling.

## Repair requirements

1. `UNIQUE_CUBIC_SOURCE` must be derived executably from the complete frozen Appendix-D j=1 source split. The repair must construct the `theta`, `delta`, `delta'`, and `delta''` pieces from the rederived `c1,c2,c3` coefficients and derive the pullback scaling exponent for each delta derivative from the positive-scale distribution rule rather than loading a conclusion-bearing order table.
2. The production path and adversarial fixtures must use one common transfer classifier.
3. `REMOVE_HIGHEST_CONTACT_NEGATIVE` must physically remove/zero the `c3/delta''` source term while preserving `theta`, `delta`, and `delta'`, then pass that mutated split through the same transfer classifier. The classifier must reject cubic source attribution.
4. `WRONG_RATIO_NEGATIVE` and `SYNTHETIC_CANCELLATION` must also use the same transfer classifier.
5. The accepted exact SO(3)/non-orthogonal rotation controls from `f903669...` must remain active.
6. Both exact Python lanes (3.11 and 3.13) must rerun with pinned `sympy==1.14.0`, `numpy==2.3.3`; aggregate classification requires exact lane agreement and all frozen controls.
7. Fresh artifact IDs/digests are required. Historical run `35023270636` remains immutable history and is not downstream authority unless this repair independently validates the frozen contract.

## Allowed terminal outcomes

The repair reuses only the original frozen labels:

- `SOURCE_J1_K5_CHANNEL00000_HIGHEST_CONTACT_SURVIVES_LEADING_SCOPED`
- `SOURCE_J1_K5_CHANNEL00000_HIGHEST_CONTACT_CANCELS_LEADING_SCOPED`
- `SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_TRANSFER_BLOCKED_SCOPED`
- `INVALID_IMPLEMENTATION`

No new scientific claim is introduced by this repair.

## Governance

`RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; terminal selectors remain forbidden; Candidate Gravity remains inactive; KMQGB remains downstream of pinned DSIR authority.
