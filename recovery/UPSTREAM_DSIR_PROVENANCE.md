# Upstream DSIR provenance lock

Updated: 2026-09-14

## Repository relationship
`pppuu7-cmd/Dark-Sector-Influence-Reconstruction` (DSIR) is the upstream/foundation repository for the research program whose known-model proving/benchmark layer is maintained in `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark` (KMQGB).

This relationship is provenance/governance. It does **not** make a moving DSIR `main` an implicit replacement for already-frozen KMQGB gate inputs, and it does not weaken the local KMQGB/RQIR frozen contracts.

## Audit-time upstream head
At this provenance audit the observed DSIR `main` head is:

`05c87c85093142cfca4d0a432269d5f2440a6e88`

Commit message: `dsir: launch frozen V0.25 interpolation remedy benchmark`.

This SHA is an observation anchor, not a declaration that every historical KMQGB object was derived from that exact DSIR state.

## Required import rule
For every future KMQGB gate that imports, reuses, translates, or depends on a DSIR scientific object, assumption, normalization, observable, dataset, reconstruction result, or contract, the prospective KMQGB preregistration must identify:

1. DSIR repository identity;
2. exact DSIR commit SHA (or immutable tag) used for that imported object;
3. exact source path(s) / object identifier(s);
4. any transformation/adaptation into the KMQGB representation;
5. normalization, sign, branch, units and domain conventions relevant to the comparator;
6. whether the imported statement is an upstream established/frozen result, an executable reproduction, or only a hypothesis/input;
7. compatibility check against the frozen KMQGB/RQIR comparator contract.

No future DSIR change silently changes a prospectively frozen KMQGB gate. A later DSIR result may authorize a **new** compatibility/update gate, but it may not rewrite a historical KMQGB result post hoc.

## Authority separation
- DSIR: upstream reconstruction/foundation provenance.
- KMQGB: downstream known-model benchmark/proving execution and terminal selector discipline.
- RQIR Core v1.0 inside KMQGB remains frozen unless its own governance explicitly authorizes a new version.
- KMQGB gate preregistration remains the local execution/classification authority once frozen.

## Claim guard
This provenance lock alone establishes no scientific pass/fail result, no D7 closure, no selector label, and no Candidate Gravity activation. It exists to prevent source drift, repository confusion and silent upstream/downstream substitution.
