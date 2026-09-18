# Iter504V source-lock frozen-core identity repair — preregistration

Date: 2026-09-18
Status: FROZEN_BEFORE_IMPLEMENTATION_AND_RELAUNCH

## Gate

`ITER504V_SOURCE_LOCK_FROZEN_CORE_IDENTITY_REPAIR`

The first Iter504V source launch, run `35364872746` at head `1509c22211a41a66542be21b1a08d763fcf986b0`, failed in `source-lock` before any case job executed. All case and assembly jobs were skipped. No scientific payload was produced or consumed.

## Defect

The source-lock used runtime lookup

`git rev-parse 10ae6bcc8447d14cecc6e550065504b23f792953:<path>`

to compare inherited core source identity. Repository/API inspection shows the current launch-head blobs, Iter504U source-head blobs, and the frozen Iter504U pin blobs are exactly identical for all five inherited files. Therefore the failure is an execution/provenance lookup defect, not source-realization drift.

## Frozen exact source blobs

- `code/iter499_arb_core.py` = `1736f727ee956c181d8ff513eb0c243085131668`
- `code/iter500_compact_sandwich_kak.py` = `081515547f6c4793d148fcc3227aa6efb9a73b8f`
- `code/iter501_direct_max_envelope_interval.py` = `dd912ff1753cf270c120e01719be92e0d2df7a9f`
- `code/iter503_ad_core.py` = `68cad1cb38a8c382c77894ffc7bbea0b9ab7c1bd`
- `code/iter504_centered_shard.py` = `fee4f4f44e71aaac8ad9d9c47d27a63301f9c43b`

## Repair

Replace only the historical-commit runtime lookup with direct `git hash-object <path> == frozen_blob_sha` checks. No evaluator, assembler, aggregate, cohort, threshold, floor, precision, channel set, R/rho grid, partition, MAX_DEPTH, classifier, or claim ceiling may change.

Relaunch exactly one Iter504V source production under a new execution authority. The failed pre-science run is not a scientific Iter504V result.

Phase B remains unauthorized.
