# Iter486 preregistration — shared-node full-network Haar escape envelope

Date frozen: 2026-09-14
Status: FROZEN BEFORE IMPLEMENTATION/PRODUCTION

## Parent authority
- terminal Iter485: `ITER485_SHARED_NODE_TEN_EDGE_TOLLER_MAGNETIC_NETWORK_QUALIFIED_SCOPED`;
- source Haar snapshot: `sources/arxiv_2202_04360_sl2c_haar_cartan.json`, source-pinning commit `2cbfa37aea635bd76e1fb0291191b6efb32699cc`.

## Scientific question
Does the already-qualified full Iter485 ten-edge magnetic/intertwiner contraction decay fast enough along prospectively fixed shared-node large-rapidity escape profiles to beat the actual radial `SL(2,C)` Haar growth, or does at least one stable shared-node profile fail exponential absolute decay?

This gate is a large-rapidity **radial-envelope diagnostic**. It is stronger than the older reduced crossing-factor escape surrogate because it retains all ten source Toller matrices, the same five shared node variables, causal branch signs, and all 243 genuine boundary-intertwiner channels. It is still not a full group-integral or spectral-integral theorem.

## Source Haar lock
Use the Cartan parameterization and Haar density pinned from arXiv:2202.04360:
`dg = const * sinh(r)^2 dr du dv`.
Only the irrelevant overall constant is omitted from logarithmic slopes. No extra suppressing weight is allowed.

## Frozen realization
- `j=k=l=1` exactly as Iter485.
- Four source spectral witnesses per lane: `rho in {0.35,0.9,1.6,2.7}`.
- Base shared-node panels: Iter483/485 panels `{A,C}` in `strong` regime only; no post-hoc panel selection.
- Gauge-fixed node 0 remains identity.
- Escape cluster sizes `s in {1,2,3,4}` with fixed cluster `S_s={1,...,s}`.
- Escape radii `R in {6,8,10,12}`.
- For `a in S_s`, set `g_a(R)=B_z(R) g_a^0`; nodes outside the cluster remain `g_a^0`. This common left boost preserves every internal-cluster relative element exactly while forcing the crossing edges to carry the shared escape.
- All ten edge elements remain `h_ab=g_b^{-1}g_a` and therefore arise from exactly five shared nodes.
- Causal patterns: the same frozen Iter485 `{0to5,1to4,2to3}` assignments and edge branch signs.
- Full boundary contraction: evaluate all 243 `3^5` intertwiner channels at every `(R,rho)`.
- 24 independent lanes = 2 panels x 4 cluster sizes x 3 causal patterns, `fail-fast:false`.

## Frozen observables
For each `(R,rho)`:
1. construct all ten source Toller matrices using the Iter484 source KAK lift;
2. compute all 243 contracted values and `C_max(R,rho)=max_I |C_I|`;
3. compute actual escaped-node Haar log density
   `log H(R)=sum_{a in S_s} 2 log sinh(eta_a(R))`,
   where each `eta_a(R)` is extracted from the actual Cartan/KAK decomposition of `g_a(R)` rather than replaced by `R` by assumption;
4. define `log E(R,rho)=log C_max(R,rho)+log H(R)`;
5. define `network_slope` from a linear fit of `log C_max` on `R={8,10,12}`;
6. define `haar_slope` from `log H` on `R={8,10,12}`;
7. define `actual_slope` from `log E` on `R={8,10,12}`;
8. define slope drift as the absolute difference between the fits on `{6,8,10}` and `{8,10,12}` for `log E`.

If direct contractions approach floating-point range limits, the mathematically identical factorization
`log C_max = sum_e log ||M_e||_max + log(max_I |C_I^normalized|)`
may be used, with all normalized factors finite and nonzero; this is numerical rescaling only and may not alter the frozen object.

## Frozen controls
A. Shared-node K5 cycle residual `<1e-8` at every R.
B. Per-edge source KAK reconstruction residual `<1e-8` at every R.
C. Every relevant numerical observable is finite; `C_max>0` for every `(R,rho)`.
D. Haar radial asymptotic control: `|haar_slope-2s| < 0.05` in every lane.
E. Haar insertion bookkeeping: `|(actual_slope-network_slope)-haar_slope| < 1e-8`.
F. At `R=10`, corrupt exactly one crossing edge independently of the nodes; the K5 cycle residual must exceed `1e-5`.
G. The inherited false Toller composition negative control must exceed `1e-5` at at least one frozen rho in each lane.

Control failure makes the lane invalid; scientific slope labels are assigned only to valid lanes.

## Frozen scientific classifier
For each valid `(lane,rho)`:
- **DECAY witness** iff `actual_slope <= -0.10` and slope drift `<=0.05`.
- **NONDECAY witness** iff `actual_slope >= 0.00` and slope drift `<=0.05`.
- otherwise `ASYMPTOTIC_INCONCLUSIVE`.

Aggregate labels:
1. `ITER486_HAAR_ESCAPE_ACTUAL_ENVELOPE_DECAY_QUALIFIED_SCOPED` iff all 24 lanes are valid and every frozen rho in every lane is a DECAY witness.
2. `SCIENTIFIC_FAIL_ITER486_HAAR_ESCAPE_ACTUAL_ENVELOPE` iff all expected lanes are valid and at least one frozen `(lane,rho)` is a stable NONDECAY witness. This means only failure of exponential absolute-decay along at least one prospectively fixed shared-node escape profile.
3. `INCONCLUSIVE_ITER486_HAAR_ESCAPE_ASYMPTOTIC` iff all expected lanes are valid, there is no NONDECAY witness, but not all points satisfy DECAY.
4. `INFRASTRUCTURE_OR_SOURCE_FAIL_ITER486` iff required source/provenance/runtime/output controls fail before the scientific classifier is meaningful.

## Interpretation ceiling
Even a stable NONDECAY witness is **not** by itself a theorem that the physical causal vertex diverges. A one-dimensional escape profile can diagnose failure of this exponential absolute-envelope test, but a full Haar statement would still require control of neighborhoods/angular measure and then the ten spectral integrations. Conditional cancellation, principal-value/boundary-value prescriptions, and source-defined distributional amplitudes remain separate questions.

A DECAY aggregate likewise does not prove the full Haar integral converges; it only rules out these frozen escape profiles as exponential absolute obstructions.

No D7-S2 closure, terminal D7 label, or Candidate Gravity authorization is permitted by Iter486 alone.
