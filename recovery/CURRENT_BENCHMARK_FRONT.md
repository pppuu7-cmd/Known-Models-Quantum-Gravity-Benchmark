# KMQGB Current Benchmark Front

**Updated:** 2026-09-08  
**KMQGB iteration:** 031  
**Repository:** `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`  
**Branch:** `main`  
**Phase:** WAVES 1–8 TERMINALLY CLASSIFIED / RESIDUAL-SPACE GEOMETRY FROZEN

## Coverage

- Wave 1: **9/9 = 100%** — immutable.
- Wave 2: **5/5 = 100%** — immutable.
- Wave 3: **5/5 = 100%** — immutable.
- Wave 4: **5/5 = 100%** — immutable.
- Wave 5: **5/5 = 100%** — immutable.
- Wave 6: **5/5 = 100%** — immutable.
- Wave 7: **5/5 = 100%** — immutable.
- Wave 8: **5/5 = 100%** — immutable.
- Globally authorized robust unique-QG residuals: **0**.
- External Candidate Gravity readiness: **24%**.

## Wave 8 terminal result — residual-space geometry

All five methodology targets are `PASS_RQIR_GATE`.

The benchmark now defines novelty through the **Comparator-Orthogonal Residual (COR)** rather than a qualitative feature label.

For physical residual `r`, covariance `Sigma`, and union comparator Jacobian `J_C`, whiten

`z=Sigma^(-1/2)r`, `A=Sigma^(-1/2)J_C`.

Then

`Pi_perp=I-AA^+`,

`COR=Pi_perp z`.

For candidate signal direction `s`,

`eta(s)=||Pi_perp Sigma^(-1/2)s|| / ||Sigma^(-1/2)s||`.

`eta=0` means exact local tangent degeneracy. Nonzero `eta` is only a local prefilter and must survive finite/global profiling.

Authoritative protocol: `protocol/RESIDUAL_SPACE_GEOMETRY.md`.

Reference implementation: `code/residual_space_geometry_reference.py`.

A deterministic numerical self-test found machine-precision behavior for projector idempotence, tangent annihilation and nuisance reparameterization invariance.

## Constraints-first rule

Exact Ward/contact/gauge/physical constraints are quotiented **before** comparator rank counting.

Frozen order:

`physical constraints -> physical observable basis -> comparator/nuisance quotient`.

## Nuisance attribution geometry

Use a joint tangent matrix

`J=[J_dyn J_state J_detector J_cal J_mediator ...]`.

The final novelty verdict uses the joint span. Block ranks/principal angles only diagnose which attribution layer absorbs the signal.

## Nonlinear/global gate

A local COR must survive

`d_C^2(y)=inf_theta [y-c(theta)]^T Sigma(theta)^(-1)[y-c(theta)]`

inside the prospective common domain.

For theory-family separation,

`d_min^2=inf_(lambda,theta)||Sigma^(-1/2)[k(lambda)-c(theta)]||^2`.

## Future KG parameter identifiability

For a future KG Jacobian `J_KG`, freeze

`B_KG=Pi_perp Sigma^(-1/2)J_KG`.

Only singular directions of `B_KG` with nonzero robust singular values are candidates for Fisher/resources after global profiling.

## RQIR COR pre-registration

Created `protocol/RQIR_COR_APPLICATION_PRECHECK.md`.

Latest external RQIR scientific authority directly observed: **Iteration 587**, `MODEL_READINESS=24%`.

- Iter424 physical gate `5/5 PASS`;
- Iter581 exact15 raw-valid PASS;
- Iter582 supplies three q2-resolved operator buckets but **no Source/Born subtraction yet**;
- Iter584 mixed K2 is raw-valid according to Iter587 authority;
- Iter586 proves off-shell source completion is required for the timelike buckets;
- Iter587 raw-validates the symmetric off-shell K1 routing and exact Ward longitudinal term.

Exact external next gate: construct complete K1-exchange + K2-contact MSSC source Ward object before mapping to Iter582 and comparator subtraction.

KMQGB therefore does **not** treat Iter582 operator values as residual data.

If the future matched residual is an imaginary-only three-bucket vector, then `m_phys<=3` and

`dim local comparator complement = 3-rank(A_union)`.

If the union comparator tangent reaches rank 3, no local residual direction exists in those three coordinates regardless of numerical precision. Cross-order/cross-attribution augmentation is then mandatory.

## Shared runner status

Direct GitHub Actions checks at this iteration found no `in_progress` and no `queued` RQIR runs. The runner appears free, but KMQGB has no justified heavy numerical target yet, so no heavy job was launched merely to consume compute.

## Exact next KMQGB front

Construct **optimal comparator-annihilating contrasts** and observable-design criteria:

1. left-nullspace contrasts `w^T J_C=0`;
2. covariance-optimal contrast for a proposed signal;
3. exact dimension/rank gain from adding cross-order observables;
4. correlated-noise/common-mode rejection;
5. projected singular-value design criterion for selecting the most informative future KG observable set.
