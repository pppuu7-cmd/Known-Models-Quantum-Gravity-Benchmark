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

The repaired root evaluator initially computes each full-envelope slope/drift enclosure with Arb and evaluates the composite `within_tolerance` boolean with exact Arb inequalities. However, it then serializes `S_lower`, `drift_upper`, and fixed-channel drift bounds through `core.bound_float(...)`. Several scientifically active mechanism predicates are subsequently reconstructed from those binary64 summaries rather than from exact Arb truth values. This includes:

- `derivative_radius_sensitivity` via serialized full-D and center-D `drift_upper`;
- full-D and center-D violation tests used by the terminal classifier;
- fixed-channel `all-within` competition tests via serialized maximum fixed-channel drift;
- corresponding assembler and adversarial-Critic reconstructions.

The core module itself labels ordinary Arb-to-float conversion as display-only and not suitable for validated decisions. Therefore the current Iter504S scientific classifier transport is not fully interval-rigorous at the exact threshold.

This is not formally equivalent to the preregistered Arb inequality. In CPython binary64,

`0.05.as_integer_ratio() = 3602879701896397 / 72057594037927936`

which exceeds exact `1/20` by

`1 / 360287970189639680`.

Thus a sufficiently near-threshold exact upper bound can in principle be assigned a different truth value after binary64 conversion. Converting before selecting a fixed-channel maximum can also collapse distinct high-precision endpoints to the same binary64 value.

The issue was found by static source audit only. No partial mechanism number from run `35175533159` was consumed to discover, broaden, or define this firewall.

## Authority rule for the running execution

Do not cancel, mutate, or duplicate run `35175533159`.

Because every non-INVALID terminal mechanism class depends on at least one drift comparison that is currently transported/reconstructed through binary64, **no terminal mechanism class from run `35175533159` is eligible for final scientific promotion** under the benchmark's validated-decision standard.

After it becomes terminal, the run remains useful as an execution diagnostic and a reproducibility/control input, but its mechanism label is provisional/non-authoritative until reproduced by the exact-threshold implementation below.

Any `ITER504S_INVALID`, failed aggregate, failed Critic, or cross-environment decision disagreement remains INVALID and is not converted into a scientific FAIL.

This authority rule is frozen before the terminal outcome and applies identically to `ROOT_DERIVATIVE_RADIUS_LOCALIZED`, `CHANNEL_COMPETITION_NECESSARY`, `FIXED_CHANNEL_NONSTATIONARITY_REMAINS`, and `MIXED`; it cannot be selected according to whether the observed outcome is favorable.

## Frozen minimal exact-threshold repair

After the current run is terminal, one repaired execution may change only threshold-decision transport and verification:

1. Keep every scientifically active `du`, `slo`, and related Arb quantity as an Arb object until all threshold/floor booleans have been evaluated.
2. For every full-envelope row serialize explicit producer truth values computed only as Arb predicates:
   - `slope_floor_satisfied := slo >= arb('1.0')`;
   - `drift_within_tolerance := du <= arb('0.05')`;
   - `within_tolerance := slope_floor_satisfied AND drift_within_tolerance`.
3. Define `derivative_radius_sensitivity` only from the exact producer drift booleans: full-D `drift_within_tolerance=false` and center-D `drift_within_tolerance=true`. Never reconstruct it from float summaries.
4. During fixed-channel computation, define each channel's `drift_within_tolerance` only by the exact Arb predicate `du <= arb('0.05')` before serialization.
5. Define `all_candidate_fixed_channel_drifts_within_tolerance` as `complete AND candidates_nonempty AND all(exact_channel_flags)`; never reconstruct it from a serialized float maximum.
6. Serialize a deterministic `violating_channel_indices` list, or equivalently all per-candidate exact boolean flags, so downstream consumers can verify the logical reduction without comparing binary64 values to the threshold.
7. `S_lower`, `drift_upper`, `max_fixed_channel_drift_upper`, and similar binary64 fields remain display/diagnostic metadata only. They may not decide any scientific class or mechanism flag.
8. Assembler and independent Critic must reconstruct all mechanism flags and the final classifier exclusively from producer exact-Arb booleans plus structural completeness/provenance fields. They must reject any inconsistency among composite booleans and their constituent exact decision flags.
9. Cross-environment comparison must compare these exact decision booleans, candidate identities, possible-max identities, dominance booleans, exact rational case identities, and final classification. Floating serialization differences are diagnostic unless they alter a producer exact decision, in which case the gate is INVALID until explained.
10. Preserve `python-flint==0.9.0`, 384-bit precision, all 243 channels, exact LOW/MID/HIGH points, roots 13-15, rhos/R grid, source path, no-pruning rule, exact threshold `1/20`, floor `+1`, and the already frozen terminal classifier order.

## Execution firewall

No second Iter504S execution is authorized while run `35175533159` is nonterminal.

After terminalization, freeze exact-threshold evaluator/assembler/aggregate/Critic hashes and a single repaired workflow authority before launching exactly one repaired scientific execution. Do not use run `35175533159` numerical values to alter thresholds, points, channels, precision, cohort, source, or classifier order.

## Claim ceiling

This is an execution-rigor firewall only. It makes no Iter504S mechanism claim, does not change Iter504R, does not reclassify the 1888 parent states, does not close D7, and does not establish quantum gravity or new physics.
