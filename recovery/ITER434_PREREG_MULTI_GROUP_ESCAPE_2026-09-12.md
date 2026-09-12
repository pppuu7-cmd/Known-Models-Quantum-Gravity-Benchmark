# Iter434 Preregistration — Correlated Multi-Group Large-Boost Escape Rays

Date frozen: 2026-09-12, before any Iter434 Actions result exists.
Prerequisite: Iter433 `PASS_SINGLE_GROUP_LARGE_BOOST_RADIAL_ENVELOPE`.

## Scientific question
Does the source-faithful gamma-simple Toller carrier retain an exponentially decaying absolute radial envelope when several gauge-unfixed K5/4-simplex group variables escape together along the same collinear boost ray?

## Frozen geometry and profiles
Gauge-fix K5 vertex 0. For each cluster size `s = 1,2,3,4`, boost vertices `1..s` by the same boost `B(beta)` and leave the remaining vertices at the identity. Edges internal to either cluster have zero relative boost; only the K5 cut edges carry relative rapidity `beta`. Therefore the number of decaying crossing edges is exactly `s*(5-s)` while the radial Haar growth contributes `exp(2*s*beta)`.

Use the same published gamma-simple Toller closed forms validated in Iter432/433, with `rho = gamma*j`, gammas `{0.1, 0.2375, 0.5}`, and deterministic half-integer crossing-edge spins cycling through `{1/2,1,3/2,2}`. For each `s`, test two branch/magnetic families: (a) the slow/worst Toller tail (`alpha=1` per crossing edge), alternating causal sign by edge while choosing `m=-j` for `+` and `m=+j` for `-`; (b) a fast-control family choosing the opposite extremal magnetic labels. This gives `3 gammas × 4 cluster sizes × 2 families = 24` independent profiles.

## Frozen analytic discriminator
For each profile, with published branch exponent `alpha_e = 1 + |j + sign*m|`, define

`lambda = 2*s - sum_{crossing edges} alpha_e`.

A strictly negative `lambda` is required for exponential absolute radial decay along that ray. `lambda >= 0` is a scientific FAIL of this exponential absolute-envelope criterion for that profile. It is NOT a physical-divergence theorem.

## Frozen numerical control
Evaluate the exact closed-form crossing-edge Toller product times `sinh(beta)^(2*s)` at `beta = 6,8,10,12`. The final log-slope must agree with the analytic `lambda` to `< 2e-4`. Non-finite output or disagreement at/above that tolerance is `NUMERICAL_FAIL`, not a scientific result.

## Aggregate interpretation
- `PASS_MULTI_GROUP_EXPONENTIAL_ABSOLUTE_ENVELOPE` only if all 24 structurally/numerically valid profiles have `lambda < 0`.
- `FAIL_MULTI_GROUP_EXPONENTIAL_ABSOLUTE_ENVELOPE` if numerical controls are valid but at least one prospectively included ray has `lambda >= 0`.
- The FAIL interpretation is limited to failure of this absolute exponential convergence bound. Conditional/angular cancellation, boundary-intertwiner contraction, finite-beta pole/distributional structure, and a normalized causal vertex remain separate.

## Locks
D7-S2 remains OPEN regardless of Iter434 outcome. D2 and D4 do not close. D7 terminal classifier remains forbidden. Candidate Gravity remains inactive. No threshold or profile family may be changed after inspecting Iter434 results.