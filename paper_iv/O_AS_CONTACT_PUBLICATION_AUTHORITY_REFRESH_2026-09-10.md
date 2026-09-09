# O-AS Contact-Publication Authority Refresh — 2026-09-10

**KMQGB iteration:** 171  
**RQIR standard:** Core v1.0 FROZEN  
**CW2 object:** CW2-01 / O-AS

## Question

Has the remaining asymptotic-safety contact contribution moved from a merely anticipated ingredient to a sufficiently stable same-realization authority that can close

`SAME_REALIZATION_CONTACT_COMPLETE_DIFFEO_ERROR_CONTROLLED_LORENTZIAN_SCALAR_SCATTERING_CERTIFICATE`?

## Stable preprint authority

Chiesa, Pawlowski & Reichert, arXiv:2603.10168, remains the stable inspectable preprint authority for the mediated scalar-scattering calculation.

It explicitly defines

`A = A_s + A_t + A_u + A_4`

but states that the published calculation focuses on `A_s+A_t+A_u` and neglects the direct contact term `A_4`. The latter is assigned to separate work by Chiesa & Reichert, `in preparation (2026)`.

Therefore the stable preprint by itself still does **not** close CW2-01.

## August–September 2026 public-progress authority

A public NExT PhD Workshop programme on 24 August 2026 lists a new presentation of the same scalar-scattering programme by Angelo P. Chiesa and provides presentation material (`scalar-grav-NeXT.pdf`).

More importantly, the ERG2026 contribution on 3 September 2026 explicitly states that the mediated amplitude is complemented/corroborated by the **gravitational contribution to the contact amplitude**, which is resummed **directly in Lorentzian signature**, and that the resulting cross section remains GR-compatible in the IR and compatible with unitarity in the UV. ERG2026 also exposes presentation material (`scalar-grav-ERG-26.pdf`).

This is a genuine authority upgrade relative to the March preprint: the contact sector is no longer only a future-work placeholder at the programme level.

## What this closes

The following narrower uncertainty can now be retired:

`DOES_THE_CHIESA_REICHERT_PROGRAMME_HAVE_A_Lorentzian_CONTACT_CONTRIBUTION?`

Programme-level answer: **yes, publicly reported by September 2026**.

This materially contracts CW2-01.

## What remains open

RQIR does not score a programme claim or conference abstract as a composed physical observable. The following are still missing from a stable, inspectable same-realization package:

1. explicit `A_4` equations or equivalent reproducible numerical object;
2. proof that `A_4` uses the same scalar species, external-state convention and crossing prescription as the mediated `A_s+A_t+A_u` result;
3. identical or explicitly mapped RG trajectory/fixed-point branch and renormalisation conditions;
4. common physical normalization and Lorentzian prescription;
5. propagation of flow/truncation/reconstruction/contact-sector errors into the **full** amplitude/cross section;
6. same-domain GR/EFT comparator for the full contact-complete observable.

The March arXiv record is still the stable calculation and remains contact-incomplete. No standalone Chiesa–Reichert contact preprint or contact-complete arXiv revision was found in the 2026-09-10 authority refresh.

## Updated classification

`PROMISING_SAME_PROGRAMME_CONTACT_COMPLETE_PRESENTATION__REPRODUCIBLE_SAME_REALIZATION_CERTIFICATE_MISSING`

CW2-01 remains **OPEN** and contributes zero terminal closure.

## Exact blocker after Iter171

The blocker is sharpened from generic contact availability to

`STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`.

This is narrower than the Iter154/153 blocker because programme-level existence of a Lorentzian-resummed contact contribution is now directly public.

## Compute decision

Heavy computation remains **IDLE**. A numerical KMQGB campaign would still have to invent the missing `A_4` realization or error map and would therefore contaminate the benchmark with model-building assumptions.

## Next search trigger

CW2-01 should be re-audited immediately if any of the following appears:

- a Chiesa–Reichert standalone contact-amplitude preprint;
- a new arXiv version of 2603.10168 including `A_4`;
- publicly inspectable ERG/NExT equations/data sufficient to bind realization, normalization and error propagation.

Until then, do not synthesize `A_complete` by splicing other AS contact calculations into arXiv:2603.10168.
