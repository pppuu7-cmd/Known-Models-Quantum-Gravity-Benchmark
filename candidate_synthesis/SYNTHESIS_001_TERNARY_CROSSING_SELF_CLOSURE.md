# SYNTHESIS-001 — Ternary Crossing Self-Closure

**Status:** REJECTED at A3 / retained failed synthesis control.  
**KMQGB iteration:** 084.  
**Purpose:** make the first explicit post-O1–O4 parent synthesis attempt and force it through A1–A4 rather than continuing broad taxonomy work.

## 1. Proposed finite rule

Let

`X = stu / Lambda^6`

be a crossing-symmetric dimensionless hard variable. Define a single hard form factor by the analytic fixed-point equation

`F(X) = 1 + X F(X)^3`,

with the branch normalized by

`F(0)=1`.

Interpretation attempted: a hard interaction cell either remains elementary (`1`) or self-resolves into three channel-linked descendants (`X F^3`). The ternary structure was chosen to treat the three four-point Mandelstam channels symmetrically rather than selecting one channel.

A schematic gauge-invariant four-graviton correction would be

`Delta M4 = eta * T_R4(helicities,s,t,u) * [F(X)-1]`,

where `T_R4` is a fixed crossing-symmetric on-shell gravitational contact tensor and `(Lambda,eta)` are the only continuous hard data in this exploratory capsule.

No claim is made that this normalization is already a physical KG amplitude; the point is to test the parent logic.

## 2. A1 — explicit constructive object

The fixed-point equation is explicit and finite. It is not an arbitrary tabulated function.

However the physical motivation is only a ternary self-similarity/composition rule. It is not yet derived from gravitational constraints, causal diamonds or a microscopic Hilbert-space law.

Classification:

`A1 PARTIAL__EXPLICIT_RULE_BUT_GRAVITY_SPECIFIC_ORIGIN_WEAK`.

## 3. A2 — functional freedom

Write

`F(X)=sum_{n>=0} c_n X^n`, `c_0=1`.

The fixed-point equation determines every coefficient recursively. The solution is the Fuss-Catalan generating function with

`c_n = 1/(2n+1) * binom(3n,n)`.

There is no coefficient tower to fit independently.

The first terms are

`F=1+X+3X^2+12X^3+55X^4+273X^5+...`.

The first algebraic branch point occurs when the implicit-function Jacobian vanishes:

`1-3 X F^2=0`.

Together with `F=1+XF^3`, this gives

`F_c=3/2`, `X_c=4/27`.

Thus the global hard function is non-polynomial/non-rational and its infinite local expansion is tied to finite data.

Classification:

`A2 PASS__ZERO_FUNCTIONAL_TOWER_BEYOND_FINITE_SCALE_NORMALIZATION_DATA`.

## 4. Contact-difference gate

At low energy, every finite Taylor order of `Delta M4` is a local analytic contact contribution and lies in full C5 after matching. Any genuine escape would reside only in the resummed branch structure at `X~4/27`, so this proposal is necessarily an E1 hard/nonanalytic construction, not an IR-EFT residual.

This is consistent with `P4_SAME_FACTORIZATION_CONTACT_DIFFERENCE_THEOREM.md`.

## 5. A3 — decisive melonic/tensor-model containment

The exact self-consistency equation is not architecture-new.

Random tensor models have melonic generating functions obeying

`G(z)=1+z G(z)^(d+1)`

with Fuss-Catalan coefficients. In particular `d=2` gives the same cubic algebraic recursion as SYNTHESIS-001.

Large-N tensor-model Schwinger-Dyson equations likewise generate Fuss-Catalan two-point functions from melonic recursion.

KMQGB already registers random tensor models/GFT/TGFT as quantum-gravity comparator architectures.

Therefore the proposed finite recursion is, at best, a new **assignment** of a known melonic combinatorial law to a four-graviton form factor. It does not establish a new parent principle.

Classification:

`A3 FAIL__MELONIC_RANDOM_TENSOR_MODEL_RECURSION_CONTAINED`.

## 6. Independent analytic concern

A branch condition defined by

`stu/Lambda^6 = 4/27`

creates a channel-dependent branch locus in `s` whose position depends on `t` through `u=-s-t`. A physical Lorentzian amplitude would need a detailed Landau/unitarity explanation for such a branch geometry.

No such microscopic spectral origin exists in this synthesis attempt.

Thus even absent the tensor-model comparator, dispersive/causal origin would remain blocked.

## 7. A4 / CTP

The scalar hard function is explicit, but a complete normalized helicity amplitude and same-parent CTP/retarded hierarchy were not derived before A3 failure.

Per the construction playbook, development stops here rather than manufacturing those layers for a comparator-contained object.

## 8. Lesson for SYNTHESIS-002

A future nonlinear recursion must be **gravity-sensitive in its rule**, not merely in the tensor prefactor attached after solving a scalar combinatorial equation.

Specifically, the recursion should involve at least one of

- the gravitational Ward/constraint operator itself;
- a physical helicity/tensor contraction that cannot be replaced by scalar counting;
- a linked scattering/CTP identity built into the same rule;
- another intrinsically gravitational object that survives tensor/vector/matrix-model reinterpretation.

Attaching `T_R4` to a scalar recursion after the fact is insufficient attribution.

## 9. Score consequence

No P4 credit. R4 remains 45%.
