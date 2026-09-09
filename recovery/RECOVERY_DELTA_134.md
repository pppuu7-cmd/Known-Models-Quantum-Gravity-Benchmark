# Recovery Delta 134

**Iteration:** 134  
**Status:** immutable recovery; score-neutral.

Added

- `protocol/P5_DETECTOR_VISIBLE_RESIDUAL_PHYSICAL_COVARIANCE_GATE.md`;
- `code/detector_visible_residual_physical_covariance_reference.py`.

The new gate extends comparator-orthogonal residual geometry into detector space. It requires source-traceable covariance, complete apparatus nuisance tangents, explicit independent calibration priors, fail controls and stress robustness. The executable fixture ports the external RQIR SYRTE Fig.-8 physical covariance and reproduces its source scales before checking detector-visible profiled information.

The fixture correctly rejects static/free-offset, no-reference and unconstrained-reference cases, while known or independently-prior-constrained reference cases remain identifiable under the physical covariance and crosstalk stress.

The frozen `residual/identifiability/rigidity` component remains 19/20 because the external authority is still phase-Gaussian rather than fully detector-facing nonlinear `P=(1+C cos Phi)/2` with contrast/readout nuisance.

**Scores:** R1 92, R2 89, R3 24, R4 45.