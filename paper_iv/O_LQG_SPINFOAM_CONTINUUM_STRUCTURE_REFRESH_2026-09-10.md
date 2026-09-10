# O-LQG / spin-foam continuum-structure authority refresh — 2026-09-10

**KMQGB iteration:** 197  
**RQIR Core:** v1.0 FROZEN  
**Scope:** fresh-literature audit for the open `EPRL_REGGE_TO_AREA_REGGE_PARITY_COUPLING_MATCHING_CERTIFICATE` gate.

## New primary authority

Matteo Bruno, Eugenia Colafranceschi, Fabio M. Mele, Carlo Rovelli, *Structure of the continuum limit of spin foams*, Phys. Rev. D 114, 066005 (published 8 September 2026; accepted 5 August 2026), introduces a model-independent axiomatic framework in which spin-foam Hilbert spaces and amplitudes are assigned to triangulation/topological data and the set of triangulations is equipped with suitable orders so that a precise continuum-limit notion can be formulated and analysed.

This is a material authority upgrade for KMQGB because the continuum-limit step no longer has to be described only informally as an unspecified refinement limit.

## What is now closed at scoped structural level

`PASS_STRUCTURAL_GATE__SPINFOAM_CONTINUUM_LIMIT_CAN_BE_DEFINED_BY_ORDERED_TRIANGULATION_REFINEMENT_FRAMEWORK`.

This supplies a mathematically explicit host for asking whether a concrete spin-foam realization possesses a compatible continuum trajectory and whether amplitudes are consistent under refinement.

## What it does NOT close

The 2026 result is deliberately model-independent. It does not by itself provide a same-realization EPRL coarse-graining trajectory, an EPRL-to-Area-Regge/area-metric coupling map, or the required ancestry/normalization of the Immirzi/parity-sensitive parameters. It also does not supply the RQIR comparator-facing normalized Lorentzian observable and propagated truncation/refinement remainder required for family-level closure.

Therefore it is forbidden to promote the structural continuum framework to an EPRL physical-object PASS.

O-LQG remains:

`BLOCKED_MISSING_REQUIRED_OBJECT`.

The exact blocker is contracted to:

`EPRL_CONTINUUM_TRAJECTORY_IN_ORDERED_REFINEMENT_FRAMEWORK_PLUS_REGGE_TO_AREA_REGGE_PARAMETER_ANCESTRY_AND_ERROR_CERTIFICATE`.

## Relation to GFT/spinfoam

The paper also strengthens the need to keep the GFT/spinfoam independence-or-reduction question explicit. A model-independent spin-foam continuum framework is not an equivalence theorem to a particular GFT realization. No GFT family-level promotion follows.

## Compute decision

Heavy compute remains `IDLE`. The missing object is a same-realization refinement/coarse-graining and parameter-ancestry certificate. A numerical scan without prospectively frozen realization, refinement prescription and comparator would not change the terminal classification.

## Paper-IV consequence

No Tier-1 family becomes terminal. D2, D4 and D7 remain open; `NEW_REQUIRED` remains unauthorized and Candidate Gravity remains inactive at R3=24%.
