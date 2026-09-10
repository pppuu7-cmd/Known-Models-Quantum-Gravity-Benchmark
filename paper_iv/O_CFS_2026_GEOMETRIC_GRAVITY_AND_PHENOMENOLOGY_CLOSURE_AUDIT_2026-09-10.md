# CFS 2026 geometric-gravity and phenomenology closure audit

**Date:** 2026-09-10  
**KMQGB iteration:** 211  
**RQIR Core:** v1.0 FROZEN

## Question

Does current Causal Fermion Systems (CFS) literature already provide a same-realization, gravity-specific beyond-GR/beyond-continuum observable with fixed state/regularization authority, normalization, an identical-domain GR/Einstein-Dirac comparator, and propagated uncertainty?

This audit updates `paper_iv/O_CFS_BEYOND_CONTINUUM_OBSERVABLE_CLOSURE_AUDIT_2026.md` with the July-2026 geometric derivation and re-tests older phenomenological candidates rather than treating `no observable` as a blanket statement.

## Positive control A — nonperturbative curved-spacetime classical gravity

P. Fischer and F. Finster, *The Continuum Limit Analysis of Causal Fermion Systems for Curved Spacetimes*, arXiv:2605.30199 (2026), constructs CFSs on globally hyperbolic spacetimes using a quasi-free Hadamard state and chart-independent `i epsilon` regularization. In the analyzed continuum setup, the causal-action Euler-Lagrange equations are satisfied iff the coupled Einstein-Dirac equations hold.

Retained status:

`EXACT_COMPARATOR_IDENTITY__EINSTEIN_DIRAC_CONTINUUM_SCOPE`.

## Positive control B — direct geometric Lorentzian Einstein bridge

F. Finster and C. Krpoun, *A Geometric Derivation of the Einstein Equations from the Causal Action Principle*, arXiv:2607.13871 (July 2026), gives a substantially more direct geometric bridge:

- the causal-action Lagrangian induces geometric structures;
- in the CFS specialization a Lorentzian metric is constructed in four spacetime dimensions;
- the Euler-Lagrange equations yield the Einstein equations with an energy-momentum tensor organized in a power expansion in the short regularization length `delta`;
- the gravitational coupling scales as `delta^2`;
- the formalism provides a systematic route to higher-order corrections.

This retires any residual blocker phrased as `no direct Lorentzian Einstein-equation bridge`.

However, Section 7 explicitly states that the identified correction families still need to be worked out in detail. The effects of the regularizing vector field on the Einstein equations remain to be analyzed. The extension of the geometric Einstein interpretation to non-smooth/quantum spacetimes is presented as an open problem.

Therefore this paper supplies a **correction generator/procedure**, not yet a frozen detector-facing correction observable with a numerical/comparator/error package.

## Candidate phenomenology A — correlated-state dark matter / dark energy

F. Finster and J. M. Isidro, *A Mechanism for Dark Matter and Dark Energy in the Theory of Causal Fermion Systems*, Class. Quantum Grav. 40 (2023) 075017, arXiv:2209.02234, provides concrete gravitationally interpretable scaling laws,

`Lambda ~ 1/T^2`,  
`T^0_0 ~ 1/(G T^2)`,

where `T` is the lifetime of the universe. Taking `T` of the order of the current cosmic age gives the observed order of magnitude for dark-energy/dark-matter scales.

This is retained as genuine CFS phenomenological structure, but it does **not** close the RQIR decision object:

1. the analysis explicitly works through the continuum-limit contribution to the Einstein equations;
2. the optimal microscopic regularization that realizes the causal-action minimizer is stated to be largely unknown and is assumed to exist;
3. the continuum-limit prefactors become empirical regularization parameters, and the paper states that even their signs are presently unknown;
4. consequently the scaling law is not yet a fixed-normalization, parameter-closed prediction with propagated theory uncertainty;
5. it therefore cannot furnish a robust comparator-orthogonal CFS residual against GR/EFT or other QG frameworks.

Classification:

`PASS_SCOPED_PHENOMENOLOGY__COSMOLOGICAL_T_MINUS_2_SCALING_EXISTS__BLOCKED_NORMALIZATION_REGULARIZATION_SIGN_AND_ERROR_CLOSURE`.

## Candidate phenomenology B — dynamical gravitational coupling

F. Finster and C. Röken, *Dynamical Gravitational Coupling as a Modified Theory of General Relativity*, arXiv:1604.03872, gives an explicit modified-gravity model motivated by CFS and works out FRW, collapse, Newtonian and solar-system consequences.

This is not promoted to the required CFS residual because the CFS research programme itself notes that the derivation assumes microscopic propagation governed by a Dirac/hyperbolic equation; that assumption has not been established directly from the causal action principle and may require modified corrections if microscopic Dirac dynamics fails.

Classification:

`PASS_SCOPED_CFS_MOTIVATED_MODIFIED_GRAVITY_MODEL__BLOCKED_DIRECT_CAUSAL_ACTION_DERIVATION_AUTHORITY`.

## Candidate phenomenology C — modified measures

F. Finster, E. Guendelman and C. F. Paganini, *Modified Measures as an Effective Theory for Causal Fermion Systems*, Class. Quantum Grav. 41 (2024) 035007, arXiv:2303.16566, demonstrates a structural route by which modified-measure gravity can arise as an effective CFS description. The paper presents this as a foundation for determining which modified-measure theories are actually consistent with the causal action principle; it does not freeze a unique CFS-derived correction realization and detector-facing comparator package.

Classification:

`PASS_SCOPED_EFFECTIVE_MODIFIED_MEASURE_MAP__BLOCKED_UNIQUE_CAUSAL_ACTION_SELECTION_AND_OBSERVABLE_CLOSURE`.

## RQIR conclusion

The old shorthand `no CFS beyond-continuum observable exists` is too coarse. Current literature contains several **candidate correction/phenomenology routes** and a 2026 geometric machinery capable in principle of deriving systematic corrections. What remains missing is closure of one route all the way through the frozen RQIR interface.

Updated school-level blocker:

`BLOCKED_CFS_CORRECTION_CANDIDATES_EXIST_BUT_NO_CAUSAL_ACTION_FIXED_REALIZATION_TO_NORMALIZED_GRAVITY_OBSERVABLE_COMPARATOR_WITH_PROPAGATED_ERROR`.

Required chain:

`causal-action-fixed microscopic/state realization -> explicit non-GR correction coefficient/sign -> normalized gravity observable -> same-domain GR/Einstein-Dirac comparator -> nuisance/regularization/truncation propagation -> robust residual`.

Consequences:

- CFS is **not scientifically failed**.
- No family-level residual is defined.
- The stronger 2026 gravity results make CFS more credible and the blocker narrower.
- CFS contributes zero exclusion evidence toward `NEW_REQUIRED`.
- D2/D4 remain open.
- No new RQIR-Core failure mode appears: the obstruction maps to already-frozen identifiability/resource, provenance, normalization/comparator and uncertainty closure rules.
- Paper III remains `NO_REOPEN`.

## Heavy compute

`IDLE`.

Numerical work is premature because the decisive correction coefficients/realization are not yet frozen by authority. Heavy compute is authorized only once a concrete correction formula with fixed state/regularization and comparator can change classification.

## Next CFS gate

`CFS_CORRECTION_COEFFICIENT_AND_REGULARIZATION_SELECTION_AUTHORITY_SEARCH`.

Search specifically for a causal-action-derived result that fixes at least one correction coefficient/sign or removes the regularization freedom in a gravity observable. If none is located after a bounded primary-source sweep, park CFS as BLOCKED under the current material scope and advance to the next nonterminal Tier-1 family.
