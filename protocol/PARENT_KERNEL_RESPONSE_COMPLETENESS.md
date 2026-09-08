# Parent-Kernel Response Completeness for Future Candidate Gravity

**Status:** frozen methodology / pre-ansatz guardrail.  
**Motivation:** external RQIR Iteration 590 demonstrated concretely that a selected K1/K2 subset does not exhaust the third mixed response of a single covariant source kernel. Future Candidate Gravity must therefore derive source/contact response from the whole parent object rather than hand-selecting diagram families.

## 1. Parent inverse-kernel setup

Let

`G = K^(-1)`

where `K[lambda]` is one parent inverse kernel depending smoothly/functionally on source/background/deformation labels `lambda_a`.

For any nonempty label set `B`, define

`K_B = partial_B K`.

All derivatives in this protocol are mixed derivatives evaluated in the same declared parent realization and at the same background/kinematics.

## 2. Exact ordered-partition formula

For labels `S={1,...,n}`, the complete mixed derivative of `G=K^(-1)` is

`D_S G = sum_(k=1..n) (-1)^k sum_(B1,...,Bk in OP(S,k)) G K_B1 G K_B2 G ... K_Bk G`,

where `OP(S,k)` is the set of **ordered set partitions** of `S` into `k` nonempty disjoint blocks whose union is `S`.

Every ordered partition appears once.

This is the multi-label inverse-kernel analogue of the resolvent derivative rule and supplies a diagram-independent completeness ledger.

## 3. Low orders

### First order

`D_1 G = -G K_1 G`.

### Second order

`D_12 G = -G K_12 G + G K_1 G K_2 G + G K_2 G K_1 G`.

Origin families:

- one local/mixed `K2` contact;
- two ordered `K1^2` chains.

### Third order

`D_123 G = -G K_123 G`

`+ sum_6 [G K_i G K_jk G]`

`- sum_6 [G K_i G K_j G K_k G]`.

Origin families:

- one `K3` contact;
- six ordered `K1/K2` placements;
- six ordered `K1^3` chains.

This is exactly the structural completeness pattern independently reached by the external RQIR Iteration 590 source audit.

## 4. Combinatorial count

At order `n`, the number of ordered-partition terms with `k` kernel blocks is

`N(n,k) = k! S(n,k)`,

with `S(n,k)` the Stirling number of the second kind.

Total term count is the ordered Bell/Fubini number

`N_total(n)=sum_k k! S(n,k)`.

Examples:

- `n=1`: `1` term;
- `n=2`: `1+2 = 3` terms;
- `n=3`: `1+6+6 = 13` terms;
- `n=4`: `1+14+36+24 = 75` terms.

This growth is precisely why future KG source/contact completeness should be generated algorithmically rather than by visual diagram selection.

## 5. Inductive completeness argument

Assume the ordered-partition formula at order `n` and differentiate by one new label `x`.

A derivative can act on

1. a kernel block `K_B`, producing `K_(B union {x})`: this inserts `x` into one existing block without changing the number of blocks/sign;
2. any propagator factor `G`, using `D_x G=-G K_x G`: this inserts a new singleton block `{x}` in one of the ordered positions and increases the block count by one, flipping the sign.

Every ordered partition of the enlarged label set arises uniquely by one of these two mechanisms. Thus the formula is complete by induction.

## 6. Channel-origin classification is a separate gate

Response completeness does **not** mean every complete term contributes to every discontinuity/cut observable.

For a frozen channel variable `s`, each ordered-partition term must be classified by analytic origin.

A strictly local polynomial contact `K_B` with no internal propagator/nonanalytic form factor is analytic in `s` in its declared local domain and therefore has no standalone branch discontinuity there.

However:

- propagator chains can carry poles/cuts;
- a nominal contact can be nonlocal after integrating out fields or can contain a nonanalytic form factor;
- composite source routing can change which invariant enters a given factor;
- cancellation among complete terms may be required by Ward identities.

Therefore the correct order is

`complete same-parent response -> origin classification -> Ward/contact cancellation -> channel discontinuity -> comparator quotient`.

Never drop a term merely because it is called reducible, contact, Born-like, or non-1PI without proving the relevant frozen observable annihilates it.

## 7. Ward/contact completeness

The same ordered-partition response must be used when checking longitudinal/gauge/Ward identities.

A Ward cancellation that closes only after omitting one allowed ordered-partition family is not a valid physical-basis reduction unless the omitted family's contribution has independently been proven zero in that exact observable.

Thus the future KG constraints-first pipeline becomes

`parent kernel -> all ordered partitions -> exact source/contact Ward object -> physical basis -> comparator residual geometry`.

## 8. Candidate Gravity design rule

For a future KG parent functional/kernel, every proposed `n`-th-order response observable must ship with

1. the parent `K` or equivalent CTP generating object;
2. the full ordered-partition response ledger at that order;
3. analytic/cut origin classification for every family;
4. Ward/contact completion on the same routing;
5. the comparator Jacobian only **after** this physical object is closed.

This prevents a false `DeltaGamma_KG` from being created by comparing an incomplete KG response against a more complete comparator, or vice versa.

## 9. Relation to full-C5 matching

The completeness rule applies symmetrically to Candidate Gravity and C5.

At a given perturbative/source-response order, compare

`Gamma_KG_complete(order n)`

against

`Gamma_C5_complete_matched(order n)`

in the same channel/routing/domain.

A residual is not authorized when either side is missing an ordered-partition family required by its own parent dynamics.

## 10. Promotion guardrail

No Candidate Gravity ansatz/readiness increase follows from this methodology alone.

It is a mandatory completeness precondition before COR/global comparator profiling and before any residual can count toward a future KG ansatz.
