# V8 implementation protocol — derivative-contact counterterm equivalence

Date: 2026-09-16
Status: PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION_OR_RESULT
Gate: `SOURCE_J1_K5_TRIANGLE_DERIVATIVE_CONTACT_COUNTERTERM_EQUIVALENCE_GATE`
Parent preregistration commit: `38054879237dd03e9d368ceb47356e669c02b516`

This supplement only makes the already-frozen V8 mathematical construction executable. It does not change the parent scientific question, classification taxonomy, controls, or interpretation ceiling.

## Exact object and finite local class

Use the same local normal coordinates as repaired V7:

- `B12=x`,
- `B23=y`,
- `B13=x+y` (equivalently the sign-insensitive root `-x-y` for the even `delta''` contact).

The three one-dimensional `delta''` factors have local scaling degree `3+3+3=9` on a two-dimensional normal space, so the point-supported extension freedom has derivative order at most `9-2=7`.

Start from the complete jet class

`sum_{i+j<=7} c_ij partial_x^i partial_y^j delta_(0,0)`.

Do not hand-select a smaller basis. Construct the six triangle-permutation coordinate matrices from the root triple `(x,y,-x-y)`, induce the dual action on derivative symbols, and solve exact rational invariance equations degree by degree for `d=0,...,7`. The resulting invariant-basis dimensions themselves are decision-audited output. No basis element may be added or removed after execution.

## Action on the frozen Gaussian family

For widths `(a,b,c)`, use the centered Gaussian test

`phi_(a,b,c)(x,y)=exp[-a x^2-b y^2-c(x+y)^2]`.

For every homogeneous invariant jet symbol of even derivative order `d=2m`, compute its exact distributional action on `phi` and divide by `(a+b+c)^m`. This quotient is the frozen scale-free local-counterterm action and must satisfy exact common-rescaling invariance between V7 schemes A `(1,1,1)` and A4 `(4,4,4)`.

Odd-order derivatives of this centered even Gaussian vanish exactly. They remain in the complete invariant jet basis and must be reported as zero-action columns rather than deleted post hoc.

All derivative actions are computed directly from the exact Taylor coefficients of the quadratic Gaussian with `fractions.Fraction`; no floating decision path is allowed.

## Equivalence linear system — frozen before result

The counterterm is allowed to shift the common finite normalization. Therefore the scientific equivalence condition is equality of the corrected scheme values, not an extra requirement that the counterterm action vanish on scheme A.

Let `K_s` be the frozen repaired-V7 diagnostic and `M_s` the row of normalized local-jet actions for scheme `s`. Solve exactly

`(M_s-M_A) c = K_A-K_s`

for `s in {A4,B,C}`.

Adding the extra equation `M_A c=0` would impose a new renormalization condition not supplied by the V8 preregistration or source authority and is forbidden in this gate.

Report exact rank, augmented rank, nullity, one canonical RREF solution (free variables set to zero), the complete affine nullspace basis, and the corrected common value for the canonical solution when one exists.

## Frozen source-authority interpretation

The companion authority ledger `inputs/source_j1_k5_triangle_derivative_contact_counterterm_authority_v8.json` is frozen in the same pre-implementation commit. It enumerates the immutable V4/V5/V7/V8 authority corpus by blob SHA and records, before the solve, whether any prior authority affirmatively fixes numerical coefficients for this finite collision-supported jet class.

Do not infer authority from a single missing prose literal. Runtime source locking must verify every listed blob SHA and the positive scope facts consumed from the corpus. The ledger's prospective coefficient-authority status is then consumed by the classifier.

Classification after exact controls:

- exact solvability + all finite coefficients source-fixed uniquely -> `SOURCE_FIXED_UNIQUE_SCOPED`;
- exact solvability + at least one admissible finite coefficient/source normalization unfixed -> `SOURCE_UNFIXED_FINITE_LOCAL_FREEDOM_SCOPED`;
- augmented-rank obstruction -> `COUNTERTERM_CLASS_INSUFFICIENT_SCOPED`;
- inability to construct/authorize the frozen class from the locked authority corpus -> `MISSING_AUTHORITY_BLOCKED`;
- failed provenance, completeness, symmetry, synthetic fixtures, lane agreement, or exact controls -> `INVALID_IMPLEMENTATION`.

## Frozen controls

In addition to the parent preregistration controls:

1. exact invariant-space completeness is checked by the nullity of the full degree-by-degree permutation-invariance constraint matrix;
2. every emitted basis vector is re-substituted through all six dual permutation actions;
3. A4 and A counterterm-action rows must match exactly;
4. all odd-order basis columns must act as exact zero on every frozen centered Gaussian scheme;
5. a synthetic in-span fixture is generated from the fixed coefficient vector `(1,2,...,n)` and must solve exactly;
6. a synthetic outside-span fixture is fixed as a scheme-difference vector with A4-A component `1` and all other components `0`; it must be rejected because common-rescaling invariance forces every admissible column to have A4-A component `0`;
7. the four V7 `K` values must reproduce byte-for-byte as exact rational strings before the counterterm solve.

## Interpretation ceiling

This gate tests only whether the repaired-V7 **finite set of Gaussian scheme differences** lies in the action span of the prospectively frozen S3-invariant local jet class and whether prior authority fixes that finite freedom. It is not an all-mollifier theorem, not a distributional-extension existence/nonexistence theorem, not a full-K5 theorem, not model/family failure, not D7 closure, and not a terminal selector or Candidate Gravity authority.
