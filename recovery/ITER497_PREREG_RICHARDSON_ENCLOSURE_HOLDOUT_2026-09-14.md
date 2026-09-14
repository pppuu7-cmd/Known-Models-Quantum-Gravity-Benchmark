# Iter497 preregistration — Richardson enclosure holdout

**Prospectively frozen before implementation.**

## Authority and purpose
Iter496 terminal authority is `ITER496_COEFFICIENT_STENCIL_CONVERGENCE_QUALIFIED_SCOPED` from production head `1098eb1f8a8ceac78013e8c85194bad61d43cf6a`, run `34807803061`, aggregate artifact `10333948552`, digest `sha256:3d8f62cc56d51ae0045c6a8ad30a1655713e1b18fda7caed6420b784bb68d274`.

Iter496 materially suppressed the Iter495 remainder and restored near-cubic median scaling, but retained nonuniform outliers. Iter497 is a conservative **finite holdout enclosure validation**, not a continuous interval theorem.

## Frozen geometry and states
- q = 1 only.
- Active coordinates remain exactly `[0,1,3,5,6,11]`.
- Same eight frozen 6-D directions / four direction blocks as Iter495/496.
- Causal classes exactly `0to5`, `1to4`, `2to3`.
- Same four frozen rho witnesses inherited from the authoritative evaluator.
- Both direction signs are retained.
- Coefficient stencils remain exactly `h={0.0050,0.0025,0.00125}`; no new h values may be introduced.
- Richardson coefficients are exactly `(4*C_0.00125-C_0.0025)/3`.

## Training and independent holdout amplitudes
The enclosure is built only from the already-qualified training amplitudes `{0.00125,0.0025}`.

Independent, prospectively frozen holdouts are exactly:
`{0.00150,0.00175,0.00200,0.00225}`.

No amplitude may be added, removed or shifted after production evidence is seen.

## Frozen conservative enclosure
For each causal/rho/direction/sign state:
1. Compute Richardson quadratic prediction `T_R(x)`.
2. Compute the absolute training residuals at amplitudes `0.00125` and `0.0025`.
3. Define `K3 = max(|r(a)|/a^3)` over those two training amplitudes.
4. Freeze cubic remainder allowance at holdout amplitude `a` as `E3(a)=2*K3*a^3`. Safety factor `2` is fixed prospectively.
5. Define coefficient uncertainty from the two finest raw stencils as `E_C = (4/3)*|C_0.00125-C_0.0025|` coefficientwise. Propagate it by triangle inequality through all linear, diagonal-quadratic and mixed-quadratic monomials at the holdout point to obtain `EC(x)`.
6. Total enclosure is `E_total(x)=E3(a)+EC(x)`.
7. A holdout is covered iff `|actual-T_R(x)| <= E_total(x)` with only floating-point comparison slack `1e-12*max(1,E_total,|actual|,|T_R|)`.

This enclosure is deliberately conservative and may double-count coefficient uncertainty. No fitted safety factor, fitted exponent, fitted direction weight or fitted cancellation is allowed.

## Frozen matrix
`3 causal classes × 4 direction blocks = 12 independent Actions jobs`, `fail-fast:false`, `max-parallel:12`.

Each job must emit all holdout residuals, component allowances, coverage booleans and margin ratios. Aggregate must consume all 12 raw artifacts.

## Interpretation rule
- `ITER497_RICHARDSON_ENCLOSURE_HOLDOUT_QUALIFIED_SCOPED`: all numerical/source controls valid and **every** prospectively frozen holdout is covered.
- `SCIENTIFIC_FAIL_ITER497_RICHARDSON_ENCLOSURE_HOLDOUT`: controls valid but at least one frozen holdout violates the preregistered enclosure.
- `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER497`: source/numerical/control validity fails; this is not scientific evidence.

A qualified PASS authorizes only a subsequent genuinely validated interval/uniform neighborhood certificate. It is not itself a positive-measure theorem, Haar convergence/divergence theorem, D7-S2 closure, or terminal D7 classifier.

If scientific FAIL occurs, the next gate must be a prospectively frozen higher-order/direct interval treatment; no post-hoc enlargement of factor 2, h set, directions, rho values or holdout amplitudes is allowed.

## Scope guards
D7-S2 remains NOT_CLOSED; D7-S3 NOT_CLOSED; D7-S4 PARTIAL_GLOBAL_NOT_CLOSED. `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED` remain forbidden. Candidate Gravity inactive. Ten-source spectral normalization/order/i-epsilon, Iter461 collision geometry and PV/conditional/distributional admissibility remain independent blockers.
