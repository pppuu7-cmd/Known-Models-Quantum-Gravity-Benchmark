# Iter479 preregistration — source Toller leading magnetic coefficient rank

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Parent: main through Iter477–478 recovery.

## Question
Given Iter477's exact nonzero one-wedge branch leading coefficients `C_m` and the source Eq.(7) magnetic reconstruction `T = U1 diag(t_m) U2`, can the leading `beta^(-(2j+1))` coefficient disappear solely because of the internal left/right magnetic reconstruction?

## Frozen algebraic model
For one source branch at fixed `j,rho`:
`t_m(beta) = C_m beta^(-(2j+1)) + lower-order terms`, with every `C_m != 0` in the qualified Iter477 source scope.
Then the leading full magnetic matrix is
`L = U1 diag(C_m) U2`,
where Eq.(7) uses SU(2) Wigner matrices `U1,U2` and hence they are invertible/unitary.

The rank certificate is algebraic: multiplication by invertible matrices preserves rank, so if all diagonal `C_m` are nonzero then `rank(L)=2j+1` and the leading term cannot vanish identically inside the single-wedge magnetic reconstruction.

## Frozen panel
A. coefficient nonvanishing: gamma={7,8}, j={1,2,5}, every integer m in [-j,j], rho=gamma*j, using the exact Iter477 DLMF/source coefficient formula.
B. explicit Eq.(7) numerical control at j=1 using the four angle lanes inherited from Iter457.
C. determinant identity control: `det(L)=det(U1)*det(diag(C))*det(U2)`.
D. negative control: forcibly zero one diagonal leading coefficient and require determinant/rank loss.

## PASS rule
PASS iff:
1. every frozen source leading coefficient is finite and nonzero;
2. all j=1 lane matrices satisfy unitarity/invertibility and the determinant identity at high precision;
3. all correct leading matrices are nonsingular/full rank;
4. every forced-zero diagonal negative control is singular.

PASS label: `ITER479_SOURCE_TOLLER_LEADING_MAGNETIC_MATRIX_FULL_RANK_QUALIFIED_SCOPED`.

## Scope guards
A PASS rules out only **cancellation internal to a single-wedge Eq.(7) magnetic reconstruction**. It does not rule out cancellation after contraction with intertwiners/boundary tensors, between different wedges, under gauge/group integration, under angular integration, or in a full K5 collision stratum. It is not a causal-vertex divergence theorem and must not be compared directly to Iter471 pcrit as a contracted collision exponent. D7-S2 remains fail-closed.