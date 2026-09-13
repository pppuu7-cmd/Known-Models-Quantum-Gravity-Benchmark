# Iter482 terminal result — common-node SU(2) correlated network

Date: 2026-09-13

## Authority
- Preregistration: `c23770098211125f25fb29d57c02db579febf2bf`.
- Implementation: `db87a3144b92aca8e0b1fce125c8ce20bc81ece7`.
- Production head: `07ff8d9b6d15279b73296b26767d0af260bf33a0`.
- Authoritative run: `34779214066`.
- Aggregate job: `103783117185`.
- Aggregate artifact: `10324334345`.
- Aggregate digest: `sha256:e80292603e898b730b7d7dce01e4bf239138b7637edf20a480e97891be233f81`.

## Scientific classification
`ITER482_COMMON_NODE_SU2_CORRELATED_NETWORK_NONZERO_WITNESS_SCOPED` — SCIENTIFIC PASS, scoped.

All 18 raw artifacts were consumed individually and the frozen aggregate was independently checked. The production matrix was `gamma in {7,8}` x three causal representatives x three common-node panels Q0/Q1/Q2.

## Raw results
- All 18/18 lanes have `scientific_pass=true` and every frozen A-E/G-J control true.
- All 18 lanes retain `243/243` nonzero normalized intertwiner-network witnesses above `R>1e-12`.
- `R_max` ranges from `4.301795749349847e-4` to `2.3126893230311866e-3`.
- Node-unitarity maximum residual: `2.2460374679281924e-16`.
- Edge-unitarity maximum residual: `6.662896919001242e-16`.
- Common-node triangle-cycle maximum residual: `4.0029660424867215e-16`.
- Common-left-gauge maximum residual: `3.4021815010030383e-16`.
- Deliberately corrupted-edge cycle residuals lie in `[0.3804220760106384, 0.42555149587837077]`, so the negative control is strongly detected.
- Eq.(90) intertwiner Gram residual is `5.551115123125783e-17` in every lane.
- Magnetic-basis reindex relative residual maximum is `6.532684628953591e-16`.
- Zero-edge-matrix controls vanish exactly.
- Diagnostic only: the prior Iter481 independent-edge P0/P1 products violate the same common-node triangle closure at O(1): `P0=1.3081607710474787`, `P1=1.2650210852112318`. This does not invalidate Iter481; it confirms its preregistered local-control scope and demonstrates why Iter482 is a materially stronger correlated test.

## Interpretation
On these frozen j=1 compact control slices, imposing one shared set of five SU(2) node rotations — hence exact K5 cycle consistency across all ten edges — still does not force universal cancellation of the already-qualified leading magnetic/intertwiner network. This removes the hypothesis that exact compact common-node correlation by itself is sufficient to generate the missing universal cancellation.

## Scope guards
The gate is a compact SU(2) common-node control only. It does not establish a unique Toller KAK decomposition for the pure-SU(2) slice, and it does not include noncompact `SL(2,C)` boosts, Haar integration, spectral integration, convergence, distributional boundary-value validity or a full causal-vertex theorem. `D7-S2=NOT_CLOSED`, `D7-S3=NOT_CLOSED`, `D7-S4=PARTIAL_GLOBAL_NOT_CLOSED`. No terminal D7 classifier or Candidate Gravity authorization follows.

## Next permitted gate
The next dependent step must restore genuinely noncompact common-node `SL(2,C)` geometry. Before using any source Eq.(7) factorization inside the network, prospectively qualify the numerical/exact KAK/polar-decomposition machinery on shared-node `SL(2,C)` panels with reconstruction, cycle, gauge, determinant, boost-rapidity and deliberately corrupted controls. Only after that machinery is terminally qualified may a source-faithful boost-dependent magnetic/Toller network or controlled Haar/quadrature gate be opened.