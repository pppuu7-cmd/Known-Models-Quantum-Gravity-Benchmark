# SOURCE_J1_K5_GAUSSIAN_FULL_COLLISION_RADIAL_ACTION_COMPLETENESS — terminal result

Date: 2026-09-15
Status: TERMINAL

## Authority

- Gate: `SOURCE_J1_K5_GAUSSIAN_FULL_COLLISION_RADIAL_ACTION_COMPLETENESS_GATE`
- Frozen preregistration: `research/prereg/SOURCE_J1_K5_GAUSSIAN_FULL_COLLISION_RADIAL_ACTION_COMPLETENESS_2026-09-15.md`
- Frozen preregistration commit: `ca36d4a61cff7e32746d1c13a676117d1e392c87`
- Implementation commit: `92784685805025a60c8c983e832aea055a9c4491`
- Workflow head: `d701a66f8c931044d341339ef89e24b0352c35d9`
- Authoritative run: `34959123795`
- Job: `104348228506`
- Artifact: `full-collision-radial-action-completeness`, ID `10392691339`
- Artifact digest: `sha256:c387f77e850452292e82d5ad43cce223c3327f2c81c4c53c0789de5911af7627`

## Frozen terminal classification

`AUX_GAUSSIAN_FULL_COLLISION_ORDER26_RADIAL_ACTION_SPACE_EXHAUSTED_SCOPED`

## Exact certificate

Every multiindex `beta in N^4` with `|beta|<=26` was enumerated exactly.

- total multiindices: `27405 = C(30,4)`
- nonzero actions on `phi_alpha(x)=exp(-alpha |x|^2)`: `2380`
- exact radial degree set: `{0,1,...,13}`
- exact action-space rank: `14`

Every positive control passed:

- all-even multiindices map nontrivially;
- any odd component maps to zero;
- degree set complete;
- Laplacian identity exact;
- monomial witnesses exact;
- rank 14 exact;
- no floating-rank decision.

Every adversarial control passed:

- synthetic cap 24 gives degree ceiling 12;
- synthetic cap 24 gives rank 13;
- a nonradial test factor distinguishes same-total-order multiindices, excluding accidental hard-wiring to total order.

## Strengthened consequence with parent run 34958385950

The parent counterterm-renormalization gate already tested the complete degree-<=13 alpha-polynomial action against independent held-out radial Gaussian test functions and found P1/P3 divergent after subtraction.

This exact theorem gate now proves that degree-<=13 alpha-polynomial space is the complete action, on that frozen radial Gaussian family, of **every distribution supported at the full K5 collision point with derivative order <=26**:

`C = sum_{|beta|<=26} c_beta partial^beta delta_0`.

Therefore, within the frozen auxiliary scalar Gaussian setup and the derivative-order cap 26, **no full-collision-supported local counterterm can remove the P1/P3 held-out divergence** observed in run `34958385950`.

This is stronger than the earlier wording restricted to the O(4)-invariant Laplacian basis.

## Claim ceiling

This exact scoped result does NOT rule out:

- counterterms supported on proper K5 collision strata;
- higher derivative order if a separately justified correlated/anisotropic scaling-degree analysis authorizes it;
- nonlocal or source-defined extensions;
- source-authorized prescriptions outside the auxiliary scalar Gaussian witness.

It does not establish published Eq. (4) existence/nonexistence, model/family failure, D7-S2/S3/S4 closure, any terminal selector, or Candidate Gravity activation.

## Next admissible frontier

The next efficient exact question is whether the same scalar Gaussian surrogate has superficially divergent **proper collision strata**. Reuse only K5 set-partition combinatorics from the historical Iter461 branch and recompute all local dimensions/divergence degrees for the current one-scalar-per-free-vertex surrogate. Do not import Iter461's 3D thresholds.
