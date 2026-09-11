# Recovery delta — Iter277

Date: 2026-09-11

## What changed

Iter277 tested the newly promoted RQCP Tier-1 family on independent resource axes rather than repeating its already saturated spatial-refinement calculation.

Two parallel compute waves were completed:

- `rqcp-scoped-robustness-probes`, run `34551324978`: 19 independent probes plus aggregate, all success;
- `rqcp-cutoff-extension`, run `34551533448`: cutoff 18/20/24/28, 4/4 success.

The methodology CI attached to the cutoff-extension head, run `34551533303`, passed preflight, all four methodology shards and the aggregate/bundle job.

## Scientific result

The independent implementation reproduces the published cutoff-8 fixed-band RQCP quantities to floating numerical precision. However, the local oscillator Hilbert/domain cutoff is an independent material axis:

- cutoff 8 -> 28: `G` shifts by ~7.3245%;
- gap shifts by ~3.0706%;
- `G gap^2` shifts by ~1.3599%.

The sequence then rapidly stabilizes:

- cutoff 24 -> 28: `G` changes by ~1.80e-8 relative;
- gap by ~1.35e-9;
- `G gap^2` by ~1.53e-8.

The finite quartic grid is modestly sensitive and keeps positive `G`; the mixed geometry-matter response is highly stable to the tested derivative-step grid.

This does not refute the upstream fixed-band result because its finite cutoff is a declared physical-domain input. It does show that spatial-regulator closure is not by itself complete resource closure.

## Methodological delta

`MULTI_AXIS_RESOURCE_CLOSURE`

If an independent regulator/truncation/basis/domain/finite-volume/resolution/approximation axis materially moves a normalized target observable, that axis must be closed separately by controlled removal/convergence or justified by an autonomous physical-selection principle with propagated observable uncertainty.

One-axis convergence cannot silently close another axis.

## Current global lock

- RQIR Core v1.0: FROZEN.
- Tier-1 census: 15.
- Strict terminal: 1/15.
- Strict nonterminal: 14/15.
- Candidate-family terminal: 0/14.
- Tier-2 unresolved: 0.
- D2: NOT_CLOSED_COVERAGE_AND_OBJECTS.
- D3: PARTIAL.
- D4: PARTIAL_GLOBAL_NOT_CLOSED.
- D7: NOT_CLOSED / NOT_YET_AUTHORIZED.
- Candidate Gravity: inactive, canonical R3=24%.

## Exact next gate

`D7_S2_EXTERNAL_AUTHORITY_DRIVEN_TERMINALIZATION_WITH_MULTI_AXIS_RESOURCE_CLOSURE`

Priority remains:

1. immediately ingest a stable public Asymptotic-Safety same-realization `s+t+u+A4` package if it appears;
2. reopen RQCP only for a genuinely new all-band/background-independent autonomous-gravity bridge plus Hilbert-cutoff removal or autonomous cutoff/domain selection with propagated uncertainty;
3. otherwise reopen another Tier-1 family only on materially new authority capable of changing its strict family classification.

Do not spend compute repeating already saturated fixed-band controls merely to keep runners busy.
