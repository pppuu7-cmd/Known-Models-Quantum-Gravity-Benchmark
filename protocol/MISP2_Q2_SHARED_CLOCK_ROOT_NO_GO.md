# MISP2 Q2 — Shared-Clock Fractional-Root Locality Obstruction

**Status:** exact no-go for a specific repair of the spin-2 representation-lift control.  
**KMQGB iteration:** 065.  
**Scope:** same BCC translation lattice, finite-range translation-invariant update, and the attempt to repair the factor-four spin-2 light-cone mismatch by replacing the Weyl group element with a continuous fourth root before taking the spin-2 representation.  
**Not a no-go:** all direct spin-2 QCAs, composite constructions, larger-register circuits, or other prospectively derived updates.

## 1. Blocked repair

The Q2 representation-lift control gives

`U_2(k)=Sym^4[A(k)]`

and physical extreme-helicity phases `±4 omega(k)`, while the fundamental Weyl matter sector has `±omega(k)`.

A tempting repair is to choose a group element `B(k)` satisfying

`B(k)^4 = A(k)`

and use

`U_2,repair(k)=Sym^4[B(k)]`.

Then the spin-2 extreme phase would be `±omega(k)` and the IR speed would match the matter clock.

The question is whether such `B(k)` can remain an exact finite-range symbol on the **same** translation lattice.

## 2. Restriction to one BCC momentum axis

For the prospectively frozen `+` BCC Weyl automaton and `k=(k_x,0,0)`, define

`theta = k_x/sqrt(3)`.

The exact symbol reduces to

`A(theta)=cos(theta) I - i sin(theta) sigma_x = exp[-i theta sigma_x]`.

In the fixed `sigma_x` eigenbasis,

`A(theta)=diag(z^-1,z)`, `z=e^{i theta}`.

A translation-invariant finite-range operator on the same lattice restricts along this one-parameter subgroup to a matrix whose entries are finite Laurent polynomials in `z` with **integer powers**.

## 3. Laurent-ring proof

Suppose a finite-range matrix `B(z)` obeys

`B(z)^4=A(z)`

for all `z` on an open arc and hence algebraically by continuation.

Because `B` commutes with its fourth power,

`[B(z),A(z)]=0`.

For generic `z` the two eigenvalues `z^-1` and `z` of `A` are distinct. Therefore `B` is diagonal in the same constant `sigma_x` eigenbasis:

`B(z)=diag(b_-(z),b_+(z))`,

where `b_±(z)` are finite Laurent polynomials.

They must satisfy

`b_-(z)^4=z^-1`,

`b_+(z)^4=z`.

Consider any nonzero finite Laurent polynomial

`b(z)=sum_{m=m_min}^{m_max} c_m z^m`,

with nonzero endpoint coefficients. The exponent width is

`w(b)=m_max-m_min`.

For products,

`w(b^4)=4 w(b)`.

A monomial target `z^q` has width zero, so `b^4=z^q` implies `w(b)=0`; thus `b(z)=c z^m` is itself a monomial. Then

`c^4 z^(4m)=z^q`,

so `4m=q`.

For `q=+1` or `q=-1`, no integer `m` exists.

Therefore no finite Laurent-polynomial `b_±(z)` exists, and hence no exact finite-range same-lattice `B(z)` exists with `B^4=A`.

## 4. Equivalent periodicity witness

The principal continuous root is

`B_pr(theta)=exp[-i theta sigma_x/4]`.

It contains Fourier characters `exp(±i theta/4)`, corresponding to quarter-lattice exponents rather than integer translation characters. In particular it is not `2pi`-periodic in `theta` even though the original lattice character `z=e^{i theta}` is.

This is a simple witness; the Laurent-ring argument above is the exact proof and does not depend on choosing the principal branch.

## 5. Classification

The attempted repair is classified

`BLOCKED__SAME_LATTICE_FRACTIONAL_ROOT_IS_NOT_FINITE_RANGE`.

Combined with Iter064:

`same Weyl group element -> exact finite range but spin2 speed x4`,

`fourth-root group element -> correct extreme phase but not a finite-range symbol on the same translation lattice`.

This closes the simplest representation-lift repair loop.

## 6. What remains open

The obstruction does not rule out a directly constructed five-dimensional or larger spin-2 update whose entries are different finite Laurent polynomials and whose physical helicity branches have the correct common-clock slope.

Allowed next Q2 branches include prospectively frozen

- direct `5x5` constrained finite-range unitary symbols not obtained as `Sym^4` of one Weyl element;
- doubled/chiral or curvature-pair registers;
- finite-depth products of several local gates whose combined physical spin-2 generator is correctly normalized;
- composite/quantum-link constructions;
- local constraint ancillas that alter the physical dispersion while preserving exact microscopic unitarity.

Each branch must retain fixed finite microscopic freedom and pass the historical higher-spin/discrete-QFT comparator audit.

## 7. General spin-j corollary for naive representation lifts

For a fundamental `SU(2)` element

`A=exp[-i omega n.sigma]=exp[-i 2 omega J_(1/2,n)]`,

the same element in spin `j` gives extreme-helicity phases

`±2 j omega`.

Matching the fundamental phase by a pure group-element root would require a `2j`-th root of the primitive lattice character on the axial control. If the primitive exponent is not divisible by `2j` in the lattice character group, the same Laurent-ring obstruction applies.

For `j=2`, the required root is fourth order and the primitive BCC axial exponent `±1` is not divisible by four.

## 8. Executable witness

Reference:

`code/misp2_shared_clock_root_no_go_reference.py`.

The script checks

- the exact axial reduction of the BCC Weyl matrix;
- nonperiodicity of the principal fourth root under the primitive `2pi` character period;
- integer-exponent divisibility failure for finite Laurent monomial roots;
- the phase repair `Sym^4(B_pr)` would have produced if locality were ignored.

## 9. Score consequence

This is another exact Q2 elimination, not a P4 survivor.

R1/R2/R3/R4 remain unchanged under their frozen rubrics. The next constructive target is a **direct common-clock constrained spin-2 finite-range update**, not another representation-root repair.
