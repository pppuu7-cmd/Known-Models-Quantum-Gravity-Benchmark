# PF2-05A — Higher-derivative fakeon scoped same-realization audit

**Date:** 2026-09-10  
**Iteration:** 187  
**Parent family:** `PERTURBATIVE_HIGHER_DERIVATIVE`  
**RQIR Core:** v1.0 FROZEN

## Frozen realization

Scoped parent: four-dimensional local quadratic gravity in the `R + R^2 + C^2` class with the massive spin-2 pole quantized as a fakeon / purely virtual particle using the average-continuation prescription. The inflationary realization uses the same curvature-squared parent and the fakeon projection, with scalaron mass `m_phi` and spin-2 fakeon mass `m_chi`.

This record is intentionally narrower than a family verdict. It certifies that one materially defined quantization branch possesses a coherent package of: renormalizable higher-derivative dynamics, a perturbative-unitarity prescription, no spin-2 fakeon as an asymptotic external state, and explicit inflationary scalar/tensor observables. It does not certify ordinary microscopic locality/causality.

## Primary authorities

- D. Anselmi, *Fakeons and Lee-Wick Models*, arXiv:1801.00915.
- D. Anselmi, M. Piva, *Quantum Gravity, Fakeons And Microcausality*, arXiv:1806.03605.
- D. Anselmi, *Fakeons, Microcausality And The Classical Limit Of Quantum Gravity*, arXiv:1809.05037.
- D. Anselmi, E. Bianchi, M. Piva, *Predictions of quantum gravity in inflationary cosmology: effects of the Weyl-squared term*, arXiv:2005.10293.
- M. Piva, *Higher-Derivative Quantum Gravity with Purely Virtual Particles: Renormalizability and Unitarity*, arXiv:2305.12549.

Matched causality diagnostic control:

- J. D. Edelstein, R. Ghosh, A. Laddha, S. Sarkar, *Causality constraints in Quadratic Gravity*, arXiv:2107.07424.

## Accepted scoped statements

1. The fakeon prescription removes the massive spin-2 mode from the asymptotic spectrum while retaining it as a purely virtual mediator.
2. Within the cited perturbative construction, spectral/cutting identities provide the advertised perturbative-unitarity control and power-counting renormalizability is retained.
3. The inflationary `R + R^2 + C^2` realization yields explicit scalar/tensor fluctuation amplitudes and spectral indices; the construction requires `m_chi > m_phi/4` in the quoted analysis and gives a constrained tensor-to-scalar ratio.
4. The same fakeon programme predicts microscopic causality modification/violation above the fakeon scale. KMQGB therefore does **not** label this branch `ordinary_microcausality=PASS`.
5. A positive polarization-independent Shapiro time delay in the CEMZ shock-wave diagnostic for quadratic gravity is a distinct scoped causality control and does not erase the fakeon microcausality statement. The diagnostics refer to different notions/domains.

## RQIR classification

`PASS_RQIR_GATE__SCOPED_FAKEON_RENORMALIZABILITY_UNITARITY_INFLATION_OBSERVABLE_CONTROL`

Declared scope of PASS:

- fixed fakeon quantization prescription;
- perturbative renormalizability/unitarity control;
- existence of a normalized calculable inflationary observable sector;
- explicit declaration that ordinary microcausality is replaced/modified rather than silently assumed.

Not included in the PASS:

- global causal acceptability of the fakeon branch;
- proof that its inflationary predictions contain a comparator-orthogonal quantum-gravity residual after a complete Starobinsky + local-EFT + state/nuisance comparator fit;
- proof that Lee-Wick, PT/modified-inner-product, Euclidean OS, or other higher-derivative branches reduce to this realization;
- family-level sufficiency or exclusion.

## Comparator status

The obvious same-domain controls include Starobinsky `R+R^2` inflation and the complete applicable local higher-curvature EFT/state/nuisance family. The cited fakeon inflation papers provide explicit predictions, but KMQGB has not yet frozen a full comparator-manifold fit proving a nonzero comparator-orthogonal residual.

Therefore this scoped object records a **defined positive construction control**, not a unique-QG residual.

## Next fakeon gate

`HIGHER_DERIVATIVE_FAKEON_INFLATION_FULL_COMPARATOR_QUOTIENT_PLUS_CAUSAL_REPLACEMENT_CERTIFICATE`

Minimum payload:

- exact fakeon inflation realization and parameters;
- scalar/tensor observable vector and covariance/domain;
- Starobinsky and complete same-order local-EFT comparators;
- nuisance/state/background parameter incidence;
- fakeon causal-replacement domain and validity conditions;
- comparator projection/global profiling result;
- holdout observable not used for parameter tuning;
- uncertainty/remainder ledger.

## D7 firewall

This child PASS does not change the parent `PERTURBATIVE_HIGHER_DERIVATIVE = PARTIAL_SUBFAMILY_ONLY`, does not count as family exclusion, and does not activate Candidate Gravity.
