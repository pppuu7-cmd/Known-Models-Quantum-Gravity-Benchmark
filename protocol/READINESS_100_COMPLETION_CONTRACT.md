# KMQGB 100% Repository / Methodology Completion Contract

**Introduced:** KMQGB Iter178  
**Scope:** R1 repository readiness and R2 KMQGB methodology/material readiness only.  
**Scientific firewall:** this contract does **not** change R3 Candidate Gravity scientific readiness, legacy R4, Closure Wave 02, or the Paper-IV global verdict.

## 1. Why this contract exists

`protocol/READINESS_METRICS.md` froze the remaining non-scientific deficits as:

### R1

- executable layer: `12/15`;
- candidate/pre-ansatz scaffold: `7/10`;
- automated reproducibility/tests/CI/artifact packaging: `8/10`.

All other R1 components were already full, giving `92/100`.

### R2

- Beyond-C5 escape / parent-principle methodology: `10/15`;
- executable methodology: `8/10`;
- consolidated playbook/article-ready synthesis: `7/10`.

All other R2 components were already full, giving `90/100`.

The missing points are therefore **repository and methodology obligations**, not missing physical discoveries. They may be closed without pretending that an open Paper-IV physical object is terminal.

## 2. Non-negotiable separation of percentages

The following statements may simultaneously be true:

- `R1 = 100%`: repository infrastructure is complete for its declared purpose;
- `R2 = 100%`: the benchmark methodology/material package is complete for its declared purpose;
- `R3 < 100%`: no scientifically complete Candidate Gravity model exists;
- `CW2 < 3/3`: known-framework physical closure objects remain open;
- `Paper IV = NOT_YET_AUTHORIZED`.

Any validator that forces these distinct quantities to move together is wrong.

## 3. Frozen closure obligations for R1

### R1-E — executable layer `12/15 -> 15/15`

All three points close only when the repository contains:

1. a machine-readable executable-test registry with purpose and command for every critical frozen methodology control;
2. one orchestrator that validates the registry and executes the registered controls fail-closed;
3. a repository-completion validator that checks the cross-file governance invariants, including the scientific firewall.

Required authorities:

- `protocol/EXECUTABLE_TEST_REGISTRY.json`;
- `code/methodology_orchestrator.py`;
- `code/repository_completion_validator.py`.

### R1-C — candidate/pre-ansatz scaffold `7/10 -> 10/10`

All three points close only when the repository contains:

1. a prospective machine-readable v1.3 candidate template that can represent a scientifically BLOCKED state without inventing values;
2. a documented schema for that record;
3. a fail-closed validator that prevents promotion, heavy-compute authorization, or publication wording from outrunning the evidence.

Required authorities:

- `schemas/candidate_gravity_record_v1_3.schema.json`;
- `templates/candidate_gravity_record_v1_3.template.json`;
- `code/kg_candidate_record_v13_validator.py`.

A valid blocked template counts as scaffold completeness. It does **not** count as Candidate Gravity scientific progress.

### R1-P — reproducibility/tests/CI/artifact packaging `8/10 -> 10/10`

Both points close only when:

1. the critical release bundle has an explicit machine-readable contents policy;
2. a deterministic builder hashes every included file and produces a reproducibility ZIP with a manifest;
3. CI builds the bundle and uploads it as a workflow artifact after all validators pass.

Required authorities:

- `release/BUNDLE_CONTENTS.json`;
- `code/build_release_bundle.py`;
- `.github/workflows/methodology-ci.yml`.

## 4. Frozen closure obligations for R2

### R2-B — Beyond-C5 / parent-principle methodology `10/15 -> 15/15`

The five remaining points close only when one operational procedure connects all of the following without a conceptual gap:

`escape-door declaration -> functional-freedom test -> parent object -> same-realization map -> physical reduction -> full comparator quotient -> residual -> rigidity/holdout -> compute authorization -> publication claim`.

The procedure must contain explicit stop states and must accept `BLOCKED` as a scientifically valid outcome.

Authority:

- `protocol/BEYOND_C5_PARENT_PRINCIPLE_DECISION_PROCEDURE.md`.

### R2-X — executable methodology `8/10 -> 10/10`

Both points close when:

1. the operational methodology is represented in the executable registry/orchestrator;
2. CI executes the orchestrator plus the prospective-record and repository-completion validators.

Text-only methodology cannot close this component.

### R2-A — consolidated playbook / article-ready synthesis `7/10 -> 10/10`

All three points close only when a publication-facing package exists with:

1. a claim/evidence/status matrix that distinguishes theorem, derived KMQGB result, external authority, blocked item and forbidden wording;
2. a methods/evidence narrative showing exactly how a result can be reconstructed from the repository;
3. a limitations section that explicitly preserves open CW2 objects and forbids translating infrastructure completeness into scientific completeness.

Authorities:

- `publication/KMQGB_METHODS_EVIDENCE_MATRIX.md`;
- `publication/claim_evidence_matrix.json`.

## 5. Promotion rule for R1/R2

R1 and R2 may be changed to 100 **only after**:

- every required authority above exists on `main`;
- the methodology CI runs the new controls;
- the latest CI run on the canonical completion commit is `success`;
- `recovery/state.json` still reports the unchanged scientific statuses unless separately justified by new physical evidence.

The score-changing recovery delta must name this contract and the successful CI run.

## 6. Scientific anti-inflation invariants

At the time this contract is introduced, the completion validator must enforce at least:

- `RQIR Core v1.0 = FROZEN`;
- Paper IV remains `NOT_YET_AUTHORIZED` unless the frozen decision ledger independently changes;
- `NEW_REQUIRED` remains unauthorized while blocked known-framework objects exist;
- Candidate Gravity scientific readiness is not inferred from repository readiness;
- a BLOCKED candidate template is valid and must not be auto-promoted;
- heavy compute remains forbidden for structural/provenance/matching blockers.

## 7. Definition of “repository prepared to 100%”

For this project, the phrase means:

> every repository and methodology obligation needed to continue, audit, reproduce, package, restore, benchmark known frameworks, and evaluate a future Candidate Gravity proposal is present and machine-checked.

It does **not** mean:

> all open quantum-gravity physics has been solved.

This distinction is permanent.