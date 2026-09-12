# KMQGB recovery/front delta — Iter444 terminal + Iter447 launch

Date: 2026-09-13

## Source-of-truth ordering
This delta supplements the stale monolithic `recovery/CURRENT_BENCHMARK_FRONT.md`. Newest validated Actions artifacts + newer recovery deltas/commits remain authoritative.

## Iter444 — terminal consumed
- Run: `34718089193`
- Head: `62aa79675df92e5554bd7970e4227997cf4b111a`
- Summary artifact ID: `10305473125`
- Artifact digest: `sha256:7927b7314031c3a7378de943bf52d4e861be498c4447acf2b4116f207a10c2b0`
- Raw summary SHA256: `40e89b351754aa03d1ed109ef155a3e75ac20edc2b987e82b8de50e558eeee41`
- 16/16 lanes passed; controls valid.
- Frozen classification: `SOURCE_TWO_GROUP_SEPARATED_RADIAL_ENVELOPE_INTEGRABLE_ON_FROZEN_GRID`.
- Worst common-shift log slope: `-2.000000034594013`.
- Max external scaled-envelope variation: `6.04858197541036e-06`.

Scientific interpretation: scoped support for separated two-group radial integrability on the frozen grid. It does not establish full causal-vertex finiteness and does not supersede Iter445/446. Together with terminal Iter446, the remaining fixed-label D7-S2 blocker is localized to local pair/multi-pair collision strata and their invariant-contraction/distributional treatment.

## Current formal locks
- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`
- D4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7-S2: `STRENGTHENED_BUT_NOT_CLOSED`
- D7-S3: `NOT_CLOSED`
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7: `NOT_CLOSED / NOT_YET_AUTHORIZED`
- Terminal D7 classifier remains forbidden.
- `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` remain unauthorized.
- Candidate Gravity remains inactive.

## Iter447 — preregistered next D7-S2 gate
Branch: `research/iter447-collision-strata-local-power`

Preregistration commit: `86731f0b583d8871b17b0a1f46c0465bbaf29342` (`status/ITERATION_447.md`), created before implementation/production.
Implementation commit: `f31887ccd0d0933cac8ca87b38a40da58f1452a0`.
Workflow creation commit: `8ce4751041c2058faac2e9da7da356317682a03b`.
Authoritative production trigger/head: `316e3e392e66ff24c1242f6173e8f6893cc3710e`.
Authoritative run: `34721476885`.

Frozen matrix: gamma `{7,8}` x j `{2,5}`, all integer m, both Toller branches, beta collision sequence `2^-n` for n=4..10, 100 dps. Frozen isolated-pair local-power support threshold: worst `p_local < 2.9` plus witness stability spread `<=0.20`. Green CI alone is not a scientific PASS.

Scope lock: this is only an isolated pair-collision local-power diagnostic. Even a PASS leaves simultaneous shared-variable two-/three-pair collision geometry/invariant contraction open and gives no full vertex finiteness theorem.

## Next permitted gate
Consume Iter447 terminal artifact against the frozen preregistration. If PASS, preregister explicit simultaneous two-/three-pair collision shared-variable/invariant-contraction audit. If obstruction, preregister branch-sum/invariant-contraction cancellation diagnostics without retuning Iter447 thresholds/grid.
