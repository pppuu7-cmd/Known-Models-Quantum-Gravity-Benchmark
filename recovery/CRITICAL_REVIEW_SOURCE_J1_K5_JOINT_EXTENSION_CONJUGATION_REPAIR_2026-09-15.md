# KMQGB Critical Review — source j=1 K5 joint-extension conjugation counterexample repair

Date: 2026-09-15
Lane: independent Critical Review / Verification
Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
Verdict: `CONFIRMED_SCOPED`

## RESULT_REVIEWED

Reviewed exactly one latest terminal substantive Research result:

- `results/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_RESULT_2026-09-15.md`;
- terminal result commit `9e4627fd02204b27be3f211660db4c689776d808`;
- recovery handoff `recovery/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_HANDOFF_2026-09-15.md`;
- handoff/main head at review start `2eb0da9c987eb706df29971ccea29f65928005d7`;
- Research classification under review: `SOURCE_J1_K5_FROZEN_CONJUGATION_CONSTRAINTS_LEAVE_NONZERO_COLLISION_AMBIGUITY_SCOPED`.

The reviewed claim is strictly scoped to the source-order fixed `j=1`, nonzero-real-`rho`, intertwiner-channel `00000`, full-K5-collision realization. It claims that the particular frozen constraint set tested by the v2 gate has a nonzero collision-supported homogeneous kernel. It does not claim existence of a base joint extension, source selection of the witness, or physical/global nonuniqueness.

Concurrent authoritative Research workflows were checked fresh and remain non-terminal:

- Iter504 run `34907349374`: `queued`, conclusion `null`;
- Iter461 run `34748503239`: `queued`, conclusion `null`.

No partial substantive values from either run are consumed in this review.

## PREREG_CHECK

The authoritative preregistration is:

- `research/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_PREREG_V2_2026-09-15.md`;
- commit `7b83dc0f29ef142d56d36ceb89909810a1f1fc26`;
- status `PROSPECTIVE_FROZEN`.

Chronology is valid:

1. historical v1 prereg `b194a6d4b56f93eabb982fd3af7f7da93d0a068b`;
2. v1 prospective withdrawal before certificate/workflow/substantive computation `6dedf5e02b63147420f2ebf5fb7abd99499095fd`;
3. authoritative v2 prereg `7b83dc0f29ef142d56d36ceb89909810a1f1fc26`;
4. implementation `5ce3a5fafd19f7ade17f3f9dc83ff252124376df`;
5. workflow/production head `ac239d4d568ca03e3233b7ed89eed9b3e4cae032`;
6. terminal Actions run `34927882706`;
7. canonical result/hash/provenance copies;
8. terminal Research result `9e4627fd02204b27be3f211660db4c689776d808`;
9. recovery handoff `2eb0da9c987eb706df29971ccea29f65928005d7`.

Direct compare from the v2 prereg commit to the workflow head shows only two added files: the repair certificate and its workflow. No frozen dependency, source tensor, scaling audit, witness definition, threshold, object, or interpretation ceiling changed between preregistration and execution.

The v2 frozen contract includes HYPOTHESIS, exact OBJECT, DEPENDENCY, SOURCE/REALIZATION AUTHORITY, FROZEN INPUTS, POSITIVE/NEGATIVE CONTROLS, PASS, FAIL, BLOCKED/INVALID, and INTERPRETATION CEILING. No hidden post-hoc threshold or outcome-dependent domain/state selection was found.

## OBJECT_IDENTITY_CHECK

The computed object is the intended fixed-channel source-order K5 object, not a reordered ten-spectral surrogate or an independent-edge replacement.

The certificate source-locks `_SUPPORTS[0]` directly from `code/iter499_arb_core.py`. That tensor is the same channel-0 tensor used by the validated five-node/tensor-network contraction. The actual network convention in `iter499_arb_core.py::contract_all` uses five node tensors and ten edge matrices with endpoint labels inherited from `iter482_common_node_su2_control.py`.

The homogeneous ambiguity itself is

`Delta(kappa) = c(kappa) delta_N`,

with `delta_N` supported on the full collision stratum `N=K^4`, `K=SU(2)`, inside gauge-fixed `G^4`, `G=SL(2,C)`. The independent scaling audit gives codimension `12`, target transverse scaling degree `30`, and same-scaling ambiguity order at most `18`; a zeroth-order `delta_N` has scaling degree `12` and is therefore inside that already-established local ambiguity window.

No lower collision stratum is substituted for the full-collision object.

## SOURCE/REALIZATION_CHECK

The upstream one-wedge authority retained by the previous Critic is the exact frozen relation

`conj(T_plus(U1,beta,U2;rho)) = C T_minus(U1,beta,U2;rho) C`,

with unchanged real `rho` and

`C = [[0,0,1],[0,-1,0],[1,0,0]]`.

The repair certificate does not rediscover or alter that source law. It propagates it through the same channel-0 intertwiner tensor and computes the required exact tensor identity.

Exact result:

`(C tensor C tensor C tensor C) I_0 = I_0`

for all `81/81` magnetic components, with zero mismatch. The deliberately asymmetric frozen `C_bad` fails on four components, so the node-invariance control is genuinely discriminating.

Independent analytic propagation check: after complex conjugation, each K5 edge matrix contributes one `C` on each endpoint index. Regrouping the expanded contraction node by node places four `C` actions on each channel-0 intertwiner. Because the certificate proves `C^tensor4 I_0 = I_0` exactly and `C` is real/symmetric, all endpoint `C` factors are absorbed and the complete fixed-channel scalar network maps from sign pattern `kappa` to `-kappa`. This establishes the representation-valued fixed-channel propagation without relying on a sign-only surrogate. `C^2=I` is also exactly true, although it is not needed as the decisive step in this node-by-node absorption argument.

The one-wedge relation is at the same `U1,beta,U2,rho` arguments, so no additional group-variable pullback is introduced by this derived conjugation identity. For the frozen real zeroth-order collision distribution, complex conjugation leaves `delta_N` fixed; the remaining anti-linear condition is therefore correctly transferred to the coefficient family.

## PROVENANCE_CHECK

Authoritative Actions provenance is complete and terminal:

- workflow `source-j1-k5-joint-extension-conjugation-counterexample-repair`;
- run `34927882706`;
- head `ac239d4d568ca03e3233b7ed89eed9b3e4cae032`;
- status/conclusion `completed / success`;
- source-lock job `104249699277`: success;
- exact-certificate job `104249731753`: success;
- artifact `10380890593`;
- artifact name `source-j1-k5-joint-extension-conjugation-counterexample-repair`;
- artifact size `3184` bytes;
- artifact ZIP digest `sha256:64874d6a1cef2f91e9d3f2983f8d1edcf9ddcbd94dbd782605679c182b6d6f21`;
- canonical JSON SHA256 `e793c0f3b5f5a0834275d8eead664a7585f211d92aedff611376ba5fa336dd12`.

The terminal log reproduces the same exact classification and exact counts recorded in the repository result. Green CI is treated only as provenance, not as the scientific argument.

The workflow source-lock verifies ancestry of the Critic authority, reconciliation, historical derivation result, prior sum-rule result, v1 withdrawal, v2 preregistration, and repair code. A direct prereg-to-head compare additionally verifies that the scientific dependency files were not modified after v2 freezing and before the run.

## SAME_REALIZATION_CHECK

The same realization is used across the relevant chain:

- magnetic ordering and `C` are the frozen j=1 convention;
- channel tensor is source-loaded from `_SUPPORTS[0]` in Iter499 rather than copied as a second independent scientific object;
- K5 edge order is `(01,02,03,04,12,13,14,23,24,34)`;
- all `1024` independent edge-sign patterns are enumerated;
- causal patterns are generated from all `32` vertex-sign assignments by `kappa_ab=sigma_a sigma_b`, yielding exactly `16` distinct patterns with two preimages each;
- globally negated patterns yield another disjoint `16`;
- the coefficient witness is nonzero on exactly `32/1024` sectors.

No independent-edge KAK sample, fitted surrogate, reordered spectral object, different spin, different channel, or altered rho convention enters the repaired decision.

## NUMERICAL/STATISTICAL_CHECK

The decisive certificate is exact finite algebra/combinatorics, not statistical inference.

Exact certified facts:

- canonical node equality: `81/81`, zero mismatches;
- `C_bad`: `77/81` equal and `4` mismatches;
- `C^2=I`: true;
- causal image: `16` distinct patterns, two vertex-sign preimages each;
- globally negated image: `16`, intersection `0`;
- anti-linear coefficient covariance `c(-kappa)=conj(c(kappa))`: `1024/1024`, zero failures;
- K5 coefficient-pattern permutation checks: `122880/122880`, zero failures;
- independent-sign coefficient sum: exactly `(0,0)`;
- witness support: `32` sectors;
- `sd(delta_N)=12 <= 30`;
- uniform `+1` negative-control sum: `(1024,0)`;
- causal-only `+i` negative control: `32` covariance failures.

No confidence interval, stochastic covariance model, regression fit, floating threshold, or interval-dependency estimate controls the PASS classification.

## COUNTEREXAMPLE_ATTEMPTS

1. **Wrong prereg chronology.** Rejected. V1 was explicitly withdrawn before any certificate/workflow/substantive computation; v2 is the prospective authority.

2. **Post-prereg source mutation.** Rejected for the executed gate. Comparing v2 prereg to production head shows only the new certificate and workflow; frozen source/dependency files did not change in that interval.

3. **Hard-coded scientific predicate repeated from the invalidated gate.** Rejected. The repaired code computes node invariance from the source-loaded tensor, computes the sign sets, covariance, sum rule, permutations, scaling comparison, and adversarial controls. The terminal outcome is not forced by a literal joint-extension boolean.

4. **Sign-only conjugation promoted to representation-valued vertex law.** Rejected in the fixed channel. Exact `C^tensor4 I_0=I_0` plus the actual K5 endpoint contraction structure analytically absorbs the representation matrices node by node, yielding the scalar fixed-channel `kappa -> -kappa` relation.

5. **Collision distribution action silently omitted.** Rejected for the frozen zeroth-order witness. The derived one-wedge conjugation keeps the group/KAK arguments and rho unchanged; the frozen `delta_N` is real and supported on the same full-collision stratum, so complex conjugation fixes this distribution. No untested geometric pullback is required for this particular witness.

6. **Counterterm outside the extension window.** Rejected. The independent scaling audit gives target scaling degree 30 in codimension 12 and allows local normal derivatives through order 18; zeroth-order `delta_N` with scaling degree 12 is admissible without increasing the target scaling degree.

7. **Causal/co-causal sets overlap, killing the `+i/-i` construction.** Rejected. The exact enumeration gives `16+16` disjoint sectors. Analytically, a pattern cannot satisfy both `kappa_ab=sigma_a sigma_b` and `-kappa_ab=tau_a tau_b` on K5 because restricting to any triangle would require a product of three pair ratios to be simultaneously `+1` and `-1`.

8. **Independent-sign EPRL identity broken by the witness.** Rejected. Sixteen `+i` and sixteen `-i` coefficients sum exactly to zero; the remaining 992 coefficients vanish.

9. **Permutation result promoted beyond what was actually checked.** Qualification required. The exhaustive `120*1024` test proves invariance of the coefficient/sign-pattern family under K5 vertex relabeling. It is not, by itself, a theorem that an arbitrary boundary intertwiner basis is invariant under all induced local leg permutations or recouplings. The reviewed result is valid only when its phrase `K5 permutation symmetry` is read at the frozen coefficient-pattern/full-collision witness level, not as a family-wide boundary-state recoupling theorem.

10. **Finite enumeration promoted to universal all-spin/all-channel theorem.** Rejected by scope. The certificate is exact but fixed to j=1/channel-00000 and the finite K5 sign/permutation object.

11. **Nonzero homogeneous solution promoted to existence of a base extension.** Rejected. The result states the family `E_lambda=E+lambda Delta` only conditionally on existence of a base `E` satisfying the same constraints.

12. **Nonzero homogeneous solution promoted to physical/source nonuniqueness.** Rejected. Additional source-faithful joint regulator/product/normalization/nested-stratum authority may still force the witness coefficient to zero; this gate tests only the frozen constraint set.

13. **Green CI promoted to science.** Rejected. The scientific content is the exact algebraic/combinatorial witness and analytic network propagation; CI only records reproducibility/provenance.

14. **Concurrent non-terminal workflows silently consumed.** Rejected. Iter504 and Iter461 remain queued with null conclusion; no partial substantive value is used.

15. **Recovery/front navigation treated as stronger than current main.** Rejected. `recovery/CURRENT_BENCHMARK_FRONT.md` and `CURRENT_ACTIVE_FRONT_INDEX_2026-09-15.md` remain stale relative to the newest conjugation-repair chain. Current main plus the immutable prereg/result/handoff and Actions records govern. This is a recovery-navigation inconsistency, not a defect in the reviewed scientific result.

## OVERCLAIM_CHECK

The central scoped claim survives review:

For the fixed source-order j=1, nonzero-real-rho, channel-00000 full-collision realization, the explicitly tested conjunction of representation-valued fixed-channel conjugation, coefficient-pattern K5 relabeling symmetry, independent-sign EPRL zero-sum, collision support, and the already-certified scaling ceiling admits a nonzero homogeneous collision-supported witness.

This proves insufficiency of **that tested constraint set** for uniqueness. It does not prove that the published source supplies no additional selection rule.

Required wording guard for future reuse: `K5 permutation symmetry` here means the frozen K5 coefficient/sign-pattern relabeling test. Do not promote the `122880` coefficient checks into an unrestricted statement about recoupling covariance of arbitrary boundary intertwiner bases.

Do not infer:

- existence of a base joint Eq. (4) extension;
- unconditional physical/global nonuniqueness;
- source selection of `Delta`;
- impossibility of a source-faithful correlated regulator, microlocal product theorem, normalization condition, boundary condition, or nested-stratum rule that kills `Delta`;
- any other-spin/channel/family/lower-stratum result;
- D7-S2/S3/S4 closure;
- any terminal D7 selector;
- Candidate Gravity authority;
- any global quantum-gravity claim.

## VERDICT

`CONFIRMED_SCOPED`

Reason: the v2 gate is prospectively frozen, the repair is outcome-sensitive, the same source-defined channel tensor is used, exact representation-valued node propagation is verified, the coefficient witness satisfies every frozen exact condition, adversarial controls genuinely fail, and an independent analytic contraction argument confirms that the local `C` actions absorb through the complete fixed-channel K5 network. No counterexample was found to the actual scoped PASS claim.

The only material qualification is semantic/scope-related: the exhaustive permutation certificate is a coefficient/sign-pattern K5 relabeling result and must not be promoted to a universal boundary-intertwiner recoupling theorem.

## QUALIFICATIONS

1. Result applies only to fixed source-order `j=1`, nonzero real rho, channel `00000`, and the full K5 collision.
2. The result establishes a nonzero homogeneous kernel of the tested constraints, not existence of a base extension.
3. Physical/source nonuniqueness is not established; additional source-faithful joint selection authority remains open.
4. The K5 permutation check is coefficient/sign-pattern level in this fixed witness; no family-wide boundary recoupling theorem is licensed.
5. `32/1024` support and `122880` permutation checks are exact finite certificates, not all-spin/all-channel theorems.
6. Iter504 and Iter461 remain non-terminal and untouched.
7. Stale recovery/front navigation should be reconciled by the Research lane but does not override current main or this immutable audit.

## UPDATED_STATE

`SOURCE_J1_K5_FROZEN_CONJUGATION_CONSTRAINTS_LEAVE_NONZERO_COLLISION_AMBIGUITY_SCOPED = CONFIRMED_SCOPED`

Historical previous joint-extension blocker remains:

`SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_JOINT_EXTENSION_ACTION_BLOCKED_SCOPED = INVALID_IMPLEMENTATION`

and is not rewritten.

Authoritative repaired-gate provenance:

- v2 prereg: `7b83dc0f29ef142d56d36ceb89909810a1f1fc26`;
- code: `5ce3a5fafd19f7ade17f3f9dc83ff252124376df`;
- workflow/head: `ac239d4d568ca03e3233b7ed89eed9b3e4cae032`;
- Actions run: `34927882706`;
- source-lock job: `104249699277`;
- exact-certificate job: `104249731753`;
- artifact: `10380890593`;
- artifact digest: `sha256:64874d6a1cef2f91e9d3f2983f8d1edcf9ddcbd94dbd782605679c182b6d6f21`;
- canonical JSON SHA256: `e793c0f3b5f5a0834275d8eead664a7585f211d92aedff611376ba5fa336dd12`;
- terminal Research result: `9e4627fd02204b27be3f211660db4c689776d808`;
- Research handoff: `2eb0da9c987eb706df29971ccea29f65928005d7`.

Governance remains:

- `RQIR Core v1.0 = FROZEN`;
- `D7-S2 = NOT_CLOSED`;
- `D7-S3 = NOT_CLOSED`;
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`;
- terminal D7 labels and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden;
- Candidate Gravity remains inactive;
- BLOCKED/INVALID remains distinct from scientific FAIL.

## NEXT_ADMISSIBLE_GATE

Do not rerun or broaden the confirmed repair witness as a universal theorem.

The next admissible high-information gate is the Research-proposed

`SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_GATE`.

It should be prospectively frozen and source-lock the strongest additional Eq. (4) joint rule actually present in the validated source chain: correlated limiting/regulator prescription, microlocal product/extension condition, normalization condition, boundary condition, or nested-stratum compatibility rule. The decision must act explicitly on the now-confirmed `Delta` witness and be capable of returning at least:

- witness forced to zero / excluded by the added authority;
- witness preserved by the added authority;
- authority not source-pinned / `BLOCKED_OBJECT_DEFINITION` or other appropriate blocker;
- implementation/provenance invalid if the frozen contract is not executed.

If a new rule requires new scientific source/realization data, freeze a new gate before computation. Do not infer a terminal D7 classifier, selector label, or Candidate Gravity activation from the present scoped result.