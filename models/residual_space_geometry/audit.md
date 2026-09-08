# T8 Audit — Comparator Residual-Space Geometry

Benchmark family: `KMQGB-T8-RESIDUAL-GEOMETRY`

State: TERMINAL METHODOLOGY

Authoritative protocol: `protocol/RESIDUAL_SPACE_GEOMETRY.md` (`KMQGB-RSG-001`).

## T8-01 — whitened comparator tangent projector

State: `PASS_RQIR_GATE`.

For physical observable residual `r`, covariance `Sigma`, and comparator Jacobian `J_C`, whiten

`z=Sigma^(-1/2) r`, `A=Sigma^(-1/2)J_C`.

Freeze

`COR=(I-AA^+)z`.

For a candidate signal direction `s`, freeze

`eta(s)=||(I-AA^+)Sigma^(-1/2)s|| / ||Sigma^(-1/2)s||`.

`eta=0` is exact local tangent degeneracy. Nonzero `eta` is only local distinctness, not yet a robust residual.

## T8-02 — physical constraint quotient first

State: `PASS_RQIR_GATE`.

Exact Ward/contact/gauge/constraint relations must be removed **before** comparator rank counting.

For linear `L y=0`, use a basis `Z` of `ker L` and profile only in the physical coordinates. Do not count gauge-null/contact-null directions as observable novelty.

Frozen order:

`exact physical constraints -> physical basis -> comparator/nuisance quotient`.

## T8-03 — nuisance-block attribution geometry

State: `PASS_RQIR_GATE`.

Partition the tangent space into dynamics/state/detector/calibration/mediator/etc. blocks.

The final verdict uses their **joint span**, because sequential projections can be order dependent when blocks overlap.

Blockwise ranks/principal angles are retained only to diagnose **which attribution layer** absorbs a candidate direction.

This turns the qualitative attribution stack into a quantitative tangent-space ledger.

## T8-04 — nonlinear comparator-manifold robustness

State: `PASS_RQIR_GATE`.

A locally transverse COR may disappear after finite motion along a curved comparator manifold.

Freeze the common-domain global profile distance

`d_C^2(y)=inf_theta [y-c(theta)]^T Sigma(theta)^(-1)[y-c(theta)]`

with validity, state, detector and nuisance bounds included prospectively.

For theory-family separation, use

`d_min^2=inf_(lambda,theta) ||Sigma^(-1/2)[k(lambda)-c(theta)]||^2`

only in a truly common domain.

Second-order curvature/Hessian and multiple minima/boundaries must be audited when relevant.

## T8-05 — promotion certificate

State: `PASS_RQIR_GATE`.

Before a future KG ansatz may advance from design hypothesis to candidate residual, require:

1. physical constraint basis frozen;
2. common validity domain frozen;
3. full applicable same-order C5 included;
4. full comparator/nuisance union included;
5. field-redefinition/representation duplicates removed;
6. nonzero local comparator-orthogonal direction;
7. finite/global profiling does not absorb it;
8. stability under declared state/detector/calibration ranges;
9. at least two attribution layers linked by the residual;
10. Ward/contact/causal/relational constraints preserved;
11. statistical calibration performed correctly if data are used;
12. only then Fisher/resources.

For a concrete future KG parameter Jacobian `J_KG`, define

`B_KG = Pi_perp Sigma^(-1/2) J_KG`.

Its singular values diagnose parameter combinations identifiable **after** comparator profiling.

## Terminal rollup

All five T8 methodology targets: `PASS_RQIR_GATE`.

No physical Candidate Gravity residual is created by these passes.

## Main design consequence

The model-building question is now mathematically precise:

> Find an observable relation whose image has finite distance from the full physical comparator manifold after constraints, state/detector nuisance, full-C5 and attribution profiling.

Symbolically,

`Delta_KG^robust = inf_(C in comparator union) distance_W(O_KG,M_C) > 0`.

No such positive lower bound is currently established.
