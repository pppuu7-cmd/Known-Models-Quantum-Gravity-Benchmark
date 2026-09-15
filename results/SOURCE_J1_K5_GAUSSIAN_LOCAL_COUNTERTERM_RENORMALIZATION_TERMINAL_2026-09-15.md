# SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION — terminal result

Date: 2026-09-15
Status: TERMINAL

## Authority

- Gate: `SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION_GATE`
- Frozen preregistration: `research/prereg/SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION_2026-09-15.md`
- Frozen preregistration commit: `ef8d34d3e82bec110c072f2b23361f7e2d07339c`
- Production workflow head: `d6def218a9977db5a8ee881dc0c3ddbfaaaeeb19`
- Authoritative GitHub Actions run: `34958385950`
- Aggregate job: `104346212113`
- Aggregate artifact: `source-j1-k5-gaussian-local-counterterm-summary`, artifact ID `10391698051`
- Aggregate artifact digest: `sha256:5b177b1ddb812997344ae7567924cd0af260fcb3b5ac74db2f5f1a43d3631880`
- Lane artifacts:
  - P1: artifact ID `10391658175`, `sha256:260be36704571324ffa116699dbefee545f214e03e11a53db56e0320acb65fa6`
  - P2: artifact ID `10392690095`, `sha256:c90beb4e5b3a64ca9d2a214fdb82c5353bd0aa17353021838b76da0011494b6a`
  - P3: artifact ID `10391388704`, `sha256:5ce3f775dfaab0dc2491dcc165ddd962dab10589153420ab065690bd12f248ac`

## Frozen terminal classification

`AUX_GAUSSIAN_LOCAL_COUNTERTERM_ANSATZ_INSUFFICIENT_SCOPED`

The workflow itself completed successfully, but the scientific classification comes from the frozen aggregate classifier, not from CI color.

## Controls

All frozen aggregate controls passed:

- all three P1/P2/P3 lanes present;
- all lane controls passed;
- P0 excluded from the deciding calculation;
- synthetic path-dependence fixture detected correctly;
- finite ambiguity dimension before the frozen normalization conditions = 14.

The lane implementation also enforced the parent `alpha=1` lock, positive covariance controls, exact calibration interpolation, independent linear/barycentric interpolation agreement, Laplacian identity controls, degree-14 adversarial held-out control, and the frozen P3 vertex-relabel control.

## Held-out result

For every held-out Gaussian test-function parameter

`alpha in {0.55, 0.95, 1.35, 1.75, 1.95}`

the path classifications were identical:

| path | frozen classification on all five held-out alpha |
|---|---|
| P1 | `DIVERGENT_AFTER_LOCAL_SUBTRACTION` |
| P2 | `FINITE_COMPATIBLE` |
| P3 | `DIVERGENT_AFTER_LOCAL_SUBTRACTION` |

Representative final `k=8` residuals illustrate the path contrast:

- alpha=0.55: P1 `-1.0656921361198557e28`, P2 `-4.9814306373e-54`, P3 `-3.8188543578`
- alpha=0.95: P1 `-4.3895446515306427e25`, P2 `-2.0518478595e-56`, P3 `-0.6661090019`
- alpha=1.35: P1 `-4.3895107108651358e25`, P2 `-2.0518478592e-56`, P3 `-0.1486175092`
- alpha=1.75: P1 `-1.0656674160018087e28`, P2 `-4.9814306353e-54`, P3 `0.1445717993`
- alpha=1.95: P1 `8.3441436084003879e30`, P2 `3.9004601872e-51`, P3 `-1138.6689623033`

The exact classification did not use magnitude alone: it used the prospectively frozen k=5..8 residual-growth classifier.

## Scientific meaning

The full prospectively frozen O(4)-invariant collision-supported local basis through uniform divergence degree 26,

`{Delta^j delta_0 : j=0,...,13}`,

was fixed independently at each regulator state by 14 calibration Gaussian test functions and then tested on five held-out Gaussian test functions. It failed to remove the frozen divergence on P1 and P3, while P2 was finite-compatible.

Therefore the specific order-<=26 radial/O(4)-invariant local-counterterm ansatz under this auxiliary aligned-K5 Gaussian regularization is insufficient.

This is stronger than the parent unrenormalized divergence witness because it survives a prospectively frozen finite-dimensional local subtraction and independent held-out test functions.

## What this does NOT establish

It does **not** establish:

- impossibility of all renormalized extensions;
- impossibility of counterterms supported on proper K5 collision strata;
- that the naive uniform scaling-degree/divergence-degree count is the correct power counting for the correlated anisotropic regulator paths P1-P3;
- source authorization of any counterterm scheme;
- existence or nonexistence of the published Eq. (4) distribution;
- model/family failure;
- D7-S2/S3/S4 closure;
- any terminal selector (`EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED`);
- Candidate Gravity activation.

## Next admissible frontier

Do **not** raise polynomial degree post hoc.

The next informative gate should determine which assumption behind the failed full-collision order-26 ansatz is wrong or incomplete. Highest-priority candidates are:

1. a prospectively frozen K5 collision-stratum / forest counterterm test allowing counterterms on proper collision diagonals in addition to the full collision; and/or
2. an anisotropic/correlated scaling-degree certificate establishing the correct power counting for P1-P3 before any larger jet basis is authorized.

The existing independent K5 collision-partition stream must be consumed before duplicating collision combinatorics.

Governance remains unchanged: `RQIR Core v1.0 = FROZEN`; D7-S2 and D7-S3 remain not closed; D7-S4 remains partial; Candidate Gravity remains inactive; KMQGB remains downstream of pinned DSIR authority.
