# SOURCE_J1_K5_EQ4_IMPROPER_DISTRIBUTIONAL_EXISTENCE_GATE — prospective preregistration

Date: 2026-09-15
Status: PREREGISTERED; NO RESULT YET
Parent authority: `recovery/CURRENT_BENCHMARK_FRONT.md` at main `bcfc5c1371780ed6a57bc19bdd11cd61472be9ac` or fresher main if navigation-only commits follow.

## Purpose

Test **existence separately from uniqueness/selection** for the published Eq. (4) object assembled from the already source-defined one-wedge Toller distributions at the full K5 collision, without adding model data. This gate must not infer nonexistence merely because a sufficient product criterion fails.

## Frozen scope

- source order: fixed `j=1` realization already used by the confirmed collision witness;
- nonzero real rho scope only where required by the frozen upstream realization;
- fixed channel `00000`;
- full K5 collision stratum only;
- source-defined one-wedge distributions are upstream premises, not re-fit objects;
- no Candidate Gravity, no terminal D7 classifier, no EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED;
- do not consume partial Iter504 or Iter461 substantive values.

## Mandatory upstream controls

1. Preserve source identity of each one-wedge factor.
2. Preserve `T+ + T- = D` at the distributional level; any implementation that checks this only pointwise away from the singular support is INVALID_IMPLEMENTATION.
3. Preserve the independently reviewed scoped collision witness and its scope; do not reinterpret it as proof that a base joint extension exists.
4. Preserve the repaired Eq4 authority-v2 result as a source/object-definition BLOCKED result, not a scientific FAIL.

## Frozen decision ladder

The implementation must evaluate the following in order and record evidence for every row.

### E1 — source-defined joint prescription
Determine whether the frozen source corpus itself defines a joint K5 product/pullback/regulator-removal prescription at the full collision. If yes, test that prescription directly. If absent, record `NO_SOURCE_PINNED_JOINT_PRESCRIPTION`; absence alone is not nonexistence.

### E2 — sufficient microlocal existence criterion
For the exact frozen factors, test an explicitly stated sufficient product/pullback criterion (e.g. the relevant Hörmander wavefront-set exclusion) only to the extent its hypotheses are actually established by source-derived or prospectively computed wavefront data.

Possible row outcomes: `SUFFICIENT_CRITERION_PASSES`, `SUFFICIENT_CRITERION_FAILS`, `CRITERION_NOT_EVALUABLE_FROM_FROZEN_DATA`.

**Critical guard:** `SUFFICIENT_CRITERION_FAILS` MUST NOT map to nonexistence.

### E3 — constructive improper/distributional existence route
If E2 does not establish existence, test a prospectively specified construction that does not add model data: for example a source-faithful common/independent regularization family whose distributional limit is evaluated against a frozen separating test-function basis. Regulator/path/order choices may be used diagnostically, but an arbitrary choice cannot be promoted to source authority.

A constructive PASS requires convergence in the declared distribution topology for the frozen test family plus stability under the preregistered refinement sequence. Pointwise convergence away from collision is insufficient.

### E4 — genuine nonexistence criterion
A `NONEXISTENCE_SCOPED` outcome is permitted only if a prospectively frozen theorem/criterion gives a necessary obstruction and all of its hypotheses are established for this exact object. Failure of a sufficient criterion, divergence of one arbitrary regulator path, numerical overflow, or missing product authority are explicitly forbidden as nonexistence evidence.

## Frozen terminal classifications

Exactly one of:

- `SOURCE_J1_K5_EQ4_DISTRIBUTIONAL_EXISTENCE_ESTABLISHED_SCOPED` — a source-defined or source-faithful constructive distribution exists in the frozen scope and mandatory controls pass.
- `SOURCE_J1_K5_EQ4_DISTRIBUTIONAL_NONEXISTENCE_ESTABLISHED_SCOPED` — a prospectively frozen necessary obstruction is satisfied; this is intentionally a high bar.
- `SOURCE_J1_K5_EQ4_DISTRIBUTIONAL_EXISTENCE_BLOCKED_SCOPED` — no source-pinned joint prescription and neither existence nor nonexistence is established by the frozen admissible routes.
- `SOURCE_J1_K5_EQ4_DISTRIBUTIONAL_EXISTENCE_INCONCLUSIVE_SCOPED` — admissible computations terminate but do not separate the above outcomes.
- `INVALID_IMPLEMENTATION` — frozen contract/controls are not actually evaluated.
- `INFRASTRUCTURE_FAILURE` — execution/provenance failure before a scientific classifier is valid.

## Outcome-sensitive implementation requirements

- No terminal predicate may be a hard-coded boolean or inferred from mere presence/absence of prose strings.
- Every decisive predicate must be produced from parsed structured source facts, exact/symbolic derivation, or explicit numerical certificate with tolerances fixed before result-producing execution.
- Include at least one positive and one negative implementation control capable of flipping the relevant decision path.
- If numerical lanes are used, independent lanes must use a matrix with `fail-fast: false`; safe parallelism should be maximized without oversubscribing the existing heavy Iter504/Iter461 queue.
- Aggregate only terminal artifacts; missing/cancelled lanes are not zero residuals.
- First causal failure must be classified infrastructure vs numerical-method vs scientific before rerun/repair.

## Governance

This gate can at most change the scoped D7-S2 evidence ledger. It cannot close D7-S2 family-wide by itself. D7-S3 and D7-S4 remain untouched unless a later prospectively registered gate says otherwise. Candidate Gravity remains inactive.

## Next implementation step

Implement an outcome-sensitive certificate that first reconstructs the exact frozen one-wedge distribution identities and available wavefront/product data, then evaluates E1/E2. Only if E2 does not establish existence should a separate prospectively frozen constructive E3 numerical/symbolic batch be launched. Do not combine an unvalidated guessed regulator with the source object in the same terminal gate.