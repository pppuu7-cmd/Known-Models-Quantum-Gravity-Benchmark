# ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENCE_PROVENANCE_GATE — terminal record

Date: 2026-09-19

## Authority

- prospective preregistration commit: `5e67991ca4c09a9098ad3ae3a1d91601d2bbc7c7`
- exact source run: `35405065903`
- attempt: `1`
- immutable head: `31fcdacffcc394e96b73917083281edb90d6753c`
- raw result commit: `c9dacc08c9152900bfcb393d28aaa8f245c03956`
- raw result SHA256: `4b9c3727630f7631f5ae8d5c5f61b6f4ab842caac933c89d8ed10ae9b299e8e1`
- canonical result commit: `50bac01a4068d21f5a3e9d4d497e5b618424c0e7`
- canonical result SHA256: `4fb7f7709ccc0ed62af5b402d9e04cfac356626fc5681d378255e6f3cc6ff10b`

## RESULT

`ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENT_SCOPED`

The exact workflow-run endpoint remains nonterminal: `status=queued`, `conclusion=null`.

The complete exact-run latest-attempt jobs collection was read through all four pages (`per_page=100`, pages 1..4). GitHub reports `total_count=385`, matching the frozen authority inventory: one source-lock plus 384 matrix jobs. Source-lock job `105792998164` remains `completed/success`.

Nonterminal exact-run jobs remain present. Outcome-independent witnesses from separate pagination pages include:

- `105793035543` — `queued`, `cases (3.11, 0to5, b3, p0, q2)`;
- `105793039803` — `queued`, `cases (3.11, 1to4, b2, p1, q0)`;
- `105793044215` — `queued`, `cases (3.11, 2to3, b1, p1, q1)`.

Therefore the frozen coherent state holds: **run nonterminal AND exact job inventory contains nonterminal jobs**.

## Controls

Positive controls pass:

- exact run/head/attempt matched;
- source-lock remained terminal success;
- GitHub full collection reports the frozen 385-job cardinality;
- all four pagination pages were obtained;
- at least one exact-run nonterminal job is independently witnessed.

Negative controls retained:

- cancelled/timeout jobs count as terminal for this terminality relation but are not successful-complete science shards;
- artifact presence/digest was not used as execution-success evidence;
- no check-suite surrogate was introduced;
- artifact ZIP bytes were not opened;
- no scientific case/leaf/slope/drift/certification/assembly/aggregate/counterexample value was consumed.

Fresh artifact metadata first page contained 29 exact-run/head-bound, non-expired records with SHA256 digests. This is recovery metadata only and is not part of the gate decision.

## CLASSIFICATION

`ITER504V_PHASE_B_RUN_JOB_TERMINALITY_COHERENT_SCOPED`

This is metadata/provenance coherence only. It does not classify Phase-B science and does not rehabilitate the already verified authority incompleteness from cancelled/timeout required shards.

## NEW FACT

The apparently stale-looking workflow-run endpoint (`queued`) is not presently contradicted by the complete job inventory: substantial portions of the 385-job inventory remain genuinely nonterminal. Therefore no run/job terminality incoherence is established at this read.

## CLAIM CEILING

No Phase-B scientific PASS/INCONCLUSIVE/INVALID result follows. No rerun is authorized. Existing assembler/aggregate/cancelled-artifact/timeout/assembly-reachability verifier obligations remain in force. `BLOCKED != FAIL`; `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; `TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`; green status/artifact metadata != science.

No all-domain/family/D7/Candidate-Gravity/Paper-IV/global quantum-gravity claim is authorized.
