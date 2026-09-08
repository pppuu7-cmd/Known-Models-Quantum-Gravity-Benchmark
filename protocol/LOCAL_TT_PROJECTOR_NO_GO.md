# Exact Finite-Range Local TT-Projector No-Go

**Status:** permanent MISP2-QCA design lemma.  
**KMQGB iteration:** 063.  
**Scope:** exact translation-invariant finite-range **linear projector** directly onto the transverse / transverse-traceless physical subspace on an infinite homogeneous lattice.  
**Not a no-go:** local gauge-redundant formulations, constrained local codes, emergent low-energy TT sectors, approximate finite-range projectors, or explicitly nonlocal encodings.

## 1. Statement

### Vector version

Let `P` be a translation-invariant finite-range linear operator on vector fields on `Z^d`, `d>=2`.

Its Fourier symbol has the finite Laurent form

`P(k) = sum_{r in R} P_r exp(i k.r)`

for a finite neighborhood `R`.

Therefore every matrix element of `P(k)` is a trigonometric polynomial and is continuous (indeed real-analytic) on the Brillouin torus.

Suppose `P(k)` is required, for every sufficiently small nonzero `k`, to be the exact orthogonal projector onto the continuum transverse subspace

`k^perp`.

Then

`P_T(k) = I - k k^T / |k|^2`

(up to a lattice derivative symbol with the same small-k directional structure).

As `k -> 0`, `P_T(k)` has no direction-independent limit. Along `k=eps e_x`,

`P_T -> I - e_x e_x^T`,

whereas along `k=eps e_y`,

`P_T -> I - e_y e_y^T`.

These limits differ.

A continuous finite-range Fourier symbol cannot equal a function with distinct directional limits on a punctured neighborhood of the origin.

Therefore **no exact translation-invariant finite-range linear projector onto the transverse subspace exists**.

### Spin-2 TT version

In three spatial dimensions define

`pi_ij(k) = delta_ij - k_i k_j/|k|^2`

and the standard symmetric traceless transverse projector

`Pi_ij,kl(k) = 1/2 (pi_ik pi_jl + pi_il pi_jk) - 1/2 pi_ij pi_kl`.

Because `Pi` is built from `pi`, its limit at `k->0` is also direction-dependent. Hence the same continuity contradiction applies.

Therefore **no exact translation-invariant finite-range linear projector can map an unconstrained local symmetric tensor directly onto the physical TT graviton subspace at every nonzero momentum in a neighborhood of `k=0`**.

---

## 2. Lattice derivative version

A local lattice divergence is represented in momentum space by a vector symbol `q_i(k)` that is a trigonometric polynomial and satisfies

`q_i(k) = C_ij k_j + O(k^2)`

near a regular continuum point, with nonsingular `C` for an ordinary derivative realization.

The exact orthogonal projector onto `q(k)^perp` is

`P_q(k) = I - q(k) q(k)^dagger / [q(k)^dagger q(k)]`.

The denominator vanishes at the zero mode. After normalization, the limiting projector depends on the direction of `C k`, so the same obstruction remains.

Thus replacing derivatives by finite differences does not remove the exact local-projector problem.

---

## 3. Proof as a topology/continuity obstruction

The argument does not require a detailed action or graviton dynamics.

1. finite-range translation invariance -> Fourier symbol is a finite Laurent polynomial;
2. finite Laurent polynomial -> continuous at the zero mode;
3. exact physical transverse subspace depends on momentum direction;
4. its orthogonal projector has different limits along different rays approaching zero;
5. equality on a punctured neighborhood would force the finite-range symbol to inherit those incompatible limits;
6. contradiction.

The obstruction is therefore kinematic and exact in the stated scope.

It can also be viewed as the position-space fact that the continuum transverse projector contains

`partial_i partial_j Delta^{-1}`,

so exact TT extraction uses an inverse Laplacian and is spatially nonlocal.

---

## 4. What this does NOT prove

This lemma must not be overextended.

It does **not** rule out:

- local linearized gravity written with gauge-redundant metric/tetrad/connection variables;
- local lattice gauge theory with Gauss/constraint equations;
- a finite-depth local unitary whose **physical code subspace** has two helicity-2 modes;
- nonlocal observables constructed from local microscopic variables;
- approximate/quasi-local projectors valid below a finite accuracy/correlation length;
- finite volume, where zero-mode treatment and boundary conditions require a separate statement;
- explicitly `D-nonlocal` Candidate Gravity branches.

The correct conclusion is architectural:

> exact physical transversality should emerge from constraints/gauge reduction, not be hard-coded as a finite-range local projection operator.

---

## 5. MISP2-QCA consequence

For the `S-local` MISP2-QCA branch, Q1 must use local redundant variables.

Allowed starting architectures include, for example,

- symmetric tensor registers with local gauge generators;
- tetrad/frame registers with local Lorentz/spatial gauge redundancy;
- connection/link plus conjugate electric/triad registers;
- local stabilizer/constraint ancillas enforcing discrete analogues of Gauss/momentum/Hamiltonian constraints.

The physical projector may be used analytically **after** solving the constraints and going to momentum/observable space. It must not be confused with a microscopic finite-range gate.

### Q1 fail-closed rule

If a proposed "local spin-2 QCA" defines each cell directly as only two TT helicities and relies on the exact momentum-dependent TT projector to update local cells, classify

`BLOCKED__MICROSCOPIC_TT_PROJECTION_IS_NONLOCAL`.

It may proceed only by

1. reintroducing local gauge-redundant variables/constraints, or
2. explicitly declaring a nonlocal microscopic branch and re-entering the `D-nonlocal` comparator/causality audit.

---

## 6. Stronger formulation for exact physical-subspace encoding

The physical helicity bundle over momentum directions is not a fixed momentum-independent two-dimensional subspace of one local tensor register. Its embedding changes with the direction of `k`.

A finite local register can still support the bundle through a redundant ambient representation and constraints. What is forbidden by the lemma is identifying the momentum-dependent physical projector itself with an exact finite-range translation-invariant microscopic operator.

This distinction prevents a common false shortcut:

`two physical helicities` does not imply `two microscopic local components`.

---

## 7. Executable witness

Reference implementation:

`code/local_tt_projector_no_go_reference.py`.

It checks that

- vector transverse projectors along orthogonal rays have a nonzero direction-limit separation;
- spin-2 TT projectors along the same rays likewise differ;
- the separation is independent of the small radial scale `eps`, demonstrating that it is not a finite-resolution numerical artifact.

The executable is a witness to the directional-limit contradiction, while the theorem follows analytically from finite-range Fourier continuity.

---

## 8. Literature anchors

The standard momentum-space transverse projector is

`pi^mu_alpha = delta^mu_alpha - p^mu p_alpha/p^2`,

and the spin-2 transverse-traceless projector is built quadratically from it. In position space the corresponding inverse `p^2` is an inverse Laplacian/d'Alembertian, exposing the nonlocality of exact projection.

This lemma packages that standard structure into the finite-range QCA design language required by KMQGB.

---

## 9. Score consequence

This is a necessary design lemma, not a P4 parent.

- R1: unchanged;
- R2: unchanged under the frozen rubric;
- R3: externally controlled and unchanged by this lemma;
- R4: unchanged until an explicit interacting finite-freedom parent survives A1-A4.

The scientific gain is narrower Q1 search space: future MISP2 constructions must begin from a local constrained/gauge-redundant architecture rather than an impossible exact local TT-only projector.
