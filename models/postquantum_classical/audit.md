# Model Audit — modern postquantum classical gravity

Benchmark ID: KMQGB-S2-M04-POSTQUANTUM-CLASSICAL
Concrete realization ID: PQCG-MINK-CONSERVED-STOCHASTIC-MODES-2026-001
Role: modern C3b postquantum classical-spacetime comparator
State: TERMINAL
Final status: `EXACT_COMPARATOR_IDENTITY`

## Frozen realization

Use the 2026 Oppenheim–Sajjad linearized Minkowski stochastic-mode realization of postquantum classical gravity, but freeze the **local conserved transverse diffusion-kernel/SDE formulation** explicitly constructed in the same paper rather than treating the original non-conserved ultra-local DeWitt kernel as the final stochastic covariance.

Declared scope:

- fundamentally classical stochastic spacetime coupled within the classical–quantum framework;
- linearized pure-gravity stochastic sector around Minkowski for the frozen terminal comparator closure;
- scalar-vector-tensor decomposition;
- stochastic dynamical spin-2 and spin-0 sectors;
- Onsager–Machlup (OM), Martin–Siggia–Rose/Janssen–DeDominicis and stochastic-differential-equation formulations compared explicitly;
- physical probability/action restricted to the dynamical gauge-invariant sector in the declared linearized analysis;
- phenomenological Newtonian-potential / stochastic gravitational-wave observables retained as external tests, not as prerequisites for comparator identity.

This is an explicit 2026 realization, not the generic phrase "postquantum gravity".

## Bianchi issue resolved at the frozen linearized level

The initial audit retained a possible F2 blocker because Hirotani–Matsumura emphasized that a simple delta-correlated white-noise tensor kernel need not satisfy the Bianchi transversality condition.

Direct inspection of Oppenheim–Sajjad resolves the ambiguity more carefully:

1. They explicitly acknowledge that the original generalized-DeWitt diffusion matrix is not itself conserved in the naive SDE interpretation.
2. They show that in the OM action the inverse diffusion matrix is saturated by the conserved Einstein tensor, so longitudinal pieces cancel.
3. Inspired by the Bianchi critique, they then construct an alternative **local conserved diffusion matrix** built from transverse spin projectors.
4. They show that this conserved choice yields the **same OM action and the same two-point function** as the original representation in the declared linearized pure-gravity sector.
5. Their abstract/result further states that the action is positive semi-definite on all dynamical modes in the analyzed sector.

Therefore the Bianchi issue is not a terminal inconsistency of the frozen linearized stochastic-mode realization. It is a representation/kernel-definition issue that must be handled by using the conserved transverse formulation.

This scoped resolution does **not** prove full nonlinear matter-coupled constraint closure for every postquantum classical-gravity model.

## Frozen stochastic equation / kernel

In the conserved SDE representation,

`G_mn^(1) = xi_mn`,

with a local covariance built from transverse spin projectors schematically of the form

`<xi xi> = D2 [ c0 P^(0-s) + P^(2) ] delta^4(x-x')`,

where the exact scalar coefficient is the one given in Oppenheim–Sajjad Eq. (120) and the transverse projectors guarantee conservation. Gauge-fixing pieces introduced to invert the degenerate matrix drop out when saturated with conserved tensors. The resulting OM action is

`S_G = ∫ d^4x [ alpha R_mn R^mn - beta R^2 ]`

in the declared linearized construction, and the conserved-kernel SDE yields the same two-point function as the OM formulation.

## F0-F7 terminal map

| Gate | Result | Reason |
|---|---|---|
| F0 dynamics | PASS_SCOPED | explicit classical–quantum/stochastic path-integral realization and conserved local SDE kernel frozen |
| F1 required limits | PASS/PARTIAL | classical GR equation is the center of the stochastic diffusion; full nonlinear phenomenology is outside this terminal control scope |
| F2 consistency | PASS_SCOPED_LINEAR | conserved transverse kernel available; OM/JD/SDE consistency demonstrated in the frozen linearized sector; action PSD on dynamical modes |
| F3 RQIR hierarchy | STRONG_PASS_AS_COMPARATOR | stochastic metric two-point/noise structure and response arise from one explicit classical-stochastic construction |
| F4 comparator distinction | EXACT_IDENTITY_C3B | the realization is literally a modern postquantum classical-gravity member of the frozen C3 comparator family |
| F5 hard discriminator | ZERO_VS_C3B | no independent theory direction relative to its own comparator class |
| F6 identifiability | NOT_APPLICABLE_AFTER_IDENTITY | comparator residual is zero |
| F7 resources | RETAINED_AS_CONSTRAINTS | LISA/GW/decoherence tests constrain parameters but do not alter comparator identity |

## Comparator result

RQIR C3 explicitly includes postquantum classical / stochastic classical-spacetime–quantum-matter constructions. The frozen realization is therefore a direct concrete C3b member.

At theory-class level,

`Delta_C3b = 0`.

Terminal status: `EXACT_COMPARATOR_IDENTITY`.

This is a successful modern-comparator control, not evidence that postquantum classical gravity is experimentally established and not a global proof of nonlinear consistency.

## Scientific lesson

The Bianchi criticism is real for a naive non-conserved white-noise covariance, but the 2026 literature already contains a conserved transverse local formulation producing the same declared linearized OM action/two-point function. Hence RQIR must not turn the existence of a bad kernel representation into a blanket rejection of the whole postquantum classical program.

Conversely, any future Candidate Gravity signal based only on classical stochastic tensor/scalar metric power cannot be promoted until it survives this strengthened C3b comparator, not merely semiclassical C1 or stochastic-gravity C2.

## Sources

1. J. Oppenheim, M. Sajjad, *Stochastic modes in postquantum classical gravity*, arXiv:2605.05375 (2026), especially Appendix A and Eqs. (120)–(125).
2. T. Hirotani, A. Matsumura, *Testing classical-quantum gravity with geodesic deviation*, Phys. Rev. D 114, 026014 (2026), arXiv:2603.29230.
3. J. Oppenheim, Z. Weller-Davies, *The constraints of post-quantum classical gravity*, JHEP 02 (2022) 080, arXiv:2011.15112 — retained as version-dependent nonlinear/constraint warning, not silently transferred to the frozen 2026 linearized realization.
4. J. Oppenheim, *A Postquantum Theory of Classical Gravity?*, Phys. Rev. X 13, 041040 (2023).
5. External RQIR C3 comparator authority retained read-only.
