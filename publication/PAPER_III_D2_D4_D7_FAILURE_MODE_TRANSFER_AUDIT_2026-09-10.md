# Paper III D2/D4/D7 failure-mode transfer audit

**Date:** 2026-09-10  
**Scope:** KMQGB -> RQIR Paper III publication-layer stress test  
**RQIR Core:** v1.0 **FROZEN**  
**Decision type:** publication clarification / no Core change

## Question

Do the KMQGB D2/D4/D7 benchmark failures reveal a new *resource-closure* failure mode that is absent from RQIR Paper III and therefore requires changing the Paper-III method before submission?

## Frozen Paper-III resource taxonomy

Paper III evaluates the nuisance-profiled resource map only after target/calibration and detector-facing objects have been declared. For the data-only homogeneous case it already separates two genuine resource-layer outcomes:

1. **geometry-limited:** `kappa_* = 0`, so no common increase of the same resource repairs exact target/nuisance alignment;
2. **budget-limited:** `kappa_* > 0`, but the minimum resource/cost needed to reach the information target exceeds the physically available budget.

Its apparatus binding further requires physical noise, detector response, calibration and exposure to be declared. The manuscript explicitly prevents raw samples from distinct experiments being statistically concatenated, distinguishes coarse digitization from raw data, and does not retrofit prospective chirp metrology into the historical apparatus record.

## What KMQGB D2/D4/D7 are actually failing on

The current global D7 attempt has 14 Tier-1 rows, 13 nonterminal. D2 is not closed, D4 is not closed, and D7 is not closed. Across the nonterminal rows, the dominant blockers are missing or incomplete end-to-end physical objects: same-realization amplitudes, continuum-to-observable maps, invariant/normalized observables, parameter ancestry, family-level coverage, comparator normalization, and propagated error certificates.

These are not examples in which a valid Paper-III information map has been constructed and then shown to require a third kind of resource. They are cases in which the object required to define the downstream comparator is incomplete, so the residual itself is undefined at the relevant scope.

### Independent repetition 1 — TGFT

Iter208 finds positive Lorentzian Barrett-Crane relational/mean-field objects and positive FRG controls, but in different audited microscopic realizations. D6 forbids splicing them into a single same-realization chain. The result is correctly `BLOCKED_MISSING_REQUIRED_OBJECT`, not scientific FAIL and not a resource-budget failure.

### Independent repetition 2 — enhanced/nonmelonic pure tensors

Iter209 finds a reproducible pregeometric RG fixed-point candidate with regulator sensitivity, but the same realization lacks an emergent Lorentzian 3+1/4D gravity observable, normalized common-domain comparator, and propagated error map. Again the result is `BLOCKED_MISSING_REQUIRED_OBJECT`, not scientific FAIL and not a resource-budget failure.

### Global blocker-set classification

The 13 D7 blockers collapse, for Paper-III purposes, into three layers:

- **pre-resource admissibility/completeness:** the physical score/observable/calibration/error object is not yet sufficiently defined or provenance-compatible to instantiate a resource problem;
- **resource layer:** once instantiated, Paper III already distinguishes geometry-limited from budget/engineering-limited closure;
- **downstream benchmark terminality:** family coverage, common residual completion and global D7 proof obligations belong to Paper IV, not to the Paper-III resource law.

Therefore `BLOCKED` should **not** be imported into Paper III as a third resource regime. Doing so would change failure-state/admissibility semantics and would require formal Core versioning under RQIR change control.

## Transfer result

**NO_NEW_RESOURCE_FAILURE_MODE_FOUND.**

The KMQGB D2/D4/D7 evidence strengthens a narrower publication statement: a resource-closure calculation is meaningful only after the physical response, covariance, calibration, normalization and provenance needed to define `{s_k, J_k, Lambda}` and the apparatus resource ledger are mutually compatible. If those objects cannot be assembled without cross-realization splicing or missing normalization/error propagation, the design is **not yet evaluable as resource closed**; it is not a third resource-limited phase.

This statement is already implicit in Paper III's apparatus-binding and provenance sections, so it can be added as an explicit clarification without changing Eq. (1), Proposition 1, the geometry/budget dichotomy, or any frozen numerical result.

## Recommended manuscript insertion

Suggested placement: Discussion, after the current limitations paragraph and before the paragraph beginning “The method is not restricted to gravimetry.”

> A resource-closure classification also presupposes that the detector response, covariance, calibration map and physical resource ledger define one provenance-compatible experimental object. If a forecast can be assembled only by splicing incompatible realizations, or if the normalization or uncertainty propagation needed to define the detector-facing scores is absent, the design is not yet evaluable as either geometry-limited or budget-limited. This is an applicability condition on the resource calculation rather than a third resource regime: once the required physical objects are declared, Eq. (1) determines whether the remaining obstruction is nuisance geometry or finite experimental budget.

## Stop-rule assessment for Paper III

For the present KMQGB corpus, the stop criterion is now substantially satisfied: materially different branches (TGFT and enhanced/nonmelonic pure tensors), together with the global 13-family D7 blocker set, repeat object/provenance/normalization incompleteness rather than generating a new resource-layer failure mode.

This is **not** a universal proof that no future sensing architecture can expose a missing assumption. It is a prospective cross-domain stress test showing that the current benchmark evidence does not justify reopening RQIR Core v1.0 or delaying Paper III for Paper-IV completion.

## Decision

- RQIR Core v1.0: **NO CHANGE**.
- Paper III scientific closure: **RETAIN 100%**.
- KMQGB-derived action for Paper III: **one publication clarification paragraph only**.
- D2/D4/D7 continuation: remains a Paper-IV task and should not block Paper-III submission unless it later demonstrates a concrete methodological defect independent of model outcome.
