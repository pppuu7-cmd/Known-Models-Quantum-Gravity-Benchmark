# KMQGB Critical Review — source j=1 K5 vertex conjugation derivation / joint-extension decision

Date: 2026-09-15
Lane: independent Critical Review / Verification
Repository: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`
Verdict: `INVALID_IMPLEMENTATION`

## RESULT_REVIEWED

Reviewed exactly one latest terminal substantive Research result:

- `research/SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_DERIVATION_COUNTERTERM_RESULT_2026-09-15.md`
- terminal result commit: `181ca68f524fee5d9eab1c9501142d409cd02c2b`
- recovery handoff: `recovery/KMQGB_RESEARCH_CLOSURE_HANDOFF_VERTEX_CONJUGATION_DERIVATION_2026-09-15.md`
- handoff/main head before this Critic: `801498f60e12de6ed0f03c0107a8d0d48296fffd`
- Research classification under review: `SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_JOINT_EXTENSION_ACTION_BLOCKED_SCOPED`

The result contains two logically distinct parts:

1. derivation of an exact frozen j=1 one-wedge anti-linear map;
2. a terminal decision that the frozen source chain plus that newly derived map still cannot determine the joint collision-supported K5 extension action.

The first part is strongly supported. The second part is not implemented according to the prospectively frozen contract, and it is the second part that controls the terminal `BLOCKED_SCOPED` classification.

Concurrent authoritative Research workflows remain non-terminal at review time:

- Iter504 run `34907349374`: `queued`, conclusion `null`;
- Iter461 run `34748503239`: `queued`, conclusion `null`.

No partial substantive value from either run is consumed here.

## PREREG_CHECK

Prospective preregistration:

- `research/SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_DERIVATION_COUNTERTERM_PREREG_2026-09-15.md`
- commit `93f03b5f1458ad49f80065c959e596c0ac19039a`.

Chronology is prospective:

`93f03b5...` prereg -> `4b7ce62...` code -> `ec55715...` workflow/production -> Actions run `34923962807` -> `a1c99c6...` canonical result -> `181ca68...` terminal Research result -> `801498f...` handoff.

The frozen contract explicitly separates the one-wedge derivation question from the joint-extension decision question. The BLOCKED criterion requires that the one-wedge map be uniquely derived and verified **and** that the frozen source chain does not determine a unique action on collision-supported joint K5 extension terms without an additional prescription.

No post-hoc threshold/domain/state selection was found in the one-wedge numerical/symbolic part. The defect is instead an implementation mismatch in the joint decision stage.

## OBJECT_IDENTITY_CHECK

The intended object is the fixed source-order j=1 EPRL/FK full-collision problem in boundary intertwiner channel `(0,0,0,0,0)`, with ten K5 wedge signs and the previously frozen collision-supported witness.

The numerical/symbolic one-wedge calculation stays on the frozen reduced Toller/Eq. (7) realization. No reordered ten-spectral, fitted KAK, independent-edge, different-spin, or different-channel surrogate is substituted there.

However, the terminal joint-extension classifier does not actually operate on the complete joint collision-supported object. It reduces the second-stage decision to a string-presence check on an earlier authority audit that predates the newly derived map.

## SOURCE/REALIZATION_CHECK

Actions source-lock verified all six preregistered frozen blobs at production head `ec5571545ff20b4eb6e22c0b41f783d0a7722839`.

The derived reduced identities are symbolically checked directly against the frozen Iter456 formulas:

`conj(t_plus_m(rho,beta)) = t_minus_-m(rho,beta)`

for `m=+1,0,-1`, with rho unchanged.

The frozen Iter457 j=1 magnetic reconstruction is used to verify

`conj(D^1(U)) = C D^1(U) C`

and therefore the full one-wedge matrix identity

`conj(T_plus(U1,beta,U2;rho)) = C T_minus(U1,beta,U2;rho) C`.

These source/realization checks support the one-wedge sub-result.

They do not, by themselves, establish the terminal joint-extension conclusion.

## PROVENANCE_CHECK

Authoritative Actions provenance is complete for the executed certificate:

- run `34923962807`, head `ec5571545ff20b4eb6e22c0b41f783d0a7722839`, completed success;
- source-lock job `104237893942`, success;
- certificate job `104237923698`, success;
- artifact `10379315977`, name `source-j1-k5-vertex-conjugation-derivation`;
- artifact digest `sha256:c3b5563448613c944f9d7cbbe000331525da35a0704d811b17f1019d3cb5f2d6`;
- canonical repository JSON blob `28afc5874e0f5c70f96e09de5e9b19b298287bf9`.

The workflow pins Python 3.12 with `mpmath==1.3.0` and `sympy==1.14.0`.

Green CI is treated only as provenance. The implementation defect below is visible in the successful code itself and is not cured by workflow success.

## SAME_REALIZATION_CHECK

The one-wedge symbolic and full-matrix checks use the same frozen j=1 Toller/Eq. (7) realization and the same magnetic ordering. The coefficient witness control also preserves the same ten-sign K5 combinatorics.

The failure occurs when moving from those valid same-realization controls to the **joint-extension decision**: the code does not construct or test a representation-valued joint collision action in that realization.

## NUMERICAL/STATISTICAL_CHECK

The one-wedge numerical discrimination is high precision and followed by exact symbolic verification, so the scientific content does not rest on a fitted numerical residual.

Recorded controls:

- 256 frozen candidate maps tested;
- exactly one survivor in the frozen candidate class;
- survivor max reduced residual `5.6089728176988790152404640942259946910897077121379e-81`;
- exact symbolic reduced checks all zero;
- 140 full matrix points;
- max full-matrix residual `5.0527970024459366808957170543113001311949532646006e-81`;
- symbolic Wigner identity passes;
- best rejected candidate residual approximately `3.9201162702385955e-2`.

No stochastic inference, confidence interval, covariance model, or regression threshold controls the conclusion.

Qualification: uniqueness is certified only within the prospectively frozen 256-element candidate family; the exact identity itself is stronger evidence for the displayed map than the finite-search uniqueness claim.

## COUNTEREXAMPLE_ATTEMPTS

1. **Wrong source/version.** Rejected. Source-lock verifies prereg ancestry and all six frozen blob SHAs.

2. **Numerical fit promoted to exact identity.** Rejected. SymPy simplification independently returns exact zero for the three reduced identities and the Wigner relation.

3. **Green CI promoted to science.** Rejected. Workflow success is provenance only.

4. **Finite candidate search promoted to universal uniqueness.** Qualified. The displayed conjugation identity is exact in the frozen formulas, but the search proves uniqueness only inside the frozen 256-map ansatz. No broader universal anti-linear uniqueness theorem is licensed.

5. **Coefficient witness promoted directly to full vertex.** Rejected by the preregistration and result ceiling.

6. **Joint blocker genuinely recomputed after the new one-wedge derivation.** **Counterexample found.** The implementation function `joint_authority_audit()` does not derive or test the action of the newly obtained map on joint collision-supported terms. It reads only `SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_AUTHORITY_RESULT_2026-09-15.md`, checks for two pre-existing text strings, then returns `unique_joint_extension_action_derived_from_frozen_chain: False` as a hard-coded literal.

7. **Earlier authority absence can substitute for the new derivability test.** Rejected. The frozen earlier authority result explicitly states that it closes only the search for an already-pinned law and does **not** close the mathematical derivability problem; it recommends the present derivation gate as the next step. Therefore importing its pre-derivation absence classification cannot decide what follows after the newly derived map is added.

8. **The hard-coded boolean is merely an implementation detail with no effect.** Rejected. The terminal classifier branches directly on `not joint['unique_joint_extension_action_derived_from_frozen_chain']`. Once the one-wedge positive controls pass and the old text strings are found, `BLOCKED_SCOPED` is forced by construction. No possible output of the newly derived map can make the code reach PASS unless that literal is edited manually.

9. **The code nevertheless proves that no joint action follows logically from the new map.** Rejected. No explicit pair of joint extensions respecting the newly derived representation-valued law is constructed, no complete vertex contraction under the `C` matrices is evaluated, no collision-supported distribution action is derived, and no theorem is supplied showing that the new map is insufficient. The required second-stage scientific test is absent.

10. **Existing earlier one-wedge-vs-joint counterexample automatically fills the gap.** Not sufficient for this implementation. That earlier result establishes that one-wedge uniqueness alone does not fix the joint extension. The present gate adds a new representation-valued conjugation law precisely to test whether the stronger condition changes that conclusion. Reusing the old absence statement without testing compatibility with the new law is circular.

11. **Current recovery front overrides the terminal result.** Rejected. `recovery/CURRENT_BENCHMARK_FRONT.md` is stale relative to current main; current main, the terminal Research result, handoff, and Actions records govern. This navigation staleness is recorded but is not the scientific reason for the verdict.

## OVERCLAIM_CHECK

The exact one-wedge identity is a legitimate new scoped fact in the frozen j=1 realization.

The terminal statement

`SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_JOINT_EXTENSION_ACTION_BLOCKED_SCOPED`

is not presently justified by the implemented gate, because the decisive joint-extension predicate is hard-coded rather than scientifically evaluated after the new map is derived.

This does **not** imply the opposite scientific conclusion. In particular, this review does not claim that a unique source-canonical joint extension exists, that the witness is preserved, that it is excluded, or that the causal vertex fails.

The correct Critic action is to invalidate the implementation of the terminal decision while preserving the valid one-wedge derivation as a scoped sub-result.

No D7 closure, terminal selector, Candidate Gravity activation, or global quantum-gravity statement is authorized.

## VERDICT

`INVALID_IMPLEMENTATION`

Reason: the prospectively frozen gate requires an actual post-derivation test of whether the newly derived full one-wedge map plus the frozen source chain determines the joint collision-supported action. The implementation instead hard-codes the decisive predicate to `False` and relies on a pre-derivation authority-absence record. This is a direct frozen-contract/implementation mismatch.

The one-wedge sub-result remains independently supportable:

`conj(T_plus)=C T_minus C`, with rho unchanged, for the frozen j=1 realization.

But the terminal `BLOCKED_SCOPED` joint-extension classification must not be used as validated science until a contract-faithful gate is executed.

## QUALIFICATIONS

1. `INVALID_IMPLEMENTATION` applies to the terminal joint-extension decision, not to the exact one-wedge conjugation identity.
2. The Critic does not infer PASS or FAIL for the joint-extension question from this defect.
3. A code repair that merely replaces the hard-coded literal with another asserted value is not admissible.
4. Any repair must execute an outcome-sensitive joint test: either derive the complete action, or construct an explicit counterexample family satisfying the newly derived representation-valued law while differing on the joint extension, or otherwise prove insufficiency from the frozen object.
5. If that repair requires new source/realization inputs, a new prospectively frozen gate is required; history must not be rewritten.
6. Iter504 and Iter461 remain non-terminal and untouched.

## UPDATED_STATE

`SOURCE_J1_K5_ONE_WEDGE_CONJUGATION_MAP = CONFIRMED_SCOPED_SUBRESULT`

`SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_JOINT_EXTENSION_ACTION_BLOCKED_SCOPED = INVALID_IMPLEMENTATION`

Authoritative provenance retained:

- prereg: `93f03b5f1458ad49f80065c959e596c0ac19039a`;
- code: `4b7ce62af6f543667a2dbfab36c2573998897756`;
- workflow/production: `ec5571545ff20b4eb6e22c0b41f783d0a7722839`;
- Actions run: `34923962807`;
- artifact: `10379315977`;
- artifact digest: `sha256:c3b5563448613c944f9d7cbbe000331525da35a0704d811b17f1019d3cb5f2d6`;
- canonical result: `a1c99c68bece189173d47e2624dface914aa709a`;
- historical terminal Research result remains unchanged at `181ca68f524fee5d9eab1c9501142d409cd02c2b`.

Governance remains:

- `RQIR Core v1.0 = FROZEN`;
- `D7-S2 = NOT_CLOSED`;
- `D7-S3 = NOT_CLOSED`;
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`;
- terminal D7 labels and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden;
- Candidate Gravity remains inactive;
- BLOCKED/INVALID remains distinct from scientific FAIL.

## NEXT_ADMISSIBLE_GATE

Do not reuse the present `BLOCKED_SCOPED` classification as an input fact.

Run a new prospectively frozen joint-action gate if additional source/realization authority is needed. At minimum it must freeze before computation:

1. the complete fixed-channel vertex contraction/intertwiner realization needed to propagate the derived `C` action through the K5 network;
2. the exact action on the collision-supported distribution/jet basis;
3. the already derived one-wedge map `conj(T_plus)=C T_minus C` with unchanged rho as an upstream premise rather than a result to be rediscovered;
4. the frozen `+i/-i/0` witness;
5. an outcome-sensitive decision procedure that can genuinely return witness `PRESERVED`, `EXCLUDED`, or `BLOCKED` depending on the mathematics, rather than a hard-coded blocker;
6. explicit counterexample search for two distinct joint extensions that both satisfy the complete derived vertex-level conjugation law.

If all required inputs are already contained in the existing frozen authority and no new scientific input is introduced, a contract-faithful code repair may instead be preregistered as an implementation-repair gate. Any change to source/realization authority, object, witness, or decision rule requires a new prospective preregistration.
