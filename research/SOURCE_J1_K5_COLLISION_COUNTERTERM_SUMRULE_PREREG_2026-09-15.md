# Preregistration — K5 collision-counterterm ambiguity versus EPRL sum rule

Date: 2026-09-15
Status: `PROSPECTIVELY_FROZEN`

## HYPOTHESIS

The exact one-wedge identity `T+ + T- = D`, and hence the formal EPRL decomposition into all `2^10` independent wedge-sign sectors, does not by itself uniquely fix a local full-collision extension of the causal sectors.

Within the already certified full-collision scaling window, there exists an explicit permutation-invariant coefficient family for a collision-supported local counterterm `C delta_N` such that:

1. the sum of counterterms over all `1024` independent wedge-sign patterns is exactly zero, preserving the EPRL sign-sum relation;
2. every one of the `16` distinct constrained causal K5 patterns `kappa_ab=sigma_a sigma_b` receives the same nonzero shift;
3. the constrained causal sum therefore changes nontrivially.

This gate tests only the algebraic non-uniqueness left by the EPRL sign-sum constraint plus the previously established scaling-degree extension freedom. It does not assert that the published Eq. (4) has no further implicit source prescription.

## AUTHORITY

Source authority:

- Bianchi, Chen, Gamonal, *Causal spinfoam vertex for 4D Lorentzian quantum gravity*, Eq. (5): `T+ + T- = D`;
- Eq. (6): EPRL vertex as the unconstrained sum over all independent wedge signs `kappa_ab=+/-1`;
- the causal model uses the constrained subset `kappa_ab=sigma_a sigma_b`.

Repository authority:

- `research/SOURCE_J1_FULL_COLLISION_SCALING_EXTENSION_AUDIT_2026-09-15.md`: scoped full-collision scaling degree `30`, normal codimension `12`, allowed same-scaling collision-supported normal order through `18`;
- `research/SOURCE_J1_K5_ALL_CONTACT_CAUSAL_SIGN_RESULT_2026-09-15.md`: exactly `16` distinct constrained K5 edge-sign patterns from `32` vertex-sign assignments;
- `research/SOURCE_J1_K5_PUBLISHED_IEPSILON_SCOPE_RESULT_2026-09-15.md`: the published one-wedge `i epsilon` is not itself an explicit ten-wedge collision-regulator theorem.

## OBJECT

Use the `1024 = 2^10` independent K5 wedge-sign patterns.

Define the exact constrained subset

`C = { kappa : exists sigma in {+/-1}^5 with kappa_ab=sigma_a sigma_b }`.

Freeze the local collision-supported scalar counterterm shape as `delta_N`, where `N` is the full compact collision submanifold used by the scoped scaling-degree theorem. Only its coefficient bookkeeping is tested here.

Because `sd(delta_N)=codim(N)=12 <= 30`, a zeroth-normal-order `delta_N` term lies inside the already certified same-scaling extension ambiguity window. No derivative counterterms are needed for this witness.

## FROZEN COEFFICIENT FAMILY

Assign

- `c(kappa)=+63` for every `kappa in C`;
- `c(kappa)=-1` for every `kappa not in C`.

The preregistered arithmetic target is

`16*63 + 1008*(-1) = 0`.

Thus the full independent-sign EPRL sum of added counterterms vanishes exactly, while the constrained causal sum is

`16*63 = 1008 != 0`.

If summing over all 32 vertex-sign assignments rather than 16 distinct edge-sign patterns, global reversal gives multiplicity two and the corresponding shift is `32*63 = 2016 != 0`.

## POSITIVE CONTROLS

1. K5 has exactly ten edges.
2. There are exactly `1024` independent edge-sign patterns.
3. The constrained image of `sigma -> kappa` has exactly `16` distinct patterns.
4. Each constrained pattern has exactly two sigma preimages related by global reversal.
5. The complement has exactly `1008` patterns.
6. The frozen coefficient family is invariant under every permutation of K5 vertices, because membership in `C` is permutation invariant and coefficients depend only on membership.
7. Full independent-sign counterterm sum is exactly zero.
8. Distinct constrained-pattern counterterm sum is exactly `1008`.
9. Sigma-counted constrained counterterm sum is exactly `2016`.
10. `sd(delta_N)=12 <= 30`, so the witness counterterm does not exceed the already frozen scaling-degree ceiling.

## ADVERSARIAL CONTROLS

1. A uniform nonzero coefficient on all `1024` patterns must fail the EPRL zero-sum control.
2. Setting the constrained coefficient to zero must eliminate the causal shift and therefore must not satisfy PASS.
3. The implementation must verify permutation invariance by explicit enumeration of all `5! = 120` vertex permutations on all sign patterns.
4. No statement about a unique source-defined joint limit may be inferred from this algebraic ambiguity witness alone.

## PASS

Classify

`SOURCE_J1_K5_EPRL_SUMRULE_DOES_NOT_FIX_COLLISION_EXTENSION_SCOPED`

iff all exact controls pass.

Interpretation ceiling:

- the EPRL unconstrained sign-sum identity alone is insufficient to fix the collision-supported extension coefficients of the causal sectors;
- there exists an explicit nonzero causal-sector counterterm family that cancels identically in the full EPRL sign sum;
- therefore preserving Eq. (5)/(6) is not, by itself, a uniqueness condition for the causal full-collision extension.

PASS does **not** prove that the published causal vertex is nonunique after every possible source condition is imposed. A stronger joint source prescription could still fix the counterterm.

## FAIL

Classify

`SOURCE_J1_K5_EPRL_SUMRULE_FIXES_FROZEN_COUNTERTERM_WITNESS`

iff the exact implementation is valid but the frozen coefficient family does not preserve the EPRL sum or does not shift the constrained causal sector.

## BLOCKED / INVALID

`INVALID_EXTENSION_SCOPE` if `delta_N` is used outside the already certified scaling-degree window or if the implementation conflates the 16 distinct constrained edge patterns with the 32 sigma assignments.

## CONSEQUENCE

On PASS, `SOURCE_J1_K5_EQ4_IMPROPER_DISTRIBUTIONAL_EXISTENCE_GATE` must treat the following as insufficient uniqueness conditions when used alone:

- off-collision agreement;
- same scaling-degree ceiling;
- K5 permutation symmetry;
- exact EPRL independent-sign sum rule.

Any claimed unique causal collision extension must supply at least one additional source-faithful normalization/joint-limit condition that eliminates the explicit counterterm witness.

## GOVERNANCE

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal selectors forbidden.
- Candidate Gravity inactive.
- KMQGB remains downstream of pinned DSIR authority.
