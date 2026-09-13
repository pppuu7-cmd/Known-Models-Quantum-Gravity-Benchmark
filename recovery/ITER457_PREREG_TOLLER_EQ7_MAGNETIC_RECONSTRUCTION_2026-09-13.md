# Iter457 preregistration — source Eq.(7) Toller magnetic reconstruction

Date frozen: 2026-09-13
Status: preregistered before implementation/production.

## Source object
Primary source: Bianchi, Chen, Gamonal, arXiv:2601.23162v1, Eq. (7). For the Cartan decomposition
`g = U1 exp(beta sigma_z/2) U2`, `U1,U2 in SU(2)`, `beta>0`,

`T^(±,rho,k)_{jm,ln}(g) = sum_{p=-min(j,l)}^{min(j,l)} D^(j)_{mp}(U1) t^(±,rho,k)_{jlp}(beta) D^(l)_{pn}(U2)`.

The same source states Eq. (5), `T+ + T- = D`. No ordinary representation-composition law is assumed for `T±`.

## Scientific objective
Qualify the full magnetic-index reconstruction implied by source Eq. (7) for the already-qualified Iter456 reduced layer `k=j=l=1`, `p=-1,0,+1`. This gate does not extend to arbitrary spins and does not perform the noncompact vertex integral.

## Frozen inputs
- Iter456 source-faithful reduced `d_p(beta), t+_p(beta), t-_p(beta)` formulas, unchanged.
- precision: 80 decimal digits.
- `rho` panel: `[-2.3,-1.7,-0.6,0.35,0.9,1.6,2.7]` (real and off poles).
- `beta` panel: `[0.35,0.8,1.2,pi/2,2.1]`.
- four independent rotation lanes, each with deterministic Euler-angle tuples `(U1,U2)`; no data-dependent tuning.
- complete 3x3 magnetic matrix (`m,n = +1,0,-1`) in every case.

## Two independent SU(2) implementations
A. closed-form spin-1 Wigner `D(alpha,theta,gamma)=exp(-i m alpha) d^1_{mn}(theta) exp(-i n gamma)`;
B. generator-exponential construction `exp(-i alpha Jz) exp(-i theta Jy) exp(-i gamma Jz)`.

The two routes must agree before either is used as a scientific witness.

## Frozen predicates
1. **SU(2) convention control**: route A and B agree entrywise to `<=1e-38`; each is unitary to Frobenius residual `<=1e-38`.
2. **Eq.(7) implementation independence**: explicit `sum_p` reconstruction and matrix-product `D(U1) diag(t_p) D(U2)` agree entrywise for each of `T+`, `T-`, and reconstructed `D` to `<=1e-38 + 1e-35*|entry|`.
3. **Full-magnetic additive recovery**: every 3x3 entry satisfies `T+ + T- = D` to `<=1e-38 + 1e-35*|D_entry|`.
4. **Cartan U(1) redundancy**: for preregistered `chi in [0.23,-0.71,1.19]`, replacing `(U1,U2)` by `(U1 Rz(chi), Rz(-chi) U2)` leaves each reconstructed matrix unchanged to Frobenius relative/absolute residual `<=1e-35`.
5. **Left/right SU(2) covariance of the reconstruction map**: deterministic extra rotations `V_L,V_R` must satisfy reconstructed `T(V_L U1, U2 V_R)=D(V_L) T(U1,U2) D(V_R)` to `<=1e-35` for both branches and `D`.
6. **Wrong-p-index negative control**: reverse the association `p -> -p` in the reduced diagonal while keeping source Wigner factors fixed. It must violate the correct reconstructed Wigner `D` additive target by Frobenius residual `>1e-8` in at least 80% of tested nondegenerate panel points.
7. **Wrong-right-conjugation negative control**: replace the right source factor `D(U2)` by `conj(D(U2))` in one branch only. It must violate additive recovery by `>1e-8` in at least 80% of tested nondegenerate panel points.

## Aggregate rule
PASS only if all four lanes are valid and all frozen predicates pass:
`ITER457_TOLLER_EQ7_FULL_MAGNETIC_RECONSTRUCTION_QUALIFIED_SCOPED`.

Valid scientific predicate failure:
`SCIENTIFIC_FAIL_ITER457_TOLLER_EQ7_MAGNETIC_RECONSTRUCTION`.

Failure before meaningful predicate evaluation:
`INFRASTRUCTURE_OR_NUMERICAL_FAIL`.

## Interpretation lock
A PASS qualifies only the Eq. (7) Cartan magnetic reconstruction for `k=j=l=1` over the frozen finite panel. It does not establish an arbitrary-spin theorem, a group-representation law for `T±`, absolute integrability, a source-defined distributional boundary value of the full vertex, causal-vertex finiteness, D7-S2 closure, or terminal D7 classification.
