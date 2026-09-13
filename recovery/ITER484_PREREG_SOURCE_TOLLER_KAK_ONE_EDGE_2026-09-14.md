# Iter484 preregistration — source-faithful one-edge Toller/KAK reconstruction

Date frozen: 2026-09-14
Status: FROZEN BEFORE IMPLEMENTATION/PRODUCTION
Parent authorities: terminal Iter456 reduced Toller qualification and terminal Iter483 common-node SL(2,C) geometry.
Source locks: `sources/arxiv_2601_23162v1_causal_vertex.json`, `sources/arxiv_2604_24945v1_toller_cartan.json`.

## Scientific question
Can the already-qualified source reduced Toller functions from Iter456 be lifted through the source Eq.(7)/Eq.(13) Cartan decomposition to a stable full one-edge magnetic Toller matrix on the already-qualified shared-node noncompact SL(2,C) elements of Iter483, with convention, KAK-gauge, inversion/reversal and nonrepresentation controls all satisfied?

This gate tests the missing bridge between Iter456 and Iter483. It does not evaluate the ten-edge network or a Haar integral.

## Frozen object and realization
- representation sector: `k=j=l=1`, magnetic indices `m=-1,0,+1`, exactly as Iter456;
- reduced functions `d_m(beta), t+_m(beta), t-_m(beta)` are imported unchanged from `code/iter456_reduced_toller_appendixb.py`;
- real `rho` witness panel inherited from the positive nonsingular Iter456 panel: `[0.35,0.9,1.6,2.7]`; since `j=1`, these are also gamma-simple `gamma=rho` witness values, but no physical gamma selection is inferred;
- group elements use the Iter483 deterministic node construction without modification;
- one frozen edge per lane: `h_01=g_1^{-1}g_0`, for the 8 Iter483 lanes `panel in {A,B,C,D}` x `regime in {mild,strong}`;
- Cartan convention: `h=U1 A(beta) U2`, `A(beta)=diag(exp(beta/2),exp(-beta/2))`, `beta>=0`;
- KAK is obtained by SVD with determinant phases redistributed so `U1,U2 in SU(2)` exactly up to numerical tolerance;
- full spin-1 matrices use the canonical symmetric-square representation `D^1(U)` in magnetic order `(-1,0,+1)`.

## Frozen independent lanes
Eight production lanes run independently (`A-mild` ... `D-strong`) with `fail-fast:false`. Each lane evaluates all four rho witnesses. Aggregate verdict is formed only after all 8 lane artifacts are present.

## Frozen predicates
A lane is valid only if its frozen edge has `beta>1e-8`, all reduced source evaluations are finite, and all controls below are numerically meaningful.

1. **Cartan reconstruction**: `||U1 A(beta) U2-h||_max < 1e-10`; `U1,U2` unitarity and determinant-one residuals each `<1e-10`.
2. **Rapidity continuity with Iter483**: Cartan `beta` agrees with Iter483 singular-value/polar rapidity for the same edge within `1e-10`.
3. **Full magnetic additive identity**: for every rho, full matrices reconstructed as `T+=D1 diag(t+_m) D2`, `T-=D1 diag(t-_m) D2`, `D=D1 diag(d_m) D2` satisfy `||T+ + T- - D||_max <= 1e-11`.
4. **KAK axial-gauge invariance**: with frozen `theta=0.731`, replace `U1->U1 Rz(theta)` and `U2->Rz(-theta)U2`; both Toller branches and D must change by `<1e-10` max norm.
5. **Reduced branch conjugation/reversal control**: for real rho and each m, the source gamma-simple identity `conj(t^(+,rho,1)_{11m}) = t^(-,rho,1)_{11,-m}` must hold to relative/absolute tolerance `1e-35` under the already-qualified Iter456 formulas.
6. **Inversion KAK control**: using the Weyl element `W=[[0,-1],[1,0]]`, the predicted Cartan data for `h^{-1}`, `(U2^{-1} W, beta, W^{-1} U1^{-1})`, must reconstruct `h^{-1}` within `1e-10`; a direct SVD-KAK reconstruction of `h^{-1}` must produce the same full Toller matrices as the predicted KAK within `1e-9` for both branches.
7. **Naive-polar negative control**: replacing the positive polar factor by an axis-z boost without its diagonalizing SU(2) rotations, i.e. `h_bad=A(beta) U_polar`, must fail to reconstruct the frozen generic edge by `>1e-4` in every lane. This guards against identifying Iter483 polar factors directly with source KAK factors.
8. **Toller nonrepresentation negative control**: for a frozen second relative element in the same lane, compare `T+(h2 h1)` with `T+(h2)T+(h1)` at all rho witnesses. At least one rho per lane must have max-norm mismatch `>1e-5`. No group-composition property for T is assumed.

## PASS / FAIL / BLOCKED contract
PASS iff all 8 lanes are valid and predicates 1–8 pass:
`ITER484_SOURCE_TOLLER_KAK_ONE_EDGE_RECONSTRUCTION_QUALIFIED_SCOPED`.

A valid lane violating any positive predicate or failing to activate either negative control is:
`SCIENTIFIC_FAIL_ITER484_SOURCE_TOLLER_KAK_ONE_EDGE`.

If the source-locked reduced object cannot be imported/evaluated or the frozen KAK convention is undefined for a frozen edge before predicates can be tested, classify:
`BLOCKED_OR_INFRASTRUCTURE_ITER484`.
Thresholds and witness panels may not be changed after production output is seen.

## Interpretation ceiling
PASS qualifies only the source-faithful full one-edge magnetic reconstruction in the frozen j=1 witness sector on the Iter483 panels. It does not prove arbitrary-spin validity, a ten-edge contraction, Haar/group convergence, spectral convergence, a causal-vertex value, D7-S2 closure, any terminal D7 classifier, or Candidate Gravity.

## Next if PASS
The next admissible D7-S2 gate is the ten-edge boost-dependent Toller magnetic network built from five shared node variables, preserving the source edge ordering/sign convention and genuine boundary intertwiners, before any Haar/group-integration conclusion.
