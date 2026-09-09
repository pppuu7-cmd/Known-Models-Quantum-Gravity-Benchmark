# P4 Multi-Shift Contact Null-Space Gate

**Status:** exact scoped tree-amplitude prefilter.  
**KMQGB iteration:** 111.  
**Purpose:** test whether consistency among many complex-momentum recursions can remove the first-hard-datum ambiguity left by a single BCFW boundary term.

## 1. Setup

Let a physical tree amplitude admit several admissible complex deformations `S_alpha`. For each shift write schematically

`A_n = R_alpha[A_lower] + B_alpha`,

where

- `R_alpha` is the sum reconstructed from finite factorization poles under shift `alpha`;
- `B_alpha` is the boundary-at-infinity contribution.

Cross-shift consistency demands that all reconstructions yield the same physical `A_n`.

## 2. Local contact null space survives every shift

Let `C_n` be any local analytic on-shell contact amplitude with the declared helicity, crossing and derivative-order properties.

By definition `C_n` has no physical factorization poles. Therefore under every shift it contributes only through the polynomial/boundary part:

`A_n -> A_n + C_n`,

`B_alpha -> B_alpha + C_n(z->physical projection)`.

The shifted representations remain mutually consistent because the **same physical contact amplitude** is present in every reconstruction.

Thus

`agreement of many BCFW shifts`

does not by itself eliminate

`contact-amplitude null directions`.

## 3. Consequence at finite derivative cutoff

Let `C_D` denote the vector space of local generally covariant on-shell `n`-graviton contacts through derivative order `D` after on-shell identities/field redefinitions.

Cross-shift consistency alone leaves at least the allowed subspace

`N_multi-shift(D) subseteq C_D`

that obeys the candidate's helicity/crossing constraints.

As `D` grows, this space generically grows unless an independent degree/growth/order law truncates it.

Therefore multi-shift reconstruction does not solve the P4 functional-freedom problem by itself.

Classification:

`MULTI_SHIFT_CONSISTENCY__LOCAL_CONTACT_NULLSPACE_REMAINS`.

## 4. Two limiting cases

### Case A — one admissible shift has no boundary

If the candidate also has the same lower-point states and residues as GR, that shift reconstructs the ordinary GR tree amplitude in the constructible sector.

No new hard datum exists.

### Case B — all useful shifts retain a boundary

Additional shifts can constrain or recursively reconstruct parts of the boundary contribution. Boundary-recursion methods are legitimate computational tools.

But if a residual boundary operator/contact datum survives after all admissible shifts, that datum is precisely the missing irreducible hard input. Cross-shift consistency has located it, not physically selected it.

## 5. Nonlocal boundary branch

A non-polynomial/nonlocal boundary can evade the local contact statement, but then the candidate must independently derive

- its functional/sequence data;
- growth and singularity class;
- causal/unitary prescription;
- comparator escape.

It returns to the O1/O3 first-hard-datum problem rather than being solved by shift consistency.

## 6. Relation to boundary-operator literature

Boundary contributions in BCFW recursion can themselves be represented by boundary operators/form factors and can sometimes be recursively reduced using additional shifts.

That machinery supports the present distinction:

`multiple shifts can reconstruct/transport boundary information`

but

`reconstruction is not a physical origin law for the irreducible boundary operator`.

## 7. P4 rule

A multi-shift candidate may claim hard-seed selection only if

1. all declared admissible shifts are specified prospectively;
2. the common local contact null space is proven zero or finitely fixed by an independent physical degree/growth law;
3. any remaining nonlocal boundary data are finitely derived;
4. the result survives full C5 and UV comparator profiling;
5. the same parent supplies all-point and CTP/retarded completion.

## 8. Score consequence

No P4 credit. R4 remains 45%.