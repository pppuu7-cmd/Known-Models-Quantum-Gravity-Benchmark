# 4D CDT continuum / scale-setting authority sweep — Iter224

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `CDT_EDT`  
**Branch:** four-dimensional CDT  
**Gate:** `CDT_4D_CONTINUUM_RG_TRAJECTORY_LATTICE_SCALE_INVARIANT_OBSERVABLE_COMPARATOR_CLOSURE`

## Question

After the Iter200 observable closure, does current 4D CDT authority now provide the missing same-realization continuation

`critical/UV trajectory -> line of constant physics -> lattice spacing a(couplings) -> a->0 transport of normalized curvature correlator -> physical continuum observable -> GR/EFT comparator -> complete scaling/systematic error ledger`?

## A. Observable side remains a strong scoped PASS

Iter200 correctly froze the 2026 four-dimensional normalized curvature-correlator/geon capsule at one bare point in the de-Sitter-like phase. The final publication provides operator, volume, smearing and fit-window controls, and the associated stochastic samples are public on Zenodo.

No correction to that scoped PASS is required.

`PASS_RQIR_GATE__CDT_4D_NORMALIZED_CURVATURE_CORRELATOR_PHYSICAL_OBSERVABLE_WITH_OPERATOR_VOLUME_SMEARING_SYSTEMATICS_AND_OPEN_DATA` remains valid.

## B. Semiclassical 4D phase — strong positive control

The 4D de Sitter phase robustly exhibits a semiclassical universe whose average volume profile and fluctuations are described by a minisuperspace-like effective action. The 2026 Ambjørn-Loll synthesis continues to treat this as strong evidence for a well-defined classical limit, while short-distance observables such as the spectral dimension remain strongly quantum.

Classification:

`PASS_SCOPED_4D_SEMICLASSICAL_DE_SITTER_PHASE_AND_CLASSICAL_LIMIT_CONTROL`.

## C. CDT↔FRG fixed-point matching — promising but not a terminal UV certificate

The 2024 CDT↔FRG analysis identifies the generic infinite-four-volume de-Sitter-phase limit with Gaussian/IR fixed-point behavior and develops a concrete way to identify a putative UV lattice fixed point. The Monte Carlo data are compatible with such a UV fixed point, but the authors explicitly state that the current data precision is insufficient to prove its existence.

The 2026 review uses correspondingly cautious language: simulations indicate a possible/presence-like UV fixed-point structure and efforts toward nonperturbative observables are ongoing. This is a strong roadmap, not yet a demonstrated continuum trajectory with controlled scale setting.

Classification:

`PASS_SCOPED_CDT_FRG_UV_FIXED_POINT_COMPATIBILITY__NOT_PROVEN_CONTINUUM_TRAJECTORY`.

## D. 2026 additional 4D observables strengthen the de-Sitter phase but do not supply scale transport

Two recent results strengthen the physical characterization of the 4D de-Sitter phase:

1. Yang-Mills topology on thermalized 4D CDT triangulations emerges only in the de-Sitter phase, reinforcing its semiclassical-spacetime interpretation.
2. The curvature-correlator study finds operator-independent massive-like behavior over an intermediate distance window and is accompanied by public stochastic data.

Neither result measures the same gravity observable along a sequence of bare couplings approaching a critical surface with a common physical scale definition.

## E. Line of constant physics / lattice-spacing ancestry remains the decisive gap

The geon observable uses an external estimate `a ~ 2.1 l_P` at one simulation point. The publication itself warns that physical-unit conversion may carry discretization artifacts. Finite-volume stability across 80k–320k simplices does not constitute `a -> 0` scaling.

The bounded 2024–2026 authority sweep did not locate a prospectively frozen multi-coupling line of constant physics that simultaneously supplies:

- a sequence of 4D CDT bare points approaching a demonstrably higher-order critical surface/UV fixed point;
- a physical scale-setting observable evaluated at every point;
- `a(couplings)` with uncertainty;
- the normalized curvature-correlator observable remeasured/transported at every point;
- a controlled continuum extrapolation;
- a same-domain GR/EFT prediction for the extrapolated correlator;
- a unified critical-scaling + volume + discretization + operator + fit-window error ledger.

Therefore the key Iter200 continuum blocker remains substantively correct.

## 4D CDT branch disposition

`PARTIAL_SUBFAMILY_ONLY__4D_SEMICLASSICAL_AND_NORMALIZED_OBSERVABLE_STRONG_PASS__UV_CONTINUUM_LINE_OF_CONSTANT_PHYSICS_AND_COMPARATOR_BLOCKED`.

Exact missing certificate:

`CDT_4D_LINE_OF_CONSTANT_PHYSICS_TO_PROVEN_UV_CONTINUUM_TRAJECTORY_PLUS_LATTICE_SPACING_SCALING_AND_NORMALIZED_CURVATURE_CORRELATOR_GR_COMPARATOR_ERROR_CERTIFICATE`.

This is **not** a scientific FAIL of CDT and contributes zero exclusion evidence toward `NEW_REQUIRED`.

## Paper-III impact

No new transferable Paper-III failure mode is found. The distinction between finite-volume robustness and continuum-resource closure is already covered by the frozen requirement that scaling/normalization/calibration ancestry be explicit.

`PAPER_III_REOPEN = NO`.

## Heavy compute

`CONDITIONAL_HIGH_VALUE`.

Unlike many analytically blocked families, 4D CDT is close enough to a concrete numerical continuum question that heavy compute could be decision-relevant **if** a multi-bare-coupling line-of-constant-physics campaign is identified. Reprocessing the existing one-point geon data alone cannot close D2/D4. The next useful compute is prospective multi-coupling critical scaling, not another one-point refit.

## Next CDT/EDT family gate

The CDT child is parked on the explicit line-of-constant-physics certificate. The combined parent row still cannot close until EDT is independently dispositioned. Advance to:

`EDT_4D_CONTINUUM_PHASE_UV_FIXED_POINT_OBSERVABLE_COMPARATOR_AUDIT`

The next audit must determine whether modern 4D Euclidean Dynamical Triangulations, including measure-term or other extended formulations, has a controlled semiclassical/continuum phase and physical observable distinct from CDT, or whether the branch can be reduced/excluded from this parent only with an explicit scope theorem.
