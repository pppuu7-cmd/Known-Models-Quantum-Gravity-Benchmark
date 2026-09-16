# D7-S2 Eq.(4) full-K5 group-variable tangent pushforward gate — prospective preregistration

Date: 2026-09-16
Status: PREREGISTERED BEFORE OUTCOME

## Gate

`D7_S2_EQ4_FULL_K5_GROUP_TANGENT_PUSHFORWARD_GATE`

## Frozen authority

Use only already-terminal source-authorized facts:

1. Eq.(4) ordered wedges are all `1 <= a < b <= 5`.
2. Same-realization group argument identity: `g_ab = g_b^{-1} g_a`.
3. One vertex group variable is gauge-fixed to identity; the root may be any one of the five vertices only as a coordinate/gauge-root control.
4. Terminal triangle differential prerequisite: at identity, `d(g_b^{-1}g_a)=X_a-X_b`; for root 1 the `(12,23,13)` restriction is `(-X2, X2-X3, -X3)`.
5. Terminal Iter466 comparator: reduced K5 incidence rank `4`, cycle dimension `6` for every gauge root; topology only, not a physical quotient.

No physical transverse quotient, contact/distributional pushforward, Haar/contact normalization or observable projection is introduced here.

## Frozen mathematical object

Vertices: `V={1,2,3,4,5}`.
Ordered wedges: `E={(a,b):1<=a<b<=5}` in lexicographic order.

For a chosen gauge root `r`, set `X_r=0` and use the remaining four vertex tangent variables as the domain. For every wedge `(a,b)`, the source-faithful raw tangent pushforward is

`Y_ab = X_a - X_b`.

Per real Lie generator this defines an integer reduced incidence matrix `D_r : Z^4 -> Z^10`. The full real `sl(2,C)` map is six identical generator blocks.

## Prospectively frozen checks

### Lane A — exact RREF / nullspace
For every root `r=1..5`:
- construct `D_r` exactly over Q;
- compute exact rank;
- compute domain nullity and codomain left-nullity;
- verify the root-1 triangle rows reproduce the terminal triangle differential exactly;
- lift dimensions/rank/nullities by `dim_R sl(2,C)=6` without changing the per-generator incidence statement.

### Lane B — graph/unimodularity proof
For every root and every spanning tree of K5:
- select the four tree-edge rows of `D_r`;
- compute the exact 4x4 determinant;
- require determinant in `{+1,-1}`;
- enumerate spanning trees directly from edge subsets; expected tree count is not used as an acceptance shortcut.

This proves exact integral/unimodular tree coordinate charts rather than merely numerical rank.

### Lane C — orientation / S5 transport
For all 120 vertex permutations:
- transport oriented edge rows with the sign induced by re-sorting each permuted wedge back to the frozen `a<b` convention;
- transport the gauge root with the same vertex permutation;
- require the transported reduced incidence matrix to agree exactly with the directly rebuilt matrix after the corresponding signed row permutation and root-coordinate relabeling;
- require rank/cycle dimension to be invariant.

### Lane D — comparator
Require consistency with terminal Iter466 only at its declared topology scope: per-generator rank `4` and cycle dimension `6` for every root. Do not consume Iter461 partial/nonterminal values.

## Decision rule

`PASS_SCOPED` iff all source identities are locked, all five roots have exact rank 4, domain nullity 0 and left-nullity/cycle dimension 6 per generator, every enumerated spanning-tree minor for every root has determinant ±1, all 120 S5 transports agree exactly, the triangle restriction matches the terminal source-authorized differential, and Iter466 topology invariants agree.

`FAIL_SCOPED` iff the source-authorized raw group tangent map is well-defined but any exact algebraic/topological invariant above fails.

`BLOCKED_SCOPED` iff a required source identity or frozen parent authority needed to define this raw map is absent. Missing physical quotient authority does NOT block this gate because it is explicitly outside scope.

`INVALID` iff the result uses a physical quotient, V8, guessed contact projection, post-hoc orientation/basis convention, nonterminal Iter461 values, numerical tolerance, or changes these criteria after outcome inspection.

## Claim ceiling

A PASS closes only the **raw full-K5 group-variable tangent pushforward prerequisite** inside D7-S2. It does not establish a distributional/contact pushforward, a physical transverse quotient/rank, Haar/contact normalization, observable pushforward, convergence/finiteness, D7-S2 closure, a D7 selector label, model/family failure or any new-theory claim.
