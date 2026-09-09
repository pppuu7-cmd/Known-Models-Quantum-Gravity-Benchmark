# O-LQG — EPRL to Regge same-realization asymptotic certificate

**Date:** 2026-09-10  
**KMQGB iteration:** 181  
**RQIR authority:** Core v1.0 FROZEN; no criterion changed.

## Question

Does published authority satisfy any nontrivial subset of `EPRL_TO_EFFECTIVE_AREA_REGGE_SAME_REALIZATION_MATCHING_CERTIFICATE` without composing unrelated realizations?

## Declared microscopic realization

Lorentzian EPRL spinfoam amplitudes/state sums in the large-spin semiclassical regime. The result below is deliberately scoped to this realization and regime; it is not promoted to a nonperturbative coarse-graining theorem.

## Primary authority

1. Han & Krajewski, *Path Integral Representation of Lorentzian Spinfoam Model, Asymptotics, and Simplicial Geometries*, arXiv:1304.5626. The Lorentzian EPRL path integral admits large-spin critical configurations corresponding, under nondegeneracy/orientation assumptions, to classical Lorentzian simplicial geometry; at globally oriented and time-oriented critical configurations the leading phase is the Lorentzian Regge action.
2. Han, *Semiclassical Analysis of Spinfoam Model with a Small Barbero-Immirzi Parameter*, arXiv:1304.5628. With large spin and small gamma treated independently, a controlled regime produces a functional integration of the Regge action at leading order, with a stated regime dependence and curvature/deficit-angle restrictions outside it.
3. Han et al., *Complex critical points and curved geometries in four-dimensional Lorentzian spinfoam quantum gravity*, arXiv:2110.10670. Curved Regge geometries arise from large-j Lorentzian EPRL amplitudes, with the effective phase equal to Regge action plus higher-curvature corrections.
4. Han, Liu & Qu, *Complex critical points in Lorentzian spinfoam quantum gravity: 4-simplex amplitude and effective dynamics on double-Delta_3 complex*, arXiv:2301.02930. Gives an explicit procedure for deriving an effective theory of Regge geometries from the Lorentzian EPRL amplitude and numerically evaluates an effective action on a concrete complex; classical Regge gravity is reproduced for small gamma.
5. Magliaro & Perini, *Regge gravity from spinfoams*, arXiv:1105.0216. In a combined classical/flipped regime, under stated hypotheses, the spin-foam theory reduces to an effective Regge-like quantum theory and identifies two classes of corrections.

## Frozen payload decomposition

Required payload:

`{boundary_state, coarse_graining/refinement map, gamma normalization, approximation order, error/remainder, resulting Area-Regge/area-metric couplings}`.

### boundary_state — PARTIAL/CLOSED IN SCOPED ASYMPTOTIC SETUPS

Published EPRL asymptotic analyses specify spin-network/boundary data and distinguish Regge/non-Regge boundary data. This is sufficient to demonstrate that the microscopic and effective objects can belong to one declared EPRL realization in the analysed complexes.

### coarse_graining/refinement map — OPEN

The large-spin saddle/complex-critical-point construction is an asymptotic/effective map, not a demonstrated multiscale coarse-graining/refinement flow from a microscopic EPRL ensemble to a macroscopic Area-Regge action. No semigroup/blocking/refinement map with controlled accumulation of errors is supplied by the cited authority.

### gamma normalization — PARTIAL

The same EPRL Barbero-Immirzi parameter gamma occurs in the asymptotic analysis, so the microscopic-to-asymptotic Regge step does not require cross-paper renaming of an unrelated gamma. However, no certificate is yet available identifying this parameter with the running area-metric gamma_AM(mu) used by the downstream RG realization, including scheme and field-redefinition normalization.

### approximation order — PARTIAL/CLOSED LOCALLY

Large-spin and, where invoked, small-gamma expansion regimes are stated. The effective phase is Regge plus subleading/higher-curvature corrections in scoped regimes. This provides an actual approximation hierarchy rather than a purely qualitative analogy.

### error/remainder — PARTIAL

The literature identifies subleading asymptotic/higher-curvature corrections and regime restrictions, but KMQGB does not yet possess a single composable remainder bound propagated through refinement/coarse-graining and onward into area-metric couplings.

### resulting Area-Regge/area-metric couplings — OPEN

The cited EPRL results recover length/Regge effective dynamics in appropriate sectors. They do not derive the complete effective Area-Regge coupling vector, nor the parity-sensitive area-metric coupling set needed for the downstream beta_rho / beta_Delta construction.

## RQIR classification

A real same-realization bridge exists:

`Lorentzian EPRL microscopic amplitude -> large-spin critical/complex-critical effective dynamics -> Regge action + scoped corrections`.

Therefore M1 must no longer be represented as wholly absent. It is now:

**M1 = PARTIAL / ASYMPTOTIC SAME-REALIZATION PASS, NONPERTURBATIVE COARSE-GRAINING OPEN.**

This does **not** close CW2-02 because:

- the required coarse-graining/refinement map is missing;
- the EPRL gamma -> gamma_AM(mu) identity/normalization is missing;
- effective Area-Regge/area-metric parity coupling matching is missing;
- no composable full error certificate exists.

## Updated exact next gate

`EPRL_REGGE_TO_AREA_REGGE_PARITY_COUPLING_MATCHING_CERTIFICATE`

Required payload:

`{declared Lorentzian EPRL realization, asymptotic Regge sector, map from Regge variables to Area-Regge/area-metric variables, gamma_EPRL -> gamma_AM(mu) normalization, parity-sector coupling map, approximation/remainder ledger, refinement/coarse-graining compatibility}`.

A successful certificate must preserve same-realization ancestry rather than joining independent models by notation.

## Scientific conclusion

Iteration 181 closes an important binary uncertainty: the EPRL-to-effective-gravity dynamical bridge is not merely conjectural. A scoped same-realization asymptotic EPRL -> Regge bridge is published and explicit. The remaining obstruction is narrower: transport that authenticated ancestry from Regge dynamics into the Area-Regge/area-metric parity/RG realization with parameter identity and composable errors.

No Candidate Gravity readiness score is increased by this partial closure. CW2 remains nonterminal and `NEW_REQUIRED` remains unauthorized.
