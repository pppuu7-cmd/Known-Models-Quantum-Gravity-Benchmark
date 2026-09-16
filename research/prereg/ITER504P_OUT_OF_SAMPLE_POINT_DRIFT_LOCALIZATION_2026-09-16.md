# ITER504P_OUT_OF_SAMPLE_POINT_DRIFT_LOCALIZATION_GATE

Date: 2026-09-16  
Status: PROSPECTIVELY FROZEN FOR THE DECISIVE COHORT

## Motivation

Terminal Iter504 classified the full validated centered interval campaign as

`ITER504_VALIDATED_CENTERED_INTERVAL_INCONCLUSIVE_SCOPED`.

All 3072 late-slope lower bounds exceed the frozen robust NONDECAY floor `+1.0`, no uniform-decay witness exists, and the 1888 inconclusive states are localized by the frozen classifier to the drift criterion `<=0.05`.

The cheapest high-information question is whether the already-frozen independent source-point path itself exhibits drift larger than `0.05`, or whether the unresolved drift is specific to the continuous interval enclosure.

## Prospective / retrospective boundary

Before this preregistration, one terminal point artifact was inspected for independent Iter504 verification:

`0to5-b0` (`iter504-point-0to5-b0`).

Its values are therefore **not outcome-blind** and MUST NOT participate in the decisive classification. It is retained only as a disclosed non-decisive control.

The decisive cohort is frozen now as the other eleven Iter504 point lanes, none of whose substantive point values have been consumed in this research cycle:

- `0to5-b1`, `0to5-b2`, `0to5-b3`;
- `1to4-b0`, `1to4-b1`, `1to4-b2`, `1to4-b3`;
- `2to3-b0`, `2to3-b1`, `2to3-b2`, `2to3-b3`.

## Frozen data / formula

Use only the terminal point artifacts from authoritative Iter504 run `34907349374` at workflow head `56362459a826e3e376c529446678f2fbcaa269ae`.

For every decisive lane, all four signed paths, all nine frozen point amplitudes and all four frozen rhos must be present. Expected decisive records:

`11 lanes x 4 paths x 9 amplitudes x 4 rhos = 1584`.

For each record define the point drift exactly as

`D_point = abs(actual_slope - early_actual_slope)`.

The comparison threshold is inherited without change from Iter504:

`D_point <= 0.05`.

No new threshold may be selected after reading the remaining eleven artifacts.

## Terminal classifications

`ITER504P_POINT_GRID_DRIFT_WITHIN_FROZEN_TOLERANCE_SCOPED`
iff all 1584 decisive records are structurally valid and satisfy `D_point <= 0.05`.

`ITER504P_POINT_GRID_DRIFT_VIOLATION_SCOPED`
iff the decisive cohort is structurally valid and at least one record has `D_point > 0.05`.

`ITER504P_POINT_GRID_DRIFT_INVALID`
iff any decisive lane/path/amplitude/rho is missing/duplicated/malformed, source identity is not Iter504, or the formula/threshold is changed post hoc.

## Controls

- disclosed inspected lane `0to5-b0` is reported separately and cannot change classification;
- exact expected lane IDs and record count are frozen;
- maximum drift record and per-causal/block maxima are retained;
- the sign of late/early slopes is reported but does not alter the drift criterion;
- no continuous-interval conclusion is inferred from the finite point grid.

## Interpretation ceiling

A WITHIN-TOLERANCE result would localize the Iter504 inconclusiveness to rigorous continuous enclosure width/dependency control **at the sampled-point level only**; it would not prove continuous NONDECAY. A VIOLATION result would show that the 0.05 stationarity criterion is already violated at a frozen source point and therefore should not be attacked merely as an interval-overestimation problem.

Neither outcome closes D7-S2, establishes a positive-measure Haar theorem, resolves the blocked K5 contact/physical-quotient branches, or authorizes any selector/model/family conclusion.
