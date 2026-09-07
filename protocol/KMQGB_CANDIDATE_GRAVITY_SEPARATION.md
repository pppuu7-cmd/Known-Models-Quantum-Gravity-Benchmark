# KMQGB / Known-Models Benchmark — Separation from Candidate Gravity

Status: FROZEN ARCHITECTURAL RULE
Initialized: 2026-09-08
Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
Branch: `main`
Scope: benchmark / calibration of RQIR on known gravity and quantum-gravity realizations.

## 1. Core principle

KMQGB is a **parallel independent repository**, not a competing or subordinate Candidate Gravity development branch.

Conceptually:

`KMQGB = verification/calibration of frozen RQIR on known models and quantum-gravity schools through concrete realizations`

in parallel with

`Candidate Gravity = construction and blind passage of the same frozen RQIR funnel by the candidate model.`

KMQGB may strengthen the scientific reliability of the Candidate Gravity programme by demonstrating that RQIR correctly recognizes null, positive, and pathological controls. KMQGB results do **not** automatically increase Candidate Gravity readiness.

Candidate Gravity MODEL_READINESS remains externally governed by the authority in `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction`; this benchmark has no authority to change that value.

## 2. Authority and numbering firewall

KMQGB MUST NOT:

1. modify `candidate_gravity/recovery/CURRENT_QG_FRONT.md` in the RQIR repository;
2. modify Candidate Gravity recovery state, readiness, gate status, or authority files;
3. claim or consume Candidate Gravity iteration numbers;
4. write benchmark conclusions into `candidate_gravity/` as if they were Candidate Gravity results;
5. rebase scientific conclusions silently when Candidate Gravity `main` advances.

KMQGB MUST use its own repository authority and its own iteration numbering:

- `KMQGB-001`
- `KMQGB-002`
- `KMQGB-003`
- ...

The moving Candidate Gravity authority SHA/iteration may be **observed and recorded only as external context**, never adopted as KMQGB authority.

## 3. Heavy-compute isolation

KMQGB analytical work may proceed in parallel with Candidate Gravity.

If Candidate Gravity has an active heavy job on the same self-hosted runner, KMQGB MUST NOT launch a competing heavy job that can occupy or delay that runner unless one of the following is true:

- a separate runner/queue is explicitly available;
- Candidate Gravity heavy work has completed or is intentionally paused;
- resource arbitration is explicitly changed and recorded.

Default KMQGB behavior while Candidate Gravity heavy work is active: literature audit, protocol mapping, symbolic/lightweight checks, table/recovery maintenance, and preparation of later heavy jobs without dispatching them to the shared runner.

Runner contention is an operational issue and cannot be interpreted as scientific evidence.

## 4. Frozen-gate firewall

KMQGB may **read and apply** the frozen RQIR gates. It may not alter, weaken, retune, or reinterpret them after observing known-model outcomes.

If KMQGB exposes a credible flaw in the RQIR funnel itself, the response is NOT to silently modify the gate. Instead:

1. freeze the benchmark result obtained under the pre-existing rule;
2. open a separate methodological-audit record;
3. describe the suspected protocol defect and its scope;
4. evaluate the correction independently of the tested model outcome;
5. only after explicit methodological resolution may a new protocol version be created;
6. old and new protocol results must remain distinguishable and auditable.

No post-hoc criterion change is allowed to rescue or reject a known model or Candidate Gravity.

## 5. Readiness independence

KMQGB readiness and Candidate Gravity readiness are independent metrics.

A KMQGB milestone can increase confidence in the **validity of the testing apparatus**, but cannot numerically increase `MODEL_READINESS` for Candidate Gravity without new Candidate Gravity evidence satisfying its own frozen gates.

Therefore:

- KMQGB benchmark progress -> benchmark confidence/readiness only;
- Candidate Gravity model progress -> Candidate Gravity readiness only;
- successful null/positive/pathological control recognition -> stronger validation of RQIR methodology, not automatic model progress.

## 6. Control interpretation

KMQGB should deliberately include:

- **null controls**: e.g. GR when identical to the frozen comparator baseline;
- **positive controls**: realizations with known extra degrees of freedom, poles, or nonzero effects that the funnel should expose;
- **pathological controls**: realizations with known ghost/positivity/causality or consistency problems where applicable.

Before Candidate Gravity residuals are interpreted strongly, KMQGB should demonstrate that the same frozen funnel distinguishes these categories without retuning.

## 7. File/namespace policy

All KMQGB writes belong in this repository only.

Primary current-front files:

- `recovery/CURRENT_BENCHMARK_FRONT.md`
- `recovery/state.json`
- `recovery/RECOVERY_DELTA_NNN.md`

No KMQGB file may replace or shadow Candidate Gravity authority in the RQIR repository.

## 8. Recovery rule

Every fresh-chat recovery MUST read this file before any benchmark write.

If an instruction or artifact conflicts with this separation rule, stop the conflicting benchmark action, record the conflict in a new KMQGB recovery delta, and preserve Candidate Gravity authority unchanged.

## 9. Current scientific consequence

The benchmark is permitted to continue immediately and independently with GR -> GR + low-energy quantum-gravity EFT -> remaining known-model queue.

The benchmark may use the frozen Candidate Gravity/RQIR protocol as a **read-only external input**. Any later methodological revision must be separately versioned and cannot retroactively overwrite the original frozen benchmark outcome.
