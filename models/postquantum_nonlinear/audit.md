# T3-04 Audit — nonlinear postquantum-classical consistency

Benchmark ID: KMQGB-T3-M04-PQCG-NONLINEAR
Concrete audit family ID: `PQCG-COVARIANT-NONLINEAR-CONSTRAINT-001`
Role: test whether the strong C3b comparator remains consistent beyond the scoped linearized conserved-kernel sector
State: ACTIVE / NONTERMINAL

## Why this target is distinct from second-wave S2-M04

Second-wave S2-M04 froze a **linearized Minkowski pure-gravity stochastic-mode realization** with a conserved transverse kernel. That was sufficient to reject a blanket Bianchi failure at the two-point/linearized level and to retain C3b as a strong comparator.

T3-04 asks a harder question:

> Does a covariant, completely-positive classical-spacetime / quantum-matter dynamics possess a consistent nonlinear gravitational constraint structure, rather than only a consistent linearized stochastic sector?

The benchmark must not transfer either a linearized PASS or an old discrete-class non-closure result to the whole program without checking scopes.

## Authority set

### A. Constraint-algebra warning — 2022

Oppenheim & Weller-Davies, *The constraints of post-quantum classical gravity* (JHEP 02 (2022) 080), derive generalized Hamiltonian/momentum constraints for a broad **discrete class** with a quantum scalar field coupled to classical gravity.

Their explicit result is that the computed constraint algebra does **not close without additional constraints** in that class.

This is a real scoped nonlinear consistency warning. It is not a universal no-go theorem for every later continuous/covariant realization.

### B. General continuous hybrid dynamics — 2026

Oppenheim, Sparaciari, Soda & Weller-Davies, *General form of continuous hybrid classical-quantum dynamics* (Phys. Rev. A 113, 052223 (2026)), derive the general memoryless continuous hybrid classical-quantum dynamics under linearity, probability preservation and complete positivity.

This strengthens the mathematical foundation of the allowed hybrid dynamics, but by itself does not prove closure of the nonlinear gravitational Hamiltonian constraint algebra.

### C. Covariant path-integral formulation — 2026

Oppenheim & Weller-Davies, *Covariant Path Integrals for Quantum Fields Backreacting on Classical Space-Time* (Phys. Rev. X 16, 031007 (2026)), construct configuration-space path integrals for quantum fields interacting with classical fields and prove complete positivity directly. The formalism allows Lorentz and diffeomorphism invariance to be imposed in the path-integral construction.

This is a substantial improvement over a purely noncovariant hybrid model. However, **manifest/path-integral covariance is not automatically identical to canonical first-class constraint-algebra closure** in a specific nonlinear gravity realization.

The benchmark therefore treats covariance/CP and canonical closure as related but distinct consistency tests.

## Frozen consistency vector

Use

`I_PQNL = {CP, DiffCov, H_i, H_0, Closure, Bianchi, MatterBackreaction, DOF}`

where

- `CP`: complete positivity / probability preservation of the hybrid evolution;
- `DiffCov`: spacetime or spatial diffeomorphism covariance in the declared representation;
- `H_i`: momentum/spatial-diffeomorphism constraints;
- `H_0`: Hamiltonian/time-reparametrization constraint;
- `Closure`: closure/first-class status of the full constraint algebra after all required extra constraints are included;
- `Bianchi`: compatibility of stochastic/backreaction kernels with geometric conservation identities;
- `MatterBackreaction`: explicit quantum-matter backreaction rule;
- `DOF`: physical degree-of-freedom count after constraints/gauge reduction.

No nonlinear C3b realization receives an F2 PASS unless these objects refer to the **same concrete dynamics**.

## Current F0-F7 map

| Gate | State | Reason |
|---|---|---|
| F0 dynamics | PASS_FAMILY_LEVEL | explicit master-equation / continuous hybrid / covariant path-integral frameworks exist |
| F1 GR/classical limit | PASS_PARTIAL | GR limit is built into the program; exact nonlinear realization must still be frozen |
| F2 consistency | BLOCKED_NONLINEAR_CLOSURE | CP/covariance strengthened in 2026, but canonical nonlinear closure for the same covariant gravity realization is not yet demonstrated here |
| F3 hierarchy | STRONG_PARTIAL | stochastic metric + quantum matter + decoherence/backreaction structures are explicit |
| F4 comparator role | C3b_PARENT | if consistent, this remains a strong classical-spacetime comparator for KG |
| F5-F7 | BLOCKED | no promotion before nonlinear consistency object is explicit |

## Important negative/positive distinctions

- **Do not say:** “postquantum classical gravity is inconsistent because the 2022 algebra did not close.” That result is scoped to a broad discrete class and permits extra constraints.
- **Do not say:** “the 2026 covariant path integral proves the full nonlinear gravitational constraint algebra closes.” The published CP/covariance result is not the same statement.
- **Do retain:** the linearized conserved-kernel C3b comparator from S2-M04 as valid in its declared sector.
- **Do require:** one concrete nonlinear matter-coupled realization in which covariance, Bianchi identities, constraints and physical DOF are checked together.

## Candidate Gravity design lesson

A future KG model must distinguish **representation covariance** from **dynamical constraint consistency**. Writing a covariant action/path integral is not enough if the source/backreaction/noise structure fails the corresponding Ward/Bianchi/constraint algebra after quantization or hybridization.

This is another form of rigidity: the same parent dynamics must satisfy symmetry identities and physical-state reduction simultaneously.

## Current blocker

`PQCG_SAME_REALIZATION_NONLINEAR_CONSTRAINT_CLOSURE`:

1. freeze one explicit 2026 covariant classical-spacetime + quantum-matter gravitational action/path integral;
2. identify its canonical or equivalent nonlinear constraint content;
3. determine whether the additional constraints found necessary in the older discrete class have analogues or disappear in the covariant continuous formulation;
4. count the physical gravitational/stochastic DOF after all constraints;
5. only then classify T3-04 as scoped PASS, scoped FAIL, or BLOCKED_MISSING_REQUIRED_OBJECT.

## Operational completion estimate

**45%**.

## Sources

1. J. Oppenheim, Z. Weller-Davies, JHEP 02 (2022) 080, nonlinear constraint analysis for the discrete class.
2. J. Oppenheim, C. Sparaciari, B. Soda, Z. Weller-Davies, Phys. Rev. A 113, 052223 (2026), general continuous hybrid classical-quantum dynamics.
3. J. Oppenheim, Z. Weller-Davies, Phys. Rev. X 16, 031007 (2026), covariant completely-positive path-integral formulation.
4. J. Oppenheim, M. Sajjad, arXiv:2605.05375 (2026), linearized stochastic gravitational modes retained as the scoped S2-M04 control.
