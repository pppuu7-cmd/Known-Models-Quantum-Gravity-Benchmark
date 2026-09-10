# NCSG comparator-ready gravity-realization saturation audit — Iter266

**Date:** 2026-09-11  
**RQIR Core:** v1.0 FROZEN  
**Family:** `NONCOMMUTATIVE_SPECTRAL_GEOMETRY`

## Question
Does current authority provide a concrete same-realization NCSG gravity object with a GR limit and normalized weak-field observable/comparator, or is the row still blocked at the level of a formal spectral action?

## Authority synthesis
1. The almost-commutative NCSG spectral action contains Einstein-Hilbert gravity plus a Weyl-squared correction and Higgs-curvature coupling. The weak-field gravity sector is therefore not only a formal algebraic construction.
2. Nelson, Ochoa & Sakellariadou, Phys. Rev. D 82, 085021 (2010), derived the weak-field gravitational-wave sector and showed an additional massive spin-2 response that changes quadrupole radiation.
3. The 2026 EPJC paper **Post-Newtonian N-body dynamics in Extended Theories of Gravity** derives a complete 1PN N-body Lagrangian/EOM for the regular STFOG branch and treats NCSG as the scalaron-decoupling Weyl-squared specialization. For NCSG it gives explicit Yukawa-corrected metric potentials governed by a single mass parameter `beta`, retains the gravitomagnetic completion, and recovers the Einstein–Infeld–Hoffmann equations when the Yukawa correction decouples.
4. The same paper identifies Solar-System, binary-pulsar, Galactic-centre and hierarchical-system observables as direct application domains. It does not itself perform a data likelihood analysis, publish a covariance/error budget, or carry the spectral-action unification-scale parameters through a complete RG/threshold transport to the low-energy 1PN parameter with propagated uncertainties.
5. Existing NCSG phenomenology constrains the Weyl-squared scale from laboratory/Gravity-Probe-B/binary-pulsar-type tests, but these constraints do not constitute a same-realization quantum-to-low-energy uncertainty certificate.

## Scoped result
`PASS_STRUCTURAL_GATE__NCSG_HAS_EXPLICIT_LORENTZIAN_WEAK_FIELD_1PN_GRAVITY_REALIZATION_WITH_GR_LIMIT_AND_NORMALIZED_YUKAWA_OBSERVABLE_FAMILY`

This closes the obsolete blocker “no comparator-ready gravity observable exists.” It does **not** close the family under RQIR because the same-realization chain from spectral triple/cutoff data through coefficient running/threshold matching to the low-energy observable and its propagated uncertainty is not frozen.

## Remaining blocker
`BLOCKED_EXTERNAL_THEORY_DATA_OBJECT__NCSG_SAME_REALIZATION_SPECTRAL_TRIPLE_TO_LORENTZIAN_LOW_ENERGY_COEFFICIENT_TRANSPORT_PLUS_OBSERVATIONAL_COVARIANCE_AND_PROPAGATED_RG_TRUNCATION_ERROR`

Required reopen object:
- fixed spectral triple and cutoff-function moments / boundary data;
- explicit Lorentzian low-energy coefficient transport including RG and thresholds;
- fixed physical observable in the same realization;
- common-domain GR/EFT comparator;
- experimental covariance/nuisance treatment;
- propagated matching/RG/truncation uncertainty.

## RQIR disposition
- family status: `PARTIAL_SUBFAMILY_ONLY`
- family residual: `UNDEFINED`
- D2: `NOT_CLOSED`
- D4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7: `NOT_CLOSED_NOT_YET_AUTHORIZED`
- family FAIL: **no**
- Candidate Gravity activation: **no**
- Candidate Gravity R3: **24%**
- heavy compute: `IDLE`; the missing object is authority/matching/covariance, not a justified internal brute-force calculation.

## Polygon consequence
NCSG is now saturated at the level internally reachable from current literature: a real comparator-ready weak-field gravity object exists, while the remaining family-terminal requirement is an external same-realization transport/error certificate. This supports an operational polygon-readiness estimate of **~99%**, but not 100% until the remaining unsaturated Tier-1 fronts are similarly reduced to terminal or explicit external-blocker endpoints and D2/D4/D7 are rerun.

## Next gate
`WDW_SEMICLASSICAL_OBSERVABLE_CLOSURE_SATURATION_AUDIT`
