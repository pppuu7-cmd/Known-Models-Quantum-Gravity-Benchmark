# Cross-Background Rigidity

**Status:** frozen methodology / no Candidate Gravity promotion.  
**Purpose:** require one parent dynamics and one shared Wilson/parameter set to predict observables on physically different backgrounds, rather than fitting flat-space and curved-background sectors independently.

## 1. Motivation

Flat-space scattering does not exhaust the physical information carried by a gravitational parent. The same higher-curvature/nonlocal coefficients can affect

- Minkowski graviton scattering;
- black-hole entropy/extremality/thermodynamics;
- tidal response/quasinormal spectra;
- cosmological or other curved-background perturbations.

Using multiple backgrounds can create rigidity if the same parent parameters are genuinely shared.

This is not a new-theory certificate: ordinary EFT/string/asymptotic-safety parents also predict multiple backgrounds.

## 2. Shared parameter rule

Let `theta` denote parent dynamics/Wilson parameters common to all backgrounds `B_a`, with legitimate background-local nuisance/geometric parameters `psi_a`.

Predictions are

`c_a(theta, psi_a)`.

Forbidden: clone the same Wilson coefficient independently for Minkowski scattering and black-hole/cosmological backgrounds unless the parent theory itself contains background-dependent couplings.

## 3. Cross-background rank gain

Construct the honest shared Jacobian `J_BG,shared` and the diagnostic independently retuned Jacobian `J_BG,sep` exactly as in cross-representation rigidity.

Define

`R_BG = rank(J_BG,sep) - rank(J_BG,shared) >= 0`.

`R_BG>0` measures extra consistency directions created by requiring one parent parameter set across backgrounds.

## 4. Black-hole thermodynamic block

A prospective black-hole block may include physically invariant quantities such as

- Wald/generalized entropy corrections;
- mass-charge/extremality shifts where matter/charge is part of the declared model;
- surface-gravity/temperature relations;
- tidal response or quasinormal-mode data when derived in the same EFT/domain.

These observables must be computed in a curvature regime where the declared EFT/nonlocal expansion is valid.

Do not use the singular high-curvature core of a black hole as an EFT observable when curvature exceeds the cutoff.

## 5. Entropy/positivity guardrail

Thermodynamic monotonicity/entropy constraints are useful consistency tests, but they are not automatically independent of amplitude causality/positivity.

Known EFT examples show close agreement or overlap between black-hole/extremality consistency bounds and scattering positivity constraints.

Therefore the useful quantity is the **incremental post-comparator rank/information** added by the curved-background block, not the existence of an entropy inequality by itself.

## 6. Field-redefinition and observable invariance

Wilson coefficients in a redundant off-shell basis are not directly comparable across backgrounds.

Before stacking:

1. reduce to an agreed nonredundant/on-shell/EOM quotient where appropriate;
2. compare invariant scattering amplitudes and invariant thermodynamic/relational observables;
3. propagate any basis map consistently across every background block.

A coefficient mismatch created by changing field basis is not a physical residual.

## 7. Background-holdout design

A strong prospective split is

- training: selected flat-space scattering/helicity blocks;
- holdout: black-hole or cosmological observable predicted without retuning shared parent coefficients;

or the reverse.

Background-specific quantities such as mass, charge, spin or curvature scale are controlled design/background variables, not copies of the fundamental Wilson coefficients.

## 8. Comparator requirements

Apply the same background stack to any comparator that has authority in the domain:

- full C5 gravitational EFT;
- string/supergravity low-energy effective action;
- asymptotic-safety effective action where background calculations exist;
- modified-gravity/extra-DOF comparators.

A missing curved-background calculation for a comparator is `BLOCKED_MISSING_BACKGROUND_OBJECT`, not zero.

## 9. Relation to parent-principle search

Cross-background agreement can help distinguish two parents with similar flat-space amplitudes if they predict different curved-background relations.

However it does not solve the kernel-selection problem by itself. The parent principle must still derive the shared coefficients/functions prospectively.

## 10. Promotion status

Cross-background rigidity is a methodology/observable-design layer only. It does not change external Candidate Gravity readiness and does not promote an ansatz.