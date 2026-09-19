# ITER504V Phase-B case-job timeout causality provenance — terminal record

Date: 2026-09-19
Gate: `ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_PROVENANCE_GATE`
Prospective preregistration: `2fc02a80c7d4db6f05813cbb571eb01cb4fb7c53`
Canonical result commit: `558c02abd710812437f8616397d27cef7091af44`
Canonical result SHA256: `471a8369cbfdb763ef5193984fe0f60d058d183e6f5bd5fb19e61bcb1e822504`

## Classification

`ITER504V_PHASE_B_CASE_JOB_TIMEOUT_CAUSALITY_VERIFIED_SCOPED`

This is a metadata/log provenance result only. It is not a Phase-B scientific classification and it consumed no case/leaf/slope/drift/certification/assembly/aggregate/counterexample numerical payload.

## Exact authority object

- Phase-B prereg: `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`
- execution authority: `caf67585a9fad990dd90948df51839e6ed7cf891`
- immutable source launch/head: `31fcdacffcc394e96b73917083281edb90d6753c`
- source run: `35405065903`, attempt 1
- workflow blob: `a34f23eaab9b7fec0a1da2b0b684031a24cfa360`
- source-lock job `105792998164`: `completed/success`

The frozen source workflow itself sets `timeout-minutes: 360` on both `cases-311` and `cases-313` matrix jobs. Artifact upload is explicitly guarded by `if: always()`.

## Deterministic cancelled-job sample

The first six visible cancelled case jobs by ascending job id were frozen before log inspection. All six hit the same approximately six-hour numerical-execution boundary and emitted runner marker `The operation was canceled.` while the frozen `Execute frozen quartile shard` step was cancelled:

| job | Python | shard | execution elapsed | distance from 360 min | upload |
|---|---|---|---:|---:|---|
| `105793032797` | 3.13 | `0to5|b0|p1|q1` | `21597.088928 s` | `-2.911072 s` | success |
| `105793032807` | 3.13 | `0to5|b0|p0|q2` | `21600.336255 s` | `+0.336255 s` | success |
| `105793032871` | 3.13 | `0to5|b0|p2|q1` | `21596.493428 s` | `-3.506572 s` | success |
| `105793032873` | 3.13 | `0to5|b0|p0|q3` | `21596.734158 s` | `-3.265842 s` | success |
| `105793032949` | 3.13 | `0to5|b0|p0|q0` | `21597.890232 s` | `-2.109768 s` | success |
| `105793033008` | 3.11 | `0to5|b0|p2|q0` | `21598.659739 s` | `-1.340261 s` | success |

Thus all 6/6 selected cancellations lie within four seconds of the workflow's explicit 360-minute timeout boundary, and the pattern occurs in both Python environments.

Representative post-cancellation artifacts recorded directly by the same job logs:

- job `105793032797` -> artifact `10578151776`, ZIP SHA256 `568b1de7db028d7374b9f96df3b105901a987d4f69550c49d425057139dcd412`;
- job `105793032807` -> artifact `10578511467`, ZIP SHA256 `d3afa37a445d2d0144eb75643ef7c4b438ede1edfe07c04b70345a56cb69e05d`;
- job `105793032871` -> artifact `10578476614`, ZIP SHA256 `fdf7a7208432559187ba3b1551d6c6895623072e545f5868d062198647bd0d47`;
- job `105793032873` -> artifact `10577986131`, ZIP SHA256 `b697adfb4384968a81dff57bae51eaefaaf38d008ed173aca266e31062bb281f`;
- job `105793032949` -> artifact `10578986244`, ZIP SHA256 `14af8253cc3585da5a795bc3ebde1e9b0c682564ffdabbb6ff206f95369ce294`;
- job `105793033008` -> artifact `10578026205`, ZIP SHA256 `73f9e0e0984209dcd2741d239e8c675d4d08ee79a34fa381dd2997c1706e9a2d`.

No artifact ZIP was downloaded or opened for this gate.

## Positive control

Job `105793032770`, Python 3.13 shard `0to5|b0|p0|q1`, completed the frozen numerical step successfully in `16379.561743 s = 272.992696 min`, well before the 360-minute boundary; job and artifact upload both concluded success. Source-lock also remained success.

## New fact

The cancelled Phase-B shards are not unexplained scientific or numerical verdicts. For the prospectively selected sample, cancellation is caused by the execution topology hitting the workflow's explicit six-hour case-job timeout. Because upload runs under `if: always()`, timeout termination can leave a small, successfully uploaded artifact afterward.

Therefore future terminal authority must bind every shard not merely to artifact identity/digest and successful job/step conclusions, but also treat timeout-cancelled shards as incomplete implementation/provenance objects. Their artifact bytes cannot substitute for a completed four-record shard.

## Claim ceiling

`TIMEOUT_CANCELLATION != SCIENTIFIC_FAIL`.

This gate does not classify source run `35405065903`, does not assert any physical record is wrong, does not authorize a producer rerun while the source run is nonterminal, and does not advance family/D7/Candidate Gravity/Paper IV/global quantum-gravity claims.
