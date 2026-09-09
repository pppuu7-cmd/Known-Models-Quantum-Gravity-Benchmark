# O2 Causal / Algebraic Dynamical-Selection Audit

**Status:** constructive-control audit / no P4 credit.  
**KMQGB iteration:** 073.  
**Search cell:** O2 finite algebraic/causal parent with dynamical selection.

## 1. O2 target

O2 requires more than a finite kinematical algebra, gluing rule, overlap condition or causal structure. The parent must select dynamics:

`finite algebraic/causal object -> unique or low-freedom interacting spin-2 hierarchy -> hard scattering + same-parent real-time response`.

The main question in this audit is whether current causal-set / causal-diamond / HST controls already supply this complete chain.

## 2. Causal-set QFT representation bridge

Controls:

- Albertini, Dowker, Nasiri, Zalel, *In-in correlators and scattering amplitudes on a causal set*, arXiv:2402.08555 (2024).
- Zalel, *The causal set reduction formula*, arXiv:2607.04980 (2026).

These results are strong positive controls for representation completeness. They show that on a causal-set background one can define interacting in-in correlators, an in-out generating functional, S-matrix elements and a reduction formula relating matrix elements to correlators.

Thus causal discreteness is not intrinsically incompatible with the KMQGB requirement that a parent support both scattering and real-time/in-in observables.

However the cited interacting construction is ordinary field theory on a specified causal set. It does not derive the quantum dynamics of the causal structure itself or a physical interacting helicity-2 amplitude.

Classification:

`O2_REPRESENTATION_BRIDGE_PASS__GRAVITATIONAL_DYNAMICAL_SELECTOR_ABSENT`.

## 3. Benincasa-Dowker gravitational action

Controls:

- Adamson, Wallden, *Benincasa-Dowker causal set actions by quantum counting*, arXiv:2505.22217 (2025).
- Ferguson, Nasiri, Wallden, *Dynamics of discrete spacetimes with Quantum-enhanced Markov Chain Monte Carlo*, arXiv:2506.19538 (2025).

The Benincasa-Dowker action is a discrete causal-set analogue of the Einstein-Hilbert action and gives a finite constructive gravitational object for a fixed finite causal set. Recent work also develops algorithms for evaluating and sampling causal-set configurations using this action.

For the present P4 task, however:

- the architecture is already a registered causal-set/discrete comparator;
- a unique interacting physical graviton S-matrix is not derived from the action in the audited results;
- the same-parent causal-set `Gamma_CTP`/retarded spin-2 response and a hard four-graviton relation are not frozen;
- algorithmic sampling of `exp(iS)` or related ensembles is not itself a new dynamical selector.

Classification:

`O2_CAUSAL_SET_COMPARATOR__HARD_SPIN2_HIERARCHY_INCOMPLETE`.

## 4. Causal-diamond local amplitudes

Control:

- Theofilis, Wieland, *Foundational Structure of Local Amplitudes in Quantum Gravity*, arXiv:2508.09679 (2025).

The causal-diamond/null-slab framework supplies a general Hilbert-space factorization, a physical projector and gluing rules producing local amplitudes satisfying Ward identities and charge conservation.

Its explicit purpose is theory-independent: different quantum-gravity approaches may realise the scaffold differently.

Therefore the framework passes a structural consistency test but intentionally does not select one microscopic gravitational projector/dynamics.

Classification:

`O2_STRUCTURAL_SCAFFOLD__DYNAMICAL_PROJECTOR_NOT_SELECTED`.

This restates the Wave38 lesson in the sharper O2 language:

`composition/gluing/charge consistency -> many admissible dynamics`.

## 5. Holographic Space-Time / finite causal-diamond algebras

Controls include Banks' finite-dimensional causal-diamond/Hilbert-bundle/HST program and the 2025 hydrodynamic review `arXiv:2502.04924`.

The finite-dimensional subsystem idea gives genuine H1/H2-like microscopic economy. HST also has scattering constructions with Newton-law scaling and black-hole-like states in broad classes of time-dependent Hamiltonian models.

The crucial O2 issue is that the causal-diamond overlap/entropy/relativity constraints do not uniquely select one hard interaction hierarchy. Existing formulations retain a class of Hamiltonians/interactions rather than deriving a unique four-graviton tensor amplitude from the overlap principle alone.

Classification:

`O2_HST_COMPARATOR__FINITE_KINEMATICS_WITH_NONUNIQUE_HARD_DYNAMICS`.

## 6. Soft/area-fluctuation causal-diamond developments

Recent causal-diamond work relating asymptotic soft modes to finite diamonds or quantizing area fluctuations gives useful evidence that finite causal subsystems can carry quantum-geometric information.

But soft-mode/area fluctuation relations are not substitutes for the current P4 hard relation.

Classification:

`O2_SOFT_GEOMETRY_SUPPORT__H3_HARD_SCOPE_ABSENT`.

## 7. Current O2 boundary

The audited O2 controls show a complementary split:

- causal sets provide increasingly complete **real-time/scattering machinery** for fields on discrete backgrounds, but not yet a unique dynamical physical spin-2 parent;
- causal diamonds/HST provide **finite/algebraic microscopic structures**, but their consistency principles leave more than one hard dynamics;
- discrete gravitational actions provide an explicit gravitational weight, but remain registered comparator architectures and do not yet derive the required hard+CTP physical hierarchy.

No audited hit currently supplies all

`finite algebraic object + unique dynamical selection + interacting physical spin-2 hard relation + comparator escape`.

Classification:

`O2_NO_CURRENT_HARD_NEAR_SURVIVOR_IN_AUDITED_CAUSAL_ALGEBRAIC_SET`.

## 8. O2 reopen condition

A serious O2 proposal must add a **dynamical uniqueness mechanism** absent from the controls above. It must do at least one of:

1. prove that finite algebra/causal/overlap consistency plus a finite extra axiom uniquely fixes the interacting transfer operator;
2. derive a finite recursion/minimal-polynomial rule whose coefficients fix the complete hard spin-2 hierarchy;
3. derive both the hard S-matrix and CTP/retarded response from one finite operator without an arbitrary Hamiltonian/function family.

If the extra rule merely selects one member of an otherwise arbitrary Hamiltonian class by hand, A1/A2 remains blocked.

## 9. Score consequence

No readiness score changes. R4 remains 45% because O2 has not produced an explicit novel P4 survivor.
