# Iter480B — source-backed four-valent intertwiner contraction — 2026-09-13

## Authority
- withdrawn pre-production Iter480 prereg: `9e1eb674e4c05e1cb3dcea1d01104d29e7cf29fa`; invalidation `dcc77ab7c7bd061f134797236372126b27117d0b`
- Iter480B preregistration: `da49c5b97494992e62045355579645698da91821`
- implementation: `2ac4c4091bf39005bccd87ca4a11e910bcb88bf0`
- matrix implementation patch: `be9f581bc63e59f283ab9ab4cdb0d142b0206e19`
- initial production head: `265ab546f24e922894b85b9a3737475eb38629e5`
- initial run `34773180686`: NONAUTHORITATIVE numerical/control-evaluator failure; diagnostic record `006cfa06fc5d8b5855b8253b036203ecb23b3852`
- minimal evaluator-only repair / authoritative retry head: `fb7395328f2e1c12a8a49fc6b89b150de92cd4f1`
- authoritative retry run: `34773320961`
- aggregate job: `103766837720`, SUCCESS
- aggregate artifact: `10323081045`
- aggregate digest: `sha256:ef44f8a32e7641f86bcef01376eb6e7a10b26584c6ffb0ff1c23c1e45de9e3aa`

Raw authoritative lane provenance:
- g7-0to5 job `103766783499`, artifact `10323160487`, digest `sha256:d60db9bc0af288584e66c2b5783677cdf0af609378e9514f332ced061aa7449c`
- g7-1to4 job `103766783487`, artifact `10322173780`, digest `sha256:188dd75468871d2230519ea33a6b119e7321536b204f96aaa328baa64e3b9f04`
- g7-2to3 job `103766783513`, artifact `10322612380`, digest `sha256:2ca3d627532a41325bac82f03efbde80709001938cd0d2093dad983c65c5e5ff`
- g8-0to5 job `103766783525`, artifact `10321804327`, digest `sha256:71c5ef6aaa82150b5c2375bc9d6488c4c314a24e6f1e125d4a7f17c3821856f3`
- g8-1to4 job `103766783523`, artifact `10323071031`, digest `sha256:a983f82aea8c5d58c41b3ae0b94e363e59b0889a3820c7c0b359bb60b4c6c8de`
- g8-2to3 job `103766783378`, artifact `10322099024`, digest `sha256:c827ecc815fca0df94f308a1b32d27586d30521e092c45ffe977f640ecd6b47e`

## Scientific classification
`ITER480B_SOURCE_INTERTWINER_CONTRACTION_NONZERO_WITNESS_SCOPED`

All six frozen gamma x causal-representative lanes pass after raw-artifact consumption, not merely green CI.

For every frozen panel:
- Eq.(90) four-valent SU(2) intertwiner support/norm/orthogonality controls pass; representative Gram residual is `5.55e-17`.
- all 243 recoupling-channel assignments are evaluated;
- exactly `130/243` assignments provide a dimensionless nonzero leading-coefficient witness under the prospectively frozen threshold `R=|A|/S > 1e-12`;
- maximum witness ratio is the same in all panels, `R_max = 0.0046296296296296285` (approximately `1/216`), attained at channel tuple `[0,0,0,0,0]`;
- pure magnetic-label reindexing control passes with relative multiset residual `0` to `2.10e-89`;
- all-zero Toller coefficient negative control vanishes exactly (`0.0`).

The authoritative aggregate contains all 6 expected lanes and classifies all 6 as scientific PASS.

## Run-1 integrity note
Run `34773180686` is not a scientific FAIL. Its only failing predicate was an implementation of the already-frozen reindex control that divided each near-zero sorted magnitude difference by its own roundoff-scale denominator. The scientific witness, intertwiner controls and zero-vector negative control were already valid. The retry changed only the evaluator to the preregistered multiset-level relative residual and retained the same `1e-10` threshold, model, panels and witness criterion.

## Scientific meaning
Within the frozen equal-spin `j=1` diagonal-collision control, genuine source-compatible four-valent SU(2) boundary-intertwiner contraction does **not** force universal cancellation of the individual-branch Toller leading coefficient. Nonzero invariant contractions exist in every frozen gamma/causal panel.

This narrows the possible cancellation locus beyond Iter479: cancellation, if it occurs in the physical source object, must use ingredients absent from this gate (angular `U1/U2` structure tied to group elements, shared group/Haar integration, non-diagonal magnetic mixing, spectral integration, Jacobians, or full K5 collision geometry), rather than the five boundary intertwiner contractions alone.

## Scope guards
This is not a full causal-vertex result and is not a finiteness/divergence theorem. It does not show that every boundary channel is nonzero. It does not close D7-S2, D7-S3 or D7-S4. It does not authorize D7 terminal classification or Candidate Gravity.

## D7 state
- D7-S2: `NOT_CLOSED`
- D7-S3: `NOT_CLOSED`
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`
- D7-S5: `NOT_AUTHORIZED`
- Candidate Gravity: inactive

## Working readiness rubric
Keep `D2≈82%`, `D4≈68%`, `D7≈56%`, integrated path `≈67%` (`Δ0` on all four metrics relative to Iter479). Iter480B materially narrows one cancellation mechanism but does not close a frozen D7 prerequisite.

## Next permitted gate
Prospectively test the source Eq.(7) angular magnetic mixing together with the qualified boundary intertwiner contraction, keeping the result explicitly scoped away from shared SL(2,C) group/Haar integration. The implementation should reuse the already-qualified Iter479 Wigner-matrix convention rather than invent a new one. A later gate must still restore common group-variable dependence before any physical D7-S2 closure claim.
