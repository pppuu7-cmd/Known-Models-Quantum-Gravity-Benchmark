# Asymptotic Safety contact-complete freshness audit — Iter263

Date: 2026-09-11
Family: `ASYMPTOTIC_SAFETY`
RQIR Core: `v1.0 FROZEN`

## Question
Has the `CONTACT_COMPLETE_APPROXIMATION_CONTROLLED_LORENTZIAN_SCALAR_SCATTERING_CERTIFICATE` blocker from PF1-05 been closed by developments available through 2026-09-11?

## Prior state
PF1-05 already established real positive controls: Lorentzian graviton spectral functions; GR-IR to asymptotically-safe-UV interpolation; momentum-dependent Lorentzian scalar scattering; IR recovery of GR; UV cross-section compatible with stated unitarity bounds. It correctly rejected obsolete blockers such as 'no Lorentzian observable'.

The remaining object was one same-realization complete amplitude `A = A_s + A_t + A_u + A_4`, including direct contact, crossing/forward treatment, approximation/truncation uncertainty and same-domain comparators.

## Authorities checked
1. A. P. Chiesa, J. M. Pawlowski, M. Reichert, *Towards Two-to-Two Scattering of Scalars in Asymptotically Safe Quantum Gravity*, arXiv:2603.10168v1, submitted 2026-03-10.
2. ERG2026 contribution by A. P. Chiesa, 2026-09-03, *Unitarity at all scales: Towards 2-to-2 scattering of scalars in Asymptotically Safe Quantum Gravity*.
3. B. Knorr, *Asymptotically (un)safe scattering amplitudes from scratch: a deep dive into the IR jungle*, arXiv:2602.21285 (2026).

## Freshness result
As of 2026-09-11 the canonical arXiv page for `2603.10168` still lists only `v1` from 2026-03-10. Its public abstract and paper scope provide the graviton-mediated two-to-two scalar amplitude/cross section, reconstructed to Lorentzian signature, with GR recovery at low energy and UV behavior compatible with unitarity.

The ERG2026 contribution one week before this audit materially advances the frontier: its public conference description states that the mediated result is corroborated by a gravitational contribution to the contact amplitude that is resummed directly in Lorentzian signature, allowing a nonperturbative amplitude and cross-section study.

However, the conference contribution points to the same arXiv:2603.10168, whose stable public version remains v1 and does not yet provide a canonical contact-complete reproducible paper package. KMQGB therefore treats the ERG2026 result as high-value freshness evidence, but not as sufficient authority to rewrite the frozen blocker as closed.

Status:
`PROMISING_NONCANONICAL_CONTACT_PROGRESS__ERG2026_DIRECT_LORENTZIAN_CONTACT_REPORTED__STABLE_REPRODUCIBLE_CONTACT_COMPLETE_PACKAGE_PENDING`.

## Why the blocker remains substantive
Knorr 2026 independently shows in a controlled scalar-scattering model that the existence of an asymptotically safe fixed point alone does not guarantee bounded scattering amplitudes, and that derivative expansions / standard RG improvement can fail to reproduce full momentum dependence in relevant regimes. This directly supports the KMQGB rule that the missing contact term, momentum dependence and approximation-error closure cannot be filled by generic fixed-point evidence.

The remaining same-realization package still requires:
- canonical `A_s+A_t+A_u+A_4` amplitude and crossing/forward treatment;
- contact-sector and reconstruction provenance in the same Lorentzian realization;
- propagated truncation/avatar/reconstruction/scheme uncertainty, not only reconstruction method comparison;
- identical-domain GR/EFT and alternative-QG comparator predictions.

## Disposition
`BLOCKED_PENDING_STABLE_CONTACT_COMPLETE_LORENTZIAN_SCALAR_SCATTERING_PACKAGE_WITH_FULL_APPROXIMATION_ERROR_AND_COMPARATOR_CERTIFICATE`.

Operational status:
`PARKED_PENDING_POST_ERG2026_CONTACT_COMPLETE_PUBLIC_AUTHORITY`.

This is `BLOCKED`, not a scientific FAIL of Asymptotic Safety. It does not authorize `NEW_REQUIRED`.

## Governance
- strict Tier-1 family status: `BLOCKED_MISSING_REQUIRED_OBJECT`;
- D2: `NOT_CLOSED`;
- D4: `PARTIAL_GLOBAL_NOT_CLOSED`;
- D7: `NOT_CLOSED / NOT_YET_AUTHORIZED`;
- Candidate Gravity R3: 24%;
- Heavy compute: `IDLE`.

## Polygon saturation
Operational known-school polygon saturation increases from ~97% to ~98%. The Asymptotic Safety frontier is now bounded by a concrete post-ERG2026 publication/reproducibility object rather than a broad amplitude search. This is operational saturation, not strict D7 completion.

## Next gate
Do not repeatedly re-search Asymptotic Safety until `2603.10168` is revised/published or a separate stable contact-complete authority appears. Move to another finite Tier-1 blocker, prioritizing CDT/EDT continuum-observable closure, causal-set dynamics-to-continuum closure, or another row where current authority can convert the blocker into an explicit external endpoint.
