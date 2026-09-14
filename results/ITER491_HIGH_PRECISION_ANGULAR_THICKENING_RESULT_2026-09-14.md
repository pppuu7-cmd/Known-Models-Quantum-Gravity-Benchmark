# Iter491 — high-precision source-group re-evaluation of frozen Iter490 angular thickening

Date recorded: 2026-09-14
Terminal classification: `SCIENTIFIC_FAIL_ITER491_ANGULAR_THICKENING_HP`

## Frozen authority
- parent one-dimensional classification: `SCIENTIFIC_FAIL_ITER487_HAAR_ESCAPE_ACTUAL_ENVELOPE_REVALIDATED_BY_ITER489`
- Iter490 terminal parent: `INFRASTRUCTURE_OR_NUMERICAL_FAIL_ITER490`
- Iter491 preregistration: `014143403aa1ed9f32faf5c8cc4eff7ee8065d53`
- Iter491 implementation: `a7baa532b99aceeb46cd03795df017cf46aec172`
- Iter491 aggregate classifier: `a337cf01a81540b4e8ccd934256692eaf7de6c47`
- workflow / production head: `13b758af653184cb0d77ab5d663b8ebb06dce813`
- authoritative run: `34792644222`
- source-lock job: `103819634495`
- aggregate job: `103820671865`
- aggregate artifact: `10329135024`
- aggregate digest: `sha256:fb7881955756e63b309865f59ad3fa726641ed780c8d946dd805a1e69cf5e61f`

## Frozen production completeness
All 12/12 expected lanes are present and valid. There are no missing lanes and no invalid lanes. Every lane — all three frozen causal patterns at all four frozen angular radii — is classified `SCIENTIFIC_FAIL_ITER491_ANGULAR_THICKENING_HP` by the prospectively frozen lane classifier.

The workflow completed `success`; this is consistent with the design because a scientific FAIL is a valid production result rather than an infrastructure failure.

## Aggregate numerical controls
The high-precision source-group construction removes the Iter490 numerical ambiguity without changing the frozen scientific object:
- maximum high-precision KAK absolute reconstruction residual across the reported samples: `2.703624106358193e-90`, versus frozen `<1e-50`;
- maximum source-object identity relative residual versus the same frozen Iter490 double parameter point: `1.9625527574932623e-12`, versus frozen `<1e-9`;
- maximum 80/120-digit anchor relative edge-matrix difference: `6.3113450385550355e-78`, versus frozen `<1e-20`;
- maximum 80/120-digit beta difference: `4.416646276150437e-74`, versus frozen `<1e-20`;
- all frozen chart-rank, determinant, SU(2), K5-cycle, center-regression, Haar, additive and finite/positive controls pass in the valid lanes.

Thus the Iter490 failure was numerical/control-level, while Iter491 successfully evaluates the same prospectively frozen angular object at sufficient precision.

## Scientific result
No frozen angular radius in `{0.0025, 0.005, 0.01, 0.02}` has all three causal lanes classified sampled NONDECAY, and no radius is sampled ROBUST. Therefore:
- `robust_radii = []`;
- `sampled_nondecay_radii = []`;
- `largest_robust_radius = null`;
- `largest_sampled_nondecay_radius = null`.

Across all valid sampled points the post-Haar actual-slope range is approximately
`[-9.911449338673545, -1.8577685492822726]`.
The largest sampled slope drift is `2.733679807240682`.

The unperturbed center remains the previously qualified one-dimensional NONDECAY witness (center slopes near `+4`), but the prospectively frozen nonzero angular perturbations contain strong DECAY witnesses. For example, the smallest frozen radius `eps=0.0025`, causal `0to5`, sample 0 gives slopes approximately `[-6.0367, -6.0252, -6.0481, -6.0426]` over the four frozen rho witnesses while all source/numerical controls pass.

Therefore the prospectively frozen sampled 20-dimensional angular-thickening hypothesis fails: the qualified one-dimensional NONDECAY center is not stable over these four frozen sampled angular radii.

## Exact interpretation ceiling
This FAIL does **not** prove that no smaller nonzero angular neighborhood exists around the center. In particular, shrinking below `eps=0.0025` after seeing this result is forbidden within Iter491 and would require a new, separately motivated prospective gate.

Iter491 also does not establish that the center is mathematically measure-zero or singular in the full Haar domain; a local asymptotic/tangent analysis would be required to determine whether the positive center exponent is destroyed at arbitrarily small generic angular perturbation and with what scaling.

The result therefore does **not** establish an absolute Haar-divergence theorem or an absolute Haar-convergence theorem. The one-dimensional Iter487/489 NONDECAY witness remains valid in its zero-angular-measure path scope, while the current finite sampled thickening attempt is decisively negative on its prospectively frozen radii.

## Consequence for next gates
A post-hoc smaller-radius grid is not admissible as a continuation of this experiment. The highest-information admissible angular successor, if pursued, is a separately preregistered local asymptotic/tangent-response gate at the center: derive or prospectively estimate the leading dependence of the post-Haar exponent/slope on generic compact angular directions as `eps -> 0`, with independent direction sets and a frozen scaling law. Such a gate would test whether the center path is an unstable ridge or whether an unresolved parametrically tiny open cone remains.

This angular question is independent from two other D7-S2 blockers and may be worked in parallel with them: the exact ten-source-spectral integration object and the K5 collision/boundary-value stream (Iter461, still queued at the time this result is recorded).

## Claim locks
No physical causal-vertex finiteness/divergence theorem. No absolute Haar convergence/divergence theorem. No conclusion about ten source spectral integrations. No conditional/PV or source-defined distributional conclusion. No D7-S2 closure. No terminal D7 classifier. Candidate Gravity remains inactive.