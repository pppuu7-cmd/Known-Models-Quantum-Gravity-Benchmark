# Asymptotic Safety 2026 scattering realization-split audit

**Date:** 2026-09-10  
**KMQGB iteration:** 189  
**Family:** `ASYMPTOTIC_SAFETY`  
**RQIR Core:** v1.0 FROZEN

## Question

Has the 2026 Asymptotic-Safety literature now supplied the previously missing contact-complete Lorentzian scalar-scattering object in the **same realization** as the non-perturbative mediated amplitude, so that the AS family can be promoted from `BLOCKED_MISSING_REQUIRED_OBJECT`?

## Result in one sentence

**Not yet as a stable public reproducible certificate.** The 2026 literature now supplies strongly complementary pieces, and the 3 September 2026 ERG2026 presentation explicitly reports that a Lorentzian-resummed gravitational contact contribution has been combined with the mediated amplitude, but the canonical March preprint still omits `A4` and the conference-level extension does not yet provide the full public same-realization/error/comparator package required by RQIR.

The old statement “AS has no contact result” is therefore obsolete. The correct blocker is now **public reproducibility and same-realization closure**, not mere existence of a contact calculation.

## A. Knorr 2026: analytic contact-inclusive simplified realization

Primary authority:

- B. Knorr, *Asymptotically (un)safe scattering amplitudes from scratch: a deep dive into the IR jungle*, arXiv:2602.21285v2 (17 Mar 2026).

### Frozen realization

- flat background;
- Euclidean FRG followed by analytic continuation to Lorentzian kinematics;
- two shift-symmetric scalar species for the principal massless example;
- simplified running Newton coupling with one positive fixed-point parameter `g_*`;
- cosmological constant set to zero;
- scalar fluctuations neglected as internal quantum fluctuations;
- self-feedback of the generated scalar four-point form factor neglected;
- nontrivial gravitational propagator/vertex momentum dressings are not simultaneously resolved in the scattering object.

The effective action explicitly contains a gravity-induced scalar four-point form factor. In the analytic setup it reduces to a single form factor with `F1=-F2=F`, while `F3=F4=F5=0`.

### Scattering result

The paper computes a two-to-two scalar amplitude from first principles in this simplified AS setup. Its high-energy partial waves behave schematically as

`a0(s) ~ [(pi-4 g_*)/(12 pi)] G_N s + O(1)`

and

`a2(s) ~ -[(pi+8 g_*)/(60 pi)] G_N s + O(1)`.

For `g_*>0`, no fixed-point value simultaneously bounds both partial waves in this approximation. The paper explicitly concludes that the mere existence of an RG fixed point does not guarantee bounded physical scattering.

### RQIR classification

`FAIL_RQIR_GATE__SCOPED_AS_ANALYTIC_CONTACT_MODEL_PARTIAL_WAVE_BOUNDEDNESS`

This is a **scientific FAIL of the declared simplified realization/approximation**, not a FAIL of Asymptotic Safety as a family. The paper itself states that a more complete treatment must include momentum dependence of propagators and all relevant vertices before a final verdict on AS scattering can be drawn.

### Additional methodological lesson

The same work shows that a finite-order derivative expansion can reproduce fixed-point information while failing quantitatively for the physical `k->0` momentum dependence in massless theories, and that standard RG improvement fails qualitatively in this setup. RQIR therefore must not accept a derivative-expansion or RG-improved proxy as a substitute for the contact-complete physical scattering object.

## B. Chiesa–Pawlowski–Reichert 2026: full-momentum mediated realization

Primary authority:

- A. P. Chiesa, J. M. Pawlowski, M. Reichert, *Towards Two-to-Two Scattering of Scalars in Asymptotically Safe Quantum Gravity*, arXiv:2603.10168v1 (10 Mar 2026).

### Frozen realization

- one massless minimally coupled scalar;
- flat Euclidean background for FRG computation, reconstructed to Lorentzian signature;
- harmonic-Landau gauge;
- full momentum dependence of the scalar-scalar-graviton three-point vertex is computed in a projected classical tensor structure;
- full graviton propagator input is used through momentum-dependent dressings;
- the scalar scattering amplitude is built from dressed graviton-mediated channels;
- the paper explicitly uses approximations including a uniform graviton wave function, quenched matter contribution in the graviton two-point flow, and a simple trajectory for the three-graviton Newton avatar.

### Positive control

For identical-scalar scattering the general decomposition is

`A = A_s + A_t + A_u + A4`.

The paper computes the mediated sector `A_s+A_t+A_u`; crossing generates `t,u` from the `s` channel. Its non-perturbative cross section reduces to GR at low energies and remains compatible with the stated UV unitarity bound. The amplitude approaches a constant in the UV.

### Missing object in the canonical preprint

The paper explicitly states that it **neglects the direct contact term `A4`**, whose computation is deferred to forthcoming work. Hence arXiv:2603.10168v1 by itself does not satisfy the KMQGB contact-complete same-realization certificate.

### RQIR classification

`PASS_RQIR_GATE__SCOPED_AS_FULL_MOMENTUM_MEDIATED_SCATTERING_CONTROL__A4_EXCLUDED`

This is a strong positive control, but not a family-level PASS.

## C. ERG2026 update — 3 September 2026

Primary current authority:

- ERG2026, University of Sussex, 3 Sep 2026, Angelo Portas Chiesa, *Unitarity at all scales: Towards 2-to-2 scattering of scalars in Asymptotically Safe Quantum Gravity*.

The official conference description states that the mediated amplitude uses non-perturbative momentum-dependent resummed scalar-graviton vertices and propagators together with reconstruction/analytic continuation techniques, and that these are **corroborated by the gravitational contribution to the contact amplitude, resummed directly in Lorentzian signature**. It further states that the resulting non-perturbative amplitude/cross section is compatible with GR at low energies and respects unitarity in the UV.

This is a material update: it indicates that the missing `A4` programme has progressed beyond the March preprint.

### Why this still does not close the family row

The conference statement is not yet sufficient for the frozen KMQGB family-level object because the repository does not have a stable public authority containing, in one reproducible package:

1. the exact realization vector for the mediated and contact pieces;
2. explicit `A_s,A_t,A_u,A4` normalization and assembly;
3. proof that the contact term uses the same physical trajectory/renormalisation conditions as the mediated sector;
4. crossing/forward-limit prescription;
5. gauge/regulator/avatar/truncation robustness ledger;
6. uncertainty/error/reconstruction remainder;
7. public numerical/tabulated object or equations sufficient for independent reproduction;
8. identical-domain GR/EFT and alternative-QG comparator predictions and quotient.

The conference claim is therefore recorded as `PROMISING_NONCANONICAL_CONTACT_COMPLETE_UPDATE`, not as a terminal PASS.

## D. Same-realization lesson

The two March papers cannot be naively added together:

- Knorr resolves a gravity-induced four-scalar contact form factor in a deliberately simplified analytic system, while mediated propagation/vertices are not the same fully dressed objects used by Chiesa–Pawlowski–Reichert;
- Chiesa–Pawlowski–Reichert resolve the dressed mediated sector but explicitly omit `A4` in the published v1 paper.

Therefore

`A_mediated^(Chiesa) + A4^(Knorr)`

is **not** an RQIR-authorized same-realization amplitude.

The September ERG2026 result appears to be the first evidence that a contact-complete assembly may now exist within the Chiesa/Pawlowski/Reichert programme, but KMQGB must wait for a public reproducible realization certificate rather than infer equality from project continuity or conference wording.

## E. Refined AS blocker

Old blocker:

`STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`

Refined after Iter189:

`PUBLIC_REPRODUCIBLE_CONTACT_COMPLETE_AS_SCALAR_SCATTERING_SAME_REALIZATION_ERROR_ROBUSTNESS_COMPARATOR_CERTIFICATE`

Minimum payload:

- exact realization vector `{matter, signature, background, gauge, regulator, truncation, vertex basis, propagator input, trajectory/renormalisation conditions}`;
- normalized `A_s,A_t,A_u,A4` from that realization;
- contact/mediated identity proof;
- crossing and forward-limit handling;
- IR GR limit;
- UV partial-wave/cross-section unitarity result;
- gauge/regulator/avatar/truncation/reconstruction robustness;
- public reproducibility data or equations;
- identical-domain GR/EFT and alternative-QG comparators;
- comparator-subtracted residual/error budget.

## F. D7 consequence

`ASYMPTOTIC_SAFETY` remains `BLOCKED_MISSING_REQUIRED_OBJECT`.

However the blocker is materially narrower than before: **the question is no longer whether a contact amplitude exists at all, but whether the new contact-complete 2026 result can be frozen as a public same-realization, robustness-controlled, comparator-ready object.**

This Iter189 result contributes no family-level exclusion evidence toward `NEW_REQUIRED`. No RQIR Core change is required.
