# Independent Critical Review — ITER504V Phase-B case-job timeout causality provenance

Date: 2026-09-19
Lane: independent KMQGB Critical Review / Verification
Verdict: `CONFIRMED_SCOPED`

## Result reviewed

Exactly one bounded latest terminal preterminal result:

- gate: `ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_PROVENANCE_GATE`;
- prospective preregistration: `2fc02a80c7d4db6f05813cbb571eb01cb4fb7c53`;
- canonical result commit: `558c02abd710812437f8616397d27cef7091af44`;
- terminal record commit: `a1ca2288e774895ab6f77dedc2065299df8f2b89`;
- historical classification: `ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_VERIFIED_SCOPED`;
- canonical result SHA256 recorded by the terminal authority: `471a8369cbfdb763ef5193984fe0f60d058d183e6f5bd5fb19e61bcb1e822504`.

The authoritative Phase-B source run `35405065903` remains nonterminal at fresh review time (`queued`, `conclusion=null`). Therefore this review does not classify Phase-B science and does not consume partial source scientific values.

## Preregistration / chronology

The preregistration commit precedes the result by exactly one commit in the ancestry relation (`558c02a...` is one commit ahead of `2fc02a8...`). The preregistration was therefore prospective with respect to the canonical result.

The frozen object is metadata/log provenance only for:

- source run `35405065903`, attempt 1;
- immutable source head `31fcdacffcc394e96b73917083281edb90d6753c`;
- source-lock job `105792998164`;
- first visible cancelled case jobs selected deterministically by ascending job id, capped at six;
- first visible successful case job by ascending job id as a positive control;
- no artifact ZIP bytes.

The PASS/FAIL/BLOCKED/INVALID taxonomy and interpretation ceiling are frozen before the result. Timeout cancellation is explicitly not a scientific FAIL.

## Source / realization identity

Fresh source-run metadata still binds run `35405065903` to head `31fcdacffcc394e96b73917083281edb90d6753c` and workflow `.github/workflows/iter504v-phase-b-science.yml`.

The workflow fetched directly at the immutable source head has Git blob SHA:

`a34f23eaab9b7fec0a1da2b0b684031a24cfa360`.

That exact workflow sets:

- `timeout-minutes: 360` for `cases-311`;
- `timeout-minutes: 360` for `cases-313`;
- `if: always()` on each case-job artifact upload.

This matches the frozen result's source/workflow identity.

## Independent log replay of the deterministic six-job sample

Fresh first-page job metadata reproduces the deterministic first six cancelled case jobs by ascending job id:

1. `105793032797` — Python 3.13 — `0to5|b0|p1|q1`;
2. `105793032807` — Python 3.13 — `0to5|b0|p0|q2`;
3. `105793032871` — Python 3.13 — `0to5|b0|p2|q1`;
4. `105793032873` — Python 3.13 — `0to5|b0|p0|q3`;
5. `105793032949` — Python 3.13 — `0to5|b0|p0|q0`;
6. `105793033008` — Python 3.11 — `0to5|b0|p2|q0`.

All six have job conclusion `cancelled`, frozen `Execute frozen quartile shard` step conclusion `cancelled`, and artifact-upload step conclusion `success`.

Independent direct log reads reproduce the frozen execution-step start/cancellation timestamps and runner marker `The operation was canceled.` for all six. The derived distances from the explicit 360-minute boundary agree with the canonical result:

- `105793032797`: `-2.911072 s`;
- `105793032807`: `+0.336255 s`;
- `105793032871`: `-3.506572 s`;
- `105793032873`: `-3.265842 s`;
- `105793032949`: `-2.109768 s`;
- `105793033008`: `-1.340261 s`.

Thus the full prospectively selected 6/6 sample lies within four seconds of the workflow's explicit six-hour timeout boundary, including both Python 3.13 and Python 3.11.

No selected log supplied evidence of a competing non-timeout cause. The observed timing plus the explicit runner cancellation marker and frozen job-level 360-minute limit satisfy the preregistered causal criterion.

## Positive control

The deterministically selected first successful case job, `105793032770` (Python 3.13, `0to5|b0|p0|q1`), remains `completed/success`; its frozen numerical step and upload step are both `success`.

Direct log timing reproduces the canonical successful-control duration:

`16379.561743 s = 272.992696 min`,

well below the 360-minute timeout boundary.

Source-lock job `105792998164` remains `completed/success`.

## Artifact-provenance cross-check

No artifact ZIP bytes were downloaded or opened.

Fresh Actions artifact metadata still contains the six post-cancellation artifacts named in the terminal record, with matching IDs/digests, including:

- `10578151776` / `sha256:568b1de7db028d7374b9f96df3b105901a987d4f69550c49d425057139dcd412`;
- `10578511467` / `sha256:d3afa37a445d2d0144eb75643ef7c4b438ede1edfe07c04b70345a56cb69e05d`;
- `10578476614` / `sha256:fdf7a7208432559187ba3b1551d6c6895623072e545f5868d062198647bd0d47`;
- `10577986131` / `sha256:b697adfb4384968a81dff57bae51eaefaaf38d008ed173aca266e31062bb281f`;
- `10578986244` / `sha256:14af8253cc3585da5a795bc3ebde1e9b0c682564ffdabbb6ff206f95369ce294`;
- `10578026205` / `sha256:73f9e0e0984209dcd2741d239e8c675d4d08ee79a34fa381dd2997c1706e9a2d`.

The current artifact-metadata inventory has grown beyond the earlier front snapshot (24 records were visible at this review read versus the earlier recorded 20). This does not alter the bounded timeout-causality result; it only reinforces that all preterminal inventory counts are time-local while the source run remains nonterminal.

## Counterexample-first assessment

Attempted refutations:

1. **Wrong timeout identity** — refuted: immutable workflow blob independently confirms 360 minutes in both Python matrices.
2. **Different cancellation cause in the frozen sample** — not found: all six selected logs show the same cancellation marker at the 360-minute boundary.
3. **Python-environment-specific failure** — refuted: selected sample includes both Python 3.13 and 3.11 with the same boundary pattern.
4. **Cancellation implies no artifact** — refuted in the opposite direction: each selected cancelled execution is followed by successful `if: always()` upload, consistent with the already-confirmed cancelled-job artifact provenance defect.
5. **All long-running jobs must cancel** — refuted by the positive control, which finishes at 272.992696 minutes and uploads normally.

No counterexample was found to the bounded causal claim.

## Interpretation ceiling / overclaim check

`CONFIRMED_SCOPED` means only that the prospectively selected six cancelled case jobs are bound to the frozen six-hour execution-timeout behavior and therefore are implementation/provenance-incomplete shards, not scientific verdicts.

It does not establish:

- any Phase-B PASS, INCONCLUSIVE, or scientific FAIL;
- that any physical/case value is wrong;
- all-domain or 1888-state closure;
- D7 closure;
- Candidate Gravity or Paper IV authority;
- any global quantum-gravity claim.

The source run remains nonterminal and no competing same-object scientific verdict is created by this review.

## Governance

- `RQIR Core v1.0 = FROZEN`;
- `BLOCKED != FAIL`;
- `INCONCLUSIVE != FAIL`;
- `TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`;
- artifact presence/digest != completed valid shard;
- finite/scoped result != family/global closure;
- D7 terminal selectors remain forbidden;
- Candidate Gravity remains inactive.

## Handoff

- `RESULT_REVIEWED = ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_PROVENANCE_GATE / canonical result 558c02abd710812437f8616397d27cef7091af44`
- `PREREG_CHECK = PASS`
- `OBJECT_IDENTITY_CHECK = PASS_SCOPED`
- `SOURCE/REALIZATION_CHECK = PASS_SCOPED`
- `PROVENANCE_CHECK = PASS_SCOPED` — exact run/head/workflow/sample/log and artifact-metadata bindings independently reproduced
- `SAME_REALIZATION_CHECK = PASS_SCOPED` — both Python environments show the same timeout-bound cancellation pattern
- `NUMERICAL/STATISTICAL_CHECK = NOT_CONSUMED` — no substantive Phase-B science used
- `COUNTEREXAMPLE_ATTEMPTS = wrong-timeout identity REFUTED; competing cancellation cause NOT FOUND in frozen sample; Python-specific cause REFUTED; cancelled=>no-artifact REFUTED; successful-before-timeout positive control PASS`
- `OVERCLAIM_CHECK = PASS_SCOPED`
- `VERDICT = CONFIRMED_SCOPED`
- `QUALIFICATIONS = causal authority is limited to the prospectively selected six-job sample; source run remains nonterminal; current artifact inventory is still evolving; cancellation is implementation/provenance incompleteness only`
- `UPDATED_STATE = timeout-causality closure independently confirmed; successful-complete terminal inventory must exclude timeout-cancelled shards even when upload produced artifact metadata`
- `NEXT_ADMISSIBLE_GATE = while run 35405065903 remains nonterminal, status/provenance/contract audit only. After natural terminalization, prospectively freeze exact terminal run/job/step/artifact inventory and digests before substantive payload access; require job.conclusion==success AND frozen Execute step success for every counted shard, plus all previously established shard-to-four-case, parent-child dyadic edge, unresolved-evidence classification, canonical projection-key, and canonical case-hash bindings in exactly one independent terminal Critic closure.`
