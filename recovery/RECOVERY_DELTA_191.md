# KMQGB Recovery Delta — Iteration 191

Date: 2026-09-10

## Starting point

Iter190 froze the material projectable/non-projectable Hořava family fork and identified the projectable extra scalar plus non-projectable/BPS scalar-tensor sector as distinct RQIR targets. Family status remained `PARTIAL_SUBFAMILY_ONLY`.

## New primary-source result

Two Barvinsky-Kurov-Sibiryakov authorities materially reduce the projectable branch blocker:

- arXiv:2110.14688 derives the complete one-loop beta functions for the marginal essential couplings of 3+1 projectable Hořava gravity and identifies candidate asymptotically free fixed points.
- arXiv:2411.13574 numerically follows RG trajectories from the asymptotically free fixed points and finds a trajectory family spanning the unitarity-compatible lambda range, including `0 < lambda - 1 << 1`.

New scoped classification:

`PASS_RQIR_GATE__HORAVA_PROJECTABLE_3P1_ASYMPTOTICALLY_FREE_MARGINAL_RG_TRAJECTORY_AUTHORITY`.

Authority:
`paper_iv/O_HORAVA_PROJECTABLE_3P1_RG_TRAJECTORY_SCOPE_AUDIT_2026-09-10.md`.

## Closed sub-obligation

It is no longer correct to treat absence of a 3+1 projectable UV RG trajectory as the blocker. The asymptotically free marginal trajectory has direct primary-source authority.

## Remaining blocker

The RQIR same-realization certificate still lacks the controlled crossover from that marginal z=3 trajectory into the relevant lower-derivative IR sector and then into one normalized extra-scalar observable with propagated theoretical error/remainder and a same-domain GR/EFT comparator.

New narrow gate:

`HORAVA_PROJECTABLE_AF_RG_TO_IR_RELEVANT_COUPLING_CROSSOVER_PLUS_EXTRA_SCALAR_OBSERVABLE_MATCHING_CERTIFICATE`.

## Global status

No family-level terminal status changed:
- Tier-1 terminal 1/14.
- Tier-1 nonterminal 13/14.
- Tier-2 unresolved 0.
- D2 NOT_CLOSED.
- D4 NOT_CLOSED.
- D7 NOT_CLOSED.
- global decision `NOT_YET_AUTHORIZED`.
- Candidate Gravity R3=24%, inactive.

Heavy compute remains IDLE because the missing object is RG-to-IR matching/provenance, not an unfrozen numerical parameter scan.
