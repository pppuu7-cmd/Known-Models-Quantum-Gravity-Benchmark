# KMQGB Eighth Wave — Comparator Residual-Space Geometry

**Frozen denominator:** 5 methodology targets.  
**Historical waves 1–7:** terminal and immutable.  
**Eighth-wave terminal coverage:** **5/5 = 100%**.  
**Purpose:** replace qualitative novelty labels with a mathematically explicit comparator quotient and robust residual certificate before any Candidate Gravity ansatz.

| # | Target | Terminal status | Frozen result |
|---|---|---|---|
| T8-01 | whitened comparator tangent projector | `PASS_RQIR_GATE` | Comparator-Orthogonal Residual `COR=(I-AA^+)Sigma^(-1/2)r` and local separation `eta(s)` |
| T8-02 | Ward/constraint quotient before profiling | `PASS_RQIR_GATE` | exact physical constraints are removed before comparator rank/novelty counting |
| T8-03 | nuisance-block attribution geometry | `PASS_RQIR_GATE` | final verdict uses joint dynamics/state/detector/calibration/mediator tangent span; block projections are diagnostics only |
| T8-04 | nonlinear comparator-manifold robustness | `PASS_RQIR_GATE` | local tangent distinctness must survive finite/global common-domain profiling |
| T8-05 | promotion certificate | `PASS_RQIR_GATE` | singular-value and global-distance gates frozen before ansatz/Fisher/resources |

## Core local quotient

Let the physical observable vector be `y`, comparator `c(theta)`, residual `r=y-c(theta_*)`, covariance `Sigma`, and comparator Jacobian `J_C`.

Whiten

`z=Sigma^(-1/2)r`,

`A=Sigma^(-1/2)J_C`.

Then

`Pi_perp=I-AA^+`,

`COR=Pi_perp z`.

For a predicted signal direction `s`,

`eta(s)=||Pi_perp Sigma^(-1/2)s||/||Sigma^(-1/2)s||`.

`eta=0` means exact local tangent degeneracy. Nonzero `eta` is only a local prefilter.

## Constraints-first rule

For exact `L y=0`, parameterize the physical space with `Z`, `LZ=0`, and only then compute comparator rank/projectors.

Frozen order:

`Ward/contact/physical constraints -> physical basis -> comparator/nuisance quotient`.

## Nuisance attribution blocks

Use

`J=[J_dyn J_state J_detector J_cal J_mediator ...]`.

Final novelty uses the **joint** tangent span. Block ranks and principal angles diagnose which attribution layer absorbs a candidate direction; sequential projections are not used for the final verdict because they can be order dependent.

## Nonlinear/global gate

Freeze

`d_C^2(y)=inf_theta [y-c(theta)]^T Sigma(theta)^(-1)[y-c(theta)]`

inside the prospective common validity/nuisance domain.

For theory-family separation,

`d_min^2=inf_(lambda,theta) ||Sigma^(-1/2)[k(lambda)-c(theta)]||^2`.

A local COR is not a robust residual until curved-manifold/finite profiling confirms it.

## Candidate-parameter gate

For a future KG Jacobian `J_KG`,

`B_KG=Pi_perp Sigma^(-1/2)J_KG`.

Singular values of `B_KG` identify parameter combinations that remain locally measurable **after** comparator profiling.

Zero singular values are absorbed KG directions; near-zero singular values are near-degeneracies.

## Promotion rule

No KG ansatz may be promoted until a residual

- lives in the exact physical constraint basis;
- is outside the full comparator/nuisance tangent span;
- survives finite/global profiling;
- is stable across declared state/detector/calibration ranges;
- links multiple attribution layers;
- preserves Ward/contact/causal/relational structure;
- survives full-C5 same-order matching and field-redefinition/EFT quotient.

Only then may Fisher/resources be computed.

## Main consequence

The benchmark now defines novelty geometrically:

`Delta_KG^robust = inf_(C in comparator union) distance_W(O_KG,M_C) > 0`.

No such positive comparator-manifold distance has yet been established for Candidate Gravity.

Authoritative detailed protocol: `protocol/RESIDUAL_SPACE_GEOMETRY.md`.
