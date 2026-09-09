# KMQGB Recovery Delta 177

**Date:** 2026-09-10

CW2-02 / O-LQG has been converted from a latent-parameter RG condition into a direct observable-space transport equation.

From Iter176,

`gamma=-cot(4 psi)`

and

`Delta_gamma = 2 cot(8 psi) - q`,

with `q=(pi/8)(r+8 n_T)/Pi` after common-scale matching.

Differentiating with respect to RG time `t=ln(mu)` gives

`beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q`.

This is exactly equivalent to the gamma-space relation because

`beta_psi = beta_gamma/[4(1+gamma^2)]`.

For exact renormalized gamma-duality (`beta_Delta=0`), the observable-space tangency condition is

`beta_q + 16 csc^2(8 psi) beta_psi = 0`.

For controlled duality breaking,

`beta_q + 16 csc^2(8 psi) beta_psi = -beta_Delta_predicted`.

A crucial negative control follows: a running low-energy area-metric gamma/psi cannot consistently be combined with a frozen primordial q unless the matching flow predicts the resulting nonzero `beta_Delta`.

The strongest CW2-02 target can now be factored into

`MULTISCALE_GAMMA_CERTIFICATE = {M_same-realization, T_RG, C_observable}`

where

- `M_same-realization` proves EPRL -> area-metric provenance/parameter identity;
- `T_RG` predicts `beta_Delta` and transports the system between scales;
- `C_observable` is the fixed `(q,psi)` residual and transport equation.

Updated classification:

`PROMISING_ADAPT_EXISTING__MULTISCALE_GAMMA_FINGERPRINT_HAS_OBSERVABLE_RG_CLOSURE_EQUATION__SAME_REALIZATION_MAP_AND_BETA_DELTA_AUTHORITY_MISSING`.

Executable authority:

`code/lqg_multiscale_observable_rg_transport_reference.py`.

Audit authority:

`paper_iv/O_LQG_MULTISCALE_OBSERVABLE_RG_TRANSPORT_GATE_2026.md`.

CW2-02 remains OPEN; Closure Wave 02 remains `0/3`; Paper IV remains `NOT_YET_AUTHORIZED`.

No R1/R2/R3/R4 score change. Heavy detector compute remains idle.
