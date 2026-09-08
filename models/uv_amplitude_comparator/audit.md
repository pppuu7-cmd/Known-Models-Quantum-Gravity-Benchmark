# UV Comparator Audit — Huang–Remmen triple-product gravity amplitude

Benchmark ID: KMQGB-S2-M05-UV-COMPARATOR
Concrete comparator ID: HR-TRIPLE-SINGLE-MASS-GRAV4-001
Role: same-domain UV four-graviton comparator for first-wave M09 string threshold branch
State: TERMINAL AS COMPARATOR INFRASTRUCTURE
Final status: `PASS_RQIR_GATE`
Terminal objective: `SAME_DOMAIN_UV_COMPARATOR_ESTABLISHED`

## Frozen amplitude

Use the simplest nontrivial member of the Huang–Remmen UV-complete gravitational triple-product class:

`A_HR(s) = 1/s + 1/(m^2-s)`, `m^2>0`,

`M_HR(s,t,u) = kappa^2 R^4 A_HR(s) A_HR(t) A_HR(u)`.

This corresponds to the general construction

`A(s)=1/s + sum_n g_n^2/(m_n^2-s)`

with a single massive pole and `g_1^2=1`, satisfying the UV-softening sum rule `sum_n g_n^2=1`.

The external channel is exactly four gravitons, matching the first-wave type-II M09 scattering observable at amplitude level.

## Why it is a fair UV comparator

The amplitude:

- reduces to the Einstein four-graviton amplitude in the infrared;
- is meromorphic;
- has positive partial-wave residues in the Huang–Remmen construction;
- is crossing symmetric through the `A(s)A(t)A(u)` triple product;
- softens fixed-angle high-energy scattering from the Einstein growth to `M ~ E^-4` for the imposed coupling sum rule;
- remains a well-defined amplitude in the trans-Planckian / massive-pole region where low-energy C5 EFT is no longer the appropriate comparator.

Hence it supplies exactly the missing **same external state + same high-energy domain** comparison object for the M09 string-threshold branch.

## Important scope limitation

Huang and Remmen explicitly construct the amplitude bootstrap object without identifying a complete underlying Hamiltonian or Lagrangian microscopic theory. Therefore this file closes S2-M05 **as comparator infrastructure**, not as a full F0–F7 validation of a complete quantum-gravity model.

No claim is made that every analytic/unitary UV completion is represented by this one-parameter comparator.

## Exact comparison with type-II Virasoro–Shapiro

First-wave M09 freezes the type-II tree four-graviton amplitude with Virasoro–Shapiro Gamma-function structure. The two amplitudes share:

- the same four-graviton external channel;
- Einstein/GR infrared behavior;
- tree-level meromorphic UV-completion structure;
- crossing/triple-product organization.

But their analytic structures differ exactly.

### Pole-support discriminator

Define the positive-mass s-channel pole-support set `P_s` of the normalized scalar form factor after removing the universal massless graviton pole.

For the frozen one-mass Huang–Remmen comparator,

`P_s^HR = {m^2}`.

At that one mass, the residue decomposes into an infinite even-spin tower (an accumulation point in spin), but there is only one distinct positive mass level in the frozen comparator.

For type-II Virasoro–Shapiro,

`P_s^VS = {4 n/alpha' : n=1,2,3,...}`

up to the exact Mandelstam/sign convention frozen in M09; equivalently, it contains an infinite sequence of distinct massive string levels.

For any finite positive `m^2` and finite `alpha'`,

`P_s^HR != P_s^VS`.

Therefore the full UV amplitudes are exactly distinguishable in this pole-support observable. This removes the prior statement that **no same-domain UV comparator exists**.

### Stronger analytic distinction

Huang–Remmen further note that their `A(s)` is asymptotically bounded in physical and unphysical regions, whereas Virasoro–Shapiro inherits Gamma-function behavior; their leading Regge trajectory has infinite slope, unlike the ordinary string trajectory. Thus the pole-support difference is part of a broader exact analytic distinction.

## Cross-wave effect on M09

Historical first-wave M09 remains recorded as `BLOCKED_PROTOCOL_MISMATCH` under the comparator registry available when that queue was frozen. Historical results are not rewritten retroactively.

Prospectively, the second-wave protocol extension now allows the statement:

`M09 type-II string is DISTINCT_FROM HR-TRIPLE-SINGLE-MASS-GRAV4-001 in the full UV pole-support observable.`

This is **not** yet `ROBUST_UNIQUE_QG_RESIDUAL` for string theory, because one explicit alternative UV comparator does not exhaust the space of generalized dual-resonance / UV-complete gravity amplitudes.

## Gate summary for the comparator task

| Comparator task gate | Result |
|---|---|
| Same external state as M09 | PASS — four gravitons |
| Same UV validity domain | PASS — amplitude defined through massive/UV poles |
| GR/IR common limit | PASS |
| Analytic/unitarity control | PASS at the amplitude-bootstrap level of the cited construction |
| Exact distinction from VS | PASS — different pole-support and asymptotic/Regge structure |
| Complete microscopic F0 theory | NOT CLAIMED / BLOCKED AS FULL MODEL |
| Comparator-infrastructure objective | PASS |

## Sources

1. Y.-t. Huang, G. N. Remmen, *UV-Complete Gravity Amplitudes and the Triple Product*, Phys. Rev. D 106, L021902 (2022), arXiv:2203.00696.
2. First-wave `TYPEII-T6-GRAV4-TREE-001` audit and result in this repository.
3. Related generalized dual-resonance/string-amplitude literature retained as evidence that one comparator does not exhaust all UV completions.
