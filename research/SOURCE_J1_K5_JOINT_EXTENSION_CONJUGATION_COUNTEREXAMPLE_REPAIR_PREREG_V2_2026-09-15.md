# Preregistration v2 — source j=1 K5 joint-extension conjugation counterexample repair

Date: 2026-09-15
Status: `PROSPECTIVE_FROZEN`
Supersedes before computation: v1 commit `b194a6d4b56f93eabb982fd3af7f7da93d0a068b`, withdrawn by `research/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_PREREG_V1_WITHDRAWAL_2026-09-15.md` at commit `6dedf5e02b63147420f2ebf5fb7abd99499095fd` because its negative control was structurally non-adversarial. No v1 certificate/workflow/result was executed.

## HYPOTHESIS

After repairing the Critic-invalidated implementation by propagating the exact representation-valued j=1 conjugation matrix through the actual fixed-channel K5 intertwiner contraction, the already-verified frozen constraints still possess a nonzero collision-supported homogeneous ambiguity.

Specifically, the channel-`00000` node intertwiner is hypothesized to be exactly invariant under the four-leg action induced by `conj(T_plus)=C T_minus C`, and the coefficient family `+i` on constrained causal patterns, `-i` on their global negatives, and `0` elsewhere, times a real `delta_N`, is hypothesized to satisfy the complete derived anti-linear fixed-channel covariance, K5 permutation symmetry, the independent-sign EPRL zero-sum identity, and the certified scaling ceiling.

## exact OBJECT

Same source-order K5 realization as the reviewed collision theorem:

- fixed `j=1` and nonzero real `rho_e`;
- fixed intertwiner channel `00000`;
- ten K5 edge signs;
- full collision stratum `N=K^4`, `K=SU(2)`, in `G^4`, `G=SL(2,C)`;
- real zeroth-order collision distribution `delta_N`, `sd_N(delta_N)=12`;
- exact channel-0 spin-1 four-valent intertwiner from `code/iter499_arb_core.py`;
- exact j=1 matrix `C=[[0,0,1],[0,-1,0],[1,0,0]]`.

The object tested is a homogeneous ambiguity kernel, not existence of a base extension. Conditional on any base extension satisfying the same constraints, a nonzero homogeneous solution yields a distinct real one-parameter family by addition of `lambda Delta`, `lambda in R`.

## DEPENDENCY

Frozen repository authorities:

1. Critic `recovery/CRITICAL_REVIEW_SOURCE_J1_K5_VERTEX_CONJUGATION_DERIVATION_2026-09-15.md`, commit `1a54df61c780eb44aeef56986d2481dcfdd55410`: previous joint-extension decision is `INVALID_IMPLEMENTATION`; exact one-wedge map retained as `CONFIRMED_SCOPED_SUBRESULT`.
2. Recovery reconciliation `recovery/KMQGB_RESEARCH_CLOSURE_SYNC_POST_CRITIC_2026-09-15.md`, commit `29ed9ba003e549623db237798836006907285f97`.
3. Historical derivation result `research/SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_DERIVATION_COUNTERTERM_RESULT_2026-09-15.md`, commit `181ca68f524fee5d9eab1c9501142d409cd02c2b`, used only for the Critic-retained exact sub-result `conj(T_plus)=C T_minus C`, rho unchanged.
4. `code/iter499_arb_core.py`, exact `_SUPPORTS[0]` channel tensor.
5. `research/SOURCE_J1_FULL_COLLISION_SCALING_EXTENSION_AUDIT_2026-09-15.md`: codimension 12, leading scaling degree 30, same-scaling local ambiguity order at most 18.
6. `research/SOURCE_J1_K5_COLLISION_COUNTERTERM_SUMRULE_RESULT_2026-09-15.md`, commit `79b29ff4a3fcc0675a8d0f2958aff57310fdc20f`, only as the prior exact EPRL/permutation counterterm control.

Iter504 run `34907349374` and Iter461 run `34748503239` are independent non-terminal streams and excluded; no partial substantive values may be consumed.

## SOURCE / REALIZATION AUTHORITY

The repository-defined source-order fixed-j=1/channel-00000 object is authoritative. The anti-linear map is the Critic-retained representation-valued map, not a sign-only assumption. The intertwiner is exactly the same channel tensor used by the validated Iter499 contraction. Scaling/codimension are inherited only from the reviewed full-collision audit. This gate adds no regulator, normalization, parameter, source convention, or physical model datum.

## FROZEN INPUTS

Magnetic ordering is `(-1,0,+1)`. Freeze

`C_{mn}=(-1)^(1-m) delta_{m,-n}` = `[[0,0,1],[0,-1,0],[1,0,0]]`.

Freeze the nine nonzero channel-0 components:

`I(-1,+1,-1,+1)=+1/3`, `I(-1,+1,0,0)=-1/3`, `I(-1,+1,+1,-1)=+1/3`,
`I(0,0,-1,+1)=-1/3`, `I(0,0,0,0)=+1/3`, `I(0,0,+1,-1)=-1/3`,
`I(+1,-1,-1,+1)=+1/3`, `I(+1,-1,0,0)=-1/3`, `I(+1,-1,+1,-1)=+1/3`; all other 72 components zero.

K5 vertices are `{0,1,2,3,4}` and ordered edges `(01,02,03,04,12,13,14,23,24,34)`. Enumerate all 1024 sign patterns. Define `C_plus={kappa_ab=sigma_a sigma_b}` over all 32 vertex-sign assignments; global reversal is expected to reduce this to 16 distinct patterns. Define `C_minus={-kappa:kappa in C_plus}`.

Freeze Gaussian-integer coefficients `c=+i` on `C_plus`, `c=-i` on `C_minus`, and `c=0` otherwise. Freeze real `delta_N` with scaling degree 12 and certified ceiling 30.

The implementation must compute, not hard-code, the following:

1. all 81 exact-rational components of `(C tensor C tensor C tensor C)I` versus `I`;
2. whether this exact node identity permits all representation-valued `C` actions to be absorbed in the complete fixed-channel scalar K5 contraction;
3. cardinalities/preimages of `C_plus` and `C_minus` and their intersection;
4. all 1024 relations `c(-kappa)=conj(c(kappa))`;
5. exact `sum_kappa c(kappa)`;
6. all `120*1024=122880` K5 vertex-permutation coefficient checks;
7. nonzero witness support and `12<=30`;
8. exact pass/fail counts.

## POSITIVE CONTROLS

- Canonical `C` must leave all 81 channel-0 tensor components invariant exactly.
- `C_plus` must contain 16 distinct patterns, each with two vertex-sign preimages; `C_minus` must contain 16 and be disjoint from `C_plus`.
- Anti-linear covariance must hold for all 1024 patterns.
- All 122880 permutation checks must pass.
- Full independent-sign coefficient sum must be exactly `0+0i`.
- Witness support must be nonzero and `sd(delta_N)=12<=30`.

## NEGATIVE CONTROLS

Freeze the deliberately asymmetric reversal matrix

`C_bad=[[0,0,1],[0,-1,0],[-1,0,0]]`,

which differs from canonical `C` only by flipping the `(+1,-1)` matrix entry. Its four-leg action must fail equality with the channel-0 tensor on at least one of 81 components.

Additionally:

- uniform coefficient `+1` on all 1024 patterns must fail the independent-sign zero-sum condition;
- coefficient `+i` on `C_plus` and zero elsewhere must fail `c(-kappa)=conj(c(kappa))` for at least one pattern.

If any negative control fails to be adversarial as frozen, the implementation is `INVALID_IMPLEMENTATION`.

## PASS

Classify

`SOURCE_J1_K5_FROZEN_CONJUGATION_CONSTRAINTS_LEAVE_NONZERO_COLLISION_AMBIGUITY_SCOPED`

iff every positive control passes exactly, every negative control is adversarial as frozen, canonical four-leg `C` is explicitly propagated through channel `00000`, and the nonzero `c(kappa) delta_N` witness satisfies every frozen exact constraint.

PASS means only that the tested frozen constraints have a nontrivial homogeneous collision-supported kernel in this fixed scope; they therefore cannot by themselves prove uniqueness of a joint extension.

## FAIL

Classify

`SOURCE_J1_K5_TESTED_COLLISION_AMBIGUITY_ELIMINATED_BY_FULL_CONJUGATION_SCOPED`

iff source-lock and implementation are valid, negative controls behave correctly, but the preregistered witness is eliminated by complete representation-valued `C` propagation or another frozen exact constraint.

FAIL is failure of this witness, not a uniqueness theorem.

## BLOCKED / INVALID

Classify `SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_REPAIR_BLOCKED_SCOPED` if an authoritative dependency cannot be source-locked or complete fixed-channel propagation cannot be evaluated.

Classify `INVALID_IMPLEMENTATION` if a substantive scientific predicate is hard-coded instead of computed, sign-only covariance substitutes for representation-valued propagation, any v2 frozen input is changed after this commit, a negative control is not adversarial as frozen, or partial Iter504/Iter461 values are consumed.

`BLOCKED` / `INVALID` are not scientific `FAIL`.

## INTERPRETATION CEILING

PASS would prove only that complete channel-00000 conjugation covariance, K5 permutation symmetry, full independent-sign EPRL zero-sum, collision support, and the certified scaling ceiling admit a nonzero homogeneous ambiguity in this scoped realization.

It would not prove base-extension existence; published-vertex physical/global nonuniqueness; source selection of the witness; absence of any additional source-faithful regulator, microlocal product theorem, normalization, boundary condition, or nested-stratum compatibility condition that removes it; any statement for other spins/channels/families/lower strata; closure of D7-S2/S3/S4; any terminal D7 selector; Candidate Gravity authority; or any global quantum-gravity claim.

Historical FAIL/BLOCKED/INVALID records remain preserved.
