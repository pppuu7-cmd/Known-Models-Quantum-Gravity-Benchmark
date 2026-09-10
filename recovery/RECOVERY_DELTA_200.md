# KMQGB recovery delta — Iteration 200

**Date:** 2026-09-10  
**Base canonical main:** `86cfc553f03c50ea229a382f621ce45353b13d1a` (Iter199)  
**RQIR Core:** v1.0 FROZEN.

## New scoped result

The old CDT blocker bundled two distinct deficits: continuum trajectory and physical observable. Iter200 closes only the latter in a fixed four-dimensional CDT realization.

Maas, Plätzer and Pressler, *Hints for a Geon from Causal Dynamic Triangulations*, Phys. Lett. B 879 (2026) 140600 / arXiv:2504.11047v4, measure normalized curvature-curvature correlators at `Delta=0.6`, `kappa_0=2.2` and extract a common massive-like screening scale using multiple curvature operators. The final version contains volume and smearing systematics and the underlying stochastic samples are public on Zenodo record 20589545.

Frozen scoped disposition:

`PASS_RQIR_GATE__CDT_4D_NORMALIZED_CURVATURE_CORRELATOR_PHYSICAL_OBSERVABLE_WITH_OPERATOR_VOLUME_SMEARING_SYSTEMATICS_AND_OPEN_DATA`.

The “geon” interpretation remains tentative. KMQGB freezes the existence and controlled measurement of the 4D gravity-sector observable, not a discovery claim.

## Why the parent remains nonterminal

The observable is measured at one bare parameter point. It is not transported along a line of constant physics to a demonstrated critical point; its quoted physical mass conversion uses an external lattice-spacing estimate and is explicitly subject to discretization uncertainty. The CDT↔FRG scaling programme develops a UV/IR matching strategy but states that current numerical precision is insufficient to decide whether a CDT UV fixed point exists. No same-domain GR/EFT/alternative-QG correlator quotient is frozen, and EDT is not dispositioned by this CDT child.

## Refined family blocker

`CDT_4D_LINE_OF_CONSTANT_PHYSICS_TO_UV_CONTINUUM_TRAJECTORY_PLUS_LATTICE_SPACING_SCALING_AND_GEON_CORRELATOR_COMPARATOR_ERROR_CERTIFICATE__EDT_DISPOSITION`

## Matrix effect

- scoped child rows with defined residual/control: **9 -> 10**;
- Tier-1 required: **14**;
- terminal family rows: **1/14**;
- nonterminal family rows: **13/14**;
- `CDT_EDT`: `PARTIAL_SUBFAMILY_ONLY`;
- family residual: undefined.

## Global status

No terminal promotion:

- D2: NOT_CLOSED;
- D4: NOT_CLOSED;
- D7: NOT_CLOSED;
- Paper IV: `NOT_YET_AUTHORIZED`;
- Candidate Gravity R3: 24%, inactive;
- Closure Wave 02: 0/3 terminal;
- heavy compute: IDLE.

## Authorities added

- `paper_iv/O_CDT_4D_GEON_GRAVITY_OBSERVABLE_SCOPE_AUDIT_2026-09-10.md`
- `post_freeze_paper_iv_wave_02/PF2_02B_CDT_4D_GEON_OBSERVABLE/result.json`
- `paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_DELTA_200.json`
- `paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_200.json`

## Next operation

1. Synchronize `recovery/state.json` and `CURRENT_BENCHMARK_FRONT.md`.
2. CI-validate Iter200 and merge only from the exact validated head.
3. Search for a multi-bare-coupling 4D CDT line-of-constant-physics / critical-scaling data capsule capable of transporting the correlator toward `a -> 0`.
4. If no such object exists, park CDT as literature/data-limited and move to the next family rather than re-fitting the same fixed-point dataset.
