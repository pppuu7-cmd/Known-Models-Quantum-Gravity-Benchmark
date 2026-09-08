# P4 Functional-Freedom No-Go Filter

**Status:** permanent pre-P4 necessary-condition filter.  
**KMQGB iteration:** 059.  
**Purpose:** reject structural parent principles that leave an arbitrary hard gravitational function/tower even after all of their stated consistency conditions are imposed.

## 1. Motivation

Wave 38 exposed a recurring failure mode:

`structural consistency principle -> many admissible dynamics`.

This file converts that observation into a reusable hard test.

A P4 survivor is allowed a finite/low-dimensional set of physical parameters. It is **not** allowed to hide an arbitrary function, arbitrary spectral measure, or an independently tunable Wilson coefficient at every order behind a structural slogan.

## 2. Common-domain setup

Work only after the applicable full-C5 contribution and all required physical reductions are defined on the same observable domain.

Write the physical hard four-graviton object schematically as

`A4 = A4_C5,matched + DeltaA4`.

For one physical helicity/tensor sector, write an allowed candidate deformation as

`DeltaA4 = T_phys(1,2,3,4) F(s,t,u)`,

where

- `T_phys` is a gauge-invariant physical tensor/helicity structure;
- `F` carries the remaining invariant hard dependence;
- on massless 4-point kinematics `s+t+u=0`;
- crossing/permutation, analyticity/dispersion class, soft order and any other declared candidate conditions act as constraints on `F` and/or `T_phys`.

The notation is schematic and is not a claim that every gravity amplitude factorizes globally into one tensor times one scalar. The test applies sector by sector or to a vector of independent physical structures.

## 3. Structural-null deformation space

For a proposed parent principle `P`, define

`N_P = {delta A4 != 0 | every stated P-constraint remains satisfied by A4 + delta A4}`.

The constraints must include every property the proposal claims as its selector, for example:

- Lorentz/diffeomorphism-covariant physical Ward reduction;
- crossing/permutation symmetry;
- fixed leading soft theorem data;
- declared locality/nonlocality and analyticity class;
- causal support assumptions;
- any gluing/composition/duality/overlap conditions;
- any fixed lower-order matching data.

`N_P` measures the hard dynamical freedom invisible to the proposed principle.

## 4. No-go statement

### Functional-Freedom No-Go

If `N_P` contains an infinite linearly independent tower of admissible hard deformations, then `P` **cannot by itself satisfy KMQGB P4**.

Reason: P4 requires finite/low-dimensional free data and an explicit derivation of a nontrivial hard/cross-representation relation. Infinite-dimensional `N_P` means the principle leaves an arbitrary function/tower unfixed, so the hard dynamics is chosen rather than derived.

A finite nonzero `dim N_P` is not an automatic failure, but every surviving free direction must be explicitly declared as parent data and must remain shared across the relevant order/representation/background blocks.

`dim N_P = 0` on the declared physical domain is the strongest form of hard selection, but is not sufficient by itself: P5 comparator survival and P6 machine-record requirements still apply.

## 5. Constructive witness for failure

Suppose the claimed principle fixes covariance/Ward identities, crossing, a finite number of soft coefficients and an analytic `S-local` class, but does not fix all local higher-derivative contact data.

If an allowed physical contact structure `T_phys` exists, one may choose crossing-symmetric polynomials `p_n(s,t,u)` that vanish to sufficiently high soft order and define

`delta A4_n = c_n T_phys p_n(s,t,u)`.

For increasing derivative order, the family `{p_n}` can generate an unbounded tower while preserving the finite set of lower-order constraints. Then

`{delta A4_n} subset N_P`,

so `dim N_P` grows without bound and the principle fails P4 as a standalone selector.

The precise polynomial basis is helicity-, dimension- and parity-dependent. The no-go requires only one unbounded allowed tower, not a universal scalar basis for all sectors.

## 6. Why gravity EFT makes this filter nontrivial

Four-graviton EFT amplitudes admit higher-derivative corrections associated with operators such as `R^3`, `R^4` and higher-derivative descendants. Crossing and perturbative unitarity strongly constrain their coefficients but, absent stronger UV/microscopic assumptions, do not generically select a unique complete coefficient tower.

Representative evidence:

- Z. Bern, D. Kosmopoulos, A. Zhiboedov, *Gravitational Effective Field Theory Islands, Low-Spin Dominance, and the Four-Graviton Amplitude*, J. Phys. A 54 (2021) 344002, arXiv:2103.12728: four-graviton higher-dimension EFT coefficients are constrained by crossing/unitarity/dispersion and form restricted regions/islands rather than being fixed by those structural conditions alone.
- Y.-t. Huang, G. N. Remmen, *UV-complete gravity amplitudes and the triple product*, Phys. Rev. D 106 (2022) L021902: an infinite class of UV-complete four-graviton amplitudes can share the Einstein low-energy limit while differing in UV completion, illustrating that broad S-matrix health conditions need not select a unique parent.

These references are comparator evidence, not proof of the abstract statement; the proof is the existence of a nontrivial structural-null deformation family for the specific proposal under test.

## 7. Important caveat — bounds versus selection

Positivity, dispersion, Regge behavior, modularity, duality or other constraints can reduce `N_P` drastically.

They rescue a proposal only if the **full declared parent principle** actually fixes the remaining freedom to a finite low-dimensional set and derives the required hard relation prospectively.

Therefore:

- `allowed interval/island` is not yet unique parent selection;
- `functional equation with arbitrary boundary function` is not low freedom;
- `spectral representation with arbitrary positive rho(mu)` is not low freedom;
- `one free scale/coupling shared everywhere` may be acceptable if the rest is derived;
- a microscopic theory that fixes the complete tower is not rejected merely because its EFT expansion contains infinitely many terms.

The distinction is **infinite number of predictions** versus **infinite number of independent choices**.

## 8. Machine-friendly diagnostic

For any future P4 proposal, record

- `constraint_set_P`;
- `hard_basis_cutoff_D`;
- `allowed_basis_size_before_P`;
- `rank_of_P_constraints_at_D`;
- `nullity_NP_at_D`;
- whether `nullity_NP_at_D` stabilizes to a declared finite parent dimension or grows with `D`;
- cross-order/representation parameter incidence.

Define the finite-cutoff structural freedom count

`FF_D(P) = dim N_P(D)`.

Interpretation:

- if `FF_D` keeps growing as the EFT/hard basis cutoff is raised, classify `FUNCTIONAL_FREEDOM_BLOCKED`;
- if `FF_D -> k` with small declared finite `k`, the proposal may proceed to full P4 derivation audit;
- if the claimed microscopic object fixes those `k` parameters as well, proceed to P5 comparator survival.

`FF_D` is a prefilter, not a physical observable and not a replacement for global comparator profiling.

## 9. Immediate application to Wave 38 motifs

The new filter explains the common Wave38 failures:

- projector gluing without a projector-selection law leaves projector dynamics free;
- associativity/nonassociativity constraints without a microscopic product-selection law leave hard kernels free;
- generic UV/IR reciprocity without a unique spectral law leaves reciprocal functions/measures free;
- overlap-spectrum consistency without a Hamiltonian-selection law leaves many compatible dynamics free.

Known explicit microscopic theories can evade this no-go because the microscopic dynamics itself supplies the missing selector. Such theories then enter the ordinary P5 comparator test rather than being rejected for having rich low-energy expansions.

## 10. P4 gate update

Before spending substantial analytic or numerical effort on any new parent proposal:

1. construct the physical hard-basis deformation space at increasing cutoff/order;
2. impose the candidate's complete stated structural constraints;
3. compute or reason about `FF_D(P)`;
4. reject immediately if the surviving freedom grows without bound;
5. only if freedom is finite/low-dimensional demand the explicit 4-point/higher or cross-representation derivation required by P4.

This filter does **not** increase R4 by itself. It prevents false P4 promotion and makes the next constructive search substantially cheaper and more reproducible.
