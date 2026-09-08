# Stable Readiness Metrics for Candidate Gravity Research

**Status:** frozen reporting methodology.  
**Purpose:** keep repository readiness, KMQGB methodology readiness and scientific Candidate Gravity readiness separate and stable across chats/iterations.

These percentages measure different objects and must never be merged.

## R1 — Repository readiness for future Candidate Gravity construction

This measures whether the KMQGB repository is a reliable, reproducible workspace from which a future KG candidate can be built, audited and restored.

Weights:

1. recovery/provenance/versioning: 20 points;
2. benchmark corpus/comparator registry preservation: 15 points;
3. permanent KG protocol organization: 20 points;
4. executable schema/validator/reference-code layer: 15 points;
5. candidate/pre-ansatz machine-record scaffold: 10 points;
6. automated reproducibility/tests/CI/artifact packaging: 10 points;
7. external RQIR firewall/authority synchronization: 10 points.

Current score at KMQGB Iteration 049:

- recovery/provenance/versioning: `20/20`;
- benchmark/comparator corpus: `15/15`;
- permanent protocols: `20/20`;
- executable layer: `12/15` — schema, validator and multiple reference implementations exist, including cross-representation rigidity, but full CI/end-to-end automated scientific checks are incomplete;
- candidate/pre-ansatz scaffold: `7/10` — fail-closed records exist, but no promoted candidate package exists;
- automated reproducibility/CI/artifact packaging: `6/10` — reference scripts exist, but complete automated pipeline/CI coverage is not frozen;
- external firewall/synchronization: `10/10`.

**R1 = 90/100 = 90%.**

R1 may increase only when one of the scored infrastructure gaps is actually closed. Scientific model progress alone does not increase R1.

## R2 — KMQGB methodology/material readiness for building a future KG

This measures how mature the benchmark-derived construction method is, not whether a new theory has been found.

Weights:

1. known-model benchmark/comparator evidence: 15 points;
2. comparator/attribution taxonomy: 15 points;
3. response-completeness/Ward/constraint/projection methodology: 15 points;
4. residual geometry/identifiability/rigidity/holdout/test-suite methodology: 20 points;
5. Beyond-C5 escape and parent-principle selection methodology: 15 points;
6. executable/machine-readable methodology: 10 points;
7. consolidated construction playbook/article-ready synthesis: 10 points.

Current score at KMQGB Iteration 049:

- benchmark/comparator evidence: `14/15` — broad but not literally exhaustive of all QG realizations;
- comparator/attribution taxonomy: `15/15`;
- completeness/constraints/projection: `15/15`;
- residual/identifiability/rigidity: `19/20` — global nonlinear application to a real KG residual is still absent;
- escape/parent-principle methodology: `9/15` — amplitude-principle saturation and cross-representation rigidity are now frozen, but no genuinely novel parent-selection principle has survived known comparators;
- executable methodology: `8/10` — fail-closed records/validators and reference implementations exist but full automated end-to-end scientific pipeline is incomplete;
- consolidated playbook/synthesis: `6/10` — design priors and recovery are strong, but final compact construction manual/paper-grade synthesis is not yet complete.

**R2 = 86/100 = 86%.**

Change from Iteration 048: `+1 percentage point`, entirely from the parent-principle/escape methodology component. No scientific KG readiness was promoted.

## R3 — Scientific readiness of Candidate Gravity itself

This is controlled **only by external RQIR Candidate Gravity authority** and its own stable rubric. KMQGB cannot promote this value.

At the latest directly observed authority used when freezing this metric, RQIR reports

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

Therefore

**R3 = MODEL_READINESS = 24%.**

Always refresh external `candidate_gravity/recovery/CURRENT_QG_FRONT.md` before reporting R3.

## R4 — Current research-task completion

Every research iteration should additionally report the percentage completion of the currently active finite task/wave.

R4 is task-local and resets when a new task is frozen. It must not be confused with R1, R2 or R3.

## Reporting format

Every future KMQGB/Candidate Gravity iteration should include at least:

- `Repository readiness (R1): XX%`;
- `KMQGB methodology/material readiness (R2): XX%`;
- `Candidate Gravity scientific readiness (R3): XX%`;
- `Current task completion (R4): XX%`.

Any score change must state which rubric component changed and why.
