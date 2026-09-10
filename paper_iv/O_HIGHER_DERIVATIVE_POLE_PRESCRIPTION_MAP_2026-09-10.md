# Higher-derivative quantum gravity pole-prescription map

**Date:** 2026-09-10  
**Iteration:** 187  
**RQIR authority:** Core v1.0 FROZEN  
**Parent family:** `PERTURBATIVE_HIGHER_DERIVATIVE`

## Purpose

Resolve the first half of the Iter186 blocker
`HIGHER_DERIVATIVE_POLE_PRESCRIPTION_FAMILY_MAP_PLUS_SAME_REALIZATION_CAUSALITY_OBSERVABLE_COMPARATOR_CERTIFICATE`
without letting one quantization prescription stand for the entire higher-derivative family.

## Fixed local action class

The common quadratic local gravity skeleton is taken schematically as

\[
S=\int d^4x\sqrt{-g}\left[-\frac{M_P^2}{2}R+a R^2+b R_{\mu\nu}R^{\mu\nu}+\cdots\right],
\]

with the equivalent Weyl-squared basis allowed.  The crucial RQIR distinction is not only the action coefficients but also the pole/quantization prescription applied to the additional massive modes.

## Material prescription map

### HD-P1 — ordinary Feynman/Stelle spin-2 pole

Authority: K. S. Stelle, *Renormalization of Higher-Derivative Quantum Gravity*, Phys. Rev. D 16 (1977) 953; D. Anselmi & M. Piva, *The Ultraviolet Behavior of Quantum Gravity*, JHEP 05 (2018) 027.

The four-derivative local action is power-counting renormalizable.  With the ordinary Feynman prescription, however, the additional massive spin-2 pole has the wrong-sign residue/negative-metric interpretation.  This is exactly the standard unitarity problem of Stelle gravity.

**RQIR scoped disposition:**
`FAIL_RQIR_GATE__SCOPED_STANDARD_POLE_POSITIVE_METRIC_UNITARITY`

Scope: ordinary Feynman quantization of the additional massive spin-2 pole.  This FAIL is not promoted to the whole higher-derivative family because alternative pole prescriptions change the physical state space.

### HD-P2 — fakeon / purely-virtual spin-2 prescription

Authorities:

- D. Anselmi & M. Piva, *Fakeons and Lee-Wick Models*, JHEP 02 (2018) 141, arXiv:1801.00915.
- D. Anselmi & M. Piva, *The Ultraviolet Behavior of Quantum Gravity*, JHEP 05 (2018) 027, arXiv:1803.07777.
- D. Anselmi & M. Piva, *Quantum Gravity, Fakeons And Microcausality*, JHEP 11 (2018) 021, arXiv:1806.03605.
- M. Piva, *Higher-Derivative Quantum Gravity with Purely Virtual Particles: Renormalizability and Unitarity*, EPJ Plus 138 (2023), arXiv:2305.12549.

The fakeon prescription removes the unwanted spin-2 mode from the asymptotic physical spectrum while retaining it virtually.  The cited construction supplies a perturbatively unitary, renormalizable gravity realization under this prescription.

However, the same theory predicts microscopic causality violation at energies above the fakeon mass.  Therefore the fakeon branch is **not** a causality PASS under the frozen KMQGB/RQIR funnel merely because its S-matrix is perturbatively unitary.  The causality feature must be carried explicitly into any same-realization observable certificate.

**RQIR scoped disposition:**
`PARTIAL_RQIR_CONTROL__FAKEON_RENORMALIZABILITY_UNITARITY_PASS__MICROCAUSALITY_NOT_CLOSED`

This is deliberately not labelled a family FAIL: whether the frozen causal gate is violated by the specific comparator-visible observable/domain must be demonstrated in the same realization and declared energy regime.

### HD-P3 — Lee-Wick-like / alternative contour prescriptions

Alternative complex-pole/contour prescriptions are materially different from both the ordinary Feynman ghost and the fakeon average-continuation prescription.  The fakeon literature explicitly distinguishes these constructions.  They cannot be silently represented by HD-P1 or HD-P2.

**RQIR status:** `BLOCKED_MATERIAL_PRESCRIPTION_REQUIRES_OWN_REALIZATION_CERTIFICATE`.

### HD-P4 — degenerate/scalar-only higher-curvature sectors

Special sectors such as pure `R+R^2` do not carry the same massive spin-2 pole structure.  They can be perfectly meaningful EFT/scalar-tensor models, but by themselves they do not inherit the full renormalizable four-derivative gravity claim of the generic quadratic action.  They therefore require either an explicit reduction to the GR/EFT comparator row in the tested domain or a separate UV-parent claim before they can affect Paper-IV family closure.

## What is now closed

The previous blocker asked first for a `pole_prescription_map`.  This component is now materially resolved at the level needed to prevent an invalid family-wide inference:

1. ordinary Feynman/Stelle ghost branch — scoped unitarity FAIL;
2. fakeon/purely-virtual branch — renormalizability/unitarity control exists, causality remains a same-realization hard question;
3. alternative Lee-Wick/contour branches — cannot be represented by the first two without an explicit map;
4. scalar-only/degenerate sectors — must be separated from the generic spin-2 higher-derivative UV claim.

## What remains open

The parent family remains `PARTIAL_SUBFAMILY_ONLY`.

The narrowed family blocker is:

`HIGHER_DERIVATIVE_REMAINING_PRESCRIPTIONS_PLUS_FAKEON_SAME_REALIZATION_CAUSALITY_OBSERVABLE_COMPARATOR_CERTIFICATE`

Minimum payload:

- one fixed fakeon gravity realization and mass convention;
- declared energy domain relative to the fakeon mass;
- normalized causality/time-response observable in that same realization;
- IR GR map;
- identical-domain GR/local-EFT comparator;
- approximation and error/remainder authority;
- explicit disposition/reduction of remaining materially distinct pole prescriptions.

## D7 consequence

This iteration adds a genuine scoped scientific FAIL, but **does not reduce the Tier-1 nonterminal count**.  `PERTURBATIVE_HIGHER_DERIVATIVE` remains nonterminal until the remaining material prescriptions and the fakeon same-realization causality/comparator object are resolved.

`BLOCKED != FAIL`; scoped FAIL != family exclusion; therefore D7 remains `NOT_YET_AUTHORIZED` and Candidate Gravity remains inactive.
