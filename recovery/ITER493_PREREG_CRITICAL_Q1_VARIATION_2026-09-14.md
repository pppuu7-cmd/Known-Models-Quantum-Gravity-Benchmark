# Iter493 Preregistration — Critical q=1 first/second angular variation

Date: 2026-09-14
Status: prospectively frozen before implementation.

## Authority
Iter492 terminal classification is `ITER492_TANGENT_BOUNDARY_LAYER_BRACKET_QUALIFIED_SCOPED`, with the smallest frozen FULL_NONDECAY exponent `q=1.00`; `q=0.75` fails and `q=1.00` passes on the finite frozen matrix. Iter493 must not add post-hoc q points. It interrogates the already-frozen critical scaling `eps(R)=kappa*exp(-R)`.

## Scientific question
At the critical q=1 boundary layer, what are the local first and second variations of the post-Haar actual radial slope with respect to the full 20-dimensional angular chart at the center NONDECAY ray? The purpose is to distinguish a smooth critical boundary layer from a numerically singular/coordinate-specific ridge and to identify which angular coordinates dominate the local response.

## Frozen design
- causal classes: `0to5`, `1to4`, `2to3`.
- angular basis: all 20 standard coordinate basis vectors of the existing Iter490/491 20-D chart; no direction selection after computation.
- matrix partition: four fixed coordinate blocks `[0..4]`, `[5..9]`, `[10..14]`, `[15..19]` for each causal class; 12 independent jobs; `fail-fast:false`; `max-parallel:12`.
- critical exponent: `q=1.00` only.
- symmetric amplitudes: `kappa in {0.005, 0.010}` with both signs for every coordinate.
- center: exact zero perturbation, using the already-qualified HP source geometry.
- rho witnesses: all four source witnesses inherited from Iter486/491.
- R grid, KAK conventions, intertwiner channels, Haar bookkeeping and source-object controls: unchanged from Iter492.

For each causal × coordinate × rho, define using the actual radial slope `s(kappa)` returned by the unchanged Iter492 source evaluator at q=1:

- first variation `D_h = [s(+h)-s(-h)]/(2h)` for h=0.005 and 0.010;
- second variation `Q_h = [s(+h)+s(-h)-2 s(0)]/h^2` for h=0.005 and 0.010.

The raw values at both step sizes are authoritative outputs. No scientific magnitude threshold is imposed post hoc.

## Frozen numerical validity controls
A lane is numerically valid only if:
1. center and every +/- evaluation pass all inherited Iter492 HP/source controls;
2. all returned slopes/variations are finite;
3. center regression against the Iter491 HP center is within the inherited tolerance;
4. no missing rho state is allowed.

A finite-difference convergence diagnostic is also recorded, but is not allowed to convert an otherwise valid scientific result into a desired sign/magnitude outcome. Specifically record for each first/second variation the absolute two-step discrepancy and scale-normalized discrepancy `|x_0.005-x_0.010|/max(1,|x_0.005|,|x_0.010|)`.

## Frozen aggregate outputs
- max and median absolute first variation over all causal × coordinate × rho states;
- max and median absolute second variation;
- coordinate/causal/rho location of extrema;
- two-step discrepancy maxima;
- sign-stability counts of first variation between the two step sizes;
- per-coordinate response norm aggregated over causal/rho states.

## Interpretation rule
If all jobs are valid, classify `ITER493_CRITICAL_Q1_LOCAL_VARIATION_QUALIFIED_SCOPED` and report the measured response tensor diagnostics, regardless of whether the response is small or large. If any inherited source/HP control fails, classify `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER493` and diagnose the first causal failure; do not relax thresholds.

Even a valid Iter493 result is a finite-grid/local-variation diagnostic only. It is **not** an analytic or interval proof, does not establish an open positive-measure angular neighborhood, does not prove Haar convergence/divergence, does not close D7-S2, and does not authorize any terminal D7 label or Candidate Gravity. A subsequent analytic/uniform certificate remains mandatory if the local response supports one.

## Locks
D7-S2 `NOT_CLOSED`; D7-S3 `NOT_CLOSED`; D7-S4 `PARTIAL_GLOBAL_NOT_CLOSED`. `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` forbidden. Candidate Gravity inactive.
