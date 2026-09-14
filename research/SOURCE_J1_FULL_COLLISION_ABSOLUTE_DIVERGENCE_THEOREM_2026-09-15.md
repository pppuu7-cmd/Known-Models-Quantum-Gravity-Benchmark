# Source-order j=1 K5 full collision — scoped absolute-divergence theorem

Date: 2026-09-15
Status: `DERIVED_KMQGB` theorem for a fixed allowed j=1 boundary channel; source-defined/distributional amplitude remains open

## Statement

For the source-order causal K5 vertex with fixed j=1 labels, fixed nonzero real rho on every edge, any of the frozen causal signatures `0to5`, `1to4`, or `2to3`, and the allowed intertwiner channel

`(i0,i1,i2,i3,i4) = (0,0,0,0,0)`,

the gauge-fixed four-group integrand is **not locally absolutely integrable** in a neighborhood of the full K5 collision stratum.

Equivalently, the ordinary absolute Haar integral of this fixed channel diverges already from the full-collision neighborhood.

This does **not** rule out a source-defined distributional/Feynman boundary value, conditional finite part, cancellation after summing causal branches, or another explicitly justified prescription.

## Inputs already derived

`research/SOURCE_J1_TOLLER_COLLISION_POLE_LEDGER_2026-09-15.md` gives the exact one-edge cubic pole

`T_plus = +A(rho) beta^-3 D^1(U1) Q D^1(U2) + O(beta^-2)`,

`T_minus = -A(rho) beta^-3 D^1(U1) Q D^1(U2) + O(beta^-2)`,

with

`A(rho)=3 i/[4 rho(1+rho^2)] != 0`,

`Q=diag(1,-2,1)`

in the frozen spherical basis.

The exact repository intertwiners are those in `iter499_arb_core._SUPPORTS`.

## Normal coordinates at the full collision

Gauge fix vertex 0 to the identity. The full Cartan-collision stratum is

`Sigma_full = K^4`, `K=SU(2)`,

because `beta(g_a)=0` for every root edge iff each `g_a` lies in `K`; then every relative `g_b^-1 g_a` also lies in `K`.

The normal bundle has dimension

`4 * dim(SL(2,C)/SU(2)) = 4*3 = 12`.

Near a point of `Sigma_full`, use compact coordinates `k_a` along `K^4` and boost-normal coordinates `X_a in p ~= R^3`. Haar measure is smooth and nonvanishing in these local coordinates, so normal radial scaling

`X_a = t x_a`, `t -> 0+`

has volume element comparable to

`t^(12-1) dt dOmega = t^11 dt dOmega`

on any fixed angular cone.

## Exact tangent witness

At the compact base point `k_a=identity`, choose the fixed rational tangent vectors

- `x0=(0,0,0)`;
- `x1=(1,0,0)`;
- `x2=(0,1,0)`;
- `x3=(0,0,1)`;
- `x4=(1,1,1)`.

All ten differences `v_ab=x_a-x_b` are nonzero.

For a pure infinitesimal boost in direction `n=v/|v|`, the Cartesian spin-1 form of the leading quadrupole is

`Q(n)=I-3 n n^T = I-3 vv^T/(v.v)`.

The three frozen spherical j=1 intertwiners transform **exactly** into the Cartesian invariant tensors

`I0_ijkl = (1/3) delta_ij delta_kl`,

`I1_ijkl = (1/6)(delta_ik delta_jl - delta_il delta_jk)`,

`I2_ijkl = (1/10)(delta_ik delta_jl + delta_il delta_jk) - (1/15)delta_ij delta_kl`.

Their exact norms are `1`, `1/3`, and `1/5`, matching the frozen KMQGB Gram normalization.

Contracting the ten exact rational matrices `Q(v_ab)` with five `I0` tensors using the frozen K5 incidence/index ordering gives

`C_00000 = 11/24 != 0`.

The exact certificate also finds 224/243 leading angular channels nonzero for this tangent configuration. Only the nonzero `00000` witness is needed for the theorem.

## Causal-sign control

At cubic order a minus Toller branch contributes only an overall minus sign relative to the plus branch.

For the frozen signatures the numbers of opposite-sign K5 edges are

- `0to5`: 0;
- `1to4`: 4;
- `2to3`: 6.

All are even. Therefore the product of the ten cubic branch signs is `+1` in every frozen causal class. The nonzero leading coefficient cannot disappear by a global causal sign.

## Leading homogeneous scaling

For the tangent family above,

`beta_ab = t |v_ab| + O(t^2)`.

Hence every edge contributes a cubic factor `t^-3`, and ten edges give

`t^-30`.

The complete channel-00000 leading coefficient is a nonzero scalar multiple of

`(11/24) * product_edges A(rho_e) * product_edges |v_ab|^-3`.

For the frozen common-rho witnesses, and more generally for any nonzero real `rho_e`, this coefficient is nonzero.

Because the leading coefficient depends continuously on the compact base point and on angular tangent data away from pair coincidences, its nonzero value at the rational witness implies a positive-measure open cone on which its absolute value is bounded below by a positive constant. The `O(t^-29)` remainder is then dominated by the `t^-30` leading term for sufficiently small `t` on a smaller cone.

## Absolute-divergence conclusion

On that open cone the absolute value of the fixed-channel integrand is bounded below by

`c t^-30`

for some `c>0`. Multiplying by the 12-dimensional normal volume element gives the lower-bound radial integral

`integral_0^eps c t^(11-30) dt = c integral_0^eps t^-19 dt`,

which diverges.

Therefore the fixed j=1 channel `(0,0,0,0,0)` is not locally absolutely integrable at the full K5 collision for any frozen causal assignment. QED.

## Reproducibility certificate

`code/source_j1_full_collision_leading_certificate.py` checks, in exact arithmetic:

1. the spherical-to-Cartesian transform of all three frozen intertwiners;
2. the exact Gram norms `1,1/3,1/5`;
3. the fixed rational tangent configuration;
4. `C_00000=11/24`;
5. `224/243` nonzero leading channels;
6. causal minus-edge counts `0,4,6`.

The certificate is a verification of the algebraic theorem, not an outcome-tuned classifier.

## Relation to the noncompact-tail theorem

`research/SOURCE_ORDER_K5_HAAR_TAIL_SPANNING_TREE_THEOREM_2026-09-15.md` proves absolute integrability of all noncompact tails at every fixed positive collision cutoff `delta`.

The two results are compatible and sharpen the source-order diagnosis:

- collision-separated noncompact infinity: `ABSOLUTE_JUSTIFIED_SCOPED`;
- full K5 collision for the j=1 channel 00000: `ABSOLUTE_DIVERGENCE_PROVED_SCOPED`;
- source-defined/distributional collision prescription and its compatibility: still open.

Thus, for this channel, the failure of ordinary absolute integrability is localized to collision removal rather than to noncompact Haar infinity away from collisions.

## Relation to Iter504

Iter504 remains scientifically valid within its frozen pathwise scope and is not cancelled. Its max-envelope classifier probes a specific continuous q=1 escape family, whereas the theorem above concerns a different mechanism: local full-collision singularity.

An Iter504 NONDECAY result would therefore be additional scoped tail information, not the proof of absolute divergence established here. An Iter504 DECAY result would likewise not repair the independently proved collision divergence.

## D7 interpretation ceiling

This theorem is sufficient to reject an **ordinary absolute-Haar-finiteness claim** for the specified fixed j=1 causal channel.

It is not sufficient by itself to close all of D7-S2 because the repository explicitly distinguishes:

- absolute integrability;
- conditional/improper convergence;
- principal-value constructions;
- source-defined Feynman/distributional amplitudes.

The remaining D7-S2 task is therefore no longer “does every fixed-label source-order Haar integral converge absolutely?” for this channel; it is to determine whether the published/source-defined causal prescription supplies a mathematically legitimate non-absolute collision extension and, if so, with what uniqueness/order-independence properties.

## Claim guards

- No universal statement over all boundary channels/spins is claimed.
- No spin-sum theorem is claimed.
- No cancellation after summing `T+ + T-` is denied; indeed that sum restores the Wigner branch and cancels the cubic pole edgewise.
- No principal-value or distributional finite value is claimed or excluded.
- No equality with the reordered ten-spectral representation is claimed.
- `D7-S2 = NOT_CLOSED` pending the source-defined collision-extension question.
- `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- No terminal D7 selector is authorized.
- Candidate Gravity remains inactive.
