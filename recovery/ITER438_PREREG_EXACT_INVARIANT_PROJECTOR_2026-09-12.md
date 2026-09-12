# Iter438 preregistration — exact invariant-projector/global-magnetic support

Date: 2026-09-12
Status: FROZEN BEFORE ITER438 COMPUTATION

## Dependency lock
Iter437 terminally classified `SOURCE_BACKED_SLOW_OBSTRUCTION_SURVIVES_LOCAL_MAGNETIC_CLOSURE` with exactly 12 surviving profiles. Iter438 is restricted to that frozen subset and may not add/remove profiles after seeing results:
`(10,3), (10,4), (11,3), (12,3), (12,4), (13,3), (14,3), (3,4), (5,4), (6,4), (9,3), (9,4)`.

## Frozen object
Keep exactly the Iter437 K5 source sectors, boosted clusters, crossing-edge extremal magnetic labels, and published Lorentzian boundary-spin pattern (four `j=5` edges incident to node 0; six `j=2` remaining edges; primitive homogeneous scale `lambda=1`). No spin, sign, or magnetic prescription may be retuned.

For every surviving profile, enumerate all globally consistent magnetic labels on the noncrossing/free K5 edges. For each complete global assignment, test whether the magnetic basis state has nonzero projection onto the 4-valent SU(2) invariant subspace at **all five** vertices.

## Exact projector-support rule
At each 4-valent vertex, sort incident legs deterministically. A magnetic basis state has projector support iff there exists an admissible intermediate spin `k` for which both exact Clebsch–Gordan couplings in a complete recoupling basis are nonzero. Nonzero CG support is evaluated with the exact rational Racah sum for the corresponding Wigner-3j symbol, so no floating threshold defines a zero.

## Independent control
Evaluate the same invariant-projector support in two complete recoupling schemes, `(01)|(23)` and `(02)|(13)`. The full set of globally supported magnetic assignments must agree exactly between the two schemes. Any disagreement, invalid source pattern, invalid fixed magnetic label, incorrect frozen-profile identity, or failure to reproduce the Iter435 slow tail condition is `CONTROL_INVALID` and blocks scientific interpretation.

## Frozen classification
Per lane:
- `SOURCE_BACKED_PROFILE_SURVIVES_EXACT_INVARIANT_PROJECTOR` iff at least one globally consistent noncrossing-edge magnetic assignment has nonzero invariant-projector support at all five vertices in both recoupling schemes.
- `SOURCE_BACKED_PROFILE_EXCLUDED_BY_EXACT_INVARIANT_PROJECTOR` iff none does, with valid controls.
- `CONTROL_INVALID` otherwise.

Aggregate:
- `SOURCE_BACKED_SLOW_OBSTRUCTION_SURVIVES_EXACT_INVARIANT_PROJECTOR` iff at least one of all 12 valid lanes survives.
- `SOURCE_BACKED_SLOW_OBSTRUCTION_KILLED_BY_EXACT_INVARIANT_PROJECTOR` iff all 12 valid lanes are excluded.
- any invalid lane => `CONTROL_INVALID`.

## Scope guard
This is a stronger exact discrete SU(2) support test than Iter437, including global edge-magnetic consistency and exact local invariant-projector support. Survival is still **not** a noncompact causal-vertex divergence theorem, not a full Haar/angular contraction, not finite-normalized vertex evidence, and not stack-cutoff or UV→Regge/GR transport. Exclusion would be scoped only to this published boundary-spin pattern and these frozen slow-extremal profiles. D2/D4/D7-S2/S3/S4 remain open unless their own contracts close them; terminal D7 and Candidate Gravity remain unauthorized.