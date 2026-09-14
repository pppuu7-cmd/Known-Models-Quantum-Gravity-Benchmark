# Iter499 terminal result — direct Arb max-envelope interval gate

Date: 2026-09-14

## Frozen authority
- Preregistration: `recovery/ITER499_PREREG_DIRECT_MAX_ENVELOPE_ARB_INTERVAL_2026-09-14.md`, commit `5fd8124af8edb374d6b48c2a5e2e66cd7b322e54`.
- Arb/Acb core: `code/iter499_arb_core.py`, commit `f16f3106925f13e6e1d847f2d555b5d8fedc5b4d`.
- Lane evaluator: `code/iter499_direct_max_envelope_interval.py`, commit `bd935a81c2d2b1a1f4db78e1355054d92d36760f`.
- Aggregate: `code/iter499_aggregate.py`, commit `cde7d15e03dd6d9a0ac6a78d61b07da4ff3ec517`.
- Production workflow/head: `33d4dacc705247ab5966f1c01083cd92ee8ab2c1`.
- Authoritative run: `34818229950`.
- Aggregate job: `103895072732`.
- Aggregate artifact: `10337765174`.
- Aggregate digest: `sha256:70006ae095cebcb82dddbcfa4af72d40da7c8d3845747411a50a28eecd7b9513`.

## Terminal classification
`ITER499_NUMERICAL_METHOD_BLOCKER`

This is **not** a scientific fail of the frozen q=1 NONDECAY interval claim. The validated construction fails before any max-envelope/slope state is admitted to the science classifier.

## Aggregate facts
- expected jobs: 12;
- raw jobs present: 12/12, each exactly once;
- structural aggregate validity: PASS;
- jobs classified `ITER499_NUMERICAL_METHOD_BLOCKER`: 12/12;
- valid direction boxes reaching the max-envelope classifier: 0;
- valid rho-box science states: 0;
- no scientific slope/drift extrema are therefore promotable from Iter499.

The first inspected raw lanes (`0to5-b0`, `0to5-b1`, `1to4-b3`) each show the same frozen failure: all 64 signed-direction/box attempts stop at `KAK eigenvalue positivity/separation not certified` before Toller-network contraction. Exact-rational intertwiner regression is zero in the inspected lanes, so the failure occurs upstream of the 243-channel contraction.

## Diagnostic localization
A separate frozen diagnostic-only run was launched after the production blocker was observed; it does not replace or repair Iter499.

Authority:
- diagnostic prereg `e7cde62aa389af7226a852df0c2ae20492c75889`;
- implementation `14a3821b93e758915e38322e3891336830302681`;
- workflow/head `25405b085dde2a255ca0bd5b44f0edad539cc97f`;
- run `34818721003`;
- artifact `10336829843`;
- digest `sha256:a1edf763095c80c512b5ef0776187124154fc17695e29a68715021742f71a85e`.

Diagnostic classification: `ITER499_DEPENDENCY_DIAGNOSTIC_UNRESOLVED`.

The diagnostic nevertheless isolates the mechanism sharply on representative box `A0=[0.00125,0.001328125]`, direction `[1,1,1,1,1,1]`, sign `+`:
- midpoint algebraic equivalence between naive and factorized relative matrices passes for all ten edges and all R values;
- factorizing the shared-node relative matrix cures every internal edge `1<=a<b<=4` at R=6,8,10,12;
- naive `0b` edges show interval dependency failures, while the factorized form cures them through R=10;
- at R=12 only factorized edge `(0,1)` still loses the KAK certificate;
- naive node 1 itself loses the certificate at R=10 and R=12.

Therefore the original hypothesis "only the relative-matrix inverse/product destroys the interval KAK" was too narrow. There is an additional avoidable interval-width problem in applying a generic KAK eigensolver to compactly perturbed boosted nodes/0b edges.

## Exact enabling observation
For each escaped node,

`g_a = L_a B G_a R_a`,

with amplitude-dependent `L_a,R_a in SU(2)`. Hence the singular values and Cartan rapidity beta of `g_a` are **exactly invariant** under `L_a` and `R_a`; node beta is the beta of the fixed middle matrix `B G_a` and does not depend on the amplitude interval.

Likewise,

`h_0b = g_b^{-1} = R_b^{-1} (G_b^{-1} B^{-1}) L_b^{-1}`,

so its singular values/beta are exactly those of the fixed middle matrix `G_b^{-1} B^{-1}`. If

`G_b^{-1} B^{-1} = U1 A U2`,

then a valid compact-sandwich KAK is

`h_0b = (R_b^{-1} U1) A (U2 L_b^{-1})`.

No interval eigensolver is needed for node or 0b beta, and no determinant projection or midpoint approximation is introduced.

For internal edges `1<=a<b<=4`, the dependency-preserving factorization

`h_ab = R_b^{-1} G_b^{-1} B^{-1} L_b^{-1} L_a B G_a R_a`

already passes the representative diagnostic across all four R values. Outer compact factors may be stripped before KAK and restored afterward.

## Next admissible gate
Before any repeat of the Iter499 max-envelope science classifier, prospectively test the compact-sandwich/factorized KAK construction across the **entire frozen Iter499 16-box state space**. The enabling gate must:
1. preserve the exact Iter499 geometry and box cover;
2. use compact covariance for node and 0b KAK instead of a generic interval eigensolver on their full ball matrices;
3. use factorized internal relative matrices;
4. validate reconstruction/unitarity/determinant containment and midpoint agreement against the established high-precision source object;
5. make no NONDECAY/max-envelope claim.

Only a full enabling PASS may authorize a new prospective direct-envelope production iteration.

## Scope ceiling
No continuum certificate, multidimensional angular neighborhood, positive-measure theorem, absolute Haar convergence/divergence result, ten-spectral integration result, physical causal-vertex finiteness/divergence theorem, D7-S2 closure, terminal D7 label or Candidate Gravity activation follows from Iter499.
