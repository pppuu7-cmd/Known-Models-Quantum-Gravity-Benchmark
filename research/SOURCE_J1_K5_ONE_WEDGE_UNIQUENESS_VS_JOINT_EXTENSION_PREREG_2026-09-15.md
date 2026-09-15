# Preregistration — one-wedge Toller uniqueness versus joint K5 collision extension

Date: 2026-09-15
Status: `PROSPECTIVELY_FROZEN`

## HYPOTHESIS

The published uniqueness theorem for each individual reduced Toller matrix does not, by itself, uniquely fix the extension of the correlated ten-wedge product across a K5 full-collision stratum.

Reason to test: the one-wedge theorem constrains each factor `T_e` separately in its own Lorentz-group variable/representation data, while the already certified ambiguity witness changes only the **joint extension** of the ten-factor product by a distribution supported on the common collision submanifold `N`. Such a joint collision-supported term can leave every individual factor exactly unchanged.

The gate is a logical/source-scope independence test. It does not assert that no stronger source-derived joint normalization exists.

## PRIMARY SOURCE AUTHORITY

Bianchi, Chen and Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, arXiv:2604.24945 / Phys. Rev. D 114, 046014 (2026).

Freeze the published one-wedge theorem for `beta>0`:

1. Ruhl's functions of the second kind exist and are unique.
2. The reduced Toller matrices are uniquely characterized by their one-wedge asymptotic properties, matching properties, meromorphic Toller-pole structure, and the additive rule `t^+ + t^- = d`.
3. The paper proves that the one-wedge Feynman `i epsilon` contour prescription extracts these unique branches and is equivalent to the analytic definition.
4. The full Toller `T` matrices are then built from the unique reduced `t` matrices by Cartan decomposition.

Relevant published equations/locations:

- Eqs. (5)-(12): one-wedge functions of the second kind and uniqueness data;
- Eqs. (13)-(15): full one-wedge Toller matrices and additive relation;
- Sec. III.1 / Eqs. (16)-(20): one-wedge Feynman `i epsilon` representation establishing the same branch selection.

## REPOSITORY AUTHORITY

- `research/SOURCE_J1_K5_PUBLISHED_IEPSILON_SCOPE_RESULT_2026-09-15.md`;
- `research/SOURCE_J1_K5_EQ4_LOCAL_EXTENSION_EXISTENCE_RESULT_2026-09-15.md`;
- `research/SOURCE_J1_K5_COLLISION_COUNTERTERM_SUMRULE_RESULT_2026-09-15.md`.

Frozen joint-extension witness:

- local full-collision extension exists on the reviewed conic patch;
- same-scaling extension freedom contains zeroth-order `delta_N`;
- exact coefficient family `+63` on 16 constrained causal sign patterns and `-1` on 1008 unconstrained sign patterns preserves the full EPRL independent-sign sum while shifting the causal sector;
- K5 permutation covariance is preserved.

## OBJECT

Compare two levels of data without identifying them:

### Level W — one-wedge data

For every K5 edge `e`, keep the source Toller matrices `T_e^(+)` and `T_e^(-)` **identically unchanged**.

Therefore all one-wedge properties remain exactly unchanged:

- asymptotics in representation parameter;
- matching properties;
- Toller pole locations/residues encoded in the unique one-wedge function;
- `T_e^(+) + T_e^(-) = D_e`;
- the one-wedge Feynman `i epsilon` representation.

### Level J — joint product extension

Let `E_kappa` be any local extension of the punctured ten-wedge product for independent sign pattern `kappa` on the frozen conic full-collision patch.

Define a second extension family

`E'_kappa = E_kappa + c(kappa) delta_N`,

with the already frozen exact coefficients

- `c(kappa)=+63` on the 16 constrained K5 causal patterns;
- `c(kappa)=-1` on the other 1008 patterns.

No individual one-wedge Toller matrix is redefined in passing from `E` to `E'`.

## POSITIVE CONTROLS

1. All 10 individual wedge-factor pairs `(T_e^+,T_e^-)` are bit-for-bit/logically identical between extension families `E` and `E'`.
2. Therefore all one-wedge asymptotic, matching, pole, additive and Feynman-branch conditions have identical truth values for `E` and `E'`.
3. `E` and `E'` agree off the collision submanifold `N` because `delta_N` is supported on `N`.
4. Both stay within the frozen scaling-degree ceiling because `sd(delta_N)=12 <= 30`.
5. The exact full EPRL independent-sign counterterm sum remains zero.
6. K5 permutation covariance of the coefficient family remains exact.
7. The constrained causal sector shift remains nonzero (`1008` over distinct constrained patterns).

## ADVERSARIAL CONTROLS

1. If a proposed 'one-wedge uniqueness condition' explicitly depends on the joint ten-wedge distribution or on a collision-normalization functional, it is not a one-wedge condition and must be classified outside this gate.
2. The gate must not infer that `E'` is source-authorized; it is only an ambiguity witness compatible with the frozen one-wedge data.
3. The gate must not infer that no source-derived joint condition exists.
4. The gate must preserve the distinction between uniqueness of factors and uniqueness of their singular product.

## PASS

Classify

`SOURCE_J1_K5_ONE_WEDGE_TOLLER_UNIQUENESS_INSUFFICIENT_FOR_JOINT_EXTENSION_SCOPED`

iff all controls pass.

Interpretation ceiling:

- the companion-paper uniqueness theorem fully fixes each one-wedge Toller matrix but does not, by itself, eliminate the explicit joint collision-supported extension witness;
- therefore source-canonical uniqueness of Eq. (4) requires at least one condition that is genuinely joint in the ten wedge factors / four correlated group variables;
- repeating or strengthening only one-wedge analytic uniqueness arguments cannot close the full-collision product problem.

PASS does **not** prove that the published causal vertex is nonunique after all source conditions are imposed.

## FAIL

Classify

`SOURCE_J1_K5_ONE_WEDGE_TOLLER_UNIQUENESS_FIXES_JOINT_EXTENSION_WITNESS`

iff an actually published one-wedge uniqueness condition changes or constrains the joint collision counterterm coefficient while leaving all ten individual Toller matrices fixed.

Such a FAIL requires an explicit source equation/theorem, not an inference from terminology such as 'unique Toller matrix'.

## BLOCKED / INVALID

`INVALID_LEVEL_CONFLATION` if the implementation treats a condition on the joint product as though it were part of the one-wedge uniqueness theorem.

`BLOCKED_SOURCE_AUTHORITY` if the claimed one-wedge uniqueness theorem cannot be pinned to the published companion paper.

## CONSEQUENCE

On PASS, the authorized normalization frontier is narrowed to genuinely joint source data:

`SOURCE_J1_K5_EQ4_JOINT_NORMALIZATION_AUTHORITY_GATE`.

That gate must search/test conditions attached to the full vertex/product rather than to individual Toller factors, for example:

- a published joint limiting prescription;
- a vertex-level distributional identity;
- a joint Ward/gauge/causal normalization condition;
- or another explicit source theorem that acts on collision-supported terms.

An auxiliary KMQGB regulator is not source authority unless source-equivalence is separately proved.

## GOVERNANCE

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors forbidden.
- Candidate Gravity inactive.
- KMQGB remains downstream of pinned DSIR authority.
