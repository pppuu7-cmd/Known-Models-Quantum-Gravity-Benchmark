# Iter504U pre-execution source audit

Date: 2026-09-17
Status: `FROZEN_BEFORE_ANY_ITER504U_SCIENTIFIC_EXECUTION`

## Reviewed object

Gate: `ITER504U_HELDOUT_LOCAL_D_GENERALIZATION_FIREWALL`

Preregistration: `05b8e9354c9a7805f0fce18b904346a986a0787f`

Parent independent Critic: `8624532254981fbea6f8fcfac09cd538e2066aa4`, verdict `CONFIRMED_SCOPED` for the exact-run Iter504T decision-canonicalization authority.

Methodology CI: Actions run `35246378450`, terminal `completed/success`.

At the time of this audit no Iter504U held-out scientific execution has been authorized or launched and no held-out local-D scientific output has been consumed.

## Outcome-blind checks

1. The six held-out identities are hard-coded exactly as preregistered and do not depend on runtime values.
2. Development boxes `13,14,15` are explicitly forbidden as held-out cases.
3. Box intervals are exact rationals inherited from the parent definition `(16+k)/12800 .. (17+k)/12800`.
4. Parent direction/sign mapping is consumed from the unchanged Iter504 parent `path_spec` and independently hard-checked by assembler/Critic.
5. Base source realization `iter499/500/501/503/504` is byte-identical to exact repair head `10ae6bcc8447d14cecc6e550065504b23f792953`; methodology CI verifies this with Git object identities.
6. Precision, 243-channel completeness, R/rho cohorts, threshold `1/20`, floor `1`, deterministic dyadic subdivision and `MAX_DEPTH=3` are frozen before execution.
7. Every visited interval constructs a fresh interval dual amplitude and recomputes the local derivative object directly; the root/development derivative enclosure is not reused.
8. Producer scientific decisions use Arb comparisons before serialization; ordinary float bounds are display-only.
9. C4 binding is explicit in the new producer: `leaf.certified = all(rho.certified for rho in leaf.per_rho)`.
10. Assembler and independent Critic both independently recompute the C4 binding and exact dyadic cell identity.
11. Possible-max channel sets are transported as identities/diagnostics and are not pruning authority.
12. Parent-child derivative inclusion is retained as a control record but is not made a prerequisite for scientific certification; failure of inclusion is not silently reinterpreted as physics failure.
13. The Critic has frozen negative controls for wrong case identity, development-case insertion, missing held-out case, threshold/floor/depth/channel changes, wrong R/rho cohorts, derivative reuse, float decision transport, non-dyadic partition, C4 contradiction and removed binding tag.
14. PASS requires zero unresolved leaves across all six cases; valid unresolved leaves at depth 3 map to INCONCLUSIVE, not FAIL.
15. Cross-environment authority compares exact structural/decision projections, not display floats.

## Implementation identities reviewed

- held-out case evaluator blob `bf457eef08f7df32523c9e22ce3b3713f10d97a0`;
- environment assembler blob `5c3b04f25c5fb2523c3788b725ccf84ca23a07f1`;
- cross-environment aggregate blob `23165f9d99ff9a2f90c27a51cb889d5920327f92`;
- independent Critic blob `c2a7ea31ddc151bf02a3995d761cae95bdabd0db`;
- prepared scientific workflow blob `16fc117606916664dab2aac0d9a501d65bf4edae`.

## Methodology CI result

Run `35246378450` completed successfully. Its substantive checks passed:

- syntax of all four Iter504U code paths;
- exact frozen cohort strings;
- exact science constants and labels;
- explicit leaf/per-rho binding;
- required negative-control hooks;
- ancestry of preregistration, parent Critic, outcome-blind toolkit and exact repair head;
- byte-identical base source realization relative to exact repair head `10ae6bcc8447d14cecc6e550065504b23f792953`.

## Pre-execution verdict

`ITER504U_PREEXECUTION_METHODOLOGY_VALID_SCOPED`

No source-level mismatch with the frozen held-out contract was found before execution.

This is methodology/provenance readiness only. It is not a scientific PASS and contains no held-out outcome.
