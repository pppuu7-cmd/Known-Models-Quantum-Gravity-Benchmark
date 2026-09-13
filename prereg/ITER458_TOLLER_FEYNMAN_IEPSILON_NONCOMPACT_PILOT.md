# Iter458 preregistration — Toller Feynman i-epsilon noncompact pilot

Frozen before implementation and production.

## Scientific question
For the already-qualified source sector `j=l=k=1`, does the primary-source Feynman projector

`I_eps^(±)[d] = int_R d(rhot)/(2*pi*i) * [± P_11(rhot;rho)/(rhot-rho∓i eps)] * d_11m^(rhot,1)(beta)`

show stable ordinary symmetric-real-axis truncation toward the independently qualified closed-form Toller branch on a held-out panel as `eps -> 0+` and the noncompact window grows?

This gate tests only an ordinary symmetric finite-window numerical realization of the source Eq. (20) projector. A FAIL does not refute the source distributional/contour identity and does not imply divergence of the causal vertex.

## Source lock
Use exactly the source projector polynomial
`P_11(rhot;rho)=prod_{n=0}^2 [i*rhot-(n-1)]/[i*rho-(n-1)]`
and denominator/sign prescription `±/(rhot-rho∓i eps)`. No `beta+i eps`, damping factor, fitted subtraction, contour deformation, or regulator replacement is allowed.

## Frozen panel
Independent lanes `m=-1,0,+1` plus one cross-check lane.
Targets:
- `rho in {0.35, 1.60}`
- `beta in {0.80, 2.10}`
- `eps in {0.20, 0.08, 0.032, 0.0128}`
- symmetric windows `R in {50,100,200,400}`
- deterministic midpoint step `h=0.0125`; grids are half-step shifted so `rhot=0` is never sampled.
- complex128 arithmetic for the production pilot; an independent compensated-sum route is required.

Both `+` and `-` branches are tested against the already-qualified closed forms from Iter456. The sum `I_eps^+ + I_eps^-` is also compared with `d(rho)` at every target.

## Frozen controls and diagnostics
1. Exact source sign/polynomial implementation agreement between two independently organized code paths: `<=1e-12` relative/absolute envelope.
2. NaN/Inf forbidden; all lanes must produce all requested points.
3. Direct sum vs compensated pairwise/Kahan accumulation disagreement `<=2e-9 * max(1,|I|)`.
4. For each fixed `eps`, final-window Cauchy stability between `R=200` and `R=400` must satisfy `<=0.02 * max(1,|I_R400|)` for both branches.
5. At `eps=0.0128`, branch error against independently qualified `t±` must be `<=0.05 * max(1,|t±|)` for every target.
6. At every window/epsilon point, additive projector recovery `I_eps^+ + I_eps^- -> d` is recorded; at the final `(R=400,eps=0.0128)` point require `<=0.05 * max(1,|d|)`.
7. Wrong-sign control obtained by flipping only the Feynman denominator sign while keeping the branch label fixed must fail the branch-target threshold on at least 75% of target cases.
8. Epsilon trend: final-window branch error at `eps=0.0128` must not exceed the error at `eps=0.20` by more than `10%` of `max(1,|t|)`.

## Frozen classifier
- all lanes structurally valid and all predicates pass -> `ITER458_TOLLER_FEYNMAN_IEPSILON_ORDINARY_TRUNCATION_SUPPORTED_SCOPED`
- structurally valid but any scientific predicate fails -> `SCIENTIFIC_FAIL_ITER458_TOLLER_FEYNMAN_IEPSILON_ORDINARY_TRUNCATION`
- missing/invalid outputs, exception, serialization or runner failure -> `INFRASTRUCTURE_OR_NUMERICAL_FAIL`

## Interpretation lock
A PASS is finite-panel support only for this ordinary symmetric-truncation realization of the source projector; it does not prove the full causal vertex converges or close D7-S2 automatically. A scientific FAIL localizes ordinary symmetric truncation as inadequate on this panel and requires a mathematically justified oscillatory/distributional/contour treatment rather than threshold weakening. No terminal D7 classifier or Candidate Gravity activation is authorized by this gate.
