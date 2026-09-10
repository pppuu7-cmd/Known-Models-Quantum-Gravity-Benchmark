# Asymptotic Safety — contact-complete scattering and Lorentzian spectral authority refresh (Iter243)

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `ASYMPTOTIC_SAFETY`  
**Gate:** `ASYMPTOTIC_SAFETY_CONTACT_COMPLETE_SCATTERING_AND_LORENTZIAN_SPECTRAL_AUTHORITY_REFRESH`

## Question

Has the narrow O-AS blocker now closed through a stable same-realization object containing the complete scalar amplitude

`A = A_s + A_t + A_u + A_4`

with Lorentzian prescription, normalization, crossing and propagated flow/reconstruction/contact errors?

## A. Stable scalar-scattering preprint remains contact-incomplete

Chiesa, Pawlowski and Reichert, arXiv:2603.10168, remains at v1 (submitted 10 March 2026) in the arXiv record checked on 10 September 2026. The paper explicitly defines the identical-scalar amplitude as

`A = A_s + A_t + A_u + A_4`

and explicitly states that the work focuses on the three graviton-mediated channels and neglects the direct contact term `A_4`, assigning its computation to Chiesa and Reichert, `in preparation (2026)`.

The stable paper therefore remains:

`PASS_SCOPED_MEDIATED_FULL_MOMENTUM_SCALAR_SCATTERING__CONTACT_INCOMPLETE`.

## B. ERG2026 gives a real programme-level contact upgrade

At ERG2026 on 3 September 2026, Angelo Portas Chiesa publicly reported that the mediated amplitude is complemented/corroborated by the gravitational contribution to the contact amplitude, resummed directly in Lorentzian signature, and that the resulting cross section is GR-compatible in the IR and compatible with unitarity in the UV.

This retains and strengthens the Iter171 conclusion:

`PROMISING_SAME_PROGRAMME_CONTACT_COMPLETE_PRESENTATION__REPRODUCIBLE_SAME_REALIZATION_CERTIFICATE_MISSING`.

The conference statement establishes programme-level existence of the missing sector but does not, by itself, provide the stable equations/data/error package required by RQIR.

## C. Lorentzian spectral-function authority materially strengthens the two-point sector

Assant, Litim and Reichert, arXiv:2606.19321, compute graviton spectral functions directly within Lorentzian functional renormalisation. The work derives and solves flows for Källén-Lehmann representations, finds normalisable spectral functions across several renormalisation conditions, matches effective theory in the IR, and derives the quantum effective action through quadratic order in curvature with induced form factors.

KMQGB classification:

`PASS_SCOPED_AS_LORENTZIAN_GRAVITON_SPECTRAL_FUNCTION_AND_QUADRATIC_EFFECTIVE_ACTION_CONTROL`.

This is scientifically important because it reduces uncertainty about the propagator/spectral/unitarity side of the AS observable programme.

It does **not** close `A_4`: two-point spectral control and a scalar four-point contact vertex are different 1PI objects. D6 forbids replacing the missing contact sector with the spectral-function result.

## D. Knorr leading-order scalar scattering remains an independent realization/control

Knorr, arXiv:2602.21285v2, provides an analytically tractable leading-order AS scalar-scattering model and shows that fixed-point existence alone does not guarantee bounded scattering; momentum dependence is essential and standard derivative/RG-improvement approximations can fail.

This is a strong negative/robustness control, but it is not automatically the same truncation/trajectory/reconstruction realization as Chiesa–Pawlowski–Reichert. Its contact information cannot be spliced into arXiv:2603.10168 without an explicit equivalence map.

## E. Exact missing object after Iter243

The old blocker remains correct but can be described with stronger positive context:

`STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`.

Minimum payload:

1. explicit `A_4` formula or reproducible numerical object;
2. same scalar species/external-state conventions as `A_s+A_t+A_u`;
3. same RG trajectory/fixed-point branch and renormalisation conditions;
4. same Lorentzian reconstruction/direct-flow prescription or explicit map;
5. contact + mediated crossing/normalization;
6. full `A_s+A_t+A_u+A_4` amplitude/cross section;
7. propagated truncation, flow, reconstruction, regulator and contact-sector uncertainty;
8. same-domain GR/EFT comparator.

## Family disposition

`BLOCKED_MISSING_REQUIRED_OBJECT__MEDIATED_SCATTERING_AND_LORENTZIAN_SPECTRAL_SECTORS_STRONG__PROGRAMME_LEVEL_CONTACT_COMPLETE_RESULT_PUBLIC__STABLE_SAME_REALIZATION_A4_ERROR_COMPARATOR_PACKAGE_MISSING`.

This is **not** a scientific FAIL of Asymptotic Safety.

## Paper-III impact

No new transferable resource-closure failure mode appears. The separation of 2-point spectral authority, 3-point mediated scattering and 4-point contact authority is an instance of the already-frozen same-realization/provenance closure rule.

`PAPER_III_REOPEN = NO`.

## Heavy compute

`IDLE`.

Without the same-realization contact vertex, KMQGB computation would have to invent/interpolate the decisive missing input. Recomputing the mediated channels or spectral functions cannot close the full amplitude.

## Route consequence

O-AS is now parked on a single externally identifiable near-term object. Re-searching it before a contact preprint/revision/data release has low information gain.

The next step is a global active-set actionability reselection: separate branches that are authority-blocked from branches where a prospectively frozen computation can actually change classification.

## Next gate

`PAPER_IV_ACTIVE_SET_COMPUTE_ACTIONABILITY_AND_INFORMATION_GAIN_RESELECTION_ITER244`
