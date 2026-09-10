# Nonlocal QG cross-order/full-momentum rigidity and material-branch audit — Iter249

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `NONLOCAL_QG`

## Question
Does the finite-parameter weak-field GF_N radial shape established in Iter232–248 remain an identifiable, realization-invariant physical shape after moving to full-momentum/on-shell observables and across perturbative order? Separately, which weakly-nonlocal action classes are materially inequivalent and therefore cannot share a family residual without an explicit map?

## Primary authorities
1. Donà, Giaccari, Modesto, Rachwał & Zhu, *Scattering amplitudes in super-renormalizable gravity*, arXiv:1506.04589. For gravity actions quadratic in Ricci/scalar curvature with weakly-nonlocal form factors, the on-shell four-graviton tree amplitude is Einstein's; a field-redefinition argument extends the equality to on-shell n-graviton tree amplitudes. Adding a genuinely Riemann-tensor form-factor operator (apart from the 4D Gauss–Bonnet exception) changes the amplitudes and makes them form-factor dependent.
2. Modesto & Calcagni, *Tree-level scattering amplitudes in nonlocal field theories*, arXiv:2107.04558. For the declared stable/unitary weakly-nonlocal class, tree-level n-point amplitudes agree with the underlying local theory, including nonlocal gravity with or without matter under the theorem's hypotheses.
3. Calcagni & Modesto, *Path integral and conformal instability in nonlocal quantum gravity*, arXiv:2402.14785. Supplies a Lorentzian path-integral/perturbative prescription with Efimov analytic continuation, but does not provide the same-realization loop-level full-momentum observable/error capsule needed here.

## Result 1 — the Iter248 weak-field shape is not a universal on-shell tree S-matrix fingerprint
For the Ricci/scalar form-factor subclass covered by the field-redefinition theorem, the off-shell/source weak-field response may depend on the nonlocal kernel while the on-shell tree S-matrix is exactly degenerate with GR. Therefore the GF_N radial profile must be treated as an observable/domain-specific object, not as a shape that can automatically be transported to an on-shell full-momentum scattering comparator.

Scoped disposition:
`PASS_SCOPE_GATE__RICCI_SCALAR_WEAKLY_NONLOCAL_TREE_ONSHELL_NPOINT_AMPLITUDES_REDUCE_TO_LOCAL_GR_UNDER_FIELD_REDEFINITION_THEOREM`.

This is neither a family PASS nor a family FAIL. It is an identifiability/reduction statement.

## Result 2 — material branches cannot be collapsed by the same theorem
The same primary authority explicitly separates actions containing a nontrivial Riemann-tensor form factor: their tree amplitudes depend on the form factors. Hence a minimum material census must distinguish at least:

- Ricci/scalar weakly-nonlocal actions inside the field-redefinition/equivalence class;
- Riemann/Weyl-form-factor actions outside that tree-amplitude reduction;
- IR inverse-d'Alembertian cosmological nonlocal models;
- ghost-free/infinite-derivative weak-field realizations with specified entire form factors;
- quantum-effective-action/nonlocal form-factor parameterizations derived or reconstructed by other dynamics.

No family-level residual may splice observables or errors between these branches without an explicit same-realization/equivalence certificate.

Scoped governance result:
`PASS_MATERIAL_BRANCH_SEPARATION_GATE__NONLOCAL_RICCI_SCALAR_TREE_EQUIVALENCE_CLASS_MUST_BE_SEPARATED_FROM_RIEMANN_WEYL_AND_IR_NONLOCAL_REALIZATIONS`.

## Result 3 — cross-order rigidity remains BLOCKED
The tree-level equivalence theorem does not supply the required loop-level same-realization object. The audited authority set does not provide a single fixed GF_N action with all of:

`full-momentum loop-corrected physical observable -> renormalization prescription -> same-realization parameter transport -> local/EFT nuisance quotient -> propagated truncation/analytic-continuation/remainder error -> common-domain comparator`.

The 2024 Lorentzian path-integral authority strengthens the prescription layer but does not close this observable/error chain. Absence here is bounded to the audited authority set through 2026-09-10 and is not a proof of nonexistence.

Disposition:
`BLOCKED_MISSING_REQUIRED_OBJECT__NONLOCAL_SAME_REALIZATION_LOOP_LEVEL_FULL_MOMENTUM_OBSERVABLE_PARAMETER_TRANSPORT_COMPARATOR_AND_PROPAGATED_ERROR_CERTIFICATE`.

## Consequence for functional rigidity
The strongest defensible conclusion is not that the GF_N shape is rigid across orders, and not that it fails. Instead:

`SCOPED_NONRIGID_IDENTIFIABILITY__WEAK_FIELD_OFFSHELL_SHAPE_DOES_NOT_DEFINE_AN_INDEPENDENT_TREE_ONSHELL_SMATRIX_SHAPE_IN_THE_RICCI_SCALAR_EQUIVALENCE_CLASS__LOOP_LEVEL_RIGIDITY_UNRESOLVED`.

This narrows the next search: loop-level work is decision-relevant only if it lives in the exact same action/branch and produces a physical observable not removable by the declared field redefinition/equivalence map.

## Family disposition
`NONLOCAL_QG` remains `PARTIAL_SUBFAMILY_ONLY`; family residual remains `UNDEFINED`; scientific family FAIL remains false. D2/D4 remain open and D7 remains `NOT_CLOSED`; `NEW_REQUIRED` is not authorized.

## Heavy compute
`IDLE`. The blocker is analytical/provenance/realization matching. A new numerical run without a fixed same-realization loop observable and prospective thresholds cannot change terminal classification.

## Next gate
`NONLOCAL_QG_RIEMANN_WEYL_FORM_FACTOR_BRANCH_FULL_MOMENTUM_OBSERVABLE_CAUSALITY_UNITARITY_AND_ERROR_CERTIFICATE`.

This branch has nontrivial tree-level amplitude dependence and therefore carries higher information gain than repeating GF_N static-potential calculations.