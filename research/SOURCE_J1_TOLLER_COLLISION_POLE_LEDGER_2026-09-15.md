# Source j=1 Toller collision-pole ledger

Date: 2026-09-15
Status: `DERIVED_KMQGB` local asymptotic lemma; no full collision verdict

## Object

Use the exact j=1 source formulas already frozen in `code/iter499_arb_core.py::source_coeffs`, with real `rho != 0` and boost Cartan parameter `beta -> 0+`.

The magnetic ordering below is `m=(-1,0,+1)`.

Define

`A(rho) = 3 i / [4 rho (1+rho^2)]`.

## Cubic leading pole

Direct Laurent expansion of the exact source formulas gives

`t_plus(beta) = A(rho) beta^-3 (1,-2,1) + O(beta^-2)`,

`t_minus(beta) = -A(rho) beta^-3 (1,-2,1) + O(beta^-2)`.

Thus every individual causal branch has a genuine cubic local pole before network contraction, while the published additive identity

`T_plus + T_minus = D`

cancels the cubic pole between the two branches, as it must for the regular Wigner matrix.

The next coefficients are also branch-opposite in the expected source pattern. Componentwise, writing

`t = c3 beta^-3 + c2 beta^-2 + c1 beta^-1 + O(1)`,

the exact coefficients are:

| branch,m | `c3` | `c2` | `c1` |
|---|---|---|---|
| `+,-1` | `+A` | `+3/[4(1+rho^2)]` | `-3 i/(8 rho)` |
| `+,0` | `-2A` | `0` | `-3 i rho/[4(1+rho^2)]` |
| `+,+1` | `+A` | `-3/[4(1+rho^2)]` | `-3 i/(8 rho)` |
| `-,-1` | `-A` | `-3/[4(1+rho^2)]` | `+3 i/(8 rho)` |
| `-,0` | `+2A` | `0` | `+3 i rho/[4(1+rho^2)]` |
| `-,+1` | `-A` | `+3/[4(1+rho^2)]` | `+3 i/(8 rho)` |

These coefficients follow algebraically from the exact source formulas; no numerical fit or post-hoc threshold is used.

## Full-matrix form of the leading pole

For a KAK decomposition `g = U1 exp(beta sigma3/2) U2`, the j=1 full Toller matrix has leading term

`T_plus(g) = A(rho) beta^-3 D^1(U1) Q D^1(U2) + O(beta^-2)`,

`T_minus(g) = -A(rho) beta^-3 D^1(U1) Q D^1(U2) + O(beta^-2)`,

where

`Q = diag(1,-2,1)`

in the frozen `(-1,0,+1)` magnetic ordering.

Hence the leading singular tensor is traceless and quadrupole-like rather than proportional to the identity. Cancellation inside a K5 causal network is therefore a genuine intertwiner/angular question; it cannot be decided from scalar power counting alone.

## Relation to collision power counting

If a cluster collision were to retain a nonzero product of these cubic leading tensors on every internal edge, the naive per-edge power would be `p=3`.

The prospectively frozen Iter461 partition contract has naive critical powers:

- `2+1+1+1`: `pcrit=3`;
- `2+2+1`: `pcrit=3`;
- `3+1+1`: `pcrit=2`;
- `3+2`: `pcrit=9/4`;
- `4+1`: `pcrit=3/2`;
- `5`: `pcrit=6/5`.

Therefore the uncancelled cubic term would be at least borderline already for pair collisions and power-counting-supercritical for every larger cluster type. This statement is only a **priority diagnostic**. It is not a divergence theorem because the network/intertwiner contraction may cancel leading homogeneous tensors or reduce their order on specific strata.

## New exact collision question

The collision problem is now sharpened to a finite leading-tensor test:

> For each K5 collision stratum and causal assignment, does the contraction of the internal-edge tensors `D^1(U1) Q D^1(U2)` with the exact j=1 intertwiners vanish identically at the homogeneous leading order? If yes, what is the first surviving Laurent order? If no, can a nonzero leading coefficient be certified on an open angular set?

A single generic nonzero witness is sufficient to refute **universal leading-pole cancellation**, but is not by itself enough to declare the complete physical amplitude divergent until the corresponding local measure and remaining factors are controlled.

## Compatibility with the Haar-tail theorem

`research/SOURCE_ORDER_K5_HAAR_TAIL_SPANNING_TREE_THEOREM_2026-09-15.md` assumes a fixed positive collision cutoff `beta_e >= delta`; its constant `C_delta` is allowed to diverge as `delta -> 0`. The cubic pole derived here explains exactly why collision-cutoff removal is a separate theorem and does not invalidate the noncompact-tail result.

## Claim guards

- No K5 leading-network cancellation/noncancellation result is claimed yet.
- No collision integral convergence/divergence result is claimed.
- No Iter461 result is pre-consumed or duplicated.
- `D7-S2 = NOT_CLOSED`.
- Candidate Gravity remains inactive.
