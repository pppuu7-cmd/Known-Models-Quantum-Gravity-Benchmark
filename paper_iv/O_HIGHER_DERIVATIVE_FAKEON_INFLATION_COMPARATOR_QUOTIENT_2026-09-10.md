# Higher-derivative fakeon inflation — leading comparator quotient

**Date:** 2026-09-10  
**KMQGB iteration:** 188  
**Parent family:** `PERTURBATIVE_HIGHER_DERIVATIVE`  
**RQIR Core:** v1.0 FROZEN

## Question

Does the leading inflationary tensor block of the fakeon `R+R^2+C^2` realization identify the fakeon quantization prescription, or is it already shared by the same quadratic action under other spin-2 quantizations?

## Frozen observable block

Use the leading slow-roll tensor observables

`O = (r, n_t)`

for the local quadratic action containing the Einstein term, the scalaron `R^2` term, and the Weyl-squared term. Define

`q = m_2^2 / m_0^2 > 0`,

where `m_0` is the scalaron mass and `m_2` the massive spin-2 scale.

The published leading-order relation is

`r(q,N_e) = 24/N_e^2 * q/(1+2q)`

and

`n_t = -r/8`.

For the fakeon Starobinsky/Weyl-squared realization, the quoted consistency condition `m_2 >= m_0/4` gives `q >= 1/16`, hence

`4/(3 N_e^2) <= r < 12/N_e^2`,

with the upper endpoint approached in the Starobinsky decoupling limit `m_2/m_0 -> infinity`.

## Primary literature authority

Buoninfante (2025), *Strict renormalizability as a paradigm for fundamental physics*, arXiv:2504.05900 / JHEP 07 (2025) 175, explicitly states that the leading slow-roll expression for `r` is **independent of the type of quantization used for the spin-two ghost**, and gives the formula above. The same discussion gives `n_t ~= -r/8` and the fakeon-specific lower mass bound.

The fakeon calculation itself is given in Anselmi, Bianchi and Piva (2020), arXiv:2005.10293, where the `R+R^2+C^2` fakeon realization yields `4/3 < N^2 r < 12` at leading order and the relation `r ~= -8 n_T` remains unchanged by the Weyl-squared term.

Dondarini (2023), arXiv:2306.04687, provides an additional warning that causal/fakeon projection issues can make apparently simple decoupling arguments singular in other inflationary realizations. This strengthens the decision to keep the current result strictly scoped to the published leading Starobinsky/Weyl-squared block.

## RQIR comparator logic

The correct attribution question is not whether the Weyl-squared term changes `r` relative to pure Starobinsky gravity. It does. The stricter question is whether the **fakeon prescription** is identified by this observable block.

Let `Q_f(q)` denote the fakeon leading map and `Q_a(q)` any same-action quadratic-gravity realization to which the published quantization-independent leading formula applies. Then, on the shared domain,

`Q_f(q) = Q_a(q) = (r(q), -r(q)/8)`.

Therefore the fakeon-attribution difference is exactly

`delta O_quantization = Q_f - Q_a = 0`.

For any covariance whitening and comparator projection that contains this same-action quantization direction,

`Pi_perp Sigma^(-1/2) delta O_quantization = 0`.

This is an **exact comparator identity for attribution to the quantization prescription in the declared leading block**. It is not a claim that the full quadratic action is observationally identical to Starobinsky gravity, nor that all higher-order fakeon predictions are identical to ghost/Lee-Wick/PT constructions.

## Executable control

Authority:

`code/higher_derivative_fakeon_inflation_comparator_reference.py`

The reference test:

- scans the fakeon domain beginning at `q=1/16` for representative `N_e` values;
- verifies exact equality of the fakeon and same-action quantization-independent leading maps;
- verifies `n_t + r/8 = 0`;
- verifies the lower fakeon boundary `r=4/(3N_e^2)`;
- verifies the large-`m_2` Starobinsky limit `r -> 12/N_e^2`;
- records zero comparator-orthogonal attribution residual in this block.

## Classification

**`PASS_RQIR_GATE__SCOPED_FAKEON_LEADING_INFLATION_QUANTIZATION_NONIDENTIFIABILITY`**

Residual classification:

**`EXACT_ZERO_FAKEON_ATTRIBUTION_RESIDUAL_AGAINST_SAME_ACTION_QUANTIZATION_COMPARATOR_IN_LEADING_R_NT_BLOCK`**.

This is a negative uniqueness result, not a scientific FAIL of the fakeon theory.

## What remains open

The result closes only the leading `(r,n_t)` attribution block. It does not close the parent family because the following can still carry prescription-sensitive information:

1. next-to-leading and higher slow-roll corrections and runnings;
2. detailed tensor spectral shape beyond the two-number leading block;
3. fakeon causal/nonlocal response and its characteristic scale;
4. resonance/width/peak observables associated with purely virtual propagation;
5. other backgrounds or scattering observables;
6. full comparison against Starobinsky plus complete local higher-curvature EFT, state, reheating/background and nuisance freedom;
7. terminal disposition of the non-fakeon material quantization branches.

## Refined next gate

The immediate fakeon discriminator is now narrowed to

`HIGHER_DERIVATIVE_FAKEON_BEYOND_LEADING_INFLATION_OR_CAUSAL_RESPONSE_COMPARATOR_CERTIFICATE`.

A future PASS for unique fakeon attribution must use an observable that changes with the quantization prescription itself, rather than only with the common local `C^2` action coefficient.

## D7 consequence

No family-level status changes. `PERTURBATIVE_HIGHER_DERIVATIVE` remains `PARTIAL_SUBFAMILY_ONLY`; the result contributes zero family-exclusion evidence toward `NEW_REQUIRED` and does not activate Candidate Gravity.
