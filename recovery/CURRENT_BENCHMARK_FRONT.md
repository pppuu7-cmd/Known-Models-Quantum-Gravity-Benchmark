# Current Benchmark Front
Updated: 2026-09-16

Fresh repository `main` and fresh Actions state always outrank this navigation document if they diverge.

## Latest terminal Research execution reviewed

`SOURCE_J1_K5_CHANNEL_COVERAGE_V5`

Prospective/frozen chain:

- parent Critic-confirmed V4 front `fd7905526514fbf5768041bd1aedc305b638f773`;
- V5 preregistration `d30274a74e206287b5dc3cf9cba02fa66e13c74b`;
- V5 implementation `abff2fceb51519ef47461f0060454f89ca798353`;
- workflow head `22fb468b79218176fe628266d311909cf87ddca5`;
- authoritative run `35041893961`, terminal `completed/success`.

Jobs:

- Python 3.11 exact lane `104623351833`, success;
- Python 3.13 exact lane `104623351638`, success;
- aggregate `104624134356`, success.

Artifacts:

- Python 3.11 `10424574808`, digest `sha256:847ce7d9f818069861adb98e8b05c62ca4a9f5ceefb3a3437ec5b8ce0b5c238f`;
- Python 3.13 `10425721638`, digest `sha256:c4cd1f7c94254344347d55cff51eac7f5d0464a7780ec5485c01fc5a00122b29`;
- aggregate `10425727109`, digest `sha256:a8775abfca4f5059eb55a72d1ed58a1ee4464fecc211e122ca15a51850666e7d`.

Research classification:

`CHANNEL_COVERAGE_NONZERO_SCOPED`.

Exact finite result on the frozen `j=1` fixed-tangent intertwiner basis:

- complete channel cube = `243 = 3^5` channels;
- nonzero channels = `224`;
- zero channels = `19`;
- channel `00000 = 11/24`;
- complete map SHA256 `2bceeb84db17ef0f01df4aa3350f8800d9e8e531ed68ed9ef10ca10cecfc9d0d`;
- both exact Python lanes agree on the complete map and all decision-critical fields.

## Latest independent Critical Review

Audit:

`recovery/CRITICAL_REVIEW_SOURCE_J1_K5_CHANNEL_COVERAGE_V5_2026-09-16.md`

Critic commit:

`d7c51b25c88c2f0600e5d7db13f25938822dd7ea`

Verdict:

`QUALIFIED`

The exact finite channel map and the `224/243` support census are independently confirmed. The qualification is contract-level rather than an implementation mismatch: V5 requires the positive control `channel 00000 = 11/24`, which already guarantees at least one nonzero channel. Therefore the frozen classification `CHANNEL_COVERAGE_NONZERO_SCOPED` is logically implied by that mandatory control once the other controls pass and does not prospectively discriminate a one-channel-support cube from a broadly supported cube.

The observed exact count `224/243` is valid scoped data. There is no prospectively frozen metric or threshold defining `broad nonzero support`, so no downstream thresholded breadth claim may be retrofitted to this result.

The zero-edge negative control is valid but weak: multilinearity makes the whole network vanish when an edge tensor is replaced by exact zero. It confirms that the edge participates but does not independently validate the `224/19` support structure. The full exact replay does validate that structure.

## Parent V4 authority

Fresh same-contract repaired V4 run `35033194283` remains independently `CONFIRMED_SCOPED` by Critic commit `1f61dafb51726e36cdc11e903621be8809d6dfa0`.

V4 established only survival of the highest `delta''` contact leading homogeneous tensor for frozen `j=1`, real nonzero `rho`, fixed full-K5 tangent witness, and channel `00000`. Historical run `35023270636` remains immutable `INVALID_IMPLEMENTATION` history.

V5 broadens only the finite channel basis at the same tangent realization; it does not broaden tangent, spin, collision-stratum, or distribution-product scope.

## Scope / interpretation ceiling

V5 does **not** establish:

- all tangents or all spins;
- a basis-independent support-density theorem;
- existence/nonexistence of the joint product of the ten contact distributions;
- complete K5 vertex convergence/divergence;
- joint source Feynman-regulator success/failure;
- model/family failure;
- D7 closure;
- any terminal selector;
- Candidate Gravity activation.

Finite channel census != universal theorem and scoped child result != family closure.

## Provenance hardening note

The run is reproducible at workflow head `22fb468...`, and parent-to-head comparison changed only the V5 preregistration, V5 implementation, and V5 workflow. V5 imports the exact V4 angular kernel and tangent/input realization without modifying them. Future descendants should additionally emit exact blob SHAs for the imported contraction-kernel file and tangent/input file in their artifacts rather than relying only on ancestry.

## Independent registered workflows

Do not consume partial substantive values:

- Iter504 run `34907349374`, head `56362459a826e3e376c529446678f2fbcaa269ae`: freshly checked `queued / conclusion=null`;
- Iter461 run `34748503239`, branch `research/iter461-k5-collision-partitions`, head `05c7f87c8519349057332bf90021f1128e1eefc3`: freshly checked `queued / conclusion=null`.

## Next admissible work

Keep two questions separate.

1. For **channel-support breadth**, prospectively freeze a new gate with the support statistic, basis dependence, any symmetry/orbit quotient, and exact PASS/FAIL threshold before using `224/243` as a deciding criterion. Do not retrofit a threshold after seeing the census.
2. For **joint contact-distribution transversality / wavefront admissibility**, prospectively freeze the actual joint distribution-product object, covectors/wavefront criterion, same-realization dependencies, positive/negative controls, and distinct PASS/FAIL/BLOCKED semantics. The V5 channel map may be an input, but `224/243` alone is not a product-existence or failure theorem.

Any change of tangent realization, intertwiner basis, source authority, channel definition, or decision threshold requires a new prospectively frozen gate.

## Governance lock

- `RQIR Core v1.0 = FROZEN`.
- `BLOCKED != FAIL`.
- finite certificate != universal theorem.
- missing object != zero residual.
- scoped child result != family closure.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 labels and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden until required subgates close.
- Candidate Gravity remains inactive.
- Green CI is provenance, not science.
- No authority exists for `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.
