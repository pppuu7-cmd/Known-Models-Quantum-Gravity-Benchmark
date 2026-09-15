# Preregistration — published i-epsilon scope / joint-regulator authority gate

Date: 2026-09-15
Status: `PROSPECTIVELY_FROZEN_SOURCE_AUDIT`

## HYPOTHESIS

The published causal-vertex definition of Bianchi, Chen and Gamonal supplies a Feynman `i epsilon` prescription for each **single Toller matrix**, but the displayed causal-vertex definition does not itself introduce a common ten-wedge positive-regulator family or an ordered ten-regulator limit across the correlated K5 group integral.

Therefore the one-wedge `i epsilon` representation may not be promoted, without a further theorem/construction, to a joint K5 collision-extension prescription that resolves the full-collision product problem.

This is a source-authority/scope gate. It does not test whether such a joint limit exists mathematically.

## PRIMARY SOURCE AUTHORITY

Bianchi, Chen and Gamonal, *Causal spinfoam vertex for 4D Lorentzian quantum gravity*, arXiv:2601.23162 / Phys. Rev. D 113, 126020 (2026).

Frozen source locations:

- Eq. (3): definition of one Toller matrix by `lim_{epsilon->0+}` of a spectral integral in `tilde rho`;
- text immediately after Eq. (3): one Toller matrix is associated to each wedge;
- Eq. (4): causal vertex is the four-group integral of the product of ten Toller matrices;
- Eq. (5): exact one-wedge additive relation `T+ + T- = D`;
- Discussion item ii: finiteness of the causal model must be investigated again because Toller poles may lead to new divergences;
- Eq. (17): coherent one-wedge realization contains `theta(kappa B)+kappa delta^(rho,j)(B)`.

Primary public HTML authority pinned by equation number:
`https://arxiv.org/html/2601.23162`.

## OBJECT

Audit only the published single-vertex definition in Eqs. (3)-(4), plus the explicit finiteness statement in the Discussion.

Do not infer from silence outside this scope that no alternative joint construction exists in unpublished work, a companion paper, or future literature.

## CHECKS

### Positive source checks

1. Eq. (3) contains an explicit `lim_{epsilon->0+}` inside the definition of a single `T^(+/-)` matrix.
2. The regulator in Eq. (3) acts in the one-wedge spectral integration variable `tilde rho`.
3. The text associates one already-defined Toller matrix to each wedge.
4. Eq. (4) is written as a group integral of `prod_ab T_ab` and displays no common `epsilon`, vector `epsilon_ab`, regulator path, or order of regulator removal.
5. Eq. (4) is explicitly stated to define the fixed-causal-structure vertex amplitude.
6. The Discussion explicitly says the finiteness question for the causal model must be investigated again to check whether Toller poles introduce new divergences.
7. Eq. (17) contains source-defined one-wedge distributional contact terms, so the audit must not misclassify a one-wedge distribution as unspecified.

### Adversarial controls

1. Do **not** classify absence of an explicit joint regulator in Eq. (4) as proof that Eq. (4) has no mathematical meaning.
2. Do **not** classify open finiteness as proof of divergence.
3. Do **not** claim that a common-regulator family would be source-equivalent unless equivalence is separately proved.
4. Do **not** claim that independent wedge regulators are source-authorized merely because Eq. (3) uses an `epsilon` symbol per one-wedge formula.
5. Preserve the exact one-wedge identity `T+ + T- = D` as established source authority.

## PASS

Classify

`SOURCE_CAUSAL_VERTEX_PUBLISHED_IEPSILON_IS_ONE_WEDGE_NOT_JOINT_COLLISION_REGULATOR_SCOPED`

iff checks 1-7 are verified from the primary published/arXiv source.

Interpretation ceiling:

- the published `i epsilon` representation fixes the individual Toller matrices;
- the displayed vertex formula then multiplies those Toller matrices under the correlated group integral;
- the displayed definition does not itself provide a ten-wedge prelimit regulator path/order that can be cited as a ready-made theorem resolving the K5 collision extension problem;
- because the paper itself leaves causal-vertex finiteness open, KMQGB must prove the group-integral/product issue rather than treating one-wedge `i epsilon` as automatic closure.

PASS does **not** imply that Eq. (4) is ill-defined, divergent, non-renormalizable, or that no canonical source-compatible extension exists.

## FAIL

Classify

`SOURCE_CAUSAL_VERTEX_PUBLISHED_JOINT_COLLISION_REGULATOR_EXPLICITLY_SPECIFIED`

iff the frozen source definition itself explicitly supplies a ten-wedge correlated positive-regulator family plus its regulator-removal prescription across the group integral, sufficient to identify the collision extension without adding new source data.

## BLOCKED / INVALID

`INVALID_SOURCE_AUDIT` if conclusions are based on secondary summaries rather than the frozen primary equations/discussion, or if the gate confuses one-wedge spectral regulation with group-collision regularization.

## CONSEQUENCE

On PASS, split the broad `SOURCE_J1_K5_JOINT_FEYNMAN_REGULATOR_EXTENSION_GATE` into two explicit tasks:

1. `SOURCE_J1_K5_EQ4_IMPROPER_DISTRIBUTIONAL_EXISTENCE_GATE` — does Eq. (4), with the already-defined Toller factors, exist in the source-prescribed sense at the K5 collisions?
2. `SOURCE_J1_K5_ADDITIONAL_JOINT_REGULATOR_EQUIVALENCE_GATE` — only if needed, construct a prospective common/independent regulator family and prove it converges to the same source object rather than silently defining a new model.

This separation prevents an auxiliary regulator invented by KMQGB from being mistaken for part of the published model.

## GOVERNANCE

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors forbidden.
- Candidate Gravity inactive.
- KMQGB remains downstream of pinned DSIR authority.
