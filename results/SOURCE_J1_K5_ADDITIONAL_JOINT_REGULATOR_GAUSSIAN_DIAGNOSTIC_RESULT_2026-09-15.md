# SOURCE_J1_K5_ADDITIONAL_JOINT_REGULATOR_GAUSSIAN_DIAGNOSTIC — terminal result

Date: 2026-09-15
Status: `TERMINAL_SCIENTIFIC_DIAGNOSTIC_SCOPED`
Classification: `AUX_GAUSSIAN_JOINT_REGULATOR_REJECTED_UNRENORMALIZED_SCOPED`

## Frozen authority

Preregistration:

- `research/prereg/SOURCE_J1_K5_ADDITIONAL_JOINT_REGULATOR_GAUSSIAN_DIAGNOSTIC_2026-09-15.md`
- prereg commit `b4d5fc5734fe3fdde4b1008651b4e86f911e457a`

Decision-precedence protocol:

- `research/prereg/SOURCE_J1_K5_ADDITIONAL_JOINT_REGULATOR_GAUSSIAN_DIAGNOSTIC_PROTOCOL_2026-09-15.md`
- protocol commit `1d5b9123f71db860816ba7e8948c7ee5a78b364d`

Implementation:

- `code/source_j1_k5_additional_joint_regulator_gaussian_diagnostic.py`
- implementation commit `8ca8ba683b0bada0faca8015daae0ac6393db338`

Workflow head:

- `.github/workflows/source-j1-k5-additional-joint-regulator-gaussian-diagnostic.yml`
- commit `14ed14ee9f7951f5a3a9c65d8a33b9e3f45e5af1`

Parent validated frontier:

- terminal repaired Eq.4 existence result commit `6c4d479c42d3b71de4c4c32c5abb910728b97fc9`
- classification `SOURCE_J1_K5_EQ4_DISTRIBUTIONAL_EXISTENCE_BLOCKED_SCOPED`

The Critic-invalidated redundant joint-Feynman authority result at historical commit `aecdc3e6...` is not consumed as a premise.

## Execution provenance

Authoritative workflow run:

- run `34954054888`
- run status/conclusion: `completed/success`
- source-lock job `104331699506`: `success`
- diagnostic job `104331985957`: `success`
- artifact `10390423124`
- artifact name `source-j1-k5-additional-joint-regulator-gaussian-diagnostic`
- artifact size `2701` bytes
- artifact digest `sha256:7679e9349798386bc53757207cbb85142420e10ae89745b62e4ab4117cf54009`
- arithmetic precision: `160` decimal digits
- pinned `mpmath==1.3.0`

Green workflow status is provenance only; the scientific terminal label is the frozen classifier output below.

## Frozen object

The diagnostic replaces each highest-contact factor `delta''(B_e)` on the exact aligned K5 conormal witness by the second derivative of a normalized Gaussian approximate identity and pairs the ten-factor smooth product with `phi(x)=exp(-x dot x)` on the four active normal coordinates.

The exact K5 conormal authority was reproduced in source-lock:

- 10 K5 edges;
- ambient normal dimension 12;
- conormal rank 4;
- relation-space dimension 6;
- exact triangle relations;
- wrong-sign adversarial triangle nonzero.

P0, the common-regulator path, was prospectively frozen as exploratory reproduction only and is not decision evidence. Scientific classification consumes only the new anisotropic paths P1-P3.

## Controls

All frozen controls passed:

- `zero_edge_gaussian_integral = true`
- `one_edge_closed_formula = true`
- `vertex_relabel_invariance = true`
- covariance symmetry errors were exactly `0.0` in emitted diagnostics
- positive-definite Gaussian precision matrix controls passed
- internal second/fourth Wick-moment controls passed inside the implementation

`controls_pass = true`.

## New path results

Frozen regulator grid: `t_k = 2^{-k}`, `k = 3,4,5,6,7,8`.

### P1

Exponents in edge order `12,13,14,15,23,24,25,34,35,45`:

`(1,1,1,1,2,2,2,2,2,2)`

Result:

- status `UNRENORMALIZED_DIVERGENT_DIAGNOSTIC`
- terminal median tail growth `g_tail = 40.9990775603736422466822663728`
- final relative change `0.999999999999545179916341479733`
- final-three signs `(+,+,+)`
- `|J|` grows from approximately `1.94e36` at `k=3` to `9.49e97` at `k=8`.

### P2

Exponents:

`(2,2,2,2,1,1,1,1,1,1)`

Result:

- status `UNRENORMALIZED_DIVERGENT_DIAGNOSTIC`
- `g_tail = 26.0110331215379591304093293623`
- final relative change `0.999999985127314053611963120231`
- final-three signs `(+,+,+)`
- `|J|` grows from approximately `3.02e28` at `k=3` to `7.73e67` at `k=8`.

### P3

Exponents:

`(1,2,3,4,2,3,4,3,4,4)`

Result:

- status `UNRENORMALIZED_DIVERGENT_DIAGNOSTIC`
- `g_tail = 66.0070535518153169694864491807`
- final relative change `0.999999999999999999986464042703`
- final-three signs `(+,+,+)`
- `|J|` grows from approximately `3.63e63` at `k=3` to `1.17e163` at `k=8`.

For provenance only, P0 reproduction also reproduced the pre-disclosed divergent behavior (`g_tail ~= 26.00035`) but P0 was not used by the classifier.

## Frozen classification

All three NEW paths P1-P3 satisfy the preregistered `UNRENORMALIZED_DIVERGENT_DIAGNOSTIC` predicate. Therefore the prerequisite of at least two new divergent paths is exceeded and the terminal classification is mechanically:

`AUX_GAUSSIAN_JOINT_REGULATOR_REJECTED_UNRENORMALIZED_SCOPED`

No path-dependence terminal label is promoted merely because the divergent growth exponents differ; the frozen precedence supplement explicitly forbids that promotion when all NEW paths are divergent diagnostics.

## New scientific fact

The most direct unrenormalized Gaussian approximate-identity lifting of the source-present highest-contact sector does **not** provide a finite immediate joint extension on the exact aligned K5 witness for any of the three prospectively frozen anisotropic regulator-rate families. The divergence is robust to a large change in relative regulator rates and is not an artifact of the common-regulator exploratory path alone.

This materially narrows the additional-joint-regulator frontier: any viable auxiliary construction must do more than independently smooth each `delta''(B_e)` and remove the smoothings without subtraction/extension conditions.

## Interpretation ceiling

This result rejects only the frozen **unrenormalized Gaussian auxiliary extension candidate** on the aligned highest-contact K5 witness with the frozen Schwartz localization.

It does **not** establish:

- distributional nonexistence of the published Eq. (4) object;
- divergence of every source-compatible or renormalized extension;
- path dependence between distinct finite distributional limits;
- failure of an Epstein-Glaser/microlocal/collision-counterterm construction;
- source equivalence or inequivalence of any renormalized candidate;
- family-wide model failure;
- D7-S2/D7-S3/D7-S4 closure;
- any terminal selector or need for a new quantum-gravity model.

The next high-information gate must address whether the observed divergent Gaussian family can be renormalized by collision-supported counterterms under already frozen covariance/source/additive constraints, and whether those constraints uniquely fix the finite extension or leave genuine free parameters. Such counterterms are KMQGB-derived mathematical extension data unless separately source-authorized.

Global locks remain:

- `RQIR Core v1.0 = FROZEN`
- `D7-S2 = NOT_CLOSED`
- `D7-S3 = NOT_CLOSED`
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`
- terminal D7 selectors forbidden
- Candidate Gravity inactive
- KMQGB downstream of pinned DSIR authority
