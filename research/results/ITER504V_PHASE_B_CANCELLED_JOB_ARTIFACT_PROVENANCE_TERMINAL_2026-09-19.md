# ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_GATE — terminal record

Date: 2026-09-19
Lane: KMQGB Research / Closure

## Preregistration

Prospective freeze commit: `a0e28e3a96e109ee9ed440a267ee1407cddf2d55`.

Exact object: metadata-only audit of authoritative Phase-B source run `35405065903`, attempt 1, immutable head `31fcdacffcc394e96b73917083281edb90d6753c`. Artifact ZIP bytes and substantive science payload were forbidden and were not opened.

## Result

`ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_DEFECT_VERIFIED_SCOPED`

The source run remained nonterminal (`queued / conclusion=null`) at the post-freeze observation. Source-lock job `105792998164` remained `completed/success`.

The frozen first-page snapshot contained 30 jobs:

- 8 `completed/success` (including source-lock);
- 12 `completed/cancelled`;
- 8 `in_progress`;
- 2 `queued`.

Fresh run artifact metadata exposed 20 records, all bound to exact run `35405065903` / head `31fcdacffcc394e96b73917083281edb90d6753c`, non-expired and SHA256-digested.

## Positive controls

PASS. A normal visible successful shard exists with job conclusion `success`, frozen execution step conclusion `success`, upload-artifact conclusion `success`, and matching artifact metadata. Source-lock remains successful. Exact run/head/digest metadata binding is present for all inspected artifact records.

## Adversarial provenance result

The cancelled-job artifact chain was reproduced 12 times on the inspected first page. In each verified chain:

1. the case job conclusion is `cancelled`;
2. `Execute frozen quartile shard` conclusion is `cancelled`;
3. `Run actions/upload-artifact@v4` conclusion is `success`;
4. a deterministically matching artifact metadata record exists for the same `(python, causal, block, path, quartile)` identity;
5. that artifact is non-expired, SHA256-digested and bound to the same exact source run/head.

Representative exact chains:

- job `105793032797`, `cases (3.13, 0to5, b0, p1, q1)` -> artifact `10578151776`, `iter504v-phaseb-3.13-0to5-b0-p1-q1`, digest `sha256:568b1de7db028d7374b9f96df3b105901a987d4f69550c49d425057139dcd412`;
- job `105793033008`, `cases (3.11, 0to5, b0, p2, q0)` -> artifact `10578026205`, `iter504v-phaseb-3.11-0to5-b0-p2-q0`, digest `sha256:73f9e0e0984209dcd2741d239e8c675d4d08ee79a34fa381dd2997c1706e9a2d`;
- job `105793033047`, `cases (3.11, 0to5, b0, p1, q1)` -> artifact `10578656499`, `iter504v-phaseb-3.11-0to5-b0-p1-q1`, digest `sha256:eb9010aa5b5a0b820f4e6216d97bbb32768e5d0fc23e22881b4c5addff764b49`.

All 12 exact chains are frozen in `research/results/ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_RESULT_2026-09-19.json`.

Chain-list SHA256: `d0d7c9840e76300feeffe40eb09650eaf0a00f4ddd117c77ccfff5832a6b4dee`.

Canonical decision projection:

`ITER504V_PHASE_B_CANCELLED_JOB_ARTIFACT_PROVENANCE_DEFECT_VERIFIED_SCOPED|run=35405065903|head=31fcdacffcc394e96b73917083281edb90d6753c|cancelled_chains=12|artifact_metadata=20|science_consumed=false`

Canonical decision SHA256: `6e2de425bc3b8cc83c75641c160e352061c2479b2f0564ce3b5b2eb3882f9e2f`.

## New authority obligation

Artifact existence, artifact ID and GitHub digest are not sufficient evidence that a Phase-B shard completed validly. Before any shard artifact can enter terminal scientific authority, the independent terminal Critic must bind that artifact to:

- exact frozen shard identity;
- `job.conclusion == success`;
- frozen `Execute frozen quartile shard` step conclusion `success`;
- successful upload;
- the already-required `shard.json` / four-record physical-content identity and content hashes.

An artifact emitted after a cancelled execution step must not count toward the required 192 complete shards per environment, even if upload succeeded and a valid GitHub digest exists.

## Classification ceiling

This is an execution-provenance/authority-path defect for exact run `35405065903` only. It does not classify Phase-B science while the run is nonterminal, does not assert any case value is scientifically wrong, and does not convert cancellation into a physics FAIL. `INVALID_IMPLEMENTATION != SCIENTIFIC_FAIL`; `BLOCKED != FAIL`; partial artifact != terminal authority.

No D7, Candidate Gravity, Paper IV, family-level or global quantum-gravity claim is advanced.
