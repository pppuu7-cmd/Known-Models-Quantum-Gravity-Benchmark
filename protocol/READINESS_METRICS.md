# Stable Readiness Metrics for Candidate Gravity Research

**Status:** frozen reporting methodology.  
**Purpose:** keep repository readiness, KMQGB methodology readiness and scientific Candidate Gravity readiness separate and stable across chats/iterations.

These percentages measure different objects and must never be merged.

## R1 — Repository readiness for future Candidate Gravity construction

Weights:

1. recovery/provenance/versioning: 20 points;
2. benchmark corpus/comparator registry preservation: 15 points;
3. permanent KG protocol organization: 20 points;
4. executable schema/validator/reference-code layer: 15 points;
5. candidate/pre-ansatz machine-record scaffold: 10 points;
6. automated reproducibility/tests/CI/artifact packaging: 10 points;
7. external RQIR firewall/authority synchronization: 10 points.

Current score:

- recovery/provenance/versioning: `20/20`;
- benchmark/comparator corpus: `15/15`;
- permanent protocols: `20/20`;
- executable layer: `12/15` — schema, fail-closed validator and reference implementations exist; Iter059 adds an executable P4 functional-freedom prefilter, but a full candidate end-to-end numerical pipeline is not yet frozen;
- candidate/pre-ansatz scaffold: `7/10` — exploratory machine records exist, but no promoted candidate package exists;
- automated reproducibility/tests/CI/artifact packaging: `8/10` — `.github/workflows/methodology-ci.yml` validates repository JSON, compiles reference code, runs validator/completeness/COR/contrast/cross-order/intervention/holdout/minimal-suite/cross-representation and P4 functional-freedom self-tests, and checks recovery/construction entrypoints on GitHub-hosted runners. Remaining gap: richer artifact packaging/end-to-end candidate fixture/coverage reporting;
- external firewall/synchronization: `10/10`.

**R1 = 92/100 = 92%.**

Iter060 does not raise R1 because the remaining repository-readiness gaps are end-to-end candidate execution/packaging rather than documentation availability.

## R2 — KMQGB methodology/material readiness for building a future KG

Weights:

1. known-model benchmark/comparator evidence: 15 points;
2. comparator/attribution taxonomy: 15 points;
3. response-completeness/Ward/constraint/projection methodology: 15 points;
4. residual geometry/identifiability/rigidity/holdout/test-suite methodology: 20 points;
5. Beyond-C5 escape and parent-principle selection methodology: 15 points;
6. executable/machine-readable methodology: 10 points;
7. consolidated construction playbook/article-ready synthesis: 10 points.

Current score:

- benchmark/comparator evidence: `15/15` — the corpus includes scoped terminal audits of the first/second-wave controls plus major architecture classes including covariant LQG/spinfoams, GFT/TGFT, random tensor models, causal fermion systems, QFT-vector/induced gravity and matrix-model parent precedents. This does **not** mean literally every model in the literature is exhausted;
- comparator/attribution taxonomy: `15/15`;
- completeness/constraints/projection: `15/15`;
- residual/identifiability/rigidity: `19/20` — global nonlinear application to a real KG residual is still absent;
- escape/parent-principle methodology: `10/15` — amplitude-principle saturation, cross-representation/background audits, spectral-origin completeness, Wave38 structural-prefiltering and the Iter059 `P4_FUNCTIONAL_FREEDOM_NO_GO` provide a reproducible necessary-condition kill test, but no novel parent-selection principle has survived known comparators and produced the required explicit hard relation;
- executable methodology: `8/10` — fail-closed records/validators, reference implementations, functional-freedom diagnostic and methodology CI exist, but full end-to-end candidate promotion automation is incomplete;
- consolidated playbook/synthesis: `7/10` — Iter060 adds `protocol/CANDIDATE_GRAVITY_CONSTRUCTION_PLAYBOOK.md`, a single fail-closed operational route from raw idea through pre-P4 functional-freedom/containment filters, G0-G10 promotion gates, machine record, holdout and compute triage. Remaining gap: paper-grade consolidated synthesis with polished derivations/examples and article-ready presentation.

**R2 = 89/100 = 89%.**

Change from Iter059: `+1 percentage point`, solely from consolidated playbook/synthesis `6/10 -> 7/10`. No scientific Candidate Gravity result is implied by this methodology increase.

## R3 — Scientific readiness of Candidate Gravity itself

Controlled **only by external RQIR Candidate Gravity authority** and its stable rubric. KMQGB cannot promote this value.

Latest directly observed authority at KMQGB Iter060 is **RQIR Iteration 616**:

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

Iter616 closes exact source/Iter582 q2-bucket identity and exact external scalar endpoint amputation, narrowing the remaining native binding ambiguity to one common nonzero scalar `N_native`. The full native binding is still `BLOCKED`, not FAIL and not residual; no robust comparator-subtracted residual has therefore been authorized.

**R3 = 24%.**

Before every future R3/heavy-compute report, refresh external RQIR authority again.

## R4 — Current research-task completion

Current task: `MINIMAL_NOVEL_PARENT_PRINCIPLE_SEARCH`.

Authority: `protocol/MINIMAL_NOVEL_PARENT_PRINCIPLE_SEARCH_RUBRIC.md`.

Current score:

- P1 known-principle saturation `15/15`;
- P2 multi-representation/background rigidity `15/15`;
- P3 spectral-origin/dispersion requirements `15/15`;
- P4 explicit novel low-freedom parent principle `0/25`;
- P5 immediate comparator survival `0/20`;
- P6 pre-ansatz machine record for a genuine survivor `0/10`.

**R4 = 45%.**

Wave38 and Iter059/060 methodology work reduce false-positive search space and process ambiguity but do not raise R4. The fail-closed pre-P4 rule remains: a parent whose structural-null hard freedom `FF_D(P)` grows without bound with hard/EFT cutoff is `FUNCTIONAL_FREEDOM_BLOCKED`. Only an actual explicit finite-freedom constructive survivor may raise R4.

## Reporting format

Every future KMQGB/Candidate Gravity iteration must report:

- `Repository readiness (R1): XX%`;
- `KMQGB methodology/material readiness (R2): XX%`;
- `Candidate Gravity scientific readiness (R3): XX%`;
- `Current task completion (R4): XX%`.

Any score change must state which rubric component changed and why.
