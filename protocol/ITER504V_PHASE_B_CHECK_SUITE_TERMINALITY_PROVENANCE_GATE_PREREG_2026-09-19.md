# ITER504V Phase-B check-suite terminality provenance gate — preregistration

Date: 2026-09-19
Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
Lane: KMQGB Research / Closure
Gate: `ITER504V_PHASE_B_CHECK_SUITE_TERMINALITY_PROVENANCE_GATE`

## HYPOTHESIS

GitHub check-suite state can be used as an independent metadata-only terminality witness for authoritative Phase-B source run `35405065903` only if it is coherent with the fresh workflow-job inventory. In particular, if at least one job in the exact run remains nonterminal, the exact check suite must also remain nonterminal and must not carry a terminal conclusion.

## exact OBJECT

Only GitHub Actions metadata for:
- repository `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`;
- source run `35405065903`, attempt `1`;
- immutable source head `31fcdacffcc394e96b73917083281edb90d6753c`;
- exact check suite `95888147622`;
- exact workflow jobs belonging to that run/attempt/head.

No Actions artifact ZIP bytes, case payloads, leaves, slopes, drifts, certification values, assemblies, aggregates, or counterexample values are admissible inputs.

## DEPENDENCY

- Phase-B preregistration `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
- one-source execution authority `caf67585a9fad990dd90948df51839e6ed7cf891`;
- immutable launch/head `31fcdacffcc394e96b73917083281edb90d6753c`;
- full-job-inventory provenance closure prereg `cb69a9057a0b74cf8680e57f2d810d72ccdc6f93` and terminal authority `4f2ee5a7f6312733ec782ec3a6ee461fc6527a3b`.

## SOURCE / REALIZATION AUTHORITY

GitHub REST metadata for the exact run, exact check suite, and exact jobs is the sole execution/provenance source. Repository `main` and frozen Phase-B authority define the scientific object; this gate does not read or classify scientific payload.

## FROZEN INPUTS

- run id `35405065903`;
- attempt `1`;
- head `31fcdacffcc394e96b73917083281edb90d6753c`;
- check-suite id `95888147622`;
- expected source-lock id `105792998164`;
- expected instantiated job inventory from prior closure: total `385` = source-lock `1` + matrix jobs `384`;
- no downstream science payload access.

## POSITIVE CONTROLS

1. Run/check-suite/job metadata must bind to the frozen repository/head.
2. Source-lock remains terminal `success`.
3. Fresh job metadata must expose at least one exact-run job and preserve run/head identity.
4. If a nonterminal job is observed, its status must be one of GitHub's nonterminal states and its conclusion must be null.

## NEGATIVE CONTROLS

- wrong run id, wrong attempt, wrong head, or wrong check-suite id -> `INVALID_IMPLEMENTATION`;
- terminal check suite (`status=completed` with terminal conclusion) while any exact-run job is fresh-nonterminal -> terminality-signal defect;
- check-suite endpoint unavailable or unable to bind to exact head/run while jobs are readable -> `BLOCKED_SCOPED`;
- any scientific payload consumption -> `INVALID_IMPLEMENTATION`.

## PASS

`ITER504V_PHASE_B_CHECK_SUITE_NONTERMINALITY_COHERENT_SCOPED` iff fresh exact-run metadata shows at least one nonterminal job and the exact check suite is also nonterminal with no terminal conclusion, with all identity controls satisfied.

## FAIL

`ITER504V_PHASE_B_CHECK_SUITE_TERMINALITY_SIGNAL_DEFECT_VERIFIED_SCOPED` iff fresh exact-run metadata shows at least one nonterminal job but the exact check suite is terminal or carries a terminal conclusion.

## BLOCKED / INVALID

- `ITER504V_PHASE_B_CHECK_SUITE_TERMINALITY_PROVENANCE_BLOCKED_SCOPED` for inaccessible/insufficient exact check-suite metadata;
- `INVALID_IMPLEMENTATION` for identity mismatch, criteria violation, or prohibited scientific payload access.

## INTERPRETATION CEILING

This is metadata/provenance closure only. PASS means only that the exact check suite is presently coherent with a nonterminal exact-run job state and may be used as an auxiliary terminality signal. FAIL means only that the check-suite terminality signal is unreliable for this run. Neither outcome classifies Phase-B science, repairs cancelled shards, authorizes rerun, promotes any child result to all-domain/family/D7 closure, or supports Candidate Gravity / Paper IV / global quantum-gravity claims.

Frozen governance retained: `RQIR Core v1.0 = FROZEN`; `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; `TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`; green CI != science.
