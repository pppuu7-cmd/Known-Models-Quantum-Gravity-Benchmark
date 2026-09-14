# Iter503V infrastructure contingency preregistration — causal-independent cache reuse

Date: 2026-09-15
Status: `FROZEN_BEFORE_CURRENT_OUTCOME`; dormant unless the activation condition below is met

## Current authority

- Active verifier workflow: `iter503v-endpoint-contract-verifier`.
- Authoritative run: `34898125306`.
- Frozen run head: `d1b40c8f96489a2166477c3863efa4905f4b8f27`.
- Frozen boxes: `{0,7,15}`.
- Frozen causals: `{0to5,1to4,2to3}`.
- Frozen endpoint checks: 288 total.

At the time of this preregistration the source-lock is successful and all three box lanes are still inside the frozen raw endpoint verifier. No lane result or aggregate result is available.

## Activation condition

This contingency may be activated **only** if run `34898125306` terminates without a valid complete aggregate verdict because of infrastructure/runtime failure such as hosted-runner timeout, cancellation, or missing artifacts.

If the authoritative run produces a valid complete aggregate `ITER503V_ENDPOINT_CONTRACT_CONFIRMED` or `ITER503V_ENDPOINT_CONTRACT_VIOLATION`, this contingency is not authorized as a replacement, reinterpretation, or second chance.

## Observation motivating the allowed optimization

The frozen implementation repeats expensive stages that are mathematically independent of the causal signature:

1. in the centered path, state construction, geometry/KAK, center source regression, and node Haar/logH data depend on `(box,R,direction,sign)` but not on `causal`;
2. in the high-precision point path, geometry and node/edge KAK depend on `(endpoint amplitude,R,direction,sign)` but not on `causal`;
3. the causal dependence enters when each edge selects the `p` or `m` Toller branch using `sigma_a sigma_b` and then through the resulting contraction.

Reusing the causal-independent stages changes evaluation order/caching only. It must not change the frozen mathematical object.

## Frozen allowed transformation

A contingency implementation may perform only the following semantic-preserving factorization.

### Centered path

For each frozen `(box,R)`:

- construct the Iter503 dual state exactly once;
- construct the source-faithful center state exactly once;
- evaluate the same construction/cycle/source-regression controls;
- compute the same centered node `logH` enclosure;
- for every `(edge,rho)`, compute both source branches with the same Iter503 AD/full-Toller routines;
- for each causal, select the appropriate already-computed branch using the unchanged `sigma_a sigma_b` rule;
- run the unchanged 243-channel contraction and envelope bound separately for each causal.

### High-precision point path

For each frozen `(box endpoint,R)`:

- construct the same Iter491/492 high-precision geometry once;
- compute the same node and edge KAK data once;
- for every `(edge,rho)`, compute both `Tp` and `Tm` from the same KAK data and keep the same normalization bookkeeping;
- for each causal, select the appropriate branch with the unchanged signature rule;
- run the unchanged source-faithful contraction separately for each causal and form the same raw `Y`.

No cache may be reused across different amplitude boxes, endpoints, or `R` values.

## Frozen invariants

The contingency must preserve exactly:

- `DIRECTION = [1,1,1,-1,-1,-1]`;
- `SIGN = +1`;
- boxes `[0,7,15]` and the exact same endpoints;
- causals `['0to5','1to4','2to3']`;
- `R = {6,8,10,12}`;
- `rho = {0.35,0.9,1.6,2.7}`;
- the established Iter491/492 high-precision point evaluator formulas and precision;
- the Iter503 centered enclosure formulas and `python-flint` precision;
- all 243 channels and contraction paths;
- all construction, KAK, cycle, source-additivity, finite-envelope, source-identity and regression controls;
- the exact endpoint containment predicate;
- 96 checks per box / 288 checks total;
- the aggregate classification labels and scope guards.

No tolerance, amplitude interval, representation parameter, channel, sign, causal class, precision, or endpoint may be changed.

## Mandatory equivalence guard before a contingency verdict is promotable

The optimized implementation must include an equivalence audit that verifies the cache factorization itself rather than assuming it.

At minimum, on a prospectively fixed microcontrol taken from the same frozen domain, compare legacy and cached evaluation for:

1. selected causal-independent KAK/geometry invariants;
2. both precomputed `p` and `m` branch matrices before causal selection;
3. causal-selected channel/envelope outputs;
4. high-precision raw `Y` values;
5. centered lower/upper `Y` enclosure bounds and the final containment boolean.

The cache audit passes only if all discrete branch selections/booleans agree exactly and all numerical differences satisfy the already-existing regression tolerances of the underlying paths. No new looser tolerance may be introduced for this audit.

If the cache-equivalence guard fails, classify the contingency `ITER503V_OPTIMIZATION_EQUIVALENCE_BLOCKER` and do not use it to infer endpoint-contract status.

## Permitted terminal meanings after activation

Only after the activation condition and equivalence guard both pass may the existing frozen Iter503V classifications be emitted:

- `ITER503V_ENDPOINT_CONTRACT_CONFIRMED`;
- `ITER503V_ENDPOINT_CONTRACT_VIOLATION`;
- `ITER503V_INVALID_OR_BLOCKED`.

Caching/runtime improvement is infrastructure work only and cannot turn a violation into a confirmation by changing the mathematical contract.

## Scope guards

- No dependent full 12-lane D7-S2 science campaign is authorized by this contingency preregistration.
- `D7-S2 = NOT_CLOSED` until the active/authorized endpoint contract is terminal and the subsequent science gate is separately preregistered and consumed.
- Scientific thresholds remain unchanged.
- Candidate Gravity remains inactive.
