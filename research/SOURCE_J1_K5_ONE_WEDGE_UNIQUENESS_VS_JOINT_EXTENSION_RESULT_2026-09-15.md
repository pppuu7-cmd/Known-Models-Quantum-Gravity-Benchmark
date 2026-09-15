# Terminal result — one-wedge Toller uniqueness versus joint K5 collision extension

Date: 2026-09-15
Status: `TERMINAL_SCOPED`
Classification: `SOURCE_J1_K5_ONE_WEDGE_TOLLER_UNIQUENESS_INSUFFICIENT_FOR_JOINT_EXTENSION_SCOPED`

## Frozen authority

- preregistration: `research/SOURCE_J1_K5_ONE_WEDGE_UNIQUENESS_VS_JOINT_EXTENSION_PREREG_2026-09-15.md`
- frozen prereg commit: `88c3d04a627b4cbef29c6b3246052a58508aaa0a`
- exact logical/arithmetic implementation: `code/source_j1_k5_one_wedge_uniqueness_vs_joint_extension_certificate.py`
- implementation commit: `fa97e038e5b417271dfc4a396c89f5fe2f1cce0d`
- workflow head: `082bbae295f857dd61af54479ded2ca6be0ed62e`

## Authoritative run

- workflow run: `34916807591`
- source-lock job: `104216105796`, success
- exact-certificate job: `104216135656`, success
- artifact: `10376397688`
- artifact name: `source-j1-k5-one-wedge-uniqueness-vs-joint-extension`
- artifact digest: `sha256:dc7780208270cdcbb623171914ee86936523f245d7c4c509f018a72a62b1e8a1`

## Published one-wedge authority

Bianchi, Chen and Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, arXiv:2604.24945 / Phys. Rev. D 114, 046014 (2026), states for `beta>0` that Ruhl's functions of the second kind exist uniquely and that the reduced Toller matrices are uniquely characterized by their one-wedge asymptotic, matching and meromorphic pole properties together with the additive sum rule. The Feynman `i epsilon` contour representation extracts the same unique one-wedge branches.

This result fully respects that theorem. No individual Toller matrix is altered.

## Exact certified level separation

The certificate compared two local joint-extension families `E` and `E'` while keeping all ten one-wedge factor pairs exactly identical.

Certified controls:

- one-wedge factor count = `10`;
- all one-wedge factors identical between `E` and `E'` = `true`;
- individual factors modified = `false`;
- one-wedge uniqueness properties have identical truth values = `true`;
- joint difference is `c(kappa) delta_N`;
- joint difference is supported only on the full-collision submanifold `N`;
- off-collision restrictions of `E` and `E'` are identical;
- joint counterterm lies within the frozen scaling ceiling (`12 <= 30`);
- full EPRL independent-sign shift = `0`;
- constrained causal distinct-pattern shift = `1008`;
- sigma-counted causal shift = `2016`;
- all `122880` S5 pattern-permutation covariance checks pass.

The exact logical outputs are therefore:

- `one_wedge_uniqueness_truth_values_change = false`;
- `joint_extension_changes = true`;
- `one_wedge_uniqueness_alone_excludes_joint_counterterm = false`;
- `genuinely_joint_source_condition_required_for_uniqueness = true`.

## Scientific interpretation

Uniqueness of each source Toller factor and uniqueness of the singular correlated ten-factor product are distinct mathematical questions.

The published one-wedge theorem fixes every individual `T_e^(+/-)` but does not, by itself, constrain an additional distribution supported only where the ten already-fixed factors meet on the common K5 collision set.

Therefore repeating the one-wedge analyticity/asymptotics/pole/sum-rule argument cannot close the current Eq. (4) collision-extension uniqueness problem.

Any successful source-canonical uniqueness proof must contain at least one genuinely **joint vertex-level condition** acting on collision-supported terms.

## Claim ceiling

This result does **not** prove:

- that the published causal vertex is ultimately nonunique;
- that the explicit counterterm witness is source-authorized;
- that no vertex-level source identity or normalization exists;
- that an auxiliary regulator cannot be proved source-equivalent;
- closure of lower K5 collision strata;
- closure of D7-S2, D7-S3 or D7-S4;
- any terminal selector.

## Frontier consequence

Authorized analytical frontier:

`SOURCE_J1_K5_EQ4_JOINT_NORMALIZATION_AUTHORITY_GATE`

The search is now restricted to conditions genuinely attached to the full vertex/product, for example:

- a published joint limiting prescription;
- a vertex-level distributional identity;
- a joint gauge/causal normalization condition;
- a causal/co-causal relation acting on collision-supported terms;
- or another explicit source theorem that is not reducible to ten separate one-wedge uniqueness statements.

## Governance

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors remain forbidden.
- Candidate Gravity remains inactive.
- KMQGB remains downstream of pinned DSIR authority.
