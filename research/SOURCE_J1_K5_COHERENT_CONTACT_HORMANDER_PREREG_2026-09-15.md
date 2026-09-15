# Preregistration — source j=1 K5 coherent-contact Hörmander gate

Date: 2026-09-15
Status: `PROSPECTIVELY_FROZEN`

## HYPOTHESIS

For the source coherent-state realization of the causal Toller wedge, the standard Hörmander sufficient criterion for multiplication of distributions fails at an explicit full-K5-collision point already for a three-wedge contact-term subproduct on one K5 triangle.

This gate tests only failure/satisfaction of the standard sufficient criterion. Failure of that criterion is **not** a proof that the product does not exist and is **not** a proof of non-uniqueness of the full source-defined vertex.

## SOURCE / REALIZATION AUTHORITY

Primary source: Bianchi, Chen and Gamonal, *Causal spinfoam vertex for 4D Lorentzian quantum gravity*, arXiv:2601.23162 / Phys. Rev. D 113, 126020 (2026).

Freeze the source coherent formulas:

- Eq. (17)/(35): the coherent Toller integrand contains `Theta_{sigma,rho,j}[B(z,g)]`;
- Eq. (32):
  `B(z,g) = log(<g^dagger z|g^dagger z>/<z|z>)`;
- Eq. (36):
  `Theta_{sigma,rho,j}[x] = theta(sigma x) + sigma delta^(rho,j)(x)`;
- Eq. (37): `delta^(rho,j)` is a finite sum of derivatives of `delta(x)`;
- Eq. (39): the coefficients come from the exact polynomial `F_j`.

Repository authority:

- `research/SOURCE_J1_TOLLER_COLLISION_POLE_LEDGER_2026-09-15.md`;
- `research/SOURCE_J1_FULL_COLLISION_ABSOLUTE_DIVERGENCE_THEOREM_2026-09-15.md`;
- `research/SOURCE_J1_FULL_COLLISION_SCALING_EXTENSION_AUDIT_2026-09-15.md`.

## OBJECT

Work at the compact full-collision base point with gauge-fixed vertex 1:

- `g_1 = I`;
- `g_a = exp(X_a . sigma / 2)` for `a=2,3,4,5`, evaluated to first order at `X_a=0`;
- normal coordinate space is therefore `R^12` with ordered coordinates `(X2x,X2y,X2z,X3x,X3y,X3z,X4x,X4y,X4z,X5x,X5y,X5z)`.

Freeze the K5 triangle edges

- `(12)`, `(23)`, `(13)`

and the same coherent spinor on those three independent wedge spinor factors,

- `z_12 = z_23 = z_13 = z0 = (1,0)^T`.

Its Bloch vector is frozen as

- `n(z0) = (0,0,1)`.

For edge `(ab)`, use the source group argument `g_ab = g_b^-1 g_a` and define `B_ab = B(z_ab,g_ab)`.

## EXACT LINEARIZATION TO BE TESTED

From source Eq. (32), at `g=I`:

- `B(z,I)=0` identically in `z`, hence `d_z B|_{g=I}=0`;
- for a pure boost perturbation `g(t)=exp(t H/2)` with Hermitian `H=h.sigma`,
  `d/dt B(z,g(t))|_0 = <z|H|z>/<z|z> = n(z).h`.

Therefore the frozen edge conormals in the 12 normal variables are predicted to be

`dB_ab = (e_a-e_b) tensor n(z_ab)`

with `X_1=0`.

The exact triangle-cycle relation to test is

`dB_12 + dB_23 - dB_13 = 0`.

No floating-point tolerance is permitted for this relation; all entries are integers/rationals.

## j=1 CONTACT CONTROL

For `j=1`, Eq. (39) freezes

`F_1(rho+sigma q,rho) = 1 + c1 (sigma q) + c2/2 (sigma q)^2 + c3/6 (sigma q)^3`,

with the exact coefficients to be algebraically verified:

- `c1 = (3 rho^2 + 1)/(rho(1+rho^2))`;
- `c2 = 6/(1+rho^2)`;
- `c3 = 6/(rho(1+rho^2))`.

Thus for real `rho != 0`, the `delta''(B)` coefficient in `delta^(rho,1)(B)` is predicted to be

`i/[rho(1+rho^2)] != 0`.

This control prevents a false transversality diagnosis based on a contact component absent from the frozen j=1 source object.

## WAVEFRONT / PRODUCT CRITERION

Use only the standard local fact for a submersion `B` that nonzero `delta^(n)(B)` contact terms have conormal wavefront directions proportional to nonzero real multiples of `dB` on `B=0`.

The standard Hörmander sufficient multiplication criterion requires that no selection of wavefront covectors from the factors at the same base point sum to zero.

The frozen three-edge test selects the nonzero j=1 `delta''(B)` contact component on each of `(12),(23),(13)`.

## POSITIVE CONTROLS

1. Exact Bloch vector of `z0` equals `(0,0,1)`.
2. `d_z B|_{g=I}=0` by exact source identity `B(z,I)=0`.
3. Exact `dB_12`, `dB_23`, `dB_13` each are nonzero 12-vectors.
4. Exact j=1 `c1,c2,c3` agree with the frozen formulas above.
5. The `delta''` coefficient is nonzero for a frozen symbolic assumption `rho != 0`.

## NEGATIVE / ADVERSARIAL CONTROLS

1. A forest pair, e.g. `(12),(13)`, must have linearly independent frozen conormals at `z0`; otherwise the implementation is invalid.
2. Replacing the third triangle edge `(13)` by a disjoint/non-cycle edge in the frozen check must not spuriously reproduce the same 3-edge integer relation.
3. No conclusion about product nonexistence is permitted from criterion failure alone.

## PASS

Classify

`SOURCE_J1_K5_COHERENT_CONTACT_HORMANDER_CRITERION_FAILS_SCOPED`

iff all positive/adversarial controls pass and the exact nontrivial relation

`dB_12 + dB_23 - dB_13 = 0`

is certified for three source-present nonzero `delta''(B)` contact components.

Interpretation ceiling of PASS:

- the textbook Hörmander sufficient product criterion cannot globally justify the naive coherent-contact three-wedge subproduct, hence cannot by itself justify the full ten-wedge coherent contact product across the full K5 collision;
- a stronger source-defined joint regulator/extension theorem is still required.

PASS does **not** imply product nonexistence, non-uniqueness of the final vertex, or closure of D7-S2.

## FAIL

Classify

`SOURCE_J1_K5_COHERENT_CONTACT_HORMANDER_TRANSVERSE_AT_FROZEN_WITNESS`

iff all controls are valid but the exact triangle cycle relation is nonzero.

## BLOCKED / INVALID

Classify `INVALID_SOURCE_REALIZATION` if the implementation does not use source Eq. (32), the frozen relative group orientation, or the exact j=1 contact coefficient.

Classify `BLOCKED_MICROLOCAL_AUTHORITY` if the conormal-product theorem needed for interpretation cannot be stated without adding unverified assumptions.

## CONSEQUENCE / NEXT GATE

On PASS, the next admissible source-order analytical gate is a prospectively frozen **joint Feynman regulator / extension gate** on the same fixed j=1 full-collision scope. It must distinguish:

- existence of a joint distributional limit;
- regulator path/order independence;
- collision-supported extension ambiguity;
- preservation of `T+ + T- = D` at the joint level.

No lower collision stratum is consumed here; Iter461 remains the independent partition stream.

## GOVERNANCE

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors remain forbidden.
- Candidate Gravity remains inactive.
- KMQGB remains downstream of the pinned DSIR authority; this gate changes no upstream object.
