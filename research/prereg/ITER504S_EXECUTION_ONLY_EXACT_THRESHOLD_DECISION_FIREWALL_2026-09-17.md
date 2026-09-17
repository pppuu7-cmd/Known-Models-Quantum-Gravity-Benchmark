# Iter504S — execution-only exact-threshold decision firewall

Date: 2026-09-17
Status: PROSPECTIVELY FROZEN WHILE REPAIRED RUN 35175533159 IS NONTERMINAL AND BEFORE CONSUMING PARTIAL SCIENTIFIC VALUES

Scientific preregistration remains exactly:

`f6367456aa715fe6282ab70c1b2005971a4568c7`

Existing execution-only repair authorities remain:

- derivative extraction `88c92f86a765e9d8b441152674fc2c303f3f1ff3`;
- fixed-channel drift semantics `4ef41c0f4ceed3082fd4d80930ef5d848f18802b`.

This record changes no scientific threshold, cohort, point, source, formula, or terminal class. It freezes a source-level rigor firewall discovered independently of the nonterminal output.

## Outcome-blind source-level mismatch

The scientific threshold is the exact decimal/rational value

`0.05 = 1/20`.

The repaired root evaluator computes the full-envelope and derivative-radius predicates directly with Arb objects, e.g. `du <= arb('0.05')`. Those producer booleans are rigorous.

However, the fixed-channel convenience predicate currently serializes an Arb upper endpoint through `core.bound_float(..., 'upper')` and then tests

`float(max_fixed_channel_drift_upper) <= 0.05`.

The assembler and adversarial Critic repeat the same binary64 comparison.

This is not formally identical to the preregistered Arb inequality. In CPython binary64,

`0.05.as_integer_ratio() = 3602879701896397 / 72057594037927936`

which exceeds exact `1/20` by

`1 / 360287970189639680`.

Therefore a sufficiently near-threshold value can in principle be assigned a different fixed-channel truth value after binary64 conversion. In addition, selecting a maximum after conversion can collapse distinct high-precision endpoints to the same binary64 value.

The issue was found by static source audit only. No partial mechanism number from run `35175533159` was consumed to discover or define this firewall.

## Dependency-localized authority rule for the running execution

Do not cancel, mutate, or duplicate run `35175533159`.

After it becomes terminal:

1. If its terminal class is `ITER504S_ROOT_DERIVATIVE_RADIUS_LOCALIZED_SCOPED`, the fixed-channel all-within predicate is not on the winning classifier dependency path. The result may remain scientifically authoritative provided the existing assembler and Critic both confirm the producer exact-Arb full-envelope/derivative-radius booleans with no errors and both environments agree.
2. If its terminal class is `ITER504S_CHANNEL_COMPETITION_NECESSARY_SCOPED`, `ITER504S_FIXED_CHANNEL_NONSTATIONARITY_REMAINS_SCOPED`, or `ITER504S_MIXED_MECHANISM_SCOPED`, do not promote that mechanism class from this execution. These branches depend on the fixed-channel threshold predicate and require the exact-threshold repair below.
3. Any `ITER504S_INVALID`, failed aggregate, failed Critic, or cross-environment decision disagreement remains INVALID and is not converted into a scientific FAIL.

This conditional rule is frozen before the terminal outcome, so it cannot be selected to preserve a favorable class.

## Frozen minimal exact-threshold repair

If repair is required by the dependency rule above, the next execution may change only threshold-decision transport/verification:

1. During fixed-channel computation, keep each `du` as an Arb object until the scientific predicate has been evaluated.
2. Define each channel flag only by the exact Arb predicate `du <= arb('0.05')`.
3. Define `all_candidate_fixed_channel_drifts_within_tolerance` as `complete AND candidates_nonempty AND all(exact_channel_flags)`; never reconstruct this boolean from a serialized float maximum.
4. Serialize a deterministic `violating_channel_indices` list (or equivalently all per-candidate exact boolean flags) so downstream consumers can verify the logical reduction without comparing binary64 values to the threshold.
5. `max_fixed_channel_drift_upper` remains display/diagnostic metadata only. Its binary64 representation may not decide any scientific class.
6. Assembler and independent Critic must reconstruct competition/nonstationarity solely from candidate completeness plus the serialized exact-Arb channel decision set. They must reject any mismatch between the all-within boolean and that decision set.
7. Full-envelope and derivative-radius predicates must continue to be computed in Arb at the producer. Binary64 fields remain diagnostics only; downstream checks may confirm that float summaries are consistent away from the threshold but may not redefine the scientific inequality.
8. Preserve `python-flint==0.9.0`, 384-bit precision, all 243 channels, exact LOW/MID/HIGH points, roots 13-15, rhos/R grid, source path, no-pruning rule, exact threshold `1/20`, floor `+1`, and the already frozen terminal classifier order.

## Execution firewall

No second Iter504S execution is authorized while run `35175533159` is nonterminal.

If a repaired execution becomes necessary after terminalization, freeze repaired evaluator/assembler/Critic hashes and a single repaired workflow authority before launching it. Do not use the first run's numerical values to alter thresholds, points, channels, depth, precision, cohort, or classifier order.

## Claim ceiling

This is an execution-rigor firewall only. It makes no Iter504S mechanism claim, does not change Iter504R, does not reclassify the 1888 parent states, does not close D7, and does not establish quantum gravity or new physics.
