# Iter502 — prospectively frozen dyadic dependency-repair gate

**Frozen before implementation / production.** This is a numerical-enclosure repair prerequisite for D7-S2, not a new scientific classifier and not a D7 closure claim.

## Authority and causal trigger
Iter501 (`run 34820198677`) terminated as `ITER501_NUMERICAL_METHOD_BLOCKER`: all 12 frozen lanes were present, while source point-containment failed because the validated direct 243-channel max-envelope enclosure lost dependency information over the original amplitude boxes. This gate must distinguish a finite-width interval dependency artifact from a deeper enclosure-method blocker. No Iter501 scientific DECAY/NONDECAY conclusion is imported.

## Frozen scope
- Same source-faithful C-panel geometry, q=1 shrinking layer, six active angular coordinates `[0,1,3,5,6,11]`, eight directions, both signs, three causal classes and four rho witnesses as Iter501.
- Same `R={6,8,10,12}`, exact-rational j=1 intertwiners, all **243 intertwiner channels**, compact-sandwich/factorized KAK from Iter500, and source Toller branches.
- The original 16 closed amplitude boxes covering `[0.00125,0.00250]` are each partitioned into exactly **8 equal closed dyadic subboxes**. Their union is exactly the original frozen domain; no domain point is removed and no threshold is changed.
- The 9 Iter501 source-regression point amplitudes remain unchanged. Each must be contained by at least one validated dyadic subbox that contains that amplitude.
- `python-flint==0.9.0`, 384-bit Arb/Acb arithmetic.
- Matrix is `3 causal × 4 direction-block = 12` independent jobs, `fail-fast:false`, `max-parallel:12`.

## Frozen scientific thresholds (unchanged from Iter501)
- drift tolerance `0.05`;
- robust NONDECAY floor `+1.0`;
- NONDECAY floor `0.0`;
- uniform DECAY witness ceiling `-0.10`.

## Frozen interpretation
1. If any subbox has arithmetic/KAK/source/finite-envelope failure, or any unchanged source-regression point is not contained by the union of eligible validated subboxes, classify the lane `ITER502_NUMERICAL_METHOD_BLOCKER`.
2. Only after the containment prerequisite passes may interval classes be interpreted scientifically.
3. If every validated state is robust NONDECAY: `ITER502_DYADIC_DIRECT_MAX_ENVELOPE_INTERVAL_ROBUST_QUALIFIED_SCOPED`.
4. If every validated state is NONDECAY or robust NONDECAY: `ITER502_DYADIC_DIRECT_MAX_ENVELOPE_INTERVAL_NONDECAY_QUALIFIED_SCOPED`.
5. If any validated state is a uniform-decay witness: `SCIENTIFIC_FAIL_ITER502_UNIFORM_NONDECAY_INTERVAL`.
6. Otherwise: `ITER502_VALIDATED_INTERVAL_INCONCLUSIVE_SCOPED`.

The fixed 8-way cover is a prospectively frozen numerical repair; it must not be refined post hoc inside Iter502. A blocker at this fixed cover requires a different prospectively frozen dependency-preserving method (e.g. centered/mean-value or direct correlated factor enclosure), not threshold relaxation.

## Scope guards
D7-S2 remains `NOT_CLOSED`; D7-S3 remains `NOT_CLOSED`; D7-S4 remains `PARTIAL_GLOBAL_NOT_CLOSED`. Terminal D7 classifier and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden while required gates are open. Candidate Gravity remains inactive. No positive-Haar-measure, absolute-Haar, spectral-integral, PV/conditional, distributional-boundary-value, or K5-collision theorem follows from this gate alone.
