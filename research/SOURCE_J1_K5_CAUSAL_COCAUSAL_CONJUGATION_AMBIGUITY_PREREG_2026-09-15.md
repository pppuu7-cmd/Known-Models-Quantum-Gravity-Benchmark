# Preregistration — causal/co-causal conjugation-compatible collision ambiguity

Date: 2026-09-15
Status: `PROSPECTIVELY_FROZEN`

## HYPOTHESIS

Even after supplementing the already tested joint conditions with global wedge-sign reversal / complex-conjugation covariance motivated by the published Toller relations and by the causal/co-causal vertex pair, a nonzero collision-supported extension ambiguity remains.

The gate constructs an exact coefficient family `c(kappa)` for a real collision distribution `delta_N` such that

- the full `2^10` EPRL independent-sign sum is unchanged;
- K5 vertex-permutation covariance is exact;
- `c(-kappa)=conj(c(kappa))` for every independent wedge-sign pattern;
- the causal sector `C_+` and co-causal sector `C_-` receive nonzero conjugate shifts.

This is an adversarial uniqueness test. It does not claim that the published source explicitly imposes this coefficient-level conjugation law as its complete joint collision normalization.

## SOURCE AUTHORITY

Primary causal-vertex paper, Bianchi–Chen–Gamonal, arXiv:2601.23162 / Phys. Rev. D 113, 126020 (2026):

- Eq. (6): full EPRL vertex is the unconstrained sum over all independent wedge signs;
- Discussion item v: causal vertex `C_+` is the sum over `kappa_ab=sigma_a sigma_b`, while co-causal vertex `C_-` is the sum over `kappa_ab=-sigma_a sigma_b`; their nondegenerate Lorentzian semiclassical phases are opposite.

Published Toller companion, arXiv:2604.24945 / Phys. Rev. D 114, 046014 (2026):

- Eqs. (21)-(25): exact one-wedge complex-conjugation / sign-branch relations between the two Toller branches.

Repository authority:

- `research/SOURCE_J1_K5_EQ4_LOCAL_EXTENSION_EXISTENCE_RESULT_2026-09-15.md`;
- `research/SOURCE_J1_K5_COLLISION_COUNTERTERM_SUMRULE_RESULT_2026-09-15.md`;
- `research/SOURCE_J1_K5_ONE_WEDGE_UNIQUENESS_VS_JOINT_EXTENSION_RESULT_2026-09-15.md`.

## OBJECT

K5 has ten independent wedge signs `kappa in {+/-1}^10`.

Define

`C_+ = { kappa_ab=sigma_a sigma_b : sigma in {+/-1}^5 }`

as a set of distinct edge-sign patterns, and

`C_- = { -kappa : kappa in C_+ }`.

Freeze the collision-supported distribution `delta_N` to be real under complex conjugation and inside the already certified scaling window (`sd(delta_N)=12 <= 30`).

## FROZEN COEFFICIENT WITNESS

Use Gaussian-integer coefficients

- `c(kappa)=+i` for `kappa in C_+`;
- `c(kappa)=-i` for `kappa in C_-`;
- `c(kappa)=0` otherwise.

Target exact identities:

1. `C_+` has 16 distinct patterns.
2. `C_-` has 16 distinct patterns.
3. `C_+ intersect C_-` is empty.
4. The remaining noncausal set has `1024-32=992` patterns.
5. For every pattern, `c(-kappa)=conj(c(kappa))`.
6. Full EPRL counterterm sum is exactly zero.
7. Causal distinct-pattern shift is `+16 i`.
8. Co-causal distinct-pattern shift is `-16 i`.
9. If summed over all 32 sigma assignments, the shifts are `+32 i` and `-32 i` respectively because of global-reversal multiplicity two.
10. The coefficient family is invariant under all `5!` K5 vertex permutations.

## POSITIVE CONTROLS

- Enumerate all 1024 independent sign patterns exactly.
- Enumerate all 32 sigma assignments and verify 16 distinct `C_+` patterns, each multiplicity two.
- Construct `C_-` by exact global edge-sign reversal and verify disjointness.
- Verify the 992 complement count.
- Verify all `120*1024` permutation-pattern covariance checks.
- Verify all 1024 conjugation/sign-reversal checks.
- Verify exact Gaussian-integer EPRL and causal/co-causal sums.
- Verify `sd(delta_N)=12 <= 30`.

## ADVERSARIAL CONTROLS

1. A coefficient family supported only on `C_+` with real coefficient `+1` must fail `c(-kappa)=conj(c(kappa))`.
2. A uniform nonzero real coefficient on all 1024 patterns must fail the EPRL zero-sum condition.
3. The gate must not identify this coefficient covariance with a proof of the complete vertex-level conjugation theorem; it is only a stronger ambiguity witness compatible with the frozen sign-flip/conjugation structure.
4. The gate must not claim the witness is source-selected.

## PASS

Classify

`SOURCE_J1_K5_CAUSAL_COCAUSAL_CONJUGATION_STILL_LEAVES_COLLISION_AMBIGUITY_SCOPED`

iff all exact controls pass.

Interpretation ceiling:

- EPRL sign-sum preservation + K5 permutation covariance + same-scaling extension + global `kappa -> -kappa` complex-conjugation covariance still do not uniquely fix the causal collision extension;
- any source-canonical uniqueness condition must be stronger than these constraints used together.

PASS does **not** prove that the complete published causal/co-causal vertex relation leaves the same ambiguity after every boundary-index, rho, and magnetic-index transformation is imposed.

## FAIL

Classify

`SOURCE_J1_K5_CAUSAL_COCAUSAL_CONJUGATION_ELIMINATES_FROZEN_WITNESS`

iff the exact coefficient family fails any frozen identity above.

## BLOCKED / INVALID

`INVALID_CONJUGATION_PROMOTION` if coefficient-level `c(-kappa)=conj(c(kappa))` is promoted to a complete theorem about the full vertex without separately treating representation and boundary-index transformations.

## CONSEQUENCE

On PASS, the next joint-normalization search must look for a vertex-level condition stronger than:

- off-collision agreement;
- same scaling degree;
- EPRL sign sum;
- K5 permutation covariance;
- one-wedge Toller uniqueness;
- global edge-sign reversal / conjugation covariance at the coefficient level.

Candidate source-level constraints must act genuinely on collision-supported joint distributions.

## GOVERNANCE

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors forbidden.
- Candidate Gravity inactive.
- KMQGB remains downstream of pinned DSIR authority.
