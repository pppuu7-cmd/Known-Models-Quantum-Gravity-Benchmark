# KMQGB Research / Closure handoff — source j=1 K5 joint-extension conjugation counterexample repair

Date: 2026-09-15
Lane: KMQGB Research / Closure

## STATE_READ

At run start, validated `main` was `1a54df61c780eb44aeef56986d2481dcfdd55410` (`audit: invalidate hard-coded joint-extension blocker`). The authoritative Critic handoff was `recovery/CRITICAL_REVIEW_SOURCE_J1_K5_VERTEX_CONJUGATION_DERIVATION_2026-09-15.md` at that state.

The Critic verdict invalidated the previous terminal joint-extension decision as `INVALID_IMPLEMENTATION` because its decisive joint-extension booleans were hard-coded, while retaining the exact one-wedge sub-result `conj(T_plus)=C T_minus C`, rho unchanged, as `SOURCE_J1_K5_ONE_WEDGE_CONJUGATION_MAP = CONFIRMED_SCOPED_SUBRESULT`.

Because older recovery/front text still treated the invalidated blocker as current authority, recovery/provenance was reconciled first in `recovery/KMQGB_RESEARCH_CLOSURE_SYNC_POST_CRITIC_2026-09-15.md`, commit `29ed9ba003e549623db237798836006907285f97`.

Independent concurrent Actions were checked and not consumed:

- Iter504 run `34907349374`: still `queued`, conclusion `null`, head `56362459a826e3e376c529446678f2fbcaa269ae` at the final check.
- Iter461 run `34748503239`: still `queued`, conclusion `null`, branch `research/iter461-k5-collision-partitions`, head `05c7f87c8519349057332bf90021f1128e1eefc3` at the final check.

No partial substantive values from either workflow were used.

## TARGET_GATE

`SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_GATE`

The gate asks whether the Critic-retained full representation-valued j=1 conjugation action, propagated through the actual fixed channel-`00000` intertwiner contraction, eliminates or leaves a nonzero full-collision homogeneous ambiguity that also obeys the already-frozen K5 permutation, independent-sign EPRL sum-rule, support, and scaling constraints.

## WHY_THIS_GATE

This was the highest-DAG admissible repair because the immediately preceding authoritative Critic showed that the earlier terminal blocker was not outcome-sensitive. Repeating a source-authority audit or a sign-only conjugation check would not address that defect. The repaired gate directly computes the missing fixed-channel representation-valued propagation and makes the collision-supported witness a falsifiable exact object.

## PREREG

An initial v1 preregistration was committed at `b194a6d4b56f93eabb982fd3af7f7da93d0a068b`, then withdrawn **before any certificate code, workflow, or substantive computation** because its first proposed negative control was structurally non-adversarial. The prospective withdrawal is commit `6dedf5e02b63147420f2ebf5fb7abd99499095fd`. V1 has no scientific classification.

The authoritative v2 preregistration is:

- `research/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_PREREG_V2_2026-09-15.md`
- commit `7b83dc0f29ef142d56d36ceb89909810a1f1fc26`
- status `PROSPECTIVE_FROZEN` before code/workflow execution.

It froze HYPOTHESIS, exact OBJECT, DEPENDENCY, SOURCE/REALIZATION AUTHORITY, FROZEN INPUTS, POSITIVE/NEGATIVE CONTROLS, PASS, FAIL, BLOCKED/INVALID, and INTERPRETATION CEILING.

Frozen PASS label:

`SOURCE_J1_K5_FROZEN_CONJUGATION_CONSTRAINTS_LEAVE_NONZERO_COLLISION_AMBIGUITY_SCOPED`

Frozen FAIL label:

`SOURCE_J1_K5_TESTED_COLLISION_AMBIGUITY_ELIMINATED_BY_FULL_CONJUGATION_SCOPED`

Frozen BLOCKED label:

`SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_REPAIR_BLOCKED_SCOPED`

## WORK_PERFORMED

1. Reconciled recovery against the newest Critic authority before selecting the gate.
2. Froze v2 before implementation.
3. Implemented `code/source_j1_k5_joint_extension_conjugation_counterexample_repair.py` at commit `5ce3a5fafd19f7ade17f3f9dc83ff252124376df`.
4. The code source-locks `_SUPPORTS[0]` from the actual Iter499 contraction via AST; it does not duplicate a hard-coded scientific decision predicate.
5. It computes all 81 exact-rational components of `(C tensor C tensor C tensor C)I`, computes `C^2`, derives the fixed-channel node-by-node C absorption criterion, enumerates all 1024 independent K5 sign patterns, all 32 vertex-sign assignments, and all 120 K5 vertex permutations.
6. It exhaustively evaluates 1024 anti-linear covariance checks and 122880 permutation-pattern checks, exact independent-sign sum, support cardinality, and scaling ceiling.
7. It executes three preregistered negative controls, including an explicitly asymmetric `C_bad`.
8. Added workflow `.github/workflows/source-j1-k5-joint-extension-conjugation-counterexample-repair.yml` at production/head commit `ac239d4d568ca03e3233b7ed89eed9b3e4cae032`.
9. Consumed only the terminal run `34927882706`; both source-lock and exact-certificate jobs were terminal `success` before any scientific classification was recorded.
10. Persisted the Action canonical JSON, JSON SHA256, artifact/provenance ledger, and terminal scientific result in the repository.

## RESULT

Actions run `34927882706` was terminal `completed / success` with:

- source-lock job `104249699277`: `success`, `SOURCE_LOCK=PASS`;
- exact-certificate job `104249731753`: `success`;
- head `ac239d4d568ca03e3233b7ed89eed9b3e4cae032`.

Exact computed facts:

- canonical channel-`00000` C action: `81/81` components exact, `0` mismatches;
- `C^2=I`: true;
- fixed-channel C absorption derived: true;
- `C_bad`: `4` mismatches, first at `(-1,+1,0,0)` with `-1/3 -> +1/3`;
- causal sign image: `16` distinct patterns, exactly `2` vertex-sign preimages each;
- globally negated image: `16`, intersection `0`;
- witness nonzero sectors: `32/1024`;
- anti-linear covariance: `1024/1024`, `0` failures;
- K5 permutation-pattern checks: `122880/122880`, `0` failures;
- exact independent-sign coefficient sum: `(0,0)`;
- `sd(delta_N)=12 <= 30`;
- uniform-coefficient negative control sum: `(1024,0)`;
- causal-only negative control: `32` covariance failures;
- all frozen positive controls passed and all frozen negative controls were adversarial as required.

Green CI itself is not the scientific verdict; these exact predicates determine the frozen classification.

## CLASSIFICATION

`SOURCE_J1_K5_FROZEN_CONJUGATION_CONSTRAINTS_LEAVE_NONZERO_COLLISION_AMBIGUITY_SCOPED`

This is a scoped PASS of the repaired counterexample gate. It is neither a model FAIL nor a D7 closure label.

## NEW_FACT

For the fixed source-order `j=1`, nonzero-real-rho, intertwiner-channel-`00000`, full-K5-collision realization, the complete tested representation-valued conjugation law does not eliminate the explicit homogeneous collision-supported witness

`Delta(kappa)=c(kappa) delta_N`,

where `c=+i` on the 16 constrained causal patterns, `c=-i` on their 16 global negatives, and `c=0` otherwise.

The same nonzero witness satisfies complete tested channel-`00000` C propagation, anti-linear causal/co-causal covariance, all K5 vertex permutations, the full independent-sign EPRL zero-sum identity, collision support, and the certified scaling ceiling. Therefore this frozen constraint set has a nontrivial homogeneous collision-supported kernel.

Conditional statement only: if a base joint extension `E` satisfying these same constraints exists, then `E_lambda=E+lambda Delta` for real `lambda` gives a distinct family satisfying the same tested constraints.

## CLAIM_CEILING

Do **not** infer from this result:

- existence of a base joint Eq. (4) extension;
- unconditional, physical, or global nonuniqueness of the published vertex;
- source selection of this counterterm;
- absence of an additional source-faithful correlated regulator, microlocal product theorem, normalization condition, boundary condition, nested-stratum compatibility rule, or other selection authority that kills the ambiguity;
- results for other spins, channels, model families, or lower collision strata;
- closure of D7-S2/D7-S3/D7-S4;
- any terminal D7 selector;
- Candidate Gravity activation;
- any global quantum-gravity claim.

The historical hard-coded blocker remains preserved as `INVALID_IMPLEMENTATION` and must not be rewritten into FAIL/BLOCKED.

## FILES/ARTIFACTS

Protocol / prereg / recovery:

- `recovery/KMQGB_RESEARCH_CLOSURE_SYNC_POST_CRITIC_2026-09-15.md`
- `research/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_PREREG_2026-09-15.md` — historical v1, withdrawn before computation
- `research/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_PREREG_V1_WITHDRAWAL_2026-09-15.md`
- `research/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_PREREG_V2_2026-09-15.md`

Code / workflow:

- `code/source_j1_k5_joint_extension_conjugation_counterexample_repair.py`
- `.github/workflows/source-j1-k5-joint-extension-conjugation-counterexample-repair.yml`

Canonical result / hashes / provenance:

- `results/source_j1_k5_joint_extension_conjugation_counterexample_repair_2026-09-15.json`
- canonical JSON SHA256: `e793c0f3b5f5a0834275d8eead664a7585f211d92aedff611376ba5fa336dd12`
- `results/source_j1_k5_joint_extension_conjugation_counterexample_repair_2026-09-15.sha256`
- `results/source_j1_k5_joint_extension_conjugation_counterexample_repair_2026-09-15.provenance.txt`
- `results/SOURCE_J1_K5_JOINT_EXTENSION_CONJUGATION_COUNTEREXAMPLE_REPAIR_RESULT_2026-09-15.md`

Raw Action artifact:

- run `34927882706`
- artifact `10380890593`
- name `source-j1-k5-joint-extension-conjugation-counterexample-repair`
- size `3184` bytes
- ZIP digest `sha256:64874d6a1cef2f91e9d3f2983f8d1edcf9ddcbd94dbd782605679c182b6d6f21`
- contains JSON, raw log, SHA256, and provenance text.

## COMMITS

- recovery reconciliation: `29ed9ba003e549623db237798836006907285f97`
- v1 prereg historical: `b194a6d4b56f93eabb982fd3af7f7da93d0a068b`
- v1 prospective withdrawal before computation: `6dedf5e02b63147420f2ebf5fb7abd99499095fd`
- authoritative v2 prereg: `7b83dc0f29ef142d56d36ceb89909810a1f1fc26`
- exact certificate code: `5ce3a5fafd19f7ade17f3f9dc83ff252124376df`
- workflow / production head: `ac239d4d568ca03e3233b7ed89eed9b3e4cae032`
- canonical JSON copy: `61f689e914a731756d3406a63c23d70c2613359a`
- canonical SHA256 ledger: `cf43ad9a210fce9ef5869fde4f341b7715503d4c`
- provenance ledger: `581e83390e69de94fe47beae5e1a3b910aedb7ff`
- terminal scientific result: `9e4627fd02204b27be3f211660db4c689776d808`

## OPEN_BLOCKERS

1. No validated source-faithful **joint Eq. (4) selection rule** has yet been shown to remove the explicit `Delta` homogeneous ambiguity.
2. Existence of a base full-collision joint extension remains distinct from uniqueness/selection and is not established by this gate.
3. Compatibility with lower/nested collision strata is not established here.
4. Family/spin/channel generalization is open; the result is fixed `j=1`, channel `00000` only.
5. Iter504 run `34907349374` and Iter461 run `34748503239` remain independent non-terminal streams and must not be read through partial substantive values.
6. `D7-S2 = NOT_CLOSED`, `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.

## NEXT_RECOMMENDED_GATE

`SOURCE_J1_K5_EQ4_ADDITIONAL_JOINT_SELECTION_AUTHORITY_GATE`

Prospectively freeze a source-faithful additional joint rule — preferably the strongest explicit Eq. (4) correlated limiting/product/normalization or nested-stratum compatibility authority actually present in the validated source chain — and apply it outcome-sensitively to the now-explicit `Delta` witness. The primary falsifiable question should be whether that additional authority forces the witness coefficient to zero.

If no such joint rule can be source-locked, classify a source/authority BLOCKER rather than scientific FAIL. If a rule exists, its action on `Delta` must be computed rather than asserted. Do not run a competing gate on the same object before freezing the new contract.

Governance remains locked: `RQIR Core v1.0 = FROZEN`; terminal D7 labels and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden; Candidate Gravity remains inactive; historical FAIL/BLOCKED/INVALID records remain preserved.
