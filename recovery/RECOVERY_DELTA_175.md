# KMQGB Recovery Delta 175

**Date:** 2026-09-10

Canonical chronology note: the area-metric bridge audit remains Iter174. The concurrently landed gamma-duality RG-tangency work is canonicalized here as Iter175. See `recovery/PROVENANCE_CORRECTION_ITER174_CONCURRENT_COLLISION.md`.

CW2-02 / O-LQG is now reduced to an exact RG-preservation condition.

Define

`rho = 2 f_GB^ren/f_CS^ren`,

`Delta_gamma = rho - (gamma - 1/gamma)`.

Then the gamma-dual surface is preserved under coarse-graining if and only if

`beta_Delta = beta_rho - (1+1/gamma^2) beta_gamma = 0`

on `Delta_gamma=0`.

For multiplicative Wilson flows and `gamma^2 != 1`:

`(gamma - 1/gamma)(eta_GB-eta_CS) = (1+1/gamma^2) beta_gamma`.

This yields three important conclusions:

1. gamma running does **not** by itself destroy the gamma-dual fingerprint;
2. gamma running is compatible with exact duality only if the parity-even/odd coefficient ratio runs in the exact required lockstep;
3. knowing `beta_gamma` alone, including the new area-metric flow from Iter174, is insufficient — the same realization must provide `beta_rho` or equivalent parity-sector Wilson flow.

The area-metric RG programme makes this gate concrete rather than hypothetical: it supplies a spin-foam-motivated running gamma tied to left/right non-length-sector imbalance, and reports freezing of the inverse-Immirzi flow in the decoupling limit. If the EPRL-to-area-metric same-realization map is later established, that limit gives a simple IR target `beta_gamma -> 0`, after which exact gamma-duality additionally requires `beta_rho -> 0`.

New decisive object:

`RG_COVARIANT_EPRL_TO_AREA_METRIC_GAMMA_MATCH`.

Required new quantity:

`beta_Delta`.

Updated classification:

`PROMISING_ADAPT_EXISTING__AREA_METRIC_GAMMA_FLOW_EXISTS__GAMMA_DUALITY_REDUCED_TO_SAME_REALIZATION_RG_TANGENCY__BETA_DELTA_MISSING`.

Executable authority:

`code/lqg_gamma_duality_rg_tangency_reference.py`.

Audit authority:

`paper_iv/O_LQG_GAMMA_DUALITY_RG_TANGENCY_GATE_2026.md`.

CW2-02 remains OPEN; Closure Wave 02 remains `0/3`; Paper IV remains `NOT_YET_AUTHORIZED`.

No R1/R2/R3/R4 score change. Heavy detector compute remains idle.
