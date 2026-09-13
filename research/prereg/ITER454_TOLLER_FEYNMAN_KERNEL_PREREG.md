# Iter454 — Toller Feynman-kernel source qualification

Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION
Date: 2026-09-13

## Goal
Qualify the source-defined scalar spectral projector/kernel layer needed before any physical Eq.(3)/(7) Toller matrix-element insertion. This gate does NOT claim a complete physical Toller kernel and does NOT evaluate the causal vertex.

Primary source: Bianchi–Chen–Gamonal, arXiv:2604.24945v1, especially Eqs. (11)–(17): Toller poles, t+ + t- = d, Cartan reconstruction, and the Feynman projector kernel P_jl(tilde-rho;rho).

## Frozen independent lanes
Four lanes with fixed tuples (j,l,rho):
- L0=(0,0,0.37)
- L1=(1,1,0.73)
- L2=(1,2,1.11)
- L3=(2,2,1.57)
All use 80 decimal-digit arithmetic.

## Frozen tests
For each lane:
1. P_jl(rho;rho)=1 within 1e-60.
2. Source Toller-pole locations i*rho=-j,...,l are enumerated exactly.
3. At every source pole represented as tilde-rho=-i*n (n=-j,...,l), the reciprocal-gamma factor 1/Gamma(-j-i*tilde-rho) is numerically zero/finite-limit compatible to <=1e-50 when approached with delta=1e-30. This is a local cancellation prerequisite, not a full meromorphic proof.
4. The Sokhotski–Plemelj branch difference, tested on the normalized Gaussian control f(x)=exp(-(x-rho)^2), converges to f(rho)=1 under symmetric finite integration as epsilon decreases through [0.2,0.1,0.05,0.025]. Frozen requirement: last absolute error < 0.03 and strictly lower than first error.
5. A deliberately wrong same-sign branch combination must NOT approximate the delta reconstruction: last absolute error > 0.2.

## Frozen aggregate classification
PASS only if all 4 lanes pass all 5 tests: `ITER454_TOLLER_FEYNMAN_PROJECTOR_KERNEL_QUALIFIED_SCOPED`.
Otherwise: `SCIENTIFIC_FAIL_ITER454_TOLLER_FEYNMAN_PROJECTOR_KERNEL` if numerical predicates execute validly but fail; `INFRASTRUCTURE_OR_NUMERICAL_FAIL` if execution/precision/integration is invalid.

## Interpretation lock
A PASS qualifies only the scalar source-defined Feynman projector/kernel prerequisite. It does not supply the full reduced Toller t-matrix, Wigner-d implementation, Ruhl-phase conversion, Eq.(7) magnetic reconstruction, noncompact vertex convergence, regulator removal, normalization, D7-S2 closure, or any terminal model classifier. No thresholds may be changed after production results are viewed.
