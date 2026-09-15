# Preregistration — Eq. (4) local full-collision extension existence versus uniqueness

Date: 2026-09-15
Status: `PROSPECTIVELY_FROZEN`

## HYPOTHESIS

For the already reviewed fixed source-order `j=1`, channel-`00000` full-collision witness, restricted to the compact-base/tangent conic patch that excludes lower pair-collision directions:

1. the punctured source product has finite transverse scaling degree `30` relative to the codimension-`12` full-collision submanifold;
2. therefore a local distributional extension across that full-collision submanifold **exists** with the same scaling degree;
3. such an extension is not fixed uniquely by off-collision agreement and the scaling-degree bound because `30 >= 12`, with normal ambiguity order through `18`;
4. the already certified `delta_N` sign-family witness shows that adding the exact EPRL independent-sign sum rule and K5 permutation covariance still does not remove all collision-supported freedom.

The target classification is therefore existence-positive but uniqueness-open, not a divergence/nonexistence verdict.

## AUTHORITY

### Source model

Bianchi, Chen and Gamonal, *Causal spinfoam vertex for 4D Lorentzian quantum gravity*, especially Eqs. (3)-(6), (17) and the Discussion finiteness item.

### Extension theorem

Use the finite-scaling-degree extension theorem for distributions at a point/submanifold as stated in Brunetti and Fredenhagen, *Microlocal Analysis and Interacting Quantum Field Theories: Renormalization on Physical Backgrounds*, Commun. Math. Phys. 208 (2000) 623-661, arXiv:math-ph/9903028.

Frozen theorem use:

- finite scaling degree implies existence of an extension preserving the scaling degree;
- uniqueness holds automatically only below the transverse codimension;
- for scaling degree at or above codimension, differences of same-scaling extensions are collision-supported finite normal jets, bounded by the singular order `floor(sd-codim)` in this integer case.

### Repository premises

- `research/SOURCE_J1_FULL_COLLISION_ABSOLUTE_DIVERGENCE_THEOREM_2026-09-15.md`;
- `research/SOURCE_J1_FULL_COLLISION_SCALING_EXTENSION_AUDIT_2026-09-15.md`;
- `research/SOURCE_J1_K5_PUBLISHED_IEPSILON_SCOPE_RESULT_2026-09-15.md`;
- `research/SOURCE_J1_K5_COLLISION_COUNTERTERM_SUMRULE_RESULT_2026-09-15.md`.

Frozen exact premises:

- transverse scaling degree `sd_N=30`;
- full-collision normal codimension `12`;
- singular order `30-12=18`;
- zeroth-order `delta_N` has scaling degree `12 <= 30`;
- explicit K5 sign-family coefficients `+63` on 16 constrained patterns and `-1` on 1008 unconstrained patterns preserve the full EPRL sign sum while shifting the causal sector.

## OBJECT

Exactly the same scoped object as the reviewed full-collision theorem:

- source-order causal vertex;
- fixed `j=1`;
- fixed nonzero real edge `rho_e`;
- frozen causal signatures only as already covered by the source theorem;
- allowed intertwiner channel `00000`;
- full compact collision submanifold `N=K^4`, `K=SU(2)`, in the gauge-fixed `G^4`, `G=SL(2,C)`;
- compact tangential base and a normal conic patch around the exact rational witness;
- patch chosen away from lower pair-collision subcones.

This gate is local in the full-collision normal direction. It is not a global definition of the entire vertex and does not consume Iter461.

## POSITIVE CONTROLS

1. `sd_N=30` is finite.
2. `codim(N)=12`.
3. radial absolute-integrability exponent remains `-19`, so ordinary absolute integration is not being confused with distributional extension existence.
4. singular order is exactly `18`.
5. `sd_N >= codim(N)`, so the theorem does not grant uniqueness.
6. `sd(delta_N)=12 <= 30`, so the explicit zeroth-order ambiguity witness is allowed within the same scaling ceiling.
7. the EPRL-preserving coefficient witness has exact full sign sum zero and nonzero causal shift.
8. the published one-wedge `i epsilon` is not silently treated as an already-proved joint collision normalization.

## ADVERSARIAL CONTROLS

1. The gate must reject the false implication `absolute divergence => no distributional extension`.
2. The gate must reject the false implication `extension exists => source uniquely defines it`.
3. The gate must reject promotion from the conic full-collision patch to lower/nested collision strata.
4. The gate must reject promotion from fixed `j=1`, channel `00000` to all channels/spins.
5. The gate must not introduce an auxiliary common regulator and call it part of the published model.

## PASS

Classify

`SOURCE_J1_K5_EQ4_LOCAL_EXTENSION_EXISTS_UNIQUENESS_OPEN_SCOPED`

iff all premises and controls pass.

Interpretation ceiling of PASS:

- on the frozen conic full-collision patch, there exists at least one distributional extension of the punctured source product with the frozen scaling degree;
- ordinary absolute Haar divergence therefore does not imply nonexistence as a distribution;
- uniqueness is not supplied by off-collision agreement + scaling ceiling + EPRL sign sum + K5 permutation covariance;
- an additional source-faithful joint-limit/normalization condition is required to select a unique causal extension.

PASS does **not** prove that the published Eq. (4) is globally well-defined or globally ambiguous.

## FAIL

Classify

`SOURCE_J1_K5_EQ4_LOCAL_EXTENSION_EXISTENCE_NOT_CERTIFIED`

iff the frozen object does not satisfy the hypotheses of the finite-scaling-degree extension theorem on the stated conic patch.

## BLOCKED / INVALID

- `INVALID_THEOREM_APPLICATION` if lower collision strata are present in the patch or the starting punctured distribution is not defined on the punctured normal domain.
- `INVALID_SCOPE_PROMOTION` if the result is generalized beyond the frozen spin/channel/patch.

## CONSEQUENCE

On PASS, the remaining full-collision task is narrowed from existence to **source-canonical selection**:

`SOURCE_J1_K5_EQ4_SOURCE_NORMALIZATION_SELECTION_GATE`.

That gate must identify a source-derived condition stronger than the already-insufficient set

- off-collision agreement;
- same scaling degree;
- K5 permutation covariance;
- EPRL independent-sign sum rule,

and prove that it eliminates the explicit collision counterterm family.

Separately, lower K5 collision strata remain dependent on unresolved Iter461.

## GOVERNANCE

- `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- terminal D7 selectors forbidden.
- Candidate Gravity inactive.
- KMQGB remains downstream of pinned DSIR authority.
