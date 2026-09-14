# Iter504 preregistration — fixed-causal K5 full-collision leading contraction

**Prospectively frozen before Iter504 implementation or production evidence.**

## Purpose

Test the first source-faithful object not already closed by Iter477/479/480B/481/482/485: whether the exact leading fixed-causal Toller singular coefficient survives after **all ten K5 wedges are tied to one common five-node collision blow-up and contracted with the five genuine j=1 four-valent SU(2) intertwiners**.

This is a leading-coefficient survival gate only. It is not a local-integrability or divergence theorem.

## Frozen authority

- Iter452 pins the source causal vertex / Eq.(3)/(4)/(7) object.
- Iter477 establishes the one-wedge fixed-branch order `beta^(-(2j+1))`; for `j=1` the order is `beta^-3` and the leading magnetic coefficients are finite/nonzero on the frozen rho authorities used there.
- Iter479 establishes the source Eq.(7) leading matrix `U1 diag(C_m) U2` and its full rank.
- Iter480B establishes that genuine j=1 boundary intertwiners alone do not universally cancel the diagonal-collision leading coefficient.
- Iter481/482 establish the frozen angular and common-node compact contraction conventions.
- Iter484/485 pin the `spin1`, KAK, branch, magnetic-basis, edge-order and ten-edge contraction conventions used here.
- Iter471 gives exact K5 collision-stratum geometry, but its naive `pcrit` values are prioritization diagnostics only and are **not** used as an Iter504 classifier.

## Frozen collision blow-up

Gauge-fix node `0` and take tangent boost vectors `v_a in R^3` with `v_0=(0,0,0)`. The three prospectively frozen generic integer panels are

- `T0 = [(0,0,0),(1,2,3),(-2,1,4),(3,-1,2),(2,4,-1)]`
- `T1 = [(0,0,0),(2,-1,1),(1,3,-2),(-3,2,2),(4,1,3)]`
- `T2 = [(0,0,0),(1,-2,4),(-1,3,2),(4,2,-3),(-3,-1,1)]`.

For edge `e=(a,b)` in the existing Iter485 orientation define

`w_ab = v_a - v_b`, `r_ab = |w_ab|`, `n_ab = w_ab/r_ab`.

All ten `r_ab` must be nonzero. The exact tangent-cycle identity is

`w_ab + w_bc = w_ac`.

The corresponding finite shared-node source path used only for regression is

`g_a(t) = U(n_a) A(t |v_a|) U(n_a)^dagger`,

with `g_0=1`, where `A(beta)=diag(exp(beta/2),exp(-beta/2))` and `U(n)` is the canonical SU(2) section `Rz(phi) Ry(theta)` rotating `+z` to `n`. Relative source elements are exactly `h_ab(t)=g_b(t)^(-1) g_a(t)`.

At tangent order,

`h_ab(t) = 1 + t (w_ab . K) + O(t^2)`,

so `beta_ab(t)=t r_ab+O(t^2)`.

## Frozen source leading edge matrix

Use `j=1` and rho panel exactly `{7,8}`, inherited from the exact leading-coefficient authority of Iter477/479. Use the three existing causal representatives

- `0to5 = (+,+,+,+,+)`
- `1to4 = (-,+,+,+,+)`
- `2to3 = (-,-,+,+,+)`.

For each edge choose the fixed causal branch exactly as Iter485:

- `T+` if `sigma_a sigma_b > 0`,
- `T-` otherwise.

In the Iter484 contraction basis `m=(-1,0,+1)`, define

`L_ab = r_ab^-3 D^1(U(n_ab)) diag(C_-1,C_0,C_+1) D^1(U(n_ab))^dagger`,

where `C_m` is the exact Iter477/479 leading coefficient for the selected source branch and rho. No branch sum is allowed.

This is the coefficient of the common full-collision factor `t^-30` for ten `j=1` wedges, before any claim about the 12-dimensional normal measure or remainder integrability.

## Frozen contraction

Reuse without modification:

- `iter482_common_node_su2_control.intertwiner(i)` for `i=0,1,2`;
- the Iter482/485 node/edge label incidence;
- `contraction_path` and `contract`;
- all `243 = 3^5` boundary-intertwiner channel assignments.

For each `(panel, causal, rho)` lane compute all 243 leading contractions and the dimensionless ratio

`R_I = |C_I(L_1,...,L_10)| / product_e maxabs(L_e)`.

Freeze the nonzero witness threshold at `1e-12`, inherited from Iter480B. The classifier uses the direct maximum over all 243 channels; it does not choose a channel after seeing the data. Channel `[0,0,0,0,0]` is recorded only as a preregistered diagnostic because it was the diagonal-control maximizer in Iter480B.

There are exactly `3 panels x 3 causal classes x 2 rho values = 18` scientific lanes.

## Mandatory controls

Every lane must pass all of the following before its witness can be scientific evidence:

1. **Source coefficient control** — every selected `C_m` is finite and nonzero.
2. **Tangent geometry control** — all ten `r_ab>0`; all triangle difference-cycle identities hold to machine/exact-integer tolerance.
3. **SU(2) section control** — `U(n)` is unitary with determinant one; `D^1(U)` matches the already-qualified Iter484 `spin1` convention.
4. **Axial-section invariance** — replacing every `U(n)` by `U(n) Rz(0.371)` leaves each `L_ab` unchanged within `1e-11` relative max norm.
5. **Common-translation control** — translating all five `v_a` by `(2,-3,5)` leaves every `w_ab` and every leading matrix unchanged within `1e-12` relative max norm.
6. **Scale-homogeneity control** — replacing all `v_a` by `2 v_a` multiplies every edge leading matrix by `2^-3`, every channel contraction by `2^-30`, and leaves all dimensionless `R_I` invariant within `1e-10` relative max norm.
7. **Finite-t source regression** — at `t_coarse=1e-3` and `t_fine=5e-4`, build the exact common-node source path, use the qualified Iter484 KAK / full Toller reconstruction, select the same fixed causal branch, and compare `t^3 M_ab(t)` to `L_ab`. Require every fine per-edge relative Frobenius error `<5e-3` and every fine error `<=0.75*coarse_error + 1e-10`.
8. **Intertwiner controls** — frozen Iter482 support/norm/orthogonality controls pass.
9. **Magnetic-basis reindex control** — simultaneous `m -> -m` reversal of all intertwiners and edge matrices preserves the sorted 243 contraction magnitudes within relative `1e-10`, as in Iter485.
10. **Zero-edge negative control** — replacing edge `(0,1)` by the zero 3x3 matrix makes every leading contraction vanish below normalized `1e-14`.
11. **Finite normalized contraction** — all 243 dimensionless ratios are finite.

No control may be weakened after production evidence.

## Frozen classifications

### PASS

`ITER504_FIXED_CAUSAL_K5_FULL_COLLISION_LEADING_CONTRACTION_SURVIVES_QUALIFIED_SCOPED`

iff all 18 lanes are valid and in every lane

`max_I R_I > 1e-12`.

PASS means: on every prospectively frozen generic common-node collision tangent panel, the exact source fixed-causal `t^-30` leading coefficient survives the full ten-edge Eq.(7)-magnetic / five-intertwiner contraction in at least one boundary channel. Therefore universal pre-integration cancellation of the leading singular coefficient is not available on these frozen generic panels.

PASS does **not** establish local absolute divergence, because a uniform blow-up angular neighborhood and a source-faithful remainder/asymptotic domination theorem are still required before combining the coefficient with the collision measure.

### FAIL

`SCIENTIFIC_FAIL_ITER504_UNIFORM_FROZEN_FULL_COLLISION_LEADING_SURVIVAL`

iff all controls are valid but at least one frozen `(panel,causal,rho)` lane has

`max_I R_I <= 1e-12`.

FAIL refutes the stronger all-frozen-panel survival hypothesis only. It does not prove generic cancellation or finiteness of the physical vertex.

### BLOCKED / INVALID

`BLOCKED_OR_INFRASTRUCTURE_ITER504`

iff any source, geometry, section, finite-t regression, intertwiner, homogeneity, reindex or finite-arithmetic control fails. No leading-survival scientific interpretation is then permitted.

## Exact post-gate decision

- After PASS: the next admissible dependent collision gate is a prospectively frozen **uniform full-collision blow-up remainder/neighborhood certificate** for the same fixed-causal contracted object. Only that later gate may ask whether the `t^-30` coefficient survives on a positive-measure angular set and whether its remainder is dominated strongly enough to compare with the 12-dimensional full-collision normal measure.
- After FAIL: localize which frozen panels/causal classes/rho values cancel; do not change panels or threshold and do not infer generic cancellation.
- After BLOCKED: repair only the identified source/convention/numerical control defect.

## Claim locks

No branch summation. No independent-edge surrogate. No direct comparison of one-wedge `p=3` with Iter471 `pcrit=6/5` as if that alone proved divergence. No Haar/group-integral theorem. No ten-spectral pairing theorem. No physical causal-vertex finiteness/divergence theorem. D7-S2/S3/S4 remain unchanged; terminal D7 labels remain forbidden; Candidate Gravity remains inactive.