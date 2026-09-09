# Stable Readiness Metrics for KMQGB Post-Freeze Research

**Updated:** 2026-09-09.  
**Current authority:** post-Iter144 freeze transition / active Paper-IV PF1 wave.  
**RQIR standard:** **Core v1.0 FROZEN**.

These metrics measure different objects and must not be averaged.

## R1 — Repository readiness

Frozen component scores remain:

- recovery/provenance/versioning `20/20`;
- benchmark/comparator corpus `15/15`;
- permanent protocols `20/20`;
- executable layer `12/15`;
- candidate/pre-ansatz scaffold `7/10`;
- automated reproducibility/tests/CI/artifact packaging `8/10`;
- external firewall/synchronization `10/10`.

**R1 = 92%.**

The post-freeze governance and new Paper-IV wave improve use of the existing infrastructure but do not close a remaining whole R1 rubric point.

## R2 — KMQGB methodology/material readiness

Frozen component scores now are:

- benchmark/comparator evidence `15/15`;
- comparator/attribution taxonomy `15/15`;
- completeness/constraints/projection `15/15`;
- residual/identifiability/rigidity `20/20`;
- Beyond-C5 escape/parent-principle methodology `10/15`;
- executable methodology `8/10`;
- consolidated playbook/article-ready synthesis `7/10`.

**R2 = 90%.**

### Iter144 score change

`R2: 89 -> 90` because the previously frozen remaining criterion in `residual/identifiability/rigidity` was explicitly satisfied:

- external RQIR closed the nonlinear detector observable `P=(1+C cos Phi)/2` with contrast, contrast drift, readout gain/drift/offset and calibrated-reference nuisance under the source-traceable physical covariance;
- KMQGB independently incorporated a NumPy detector-facing regression fixture;
- methodology-ci run `34397157673` / job `102619589784` completed `success`, including both source-traceable physical-covariance and nonlinear detector-facing likelihood self-tests;
- required negative controls remain failures rather than being regularized into PASS states.

Therefore `residual/identifiability/rigidity` closes `19/20 -> 20/20` exactly as preregistered before the external result was available.

No other R2 component changes.

## R3 — Candidate Gravity scientific readiness

Controlled only by external Candidate-Gravity authority.

Latest directly checked authority remains RQIR Candidate Gravity Iter675:

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

**R3 = 24%.**

Candidate Gravity remains conditional and is not the active KMQGB research front.

## External programme status

RQIR has now frozen **Core v1.0** and reports **Papers I–III scientific/material readiness = 100%**. Paper IV remains active/prerequisite-blocked at the programme level; the last strict audit retains **55%** for Paper IV. These programme/article percentages do not replace R3.

## Legacy R4 — minimal novel parent-principle search

The historical/conditional parent-search score remains:

- P1 `15/15`;
- P2 `15/15`;
- P3 `15/15`;
- P4 `0/25`;
- P5 `0/20`;
- P6 `0/10`.

**Legacy R4 = 45%.**

This branch is now **PAUSED / CONDITIONAL ON PAPER IV**. It is preserved as design evidence but is no longer the active KMQGB task. No score is removed or promoted merely by changing research priority.

## Active task — Paper-IV frozen-core benchmark campaign

Active campaign: `post_freeze_paper_iv_wave_01`.

Frozen denominator: 5 representative known-framework regressions.

Current terminal coverage after PF1-01 CFS and PF1-02 GR/EFT:

**2/5 = 40%.**

This is a wave-completion metric, not a Candidate-Gravity readiness score.

## Governance

Post-freeze authority:

- RQIR Core v1.0 is the fixed judge;
- KMQGB owns model adapters and benchmark writes;
- future Candidate Gravity is separate and may not tune the judge;
- a real RQIR Core defect requires canonical RQIR change-control and regression over affected benchmark records.

KMQGB enforcement: `protocol/RQIR_CORE_V1_BENCHMARK_FIREWALL.md`.

## Reporting format

Future iterations should report:

- `R1 Repository readiness = 92%` unless a frozen R1 rubric component changes;
- `R2 KMQGB methodology/material readiness = 90%` unless a frozen R2 component changes;
- `R3 Candidate Gravity readiness = 24%` unless external Candidate-Gravity authority changes;
- `Legacy parent-search R4 = 45% (paused/conditional)`;
- `Active Paper-IV post-freeze wave completion = X/5 = Y%`.

Any score change must name the exact rubric component and evidence.