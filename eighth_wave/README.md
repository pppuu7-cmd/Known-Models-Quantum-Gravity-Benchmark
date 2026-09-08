# KMQGB Eighth Wave — Comparator Residual-Space Geometry

**Frozen denominator:** 5 methodology targets.  
**Historical waves 1–7:** terminal and immutable.  
**Purpose:** replace qualitative novelty labels with a mathematically explicit comparator quotient and robust residual certificate before any Candidate Gravity ansatz.

| # | Target | Question | State |
|---|---|---|---|
| T8-01 | whitened comparator tangent projector | which observable directions cannot be absorbed by infinitesimal comparator retuning? | ACTIVE |
| T8-02 | Ward/constraint quotient before profiling | how are gauge/contact/physical constraints removed before rank/novelty counting? | QUEUED |
| T8-03 | nuisance-block attribution geometry | which directions are dynamics, state, detector, calibration or mediator nuisance? | QUEUED |
| T8-04 | nonlinear comparator-manifold robustness | when does a locally transverse residual disappear under finite/nonlinear comparator motion? | QUEUED |
| T8-05 | promotion certificate | what quantitative conditions must a residual pass before a KG ansatz may be proposed? | QUEUED |

## Frozen notation

Let the real observable data vector be `y in R^m`. Complex observables are split into real and imaginary components after all exact symmetry relations are imposed.

Let a comparator parent predict

`c(theta)`

with allowed parameter/state/detector/nuisance vector `theta` and covariance matrix `Sigma` for the matched observable.

At a profiled point `theta_*`, define

`r = y - c(theta_*)`,

`J_C = partial c / partial theta |_(theta_*)`.

Whiten with `W=Sigma^{-1}` and any `W^(1/2)` satisfying the covariance metric. Define

`z = W^(1/2) r`,

`A = W^(1/2) J_C`.

The local comparator tangent space is `col(A)`. The Euclidean projector in whitened space is

`Pi_perp = I - A A^+`,

where `A^+` is the Moore-Penrose pseudoinverse.

The locally comparator-resistant residual is

`z_perp = Pi_perp z`.

Equivalent unwhitened W-orthogonal projector:

`P_perp = I - J_C (J_C^T W J_C)^+ J_C^T W`

when the displayed generalized inverse form is valid on the represented tangent subspace.

This is a local/linearized quotient only; T8-04 must guard against nonlinear manifold curvature and finite parameter excursions.
