# KMQGB Critical Review — causal/co-causal conjugation-compatible collision ambiguity

Date: 2026-09-15
Review lane: independent KMQGB Critical Review / Verification
Verdict: `CONFIRMED_SCOPED`

## RESULT_REVIEWED

Latest substantive terminal Research output reviewed exactly once:

- frozen gate: `research/SOURCE_J1_K5_CAUSAL_COCAUSAL_CONJUGATION_AMBIGUITY_PREREG_2026-09-15.md`;
- preregistration commit: `cb8b6e5a6824ef11cb39b00fd0dae15d1e753b53`;
- exact implementation: `code/source_j1_k5_causal_cocausal_conjugation_ambiguity_certificate.py`;
- implementation commit: `f322cbb7cc3cd772f2587ac3389c412014a8c1e2`;
- workflow head: `6e9a5e8b0acb964c496f82d43a76fe9765954b60`;
- authoritative workflow: `source-j1-k5-causal-cocausal-conjugation-ambiguity`;
- run: `34917064485`, terminal `success`;
- source-lock job: `104216894150`, success;
- exact-certificate job: `104216924109`, success;
- artifact: `10376117713`, `source-j1-k5-causal-cocausal-conjugation-ambiguity`;
- artifact digest: `sha256:47e5d973187494e29cd137ebf09b1081fbce65b5d34258b01bd0800e768c344b`.

Frozen Research classification under review:

`SOURCE_J1_K5_CAUSAL_COCAUSAL_CONJUGATION_STILL_LEAVES_COLLISION_AMBIGUITY_SCOPED`.

The reviewed claim is only the exact coefficient-level counterexample: EPRL independent-sign zero-sum + K5 vertex-permutation covariance + the frozen same-scaling window + global edge-sign reversal/complex-conjugation covariance do not uniquely fix the scoped collision-supported coefficient family. It is not a theorem that the complete published causal/co-causal vertex relation leaves the same ambiguity after all representation, rho, magnetic and boundary-index transformations.

Iter504 run `34907349374` remains non-terminal (`queued`) and Iter461 run `34748503239` remains non-terminal (`queued`) at this review. No partial values from either run were consumed.

## PREREG_CHECK

`CONFIRMED`.

Chronology is prospective and mechanically source-locked:

1. preregistration commit `cb8b6e5a6824ef11cb39b00fd0dae15d1e753b53` at 2026-09-15T01:22:47Z;
2. implementation commit `f322cbb7cc3cd772f2587ac3389c412014a8c1e2` at 2026-09-15T01:23:10Z, whose parent is the frozen prereg commit;
3. workflow commit `6e9a5e8b0acb964c496f82d43a76fe9765954b60` at 2026-09-15T01:23:26Z.

The workflow source-lock explicitly checks that the prereg path's latest commit is the frozen prereg commit and checks the frozen PASS label, conjugation identity and `D7-S2 = NOT_CLOSED` governance string.

No post-hoc threshold, domain, sign-sector selection, confidence rule or numerical tolerance is introduced. The witness coefficients `+i/-i/0`, the sector definitions, all target cardinalities, the scaling ledger and the claim ceiling are frozen before implementation.

## OBJECT_IDENTITY_CHECK

`CONFIRMED_SCOPED`.

The object is the ten-edge K5 sign cube `kappa in {+/-1}^10` with

- `C_+ = {kappa_ab = sigma_a sigma_b}`;
- `C_- = -C_+`;
- a common real collision-supported distribution `delta_N`;
- coefficient family `c=+i` on `C_+`, `c=-i` on `C_-`, and `c=0` elsewhere.

This is a coefficient-level joint collision-extension object. It is not the reordered ten-spectral surrogate, not a sampled numerical approximation, and not the complete representation-valued causal vertex.

Independent object check: the map from 32 vertex-sign assignments to K5 edge signs is two-to-one because `sigma` and `-sigma` give the same edge pattern, hence `|C_+|=16`. Also `C_+` and `C_-` are disjoint: if `tau_a tau_b = -sigma_a sigma_b` for every edge, then `r_a=tau_a/sigma_a` would satisfy `r_a r_b=-1` on every edge; multiplying the three equations around any K5 triangle gives `+1=-1`, impossible. Thus `|C_-|=16` and the complement has `1024-32=992` patterns.

## SOURCE/REALIZATION_CHECK

`CONFIRMED_SCOPED`.

The gate cites the repository's already terminal local-extension/scaling authority and the published-source audit chain for the EPRL independent-sign decomposition, causal/co-causal sign sectors and one-wedge Toller conjugation structure. The implementation does not alter any individual Toller factor.

The same realization is used throughout the gate: the complete graph on vertices `(1,2,3,4,5)`, its ten unordered edges, all 1024 independent edge-sign patterns, all 32 vertex-sign assignments, and all 120 K5 vertex permutations.

Crucial scope qualification: the tested conjugation condition is deliberately only

`c(-kappa)=conj(c(kappa))`

for a real scalar `delta_N`. The gate does not assert that this is the full source vertex-level conjugation law. Any rho, magnetic-index, boundary-index or representation conjugation map not encoded in this scalar coefficient object remains outside the proof.

## PROVENANCE_CHECK

`CONFIRMED`.

The authoritative run is terminal and complete. Both jobs succeeded, including the prospective source-lock. The uploaded artifact is present and has durable digest

`sha256:47e5d973187494e29cd137ebf09b1081fbce65b5d34258b01bd0800e768c344b`.

No repair occurred after the frozen gate. No historical result was rewritten. CI color is not treated as scientific proof; the scientific content below is independently checked algebraically.

A recovery/front inconsistency is present: `recovery/CURRENT_BENCHMARK_FRONT.md` and `recovery/CURRENT_ACTIVE_FRONT_INDEX_2026-09-15.md` still describe an older source-order/Iter504 frontier and do not yet index this terminal gate. This does not invalidate the gate because current main history, the frozen prereg, implementation, terminal Actions run and artifact are direct authorities. The stale navigation documents must not be used to erase the newer result.

## SAME_REALIZATION_CHECK

`CONFIRMED_SCOPED`.

Independent exact checks of the frozen witness:

- `|C_+|=16`, with global vertex-sign reversal multiplicity two;
- `|C_-|=16` and `C_+ intersect C_- = empty`;
- complement size `992`;
- global edge-sign reversal maps `C_+` bijectively to `C_-`;
- for every sector, the frozen coefficient law gives `c(-kappa)=conj(c(kappa))`;
- K5 vertex permutations preserve causal membership and co-causal membership, so the coefficient family is S5 invariant;
- the distinct-sector full EPRL counterterm sum is `16 i - 16 i = 0`;
- the causal shift is `+16 i` and the co-causal shift is `-16 i`;
- sigma-counted shifts are `+32 i` and `-32 i` because the map from sigma assignments is two-to-one.

No independent-edge surrogate is substituted for the frozen K5 incidence relation.

## NUMERICAL/STATISTICAL_CHECK

`CONFIRMED`.

There is no floating-point or statistical inference in the scientific gate. Gaussian-integer pairs represent coefficients exactly, all finite sets are exhaustively enumerated, and all assertions are exact.

The implementation performs:

- 1024 sign-reversal/conjugation checks;
- `120*1024 = 122880` explicit S5 permutation-pattern checks;
- exact EPRL, causal and co-causal sums;
- exact adversarial controls;
- exact scaling-ledger comparison `sd(delta_N)=12 <= 30`.

The scaling comparison is inherited from the already terminal scoped local-extension ledger; this gate does not promote it beyond that frozen j=1/full-collision setting.

## COUNTEREXAMPLE_ATTEMPTS

1. **Preregistration after seeing the answer.** Rejected: prereg commit precedes both code and workflow commits, and source-lock verifies the frozen commit.

2. **Wrong causal cardinality due to sigma multiplicity.** Rejected analytically: 32 sigma assignments quotient by the global reversal kernel of size two, giving 16 distinct patterns. The gate separately records distinct-pattern and sigma-counted sums.

3. **Hidden overlap `C_+ intersect C_-`.** Rejected analytically by the K5 triangle contradiction above. This is stronger than relying on workflow enumeration.

4. **Full EPRL sum not actually preserved.** Rejected for the frozen unweighted independent-sign sum: exactly 16 coefficients are `+i`, exactly 16 are `-i`, and 992 are zero, so the added collision term sums to zero.

5. **Conjugation condition accidentally fails on zero sectors.** Rejected: noncausal patterns occur in sign-reversal pairs and both coefficients are zero; causal/co-causal pairs carry `+i/-i`, which are exact conjugates.

6. **S5 covariance fails because edge ordering changes.** Rejected: the property of being of the form `sigma_a sigma_b` is invariant under relabelling vertices; global sign reversal commutes with the permutation action. The code additionally checks all 122880 pairs explicitly.

7. **Scaling-window promotion.** Rejected within scope: only zeroth-order `delta_N` with frozen transverse scaling degree 12 is used, below the already certified ceiling 30. This does not establish a global Eq. (4) extension or lower-stratum compatibility.

8. **One-wedge modification hidden inside the witness.** Rejected: the witness is an additive joint collision-supported term and does not change any individual Toller factor off the common collision support.

9. **Coefficient-level conjugation promoted to the complete physical conjugation theorem.** This would be a valid counterexample to an overclaim, because the scalar gate does not encode rho, magnetic, boundary-index and representation transformations. The preregistration explicitly excludes that promotion, so the frozen scoped result survives. Any broader claim would be `INVALID_CONJUGATION_PROMOTION` / outside this review's confirmed scope.

10. **Green CI promoted to science.** Rejected: the verdict rests on the explicit algebraic witness and independent combinatorial proof, with CI used only for provenance/reproducibility.

11. **Finite certificate promoted to family closure.** Rejected: the witness establishes insufficiency of one specified bundle of constraints for this scoped collision coefficient object only. It does not prove ultimate nonuniqueness of the published causal vertex, all spins/channels, or all collision strata.

12. **Non-terminal parallel workflows contaminating the verdict.** Rejected: Iter504 `34907349374` and Iter461 `34748503239` remain queued; no partial substantive data from them enter this review.

## OVERCLAIM_CHECK

`PASS WITH SCOPED CEILING`.

The frozen interpretation ceiling is adequate. The confirmed statement is:

> EPRL independent-sign sum preservation + K5 permutation covariance + the scoped same-scaling collision extension + coefficient-level global sign-reversal/complex-conjugation covariance still admit an explicit nonzero causal/co-causal collision-supported coefficient witness.

Do not promote this to any of the following:

- complete vertex-level causal/co-causal conjugation compatibility;
- source selection of this counterterm;
- global nonuniqueness of Eq. (4);
- every spin/channel or every collision stratum;
- failure of every source-faithful joint normalization;
- closure of D7-S2, D7-S3 or D7-S4;
- a terminal D7 selector;
- Candidate Gravity activation;
- `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

## VERDICT

`CONFIRMED_SCOPED`

The exact coefficient-level ambiguity witness is correct, prospectively frozen, reproducible and independently verified. No explicit counterexample defeats the frozen scoped claim.

## QUALIFICATIONS

1. The result is coefficient-level, not a complete representation-valued vertex conjugation theorem.
2. The common real `delta_N` and the scaling window are inherited from the already scoped j=1 full-collision extension analysis; lower/nested collision strata are not consumed.
3. The witness is not claimed to be source-selected.
4. The result proves insufficiency of the tested bundle of constraints, not ultimate nonuniqueness of the published causal vertex.
5. Distinct causal patterns (16) and sigma-counted assignments (32) must remain separate in future ledgers.
6. Iter504 and Iter461 remain non-terminal and untouched.
7. Current navigation fronts lag this gate; direct main history and this audit supersede them for locating the latest reviewed terminal source-extension result until the fronts are synchronized.

## UPDATED_STATE

- `SOURCE_J1_K5_CAUSAL_COCAUSAL_CONJUGATION_STILL_LEAVES_COLLISION_AMBIGUITY_SCOPED = CONFIRMED_SCOPED`.
- Exact authority: prereg `cb8b6e5a6824ef11cb39b00fd0dae15d1e753b53`; implementation `f322cbb7cc3cd772f2587ac3389c412014a8c1e2`; workflow head `6e9a5e8b0acb964c496f82d43a76fe9765954b60`; run `34917064485`; artifact `10376117713`; digest `sha256:47e5d973187494e29cd137ebf09b1081fbce65b5d34258b01bd0800e768c344b`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden.
- Candidate Gravity remains inactive.
- Iter504 `34907349374` remains queued/non-terminal; no partial science consumed.
- Iter461 `34748503239` remains queued/non-terminal; no partial science consumed.

## NEXT_ADMISSIBLE_GATE

Prospectively freeze and test a genuinely vertex-level source-canonical collision normalization/conjugation condition that acts on the collision-supported joint distribution and explicitly includes the transformations omitted by the coefficient-only gate, in particular the relevant rho, magnetic/boundary-index and representation conjugation maps.

The next gate must distinguish:

- a condition actually stated or derivable from source authority;
- its exact action on collision-supported joint terms;
- whether it excludes the frozen `+i/-i/0` witness or a transformed analogue;
- whether any repair changes the scientific contract.

Do not infer D7 closure from this gate. In parallel, consume Iter504 or Iter461 only if their own authoritative runs become terminal and complete.
