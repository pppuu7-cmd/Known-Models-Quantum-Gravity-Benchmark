# Asymptotic Safety diffeomorphism-invariant PIRG reopen audit — Iter278

Date: 2026-09-11
Family: `ASYMPTOTIC_SAFETY`
RQIR Core: `v1.0 FROZEN`
D7 stage: `D7-S2 STRICT_TIER1_TERMINAL_COVERAGE`

## Reopen trigger

A new primary preprint appeared after the earlier Asymptotic-Safety contact-term audit:

- Friederike Ihssen, Benjamin Knorr, Silas Mezger, Jan M. Pawlowski, Paul P. Sprenger, **Diffeomorphism-invariant Approach to Asymptotically Safe Quantum Gravity**, arXiv:`2609.07829v1`, submitted 2026-09-07.

The work introduces a physics-informed renormalisation-group construction intended to maintain quantum diffeomorphism invariance and relevance counting throughout the flow, and computes a Reuter fixed point in that formulation. This is a material new object for the background-independence / symmetry / relevance-counting side of the Asymptotic-Safety family.

It is not the missing contact-complete scalar-scattering package from Iter274, so the bounded question is not whether it automatically terminalizes the family. The bounded question is whether the new object supplies a new scoped positive control and whether its own published variants expose material approximation/procedure sensitivity relevant to the KMQGB resource-closure judge.

## Frozen Table-III numerical object

The six published Table-III variants were transcribed into `code/as_pirg_table3_common.py`. Four independent descriptive probes were then run in parallel:

1. global/by-action fixed-point dispersion;
2. near-canonical critical-exponent/relevance counting;
3. matched action/procedure comparisons;
4. decomposition of documented beta-g completion versus flow/Nielsen procedure sensitivity.

No terminal PASS/FAIL threshold is encoded in these probes. They quantify the published finite set and preserve a separate interpretation boundary.

Workflow: `asymptotic-safety-pirg-table3-audit`
Run: `34552838082`
Head: `4c775ea7c2af2f84e1d8b181a45cf87b967cdf61`

Result: 4/4 independent jobs `SUCCESS`; aggregate after the dependency barrier `SUCCESS`.

The same head was independently checked by `methodology-ci` run `34552838007`: preflight, 4/4 methodology shards, and aggregate/bundle all `SUCCESS`.

## Quantitative result

Across all six Table-III variants:

- all six preserve two positive relevant directions;
- `theta_1` ranges from 3.70 to 6.68, population CV relative to its absolute mean about `0.2181`;
- `theta_2` ranges from 1.81 to 2.07, population CV about `0.04863`;
- fixed-point `g_*` ranges from 1.130 to 3.339, population CV about `0.3528`;
- fixed-point `lambda_*` spans -0.638 to +0.135 and even changes sign across the finite published variant set.

Relative to the canonical reference `(theta_1, theta_2)=(4,2)`, all rows retain the same relevance count. Five of six have moderate deviations; the `Gamma^(a)` Nielsen/back row has the clear largest first-exponent deviation, `theta_1=6.68`, or about +67% relative to 4, while its second exponent remains only about -6.5% from 2.

The matched comparisons therefore support a specific robustness hierarchy: the **number/sign of relevant directions and especially the second critical exponent are substantially more stable than the fixed-point coordinates**, while the first exponent contains a visible procedure-sensitive outlier.

This is a scoped positive result for relevance-counting robustness, not evidence that approximation/systematic uncertainty is negligible.

## Upstream scope boundary

The preprint itself does not present the present Einstein-Hilbert-level calculation as complete quantum gravity closure. Among the still-open items discussed in the source are higher-curvature/operator completion, a more complete operator map between formulations, fuller control of approximation/systematic effects, and UV-to-IR phase structure beyond the present approximation.

KMQGB therefore must not use the new PIRG result to bypass the existing same-realization observable requirement.

## Scoped result

`PASS_SCOPED_DIFFEO_INVARIANT_RELEVANCE_PRESERVING_REUTER_FIXED_POINT_WITH_TABLEIII_VARIANT_ROBUSTNESS__NOT_CONTACT_COMPLETE_NOT_UV_IR_COMPLETE`

Family-level status remains:

`BLOCKED_MISSING_REQUIRED_OBJECT`

The active Iter274 scattering blocker remains decisive for terminalization:

`BLOCKED_PENDING_PUBLIC_CONTACT_COMPLETE_S_PLUS_T_PLUS_U_PLUS_A4_LORENTZIAN_SCATTERING_CERTIFICATE_WITH_FORWARD_LIMIT_TREATMENT_APPROXIMATION_UNCERTAINTY_BUDGET_AND_SAME_DOMAIN_COMPARATORS`

The new PIRG object attacks a different, important conceptual axis; it does not supply `A4`, a complete `s+t+u+A4` observable, or the corresponding reproducibility/comparator certificate.

## D7 consequence

- Tier-1 census remains `15`.
- Strict terminal coverage remains `1/15`.
- Candidate-family terminal coverage remains `0/14`.
- `ASYMPTOTIC_SAFETY` remains nonterminal / `BLOCKED_MISSING_REQUIRED_OBJECT`.
- D7-S2 remains `NOT_CLOSED`.
- D7-S3 remains `NOT_CLOSED`.
- D7-S4 remains `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7-S5 remains `NOT_AUTHORIZED`.
- Candidate Gravity remains inactive at canonical R3 `24%`.

No `NEW_REQUIRED`, `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, or `HYBRID_REQUIRED` conclusion is authorized.

## Methodological consequence

Iter278 does **not** create a new general RQIR failure mode beyond Iter277's `MULTI_AXIS_RESOURCE_CLOSURE`. Instead it independently reinforces that rule: robust relevance counting can coexist with materially scheme/procedure-sensitive coordinates and a non-comprehensive uncertainty budget.

The scientifically correct publication consequence is therefore:

- Paper III: no second new rule is needed; Iter277's general multi-axis/resource-closure strengthening is sufficient. Iter278 may be used only as corroborating motivation if helpful.
- Paper IV: include the new primary source and this scoped numerical audit as a material positive reopen of Asymptotic Safety, while preserving the nonterminal blocker.

## Provenance

Scientific workflow artifact digest for aggregate: `sha256:6452b6bb77549182e4ca6aeaff8c3ddfd892b2380cd093b455df89726019a6a7`.

Primary source: `https://arxiv.org/abs/2609.07829`

Earlier contact-term audit: `paper_iv/P_ASYMPTOTIC_SAFETY_CONTACT_COMPLETE_REOPEN_AUDIT_ITER274_2026-09-11.md`

## Audit conclusion

The September-2026 PIRG result materially strengthens the Asymptotic-Safety evidence base on quantum diffeomorphism invariance, background independence and relevance counting. Independent KMQGB evaluation of the six published Table-III variants confirms stable relevance counting, with a notably stable second critical exponent, but also quantifies substantial coordinate and first-exponent procedure sensitivity. The correct KMQGB outcome is a **new scoped positive control with no terminal-count change**.