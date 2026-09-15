# SOURCE_J1_K5_P1_S4_FOREST_ORBIT_REDUCTION — prospective freeze

Date: 2026-09-15
Status: PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION_OR_RESULT

## HYPOTHESIS

The stable P1 auxiliary scalar Gaussian realization has an exact vertex-stabilizer symmetry `S4` fixing the gauge/reference vertex. The exact 236-member proper-forest sum can therefore be evaluated orbitwise without changing the signed forest formula, reducing future expensive numerical work.

## OBJECT

Use zero-based vertices `V={0,1,2,3,4}` corresponding to source vertices `{1,2,3,4,5}` with vertex `0` gauge-fixed.

Use lexicographic K5 edge order

`(01,02,03,04,12,13,14,23,24,34)`

and frozen P1 regulator exponents

`(1,1,1,1,2,2,2,2,2,2)`.

Thus every edge incident to vertex `0` has exponent 1 and every edge among `{1,2,3,4}` has exponent 2.

Let `G_P1` be all 24 vertex permutations fixing vertex `0` and permuting `{1,2,3,4}` arbitrarily.

Use exactly the 236 proper-only laminar forests and scalar orders `{2:2,3:7,4:15}` from the terminal scalar order/operator authorities.

## DEPENDENCY

- scalar forest order repair terminal commit `16b6340a2bd78e350258636b226ac69adb8a40d2`;
- scalar forest operator terminal commit `eccdbcce242c561cdf6ae831f48179a7ef3dfdd0`;
- operator spec digest `sha256:c3e0ca0c5a5357887db79b7b0a1c5a0a1042c450ca13f7e2599c7e3801ef8a9c`;
- P1 exponent authority is the stable Gaussian parent implementation lineage, whose frozen vector is exactly `(1,1,1,1,2,2,2,2,2,2)`.

No P3 divergence premise is consumed.

## FROZEN EXACT CHECKS

1. Reconstruct K5 edges and P1 exponent map algorithmically.
2. Enumerate all 24 permutations fixing vertex 0 and prove they preserve every P1 edge exponent.
3. Re-enumerate all 236 proper-only laminar forests independently.
4. Compute the exact `G_P1` orbit partition of the 236 forests.
5. Verify orbit sizes sum to 236 and forest cardinality/sign `(-1)^|F|` is constant on every orbit.
6. Verify every scalar order and the exact barycentric forest operator transforms covariantly under `G_P1`.
7. For an exact `G_P1`-invariant integer fixture `A(F)` derived only from subset sizes and whether subsets contain vertex 0, compare the full 236-forest signed sum with the orbit-weighted representative sum exactly.
8. Adversarial control: a deliberately non-invariant fixture depending on a distinguished nonzero vertex must not be safely reducible by representative weighting.
9. Report exact structural jet-box workload
   `J(F)=product_{S in F}(r(S)+1)`
   for both the full forest family and one representative per P1 orbit. This is an implementation-complexity count, not a scientific observable.

## PASS

`P1_S4_FOREST_ORBIT_REDUCTION_CONFIRMED_SCOPED` iff all exact symmetry/covariance/orbit/signed-sum controls pass and both independent Python lanes return the same orbit census, representative digest, and workload counts.

## FAIL

`P1_S4_FOREST_ORBIT_REDUCTION_CONTRADICTION` iff exact implementation is valid but the frozen P1 exponent map or operator fails the stated S4 invariance.

## BLOCKED / INVALID

`P1_S4_FOREST_ORBIT_REDUCTION_BLOCKED` for an identified exact-enumeration resource failure.

`INVALID_IMPLEMENTATION` for wrong edge order, wrong P1 exponent map, wrong group, wrong forest family, sign-changing orbit, failed invariant-fixture identity, an adversarial non-invariant fixture that incorrectly passes, or floating-point group/orbit decisions.

## INTERPRETATION CEILING

PASS authorizes P1 orbit reduction only as a computational optimization for a later prospectively frozen numerical forest-subtraction gate. It is not evidence for convergence/divergence, Eq. (4), model/family failure, D7 closure, a terminal selector, or Candidate Gravity.