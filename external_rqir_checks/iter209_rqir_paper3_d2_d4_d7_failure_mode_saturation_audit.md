# KMQGB Iter209 — RQIR Paper III D2/D4/D7 failure-mode saturation audit

**Date:** 2026-09-10  
**Purpose:** decide whether the KMQGB benchmark has exposed a new *general resource-closure failure mode* that requires reopening RQIR Paper III.  
**Scope:** Paper-III impact only. This document does **not** promote Paper-IV D2/D4/D7 to terminal closure.

## Authority snapshot

The audit uses the current KMQGB state through Iter208 plus the strengthened RQIR Paper-III scientific certificate frozen on 2026-09-09.

KMQGB has already:

- made D2/D4/D7 logic explicit (Iter182);
- completed the first-pass census across all 14 Tier-1 framework families and executed a D7 evaluator (Iter186);
- resolved Tier-2 classification to zero unresolved rows;
- continued family/subfamily audits through Iter208.

The scientific Paper-IV state remains fail-closed:

- Tier-1 families: 14;
- Tier-1 terminal: 1;
- Tier-1 nonterminal: 13;
- D2: `NOT_CLOSED_COVERAGE_AND_OBJECTS`;
- D4: `PARTIAL_ACTIVE_SET_MATRIX__GLOBAL_COVERAGE_NOT_CLOSED`;
- D7: `NOT_CLOSED`;
- global Paper-IV decision: `NOT_YET_AUTHORIZED`.

Those states answer the Paper-IV question. They are not, by themselves, a reason to reopen Paper III.

## Paper-III reopening criterion

Paper III is reopened only if KMQGB produces a failure mode satisfying **all** of the following:

1. it is methodological rather than specific to one quantum-gravity theory;
2. it transfers to experiment/resource closure;
3. it is not already represented by Paper-III controls, negative controls, provenance rules, or claim boundaries;
4. it can change a positive Paper-III conclusion or the conditions under which that conclusion is stated.

Otherwise KMQGB continues as Paper-IV work while Paper III remains frozen.

## Failure-mode crosswalk

### FM-A — structural non-identifiability / unconstrained scale

KMQGB repeatedly requires an observable/residual to be identifiable after nuisance/comparator directions are removed. Paper III already contains the corresponding resource-domain failure class: static science plus free offset, science without an independently calibrated absolute reference, unconstrained reference amplitude, and recoil-only replacement all fail absolute `theta` identifiability.

**Paper-III status:** already covered. `NO_REOPEN`.

### FM-B — incompatible source or realization splicing

KMQGB D6 forbids constructing a complete object by joining pieces from different realizations without an explicit compatibility map. Iter208 TGFT is a direct example: relational Lorentzian Barrett-Crane observables and explicit FRG controls live in different audited realizations, so the chain is parked as `BLOCKED_MISSING_REQUIRED_OBJECT` rather than spliced.

Paper III already freezes an apparatus/provenance analogue: baseline apparatus/noise/detector authority, sensitivity-function authority and later chirp-metrology capability have declared roles; incompatible raw experiments are not statistically concatenated; prospective metrology is not relabelled as historical apparatus data.

**Paper-III status:** already covered. `NO_REOPEN`.

### FM-C — incomplete end-to-end physical chain

Across KMQGB, many family rows remain nonterminal because a required link is absent: UV/continuum trajectory, observable map, normalization, comparator, or error ledger. `BLOCKED` is never zero-filled or counted as exclusion.

Paper III already has an end-to-end same-apparatus resource-closure audit joining physical scale, colored covariance, detector likelihood, nuisance profiling, absolute reference metrology and resource/exposure accounting. Missing historical raw campaign data are explicitly carried as a limitation rather than silently completed.

**Paper-III status:** already covered. `NO_REOPEN`.

### FM-D — comparator/normalization absorption

KMQGB D4 requires a comparator-subtracted residual; several scoped results disappear after the proper comparator quotient or remain undefined because normalization/common-domain comparison is missing.

Paper III already treats the experiment-domain analogue by requiring an independently calibrated acceleration-equivalent reference, physical transfer/covariance mapping and an explicit calibration floor. A commanded but unmeasured scale is not treated as certified metrology.

**Paper-III status:** already covered at the resource-design level. `NO_REOPEN`.

### FM-E — scoped child result promoted to a parent/family claim

The KMQGB coverage contract explicitly forbids a scoped PASS or FAIL from being promoted to a whole framework family without family-scope proof.

Paper III already has an article-facing claim boundary: the result is for the frozen Raman atom-gravimeter architecture; it is not an observed RQIR departure, not a universal apparatus theorem, and it does not claim that historical and prospective components were one raw campaign.

**Paper-III status:** already covered. `NO_REOPEN`.

### FM-F — hidden error/provenance/reproduction dependence

KMQGB closure objects demand explicit error/remainder ledgers and machine-auditable dependencies.

Paper III freezes exact scripts and numerical outputs in a manifest and has an independent clean GitHub-hosted reproduction in which all tracked audits, including negative controls, succeeded.

**Paper-III status:** already covered. `NO_REOPEN`.

### Theory-specific blockers

KMQGB also exposes failures or blockers involving causality/time advance, UV-to-IR continuum limits, topology, physical Hilbert spaces, constraint closure, emergent Lorentzian spin-2 gravity, and family-level theory census completeness.

These are important for Paper IV but are not generic experiment/resource-closure requirements for Paper III. Importing them into Paper III would change the paper's declared scope rather than repair a defect in its methodology.

**Paper-III status:** out of scope. `NO_REOPEN`.

## Saturation result through Iter208

The post-census KMQGB work continues to sharpen concrete missing objects and theory-family boundaries, but the latest independent branches do **not** introduce a new transferable Paper-III resource-closure failure class. In particular, the Iter208 TGFT result is another instance of the already-covered same-realization/provenance-composition class.

Therefore the user's stopping criterion is met for the **current Paper-III methodological scope**:

> New KMQGB models/schools are presently refining or repeating already-covered general closure classes rather than exposing a new Paper-III resource-closure failure mode.

This is a finite benchmark-based saturation statement, not a theorem that no future model can ever expose a new cross-domain failure mode.

## Decision

`PAPER_III_KMQGB_STRESS_GATE = PASS_CURRENT_SCOPE`

`NEW_GENERAL_RESOURCE_CLOSURE_FAILURE_MODE_THROUGH_ITER208 = NONE_OBSERVED`

`PAPER_III_REOPEN_REQUIRED = NO`

`PAPER_III_SCIENTIFIC_MATERIAL_STATUS = REMAIN_FROZEN_100_PERCENT`

`PAPER_IV_D2_D4_D7_TERMINAL_STATUS = STILL_OPEN`

Paper III does **not** need to wait for full Paper-IV D2/D4/D7 terminal closure. KMQGB should continue independently toward Paper IV. Paper III should be reopened only if a future KMQGB result passes the four-part reopening criterion above.

## Next KMQGB action

Continue the active independent Paper-IV branch (`PURE_RANDOM_TENSOR_ENHANCED_NONMELONIC_CONTINUUM_TO_NORMALIZED_4D_GRAVITY_OBSERVABLE_COMPARATOR`) without changing RQIR Core v1.0 or Paper III. If that branch produces a genuinely new cross-domain closure class, run this impact gate again before submission; otherwise keep Paper III frozen.
