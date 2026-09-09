# KMQGB ↔ RQIR Core v1.0 Benchmark Firewall

**Status:** mandatory post-freeze governance.  
**RQIR authority:** `RQIR_VERSION.json` with `core_version=1.0`, `status=FROZEN`.  
**Purpose:** make KMQGB the active known-model proving ground without allowing benchmark outcomes to move the RQIR judge.

## Repository roles

- **RQIR Core v1.0:** frozen model-independent judge / observable-comparator standard.
- **KMQGB:** active known-model and known-school benchmark laboratory supplying Paper-IV evidence.
- **Future Candidate Gravity:** separate conditional model repository; it may not alter the judge used on external models.

## Mandatory benchmark header

Every post-freeze KMQGB record must declare:

- `rqir_core_version: 1.0`;
- RQIR freeze/version authority ref;
- model/school native object and domain;
- KMQGB adapter ref;
- RQIR observable block(s) used;
- comparator registry/domain;
- whether the conclusion is an observable result, a consistency result, or a missing-object block.

## Adapter rule

If a framework can be mapped into an existing RQIR observable/comparator interface by a model-specific translation, the translation is a **KMQGB adapter**. RQIR Core is not changed.

Examples include native-to-relational observable maps, regulator/continuum maps, amplitude-to-detector maps, process-to-causal-observable maps and framework-specific covariance construction.

Difficulty computing an adapter is not a Core defect.

## Core-defect escalation rule

A KMQGB result may request RQIR change-control review only when a physically admissible object cannot in principle be represented under the frozen semantics. The request must satisfy the canonical RQIR change-control document, including defect witness, adapter-impossibility proof, version bump where required and regression over affected historical benchmarks.

A model failing, being blocked, or losing novelty under a comparator is never by itself a Core defect.

## Paper-IV terminal discipline

Model-level benchmark statuses remain fail-closed, including:

- `EXACT_COMPARATOR_IDENTITY`;
- `OPERATIONALLY_DEGENERATE`;
- `FAIL_RQIR_CONSISTENCY`;
- `BLOCKED_MISSING_REQUIRED_OBJECT`;
- `BLOCKED_PROTOCOL_MISMATCH`;
- `ROBUST_NONZERO_RESIDUAL` only after full common-domain comparator quotient and detector/identifiability checks.

The overall Paper-IV decision is one of:

- `EXISTING_SUFFICIENT`;
- `ADAPT_EXISTING`;
- `HYBRID_REQUIRED`;
- `NEW_REQUIRED`.

No single `BLOCKED`, consistency failure, or uncomputed quantity counts as evidence for `NEW_REQUIRED`.

## Candidate firewall

Future Candidate Gravity results are downstream of Paper IV and may not be used to tune RQIR Core v1.0. If an independently demonstrated methodological defect requires a successor RQIR version, prior known-model benchmarks must be rerun before the candidate is re-evaluated.

## Post-freeze strategy

KMQGB will now prioritize frozen-core regression and expansion of known-school coverage. Parent-principle/Candidate-Gravity design work may remain as conditional design evidence, but it is not the active Paper-IV front unless and until the known-model benchmark programme authorizes `NEW_REQUIRED`.