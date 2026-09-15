# KMQGB recovery/front ledger delta — scalar K5 laminar-forest order repair

Date: 2026-09-15
Status: TERMINAL DELTA

## STATE_READ

The active KMQGB front was restored from current `main`, recent Research/Critic commits, frozen preregistrations, and authoritative Actions rather than stale historical snapshots.

## TERMINAL_AUTHORITY

`SOURCE_J1_K5_SCALAR_LAMINAR_FOREST_ORDER_REPAIR = SCALAR_K5_LAMINAR_FOREST_ORDER_REPAIR_CONFIRMED_SCOPED`

Authority:

- prereg `21af89b35639d0e4a854a53cf6cd3219437bd4b2`;
- implementation `6c65db48570a638976d822cc1c68ae6d21101079`;
- workflow head `eea26abe7b70c038e686078016acc17943f28c13`;
- run `34990564375`;
- terminal result commit `16b6340a2bd78e350258636b226ac69adb8a40d2`.

## NEW_EXACT_FACTS

Scalar Gaussian same-realization subtraction orders:

`{2:2, 3:7, 4:15, 5:26}`.

Proper-only K5 laminar topology, with full collision kept distinct:

- 25 proper connected subsets;
- 236 forests including empty;
- cardinality histogram `{0:1,1:25,2:105,3:105}`;
- 12 S5 orbits;
- proper forest record digest `sha256:5d1e124067d8a4dec8e0dafeb84c3fa2cdcab51e34a4be7b6c0b85fe623b5273`.

Historical all-forest topology remains 472 forests / 24 S5 orbits. Historical order table `0,3,9,18` is explicitly retained only as the separately frozen three-normal-dimensional realization and is forbidden as scalar Gaussian authority.

## SUPERSEDED_ACTIVE_PREREG

Historical prereg `a63df1f3c66dbadaec7bbaab2c916cffefb56813` (`SOURCE_J1_K5_FOREST_SUBTRACTION_P1`) must not be executed as written. It is superseded for future execution by:

1. critical qualification `0d683f0be541e4fed487a922a8569d3f730808bd`;
2. terminal scalar order/topology repair `16b6340a2bd78e350258636b226ac69adb8a40d2`.

Historical files/results are not rewritten.

## ACTIVE_FRONT

Next admissible front is an exact **scalar K5 forest-operator definition/audit gate**. Numerical P1 forest subtraction remains unauthorized until the operator is prospectively frozen and terminally validated.

The operator gate must preserve the scalar realization, exact proper-only forest family, S5 covariance modulo gauge, and full-collision/root separation.

## GLOBAL_LOCKS

- `RQIR Core v1.0 = FROZEN`
- `D7-S2 = NOT_CLOSED`
- `D7-S3 = NOT_CLOSED`
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`
- terminal D7 selectors forbidden
- Candidate Gravity inactive
- KMQGB downstream of pinned DSIR authority
- BLOCKED != FAIL; diagnostic/enabling certificate != physical closure
