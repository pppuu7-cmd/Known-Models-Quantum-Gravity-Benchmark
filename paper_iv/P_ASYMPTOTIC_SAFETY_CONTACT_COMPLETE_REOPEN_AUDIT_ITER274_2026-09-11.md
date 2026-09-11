# Asymptotic Safety contact-complete Lorentzian scattering reopen audit — Iter274

Date: 2026-09-11
Family: `ASYMPTOTIC_SAFETY`
RQIR Core: `v1.0 FROZEN`
D7 stage: `D7-S2 STRICT_TIER1_TERMINAL_COVERAGE`

## Reopen trigger

Iter273's current benchmark front explicitly marked Asymptotic Safety as a high-information external-authority watch target because September-2026 conference material reports Lorentzian contact-term progress. The frozen PF1-05 blocker is:

`CONTACT_COMPLETE_APPROXIMATION_CONTROLLED_LORENTZIAN_SCALAR_SCATTERING_CERTIFICATE`

The bounded question for this iteration is therefore:

> Has the missing same-realization direct contact contribution `A4` now become a stable, public, reproducible object sufficient to close the contact-complete Lorentzian scalar-scattering certificate and materially advance D7-S2/D7-S3?

## Archival primary source checked

Primary preprint:

- Angelo P. Chiesa, Jan M. Pawlowski, Manuel Reichert, **Towards Two-to-Two Scattering of Scalars in Asymptotically Safe Quantum Gravity**, arXiv:`2603.10168` (v1, 2026-03-10).

The paper is a major positive control. It computes the full momentum dependence of the scalar-graviton three-point vertex in the functional renormalisation group, reconstructs the timelike/Lorentzian vertex, and obtains a graviton-mediated scalar scattering amplitude and cross section that recover GR at low energy and remain bounded/compatible with unitarity in the UV.

However, the archival version explicitly writes the full amplitude as

`A = A_s + A_t + A_u + A_4`

and then states that it focuses on the graviton-mediated diagrams and **neglects the direct contact term `A_4`**. It further states that the forward-limit divergence can only be resolved with inclusion of `A_4`.

Therefore the stable primary source does not itself close the frozen PF1-05 blocker.

## September-2026 conference signal

A materially newer conference contribution exists:

- Angelo Portas Chiesa, **Unitarity at all scales: Towards 2-to-2 scattering of scalars in Asymptotically Safe Quantum Gravity**, ERG2026, University of Sussex, 2026-09-03.

The conference description links the same arXiv paper and reports a gravitational contribution to the contact amplitude resummed directly in Lorentzian signature, yielding a non-perturbative amplitude/cross-section compatible with GR at small energies and respecting unitarity in the UV. Presentation material `scalar-grav-ERG-26.pdf` is listed by the conference page.

This is exactly the kind of development that can attack the old `A4` blocker. It is therefore not noise and must remain on the active external-authority watch.

## Why terminal promotion is still forbidden

The current evidence is split across two authority levels:

1. The stable archival preprint is public and technically detailed, but explicitly omits `A_4`.
2. The September conference record reports Lorentzian contact-term completion/progress, but the bounded audit did not locate a revised archival preprint or a public same-realization reproducibility package that freezes the contact term together with the complete `s+t+u+A4` observable and uncertainty budget.

The conference report cannot be silently substituted for the missing reproducible terminal object. Under the frozen coverage contract, a promising conference result is a reopen/watch trigger, not family-level sufficiency evidence.

## Scoped result

`HIGH_VALUE_NEAR_MISS__LORENTZIAN_CONTACT_TERM_REPORTED_AT_ERG2026_BUT_NOT_YET_FROZEN_IN_A_PUBLIC_REPRODUCIBLE_CONTACT_COMPLETE_SAME_REALIZATION_PACKAGE`

Family-level status remains:

`BLOCKED_MISSING_REQUIRED_OBJECT`

Refined active blocker:

`BLOCKED_PENDING_PUBLIC_CONTACT_COMPLETE_S_PLUS_T_PLUS_U_PLUS_A4_LORENTZIAN_SCATTERING_CERTIFICATE_WITH_FORWARD_LIMIT_TREATMENT_APPROXIMATION_UNCERTAINTY_BUDGET_AND_SAME_DOMAIN_COMPARATORS`

This is `BLOCKED`, not scientific `FAIL`.

## D7 consequence

- D7-S0: `PASS`.
- D7-S1: `PASS`.
- D7-S2: `NOT_CLOSED`.
- strict Tier-1 terminal rows: `1/14`.
- strict Tier-1 nonterminal rows: `13/14`.
- `ASYMPTOTIC_SAFETY`: remains nonterminal / `BLOCKED_MISSING_REQUIRED_OBJECT`.
- D7-S3: `NOT_CLOSED`.
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7-S5: `NOT_AUTHORIZED`.
- D7-S6 / Candidate Gravity activation: `INACTIVE`.
- Candidate Gravity R3: `24%`.
- Heavy compute: `IDLE`; the decisive missing object is external archival/reproducibility authority, not a useful internal numerical sweep.

No `NEW_REQUIRED`, `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, or `HYBRID_REQUIRED` inference is authorized.

## Exact reopen condition

Reopen immediately if a stable public source supplies the same-realization Lorentzian contact term and freezes enough information to certify all of the following together:

1. complete physical `s+t+u+A4` amplitude/cross section;
2. crossing and forward-limit treatment;
3. direct linkage to the same asymptotic-safety trajectory/vertices/propagators;
4. approximation/truncation/reconstruction/contact-term uncertainty or robustness budget;
5. machine-checkable or otherwise reproducible numerical/analytic artifacts sufficient to reproduce the claimed observable;
6. same-domain GR/EFT and at least the required alternative-QG comparator capsule.

If those conditions appear, the next action is not another literature summary: ingest the package, freeze hashes/identifiers, run the D7 witness validator, and then re-evaluate D7-S2/S3/S4.

## Sources checked

- arXiv: `https://arxiv.org/abs/2603.10168`
- arXiv HTML: `https://arxiv.org/html/2603.10168v1`
- ERG2026 contribution: `https://indico.global/event/16125/contributions/164384/`

## Audit conclusion

The Asymptotic Safety front has advanced scientifically relative to the archival March-2026 paper because the September conference record now reports the previously missing Lorentzian contact contribution. But the benchmark still lacks the public, stable, contact-complete same-realization certificate required by the frozen judge. The correct state is therefore **active external-authority watch / high-value near-miss**, with no terminal-count change and no D7 authorization change.