# SYNTHESIS-004 — Finite 4↔5 Consistency Selector

**Status:** REJECTED as complete P4 origin law / retained higher-point rigidity control.  
**KMQGB iteration:** 087.  
**Purpose:** test whether a finite set of five-point soft/splitting/hidden-zero consistency relations can determine the first channel-irreducible four-graviton hard datum without inserting a microscopic parent.

## 1. Proposed selector

The attempted principle is:

> choose the four-graviton hard kernel that admits a five-graviton completion satisfying a fixed finite collection of factorization, soft and special-kinematic splitting relations with no independent higher-point freedom.

Higher-point consistency is attractive because it can impose nonlinear relations among lower-point Wilson coefficients rather than merely linear positivity bounds.

## 2. Positive control

Recent amplitude-bootstrap work shows that five-point splitting constraints can fix many five-point contact terms and impose nonlinear compatibility conditions on four-point EFT coefficients. This demonstrates that higher-point data can genuinely add rigidity.

A 2026 five-point partial-wave analysis also shows an important boundary: once both relevant channels permit spin-2 exchange, a genuine kernel can remain and additional higher-point input may be required.

Thus the mechanism is powerful but not generically complete.

## 3. Finite-locus null-deformation theorem

Suppose a finite collection of special-kinematic constraints is imposed on hypersurfaces

`L_i(kinematics)=0`, `i=1,...,N`.

Let `P_5` be any local contact polynomial/tensor compatible with the required permutation and helicity symmetries. Then

`Delta A5 = [prod_i L_i] P_5`

vanishes on every registered locus.

Therefore `A5` and `A5+Delta A5` obey exactly the same finite-locus splitting/zero data while differing away from the loci.

As the derivative/contact basis cutoff is raised, the admissible space of `P_5` grows unless another physical law, global boundedness condition, or all-kinematics functional identity removes it.

In KMQGB language, a finite list of locus constraints does not by itself force bounded `FF_D`.

## 4. Gravity-specific soft-contact witness

In flat background, an operator built schematically from five curvatures, such as a nonvanishing `Riemann^5`/`Weyl^5` invariant in an allowed helicity sector, has a pure five-graviton contact term in which each curvature contributes at least one linearized graviton.

If one external graviton momentum is `q -> 0`, its linearized curvature carries two powers of the soft momentum. Hence the pure five-point contact contribution scales at least as

`Delta A5_contact = O(q^2)`.

Such a term is invisible to the leading `O(q^-1)` and subleading `O(q^0)` universal soft-graviton data, and also evades any finite soft constraints that stop below its suppression order.

More generally, arbitrarily high-derivative generally covariant contact operators can be made increasingly soft while adding independent higher-point data.

Thus ordinary soft consistency does not select the full hard hierarchy.

## 5. A1/A2 verdict

The higher-point consistency map is explicit, but it still requires a rule fixing the null/contact directions that vanish on the imposed loci.

Classification:

- `A1 BLOCKED__FINITE_HIGHER_POINT_CONSTRAINTS_DO_NOT_SELECT_NULL_CONTACT_DIRECTIONS`;
- `A2 FAIL__CONTACT_FUNCTIONAL_FREEDOM_REAPPEARS_WITH_DERIVATIVE_ORDER`.

## 6. A3 comparator pressure

When enough special higher-point conditions do achieve strong rigidity, current positive controls frequently approach known string amplitudes. Hidden-zero/splitting constraints, Regge zeros and level-truncation/softness are already active string/S-matrix-bootstrap comparator architectures.

Therefore a future all-point consistency law must show why its constraint is a new physical gravitational law rather than a rediscovery of string/dual-resonant structure.

## 7. Reopen condition

Higher-point consistency can become a genuine parent only if the parent states an all-kinematics/all-order rule that removes the null contact directions from finite data, for example

`finite microscopic law -> complete n-point generator -> A4,A5,...`

with the same law also defining the Lorentzian/CTP continuation.

The selector must not be a finite checklist of soft/split loci whose complement can be filled by arbitrary contact terms.

## 8. Score consequence

No P4 credit. R4 remains 45%.