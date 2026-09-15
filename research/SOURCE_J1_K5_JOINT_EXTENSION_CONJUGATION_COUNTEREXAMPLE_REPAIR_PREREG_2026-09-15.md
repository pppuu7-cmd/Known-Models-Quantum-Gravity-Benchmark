# Preregistration — source j=1 K5 joint-extension conjugation counterexample repair

Date: 2026-09-15
Status: `PROSPECTIVE_FROZEN`
Lane: KMQGB Research / Closure

## HYPOTHESIS

After the Critic-invalidated implementation of the previous joint-extension decision is repaired by propagating the exact representation-valued j=1 conjugation matrix through the actual fixed-channel K5 intertwiner contraction, the already-verified frozen constraints still possess a nonzero collision-supported homogeneous ambiguity.

Concretely, the hypothesis is that the channel-`00000` node intertwiner is exactly invariant under the four-leg `C` action induced by

`conj(T_plus) = C T_minus C`,

and that the coefficient family

- `+i` on the 16 constrained causal edge-sign patterns `kappa_ab=sigma_a sigma_b`,
- `-i` on their globally negated 16 patterns,
- `0` on the remaining 992 patterns,

multiplied by a real collision-supported zeroth-order `delta_N`, obeys the complete derived anti-linear fixed-channel covariance, K5 permutation symmetry, the full independent-sign EPRL zero-sum identity, and the certified same-scaling ceiling.

## exact OBJECT

The object is the homogeneous collision-supported ambiguity for the same source-order K5 realization already certified upstream:

- fixed `j=1`;
- fixed nonzero real `rho_e`;
- fixed intertwiner channel `00000`;
- ten K5 wedge/edge signs;
- full collision stratum `N=K^4`, `K=SU(2)`, inside `G^4`, `G=SL(2,C)`;
- zeroth-order real normal distribution `delta_N` with `sd_N(delta_N)=12`;
- exact channel-0 four-valent spin-1 intertwiner used by `code/iter499_arb_core.py`;
- exact j=1 conjugation matrix `C=[[0,0,1],[0,-1,0],[1,0,0]]` in the spherical magnetic basis.

This gate tests a homogeneous ambiguity kernel. It does not assert existence of a base joint extension. If a base extension satisfying the same constraints exists, adding a real multiple of any certified nonzero homogeneous solution produces another extension satisfying those tested constraints.

## DEPENDENCY

Frozen upstream dependencies:

1. Critic authority `recovery/CRITICAL_REVIEW_SOURCE_J1_K5_VERTEX_CONJUGATION_DERIVATION_2026-09-15.md`, commit `1a54df61c780eb44aeef56986d2481dcfdd55410`: previous terminal joint-extension decision is `INVALID_IMPLEMENTATION`, while the one-wedge map is retained as `CONFIRMED_SCOPED_SUBRESULT`.
2. Recovery reconciliation `recovery/KMQGB_RESEARCH_CLOSURE_SYNC_POST_CRITIC_2026-09-15.md`, commit `29ed9ba003e549623db237798836006907285f97`.
3. Exact retained one-wedge derivation in `research/SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_DERIVATION_COUNTERTERM_RESULT_2026-09-15.md`, historical result commit `181ca68f524fee5d9eab1c9501142d409cd02c2b`, used only for the Critic-retained sub-result `conj(T_plus)=C T_minus C`, rho unchanged.
4. Exact channel tensors in `code/iter499_arb_core.py`, specifically `_SUPPORTS[0]` for channel `00000`.
5. Full-collision scaling authority `research/SOURCE_J1_FULL_COLLISION_SCALING_EXTENSION_AUDIT_2026-09-15.md`: normal codimension 12, certified leading scaling degree 30, local same-scaling ambiguity order at most 18.
6. Prior EPRL-sign counterterm audit `research/SOURCE_J1_K5_COLLISION_COUNTERTERM_SUMRULE_RESULT_2026-09-15.md`, result commit `79b29ff4a3fcc0675a8d0f2958aff57310fdc20f`, used only as an upstream control that independent-sign sum rules and K5 permutation symmetry need not alone select a collision coefficient.

Iter504 run `34907349374` and Iter461 run `34748503239` are independent non-terminal streams and are excluded from this gate; no partial substantive values from them may be used.

## SOURCE / REALIZATION AUTHORITY

The authoritative realization is the repository-defined source-order j=1 K5 object above. The representation-valued anti-linear map is frozen from the Critic-retained exact derivation, not inferred from a sign-only shortcut. The channel-0 intertwiner coefficients are frozen exactly from the same repository contraction used in Iter499. Collision scaling/codimension are frozen from the reviewed repository scaling audit.

This gate is intentionally a repository-internal exact consistency theorem. It does not introduce a new physical prescription, regulator, normalization, model parameter, or source convention.

## FROZEN INPUTS

### Magnetic matrix

Use magnetic ordering `(-1,0,+1)` for the channel tensor and

`C_{m n}=(-1)^(1-m) delta_{m,-n}`,

i.e. the exact matrix

`[[0,0,1],[0,-1,0],[1,0,0]]`.

### Channel-0 intertwiner

Freeze exactly these nine nonzero components from `_SUPPORTS[0]`:

- `I(-1,+1,-1,+1)=+1/3`
- `I(-1,+1,0,0)=-1/3`
- `I(-1,+1,+1,-1)=+1/3`
- `I(0,0,-1,+1)=-1/3`
- `I(0,0,0,0)=+1/3`
- `I(0,0,+1,-1)=-1/3`
- `I(+1,-1,-1,+1)=+1/3`
- `I(+1,-1,0,0)=-1/3`
- `I(+1,-1,+1,-1)=+1/3`.

All other 72 components are zero.

### K5 signs

Freeze vertex set `{0,1,2,3,4}` and lexicographically ordered edges

`(01,02,03,04,12,13,14,23,24,34)`.

Enumerate all `2^10=1024` independent edge-sign patterns.

The constrained causal image is exactly

`C_plus={kappa: kappa_ab=sigma_a sigma_b, sigma_a in {+1,-1}}`.

Global sigma reversal gives the same edge pattern, so the expected cardinality is 16. Define `C_minus={-kappa: kappa in C_plus}`.

Freeze the Gaussian-integer coefficient witness

`c(kappa)=+i` for `kappa in C_plus`, `-i` for `kappa in C_minus`, and `0` otherwise.

Freeze `delta_N` as real, collision-supported, zeroth normal order, with scaling degree 12. The certified ceiling is 30.

### Exact checks

1. Compute all 81 components of `(C tensor C tensor C tensor C) I` by explicit exact-rational contraction and compare to `I`.
2. Derive, rather than hard-code, whether the fixed-channel scalar contraction absorbs all `C` matrices node-by-node. Exact four-leg node invariance is the required algebraic certificate.
3. Verify `C_plus` has 16 patterns, `C_minus` has 16, and their intersection is empty.
4. Verify for all 1024 patterns `c(-kappa)=conj(c(kappa))`.
5. Verify exact full independent-sign sum `sum_kappa c(kappa)=0`.
6. Enumerate all `5!=120` K5 vertex permutations and all 1024 patterns; verify coefficient invariance in all 122880 cases.
7. Verify the witness is nonzero and `sd(delta_N)=12 <= 30`.
8. Report the exact number of nonzero witness sectors and all check counts.

## POSITIVE CONTROLS

- Canonical `C` must leave all 81 channel-0 intertwiner components invariant exactly.
- `C_plus` must contain exactly 16 patterns with exactly two vertex-sign preimages each.
- `C_minus` must contain exactly 16 patterns and be disjoint from `C_plus` for K5.
- Anti-linear covariance, permutation invariance, EPRL zero-sum, nonzero support, and scaling-ceiling checks must all pass exactly.

## NEGATIVE CONTROLS

- Replace the central entry of `C` by `+1`, i.e. use `C_bad=[[0,0,1],[0,+1,0],[1,0,0]]`; this must fail exact channel-0 four-leg invariance on at least one of 81 components.
- A uniform nonzero coefficient on all 1024 sign patterns must fail the frozen independent-sign zero-sum condition.
- A coefficient supported only on `C_plus` with value `+i` must fail the frozen anti-linear relation under `kappa -> -kappa`.

Failure of any negative control makes the implementation `INVALID`.

## PASS

Classify

`SOURCE_J1_K5_FROZEN_CONJUGATION_CONSTRAINTS_LEAVE_NONZERO_COLLISION_AMBIGUITY_SCOPED`

iff all positive controls pass exactly, all negative controls fail in the preregistered way, the canonical four-leg `C` action is explicitly propagated through the channel-0 intertwiner, and the nonzero `c(kappa) delta_N` witness satisfies every frozen check.

Scientific meaning of PASS: the tested frozen constraints have a nontrivial homogeneous collision-supported kernel in this fixed j=1/channel-00000 scope. Therefore those constraints alone cannot imply uniqueness of a joint extension.

## FAIL

Classify

`SOURCE_J1_K5_TESTED_COLLISION_AMBIGUITY_ELIMINATED_BY_FULL_CONJUGATION_SCOPED`

iff the source-locked exact implementation is valid, the negative controls behave correctly, but the preregistered nonzero witness is eliminated by the complete representation-valued `C` propagation or another frozen exact constraint.

FAIL is only failure of this witness. It is not a proof that the joint extension is unique.

## BLOCKED / INVALID

Classify `SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_REPAIR_BLOCKED_SCOPED` if an authoritative dependency cannot be source-locked or the complete fixed-channel propagation cannot be evaluated.

Classify `INVALID_IMPLEMENTATION` if any substantive scientific predicate is hard-coded instead of computed, if sign-only covariance is substituted for the representation-valued `C` propagation, if any frozen input is changed after this preregistration, if a negative control does not fail as frozen, or if partial values from Iter504/Iter461 are consumed.

`BLOCKED` and `INVALID` are not scientific `FAIL`.

## INTERPRETATION CEILING

A PASS would prove only that the explicitly frozen, verified constraints — complete channel-00000 conjugation covariance, K5 permutation symmetry, the full independent-sign EPRL zero-sum identity, collision support, and the certified scaling ceiling — possess a nonzero homogeneous ambiguity in this scoped realization.

It would **not** prove:

- that a base joint Eq. (4) extension exists;
- that the published causal vertex is physically or globally nonunique;
- that the source selects this counterterm;
- that no additional source-faithful joint regulator, microlocal product theorem, normalization, boundary condition, or nested-stratum compatibility rule removes the ambiguity;
- any statement for other spins, channels, families, or lower collision strata;
- closure of D7-S2, D7-S3, or D7-S4;
- any terminal D7 selector;
- Candidate Gravity authority or any global quantum-gravity claim.

Historical FAIL/BLOCKED/INVALID results remain preserved.
