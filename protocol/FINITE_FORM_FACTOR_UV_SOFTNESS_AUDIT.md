# Finite-Parameter UV-Soft Form-Factor Audit

**Status:** comparator/control audit / no P4 credit.  
**KMQGB iteration:** 069.  
**Primary control:** Draper, Knorr, Ripken, Saueressig, *Finite Quantum Gravity Amplitudes: No Strings Attached*, Phys. Rev. Lett. 125, 181301 (2020).

## 1. Why this control matters

A common response to the KMQGB functional-freedom objection is to choose a finite-parameter analytic form factor that makes the UV behavior finite and then claim the finite parameter count as a parent principle.

The 2020 construction is an unusually clean test of this idea because it starts directly from a Lorentzian quantum effective action and gives explicit finite-parameter functions producing bounded high-energy scalar scattering.

## 2. Effective-action construction

The authors parameterize the gravitational quantum effective action using curvature form factors and matter interactions. In the gravity sector they choose

`f_R,C(Delta)=c_R,C G_N tanh(c_R,C G_N Delta)`

with positive parameters `c_R,c_C`; a further matter interaction scale controls the crossing-symmetric self-interaction contribution.

The resulting propagator contains the massless GR pole on the real momentum axis and an infinite complex/imaginary pole structure, while the full scalar scattering construction can be made bounded/scale-free at trans-Planckian energy.

## 3. A1 — no microscopic selector

The paper explicitly states that it does **not** connect the quantum effective action to a specific microscopic quantum-gravity model. Instead the effective action is parameterized and explicit form factors are chosen to realize desired UV properties.

Thus the relevant KMQGB classification is

`A1 BLOCKED__FORM_FACTOR_CHOSEN_NOT_DERIVED_FROM_MICROSCOPIC_PARENT`.

The object is a legitimate constructive effective model. The blocker is narrower: the `tanh` functional form is not itself derived from a lower-freedom microscopic law in the cited construction.

## 4. A2 — finite numerical parameters are not sufficient

Once the `tanh` ansatz is chosen, the displayed example has only a few numerical parameters, so its **internal fit dimension** is small.

However, the KMQGB A2 requirement asks whether the functional class itself is selected rather than chosen from a much larger allowed space.

The structural requirements

- no extra real-axis propagator poles;
- bounded/scale-free UV amplitudes;
- causality/unitarity constraints

do not uniquely select `tanh` among all possible admissible form factors.

Therefore the example is not evidence that the underlying parent-functional freedom has collapsed.

Classification:

`A2 LOW_PARAMETER_EXAMPLE__FUNCTION_CLASS_NOT_UNIQUELY_SELECTED`.

This distinction prevents an arbitrary function from being hidden behind a small number of parameters after one convenient basis function has been selected by hand.

## 5. A3 — registered comparator space

The construction is formulated in the quantum-effective-action/form-factor language and explicitly discusses its relation to EFT, Stelle gravity, infinite-derivative gravity and asymptotic-safety-type form factors.

KMQGB already registers

- quantum effective-action/form-factor completions;
- modern nonlocal/form-factor gravity;
- asymptotic-safety/spectral-RG architectures

as comparator spaces.

Hence even a future microscopic derivation of this exact `tanh` example would require a new physical relation beyond those comparator predictions before being called KG-specific.

Current classification:

`A3 COMPARATOR_CONTAINED__QEA_FORM_FACTOR_ASYMPTOTIC_SAFETY_NONLOCAL_SPACE`.

## 6. A4 scope

The cited explicit amplitudes concern gravity-mediated scattering of scalar matter, not a complete KMQGB four-graviton plus same-parent CTP hierarchy.

Thus

`A4 BLOCKED_IN_REQUIRED_HARD_GRAVITON_SCOPE`.

The scalar-scattering calculation remains valuable as a UV-softness and causal/unitary consistency control.

## 7. Search lesson

The audit freezes a useful rule:

> A finite number of coefficients multiplying a hand-selected function does not by itself satisfy the finite-parent-data requirement.

For a function-valued ingredient `F(z)`, a serious P4 candidate must provide at least one of:

1. a microscopic derivation of `F` from finite parent data;
2. a uniqueness/rigidity theorem showing the stated physical principles select `F` up to finite parameters;
3. a cross-representation relation that removes the otherwise arbitrary functional directions.

Without one of these, replacing an arbitrary function by `tanh`, `exp`, a rational Padé form, or another convenient finite-parameter family is ansatz selection rather than parent derivation.

## 8. Score consequence

- R1 unchanged;
- R2 unchanged;
- R3 externally controlled;
- R4 unchanged.

This audit does not add negative-taxonomy credit; it prevents a common false P4 promotion in the finite-form-factor branch.
