# Kinematic Projection-Rank Completeness

**Status:** frozen methodology / pre-ansatz guardrail.  
**Origin:** generalized from the external RQIR Iteration 611 source-to-native obstruction.  
**Purpose:** prevent an underdetermined many-invariant parent response from being projected onto a lower-dimensional observable by an implicit or post-hoc trajectory choice.

## 1. General setup

Let a complete physical parent/source response depend on independent invariant coordinates

`x=(x_1,...,x_n)`

in a prospective common domain.

Suppose the target/native observable is parameterized by only

`s=(s_1,...,s_m)`, with `m<n`,

through a map

`s = Phi(x)`.

A value of `s` generally labels an `(n-m)`-dimensional level set in parent kinematics rather than a unique source point.

Therefore a derivative/discontinuity/pullback such as

`D_s F(x)`

is not uniquely defined until the parent point on each level set is fixed prospectively.

## 2. Rank requirement

Locally, define the Jacobian

`J_Phi = partial Phi / partial x`.

If `rank(J_Phi)=m`, then a unique local trajectory/lift requires `n-m` additional independent constraints

`C_a(x)=c_a`, `a=1,...,n-m`,

such that the stacked Jacobian

`J_lift = [J_Phi; J_C]`

has full rank `n` on the declared domain.

Equivalent formulation: prospectively define an embedding

`gamma: s -> x(s)`

satisfying

`Phi(gamma(s))=s`

and the frozen auxiliary constraints.

Without this lift, the pullback observable is `BLOCKED_MISSING_KINEMATIC_COMPLETION`.

## 3. Why one coordinate is not enough

For a scalar target `s` and `n=3` parent invariants, a fixed `s` leaves a two-dimensional level set. Two additional independent same-parent constraints are therefore required before a unique one-parameter trajectory exists.

This is exactly the pattern observed in external RQIR Iter611, where the retained source denominators depend on

`(u,a_s,a_a)`

while the frozen native hard-channel protocol provides one scalar `s`.

The KMQGB lesson is general and does not depend on those specific variables.

## 4. Directional-derivative ambiguity

If two admissible tangent vectors `v_1` and `v_2` satisfy

`J_Phi v_1 = J_Phi v_2`,

but

`grad F . v_1 != grad F . v_2`,

then the supposed derivative with respect to the same target coordinate depends on the hidden lift choice.

Such ambiguity cannot be repaired by numerical precision.

## 5. Pole/cut Jacobian consequence

For a parent denominator/root condition

`D_A(x)=0`,

a projected distribution or discontinuity in the target variable requires the frozen trajectory `x(s)` before using a simple-root Jacobian such as

`delta(D_A(x(s))) = sum_r delta(s-s_r)/|d D_A(x(s))/ds|_(s_r)`.

The root locations `s_r` and Jacobians are undefined until the lift is authoritative.

A universal distribution identity in parent variables does not by itself determine its target-coordinate pullback.

## 6. No post-hoc trajectory selection

Forbidden:

- choosing auxiliary invariants after inspecting the desired residual;
- identifying `s` with one convenient parent invariant without same-parent authority;
- importing a routing from a different scoped observable;
- deleting pole/cut families because their target pullback has not been defined;
- zero-filling an underdetermined projection;
- optimizing the trajectory to maximize COR/significance.

Any new trajectory is a prospective protocol version and must be frozen before the target projection is evaluated.

## 7. Order relative to Ward/comparator gates

Required order:

`complete parent response`

`-> exact physical/Ward reduction`

`-> invariant-rank audit`

`-> prospective kinematic lift / native mapping`

`-> pole/cut/root Jacobians in target coordinates`

`-> matched residual vector`

`-> comparator/COR/global quotient`.

A comparator residual formed before the native mapping is unique is non-authoritative.

## 8. Candidate Gravity machine-record consequence

Every future KG observable block that maps a parent object to fewer kinematic variables should record

- `parent_invariant_dimension`;
- `target_invariant_dimension`;
- `projection_rank`;
- `required_auxiliary_constraints`;
- `auxiliary_constraint_refs`;
- `trajectory_or_lift_ref`;
- `root_jacobian_ref` when cuts/poles are involved.

If `required_auxiliary_constraints > supplied_independent_constraints`, the block is scientifically `BLOCKED` while the record itself may remain structurally valid.

## 9. Design lesson

A low-dimensional observable is not automatically simple. It may hide a high-dimensional parent kinematic dependence.

Future KG should prefer relational observables whose source-to-detector/native map is either

1. uniquely derived from the parent dynamics and experimental geometry, or
2. explicitly augmented by prospectively controlled interventions that close the invariant rank.

## 10. Promotion status

This is a methodology gate only. It does not promote a Candidate Gravity ansatz or change external RQIR readiness.
