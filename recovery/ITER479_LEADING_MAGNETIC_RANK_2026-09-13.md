# Iter479 — source Toller leading magnetic coefficient rank — 2026-09-13

## Authority
- branch: `research/iter479-toller-leading-magnetic-rank`
- preregistration: `19d8d6d88ee542e43f721dadc7e9bee3900e1944`
- implementation: `ad29c9cd2c8460fe86ef7c5b59090b1265dbc2d5`
- workflow head: `ac607e820ba3093e113fca6d2e24568043d2b33a`
- workflow run: `34772768304`
- job: `103765265032`, SUCCESS
- artifact: `10322656348`
- digest: `sha256:849ecf0db0438e36904664016fcdcf1589f621c2186658648de56d8f84e46f91`

## Scientific classification
`ITER479_SOURCE_TOLLER_LEADING_MAGNETIC_MATRIX_FULL_RANK_QUALIFIED_SCOPED`

All frozen checks pass:
- every source leading coefficient on gamma={7,8}, j={1,2,5}, every integer m and both Toller branches is finite and nonzero;
- explicit j=1 Eq.(7) Wigner lanes are unitary to about 1e-91 residual;
- `det(U1 diag(C_m) U2) = det(U1) prod_m C_m det(U2)` holds at about 1e-91 relative residual;
- every correct leading matrix is nonsingular/full-rank;
- forcing any one diagonal coefficient to zero makes the negative-control matrix singular.

Representative determinant magnitudes in the explicit j=1 lanes are about `1.00758e-5` for gamma=7 and `3.07237e-6` for gamma=8; negative controls give determinant zero or numerical residual at approximately 1e-97.

## Algebraic certificate
Iter477 gives nonzero one-wedge branch coefficients `C_m` in
`t_m(beta) = C_m beta^(-(2j+1)) + lower order`.
The source Eq.(7) reconstruction has leading matrix
`L = U1 diag(C_m) U2`.
Since `U1,U2` are invertible/unitary and all diagonal entries `C_m` are nonzero, multiplication by the invertible matrices preserves rank and
`rank(L)=2j+1`.
Therefore the leading individual-branch singularity cannot disappear identically **solely inside the single-wedge magnetic Eq.(7) reconstruction**.

## Scope lock
This does NOT rule out cancellation after contraction with intertwiners or boundary tensors, among multiple wedges, under gauge/group integration, under angular integration, or in a full K5 collision stratum. It is not a physical causal-vertex divergence theorem and the one-wedge order `2j+1` must not be compared directly with Iter471 collision `pcrit` as if they were the same contracted exponent.

## D7 state
- D7-S2: `NOT_CLOSED`.
- D7-S3: `NOT_CLOSED`.
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`.
- D7-S5: `NOT_AUTHORIZED`.
- Candidate Gravity: inactive/false.

## Working readiness rubric
Keep `D2≈82%`, `D4≈68%`, `D7≈56%`, integrated `≈67%`. Iter479 materially narrows the cancellation locus but does not close a frozen D7 prerequisite.

## Next permitted S2 gate
Locate a genuinely source-backed EPRL intertwiner/boundary-tensor contraction compatible with the causal Toller magnetic indices. If such a contraction object is explicit/executable, preregister a leading-coefficient contraction test with negative controls. If it is absent, record a scoped BLOCKED result rather than inventing a contraction.