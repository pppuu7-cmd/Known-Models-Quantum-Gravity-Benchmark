# Iter504S — execution-only fixed-channel drift semantics repair

Date: 2026-09-17
Status: PROSPECTIVELY FROZEN BEFORE ANY REPAIRED EXECUTION AND BEFORE CONSUMING ITER504S SUBSTANTIVE OUTPUT

Scientific preregistration remains exactly:

`f6367456aa715fe6282ab70c1b2005971a4568c7`

This record does not change any scientific threshold, cohort, point, source or terminal classification.

## Outcome-blind implementation mismatch

The frozen Iter504S preregistration defines the fixed-channel competition diagnostic in terms of **fixed-channel drift**:

- compute fixed-channel `drift_upper` for every eligible possible-max candidate;
- record the maximum fixed-channel drift;
- test whether all eligible possible-max fixed-channel drifts satisfy `drift_upper <= 0.05`.

The first implementation instead reused a composite per-channel boolean that required both

`S_lower >= +1.0`

and

`drift_upper <= 0.05`.

That is stricter than the preregistered competition diagnostic and could misattribute a hypothetical fixed-channel slope-floor failure as fixed-channel drift nonstationarity.

This mismatch was found by static audit while first run `35173442220` was still in progress and before any substantive Iter504S artifact was consumed.

## Frozen minimal repair

For the fixed-channel competition diagnostic only:

1. define `all_candidate_fixed_channel_drifts_within_tolerance` from the actual eligible candidate drifts alone;
2. equivalently, when the competition test is complete and at least one candidate exists, this boolean is true iff `max_fixed_channel_drift_upper <= 0.05`;
3. retain `S_lower` as a reported diagnostic but do not include it in this fixed-channel drift-only competition predicate;
4. recompute `competition_necessary_full_D`, `competition_necessary_center_D`, and `fixed_channel_nonstationarity_center_D` from this drift-only predicate;
5. update the assembler and independent Critic to reconstruct the predicate from `max_fixed_channel_drift_upper`, rather than trusting a producer-provided convenience boolean.

The full-envelope `full_D_within_tolerance` scientific predicate remains unchanged and still requires both `S_lower >= +1.0` and `drift_upper <= 0.05`, exactly as preregistered.

## Execution firewall

Do not dispatch another Iter504S run while `35173442220` is queued/running. If the first run becomes terminal, treat any implementation failure separately from science and apply this repair together with the already-frozen dual-derivative extraction repair before one repaired execution.

No failed/partial first-run values may be used as scientific evidence.
