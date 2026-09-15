# Prospective preregistration — source j=1 K5 joint Feynman regulator extension gate

Date: 2026-09-15
Gate: `SOURCE_J1_K5_JOINT_FEYNMAN_REGULATOR_EXTENSION_GATE`
Status: `PROSPECTIVELY_FROZEN_BEFORE_IMPLEMENTATION_OR_RESULT`

## HYPOTHESIS

For the source-defined `j=1`, real nonzero-`rho`, source-order K5 causal object, the one-wedge Feynman `i epsilon` projectors defining the Toller branches may or may not extend to a unique correlated ten-wedge distribution through the full-K5 collision. One-wedge existence/uniqueness is not sufficient: the gate tests the joint regulator-removal limit, common-versus-independent regulator paths, collision-supported ambiguity, and preservation of the exact source identity `T+ + T- = D` at the correlated level.

## OBJECT

The exact target is the correlated ten-wedge source-order K5 distribution in the frozen `j=1`, real nonzero-`rho` sector, localized at the previously certified full-K5 collision chart. Each wedge is regulated by the source Feynman projector before regulator removal. The gate distinguishes:

1. the regulated object for strictly positive regulator vector `epsilon = (epsilon_1,...,epsilon_10)`;
2. the common path `epsilon_1=...=epsilon_10=epsilon -> 0+`;
3. independent positive paths `epsilon_e -> 0+` with arbitrary relative rates/order;
4. the resulting action on a prospectively frozen compactly-supported test-function class in the 12 normal coordinates of the full-K5 collision chart.

This gate does not replace the unresolved coherent-contact -> magnetic/intertwiner transfer. It acts at the source-defined distribution/regulator level and may terminate BLOCKED if the frozen source authority does not determine the correlated action.

## DEPENDENCY

Frozen repository authority at registration:

- terminal coherent-contact Hörmander result `research/SOURCE_J1_K5_COHERENT_CONTACT_HORMANDER_RESULT_2026-09-15.md`;
- terminal contact-representation derivation V2 result `results/SOURCE_J1_K5_CONTACT_REPRESENTATION_DERIVATION_V2_TERMINAL_2026-09-15.md`, commit `db8fbcc72c9b8397b42a96d0cc23cd0fed5c3e83`;
- exact source identity controls from the Iter503D line (`T+ + T- = D` and derivative identity);
- independent Iter461 K5 lower-collision-partition stream remains nonterminal unless a later authoritative repo result says otherwise;
- independent Iter504 centered full-max-envelope science campaign remains nonterminal unless a later authoritative repo result says otherwise.

External primary authority is frozen by version, not by moving web content:

- Bianchi, Chen, Gamonal, `Toller matrices and the Feynman i epsilon in spinfoams`, arXiv:2604.24945v1 (2026-04-27), especially the reduced Toller Feynman projector definitions/equations (17)-(20), their one-wedge contour argument, and the uniqueness statement following Eq. (20).
- Bianchi, Chen, Gamonal, `Causal spinfoam vertex for 4d Lorentzian quantum gravity`, arXiv:2601.23162, for the causal-vertex use of Toller matrices and the additive identity.

No later paper revision may enter this gate without a new preregistration or an explicit provenance-only supplement made before substantive calculation.

## SOURCE / REALIZATION AUTHORITY

The frozen external source establishes, at one-wedge reduced-matrix level:

- a Feynman `i epsilon` functional acting in the spectral variable;
- recovery of the `+` and `-` Toller branches in the `epsilon -> 0+` limit;
- the additive relation `T+ + T- = D`;
- uniqueness of the admissible one-wedge Toller splitting under the stated analyticity/asymptotic/pole assumptions;
- a specific phase convention (Ruhl convention), with other spinfoam conventions differing by a nontrivial `rho`-dependent phase.

These facts do **not** by themselves authorize exchanging ten regulator limits with K5 group integrations, multiplying singular boundary values through the full collision, or asserting path/order independence. Those are exactly the new questions tested here.

## FROZEN INPUTS

The implementation must freeze and emit hashes/identifiers for every local dependency used and must hard-code the external authority identifiers above.

Scientific inputs:

- sector: `j=1`, real `rho != 0`;
- source-order K5 with ten wedges;
- full-K5 collision normal chart of dimension 12 from the frozen coherent-contact analysis;
- all ten causal branch signs are retained as source data; no post-hoc branch deletion is allowed;
- regulator vector is strictly positive before removal;
- common-regulator and independent-regulator limits are distinct frozen tests;
- exact identity `T+ + T- = D` is a mandatory joint-level control, not an optional diagnostic.

The exact compactly-supported test-function family and any finite symbolic/numerical witness set must be committed in a protocol supplement before implementation. A finite witness may falsify path independence but may not prove universal existence by sampling alone.

## POSITIVE CONTROLS

1. **ONE_WEDGE_PROJECTOR_CONTROL** — reproduce the frozen one-wedge Feynman projector relation for a source-authorized reduced Toller matrix without changing phase convention.
2. **ADDITIVE_IDENTITY_CONTROL** — verify `T+ + T- = D` before and after every regulated operation for which both sides are defined.
3. **TRANSVERSAL_TOY_CONTROL** — a prospectively frozen distributional toy product with transversal singular supports and known path-independent limit must be accepted by the same limit-comparison machinery.
4. **REGULATOR_POSITIVITY_CONTROL** — no evaluation with nonpositive regulator is admissible as scientific evidence.

## NEGATIVE / ADVERSARIAL CONTROLS

1. **PATH_DEPENDENCE_TOY** — a prospectively frozen singular toy family with different common-versus-independent removal limits must be detected as path dependent.
2. **ORDER_SWAP_CONTROL** — if iterated independent limits depend on order, the implementation must report the mismatch rather than average it away.
3. **PHASE_CONVENTION_GUARD** — changing from the frozen Ruhl phase convention without an explicit exact transform must invalidate the affected calculation.
4. **PRODUCT_EXISTENCE_GUARD** — existence of all ten one-wedge limits must not be mechanically promoted to existence of their correlated product.
5. **REPRESENTATION_TRANSFER_GUARD** — the cubic-pole `Q=diag(1,-2,1)` / `11/24` witness and any unpinned coherent-to-magnetic map are forbidden substitutes for the source-defined joint regulator object.

## TERMINAL CLASSIFICATIONS

### PASS — `JOINT_FEYNMAN_EXTENSION_PATH_INDEPENDENT_SCOPED`

Allowed only if all source locks and controls pass, the correlated regulated K5 object is well-defined for the frozen positive-regulator domain, the regulator-removal limit exists on the frozen test-function class, common and all prospectively frozen independent/order paths agree, collision-supported ambiguity is absent within the frozen class, and the exact joint `T+ + T- = D` control is preserved.

PASS is scoped evidence only. It does not by itself close lower collision strata, D7-S2, D7-S3, D7-S4, or authorize a terminal selector.

### SCIENTIFIC FAIL — `JOINT_FEYNMAN_EXTENSION_PATH_DEPENDENT_SCOPED`

Allowed if all source locks/controls pass and two prospectively frozen admissible regulator-removal paths or orders yield demonstrably different distributional limits on the same frozen test function, or one admissible path has a limit while another does not.

This is a failure of path independence for the tested source regulator prescription in this scope; it is not a model/family FAIL and is not permission to tune the prescription after seeing the result.

### BLOCKED — `JOINT_FEYNMAN_EXTENSION_AUTHORITY_BLOCKED_SCOPED`

Allowed if controls/source locks pass but the frozen source authority is insufficient to define the ten-wedge regulated correlated action, the required test-function pairing, or the regulator/group-integration ordering without adding new model data or an unproved representation transfer.

BLOCKED != FAIL.

### INVALID — `JOINT_FEYNMAN_EXTENSION_INVALID_IMPLEMENTATION`

Required for source-lock failure, convention drift, use of partial/nonterminal Iter461 or Iter504 values, post-hoc path/test-function selection, silent branch deletion, failure of a positive/negative control, or any implementation whose terminal label is not mechanically connected to the frozen calculations.

## INTERPRETATION CEILING

The gate asks whether the **source Feynman prescription itself** canonically resolves the correlated full-K5 collision in the frozen sector. Even a PASS does not establish ordinary absolute convergence, all-spin/all-channel convergence, lower-collision closure, family sufficiency, or any final RQIR selector. A path-dependence FAIL establishes only the scoped nonuniqueness of regulator removal under the frozen prescription. BLOCKED establishes only insufficient frozen authority/definition.

Governance remains:

- `RQIR Core v1.0 = FROZEN`;
- `D7-S2 = NOT_CLOSED`;
- `D7-S3 = NOT_CLOSED`;
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`;
- terminal D7 selectors remain forbidden;
- Candidate Gravity remains inactive;
- KMQGB remains downstream of pinned DSIR authority.
