# Paper IV D2 / D4 / D7 Closure Audit

**Date:** 2026-09-10  
**Iteration:** 182  
**RQIR authority:** Core v1.0 FROZEN  
**Scope:** scientific closure audit only; no RQIR semantic change and no Candidate Gravity promotion.

## Question

Can the three remaining Paper-IV global gates be closed from currently published, same-realization, comparator-ready objects?

- D2 — major-framework complete-object coverage;
- D4 — comparator-subtracted residual matrix;
- D7 — global terminal proof obligation.

## Result

**No terminal global decision is authorized in Iter182.** The audit does not find evidence that RQIR Core is defective. It does sharpen all three gates into an explicit machine-auditable dependency graph.

D2 remains `NOT_CLOSED` because three major-framework rows are still missing required complete physical objects. D4 is upgraded from an unstructured open statement to `PARTIAL_MATRIX_FROZEN__NOT_CLOSED`: a residual matrix can be written now, but its AS/LQG/CFS rows must remain `BLOCKED_MISSING_REQUIRED_OBJECT` rather than be zero-filled or treated as exclusions. D7 remains `NOT_CLOSED` because no terminal decision is logically derivable while D2 and D4 are open.

## O-AS — Asymptotic Safety

### New authority checked

1. B. Knorr, **Asymptotically (un)safe scattering amplitudes from scratch: a deep dive into the IR jungle**, arXiv:2602.21285v2.
2. A. P. Chiesa, J. M. Pawlowski, M. Reichert, **Towards Two-to-Two Scattering of Scalars in Asymptotically Safe Quantum Gravity**, arXiv:2603.10168.
3. Related 2026 Lorentzian/form-factor developments were checked only as supporting context; they are not composed across realization boundaries unless an explicit map exists.

### What closes

- A direct contact contribution is not merely hypothetical: arXiv:2602.21285 gives an explicit contact-amplitude sector through momentum-dependent scalar four-point form factors.
- The Chiesa–Pawlowski–Reichert calculation supplies a non-perturbative Lorentzian graviton-mediated scalar-scattering object and explicitly decomposes the complete target as `A_s+A_t+A_u+A4`.

### Why D2 does not close

The two papers do **not** by themselves constitute one same-realization complete amplitude certificate. The contact calculation uses a deliberately simplified approximation, neglecting several gravitational and non-minimal form factors; its own conclusion states that a more complete treatment with momentum-dependent propagators and all relevant vertices is needed before a final amplitude-level verdict. The Chiesa–Pawlowski–Reichert calculation, meanwhile, explicitly omits `A4` in the published object.

Therefore cross-paper addition of `A4` to `A_s+A_t+A_u` is forbidden by the same-realization gate unless the trajectory, field normalization, regulator/truncation, vertex conventions and uncertainty map are explicitly matched.

### Minimal closure certificate

`O_AS_COMPLETE = {realization_vector, A_s, A_t, A_u, A4, crossing/forward prescription, trajectory map, field/vertex normalization, truncation+reconstruction error budget, GR/EFT+alternative-QG same-domain comparator}`.

Current status: `BLOCKED_MISSING_REQUIRED_OBJECT`, not `FAIL`.

## O-LQG — LQG / EPRL / spinfoam

### Authority checked

1. B. Dittrich, A. Kogios, **From spin foams to area metric dynamics to gravitons**, arXiv:2203.02409.
2. J. N. Borissova, B. Dittrich, **Towards effective actions for the continuum limit of spin foams**, arXiv:2207.03307.
3. B. Dittrich, J. Padua-Argüelles, **Twisted geometries are area-metric geometries**, arXiv:2302.11586.
4. J. Borissova, B. Dittrich, A. Eichhorn, M. Schiffer, **Renormalization group flows in area-metric gravity**, arXiv:2507.02034.
5. B. Dittrich, **Gravitational wave signatures from area metric gravity**, arXiv:2608.16046.
6. Iter181 same-realization EPRL -> Regge asymptotic authorities retained unchanged.

### What closes

- The area-metric representation of twisted/spinfoam kinematics is well motivated and explicit.
- Area-Regge continuum dynamics yields GR gravitons at leading order with controlled higher-derivative corrections in the studied regular-lattice setting.
- Area-metric gravity has a parity-sensitive left/right sector and an explicit Immirzi-dependent coupling parameterization; a beta function for the area-metric Immirzi parameter has been computed.
- Gravitational-wave/birefringence observables make the area-metric Immirzi parameter operationally identifiable in principle.

### Decisive non-closure

The 2025 area-metric RG paper explicitly treats the non-metric masses as independent because they are **not currently computable from spin-foam models**, and it assumes the existence of an intermediate effective-field-theory regime between a fundamental spin-foam scale and the Planck scale. Thus the downstream area-metric RG parameter `gamma` cannot be identified with the microscopic EPRL `gamma` merely by notation.

Likewise, the effective-spin-foam/Area-Regge results motivate and calculate a continuum route, but they do not provide the required controlled same-realization multiscale coarse-graining/refinement semigroup from one declared Lorentzian EPRL realization into the specific parity-sensitive running area-metric action used for the RG and detector observable.

### Minimal closure certificate

`O_LQG_COMPLETE = {declared Lorentzian EPRL realization, boundary/refinement prescription, EPRL->Regge asymptotic remainder, Regge->Area-Regge coarse-graining map, Area-Regge->area-metric coupling map, gamma_EPRL->gamma_AM(mu) normalization/running law, parity-coupling ancestry, beta_rho/beta_Delta transport, common-scale observable map}`.

Current status: `BLOCKED_MISSING_REQUIRED_OBJECT`, not `FAIL`.

## O-CFS — Causal Fermion Systems

### Authority checked

1. P. Fischer, F. Finster, **The Continuum Limit Analysis of Causal Fermion Systems for Curved Spacetimes**, arXiv:2605.30199.
2. F. Finster, C. Krpoun, **A Geometric Derivation of the Einstein Equations from the Causal Action Principle**, arXiv:2607.13871.
3. F. Finster, P. Fischer, **Construction of Currents in Causal Fermion Systems**, arXiv:2507.09633.

### What closes

- The curved-spacetime continuum analysis supplies an iff correspondence between the causal-action Euler-Lagrange equations and the coupled Einstein–Dirac equations in its stated setup.
- The geometric derivation identifies the gravitational coupling with the regularization-length scale and supplies a systematic expansion architecture for corrections to Einstein gravity.
- The currents construction supplies a tensor hierarchy that is designed to extend to gravitation and systematic higher-order corrections.

### Decisive non-closure

The currents paper explicitly says the rank-two equations are **expected** to encode Einstein equations; it does not present the requested first explicit normalized beyond-Einstein gravity correction tensor. The 2026 geometric work supplies a correction generator/expansion architecture, but the comparator-ready coefficient tensor still has to be worked out for a fixed state/regularization/measure realization.

Therefore one cannot subtract the full GR/EFT/C5 comparator span yet: the candidate residual vector itself is not numerically/tensorially frozen.

### Minimal closure certificate

`O_CFS_COMPLETE = {fixed minimizing/state/regularization realization, explicit first non-Einstein tensor DeltaG_mn or equivalent coefficient vector, normalization in ell_min/G_N units, conservation/Ward consistency, approximation order+remainder, observable projection, full GR/EFT/C5/QFT comparator quotient}`.

Current status: `BLOCKED_MISSING_REQUIRED_OBJECT`, not `FAIL`.

## D4 comparator-subtracted residual matrix

A machine-readable matrix is frozen in `paper_iv/PAPER_IV_COMPARATOR_RESIDUAL_MATRIX_2026-09-10.json`.

Its semantics are strict:

- `BASELINE_OR_COMPARATOR_IDENTITY` is not a novel residual;
- `SCOPED_RIGIDITY_PASS` is positive scoped evidence but not a global winner;
- `BLOCKED_MISSING_REQUIRED_OBJECT` means the residual is **undefined**, never zero;
- no `BLOCKED` row contributes exclusion evidence toward `NEW_REQUIRED`.

This is meaningful progress on D4, but D4 is not terminal until every required major-framework row has a complete same-domain observable and comparator quotient.

## D7 terminal logic

The executable validator `code/paper_iv_global_gate_validator.py` enforces:

1. D7 cannot pass unless D2 and D4 pass;
2. `NEW_REQUIRED` cannot be authorized with any required framework row `BLOCKED`/undefined;
3. `EXISTING_SUFFICIENT` requires at least one globally sufficient complete row;
4. `ADAPT_EXISTING` requires a complete row whose remaining gap is proven adapter-only;
5. `HYBRID_REQUIRED` requires complete constituent rows plus an explicit interface/no-double-counting certificate.

At Iter182 none of these terminal proof obligations is met.

## Scientific conclusion

The present failure to close D2/D4/D7 is **not evidence that all known schools are wrong**. It is evidence that the decisive comparison is still object-limited: three frameworks lack the complete same-realization physical object required for a common comparator quotient.

The strongest justified global statement remains:

`NOT_YET_AUTHORIZED`.

The next scientifically useful work is not heavier numerics. It is to derive or obtain one of the three missing closure certificates above.