# KMQGB Recovery Delta 178

**Date:** 2026-09-10  
**Scope:** repository and methodology completion; no physical Paper-IV closure claimed.

## Score change

- `R1 Repository readiness: 92% -> 100%`.
- `R2 KMQGB methodology/material readiness: 90% -> 100%`.
- `R3 Candidate Gravity scientific readiness: 24%` unchanged.
- `Legacy R4: 45%` unchanged and paused/conditional.
- PF1 remains `5/5 terminal`.
- Closure Wave 02 remains `0/3 terminal`.
- Paper IV remains `NOT_YET_AUTHORIZED`.

Authority for what may close R1/R2:

`protocol/READINESS_100_COMPLETION_CONTRACT.md`.

## New permanent repository authorities

### End-to-end methodology

`protocol/BEYOND_C5_PARENT_PRINCIPLE_DECISION_PROCEDURE.md`

connects same-realization provenance, parent/upstream primitive closure, functional freedom, escape-door taxes, rigid prediction, physical reduction, comparator quotient, residual geometry, identifiability/rigidity/holdout, multiscale transport, compute authorization and publication authorization in one fail-closed decision chain.

### Executable methodology

- `protocol/EXECUTABLE_TEST_REGISTRY.json`;
- `code/methodology_orchestrator.py`.

The registry gives each critical methodology regression an ID, command, category and purpose. The orchestrator rejects missing files, duplicate IDs, command/path mismatches, timeouts and nonzero exits.

### Candidate/pre-ansatz scaffold v1.3

- `schemas/candidate_gravity_record_v1_3.schema.json`;
- `templates/candidate_gravity_record_v1_3.template.json`;
- `code/kg_candidate_record_v13_validator.py`.

v1.3 adds explicit functional-freedom, same-realization, compute-authorization and publication-trace state on top of the mature v1.2 gates. The canonical template is intentionally scientifically BLOCKED. Its structural validity does not imply promotion.

### Repository completion validator

`code/repository_completion_validator.py`

checks cross-file completion plus scientific anti-inflation invariants. In strict mode it requires R1=R2=100 while preserving separate R3/Paper-IV/CW2 accounting.

### Reproducibility packaging

- `release/BUNDLE_CONTENTS.json`;
- `code/build_release_bundle.py`.

The builder SHA-256 hashes every frozen bundle input, inserts `MANIFEST.json`, normalizes ZIP order/timestamps/permissions, and can require a byte-identical second build.

GitHub Actions now uploads the reproducibility bundle and orchestrator summary.

### Publication synthesis

- `publication/KMQGB_METHODS_EVIDENCE_MATRIX.md`;
- `publication/claim_evidence_matrix.json`.

The publication matrix explicitly separates `ESTABLISHED_EXTERNAL`, `DERIVED_KMQGB`, `REPRODUCED_EXECUTABLE`, `OPEN_BLOCKED`, `HYPOTHESIS_ONLY`, and `FORBIDDEN_OVERCLAIM`.

## Pre-score validation

Methodology CI run `34412786245`, job `102670803282`:

- conclusion: `success`;
- all 36 steps: success;
- v1.3 scaffold test: success;
- executable registry validation: success;
- full orchestrator: success;
- repository completion invariants pre-score: success;
- deterministic bundle rebuild: success;
- artifact upload: success.

Artifact:

- name: `kmqgb-reproducibility-bundle`;
- id: `10127884011`;
- workflow digest: `sha256:e82908f7bd5b84445389697e40c16290490a4e7f407ab84daa529f3d3d3e92b1`.

This successful pre-score run satisfies the completion contract's requirement that the new capabilities exist and execute before percentages are promoted.

## Scientific state deliberately unchanged

### O-AS

Still requires:

`STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`.

### O-LQG

Still requires the missing physical parts of

`MULTISCALE_GAMMA_CERTIFICATE={M_same-realization,T_RG,C_observable}`.

`C_observable` is executable methodology. `M_same-realization` and same-parent `T_RG` remain open.

### O-CFS

Still requires:

`FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR`.

## Compute decision

Heavy compute remains `IDLE`. The active blockers remain structural/analytic/provenance/matching objects.

## Next recovery rule

After the score-promoting files are synchronized, CI must be tightened to run

`python code/repository_completion_validator.py --require-100`

and require this delta. A successful strict post-score run is the final verification lock; if it fails, R1/R2 completion must be treated as not yet frozen.
