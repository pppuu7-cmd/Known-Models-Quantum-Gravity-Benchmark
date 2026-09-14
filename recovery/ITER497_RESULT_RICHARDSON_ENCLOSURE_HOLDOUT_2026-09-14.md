# Iter497 terminal result — Richardson enclosure holdout

Authority: prereg `3209cdadeed3dc7d5c1ceb12d72e8841fb688901`; evaluator `742199df295815841725820052aad6a468786ee9`; aggregate implementation `359492922a100582994dc6eb5e44845761b987d2`; production head `a7517b7fcd12e3a1a129a16881ee3e348a7b72e8`; run `34811898887`; aggregate artifact `10336250420`; digest `sha256:1804657dd14eb939da835c0c8f0eca84a5a93d76014f11016b0f642bcad19f0f`.

Terminal classification: `ITER497_RICHARDSON_ENCLOSURE_HOLDOUT_QUALIFIED_SCOPED`.

All 12 frozen causal×direction-block lanes are present and valid. Aggregate contains 192 frozen sign/rho/direction states and 768 independent holdouts. `768/768` holdouts are covered by the prospectively frozen Richardson enclosure; worst coverage ratio is `0.483944238351976`, leaving >2x margin to the frozen boundary. All training predicates, source predicates and frozen predicates pass; no job is missing or invalid.

The envelope is exactly the preregistered one: training amplitudes `{0.00125,0.0025}`, holdouts `{0.00150,0.00175,0.00200,0.00225}`, coefficient stencils `{0.0050,0.0025,0.00125}`, Richardson coefficients `(4*C_0.00125-C_0.0025)/3`, cubic safety factor `2`, and coefficient uncertainty propagated by triangle inequality. No post-hoc h, amplitude, direction, rho, exponent or safety-factor tuning is admitted.

Scientific interpretation: the finite independent holdout blocker after Iter496 is materially narrowed. The frozen local q=1 Richardson enclosure has survived all predeclared holdouts with stable finite-grid margin. This is not a continuous interval/uniform-neighborhood certificate and does not establish positive Haar measure, absolute Haar convergence/divergence, D7-S2 closure, source spectral admissibility, or a terminal D7 classification.

Scope guards remain: D7-S2 `NOT_CLOSED`; D7-S3 `NOT_CLOSED`; D7-S4 `PARTIAL_GLOBAL_NOT_CLOSED`; `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` forbidden; Candidate Gravity inactive. Ten-source spectral normalization/order/i-epsilon, Iter461 K5 collision geometry, and PV/conditional/distributional admissibility remain independent blockers.

Next authorized dependent gate: a prospectively frozen genuinely continuous/validated interval or otherwise mathematically certified uniform-neighborhood step. A dense sample alone must not be called an interval certificate.
