# KMQGB Critical Review — source-order j=1 full-collision absolute divergence

Date: 2026-09-15
Lane: independent Critical Review / Verification
Verdict: `CONFIRMED_SCOPED`

## RESULT_REVIEWED

Reviewed exactly one bounded substantive result:

`research/SOURCE_J1_FULL_COLLISION_ABSOLUTE_DIVERGENCE_THEOREM_2026-09-15.md`

Historical theorem commit: `bf43183b12799e217e452c6335edc1114e389352`.

Scope reviewed: the source-order, gauge-fixed K5 integrand with fixed `j=1`, fixed nonzero real `rho_e`, frozen causal signatures `{0to5,1to4,2to3}`, and fixed allowed intertwiner channel `00000`, near the full K5 collision stratum. The claim reviewed is failure of ordinary local absolute Haar integrability only.

The independent Iter504 Research workflow `34907349374` is still non-terminal/queued at review time. No Iter504 partial substantive value was used and no competing Iter504 verdict is created here.

## PREREG_CHECK

This result is a deductive local theorem, not an empirical threshold gate or an outcome-tuned classifier. No post-hoc numerical threshold, fitted domain cutoff, selected confidence level, or changed pass/fail rule is used in the proof.

The algebraic witness is existential: one nonzero angular/compact-base witness plus continuity is sufficient to disprove local absolute integrability. Selection of a rational witness after deriving the exact cubic pole is therefore not a hidden threshold/domain relaxation; it is a constructive proof witness. The later certificate repair changes no scientific contract.

Status: `PASS_FOR_DEDUCTIVE_THEOREM`; no new scientific gate was retroactively substituted.

## OBJECT_IDENTITY_CHECK

The theorem uses the source-order object, not the reordered ten-spectral surrogate:

`one-wedge source Toller matrix -> product of ten Toller matrices -> gauge-fixed four-group Haar integral`.

At the full collision, after gauge fixing vertex 0, the collision stratum is `K^4` with `K=SU(2)`. Since `dim SL(2,C)=6` and `dim SU(2)=3`, the normal dimension in `G^4` is exactly `4*(6-3)=12`. A smooth nonvanishing Haar density in tubular coordinates therefore contributes normal radial measure comparable to `t^11 dt dOmega`.

For the fixed tangent configuration all ten relative tangent differences are nonzero, so the witness lies away from lower collision sub-cones. A sufficiently small angular neighborhood preserves this separation.

Status: `CONFIRMED`.

## SOURCE/REALIZATION_CHECK

The one-edge input is the exact j=1 source realization already encoded in `code/iter499_arb_core.py::source_coeffs` and reconstructed by `full_toller`. Its leading causal branches are opposite cubic poles with nonzero scalar

`A(rho)=3 i/[4 rho(1+rho^2)]`

for every fixed nonzero real `rho`, and with frozen spin-1 quadrupole `Q=diag(1,-2,1)`.

The exact certificate imports the frozen K5 incidence/sign data from `iter482_common_node_su2_control` and the frozen spherical intertwiner supports from `iter499_arb_core`; it then verifies the spherical-to-Cartesian map exactly rather than replacing the source basis with an unverified surrogate.

Status: `CONFIRMED`.

## PROVENANCE_CHECK

Initial certificate run `34908370750` failed before substantive contraction because `np.einsum(...).item()` was applied to an object already returned as `fractions.Fraction`. This was a reproducibility/code blocker only, not scientific evidence for or against the theorem.

Repair commit `bcc221b2a77572ace32fcb9dbd84fd78fb90ec03` changed scalar extraction only:

`return result.item() if hasattr(result, 'item') else result`.

It did not change the tangent configuration, intertwiners, K5 incidence, causal signatures, expected coefficient, channel count, source formulas, hypothesis, or interpretation ceiling.

Post-repair certificate run `34910999176` completed successfully at the repair head. Artifact `10374004571`, digest `sha256:3e378db8f5ac81d5086cbc82f53b2915154bd2d695206154f0220c4ce210fdc3`.

Status: `CONFIRMED`; historical failed run retained as failed provenance rather than rewritten.

## SAME_REALIZATION_CHECK

The successful certificate verifies the same realization used by the theorem:

- exact spherical-to-Cartesian intertwiner identity: true;
- intertwiner norms: `1`, `1/3`, `1/5`;
- same rational tangent points;
- same frozen K5 incidence/index ordering;
- same causal signature table;
- exact channel `00000` leading angular coefficient `11/24`;
- exact count `224/243` nonzero leading angular channels.

No independent-edge realization, polar-factor surrogate, altered KAK convention, fitted cancellation, midpoint replacement, or sampled-only object is promoted to the theorem.

Status: `CONFIRMED`.

## NUMERICAL/STATISTICAL_CHECK

The decisive contraction is exact rational arithmetic, not floating-point hypothesis testing. There is no statistical p-value, confidence interval, Monte Carlo coverage, or numerical threshold on which the theorem depends.

The local integrability exponent is analytic:

- ten edge poles: `t^(-3*10) = t^-30`;
- 12-dimensional normal radial measure: `t^(12-1) dt = t^11 dt`;
- lower-bound radial integrand: `t^(11-30)=t^-19`;
- `integral_0^eps t^-19 dt` diverges.

Status: `CONFIRMED`.

## COUNTEREXAMPLE_ATTEMPTS

1. **Wrong stratum dimension.** Recomputed codimension from `G^4` versus `K^4`: `24-12=12`; no missing normal directions found.
2. **Pair-coincidence contamination.** The frozen rational tangent witness has all ten pair differences nonzero; an open angular neighborhood can be chosen with all ten norms uniformly bounded away from zero.
3. **Leading coefficient isolated at a measure-zero ray.** The coefficient is a continuous function of compact-base and angular variables away from pair coincidences. `11/24 != 0` therefore yields a product neighborhood of positive Haar/angular measure with a uniform positive lower bound after shrinking it.
4. **Remainder cancels the leading singularity.** On that smaller neighborhood the edge Laurent remainders are one power less singular; the product remainder is `O(t^-29)` relative to a nonzero `t^-30` coefficient, so it cannot cancel the lower bound for sufficiently small `t`.
5. **Causal sign cancellation.** Frozen opposite-sign edge counts are `0,4,6`; all are even, so the cubic branch-sign product is `+1` for each frozen causal class.
6. **rho zero/pole ambiguity.** The theorem explicitly excludes `rho=0`; for each fixed nonzero real `rho_e`, `A(rho_e)` is finite and nonzero.
7. **Basis/index mismatch.** Exact spherical-to-Cartesian mapping and frozen K5 incidence are checked by the successful repository certificate.
8. **Green CI promoted to science.** Rejected as an argument. The verdict rests on the exact certificate plus analytic normal-measure/lower-bound proof; the earlier red run is correctly classified as an implementation blocker.
9. **Fixed-channel result promoted to full vertex.** Rejected. Possible cancellations after summing channels/branches and non-absolute source prescriptions remain outside this theorem.
10. **Collision theorem confused with noncompact-tail result.** Rejected. The separate spanning-tree theorem concerns fixed positive collision cutoff; the present theorem concerns cutoff removal at the full collision.

No counterexample to the stated scoped theorem survived these checks.

## OVERCLAIM_CHECK

The historical theorem's interpretation ceiling is adequate and must be retained:

- confirms ordinary local absolute divergence only for the specified fixed `j=1` channel;
- does not prove divergence of every boundary channel or spin sector;
- does not prove divergence after summing channels or causal branches;
- does not rule out principal-value, conditional, Feynman, or distributional extensions;
- does not establish equality with a reordered ten-spectral representation;
- does not close D7-S2, D7-S3, or D7-S4;
- does not authorize any terminal D7 selector;
- does not activate Candidate Gravity.

A useful wording qualification for future exposition is to state the positive-measure neighborhood explicitly as a product neighborhood in compact-base and angular variables, not merely as a single radial ray. The existing continuity argument already supplies this and no scientific conclusion changes.

## VERDICT

`CONFIRMED_SCOPED`

The scoped theorem is supported by same-realization exact provenance and an analytic local lower-bound argument. The post-result scalar-extraction repair is non-contractual and does not require a new scientific preregistration.

## QUALIFICATIONS

1. Confirmation is limited to ordinary **absolute Haar integrability** of fixed channel `00000` near the full K5 collision.
2. This is not a family-wide causal-vertex no-go theorem.
3. This is not a statement about conditional/PV/distributional source-defined amplitudes.
4. `224/243` is auxiliary finite-certificate information; only the exact nonzero `00000` witness is used for the theorem and the count is not promoted to universality.
5. Iter504 remains independent and non-terminal; no partial Iter504 science is consumed here.
6. Iter461 remains the registered independent collision-partition stream and is not duplicated or pre-consumed.

## UPDATED_STATE

- `SOURCE_J1_FULL_COLLISION_ABSOLUTE_DIVERGENCE_THEOREM`: `CONFIRMED_SCOPED` by Critical Review.
- Exact certificate authority: repair head `bcc221b2a77572ace32fcb9dbd84fd78fb90ec03`, run `34910999176`, artifact `10374004571`, digest `sha256:3e378db8f5ac81d5086cbc82f53b2915154bd2d695206154f0220c4ce210fdc3`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- Terminal D7 labels and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden.
- Candidate Gravity remains inactive.

## NEXT_ADMISSIBLE_GATE

Do not rerun or broaden this proof as a universal channel theorem without a separately justified scope extension. The next admissible collision-side work is either:

1. consume authoritative Iter461 when its registered run becomes terminal and use it to organize the remaining collision strata; or
2. prospectively specify and verify the mathematical legitimacy, uniqueness, and order-independence (where applicable) of a non-absolute source-defined/Feynman collision extension for the already-confirmed fixed-channel obstruction.

No terminal D7 classifier is authorized by this review.
