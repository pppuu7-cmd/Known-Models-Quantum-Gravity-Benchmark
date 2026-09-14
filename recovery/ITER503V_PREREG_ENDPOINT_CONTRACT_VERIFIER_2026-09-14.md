# Iter503V — prospective endpoint-contract verifier

**Frozen while authoritative Iter503 run `34895563822` is still non-terminal.** This verifier is outcome-blind with respect to Iter503 production results. It does not alter Iter503's frozen scientific/method predicate; it independently audits whether the implementation satisfies the preregistered endpoint-containment wording strongly enough to permit promotion of a green Iter503 aggregate.

## Trigger
Iter503 preregistration requires that the centered enclosure contain both endpoint point evaluations for every frozen test interval and observable tested by the enabling gate. The current Iter503 implementation explicitly checks endpoint containment after forming early/late slope intervals. Because the implementation also constructs four per-R max-envelope log-observables before the slope map, this verifier freezes a stronger raw-observable audit before Iter503 outcome is known.

## Authority under review
- Iter503 preregistration commit: `01ec9775febc726dc8cfbb0cab658573d0ed459d`.
- Iter503 implementation head under review: `d598f8c20fb6611fefa426bced6c0d4be8260baf`.
- authoritative Iter503 run: `34895563822`.
- frozen method: single-common-amplitude centered/mean-value enclosure through the source-faithful compact-sandwich/factorized KAK and full 243-channel contraction.

## Frozen verifier object
For every tuple

`causal × box × endpoint × R × rho`

with:
- causal in `{0to5, 1to4, 2to3}`;
- box in `{0, 7, 15}`;
- endpoint in `{lo, hi}` of the original Iter501 parent box;
- `R in {6,8,10,12}`;
- `rho in {0.35,0.9,1.6,2.7}`;

independently compute the high-precision source-faithful point value

`Y_point(R,rho,a) = log H(R,a) + log max_channel |C_channel(R,rho,a)|`

using the established Iter491/492 point geometry/KAK/Toller/contraction path, and compare it with the centered interval `Y_centered(R,rho,[a_lo,a_hi])` produced from the Iter503 common-amplitude interval-AD path.

Frozen total: `3 × 3 × 2 × 4 × 4 = 288` raw endpoint-containment checks.

## Independence rule
The point side must not be obtained by evaluating the Iter503 interval-AD enclosure at a singleton. It must use the pre-existing high-precision point geometry/KAK/Toller/243-channel contraction machinery. Reusing frozen source constants, channel ordering and causal sign conventions is required for object identity and is not considered loss of independence.

## Positive controls
1. All inherited point-path controls pass: group determinants, KAK reconstruction/unitarity/determinant, cycle/source-object identity, positivity/finite envelope, Haar bookkeeping and source additivity as applicable.
2. Iter503 centered-path construction/cycle/source-additivity/finite-envelope and midpoint source-regression controls pass for the same frozen tuple family.
3. All 288 high-precision raw endpoint values are contained in their corresponding centered per-R `Y` intervals.
4. The high-precision point values are finite and the max-channel envelope is positive.

## Negative/control guards
- no amplitude subdivision beyond the already frozen parent boxes;
- no threshold relaxation;
- no domain-point deletion;
- no channel selection fixed post hoc;
- max-channel switching is allowed and must be handled by direct max-envelope logic;
- no replacement of source KAK/Toller objects;
- no use of a green Iter503 aggregate as an input to this verifier's predicate.

## Verdicts
`ITER503V_ENDPOINT_CONTRACT_CONFIRMED` iff all 288 raw endpoint-containment checks and all positive controls pass.

`ITER503V_ENDPOINT_CONTRACT_VIOLATION` iff any raw endpoint point value lies outside the corresponding centered per-R interval while object/control identity remains valid.

`ITER503V_INVALID_OR_BLOCKED` iff the independent point object cannot be reconstructed, inherited controls fail, provenance/object identity is ambiguous, or the verifier implementation itself cannot be validated.

## Promotion rule
- A green Iter503 aggregate plus `ITER503V_ENDPOINT_CONTRACT_CONFIRMED` permits the original Iter503 PASS to be promoted subject to the rest of its frozen predicate.
- A green Iter503 aggregate plus `ITER503V_ENDPOINT_CONTRACT_VIOLATION` must **not** be promoted as a valid Iter503 PASS; the implementation requires a new prospectively frozen repair/audit gate.
- A blocked verifier does not convert Iter503 into scientific FAIL; it caps promotion until the contract ambiguity is resolved.

## Scope ceiling
This verifier establishes only implementation/preregistration contract fidelity for the Iter503 enabling subset. It proves no DECAY/NONDECAY result, no positive-Haar-measure statement, no spectral-integral convergence, no multidimensional angular-neighborhood theorem, no D7 closure, no terminal selector label, and no Candidate Gravity activation.
