# O3 q-Difference / q-Pochhammer Uniqueness Control

**Status:** exact A2 positive control / A3 comparator-risk audit.  
**KMQGB iteration:** 076.  
**Purpose:** test whether a finite discrete-scale recursion can uniquely generate a non-rational kernel from finite data without hiding arbitrary functional freedom.

## 1. Finite parent recursion

Take a complex function `F(z)` with

- `F(0)=1`;
- continuity/analyticity in a neighborhood of the origin;
- fixed `q` with `0<|q|<1`;
- finite constants `a,b`;
- exact recursion

`F(q z) = [(1-b z)/(1-a z)] F(z)`.

The parent data are only `(q,a,b)` plus the normalization at the fixed point `z=0`.

## 2. Exact solution

Iterating `N` times gives

`F(q^N z) = F(z) Π_{j=0}^{N-1} [(1-b q^j z)/(1-a q^j z)]`.

Since `q^N z -> 0` and `F(0)=1`, taking `N -> infinity` yields

`F(z) = Π_{j=0}^{infinity} [(1-a q^j z)/(1-b q^j z)]`.

Equivalently, using q-Pochhammer notation,

`F(z) = (a z;q)_infinity / (b z;q)_infinity`.

This is non-rational for generic nontrivial parameters and has an infinite zero/pole structure generated from finite parent data.

## 3. Uniqueness

Let `F1,F2` obey the same recursion and fixed-point normalization. Their ratio `R=F1/F2` satisfies

`R(qz)=R(z)`.

Iterating,

`R(z)=R(q^N z)`.

Continuity at `0` and `q^N z -> 0` give

`R(z)=R(0)=1`.

Hence `F1=F2` throughout the connected domain before singularities.

Therefore this recursion genuinely solves the KMQGB functional-freedom problem:

`finite q-difference law + fixed-point normalization -> unique non-rational function`.

Classification at A2:

`A2_PASS__FINITE_Q_DIFFERENCE_RULE_FIXES_INFINITE_PRODUCT`.

## 4. Why this is stronger than a form-factor ansatz

Writing down a q-Pochhammer function by hand would not pass A2. Here the function is derived as the unique solution of a finite recursion.

This is the discrete-scale analogue of the Iter075 semigroup-to-exponential uniqueness theorem and proves that O3 finite-rule generation is not limited to exponential kernels.

## 5. A3 comparator audit

The mathematical structure is immediately adjacent to a strong registered amplitude/string comparator family.

Cheung and Remmen, *Stringy Dynamics from an Amplitudes Bootstrap*, arXiv:2302.12263, derive the Coon amplitude after lifting the spectrum to a q-deformed integer spectrum and also derive deformed Virasoro-Shapiro families.

Ambrosino and Haouzi, *Meromorphic amplitudes from 3-dimensional supersymmetry*, arXiv:2606.18331, identify the Coon amplitude with a 3d `N=2` half-index of the XYZ model with nontrivial boundary conditions and construct a meromorphic modification via an elliptic completion.

Thus q-Pochhammer/q-gamma recursion is not an empty unexplored architecture. In its natural dual-resonant scattering realization it is already connected to q-deformed string/amplitude and ordinary UV QFT comparator structures.

Current classification:

`A3_FAIL_FOR_NATURAL_DUAL_RESONANT_REALIZATION__COON_QSTRING_QFT_COMPARATOR`.

The abstract q-difference theorem itself is not globally ruled out for all possible gravitational uses, but it does not provide gravity attribution or a novel spin-2 hard relation.

## 6. A4 requirement remains open

To become a real O3 survivor, a q-difference law would need a **gravity-specific microscopic origin** that derives

- the relevant tensor/helicity structure;
- the map from its q-recursion to a normalized four-graviton amplitude or cross-representation invariant;
- the same-parent retarded/CTP prescription;
- and a relation not equivalent to Coon/q-string/Virasoro-Shapiro/known QFT realization.

Without those, `q` is only a deformation parameter and the recursion is a mathematical generator, not Candidate Gravity.

## 7. Search consequence

The first two exact finite-rule uniqueness classes now have the pattern

- continuous additive semigroup -> exponential -> known entire/nonlocal comparator;
- discrete multiplicative/q-difference recursion -> q-Pochhammer -> known q-string/dual-resonant/QFT comparator neighborhood.

This suggests a deeper search constraint: a new O3 law must not merely encode continuous or discrete one-parameter composition in a way that reproduces already-known special-function amplitude architectures.

## 8. Executable witness

`code/o3_qdifference_uniqueness_reference.py` verifies numerically that the truncated infinite product converges and satisfies the finite q-difference equation to machine precision for a generic complex test point.

## 9. Score consequence

No P4 credit is awarded. R4 remains 45%.
