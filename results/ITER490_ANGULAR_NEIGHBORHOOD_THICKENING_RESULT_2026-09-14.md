# Iter490 — full-angular sampled thickening of a valid Haar NONDECAY witness

Date recorded: 2026-09-14
Terminal classification: `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER490`

## Frozen authority
- parent promoted classification: `SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE_REVALIDATED_BY_ITER489`
- preregistration: `89dc75bcd702b60e7eb0b0c18a31f884214aa5c4`
- implementation: `65f4b5bfff46c209b9fe3694e8b0df189e70accb`
- aggregate classifier: `ea91ce08f0508620e205b69474f5e68afcb88045`
- workflow / production head: `2d25756442536cbf8ab03d6044481c1f0858040c`
- authoritative workflow run: `34791552967`
- source-lock job: `103816612021`
- aggregate job: `103817112953`
- aggregate artifact: `10328343195`
- aggregate artifact digest: `sha256:a45c55bd93095f61e0aaa9b79f4ea4810e7f54b8fb07c9a13c895fe8dffc9d58`

## Frozen production completeness
All 12/12 expected lanes were created and completed successfully at the workflow level: three causal patterns `{0to5,1to4,2to3}` times four prospectively frozen angular radii `{0.0025,0.005,0.01,0.02}`. Each lane executed the frozen 16 deterministic 20-dimensional perturbation samples plus the center regression. The aggregate job completed and emitted the authoritative summary artifact.

Green CI is not a scientific PASS. The frozen aggregate classification is `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER490` because all 12 lanes are invalid under the prospectively frozen validity controls.

## Exact invalidation
The only systematic failing sampled control is `kak_two_tier`. The chart tangent-rank control is exactly `[5,5,5,5]` in every lane; center regressions reproduce the parent C-s4 slopes; cycle, finite/positive contraction, Haar-slope, Haar-bookkeeping and source-additive controls otherwise pass on the reported samples.

The frozen KAK rule requires the same absolute reconstruction threshold `<1e-8`: use double precision when it passes; otherwise re-evaluate the same edge matrix using the 100-digit KAK method and require the unchanged `<1e-8` absolute residual. In the angularly perturbed large-rapidity samples, that fallback remains above threshold in many samples, so no sampled NONDECAY/DECAY state is promotable from Iter490.

Observed invalid-sample counts for the KAK control by lane range from 4/16 at the smallest radius to 16/16 at the larger radii. Therefore there is no valid radius and the aggregate fields `largest_robust_radius` and `largest_sampled_nondecay_radius` are both null.

## Independent numerical diagnosis after terminal classification
A separate diagnostic, performed only after the frozen Iter490 verdict was known, reconstructed the prospectively frozen source geometry from the committed formulas without changing any scientific criterion. It finds:
- node determinant drift remains small, from about `1.4e-13` at eps `0.0025` to about `9.6e-13` at eps `0.02`;
- edge matrices at `R=12` reach max-entry scales from about `1.38e3` to `1.11e4` across the frozen radius grid;
- edge determinant drift grows from about `6.6e-11` to about `6.45e-9`;
- ordinary double KAK reconstruction residuals consequently reach about `8.0e-8`, `1.15e-6`, `5.32e-6`, and `3.77e-5` across the four radii, while the corresponding relative reconstruction residual remains only about `6.8e-11` to `3.4e-9`.

This supports a conditioning hypothesis: independently rotating already-large boosted nodes destroys the exact common-left cancellation in floating arithmetic, so relative edge matrices become large and an absolute matrix-entry KAK residual becomes scale-sensitive. This diagnosis does **not** retroactively validate Iter490, does not authorize replacement of its frozen absolute threshold, and does not promote its raw slopes.

## Scientific scope
Because every Iter490 lane is invalid, none of the raw perturbed slopes — including raw negative slopes seen in some samples — may be used as a scientific angular-thickening verdict. Iter490 therefore neither confirms positive-measure NONDECAY nor demonstrates that the one-dimensional Iter487 witness is path-isolated.

The parent one-dimensional result remains valid only in its previously authorized scope: `SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE_REVALIDATED_BY_ITER489`.

## Next admissible gate
A new prospective precision/stability gate is required. It must preserve the frozen angular chart/radii/samples and source group element mathematically, but construct the perturbed `SL(2,C)` node and relative matrices at high precision before KAK decomposition, rather than attempting to recover high precision from an already rounded ill-conditioned edge matrix. It must include an independent precision-convergence check and a source-object identity check before any angular-thickening science classifier is allowed.

If that new gate changes the scientific object, sample set, radii, slope thresholds or interpretation ceiling, it is invalid as a revalidation and must be treated as a distinct scientific test.

## Claim ceiling
No absolute Haar-divergence theorem. No physical causal-vertex finiteness/divergence theorem. No ten-spectral-integral conclusion. No conditional/PV or distributional conclusion. No D7-S2 closure. No terminal D7 classifier. Candidate Gravity remains inactive.