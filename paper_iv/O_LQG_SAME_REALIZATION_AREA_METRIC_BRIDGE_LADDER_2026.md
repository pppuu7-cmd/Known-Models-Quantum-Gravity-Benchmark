# O-LQG same-realization area-metric bridge ladder — 2026-09-10

**KMQGB iteration:** 180  
**RQIR standard:** Core v1.0 FROZEN  
**CW2 object:** CW2-02 / O-LQG

## Objective

Determine which parts of the required EPRL/spinfoam -> area-metric continuum map are already supported and isolate the smallest still-missing same-realization object. This note does not weaken the RQIR firewall and does not compose results from inequivalent realizations as if they were one model.

## Literature authority used

1. Dittrich & Padua-Arguelles, *Twisted geometries are area-metric geometries*, Phys. Rev. D 109, 026002 (2024): the twisted geometry of a four-simplex can be represented as an area metric. This supplies a kinematic representation bridge from a standard LQG/spinfoam boundary-geometry language to area-metric geometry.
2. Asante, Dittrich & Haggard, *Effective Spin Foam Models for Four-Dimensional Quantum Gravity* (2021), and subsequent effective-spin-foam work: effective spin foams are constructed to retain key spin-foam ingredients while replacing the full EPRL/FK amplitude by a tractable Area-Regge-based effective amplitude. This is a controlled surrogate/model-family construction, not an equality theorem to a fixed EPRL realization.
3. Dittrich & Kogios, *From spin foams to area metric dynamics to gravitons* (2022): the continuum analysis of Area Regge dynamics yields an area-metric description and graviton sector.
4. Borissova & Dittrich, *Towards effective actions for the continuum limit of spin foams* (2023): modified-Plebanski/area-metric actions are proposed as candidate effective actions motivated by the Area-Regge continuum limit.
5. Borissova, Dittrich, Eichhorn & Schiffer, *Renormalization group flows in area-metric gravity* (2025): area-metric RG flow includes a running Immirzi parameter and nontrivial parity-sector behavior.
6. *Gravitational wave signatures from area metric gravity* (2026): a Lorentzian detector-facing observable route exists in the area-metric theory, including a birefringence observable sensitive to the Barbero-Immirzi parameter.

## Bridge ladder

Define the required same-realization map as a ladder rather than one opaque arrow.

### M0 — microscopic/boundary kinematic representation

Required statement:

`EPRL/LQG boundary geometric data -> area-metric geometric data`

without adding an independent phenomenological parameter.

**Status: CLOSED at the kinematic representation level.**

The twisted-geometry/area-metric equivalence supplies an explicit representation bridge for the relevant enlarged geometry. This closes only the statement that area-metric variables are a legitimate continuum-oriented representation of the enlarged LQG/spinfoam kinematics.

It does **not** prove that a particular EPRL path integral coarse-grains to the later area-metric action used in RG or phenomenology.

### M1 — microscopic dynamics to Area-Regge/effective-spin-foam dynamics

Required statement:

`W_gamma^EPRL -> A_eff^same-realization[areas,shape data; gamma]`

with approximation, boundary state, refinement/coarse-graining prescription and error controlled.

**Status: OPEN / SURROGATE AUTHORITY ONLY.**

Effective spin foams explicitly aim to capture key EPRL/FK construction principles and are highly valuable as a calculable surrogate. However, replacing the exact EPRL amplitude by an effective Area-Regge amplitude is a model adaptation. Under the frozen KMQGB same-realization rule this cannot be silently promoted to an exact EPRL coarse-graining map.

### M2 — Area-Regge dynamics to area-metric continuum action

Required statement:

`A_eff -> Gamma_AM[G; mu]`

in a controlled continuum/refinement expansion.

**Status: PARTIAL / STRONG CONTINUUM AUTHORITY.**

Area-Regge perturbative continuum work and modified-Plebanski constructions establish a concrete area-metric effective-action target and graviton corrections. The missing part for CW2-02 is not the existence of such a continuum theory; it is same-parent attribution back to the EPRL realization selected in M1.

### M3 — Immirzi parameter identity and normalization

Required statement:

`gamma_micro^EPRL -> gamma_eff -> gamma_AM(mu)`

with a derived normalization/sign convention, not name matching.

**Status: OPEN.**

The effective-spin-foam area spectrum depends on gamma, while area-metric RG has an Immirzi parameter and beta function. Their common naming and physical motivation are insufficient for RQIR parameter identity. The map needs to follow from the same coarse-grained action/amplitude, including wave-function/operator normalization and truncation/regulator dependence.

### M4 — same-parent parity/RG transport

Required statement:

`Gamma_AM^same-parent -> {beta_gamma, beta_rho, beta_Delta}`

with `Delta_gamma = rho - (gamma - 1/gamma)` and

`beta_Delta = beta_rho - (1 + 1/gamma^2) beta_gamma`.

**Status: OPEN.**

Area-metric RG supplies beta_gamma authority, but CW2-02 still lacks the parity-sector ratio flow `beta_rho` and therefore lacks same-parent `beta_Delta` authority tied to the same microscopic realization.

### M5 — detector/cosmological observable closure

The low-energy area-metric birefringence channel and the primordial gamma-duality relation already define an executable observable consistency residual after scale transport.

**Status: OBSERVABLE MAP CLOSED / ATTRIBUTION OPEN.**

## New scientific result of Iter180

The old blocker

`EPRL/spinfoam -> area-metric map missing`

was too coarse. It is replaced by the stricter decomposed statement:

- **M0 kinematic representation compatibility: CLOSED**;
- **M1 exact/same-realization dynamical coarse-graining: OPEN**;
- **M2 area-metric continuum target: PARTIAL/STRONG**;
- **M3 gamma identity/normalization: OPEN**;
- **M4 same-parent parity RG transport: OPEN**;
- **M5 observable closure: CLOSED conditionally on M1-M4 attribution**.

This is progress because a future calculation no longer needs to prove that area metrics are an admissible representation for LQG/spinfoam geometry; it must instead attack a much narrower dynamical and parameter-matching problem.

## Minimal decisive next object

The next gate is now

`EPRL_TO_EFFECTIVE_AREA_REGGE_SAME_REALIZATION_MATCHING_CERTIFICATE`

with payload

`{boundary_state, coarse_graining/refinement map, gamma normalization, approximation order, error/remainder, resulting Area-Regge/area-metric couplings}`.

A valid certificate may be analytic, numerical, or mixed, but it must originate from one declared microscopic EPRL realization. A generic effective-spin-foam surrogate is not enough unless its relation to that realization is quantitatively derived.

## Classification

`PROMISING_ADAPT_EXISTING__KINEMATIC_AREA_METRIC_BRIDGE_CLOSED__DYNAMICAL_EPRL_TO_EFFECTIVE_AREA_REGGE_SAME_REALIZATION_CERTIFICATE_MISSING`.

## Score policy

No R1/R2 change: both remain 100%. No R3 scientific-readiness promotion is authorized because M1/M3/M4 remain open. Closure Wave 02 remains 0/3 terminal. Paper IV remains NOT_YET_AUTHORIZED. BLOCKED != NEW_REQUIRED. Heavy compute remains IDLE until a frozen same-realization payload is available.