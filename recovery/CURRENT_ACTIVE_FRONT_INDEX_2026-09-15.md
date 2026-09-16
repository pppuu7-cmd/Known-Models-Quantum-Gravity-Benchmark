# Current active front index — 2026-09-16

This is a navigation index over immutable prereg/result/recovery records. Fresh repository `main` and fresh Actions state always outrank this index if they diverge.

## Frozen global state

- Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`.
- KMQGB remains downstream of pinned DSIR authority; imports must preserve exact provenance.
- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 labels and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden until required subgates close.
- Candidate Gravity remains inactive.
- `BLOCKED/INVALID != scientific FAIL`.

## Latest terminal Research execution

`SOURCE_J1_K5_CHANNEL_COVERAGE_V5`

Frozen chain:

- parent V4 Critic-confirmed front `fd7905526514fbf5768041bd1aedc305b638f773`;
- V5 prereg `d30274a74e206287b5dc3cf9cba02fa66e13c74b`;
- implementation `abff2fceb51519ef47461f0060454f89ca798353`;
- workflow head `22fb468b79218176fe628266d311909cf87ddca5`.

Authoritative run `35041893961` is terminal `completed/success`.

Jobs:

- Python 3.11 `104623351833` success;
- Python 3.13 `104623351638` success;
- aggregate `104624134356` success.

Artifacts:

- Python 3.11 `10424574808`, digest `sha256:847ce7d9f818069861adb98e8b05c62ca4a9f5ceefb3a3437ec5b8ce0b5c238f`;
- Python 3.13 `10425721638`, digest `sha256:c4cd1f7c94254344347d55cff51eac7f5d0464a7780ec5485c01fc5a00122b29`;
- aggregate `10425727109`, digest `sha256:a8775abfca4f5059eb55a72d1ed58a1ee4464fecc211e122ca15a51850666e7d`.

Research classification:

`CHANNEL_COVERAGE_NONZERO_SCOPED`

Exact map/census:

- total `243` channels;
- nonzero `224`;
- zero `19`;
- `00000 = 11/24`;
- map SHA256 `2bceeb84db17ef0f01df4aa3350f8800d9e8e531ed68ed9ef10ca10cecfc9d0d`;
- complete map agrees across both pinned Python lanes.

## Latest independent Critical Review

- audit `recovery/CRITICAL_REVIEW_SOURCE_J1_K5_CHANNEL_COVERAGE_V5_2026-09-16.md`;
- Critic commit `d7c51b25c88c2f0600e5d7db13f25938822dd7ea`;
- verdict `QUALIFIED`.

Confirmed scoped facts:

- the frozen three-channel-per-vertex basis gives a complete `3^5=243` channel cube;
- exact enumeration gives `224/243` nonzero and `19/243` zero;
- `00000=11/24` and the complete channel map are independently reproduced;
- no floating-point support decision is used.

Qualification:

The frozen PASS classification is not a prospectively discriminating test of support breadth. Its mandatory positive control already requires nonzero `00000=11/24`, so any otherwise-valid map with only that one nonzero channel would still receive `CHANNEL_COVERAGE_NONZERO_SCOPED`. There is no frozen definition or threshold for `broad nonzero support`. The observed `224/243` census is valid data, but no breadth threshold may be retrofitted after observing it.

The zero-edge negative is structurally valid but weak because multilinearity forces all channels to vanish when an edge tensor is exact zero. The exact replay, rather than that fixture alone, validates the support census.

## Parent V4 state

Fresh same-contract repaired V4 run `35033194283` remains `CONFIRMED_SCOPED` by independent Critic `1f61dafb51726e36cdc11e903621be8809d6dfa0`.

Historical V4 run `35023270636` remains immutable `INVALID_IMPLEMENTATION` history. V5 reuses the exact V4 angular contraction kernel and same tangent realization; it does not broaden tangent, spin, distribution-product, or family scope.

## Scope lock

V5 is only a finite fixed-tangent `j=1` channel census in the frozen intertwiner basis. It does not establish:

- all tangents, spins, or collision strata;
- basis-independent support density;
- joint contact-distribution product existence/nonexistence;
- complete K5 convergence/divergence;
- model/family failure;
- D7 closure;
- terminal selectors;
- Candidate Gravity activation.

## Independent registered workflows

Do not consume partial substantive values:

- Iter504 run `34907349374`, head `56362459a826e3e376c529446678f2fbcaa269ae`: freshly checked `queued / conclusion=null`;
- Iter461 run `34748503239`, branch `research/iter461-k5-collision-partitions`, head `05c7f87c8519349057332bf90021f1128e1eefc3`: freshly checked `queued / conclusion=null`.

## Next admissible frontier

Choose one prospectively frozen question before further inference.

1. **Channel-support breadth:** freeze the statistic, basis dependence, symmetry/orbit quotient if any, and exact PASS/FAIL threshold before using the observed `224/243` as a decision variable.
2. **Joint contact-distribution transversality / wavefront admissibility:** freeze the joint object, covectors/wavefront criterion, same-realization authorities, controls, and distinct PASS/FAIL/BLOCKED semantics. The V5 map may be input data but is not by itself a distribution-product theorem.

Future descendants should also emit exact blob SHAs for imported V4 contraction-kernel and tangent/input files. Any change of tangent realization, intertwiner basis, source authority, channel definition, or threshold requires a new prospectively frozen gate.

## Restoration procedure

1. Read fresh `main` and fresh Actions first.
2. Read `recovery/CURRENT_BENCHMARK_FRONT.md`, this index, latest terminal Research execution, latest Critic, and any newer prereg/workflow.
3. Recheck Iter504 and Iter461 without consuming partial substantive values.
4. Preserve historical invalid/blocked results and apply Critic qualifications only to their scoped descendants.
5. Keep all governance locks and claim ceilings unchanged unless separately frozen authority closes them.
