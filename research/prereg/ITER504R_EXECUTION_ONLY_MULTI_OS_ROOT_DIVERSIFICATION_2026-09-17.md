# ITER504R execution-only multi-OS root diversification

Date: 2026-09-17
Status: PROSPECTIVELY FROZEN EXECUTION-ONLY ACCELERATION

## Trigger

Iter504R run `35154724661` has passed its frozen source-lock. One Ubuntu root-model job is running while the other five root-model jobs are queued. No Iter504R substantive root artifact/value has been consumed.

The three root boxes are scientifically independent until the frozen assembler. The same pinned `python-flint==0.9.0`, 384-bit Arb/Acb arithmetic and identical source code can therefore be executed on different hosted operating-system runner pools to reduce orchestration wait without changing the scientific gate.

## Frozen diversified layout

Cohort A (`python 3.11`):

- root 13 -> `windows-latest`;
- root 14 -> `ubuntu-latest`;
- root 15 -> `macos-latest`.

Cohort B (`python 3.13`):

- root 13 -> `macos-latest`;
- root 14 -> `windows-latest`;
- root 15 -> `ubuntu-latest`.

Each root job must execute the exact Iter504R implementation commit `f846820bae39963a48272deccb2e4a539100fce1`. Each cohort is assembled by the exact assembler commit `904cae881f86f213973110fc8f18a4c02d67cc3d`, and the two assembled cohorts are compared by aggregate commit `e0367d4e0b91afc668e733c2027fd39bf27637fc`.

## Scientific immutability

No change is permitted to:

- Iter504R preregistration `147d68f26ed3a14ce3cd1fd77fcd96d5fb329ec8`;
- boxes 13,14,15 or exact rational endpoints;
- causal/block/path/direction/sign;
- rho/R grids;
- root-affine mean-value construction;
- one derivative model per root;
- all 243 channels retained;
- depth 10 exact midpoint subdivision;
- robust floor `+1.0`;
- drift tolerance `0.05`;
- exact-cover contract;
- PASS/INCONCLUSIVE/INVALID semantics.

If `python-flint==0.9.0` is unavailable on a runner platform, that job is an infrastructure failure only. Do not substitute another numerical library or version.

## Equivalence / acceptance

The diversified execution is acceptable only if both assembled cohorts satisfy all frozen source/cover/model/channel controls and the final aggregate accepts their scientific outputs. Any cross-platform discrepancy is treated as an implementation/execution issue, not a scientific result.
