# KMQGB Critical preterminal audit — J1 K5 highest-contact magnetic leading transfer V4

Date: 2026-09-15
Lane: independent Critical Review / Verification
Status: PRETERMINAL — NO SCIENTIFIC VERDICT ISSUED

## RESULT_REVIEWED

No terminal V4 Research result exists yet. The bounded object audited here is the currently authoritative non-terminal workflow:

- gate `SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_LEADING_TRANSFER_V4`;
- preregistration commit `01ccbad09d4a413066b1bcfbf77861d386926e73`;
- frozen input commit `8b933f94b8eea1c6990b33f9f2f563f7fabae461`;
- implementation commit `921c2b4e3456ed6b98a24cd8896188eeea5ac2d8`;
- workflow head `896ef424efe07e9662aa017119d8e7e86d74f2c6`;
- authoritative Actions run `35018723264`;
- source-lock job `104548630701` completed/success;
- exact lanes `104553026278` (Python 3.13) and `104553026336` (Python 3.11) are queued at this audit;
- no aggregate verdict/artifact exists yet.

No partial substantive lane value is consumed and no competing PASS/FAIL/BLOCKED/INVALID verdict is created.

Current repository `main` at audit start is `e98cb3cf6f90b7d2f5bacbf5ca75b8c966ab3cd1`, which is newer than the workflow head. The later commit adds `research/SOURCE_J1_CONTACT_COLLISION_SCALING_LEMMA_2026-09-15.md`; it is not part of run `35018723264` and cannot retroactively repair that run.

## PREREG_CHECK

PASS for prospective chronology.

The chain is linear and outcome-independent:

`01ccbad...` prereg -> `8b933f9...` frozen input -> `921c2b4...` implementation -> `896ef42...` workflow.

The frozen input records terminal V3/V3K authorities. Live Actions artifact metadata independently agrees with the frozen dependency digests:

- V3 aggregate artifact `10415708250`, digest `sha256:09268182961e09b3413d13684526574c1924d6aa37f17b39a9d65477907cabc1`;
- V3K artifact `10416047992`, digest `sha256:bfa25bdfe600f090ca5f273c1797e8804b94dc190d5d68130466e692876ec292`.

The preregistration explicitly requires exact `SPHERICAL_CARTESIAN` rotation covariance and declares `INVALID_IMPLEMENTATION` if `Q` is assumed to be the contact tensor without the frozen uniqueness chain.

## OBJECT_IDENTITY_CHECK

No object-switch was found in the frozen data itself. The implementation uses:

- `j=l=k=1`;
- real nonzero symbolic `rho`;
- magnetic order `(-1,0,+1)`;
- the frozen K5 tangent points;
- channel `00000`;
- exact rational/symbolic arithmetic for the deciding contraction.

However, the general-direction tensor identity needed before the K5 object is constructed is not actually verified by the current rotation-covariance control; see the explicit counterexample below.

## SOURCE/REALIZATION_CHECK

V3/V3K source/convention dependencies are correctly frozen and their live artifact digests match the input ledger.

The V4 implementation correctly rederives the source polynomial coefficients, the z-axis magnetic cubic Laurent limits, the scalar ratio `3/4`, the spherical-to-Cartesian z-axis map, exact intertwiner norms, branch parity, and the fixed K5 contraction machinery at code level.

The unresolved implementation issue is the transition from the z-axis magnetic tensor to a generic pure-boost tangent direction. The frozen contract requires exact rotation covariance to establish

`Q(n) = I - 3 n n^T`

before those tensors are used on the ten K5 edges.

## PROVENANCE_CHECK

Current run `35018723264` is non-terminal. Source-lock completed successfully. Exact lanes are queued and there is no aggregate artifact/digest to consume.

No partial output from either exact lane is used here.

The post-launch analytic lemma commit `e98cb3c...` is repository research context only. Because it is newer than workflow head `896ef42...`, it is outside the current run's frozen execution provenance.

## SAME_REALIZATION_CHECK

PRETERMINAL IMPLEMENTATION DEFECT CANDIDATE: the exact rotation-covariance control is vacuous with respect to the target identity.

The implementation defines

`Qz = I - 3 e_z e_z^T`,
`n = R e_z`,

for a completely unconstrained symbolic `3x3` matrix `R`, and then marks rotation covariance true when

`R Qz R^T = R R^T - 3 n n^T`.

But this equality is an algebraic identity for **every** matrix `R`, because substituting `Qz = I - 3 e_z e_z^T` makes both sides identical by construction. It does not check `R R^T = I` and therefore does not establish

`R Qz R^T = I - 3 n n^T`

for an actual rotation.

### Explicit counterexample

Choose the non-rotation

`R = diag(2,1,1)`.

Then `n = R e_z = e_z`. The implementation's tested identity gives

`R Qz R^T = R R^T - 3 n n^T = diag(4,1,-2)`,

so the current control passes. But the frozen target tensor for the same unit direction is

`Q(n) = I - 3 n n^T = diag(1,1,-2)`,

which is different.

Thus the current predicate can report `rotation_covariance_identity=true` for a transformation that is not a rotation and that does not produce the frozen target tensor.

Immediately afterward, the K5 implementation constructs every edge tensor directly with

`Q(v) = I - 3 v v^T / ||v||^2`.

Therefore the general-direction form is effectively assumed after a control that does not prove it. This is precisely the failure mode named in the frozen INVALID clause: `Q` must not be assumed to be the contact tensor without the frozen uniqueness/rotation chain.

This counterexample is outcome-independent: it does not depend on the queued exact-lane numerical/symbolic outputs or on whether the eventual K5 contraction is zero or nonzero.

## NUMERICAL/STATISTICAL_CHECK

No deciding floating approximation appears in the inspected implementation path for the scientific coefficient; exact SymPy/Fraction objects drive the source algebra and contraction.

No non-terminal substantive output is consumed.

The defect above is logical/representation-theoretic, not numerical.

## COUNTEREXAMPLE_ATTEMPTS

1. **Wrong source polynomial / contact coefficient** — no defect established in static audit; code differentiates the frozen `F_1` symbolically.
2. **Wrong z-axis magnetic Laurent order** — no defect established in static audit; code takes exact one-sided symbolic limits.
3. **Wrong magnetic ordering** — explicit negative fixture exists.
4. **Imported historical `11/24`** — production contraction is recomputed from tensors; the value is used as an exact regression control, not read from a historical result file.
5. **Branch-sign cancellation assumption** — code enumerates all 32 vertex-sign assignments and derives K5 edge-product parity.
6. **Generic-direction covariance** — explicit counterexample succeeds: `R=diag(2,1,1)` passes the implemented control while violating the frozen target `Q(n)` identity.
7. **Post-hoc repair by later research note** — rejected: commit `e98cb3c...` postdates workflow head and cannot alter run `35018723264`; moreover that note addresses collision scaling, not this rotation-control defect.
8. **Green CI promoted to science** — rejected prospectively: even a future successful aggregate cannot by itself repair a frozen-contract mismatch.

## OVERCLAIM_CHECK

No terminal claim is presently admissible because the authoritative workflow is non-terminal.

In particular, no current repository evidence authorizes consuming a V4 PASS, FAIL, or BLOCKED label from partial execution. If run `35018723264` later reports a PASS/FAIL/BLOCKED on the unchanged implementation, the Critic must first resolve the rotation-covariance defect above before accepting that classification as frozen-contract compliant.

## VERDICT

NONE — authoritative Research workflow is non-terminal.

This document intentionally does not issue one of the terminal Critic verdict labels.

## QUALIFICATIONS

- Prospective chronology/source-lock provenance is presently consistent.
- V3 and V3K frozen dependency artifact digests independently match live Actions metadata.
- The current implementation contains an outcome-independent counterexample to its `rotation_covariance_identity` control.
- The defect is upstream of the generic-direction K5 tensor construction and therefore can affect the frozen implementation contract even if two exact lanes later agree perfectly.
- The later collision-scaling lemma commit does not repair this run.
- Historical Research results remain unchanged.
- RQIR Core v1.0 remains FROZEN; D7-S2/S3 remain NOT_CLOSED; D7-S4 remains PARTIAL_GLOBAL_NOT_CLOSED; terminal selectors remain forbidden; Candidate Gravity remains inactive.

## UPDATED_STATE

- `SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_LEADING_TRANSFER_V4`: authoritative run non-terminal.
- no V4 scientific verdict consumed.
- source-lock: success.
- exact lanes: queued at audit time.
- generic-direction rotation control: explicit defect candidate established by exact counterexample.
- current run must not be treated as validated generic-direction transfer authority before terminal Critic review.

## NEXT_ADMISSIBLE_GATE

First wait for the authoritative V4 workflow to reach a terminal state; do not consume partial lane values.

At terminal review, apply the counterexample above before accepting the Research classification. If the implementation is unchanged, the frozen `SPHERICAL_CARTESIAN` / rotation requirement must be evaluated against the fact that the current control is tautological for arbitrary `R`.

A contract-preserving implementation repair can replace the vacuous check by an exact SO(3) covariance proof/control, for example an exact orthogonal parameterization or generator-level proof that establishes `R R^T=I`, `n=R e_z`, and therefore `R Qz R^T = I-3nn^T`, plus an adversarial non-orthogonal matrix that must fail. The K5 edge tensors should then be derived through that validated map rather than merely instantiated from the target formula.

This is an implementation repair if HYPOTHESIS, object, source authority, tangent points, channel, decision branches, and interpretation ceiling remain unchanged. Any repair that changes the scientific transfer claim or authority corpus requires a new prospectively frozen gate.
