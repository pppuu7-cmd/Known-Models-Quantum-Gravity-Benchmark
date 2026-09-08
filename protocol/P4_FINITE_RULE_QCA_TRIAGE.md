# P4 Finite-Rule / QCA Triage and Minimal Interacting Spin-2 QCA Target

**Status:** constructive P4 search authority / no Candidate Gravity ansatz promoted.  
**KMQGB iteration:** 062.  
**Purpose:** replace generic searches for a "finite microscopic rule" with a concrete, falsifiable classification target and preserve three useful controls.

## 1. Why this branch is worth testing

The P4 bottleneck is not lack of abstract consistency principles. KMQGB already showed that gluing, duality, associativity, overlap consistency and broad spectral constraints can leave an infinite or large hard-dynamical freedom.

Quantum cellular automata (QCA) are interesting for a different reason: at the **free-field** level, a small set of microscopic requirements can be highly selective. D'Ariano and Perinotti showed that the large-scale Dirac dynamics follows from a minimal nontrivial QCA satisfying unitarity, locality, homogeneity and discrete isotropy; related work derives the Maxwell regime from the same informational/discrete program.

This is not evidence that gravity follows. It is evidence that a finite microscopic update plus symmetry/minimality can, in principle, collapse functional freedom rather than merely constrain it.

The unresolved question is therefore sharpened to:

> Does there exist a finite-range, finite-local-dimension, translation-homogeneous quantum update whose constrained physical sector contains exactly the two gapless helicity-2 modes of GR at low momentum, whose nonlinear self-interaction is fixed by the same microscopic update, and whose first hard four-graviton correction is therefore predicted rather than independently chosen?

KMQGB names this classification target **MISP2-QCA**:

`Minimal Isotropic Self-interacting Physical-spin-2 Quantum Cellular Automaton`.

MISP2-QCA is a research target, **not** a current model or novelty claim.

---

## 2. Three controls under A1-A4

### Control F1 — Chrono-Grid Dynamics (CGD, 2026)

**Reference:** N. Jovanović, *Chrono-Grid Dynamics: a discrete unitary framework for emergent gravity*, Eur. Phys. J. C 86, 752 (2026), DOI 10.1140/epjc/s10052-026-16018-y.

Published construction:

- 3D cubic/tetrahedral lattice;
- spin-1/2 site degrees of freedom;
- dynamical `SU(2)` link variables;
- local Hamiltonian and discrete proper-time step;
- continuum variables identified with Ashtekar connection and densitized triad;
- discrete geometric spectra and `6j`-symbol structure;
- explicit links to spin-foam/Ponzano-Regge and, with cosmological constant, `SU_q(2)` / Turaev-Viro structures.

**A1 — explicit parent capsule:** `PROVISIONAL_PASS` at architecture level. A microscopic lattice Hamiltonian/update is supplied.

**A2 — finite functional freedom:** `PROVISIONAL_PASS` as a finite-rule architecture, subject to full coupling/constraint counting.

**A3 — architecture containment:** `FAIL__DISCRETE_LQG_SPINFOAM_BF_COMPARATOR_CONTAINED`.

Reason: the paper itself maps the continuum variables into Ashtekar canonical variables and explicitly connects the tetrahedral quantum geometry to spin-foam/BF/Turaev-Viro structures. This is scientifically useful comparator evidence, but it is not an independent KG parent outside the registered discrete/LQG manifold.

**A4 — hard relation:** `BLOCKED`. The paper does not supply the KMQGB-required complete Lorentzian hard four-graviton/CTP object; it also lists the full Hamiltonian constraint for many interacting tetrahedra among open problems.

**Verdict:** comparator-contained, no P4 credit.

---

### Control F2 — QICT / gauge-coded QCA with constrained spin-2 sector (2026)

**Reference:** M. Sacha, *Copy-Time Geometry from Gauge-Coded Quantum Cellular Automata: Emergent Gravity and a Golden Relation for Singlet-Scalar Dark Matter*, Quantum Reports 8(2), 33 (2026), DOI 10.3390/quantum8020033.

The peer-reviewed paper deliberately separates its theorem-level copy-time result from model-dependent emergent-gravity closure. Its worked 3+1D micro-model uses a depth-`D` local circuit acting on

- Weyl matter registers;
- finite-dimensional quantum-link gauge registers;
- a compactly truncated spin-2/tetrad register;
- constraint ancillas,

with a layered global unitary of the schematic form

`U = U_gauge-matter U_matter U_B U_E U_grav Pi_Gauss Pi_grav`.

**A1 — explicit parent capsule:** `PROVISIONAL_PASS` for the worked finite-depth circuit architecture.

**A2 — finite functional freedom:** `PROVISIONAL_PASS_ONLY_IF_GATES_ARE_MICROSCOPICALLY_FIXED`.

A finite-dimensional local register and finite-depth circuit are compatible with finite parent data, but the KMQGB low-freedom requirement is satisfied only if the local gate family is fixed by a finite principle rather than promoted as an arbitrary collection of matrices/functions.

**A3 — architecture containment:** `UNRESOLVED_FOR_HARD_QG_OBJECT`.

The architecture is QCA/quantum-link rather than a direct spin-foam construction, but the published gravity closure is explicitly model-dependent and uses conservative continuum spin-2/GR consistency logic. Without an independent hard gravitational object, novelty cannot be separated from ordinary discretized GR/QFT, quantum-link/lattice-gauge, or other discrete comparator realizations.

**A4 — hard relation:** `BLOCKED_MISSING_REQUIRED_OBJECT`.

No KMQGB-authorized explicit four-graviton hard amplitude/kernel plus same-parent CTP/retarded hierarchy has been identified in the published construction.

**Verdict:** strongest audited finite-rule **near-survivor architecture**, but not P4.

---

### Control F3 — hard-amplitude uniqueness: *Strings from Almost Nothing* (2026)

**Reference:** C. Cheung, G. N. Remmen, F. Sciotti, M. Tarquini, *Strings from Almost Nothing*, Phys. Rev. Lett. 136, 251601 (2026), DOI 10.1103/cw4p-cqh7.

This is an important positive control for the functional-freedom problem. Under consistency-imposed Regge zeros plus

1. ultrasoft high-energy behavior, and
2. minimal zeros,

the minimally consistent four-point amplitude space collapses onto the Veneziano and Virasoro-Shapiro amplitudes; analogous logic extends to five points.

**A1:** amplitude-level parent/selection principle, not a microscopic local QCA.

**A2:** `PASS` as a hard functional-selection positive control: the assumptions remove the arbitrary amplitude freedom in the stated scope.

**A3:** `FAIL__STRING_DUAL_RESONANCE_COMPARATOR_CONTAINED`.

The selected object is precisely a registered string comparator.

**A4:** `PASS_IN_COMPARATOR_SCOPE` because an explicit hard amplitude is selected, but it cannot score KG P4 after A3 failure.

**Verdict:** proves that a genuinely strong selector can collapse hard functional freedom, while simultaneously illustrating why immediate comparator containment is indispensable.

---

## 3. New locality constraint for a spin-2 QCA

A naive construction might try to place only the two transverse-traceless graviton helicities in each local cell. That is not a satisfactory strictly local starting point.

In momentum space the transverse projector contains

`pi_ij(k) = delta_ij - k_i k_j / k^2`,

and the spin-2 TT projector is built from `pi`. In position space the `1/k^2` factor corresponds to an inverse Laplacian. Thus the operation that extracts a globally transverse field is spatially nonlocal.

### MISP2-QCA locality rule

A strictly finite-range microscopic parent should therefore **not** assume a local TT-only register as its fundamental variable unless it explicitly accepts nonlocal kinematics.

For the `S-local` branch, use local gauge-redundant variables instead, for example

- local symmetric-tensor/tetrad-like registers;
- local connection/link registers;
- constraint/stabilizer ancillas;
- local Gauss/diffeomorphism/Hamiltonian-analogue constraints or a demonstrably equivalent finite-code construction.

The two physical helicity-2 modes must emerge **after** constraint/gauge reduction in the long-wavelength physical sector.

This is a design constraint, not an assertion that a unique discrete realization exists.

---

## 4. MISP2-QCA — exact A1 target

A candidate MISP2-QCA parent capsule must specify all of the following before any hard calculation.

### 4.1 Microscopic data

- a fixed homogeneous graph/Cayley lattice in 3 spatial dimensions;
- finite local Hilbert/register dimension `d_loc`;
- finite interaction radius `R`;
- fixed circuit depth `D` per microscopic time step, or an equivalent bounded local Hamiltonian rule;
- one exactly unitary global step `U(theta)`;
- a finite parameter vector `theta` whose dimension does not grow with perturbative order or lattice volume;
- local gauge-redundant spin-2/tetrad/connection variables plus exact local constraints.

### 4.2 Symmetry/minimality conditions

At minimum impose prospectively

- microscopic unitarity;
- strict finite-range locality;
- translation homogeneity;
- discrete spatial isotropy sufficient to recover rotational invariance at low `|k|`;
- constraint preservation under one update step;
- no independent gapless scalar or vector gravitational modes in the physical IR sector;
- exactly two gapless helicity `+2/-2` physical branches;
- low-`k` approximately Lorentzian dispersion with one emergent light cone;
- universal coupling of the spin-2 sector to the conserved stress-energy source in the GR limit;
- one shared Newton/self-coupling scale, not independent cubic/quartic couplings.

The finite-rule selector is the combination of microscopic update + these prospective constraints. The conditions must be imposed **before** opening the candidate-specific hard amplitude.

---

## 5. MISP2-QCA A2 — finite-freedom test

The ordinary EFT `FF_D` test must be supplemented by a microscopic gate-space count.

Let `G_n(theta)` denote the finite set of local gates/update tensors after imposing unitarity, homogeneity, isotropy and exact constraints for a fixed neighborhood/depth choice.

Define

`d_gate = dim(allowed microscopic gate manifold / local basis redundancies / pure gauge reparameterizations)`.

A necessary MISP2-QCA condition is

`d_gate < infinity`

with `d_gate` independent of scattering order.

Then derive the induced hard EFT/amplitude coefficients

`c_m = c_m(theta)`.

The essential rigidity criterion is

`rank(d c_1,...,d c_M / d theta) <= dim(theta)`

for increasing hard order `M`, rather than one new independent parameter per coefficient.

### A2 fail conditions

Classify `FUNCTIONAL_FREEDOM_BLOCKED` if any occurs:

- arbitrary momentum-dependent local gate functions are allowed without derivation;
- circuit depth/radius is allowed to grow independently with perturbative order in order to fit data;
- new independent gravitational gates/couplings are inserted at every hard order;
- the constraint projector contains an arbitrary nonlocal kernel;
- the emergent spin-2 sector is fixed only after fitting its hard dispersion/amplitude.

### A2 success signature

For fixed microscopic architecture, increasing the hard expansion order should generate **more predictions than new parent parameters**.

That is the QCA analogue of the KMQGB functional-freedom requirement.

---

## 6. MISP2-QCA A3 — comparator containment test

Any eventual solution must be profiled immediately against

- ordinary lattice discretizations of GR / spin-2 EFT;
- lattice gauge and quantum-link models;
- LQG/spinfoam/GFT/tensor-network/discrete gravity;
- Regge/causal-dynamical-triangulation style constructions;
- BF/topological/categorical models;
- quantum graphity / QCA / quantum-walk emergent-field programs;
- string/matrix/amplitude parents;
- asymptotic-safety/nonlocal/spectral comparators.

A finite circuit is not novel merely because it is written as gates. Field redefinitions, digital simulation encodings and finite Trotterizations of a known comparator remain comparator-contained.

### A3 minimum novelty requirement

The microscopic update must enforce at least one physical hard relation that is not an encoding artifact and is not forced by a registered comparator parent on the same common domain.

Without that relation, the object remains an interesting discrete implementation, not KG.

---

## 7. MISP2-QCA A4 — first required hard object

The target should not begin with cosmology or a fitted Newtonian potential. The first discriminating object is the vacuum/controlled-state helicity-2 scattering hierarchy.

### Required A4 object

Derive from the same microscopic `U(theta)`:

1. physical two-helicity one-particle graviton branches and residue normalization in the IR;
2. the cubic on-shell/self-coupling structure and its GR matching;
3. the **connected 2->2 physical helicity-2 amplitude / Floquet T-matrix** at low external momentum;
4. the first lattice/finite-rule correction beyond the matched GR/C5 amplitude;
5. the retarded/Schwinger-Keldysh response generated by the same update and same `theta`.

Schematic prospective target:

`A4_QCA = A4_C5,matched + (ell_* E)^p F_QCA(theta; helicities, angles) + O((ell_* E)^(p+1))`,

where

- `ell_*` is derived from the microscopic lattice/update scale;
- `p` is derived, not selected after inspection;
- the tensor/angular function `F_QCA` is fixed by `U(theta)`;
- no independent coefficient may be assigned to each helicity/angular channel.

The P4 opportunity is not the mere existence of Lorentz violation or lattice dispersion. It is a **shared-parameter hard relation** generated by the finite parent and surviving comparator profiling.

---

## 8. Constraint-preserving nonlinear closure is the central technical gate

Free-field QCA uniqueness is not enough. Gravity requires self-interaction.

The nonlinear update must preserve the physical constraint/code subspace:

`U(theta) P_phys = P_phys U(theta) P_phys`

(or an exactly equivalent constrained-unitary statement).

At low energy the resulting Ward/constraint identities must reproduce the massless spin-2 consistency conditions and universal GR self-coupling before candidate-specific hard corrections are interpreted.

A practical classification problem is therefore:

> classify finite local gate tensors for which (i) the linearized physical sector is exactly two helicity-2 modes, (ii) the constraint algebra/code is invariant under the interacting update, and (iii) cubic consistency fixes rather than frees the quartic/higher interaction hierarchy.

This is substantially sharper than "derive gravity from information".

---

## 9. Exact next analytic program

The next useful KMQGB work on this branch is lightweight/symbolic rather than heavy numerical simulation.

### Step Q1 — choose minimal graph and register

Start with the smallest 3D homogeneous/isotropic QCA geometry known to support nontrivial Weyl-like isotropic propagation (BCC/Cayley-type candidates are natural comparators), then construct a local **gauge-redundant spin-2 register**, not a TT-only cell.

### Step Q2 — solve the free spin-2 classification

Enumerate the most general finite-range translation-invariant unitary symbol `U_0(k)` consistent with the selected discrete isotropy and constraint code.

Require that after physical reduction its small-`k` spectrum has exactly two gapless helicity-2 branches and no unwanted gapless scalar/vector gravitational branches.

If no such minimal automaton exists, increase local dimension/radius prospectively and record the no-go.

### Step Q3 — classify the first interacting local gate

Write the smallest local nonlinear/coupled update `U = U_0 U_int(theta)` preserving the constraint code exactly.

Derive the continuum cubic vertex. Require GR universal self-coupling at the leading IR order using the same `theta`.

### Step Q4 — derive quartic rigidity

Do **not** insert a separate quartic gate after matching the cubic vertex. Derive the quartic response from repeated action/expansion of the same finite update and constraint preservation.

This is the first place where an actual KG P4 candidate could appear.

### Step Q5 — compute A4 and CTP only after Q1-Q4 close

Then and only then compute the physical four-graviton/Floquet amplitude and same-parent retarded/CTP block and apply full comparator profiling.

---

## 10. Heavy-compute decision

No heavy run is authorized yet.

The current blockers are structural classification questions:

- existence of a minimal local constrained spin-2 QCA;
- exact two-helicity physical reduction;
- finite gate-manifold dimension;
- interacting constraint preservation;
- cubic-to-quartic rigidity.

These should first be solved algebraically/symbolically on the smallest architecture. Large lattice simulation before this would explore an underdetermined gate space and would not create P4 authority.

A heavy job becomes justified after Q1-Q4 produce a frozen update rule, for example to evaluate its 2->2 Floquet scattering, finite-volume convergence or nonlinear holdout behavior.

---

## 11. Current verdict

- CGD: `A3 comparator-contained`, A4 missing.
- QICT gauge-coded QCA: `A1/A2 provisional near-survivor`, A4 missing and A3 hard novelty unresolved.
- String hard-uniqueness control: `A2/A4 positive`, `A3 string-contained`.
- MISP2-QCA: **new exact classification target, not yet a parent survivor**.

Therefore

- P4 remains open;
- R4 remains unchanged;
- no Candidate Gravity ansatz is promoted;
- the constructive search is now narrowed from a generic "finite microscopic selector" to the explicit Q1-Q5 interacting spin-2 QCA problem.

## References

1. G. M. D'Ariano, P. Perinotti, *Derivation of the Dirac Equation from Principles of Information Processing*, Phys. Rev. A 90, 062106 (2014), DOI 10.1103/PhysRevA.90.062106.
2. A. Bisio, G. M. D'Ariano, P. Perinotti, *Quantum cellular automaton theory of light*, Annals of Physics 368, 177-190 (2016), DOI 10.1016/j.aop.2016.02.009.
3. N. Jovanović, *Chrono-Grid Dynamics: a discrete unitary framework for emergent gravity*, Eur. Phys. J. C 86, 752 (2026), DOI 10.1140/epjc/s10052-026-16018-y.
4. M. Sacha, *Copy-Time Geometry from Gauge-Coded Quantum Cellular Automata: Emergent Gravity and a Golden Relation for Singlet-Scalar Dark Matter*, Quantum Reports 8(2), 33 (2026), DOI 10.3390/quantum8020033.
5. C. Cheung, G. N. Remmen, F. Sciotti, M. Tarquini, *Strings from Almost Nothing*, Phys. Rev. Lett. 136, 251601 (2026), DOI 10.1103/cw4p-cqh7.
