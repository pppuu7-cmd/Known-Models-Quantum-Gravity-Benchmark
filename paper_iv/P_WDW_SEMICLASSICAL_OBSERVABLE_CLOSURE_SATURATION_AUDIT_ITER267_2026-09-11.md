# Wheeler–DeWitt semiclassical-observable closure saturation audit — Iter267

**Date:** 2026-09-11  
**RQIR Core:** v1.0 FROZEN  
**Family:** `WHEELER_DEWITT_QUANTUM_GEOMETRODYNAMICS`

## Question
Does canonical Wheeler–DeWitt quantum geometrodynamics possess concrete observable maps beyond formal wave-function solutions, and if so what prevents a family-terminal same-realization certificate?

## Authority synthesis
1. Chataignier, Kiefer & Moniz (2023), *Observations in Quantum Cosmology*, show that a weak-coupling/Born–Oppenheimer expansion of quantum geometrodynamics provides a perturbative Hilbert-space description, relational predictions and corrections to quantum fields on a classical background; primordial spectra are a concrete observable target.
2. Kiefer & Vardanyan (2022/2023) derive gauge-invariant inflationary power spectra from the Wheeler–DeWitt equation and calculate quantum-gravitational corrections in a closed universe. Thus “WDW has no normalized observable map” is obsolete.
3. Maniccia et al. (2024), *Inflationary quantum spectrum of the quasi-isotropic Universe*, explicitly recover Schrödinger dynamics for perturbations from WDW in a WKB/Born–Oppenheimer regime; the scalar spectrum has the standard scale-invariant profile while the tensor sector retains model-dependent pre-inflation information.
4. Bini, Esposito, Kiefer, Krämer & Pessina show that the same general semiclassical WDW correction problem contains an ambiguity: admissible solution choices can suppress or enhance large-scale CMB power, with the correction presently unobservable and possible unitarity questions requiring care.
5. The broader canonical framework still requires a physical Hilbert-space/inner-product prescription, relational clock/observable construction and state/boundary-condition choice. Modern 2026 work on gravitational Hilbert spaces clarifies group averaging/BRST constructions in minisuperspace and semiclassical settings, but does not supply a unique full-superspace same-realization cosmological observable/error certificate.

## Scoped result
`PASS_STRUCTURAL_GATE__WDW_HAS_GAUGE_INVARIANT_SEMICLASSICAL_INFLATIONARY_OBSERVABLE_MAPS_WITH_RECOVERED_SCHRODINGER_LIMIT`

This is a real observable-side PASS. It is not a family-level PASS because the published observable maps are semiclassical, symmetry-reduced/perturbative and depend on physical-state/boundary/clock prescriptions.

## Remaining blocker
`BLOCKED_EXTERNAL_THEORY_OBJECT__WDW_SAME_REALIZATION_FULL_SUPERSPACE_PHYSICAL_INNER_PRODUCT_STATE_SELECTION_RELATIONAL_OBSERVABLE_AND_PROPAGATED_SEMICLASSICAL_REGULARIZATION_ERROR`

A family-terminal reopen object must jointly freeze:
- regularized full canonical constraint realization and physical state space;
- positive/physical inner product or equivalent transition-amplitude prescription;
- state/boundary-condition selection and relational clock/observable map;
- one normalized physical observable in the same realization;
- GR/EFT/common-domain comparator;
- propagated Born–Oppenheimer/WKB, regularization/factor-ordering and truncation uncertainty.

## RQIR disposition
- family status: `PARTIAL_SUBFAMILY_ONLY`
- family residual: `UNDEFINED`
- D2: `NOT_CLOSED`
- D4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7: `NOT_CLOSED_NOT_YET_AUTHORIZED`
- Candidate Gravity active: **false**
- Candidate Gravity R3: **24%**
- family FAIL: **no**
- heavy compute: `IDLE`; the blocker is a missing externally authoritative theory/physical-Hilbert-space object, not a justified brute-force calculation.

## Polygon consequence
The WDW row is saturated to the current internally reachable literature boundary: concrete observables exist, while family closure requires a stronger physical-state/inner-product/relational-observable construction than current authority supplies. Operational polygon readiness remains **~99%** pending the remaining unsaturated Tier-1 fronts and a final D2/D4/D7 saturation rerun.

## Next gate
`QUANTUM_GRAPHITY_CONTINUUM_EMERGENT_GR_OBSERVABLE_CLOSURE_SATURATION_AUDIT`
