# O-LQG Area-Metric Birefringence γ Identifiability Gate — 2026-09-10

**KMQGB iteration:** 176  
**RQIR standard:** Core v1.0 FROZEN  
**CW2 object:** CW2-02 / O-LQG

## Question

If Iter174/175 eventually establish that the running area-metric Immirzi parameter is the same renormalized gamma entering the EPRL gamma-duality relation, does the Lorentzian area-metric GW/birefringence channel provide an independent gamma observable capable of breaking the Iter173 `{gamma,Delta_gamma}` degeneracy?

**Yes, structurally.**

The caveat is decisive: the result is authorized only after the same-realization parameter-identity map is established. Without that map it is cross-authority composition and cannot be used.

## Area-metric observable relation

The Lorentzian area-metric GW analysis parametrizes parity violation by `xi` with

`sinh(2 xi) = 1/gamma`

and the birefringence-axis rotation

`psi = -(1/2) arctan(tanh xi)`.

For positive gamma, this relation is exactly invertible.

Let

`y = tanh xi`.

From

`2y/(1-y^2) = 1/gamma`

one obtains the positive branch

`y = sqrt(gamma^2+1) - gamma`.

Since

`y = tan(-2 psi)`,

the relation reduces to the simple closed form

**`gamma = -cot(4 psi)`**

for

`-pi/8 < psi < 0`.

Thus `psi` alone is a structurally one-to-one gamma observable on the positive-gamma branch.

## Differential identifiability

Differentiating the inverse relation gives

`d psi/d gamma = 1/[4(1+gamma^2)]`.

This is strictly positive for every finite positive gamma.

Therefore the angle remains structurally sensitive to gamma throughout the branch, although the sensitivity becomes weak as `gamma -> infinity`.

This separates two questions that must not be conflated:

- **structural identifiability:** yes at finite positive gamma;
- **practical/resource identifiability:** potentially very poor, especially because the underlying area-metric detector signal is strongly suppressed if non-length modes are Planck-mass.

## Combination with the primordial gamma-duality relation

Iter173 generalized the primordial observable to

`q = (pi/8)(r+8 n_T)/Pi = 1/gamma - gamma - Delta_gamma`.

Take parameters

`theta = (gamma,Delta_gamma)`

and observables

`O = (q,psi)`.

The Jacobian is

`J = [[-1-1/gamma^2, -1], [1/(4(1+gamma^2)), 0]]`.

Its determinant is

**`det J = 1/[4(1+gamma^2)] > 0`**

for every finite positive gamma.

Therefore `q + psi` is structurally full rank for `{gamma,Delta_gamma}`.

This is stronger than the Iter173 geometry holdout in one respect: it provides an independent gamma-sensitive observable directly within the newly identified area-metric Lorentzian parity programme, rather than requiring an area-gap measurement. But it remains conditional on the same parameter-identity theorem.

## Direct duality-breaking estimator

Once same-realization gamma identity is established, the two observables give gamma and duality breaking algebraically:

`gamma = -cot(4 psi)`

and

`Delta_gamma = 1/gamma - gamma - q`.

Using the trigonometric identity

`cot x - tan x = 2 cot(2x)`,

this becomes the especially compact observable-level diagnostic

**`Delta_gamma = 2 cot(8 psi) - q`**.

Thus a measured discrepancy between the gamma inferred from area-metric birefringence and the primordial gamma-duality combination maps directly into `Delta_gamma`.

This is a high-value RQIR structure because `Delta_gamma=0` is a falsifiable cross-representation consistency condition rather than an independently fitted nuisance.

## Interpretation under RG flow

Iter175 established

`beta_Delta = beta_rho - (1+1/gamma^2) beta_gamma`.

Iter176 supplies a possible low-energy readout of both pieces of the resulting matching problem:

- `psi` measures the low-energy area-metric gamma, if the signal is accessible;
- `q` measures `1/gamma-gamma-Delta_gamma` in the primordial sector.

If the same-realization map is valid, the comparison reconstructs `Delta_gamma` at the relevant matched scale.

With a theoretically frozen RG trajectory, this can test whether

`Delta_gamma(mu_obs)`

agrees with the integral of `beta_Delta` from the microscopic/matching scale.

This creates a complete conceptual chain:

`microscopic EPRL gamma`
`-> area-metric gamma RG`
`-> beta_Delta / matching`
`-> low-energy birefringence gamma`
`+ primordial q`
`-> observed Delta_gamma consistency test`.

The chain is not yet authorized because its first same-realization arrows remain unproven.

## Why this does not yet close CW2-02

Three blockers remain.

### 1. Parameter identity

No audited authority yet proves

`gamma_micro = mapped gamma_AM(k) = gamma_EFT`

in one frozen realization.

Without this, combining `psi` and `q` would be a Frankenstein observable.

### 2. Scale matching

The primordial and detector-facing area-metric observables generally probe different physical scales/epochs. A frozen RG trajectory is needed to evolve gamma and Delta between them.

The correct comparison is not automatically `gamma_primordial = gamma_detector`; it is the relation predicted by the same `beta_gamma` and matching law.

### 3. Practical signal strength

The 2026 area-metric GW analysis finds the birefringence signal extremely weak for Planck-mass non-length modes. Therefore structural closure does not imply realistic near-term detectability.

This is a resource/sensitivity issue, not a structural-identifiability failure.

## New minimum experimental/theory object

The active O-LQG bridge is refined to

`SAME_REALIZATION_MULTISCALE_GAMMA_CLOSURE`.

Required payload:

1. `gamma_micro -> gamma_AM(mu)` matching law;
2. same-realization map from area-metric parity couplings into the gamma-dual EFT parameter;
3. `beta_gamma` and `beta_Delta` with uncertainty;
4. scale transport between primordial and low-energy area-metric observables;
5. observable relations `q` and `psi` with nuisance models;
6. no independent refit of gamma per sector.

If these are supplied, the combined fingerprint has a direct falsifiability statistic

`Delta_gamma = 2 cot(8 psi) - q`

(after RG transport to a common scale).

## Executable control

Reference fixture:

`code/lqg_area_metric_birefringence_gamma_identifiability_reference.py`.

It verifies:

- exact `gamma <-> psi` roundtrip on the positive branch;
- `gamma = -cot(4 psi)`;
- `dpsi/dgamma = 1/[4(1+gamma^2)]`;
- full-rank `(q,psi)` Jacobian;
- exact `Delta_gamma = 2 cot(8 psi) - q` reconstruction;
- large-gamma conditioning degradation without loss of structural rank at finite gamma.

## Status after Iter176

CW2-02 remains **OPEN**, but the observable closure route is materially stronger.

Updated classification:

`PROMISING_ADAPT_EXISTING__AREA_METRIC_BIREFRINGENCE_SUPPLIES_INDEPENDENT_GAMMA_HOLDOUT__SAME_REALIZATION_MULTISCALE_MAP_MISSING`.

No R1/R2/R3/R4 score change. Closure Wave 02 remains `0/3` because same-realization composition and RG transport are still open.

Heavy computation remains idle. The next decisive work is to establish the EPRL -> area-metric parameter/scale map; only then would a detector/resource forecast become scientifically meaningful.
