# Minimal E1 Vertex-Seed Specification — Pre-Ansatz Only

**Status:** exploratory structural specification / `BLOCKED` parent kernel / no Candidate Gravity ansatz promoted.  
**Purpose:** identify the smallest same-spin-2 nonlocal search object that is not immediately killed by Wave 16 while preserving the exact GR free pole structure.

## 1. Structural skeleton

Use a flat-background-compatible diffeomorphism-invariant parent of the schematic form

`S_skel = S_EH + (lambda/M^2) int sqrt(-g) V3[C, nabla; Phi_M]`,

where a representative cubic-curvature placement is

`V3 ~ C_mn^rs Phi_M(Box) ( C_rs^ab C_ab^mn )`.

This representative is **not yet the final parent action**.  Exact covariant operator ordering, kernel definition, CTP completion and boundary prescription remain mandatory missing objects.

The kernel `Phi_M` must be derived/frozen by a parent rule.  It may not be treated as an arbitrary function to be fitted after observing a residual.

## 2. Why the deformation starts beyond the propagator

Around Minkowski,

`C = O(h) + O(h^2) + ...`.

A regular cubic-curvature invariant begins at `O(h^3)`.  Therefore, provided the parent contains no hidden inverse-curvature or singular background dependence,

- the `O(h^2)` action is exactly Einstein-Hilbert;
- the free massless spin-2 pole/residue are unchanged;
- no additional propagator pole is introduced by this cubic seed itself.

This is a **structural two-point anchor**, not evidence of KG novelty.

## 3. Why the seed is not allowed to claim low-energy novelty

For a kernel analytic near the origin,

`Phi_M(Box) = phi_0 + phi_1 Box/M^2 + phi_2 Box^2/M^4 + ...`.

At `E << M`, each finite order maps to local curvature/derivative operators in gravitational EFT/C5.  In particular the leading local `C^3`/Riemann-cubed direction is an ordinary independent gravity-EFT operator, not a beyond-C5 certificate.

Hence **no low-energy Wilson coefficient from this seed may be called `DeltaGamma_KG`.**

Any potential distinction must involve a parent-fixed all-orders/cross-regime relation that cannot be reproduced by the matched C5 expansion in its valid domain and that survives a same-domain nonlocal/UV comparator.

## 4. On-shell nontriviality target

The search is placed in the Riemann/Weyl sector rather than an EOM-squared Ricci sector because published amplitude analyses show a key distinction:

- broad Ricci/scalar form-factor classes can be on-shell tree-equivalent to Einstein gravity by field redefinition;
- Riemann-sector form factors can alter graviton scattering amplitudes.

This establishes **where** an on-shell-nontrivial seed may live. It does not prove that this specific skeleton is nondegenerate.

## 5. First physical scattering block

For real asymptotically flat four-dimensional massless kinematics, use the **four-graviton tree amplitude** as the first physical scattering target rather than treating complexified three-point amplitudes as a direct observable residual.

At linear order in `lambda`, a complete four-point response must include, from the same parent,

1. the quartic contact obtained by expanding `V3` to `O(h^4)`;
2. exchange graphs containing one Einstein-Hilbert cubic vertex and one new `V3` cubic vertex in every required channel/orientation;
3. all gauge/contact completion required by the diffeomorphism Ward identity.

At higher order in `lambda`, graphs with two new cubic vertices and any other parent-required terms also enter.

No amplitude may be compared before this complete same-parent response is generated.

## 6. Cross-regime observable design

A useful future block should probe a dimensionless shape such as normalized helicity/crossing data over several kinematic points with

`E/M = O(1)`

while retaining lower-energy points as an EFT/IR anchor.

The same pair of shared parameters `(lambda,M)` — or fewer if the parent fixes one — must predict all points/configurations.  Independent per-energy form-factor coefficients are forbidden.

Prospective split idea:

- **training/anchor:** IR normalization and one cross-regime kinematic point;
- **holdout:** additional crossing-related energy/angle points or helicity channels predicted without shared-parameter retuning.

This is only an observable-design rule until the exact parent kernel exists.

## 7. Mandatory E1 taxes

Before any promotion, the exact seed must close all of:

1. **kernel derivation/rigidity** — `Phi_M` fixed from a parent principle, not arbitrary functional fitting;
2. **reality/CTP completion** — an in-in object defining retarded, symmetric and higher kernels consistently;
3. **causality** — front/retarded support, spacelike tails, no-signalling and global-causality/background audit;
4. **field-redefinition/on-shell equivalence** — prove the chosen Riemann/Weyl structure is not removable in the claimed observable sector;
5. **unitarity/analyticity** — no hidden unphysical poles/cuts or inconsistent residues in the declared domain;
6. **complete Ward response** — all contact/exchange families from the same parent;
7. **full C5 low-energy quotient** — every Taylor coefficient in the common EFT domain profiled correctly;
8. **same-domain nonlocal/UV comparator quotient** at `E ~ M`;
9. **cross-order/intervention/holdout rigidity**;
10. **nonzero COR + global separation**.

## 8. Current exact blocker

`PARENT_FIXED_KERNEL_DERIVATION = BLOCKED`.

Without a derivation selecting a specific low-parameter `Phi_M` and its Lorentzian/CTP prescription, choosing a convenient entire function would create an arbitrary functional ansatz and violate the rigidity principle.

## 9. Promotion status

`ANSATZ_PROMOTED = false`.

This file specifies the **next admissible search architecture**, not Candidate Gravity itself.
