# KMQGB Critical Review — J1 K5 highest-contact magnetic leading transfer V4

Date: 2026-09-15
Lane: independent Critical Review / Verification

## RESULT_REVIEWED

Exactly one latest terminal substantive Research result was reviewed: the repaired terminal Actions execution of

`SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_LEADING_TRANSFER_V4`.

Authority chain:

- preregistration commit `01ccbad09d4a413066b1bcfbf77861d386926e73`;
- frozen input commit `8b933f94b8eea1c6990b33f9f2f563f7fabae461`;
- original implementation commit `921c2b4e3456ed6b98a24cd8896188eeea5ac2d8`;
- workflow commit `896ef424efe07e9662aa017119d8e7e86d74f2c6`;
- preterminal Critic counterexample commit `0711d734fec7d5dd451254df88b19c04e0162c16`;
- contract-preserving rotation-control repair commit `f903669dd08c6ae6fa9ac4d140ff85f294dd36c1`;
- authoritative repaired run `35023270636`, terminal `completed/success`;
- source-lock job `104564036270`;
- exact lanes `104564646182` (Python 3.11) and `104564646244` (Python 3.13);
- aggregate job `104569952760`;
- aggregate artifact `10419176929`, digest `sha256:4e199ba756f57e1776454c3a0fe67708e55f6a89acfeedacdedd372b41d1f5bf`;
- lane artifacts `10418704347`, digest `sha256:3ae0be72d4160ac663def736edc485aa6d7c52520e2371f38684071297747ecd`, and `10419141859`, digest `sha256:540a1707ec8f94d5543081012b08b0f98a5688ded7e8ed50d1dd74d7cbc0c731`.

The Research aggregate classification is

`SOURCE_J1_K5_CHANNEL00000_HIGHEST_CONTACT_SURVIVES_LEADING_SCOPED`.

This review does not rewrite that historical Actions result.

## PREREG_CHECK

PASS for chronology and for the rotation repair.

The scientific contract was frozen before implementation. The repair `f903669...` changes only the previously vacuous rotation-covariance control and adds the exact non-rotation adversarial fixture already demanded by the frozen `SPHERICAL_CARTESIAN` requirement. It does not change the hypothesis, object, tangent points, channel, source formulas, PASS/FAIL/BLOCKED branches, or interpretation ceiling.

Run `35023270636` source-lock verifies the exact preregistration and frozen input byte-for-byte and checks the frozen repository-authority blobs and V3/V3K dependency digests.

## OBJECT_IDENTITY_CHECK

PASS for the deciding object.

The run remains on frozen `j=l=k=1`, real nonzero symbolic `rho`, magnetic order `(-1,0,+1)`, source Toller branches, the fixed zero-based K5 tangent witness, and channel `00000`. No floating approximation decides the contraction.

The previous generic-direction defect is repaired correctly: with `Qz=I-3 e_z e_z^T`, the new control proves exactly that

`R Qz R^T - (I-3 n n^T) = R R^T-I`, with `n=R e_z`.

Hence every orthogonal rotation satisfies the target law. The explicit `R=diag(2,1,1)` non-rotation now fails the target and is rejected.

## SOURCE/REALIZATION_CHECK

QUALIFIED at the scientific level; FAIL at frozen-control implementation fidelity.

Positive exact algebra is internally consistent:

- source `F_1` differentiation reproduces the frozen `c1,c2,c3`;
- the highest branch contact coefficient is `sigma*i/[rho(1+rho^2)]`;
- exact magnetic Laurent limits give `+/- A diag(1,-2,1)` with `A=3i/[4 rho(1+rho^2)]`;
- the exact magnetic/contact scalar ratio is `3/4`;
- the repaired spherical/Cartesian and rotation chain is now non-vacuous;
- the K5 angular contraction is recomputed as `11/24` rather than imported;
- the K5 branch-sign product is exactly `+1` for all 32 vertex-sign assignments.

Current repository state also contains the outcome-independent analytic collision-scaling lemma `research/SOURCE_J1_CONTACT_COLLISION_SCALING_LEMMA_2026-09-15.md`, commit `e98cb3cf6f90b7d2f5bacbf5ca75b8c966ab3cd1`, which independently supports the hierarchy that at `j=1` only the `delta''` contact term can supply a cubic radial pole under the frozen pure-boost collision scaling.

However, the terminal V4 implementation does not execute two frozen controls as specified.

## PROVENANCE_CHECK

PASS for Actions execution provenance.

Run `35023270636` is terminal success at head `f903669...`; all four jobs are terminal success. The two exact lanes agree exactly and the artifact digests match the aggregate download log. Green CI is treated only as execution provenance.

The repository navigation front is stale relative to current main/Actions and therefore is not used as authority for the V4 verdict.

## SAME_REALIZATION_CHECK

PASS for the repaired rotation map and fixed K5 realization.

The old counterexample `R=diag(2,1,1)` is now explicitly rejected. The K5 tensors use `Q(v)=I-3 vv^T/||v||^2`, consistent with the repaired exact rotation identity for unit tangent directions.

A separate frozen-control mismatch remains below and is independent of the K5 realization.

## NUMERICAL/STATISTICAL_CHECK

PASS for the deciding exact coefficient; no statistical inference is used.

The aggregate reports exact lane agreement, all controls true, angular contraction `11/24`, and

`physical_highest_contact_leading_coefficient = -216513/[8388608 rho^10 (rho^2+1)^10]`.

Independent algebra confirms this value:

`(11/24) * [3i/(4 rho(1+rho^2))]^10 = -216513/[8388608 rho^10 (rho^2+1)^10]`,

which is nonzero for real `rho != 0`.

Thus no numerical-method blocker is present in the deciding coefficient.

## COUNTEREXAMPLE_ATTEMPTS

1. **Old vacuous rotation covariance.** Repaired successfully. The exact residual is now tied to `R R^T-I`, and the frozen non-orthogonal counterexample is rejected.
2. **Wrong source polynomial / Laurent coefficient.** No counterexample found; exact symbolic identities agree with the frozen formulas.
3. **Wrong K5 branch parity.** No counterexample found; every vertex sign appears four times, so `prod_(a<b)(sigma_a sigma_b)=prod_a sigma_a^4=1`.
4. **Imported historical `11/24`.** No defect found; production recomputes it from the ten tensors/intertwiners.
5. **Floating approximation deciding science.** No defect found in the deciding path.
6. **`UNIQUE_CUBIC_SOURCE` control.** Counterexample to control fidelity established. The code does not derive power orders from the complete D1-D4 split. It sets
   `scaling_orders={step:0, delta:-1, delta_prime:-2, delta_double_prime:-3}`
   and then checks that the only hard-coded `-3` entry is `delta_double_prime`. This predicate cannot detect an error in the source-to-scaling derivation; it encodes the expected conclusion.
7. **`REMOVE_HIGHEST_CONTACT_NEGATIVE` control.** Explicit implementation counterexample established. The frozen control requires deleting `c3/delta''`, retaining lower contact and step pieces, and verifying that the same transfer chain rejects any cubic attribution. The implementation performs no such deletion. Instead it defines
   `remove_highest_contact_rejected = bool(A != 0 and unique_cubic)`.
   This boolean does not reference `c3`, the highest-contact coefficient, or a mutated source split. Therefore it remains true without ever exercising the required negative fixture. A no-op "deletion" path passes this control by construction.
8. **Green CI promoted to science.** Rejected: exact algebra supports the scoped coefficient, but CI cannot cure a frozen-control mismatch.

## OVERCLAIM_CHECK

The scientific claim ceiling in the preregistration is appropriate and the aggregate does not by itself assert joint distribution-product existence, complete-vertex divergence, all channels/spins/strata, model/family failure, D7 closure, a terminal selector, or Candidate Gravity activation.

Nevertheless, the Research PASS cannot be accepted as a frozen-contract-compliant terminal scientific result because mandatory outcome-sensitive negative/control logic is not implemented as frozen.

The underlying exact coefficient may well be correct; this Critic verdict is not a scientific FAIL and does not assert cancellation.

## VERDICT

`INVALID_IMPLEMENTATION`

Reason: the implementation does not satisfy the frozen gate's mandatory `UNIQUE_CUBIC_SOURCE` derivation/control and, decisively, does not execute the required `REMOVE_HIGHEST_CONTACT_NEGATIVE` fixture. Per governance, implementation mismatch invalidates the Research PASS even though the repaired rotation control and exact production coefficient are consistent.

## QUALIFICATIONS

1. The previous rotation-covariance defect is genuinely repaired by `f903669...`.
2. The exact production coefficient and nonzero fixed-channel contraction are independently algebraically consistent.
3. `INVALID_IMPLEMENTATION` here is not `SCIENTIFIC_FAIL_CONFIRMED`; it does not establish cancellation or absence of the highest-contact leading tensor.
4. The historical run `35023270636` and its PASS label remain immutable history but must not be consumed downstream as independently validated V4 authority.
5. The later analytic collision-scaling lemma is useful independent support, but it does not substitute for the prospectively required executable negative fixture.
6. Iter504 run `34907349374` and Iter461 run `34748503239` were freshly checked and remain `queued / conclusion=null`; no partial substantive values were consumed.
7. Governance remains: `RQIR Core v1.0 = FROZEN`, `D7-S2 = NOT_CLOSED`, `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; terminal selectors forbidden; Candidate Gravity inactive.

## UPDATED_STATE

- `SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_LEADING_TRANSFER_V4 = INVALID_IMPLEMENTATION` by independent Critic for terminal run `35023270636`.
- rotation covariance repair = accepted.
- exact production coefficient = independently consistent but not sufficient to validate the frozen gate.
- Research PASS `SOURCE_J1_K5_CHANNEL00000_HIGHEST_CONTACT_SURVIVES_LEADING_SCOPED` = historical, not validated downstream.
- no joint distribution-product existence conclusion.
- no model/family failure, D7 closure, selector, or Candidate Gravity activation.

## NEXT_ADMISSIBLE_GATE

A contract-preserving implementation repair may reuse the same prospective V4 gate **only if the scientific contract is unchanged**.

Required repair:

1. Replace the hard-coded `UNIQUE_CUBIC_SOURCE` predicate by an executable derivation/check of the frozen D1-D4 scaling hierarchy, or an equivalent exact implementation that actually derives the orders consumed by classification.
2. Implement one classifier/transfer function used by both production and adversarial fixtures.
3. Construct the frozen negative fixture by setting/removing `c3/delta''` while retaining `theta`, `delta`, and `delta'`, then run the same transfer classifier and require that cubic attribution is rejected.
4. Preserve the repaired SO(3)/non-orthogonal rotation control.
5. Rerun both exact Python lanes and aggregate with fresh artifacts/digests.

If the repair changes source authority, the scientific scaling lemma, source split, object, tangent witness, channel, decision branches, or interpretation ceiling, do not call it an implementation-only repair: freeze a new prospective gate instead.
