# KMQGB Critical Review — full-collision radial action-space completeness

Date: 2026-09-15
Lane: independent Critical Review / Verification

## RESULT_REVIEWED

Exactly one latest terminal substantive Research result was reviewed:

- `results/SOURCE_J1_K5_GAUSSIAN_FULL_COLLISION_RADIAL_ACTION_COMPLETENESS_TERMINAL_2026-09-15.md`
- historical result commit `5e95318f29e26f4ea954f269cbec2c69fa8089d8`
- historical classification `AUX_GAUSSIAN_FULL_COLLISION_ORDER26_RADIAL_ACTION_SPACE_EXHAUSTED_SCOPED`
- preregistration commit `ca36d4a61cff7e32746d1c13a676117d1e392c87`
- implementation commit `92784685805025a60c8c983e832aea055a9c4491`
- workflow head `d701a66f8c931044d341339ef89e24b0352c35d9`
- authoritative run `34959123795`, terminal `completed/success`
- job `104348228506`
- artifact `10392691339`
- artifact digest `sha256:c387f77e850452292e82d5ad43cce223c3327f2c81c4c53c0789de5911af7627`

The exact action-space theorem and the parent-dependent strengthened consequence are distinguished below. A newer scalar K5 collision-strata gate was launched after this result; no partial substantive value from that child is used here and no competing child verdict is created.

## PREREG_CHECK

PASS for the exact theorem gate.

The preregistration prospectively freezes dimension 4, derivative-order cap 26, the radial Gaussian family `phi_alpha(x)=exp(-alpha |x|^2)`, exhaustive multiindex enumeration, exact integer/rational decisions, positive controls, cap-24 adversarial control, and a nonradial distinguishability control. Implementation and workflow follow the frozen theorem contract.

The preregistered consequence explicitly consumes the already-terminal parent run `34958385950`; therefore correctness of that consequence is conditional on the parent lane classifications being numerically valid.

## OBJECT_IDENTITY_CHECK

PASS for the exact theorem object.

The object is the action on the frozen radial Gaussian family of all full-collision-supported distributions

`C = sum_{|beta|<=26} c_beta partial^beta delta_0`

in `R^4`. This is not a statement about proper collision strata, higher derivative order, the published Eq. (4) distribution, or the physical EPRL vertex.

The strengthened consequence must remain on this same radial Gaussian object and derivative-order cap.

## SOURCE/REALIZATION_CHECK

PASS for the exact action-space certificate; QUALIFICATION for the parent-dependent consequence.

For a multiindex `beta`, the exact identity is

`<partial^beta delta_0, phi_alpha> = (-1)^|beta| partial^beta phi_alpha(0)`.

Any odd component gives zero. If `beta_i=2m_i`, the action is a nonzero integer coefficient times `alpha^(sum_i m_i)`, with degree at most 13. Conversely `(2j,0,0,0)` witnesses every degree `j=0,...,13`.

Therefore the complete radial action space through order 26 is exactly `span{1,alpha,...,alpha^13}` independently of the parent numerical run.

The later sentence asserting that this exact theorem eliminates full-collision counterterms for the observed **P1/P3** divergence imports numerical realization facts from parent run `34958385950`. That imported P3 fact fails the independent precision control below.

## PROVENANCE_CHECK

PASS for the theorem certificate.

Actions run `34959123795` is terminal success at the frozen workflow head. Artifact ID/digest agree with the terminal result. The artifact reports exact integer/combinatorial quantities, not fitted floating ranks:

- `27405 = C(30,4)` total multiindices;
- `2380 = C(17,4)` all-even/nonzero radial actions;
- degree set `{0,...,13}`;
- rank 14;
- exact Laplacian identities through `j=13`;
- cap-24 rank 13/degree ceiling 12;
- nonradial same-order distinguishability control passed.

Green CI is not used as scientific evidence by itself.

## SAME_REALIZATION_CHECK

PASS for theorem; parent consequence only partially survives.

The theorem's radial action family is exactly the same alpha-polynomial family used by the parent counterterm calibration/held-out protocol. Hence it is legitimate to infer that a numerically established parent residual cannot be repaired by switching from the Laplacian basis to another full-collision-supported derivative distribution of order <=26: all such distributions have the same 14-dimensional action space on these tests.

However, the parent P3 residual sequence was not numerically established at the frozen 180-digit precision. The theorem cannot convert numerical roundoff in a parent premise into a mathematical divergence theorem.

## NUMERICAL/STATISTICAL_CHECK

The exact theorem itself is non-statistical and is independently confirmed analytically:

1. `# {beta in N^4: |beta|<=26} = C(30,4) = 27405`.
2. Nonzero radial actions require all-even `beta=2m`, hence `|m|<=13`; their count is `C(17,4)=2380`.
3. Their alpha degrees are exactly `0,...,13`, and `(2j,0,0,0)` supplies a nonzero witness for each degree, so rank is exactly 14.

A counterexample-first precision replay was then applied to the imported parent P3 premise using the same frozen Gaussian pairing equations, P3 exponent vector `(1,2,3,4,2,3,4,3,4,4)`, calibration grid, held-out point `alpha=0.55`, and the same degree-13 interpolation, but with 320 decimal digits instead of the parent's 180-digit minimum.

For P3 at `alpha=0.55`, the high-precision residuals are:

- `k=6`: `-1.0949127330498382764892357116459382346352027441270e-62`
- `k=7`: `-4.0433526053326554200568336617239521644061980057827e-74`
- `k=8`: `-1.4764545628254437272581862546503870202686705952075e-85`

They decrease rapidly and are finite-compatible under the frozen classifier, rather than divergent. At `k=8` the raw P3 pairing is about `1.17480537896873048e163`, so the residual is roughly `1e-248` relative to the raw/counterterm scale. A 180-digit calculation cannot resolve that subtraction. The authoritative parent artifact instead reports an order-one P3 residual (`-3.818854...`) at this point, which is therefore catastrophic-cancellation noise, not a scientific divergence witness.

This is not merely a precision preference: it is an explicit numerical counterexample to the P3 premise used in the strengthened consequence.

An independent higher-precision replay of P1 remains strongly divergent. For example at `alpha=0.55`, the residuals are approximately

- `k=5`: `-1.90071344769965935e16`
- `k=6`: `-1.58057921276257207e20`
- `k=7`: `-1.29967464051664006e24`
- `k=8`: `-1.06569213611985570e28`,

with the last two base-2 growth exponents about `13.0054` and `13.00135`. Thus the parent's aggregate `AUX_GAUSSIAN_LOCAL_COUNTERTERM_ANSATZ_INSUFFICIENT_SCOPED` classification still has an independently stable deciding witness through P1; only the P3 divergence subclaim is refuted.

## COUNTEREXAMPLE_ATTEMPTS

1. **Wrong action-space dimension.** Failed to refute theorem: exact combinatorics gives 27405 multiindices and 2380 all-even survivors.
2. **Missing radial monomial degree.** Failed: `(2j,0,0,0)` witnesses every degree 0..13.
3. **Finite certificate promoted to nonradial theorem.** Blocked by scope: theorem is only action-space completeness on the frozen radial Gaussian family; the nonradial adversarial control correctly shows same-order derivatives can differ away from radial tests.
4. **Parent P3 numerical divergence.** Explicitly refuted by the 320-digit same-object replay above. The 180-digit residual is dominated by catastrophic cancellation.
5. **Parent P1 numerical divergence.** Refutation attempt failed: higher-precision replay preserves strong monotone growth and the frozen divergence predicate.
6. **Green CI promoted to science.** Rejected: exact algebra proves the action-space theorem; CI only establishes execution provenance.
7. **Full-collision result promoted to all strata.** Rejected: proper collision-stratum counterterms remain outside this result.
8. **Order-26 cap promoted to universal power counting.** Rejected: the result itself correctly leaves correlated/anisotropic scaling-degree analysis open.

## OVERCLAIM_CHECK

The terminal classification `AUX_GAUSSIAN_FULL_COLLISION_ORDER26_RADIAL_ACTION_SPACE_EXHAUSTED_SCOPED` is correctly scoped and remains supported.

The strengthened consequence is too broad in exactly one respect: the phrase that no order<=26 full-collision counterterm can remove the **P1/P3** held-out divergence treats P3 divergence as an established parent fact. It is not. The defensible consequence is presently:

> On the frozen radial Gaussian family and derivative-order cap 26, no full-collision-supported local distribution can remove the independently stable P1 held-out divergence, because all such distributions act through the already-tested 14-dimensional alpha-polynomial space.

No statement about P3 divergence should be consumed downstream until the parent P3 lane is rerun with a precision/conditioning control sufficient for the raw-minus-counterterm cancellation.

## VERDICT

`QUALIFIED`

The exact radial action-space theorem is confirmed. The parent-dependent P1 consequence survives. The P3 part of the strengthened consequence is numerically invalidated by an explicit same-object higher-precision counterexample.

## QUALIFICATIONS

1. `AUX_GAUSSIAN_FULL_COLLISION_ORDER26_RADIAL_ACTION_SPACE_EXHAUSTED_SCOPED` remains valid as an exact theorem about radial action-space completeness.
2. Parent run `34958385950` remains terminal historically; its aggregate ansatz-insufficient classification remains supported by stable P1 divergence.
3. Parent P3 `DIVERGENT_AFTER_LOCAL_SUBTRACTION` must not be used as a validated scientific premise.
4. This review does not assert that P3 has a regulator-independent renormalized limit; it establishes only that the reported 180-digit P3 divergence sequence is a cancellation artifact under the frozen numerical protocol.
5. Proper collision strata, derivative order >26 under separately justified power counting, and source-defined/nonlocal extensions remain open.
6. No Eq. (4) existence/nonexistence conclusion, model/family failure, D7 closure, terminal selector, or Candidate Gravity activation follows.

## UPDATED_STATE

- `SOURCE_J1_K5_GAUSSIAN_FULL_COLLISION_RADIAL_ACTION_COMPLETENESS = QUALIFIED`
- exact order<=26 radial action-space rank 14 = confirmed
- exact degree set `{0,...,13}` = confirmed
- strengthened full-collision consequence for P1 = confirmed scoped
- strengthened full-collision consequence for P3 = not validated; parent numerical cancellation counterexample established
- parent aggregate ansatz-insufficient classification = still supported by P1
- `D7-S2 = NOT_CLOSED`
- `D7-S3 = NOT_CLOSED`
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`
- terminal D7 labels/selectors remain forbidden
- Candidate Gravity remains inactive

## NEXT_ADMISSIBLE_GATE

Do not rewrite the historical result and do not infer a P3 scientific FAIL.

For P3, a repair may keep the same scientific contract but must raise working precision adaptively or prospectively freeze a conditioning/precision-doubling control that demonstrates stability of `R = F-C` after the approximately 160+ digit raw/counterterm cancellation. Since the frozen preregistration specified a **minimum** of 180 digits, increasing precision without changing object, grids, basis, classifier, or thresholds is an implementation repair rather than a new scientific hypothesis; any change to those scientific fields requires a new prospective gate.

For the active Research frontier, the newly launched scalar K5 collision-strata power-counting workflow is outcome-independent of this P3 correction at the level of exact partition/power-counting combinatorics and may proceed. Its partial outputs must not be consumed before terminalization. Any downstream statement that imports parent P3 divergence must instead consume this qualification.
