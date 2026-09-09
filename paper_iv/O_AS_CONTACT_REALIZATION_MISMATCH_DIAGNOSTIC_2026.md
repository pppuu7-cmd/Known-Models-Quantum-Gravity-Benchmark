# O-AS Contact-Realization Mismatch Diagnostic — 2026-09-10

**KMQGB iteration:** 158  
**RQIR standard:** Core v1.0 FROZEN  
**Closure-wave target:** CW2-01 / O-AS.

## Question

Can the published analytic contact-term calculation in Benjamin Knorr, arXiv:2602.21285, be inserted as `A4` into the non-perturbative Lorentzian mediated amplitude of Chiesa–Pawlowski–Reichert, arXiv:2603.10168?

## Answer

**Not without an explicit same-realization derivation.**

## Mismatch 1 — scattering process / crossing structure

The analytic control of arXiv:2602.21285 develops a simple scalar-scattering model and explicitly discusses a channel such as

`phi phi -> chi chi`

with distinct scalar species. The 2603.10168 programme discusses identical-scalar scattering and assembles `s`, `t`, `u` exchange channels plus a direct contact term.

A four-scalar contact function from the distinct-species setup is therefore not automatically the identical-scalar crossing-complete `A4`.

## Mismatch 2 — effective-action truncation

The analytic contact calculation uses a deliberately simplified form-factor setup to keep the system analytically tractable. In particular, gravitational and non-minimal form factors are neglected/approximated in declared places, while the four-scalar sector is parameterized by its own form factors.

The Chiesa–Pawlowski–Reichert result instead computes a full momentum-dependent scalar–graviton 1PI vertex and combines it with dressed graviton information before Lorentzian reconstruction.

Thus the two pieces do not currently share one frozen truncation/vertex basis.

## Mismatch 3 — RG trajectory / normalization

A valid splice would require proof that the contact form factors and mediated vertex/propagator lie on the same AS trajectory and use compatible Newton-coupling, field-normalization, renormalisation-condition and Lorentzian conventions.

Shared framework membership is not enough.

## Mismatch 4 — error budget

The analytic contact control is valuable precisely because it exposes failures of derivative expansion and standard RG improvement. Those findings imply that a contact term derived in a simplified approximation cannot be promoted into the full physical amplitude without propagating the approximation uncertainty.

## Classification

`CONTACT_CONTROL_EXISTS__SAME_REALIZATION_MATCH_NOT_PROVEN`.

CW2-01 remains open.

## Exact next O-AS authority

The shortest closure path is now one of:

1. an updated Chiesa–Pawlowski–Reichert preprint/publication containing the direct contact contribution in the same calculation;
2. a stable ERG2026 presentation/data package that explicitly defines the contact term in the identical realization and gives enough formula/data authority for reproduction;
3. a paper deriving an explicit map from the Knorr contact sector to the Chiesa mediated realization, including crossing/species, normalization and approximation propagation.

Until then, `A_complete=A_mediated+A4_control` is unauthorized.
