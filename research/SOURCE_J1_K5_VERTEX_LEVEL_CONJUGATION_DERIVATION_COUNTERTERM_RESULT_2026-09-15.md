# Terminal result — source j=1 K5 vertex-level conjugation derivation / counterterm decision

Date: 2026-09-15
Status: `TERMINAL_BLOCKED_SCOPED`
Classification: `SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_JOINT_EXTENSION_ACTION_BLOCKED_SCOPED`

## Frozen authority

Prospective preregistration:

- `research/SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_DERIVATION_COUNTERTERM_PREREG_2026-09-15.md`
- preregistration commit: `93f03b5f1458ad49f80065c959e596c0ac19039a`

Recovery reconciliation before the gate:

- `recovery/KMQGB_RESEARCH_CLOSURE_FRONT_RECONCILIATION_2026-09-15T0306Z.md`
- reconciliation commit: `da4e3e0b648c8d1f458f327c573d049385836028`

Frozen code/workflow:

- certificate code: `code/source_j1_k5_vertex_conjugation_derivation_certificate.py`
- code commit: `4b7ce62af6f543667a2dbfab36c2573998897756`
- workflow: `.github/workflows/source-j1-k5-vertex-conjugation-derivation.yml`
- production/workflow commit: `ec5571545ff20b4eb6e22c0b41f783d0a7722839`

Canonical repository result:

- `results/source_j1_k5_vertex_conjugation_derivation_2026-09-15.json`
- canonical result commit: `a1c99c68bece189173d47e2624dface914aa709a`
- canonical result blob: `28afc5874e0f5c70f96e09de5e9b19b298287bf9`

## Actions provenance

Authoritative run:

- run `34923962807`
- head `ec5571545ff20b4eb6e22c0b41f783d0a7722839`
- overall Actions status: `completed`, conclusion `success`
- source-lock job `104237893942`: success
- certificate job `104237923698`: success
- artifact `10379315977`
- artifact name `source-j1-k5-vertex-conjugation-derivation`
- artifact digest `sha256:c3b5563448613c944f9d7cbbe000331525da35a0704d811b17f1019d3cb5f2d6`

Workflow color is not the science classification; the classification below follows the frozen preregistered decision rules and canonical certificate contents.

## Source-lock result

All six preregistered frozen blobs matched exactly in Actions:

1. `research/SOURCE_J1_K5_PUBLISHED_IEPSILON_SCOPE_RESULT_2026-09-15.md` -> `9a5531b6dbecc367c2869c6e9d873071a6444a66`.
2. `research/SOURCE_J1_K5_CAUSAL_COCAUSAL_CONJUGATION_AMBIGUITY_PREREG_2026-09-15.md` -> `de8916bb0444d54249ffa7ffc33553ff39d5db0f`.
3. `research/SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_AUTHORITY_RESULT_2026-09-15.md` -> `839f0ed038b60eb73dfbdc4738872d13fea2a352`.
4. `recovery/CRITICAL_REVIEW_SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_AUTHORITY_2026-09-15.md` -> `87a95edccb41ca2115ad0918b590d948bf4b9338`.
5. `code/iter456_reduced_toller_appendixb.py` -> `9626d52307763bc84c348110ed26db4a2b57b211`.
6. `code/iter457_toller_eq7_magnetic_reconstruction.py` -> `23d7108cd697012b2d9bb9ce3b2651d36b561e2b`.

The preregistration commit was verified as an ancestor of the production head before the certificate ran.

## Exact one-wedge derivation

The frozen finite candidate family had 256 possible reduced anti-linear maps of the form

`conj(t_plus_m(rho,beta)) = q_m t_minus_{s_m m}(s_r rho,beta)`

with `s_r=+/-1`, `s_m=+/-1`, and `q_m in {+1,-1,+i,-i}` for each of the three magnetic components.

Exactly one candidate survived the complete frozen numerical grid:

- `s_r = +1`;
- `s_m = -1`;
- `q_(+1)=q_0=q_(-1)=+1`;
- maximum reduced-grid relative residual `5.6089728176988790152404640942259946910897077121379e-81`.

Thus the derived reduced relation is

`conj(t_plus_m(rho,beta)) = t_minus_-m(rho,beta)`

for `m=+1,0,-1`, with **rho unchanged**.

This was not accepted on numerical fit alone: SymPy simplification against the explicit Iter456 source formulas returned exact symbolic zero independently for all three magnetic components.

The best rejected candidate in the frozen family had residual approximately `3.9201162702385955e-2`, so uniqueness on the frozen candidate class is strongly separated from the `1e-35` acceptance threshold.

## Exact magnetic / boundary-index map

In the Iter457 ordering `(+1,0,-1)`, the frozen j=1 conjugation matrix

`C = [[0,0,1],[0,-1,0],[1,0,0]]`

satisfies the exact symbolic Wigner identity

`conj(D^1(U)) = C D^1(U) C`.

Combining this with the reduced identity gives the full one-wedge representation-valued relation

`conj(T_plus(U1,beta,U2;rho)) = C T_minus(U1,beta,U2;rho) C`.

This relation fixes, within the frozen j=1 realization:

- branch: `plus -> minus` under complex conjugation;
- rho: `rho -> rho`;
- magnetic indices: `m -> -m` with the standard j=1 `C` action on the two matrix indices;
- no extra component phase beyond the `C` matrices.

Across all four frozen Iter457 angle lanes, seven rho values and five beta values, the certificate checked 140 full matrix points. Maximum full-matrix relative residual was

`5.0527970024459366808957170543113001311949532646006e-81`,

and maximum Wigner residual was exactly `0.0` in the numerical control.

## Frozen coefficient witness control

The earlier collision coefficient witness was rechecked without modification only as an adversarial consistency control:

- all 1024 wedge-sign patterns enumerated;
- `|C_+|=16`;
- `|C_-|=16`;
- `C_+ intersect C_- = empty`;
- `c(-kappa)=conj(c(kappa))` for all patterns;
- exact full EPRL counterterm coefficient sum `0+0i`.

This confirms that the earlier coefficient-level covariance is compatible with the now-derived exact one-wedge magnetic/rho conjugation map. It does **not** by itself promote the witness to a complete source-defined joint vertex counterterm.

## Joint-extension decision

The gate's second question was stricter: does the frozen source chain, together with the newly derived exact one-wedge map, uniquely determine the action on collision-supported **joint K5 extension terms** strongly enough to decide whether the frozen witness is source-allowed or source-excluded?

The answer is no within the frozen authority.

The upstream confirmed authority result already establishes that the source chain does not pin a joint collision-supported selection/normalization law. The present derivation supplies the previously missing one-wedge rho and magnetic/boundary-index anti-linear transformation, but it introduces no new joint regulator, no joint extension theorem, no regulator-removal order/path, and no independent source normalization acting on the collision-supported product distribution.

Therefore the exact one-wedge map cannot be promoted into a unique action on the joint extension solely from the frozen data.

## Frozen decision

All one-wedge derivation positive controls passed exactly, but the joint collision-extension action remains underdetermined by the frozen source chain.

According to the prospectively frozen BLOCKED criterion, the terminal classification is

`SOURCE_J1_K5_VERTEX_LEVEL_CONJUGATION_JOINT_EXTENSION_ACTION_BLOCKED_SCOPED`.

This is a **method/source-authority blocker**, not a scientific FAIL of the causal vertex and not a proof of physical nonuniqueness.

## New fact

The previously open rho/magnetic transformation question is now materially reduced: for the frozen j=1 source realization the exact one-wedge anti-linear map is

`conj(T_plus) = C T_minus C`, with `rho` unchanged.

Hence the remaining obstruction is no longer ignorance of the one-wedge representation-valued conjugation law. It is specifically the absence, in the frozen source chain, of a uniquely source-authorized action on the correlated collision-supported K5 extension/product distribution.

## Interpretation ceiling

This result does **not** establish:

- physical ambiguity or global nonuniqueness of the published causal vertex;
- nonexistence of a source-compatible joint extension;
- divergence or failure of Eq. (4) as a distribution;
- that the frozen `+i/-i/0` witness is physically realized;
- that the witness is eliminated;
- any all-spin, all-channel or all-collision-stratum theorem;
- closure of D7-S2, D7-S3 or D7-S4;
- any terminal D7 selector or `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` label;
- Candidate Gravity activation;
- `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

`BLOCKED_SCOPED` means only that the exact one-wedge transformation is insufficient to select the joint collision extension from the frozen source data.

## Open blockers / consequence

The next admissible high-information closure step should act directly on the remaining joint object rather than repeat one-wedge conjugation work. It should prospectively test whether the published source-order Eq. (4), together with its source-defined one-wedge boundary values, supplies a canonical **joint distributional product/extension rule** at the K5 collision without adding model data.

Recommended next gate:

`SOURCE_J1_K5_EQ4_JOINT_COLLISION_EXTENSION_SELECTION_GATE`.

It must distinguish at least:

1. a source-derived unique joint extension/limit;
2. multiple source-compatible extensions under the frozen one-wedge map;
3. absence of sufficient source data, classified `BLOCKED` rather than FAIL;
4. mathematical inconsistency, only if an actual contradiction is demonstrated.

Concurrent Iter504 run `34907349374` and Iter461 run `34748503239` were not consumed in this gate; no partial non-terminal substantive values entered the result.

## Governance

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors remain forbidden.
- Candidate Gravity remains inactive.
- historical FAIL/BLOCKED records are preserved.
