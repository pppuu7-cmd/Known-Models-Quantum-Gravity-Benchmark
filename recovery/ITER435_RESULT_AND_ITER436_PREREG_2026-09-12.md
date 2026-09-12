# Iter435 result + Iter436 preregistration

Date: 2026-09-12

## Iter435 terminal scientific result

Frozen gate: `recovery/ITER434_RESULT_AND_ITER435_PREREG_2026-09-12.md`.

Authoritative run: `34704066049` on head `291e11f946f1903f4e5a33e83c09662dc88048b1`.
Aggregate job: `103581058345`.
Aggregate artifact: `10301047891` (`lqg-iter435-summary`).
Artifact digest: `sha256:78ff17a5a2ece1e1777a1eb314d7232a377599660bff1247688f8d444b5bf852`.

All 16/16 source-induced K5 sign sectors were structurally valid and unique; all satisfy the positive triangle-product source-support control. The frozen fast-control profiles pass. The source-supported slow-extremal family retains 32 failing profiles, all at cluster sizes `s=3` or `s=4`; observed slow-family lambda range is `[-2,+4]`.

Scientific classification: `SOURCE_SUPPORT_DOES_NOT_REMOVE_MULTI_GROUP_ENVELOPE_OBSTRUCTION`.

Scope lock: this is a source-support-level absolute asymptotic-envelope negative result only. It is not a physical causal-vertex divergence theorem. In particular it does not establish that the simultaneous slow-extremal magnetic labels have nonzero support under SU(2) boundary intertwiners, nor does it test angular cancellation, the finite-beta distributional amplitude, normalized vertex finiteness, stack cutoff removal, or UV-to-Regge/GR transport.

Global status remains unchanged: D2=`NOT_CLOSED_COVERAGE_AND_OBJECTS`; D4=`PARTIAL_GLOBAL_NOT_CLOSED`; D7-S2=`NOT_CLOSED`; D7-S3=`NOT_CLOSED`; D7-S4=`PARTIAL_GLOBAL_NOT_CLOSED`; D7=`NOT_CLOSED / NOT_YET_AUTHORIZED`. Terminal D7 and `EXISTING_SUFFICIENT` / `ADAPT_EXISTING` / `HYBRID_REQUIRED` / `NEW_REQUIRED` remain forbidden. Candidate Gravity remains inactive.

## Iter436 prospectively frozen gate — magnetic-closure survival audit

### Scientific question
Do the Iter435 source-supported slow-extremal obstruction profiles at `s=3,4` survive the most basic local SU(2)-invariance magnetic closure requirement, or are the extremal assignments already excluded before a full intertwiner/angular contraction?

### Frozen object
Use exactly the 16 source sectors `kappa_ab=sigma_a sigma_b`, with `sigma_0=+1`, and exactly the Iter435 crossing-edge spin/magnetic assignment for the `slow-extremal` family at `s in {3,4}`:
- crossing edges are ordered lexicographically;
- crossing spins cycle through `{1/2,1,3/2,2}` in that order;
- `m=-j` on a `+` branch and `m=+j` on a `-` branch.

For every K5 vertex treat all incident legs as outgoing after the standard dual-leg sign conversion. For any incident edge whose Iter435 magnetic label is fixed, its outgoing magnetic number at the lower-numbered endpoint is `m` and at the upper-numbered endpoint is `-m`. Unfixed incident legs are not assigned a preferred value. Instead, test whether there exists at least one allowed magnetic value on each unfixed leg, in half-integer steps within `[-j,j]`, that makes the exact local magnetic closure condition `sum m_out = 0` hold.

The spins of unfixed legs are prospectively fixed by a global lexicographic K5 palette: edge number `r` in the full lexicographic ten-edge list gets `j in {1/2,1,3/2,2}[r mod 4]`. Crossing-edge spins remain the exact Iter435 crossing-order values and override the global palette where necessary. This completion rule is frozen before Iter436 results and is a diagnostic completion only, not a claimed physical boundary state.

### Frozen controls
For every lane:
- reproduce the exact Iter435 source sector and slow-extremal crossing assignment;
- reproduce `lambda>=0` for the lane, otherwise classify `CONTROL_INVALID`;
- every fixed crossing magnetic value must satisfy `|m|<=j` and correct half-integer parity;
- every K5 vertex must have four incident legs;
- brute-force existential closure result must agree with an independent interval/parity closure check.

### Frozen classifier
Each lane is one `(sector_index,s)` pair, 16 x 2 = 32 lanes.
- `MAGNETIC_CLOSURE_EXCLUDES_SLOW_EXTREMAL_PROFILE` if at least one vertex admits no completion to local `sum m_out=0`.
- `MAGNETIC_CLOSURE_ALLOWS_SLOW_EXTREMAL_PROFILE` if every vertex admits at least one completion.
- `CONTROL_INVALID` if any frozen control fails.

Aggregate interpretation:
- if all 32 lanes are excluded, classify `SOURCE_SUPPORTED_SLOW_OBSTRUCTION_KILLED_BY_LOCAL_MAGNETIC_CLOSURE_UNDER_FROZEN_COMPLETION`;
- if at least one lane survives, classify `SOURCE_SUPPORTED_SLOW_OBSTRUCTION_SURVIVES_LOCAL_MAGNETIC_CLOSURE_IN_AT_LEAST_ONE_FROZEN_PROFILE`;
- any control failure gives `CONTROL_INVALID`.

### Claim lock
Iter436 is only a necessary local magnetic-closure diagnostic. A surviving lane is not proof of nonzero invariant-intertwiner projection; an excluded lane is not a theorem for all boundary spin completions. No D7-S2 promotion or physical divergence claim follows. If any profile survives, the next permitted hard gate is exact 4-valent SU(2) invariant-projector support on surviving profiles, followed only then by angular/boundary contraction. If all profiles are excluded under this frozen completion, repeat only with an independently preregistered physically sourced boundary-spin completion; do not tune completion after seeing outputs.