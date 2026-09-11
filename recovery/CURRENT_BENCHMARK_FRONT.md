# Current Benchmark Front
Updated: 2026-09-11
Iteration: Iter280 Asymptotic Safety Lorentzian spectral-function reopen
Authoritative operational-saturation milestone: Iter270
Authoritative D7 infrastructure milestone: Iter272
Authoritative 15-row census synchronization milestone: Iter276

## Global lock
- RQIR Core v1.0 remains FROZEN.
- Tier-1 census = 15 families.
- Strict terminal coverage = 1/15.
- Strict nonterminal coverage = 14/15.
- Candidate-family terminal coverage = 0/14.
- Tier-2 unresolved = 0.
- D1 = PASS.
- D2 = NOT_CLOSED_COVERAGE_AND_OBJECTS.
- D3 = PARTIAL.
- D4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D5 = PASS.
- D6 = PASS_RULE_TARGETS_OPEN.
- D7 = NOT_CLOSED / NOT_YET_AUTHORIZED.
- D7-S0 = PASS.
- D7-S1 = PASS.
- D7-S2 = NOT_CLOSED.
- D7-S3 = NOT_CLOSED.
- D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED.
- D7-S5 = NOT_AUTHORIZED.
- D7-S6 = INACTIVE.
- Paper IV global decision = NOT_YET_AUTHORIZED.
- NEW_REQUIRED / EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED are not authorized.
- Candidate Gravity remains inactive at canonical R3 = 24%.

## Readiness metrics
- Operational polygon readiness = 100% (Iter270).
- D7 protocol infrastructure readiness = 100% (Iter272).
- 15-row decision-stack synchronization = validated (Iter276 and subsequent green methodology CI).

These are infrastructure/operational metrics, not scientific D7 closure.

## Recent material reopens

### Iter273 — LQG / spinfoam
Muxin Han, *Ultraviolet Fixed Point in Covariant Loop Quantum Gravity* (2026), supplies a complete summed-spinfoam continuum/fixed-point object. Scoped continuum result is positive. Family remains nonterminal because the same-realization physical UV-to-IR/GR trajectory, normalized gravity observable, parameter/refinement transport and comparator/error certificate remain missing.

### Iter274 — Asymptotic Safety contact-complete front
The stable Lorentzian scalar-scattering preprint supplies the mediated `s+t+u` contribution but omits direct `A4`; ERG2026 reports Lorentzian contact-term progress without a stable public reproducible contact-complete package. Family remains `BLOCKED_MISSING_REQUIRED_OBJECT`.

### Iter275–277 — RQCP
RQCP was promoted as a new independent Tier-1 parent, moving the census 14 -> 15 without increasing terminal coverage. Four-environment semantic reproduction passed. Iter277 then quantified an independent Hilbert/domain-cutoff resource axis: cutoff 8 -> 28 moves G by ~7.32%, gap by ~3.07%, and G*gap^2 by ~1.36%, while the high-cutoff sequence stabilizes strongly.

Methodological delta:
`MULTI_AXIS_RESOURCE_CLOSURE`

Every materially independent regulator/truncation/domain/finite-volume/resolution/approximation axis must be separately removed with propagated uncertainty or physically selected with propagated uncertainty. Closing one axis does not close another.

### Iter278 — Asymptotic Safety diffeomorphism-invariant PIRG
Ihssen, Knorr, Mezger, Pawlowski, Sprenger, arXiv:2609.07829v1.

Parallel Table-III audit run `34552838082`: 4/4 independent probes + aggregate success. Methodology CI run `34552838007`: success.

Scoped result:
`PASS_SCOPED_DIFFEO_INVARIANT_RELEVANCE_PRESERVING_REUTER_FIXED_POINT_WITH_TABLEIII_VARIANT_ROBUSTNESS__NOT_CONTACT_COMPLETE_NOT_UV_IR_COMPLETE`

All six published variants retain two positive relevant directions. This strengthens the Asymptotic-Safety evidence base but does not supply the missing public same-realization contact-complete `s+t+u+A4` package.

### Iter279 — Null Surface Formulation classification
The 2025–2026 NSF quantum/scattering line was tested under the frozen new-parent rule.

Parallel workflow run `34553257781`: 4/4 independent jobs + aggregate success. Methodology CI run `34553257768`: success. Final archival head `33b5914dc1136449bac21f739088fe3a65e6ade7` subsequently passed full methodology CI run `34553466935`.

Classification:
`REDUCED_TO_EXISTING_GR_PARENT__NEW_REALIZATION_NOT_NEW_TIER1_PARENT`

No 16th Tier-1 row was created. UV-finite perturbative/integration behavior is not silently substituted for bounded fixed-angle amplitude, forward regularity, or all-order equivalence.

### Iter280 — Asymptotic Safety Lorentzian graviton spectral function
Peer-reviewed primary object: Pawlowski, Reichert, Wessely, *Physics Letters B* 880 (2026) 140844, DOI `10.1016/j.physletb.2026.140844`.

Parallel workflow `asymptotic-safety-spectral-unitarity-audit`, run `34553743544`: 4/4 independent jobs + aggregate success. Methodology CI run `34553743421`: preflight + 4/4 shards + aggregate/bundle success.

Scoped result:
`PASS_SCOPED_POSITIVE_NORMALISABLE_LORENTZIAN_TT_GRAVITON_SPECTRAL_FUNCTION_WITH_UNIT_WEIGHT__NOT_PHYSICAL_HILBERT_SPACE_NOT_CONTACT_COMPLETE_NOT_FULL_CURVE_INDEPENDENTLY_REPRODUCED`

Key KMQGB checks:
- `g*=0.9554263372261876` and Eq.23–25 trajectory consistency;
- the `1/[lambda^2 log^3(lambda^2)]` UV spectral tail is sum-rule integrable;
- reported `z_spec≈1.486` implies ~67.29% pole and ~32.71% continuum weight after the stated physical rescaling;
- `2*pi*(61/(60*pi)) = 61/30` reproduces the reported IR onset relation.

Scope boundary:
- the source explicitly states that the fluctuation-graviton states are not diffeomorphism invariant and are not part of the physical Hilbert space;
- publisher data are available on request and no public article-specific numerical dataset/reference implementation was located, so the full numerical spectral curve is not independently reproduced in Iter280;
- the contact-complete `s+t+u+A4` scattering blocker remains active and independent.

Asymptotic Safety therefore remains `BLOCKED_MISSING_REQUIRED_OBJECT`; terminal count unchanged.

## Publication handoff
`recovery/PUBLICATION_IMPACT_LEDGER.md` is authoritative for manuscript impact.

Current required changes:
- Paper III: Iter277 `MULTI_AXIS_RESOURCE_CLOSURE` = `READY`; modest general methodological strengthening.
- Paper III: Iter278–280 = `NOT_NEEDED` as additional rules; optional corroboration only.
- Paper IV: Iter277 RQCP, Iter278 PIRG Asymptotic Safety, Iter279 NSF reduction case, and Iter280 Lorentzian spectral result = `READY` for inclusion.

## Current scientific decision state
- 15 Tier-1 families remain in the canonical census.
- 1/15 is strict terminal in its declared benchmark domain (GR + controlled low-energy EFT baseline).
- 0/14 candidate-QG families are strict terminal.
- Remaining families are PARTIAL/BLOCKED/nonterminal; this is not equivalent to refutation.
- D7-S2/S3/S4 remain open, therefore no global adaptation/new-theory verdict is authorized.

## Current compute policy
Do not repeat saturated grids solely to create runner activity. When a new object admits independent tests, shard them immediately and aggregate only after a dependency barrier. Literature-only missing objects remain external-authority blockers rather than excuses for artificial compute.

## Exact next gate
`D7_S2_EXTERNAL_AUTHORITY_DRIVEN_TERMINALIZATION_WITH_MULTI_AXIS_RESOURCE_CLOSURE_AND_EXPLICIT_REDUCTION_MAPS`

Priority:
1. stable public contact-complete Asymptotic-Safety `s+t+u+A4` package;
2. LQG same-realization physical UV-to-IR/GR observable/transport package;
3. RQCP all-band/background-independent autonomy bridge with Hilbert-cutoff closure;
4. other Tier-1 families only when new primary authority can materially change family classification;
5. any apparently new QG parent must first pass an explicit reduction/equivalence audit before census promotion.
