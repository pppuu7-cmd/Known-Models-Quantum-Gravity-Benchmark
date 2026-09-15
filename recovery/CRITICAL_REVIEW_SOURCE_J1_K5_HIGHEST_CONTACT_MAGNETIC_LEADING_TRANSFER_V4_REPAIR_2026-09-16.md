# KMQGB Critical Review — J1 K5 highest-contact magnetic leading transfer V4 same-contract repair

Date: 2026-09-16
Lane: independent Critical Review / Verification

## RESULT_REVIEWED

Exactly one latest terminal substantive Research result was reviewed:

`SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_LEADING_TRANSFER_V4` — fresh same-contract repaired execution.

Authority chain:

- scientific preregistration commit `01ccbad09d4a413066b1bcfbf77861d386926e73`;
- frozen input commit `8b933f94b8eea1c6990b33f9f2f563f7fabae461`;
- historical Critic commit `c0358e348bbb225719bb1617f905e38d91f33e21`, verdict `INVALID_IMPLEMENTATION` for run `35023270636`;
- accepted rotation-control repair `f903669dd08c6ae6fa9ac4d140ff85f294dd36c1`;
- same-contract repair protocol `91bcaadc83be2934e09ec3e32b17709b3306d059`, frozen before repair implementation;
- repair implementation `bbb39f58bbda2a24977d2ab1438a7f78c80bdb91`;
- repair workflow head `0b13ccac5eaf4cbb4d463411d0048c483af93af1`;
- authoritative run `35033194283`, terminal `completed/success`;
- source-lock job `104596220542`;
- exact Python 3.11 lane `104596257007`;
- exact Python 3.13 lane `104596256994`;
- aggregate job `104596351274`;
- aggregate artifact `10421794928`, digest `sha256:8f969582092101fb270afd0251f9f603b3695ff913332098fd75511b7fb0976b`;
- Python 3.11 artifact `10422336163`, digest `sha256:08808cef77802a9c19ac2ddf8c075baa311a3bed1adbd3d3786d366aaf1823e8`;
- Python 3.13 artifact `10421889454`, digest `sha256:6d8d8f94825f4cb1f0faf180242c3e6d23383ef0fe83f88f65bb63bbfdfec889`;
- terminal repaired result commit `8f1e3fe98dc34f1bef671b3dbbe6b303a404fefc`.

Research classification:

`SOURCE_J1_K5_CHANNEL00000_HIGHEST_CONTACT_SURVIVES_LEADING_SCOPED`.

Historical invalid run `35023270636` remains immutable history and is not rewritten.

## PREREG_CHECK

PASS.

Chronology is prospective and contract-preserving. The repair protocol is the direct parent of the repair implementation, and the workflow is the direct child of the repair implementation. The protocol explicitly freezes an implementation-only repair and forbids changes to HYPOTHESIS, OBJECT, source authority, source split, collision-scaling lemma, tangent witness, channel, PASS/FAIL/BLOCKED/INVALID taxonomy, and interpretation ceiling.

The source-lock job checks the frozen preregistration and input byte-for-byte, verifies the historical Critic/rotation-repair/protocol/base-implementation identifiers, locks the base implementation blob, and verifies repository authority blobs plus the V3/V3K dependency digests.

No post-hoc scientific threshold, state, channel, tangent, or source selection was introduced.

## OBJECT_IDENTITY_CHECK

PASS.

The repaired run remains on the frozen object:

- `j=l=k=1`;
- symbolic real nonzero `rho`;
- source Toller branches `sigma=+/-1`;
- magnetic ordering `(-1,0,+1)`;
- one-wedge positive pure-boost collision;
- frozen zero-based K5 tangent witness `X0=(0,0,0)`, `X1=(1,0,0)`, `X2=(0,1,0)`, `X3=(0,0,1)`, `X4=(1,1,1)`;
- fixed channel `00000`.

The implementation consumes the same frozen input and authority blobs. No surrogate object or alternate realization is substituted.

## SOURCE/REALIZATION_CHECK

PASS within the frozen scoped authority.

The source polynomial is re-differentiated exactly and yields

- `c1=(1+3 rho^2)/(rho(1+rho^2))`,
- `c2=6/(1+rho^2)`,
- `c3=6/(rho(1+rho^2))`.

The branch highest-contact coefficient is therefore `sigma*i/[rho(1+rho^2)]` multiplying `delta''(B)`.

The exact magnetic Laurent calculation independently gives

`A(rho)=3i/[4 rho(1+rho^2)]`

with branch tensors `+/- A diag(1,-2,1)`, and hence exact magnetic/contact scalar ratio `3/4` in both branches.

V3 fixes the coherent-to-magnetic Toller basis/convention bridge and V3K fixes equality of the two frozen scalar projector kernels. The separately derived collision-scaling lemma supplies the one-wedge source-order identification under the frozen positive pure-boost scaling. No additional representation change is introduced by the repair.

## PROVENANCE_CHECK

PASS.

Run `35033194283` is terminal `completed/success` at head `0b13ccac...`. All four jobs are terminal success. The live Actions artifact IDs/digests match the terminal result and recovery ledger.

The two exact lanes install the frozen versions `sympy==1.14.0` and `numpy==2.3.3`, execute the same repair certificate, and produce fresh artifacts. Aggregate download verifies both artifact digests before comparison.

Green CI is used only as execution provenance, not as scientific evidence.

## SAME_REALIZATION_CHECK

PASS.

The previous rotation-covariance defect remains repaired: the base control proves exactly

`R Q_z R^T - (I-3 n n^T) = R R^T-I`, `n=R e_z`,

so the target follows for orthogonal rotations, while the non-rotation fixture `R=diag(2,1,1)` is explicitly rejected.

The K5 edge tensors are built from the same law `Q(v)=I-3 vv^T/||v||^2` at the frozen tangent points. Branch parity is recomputed over all 32 vertex-sign assignments and gives edge-sign product `+1` identically.

The previously invalid `REMOVE_HIGHEST_CONTACT_NEGATIVE` control now genuinely changes the same source realization: the repair rebuilds the source split without `c3/delta''`, preserves `theta`, `delta`, and `delta'`, and passes this mutated split to the same `transfer_classifier` used for production. Both branches are rejected with `NO_UNIQUE_CUBIC_SOURCE_COMPONENT`.

## NUMERICAL/STATISTICAL_CHECK

PASS; the deciding result is exact and non-statistical.

The repaired `UNIQUE_CUBIC_SOURCE` control is no longer a hard-coded conclusion table. For each delta derivative order `n=0,1,2`, the implementation derives the positive-scale distribution weight from the exact test-function action and obtains exponent `-(n+1)`. Together with the scale-invariant step piece, both branches derive

- `step -> 0`,
- `delta -> -1`,
- `delta_prime -> -2`,
- `delta_double_prime -> -3`.

The use of the monomial witness `phi(y)=y^n/n!` is sufficient for this homogeneity check because the `delta^(n)` action is completely determined by the `n`th derivative at the origin; the exact ratio is `beta^{-(n+1)}` and no floating approximation enters the decision.

The K5 angular contraction is recomputed exactly as `11/24`. Independent algebra confirms

`(11/24) * [3i/(4 rho(1+rho^2))]^10 = -216513/[8388608 rho^10 (rho^2+1)^10]`,

which is nonzero for real `rho != 0`.

Both Python lanes agree exactly on all decision-critical fields compared by the aggregate, including controls, derived scaling orders/proofs, production and negative classifiers, magnetic limits, angular contraction, and physical coefficient.

## COUNTEREXAMPLE_ATTEMPTS

1. **Historical hard-coded scaling table.** Rejected by the repair: exponents are now derived by `exact_delta_pullback_exponent` from the positive-scale distribution action before comparison with the frozen expected hierarchy.
2. **Historical no-op highest-contact deletion.** Rejected by the repair: the negative fixture omits the `n=2/c3` term from the constructed source split; lower terms remain; the common classifier sees no cubic source component and returns `NO_UNIQUE_CUBIC_SOURCE_COMPONENT`.
3. **Different classifier for adversarial fixtures.** No defect found: production, remove-highest, wrong-ratio, and synthetic-cancellation fixtures all call the same `transfer_classifier`.
4. **Wrong scalar transfer.** The ratio-1 fixture is rejected exactly with `SCALAR_RATIO_MISMATCH`; physical branches give exact ratio `3/4`.
5. **Wrong magnetic ordering.** The fixture moving `-2` away from `m=0` fails the spherical/Cartesian control.
6. **Old vacuous rotation covariance.** Remains repaired; the non-orthogonal `diag(2,1,1)` fixture fails the target law.
7. **Imported historical `11/24`.** No defect found: the angular contraction is recomputed from the ten edge tensors and exact intertwiners.
8. **Synthetic zero promoted to physical cancellation.** No defect found: replacing one edge tensor by the exact zero tensor drives the same classifier to the frozen FAIL/cancellation branch, while the physical tensor set remains nonzero.
9. **Branch-sign mismatch.** No counterexample found: every vertex sign occurs on four K5 edges, so `prod_(a<b)(sigma_a sigma_b)=prod_a sigma_a^4=1`.
10. **Floating approximation / green CI promoted to science.** Rejected: all deciding algebra is symbolic/rational; CI supplies provenance only.
11. **Scoped leading certificate promoted to a joint-distribution theorem.** Rejected by the interpretation firewall. The run never multiplies the ten singular contact distributions as a distribution product.

No explicit counterexample to the repaired frozen contract was found.

## OVERCLAIM_CHECK

PASS.

The repaired terminal note preserves the frozen interpretation ceiling. The result establishes only survival of the highest `delta''` contact leading homogeneous tensor for the frozen `j=1`, real nonzero-`rho`, channel-`00000`, fixed full-K5 tangent witness.

It does not establish joint contact-product existence/nonexistence, complete vertex convergence/divergence, source Feynman-regulator success/failure, lower-contact survival, all channels/spins/strata, model/family failure, D7 closure, a terminal selector, or Candidate Gravity activation.

The statement that universal cancellation of this highest contact component is false is valid only in the sense frozen by the gate: a single exact nonzero fixed-channel/fixed-tangent witness refutes cancellation universal over that claimed sector; it is not family closure.

## VERDICT

`CONFIRMED_SCOPED`

The fresh same-contract repair removes both implementation defects that invalidated historical run `35023270636`. The repaired scaling hierarchy is executable, the highest-contact deletion is a real source-split mutation seen by the common classifier, the accepted rotation repair remains active, exact dual-lane provenance is complete, and the fixed channel-`00000` highest-contact leading coefficient is independently algebraically nonzero.

## QUALIFICATIONS

1. This verdict applies to fresh repair run `35033194283`, not retroactively to historical invalid run `35023270636`.
2. The confirmed fact is the scoped highest-contact leading tensor survival at the frozen realization/tangent/channel only.
3. No joint distribution-product theorem follows.
4. No complete-vertex divergence/convergence conclusion follows.
5. No model/family failure, D7 closure, terminal selector, or Candidate Gravity activation follows.
6. The BLOCKED label remains semantically distinct from FAIL; it is simply not activated by the present exact authority chain.
7. Iter504 run `34907349374` and Iter461 run `34748503239` were freshly checked and remain workflow-level `queued / conclusion=null`; no partial substantive values were consumed.
8. `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; terminal selectors remain forbidden; Candidate Gravity remains inactive.

## UPDATED_STATE

- fresh repaired `SOURCE_J1_K5_HIGHEST_CONTACT_MAGNETIC_LEADING_TRANSFER_V4 = CONFIRMED_SCOPED` by independent Critic;
- authoritative repaired Research classification `SOURCE_J1_K5_CHANNEL00000_HIGHEST_CONTACT_SURVIVES_LEADING_SCOPED` is independently validated for run `35033194283`;
- historical V4 run `35023270636 = INVALID_IMPLEMENTATION` remains immutable history;
- highest-contact one-wedge source-to-magnetic transfer = confirmed in the frozen j=1 realization;
- exact fixed-tangent channel-`00000` contraction `11/24` = confirmed;
- physical highest-contact leading coefficient `-216513/[8388608 rho^10 (rho^2+1)^10]` = confirmed nonzero for real `rho != 0`;
- joint distribution-product existence/nonexistence remains open;
- governance state unchanged.

## NEXT_ADMISSIBLE_GATE

Do not rerun V4 merely to repeat the same certificate. The next gate should be prospectively frozen and should increase information on the missing same-realization step beyond the fixed highest-contact tangent/channel witness.

Highest-value admissible directions are:

- a joint contact-distribution transversality/wavefront gate on the exact source realization, explicitly distinguishing `BLOCKED` from `FAIL`; or
- a stronger K5 contact-neighborhood/channel-coverage gate that broadens beyond one fixed tangent/channel without promoting a finite certificate to family closure.

Any such gate must preserve V3/V3K/source-version provenance, separately freeze the distribution-product object if used, and retain the current interpretation ceilings. No downstream terminal selector is authorized by this review.
