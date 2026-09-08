# Audit — State-Dependent Infinite-Derivative Gravity with Curvature-History Fields

**KMQGB ID:** `KMQGB-MOD-SDIDG-CURVATURE-HISTORY-2026`  
**Concrete source:** G. M. Rhythm, *A Covariant Curvature-History Field Formulation for State-Dependent Infinite-Derivative Gravity*, Annals of Physics 492 (2026) 170585 / arXiv:2608.20625.  
**Role:** modern structural comparator for E1/E2/E5 state-dependent nonlocal gravity; not promoted as quantum gravity.

## Frozen field content

The action-level description contains

`{g_mn, Phi, Delta_mn, C, chi}`,

where

- `g_mn` is the metric;
- `Phi` is ordinary matter;
- `Delta_mn` is a symmetric memory tensor;
- `C` is a curvature-history scalar;
- `chi` enforces the history equation variationally.

The history field obeys a hyperbolic sourced equation of the form

`(Box-m_c^2) C = - ell_* K`,

with `K=R_mnrs R^mnrs`, and a causal branch can be chosen using retarded boundary data.

The state-dependent nonlocality scale is a positive function

`M_eff^2 = M_eff^2(C) > 0`.

The memory-sector nonlocal form factor uses an ordered operator built from the spacetime-dependent scale and the covariant d'Alembertian.

## F0 — dynamics

`PASS_SCOPED`.

A covariant action and coupled Euler-Lagrange equations are explicitly given, including the auxiliary history fields and the noncommuting form-factor variation handled with Duhamel's formula.

## F1 — GR / low-curvature limit

`PARTIAL/PASS_SCOPED_STRUCTURE`.

The Einstein-Hilbert action is retained and the new memory/history sector is an additional modification. A complete phenomenological low-curvature matching to all required RQIR observables is not frozen here.

## F2 — consistency

### Bianchi / covariant conservation

`PASS_SCOPED_ON_SHELL`.

The memory and curvature-history stress tensors exchange energy-momentum, but their sum is covariantly conserved on shell. This is a real structural success.

### Spectrum / ghost freedom / stability

`BLOCKED_MISSING_REQUIRED_OBJECT`.

The paper explicitly does **not** prove ghost freedom, singularity resolution, full perturbative stability or a complete background spectrum.

Therefore Bianchi consistency must not be mistaken for full consistency.

## F3 — quantum/RQIR interface hierarchy

`BLOCKED_MISSING_QUANTUM_PARENT`.

The construction is a covariant modified-gravity effective framework. It does not provide the KMQGB-required quantum spin-2 CTP parent, ordered commutator hierarchy, full four-graviton quantum scattering block or relational quantum-channel object.

## F4 — comparator relation

The model is not a minimal metric-only E1 seed. Its extra fields place it in an E2/E5-type structural class as well as a state-dependent nonlocal E1 sector.

It is therefore a useful comparator against future claims such as

- “state-dependent nonlocality is new”;
- “retarded curvature memory guarantees quantum gravity”;
- “Bianchi-compatible variable nonlocal scale selects a unique kernel.”

None of those claims survive this comparator by themselves.

## F5 — hard discriminator / rigidity

`BLOCKED_ARBITRARY_FUNCTIONAL_FREEDOM`.

Although `C(x)` is dynamically and covariantly defined, the positive function `M_eff(C)` is not uniquely selected by the curvature-history principle alone.

Thus the model solves a **covariance/variational problem** for state dependence but does not solve the KMQGB **kernel-selection/rigidity problem**.

## F6 — identifiability

`NOT_REACHED`.

No common-domain robust comparator-subtracted quantum residual is available.

## F7 — resources

`NOT_REACHED`.

## Terminal KMQGB classification

`BLOCKED_QUANTUM_SPECTRUM_AND_KERNEL_RIGIDITY_COMPLETION`.

This is **not** a consistency FAIL of the published framework. The scoped Bianchi/conservation result is retained as PASS. The terminal block means only that the realization does not yet supply the quantum, spectral, rigidity and observable objects required for Candidate Gravity promotion.

## Candidate Gravity design lesson

A curvature-history auxiliary field is a concrete precedent for deriving a **state variable and retarded causal history** covariantly.

It does **not** by itself derive the nonlocal kernel. A future KG parent inspired by this route would still need

1. a principle fixing `M_eff(C)`/the operator kernel with very low freedom;
2. spectrum/ghost/causality analysis;
3. quantum CTP completion;
4. full C5/string/AS comparator profiling;
5. relational/scattering observables and exact kinematic lift.

Hence this model strengthens the distinction

`covariant state dependence != kernel rigidity != quantum-gravity novelty`.
