# Paper IV — LQG / area-metric equation attribution audit v0.1

Date: 2026-09-11
Purpose: separate direct external physics relations from KMQGB definitions and algebraic consequences before the LQG case study is frozen for CQG.
Status: FIRST ATTRIBUTION PASS / SAFE FOR v1.1 WITH THE QUALIFIERS BELOW

## 1. External source layer

### E1 — Bianchi & Rincon-Ramirez gamma-duality

Eugenio Bianchi and Monica Rincon-Ramirez, **Spinfoams, gamma-duality, and parity violation in primordial gravitational waves**, *Physical Review D* **113**, 124013 (2026), DOI `10.1103/qz89-26hk`, arXiv:`2403.06053`.

The published/arXiv article directly supplies, within its gamma-dual effective-action construction:

`2 f_GB(phi) / f_CS(phi) = gamma - 1/gamma`

and, for its slow-roll inflation model,

`1/gamma - gamma = (pi/8) (r + 8 n_T) / Pi`.

The paper also explicitly states that a top-down derivation of the effective action from the non-perturbative spinfoam dynamics is still missing. This limitation is essential to the KMQGB same-realization status.

Define for bookkeeping

`rho := 2 f_GB/f_CS`

and

`q := (pi/8)(r+8 n_T)/Pi`.

On the **ideal externally stated gamma-dual relation**,

`rho = gamma - 1/gamma`

and

`q = 1/gamma - gamma`,

so

`q = -rho`.

This sign relation is not an additional physical assumption; it is the direct algebraic consequence of the two externally stated ideal relations.

### E2 — area-metric Immirzi / birefringence relations

Bianca Dittrich, **Gravitational wave signatures from area metric gravity**, arXiv:`2608.16046` (2026).

The article gives, in the shift-symmetric Lorentzian area-metric realization,

`sinh(2 xi) = 1/gamma`

and the birefringence-axis rotation

`psi = -(1/2) arctan(tanh xi)`.

The paper states that the Barbero-Immirzi parameter can be identified with the parity-violating area-metric parameter in the construction and develops an observable optical birefringence channel. It also stresses the small signal expected for Planck-mass non-length modes.

### E3 — area-metric continuum / RG adjacent authority

Bianca Dittrich and Athanasios Kogios, **From spin foams to area metric dynamics to gravitons**, *Classical and Quantum Gravity* **40**, 095011 (2023), DOI `10.1088/1361-6382/acc5d9`, arXiv:`2203.02409`, establishes a perturbative continuum result for effective spin-foam/Area-Regge dynamics with leading GR graviton dynamics and area-metric corrections.

Johanna Borissova, Bianca Dittrich, Astrid Eichhorn and Marc Schiffer, **Renormalization group flows in area-metric gravity**, arXiv:`2507.02034` (2025), supplies an area-metric RG analysis motivated by spin foams and extracts an RG flow for the Immirzi parameter.

These are **adjacent continuum/RG authorities**. They do not by themselves prove that the microscopic EPRL realization, the area-metric flow and the Bianchi–Rincon-Ramirez inflationary EFT are one physical realization.

## 2. Equation-by-equation status

### A. `q = 1/gamma - gamma - Delta_gamma`

**Status:** `KMQGB_GENERALIZED_RESIDUAL_DEFINITION`, built around an externally established ideal relation.

External source E1 directly gives the ideal relation

`q = 1/gamma - gamma`

for the chosen gamma-dual inflation model.

KMQGB introduces `Delta_gamma` as a duality-breaking/matching residual and generalizes the ideal observable relation to

`q = 1/gamma - gamma - Delta_gamma`.

This generalized off-surface equation must therefore **not** be attributed verbatim to Bianchi & Rincon-Ramirez. The article should say that KMQGB defines the residual so that `Delta_gamma=0` recovers the source relation.

### B. `Delta_gamma = rho - (gamma - 1/gamma)`

with `rho = 2 f_GB/f_CS`.

**Status:** `KMQGB_GENERALIZED_RESIDUAL_DEFINITION`, anchored to external E1.

External E1 gives the ideal surface

`rho = gamma - 1/gamma`.

KMQGB promotes departure from that surface to the residual coordinate

`Delta_gamma := rho - (gamma - 1/gamma)`.

Combining this definition with A gives

`q = -rho`

identically for the common KMQGB residual convention. Consequently

`beta_q = - beta_rho`.

This identity should be stated explicitly in v1.1 because the earlier manuscript displayed gamma-space and observable-space beta equations without making the sign bridge visible.

### C. `beta_Delta = beta_rho - (1 + 1/gamma^2) beta_gamma`

**Status:** `KMQGB_ALGEBRAIC_IDENTITY`.

It follows exactly by differentiating

`Delta_gamma = rho - gamma + 1/gamma`

with respect to RG time `t=ln(mu)`.

No external source should be cited as if it published this KMQGB residual equation. External RG references instead motivate that `gamma` can run and supply adjacent beta-function information.

Using `beta_q=-beta_rho`, C is equivalent to

`beta_Delta = -(1 + 1/gamma^2) beta_gamma - beta_q`.

Therefore the apparent sign difference between the Iter175 and Iter177 forms is resolved.

### D. `gamma = -cot(4 psi)`

**Status:** `KMQGB_DERIVED_FROM_EXTERNAL_AREA_METRIC_RELATIONS`.

External E2 gives

`sinh(2 xi)=1/gamma`

and

`psi=-(1/2) arctan(tanh xi)`.

Let `y=tanh xi`. Then `tan(2 psi)=-y` and

`tan(4 psi) = -2y/(1-y^2) = -sinh(2 xi) = -1/gamma`.

Hence, on the positive-gamma branch used in the adapter,

`gamma = -cot(4 psi)`.

This compact inverse relation is a KMQGB algebraic reduction of the source equations, not a formula that should be presented as a direct quote from E2 unless a future source check finds it explicitly written there.

### E. `1/gamma - gamma = 2 cot(8 psi)`

**Status:** `KMQGB_TRIGONOMETRIC_IDENTITY_FROM_D`.

From D, `1/gamma=-tan(4 psi)` and `gamma=-cot(4 psi)`, therefore

`1/gamma-gamma = cot(4 psi)-tan(4 psi) = 2 cot(8 psi)`.

### F. `Delta_gamma = 2 cot(8 psi) - q`

**Status:** `KMQGB_ALGEBRAIC_IDENTITY`.

This follows from A and E after transporting `q` and `psi` to a common scale in the **same physical realization**.

The same-realization qualification is mandatory. Without the missing EPRL → area-metric → EFT parameter/provenance map, the formula is an adapter-level conditional relation, not an experimentally established cross-framework identity.

### G. `beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q`

**Status:** `KMQGB_ALGEBRAIC_IDENTITY`.

Differentiate F with respect to `t=ln(mu)`:

`d[2 cot(8 psi)]/dt = -16 csc^2(8 psi) beta_psi`.

Thus

`beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q`.

### H. `beta_psi = beta_gamma/[4(1+gamma^2)]`

**Status:** `KMQGB_DIFFERENTIAL_IDENTITY_FROM_D`.

Differentiating the positive-branch inverse relation gives

`d psi/d gamma = 1/[4(1+gamma^2)]`.

This makes G exactly equivalent to C after `beta_q=-beta_rho` is used.

## 3. Consistency certificate

The two KMQGB representations are algebraically consistent:

Wilson/EFT residual coordinates:

`Delta_gamma = rho - (gamma - 1/gamma)`

`beta_Delta = beta_rho - (1+1/gamma^2) beta_gamma`.

Observable coordinates:

`Delta_gamma = 2 cot(8 psi) - q`

`beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q`.

The bridge identities are

`q=-rho`,

`beta_q=-beta_rho`,

`gamma=-cot(4 psi)`,

`beta_psi=beta_gamma/[4(1+gamma^2)]`.

Substitution maps either beta equation into the other exactly.

`LQG_EQUATION_INTERNAL_SIGN_CONSISTENCY = PASS`.

## 4. Attribution table for the manuscript

| Relation | Manuscript attribution |
|---|---|
| `2 f_GB/f_CS = gamma - 1/gamma` | direct external: Bianchi & Rincon-Ramirez |
| `q=(pi/8)(r+8n_T)/Pi = 1/gamma-gamma` on ideal gamma-dual model | direct external: Bianchi & Rincon-Ramirez |
| `sinh(2xi)=1/gamma` | direct external: Dittrich 2026 area-metric realization |
| `psi=-(1/2) arctan(tanh xi)` | direct external: Dittrich 2026 area-metric realization |
| `Delta_gamma := rho-(gamma-1/gamma)` | KMQGB residual definition |
| `q=1/gamma-gamma-Delta_gamma` | KMQGB generalized residual form of external ideal relation |
| `q=-rho` | KMQGB algebraic consequence under the common residual convention |
| `beta_Delta=beta_rho-(1+1/gamma^2)beta_gamma` | KMQGB derivative identity |
| `gamma=-cot(4psi)` | KMQGB reduction of Dittrich source relations |
| `Delta_gamma=2cot(8psi)-q` | KMQGB composite algebraic identity, conditional on same-realization/scale transport |
| `beta_Delta=-16csc^2(8psi)beta_psi-beta_q` | KMQGB derivative identity |

## 5. CQG wording required

Preferred wording:

> Bianchi and Rincon-Ramirez provide the ideal gamma-dual EFT relations linking the parity-even/parity-odd higher-curvature coefficient ratio and a primordial tensor observable combination to the Barbero-Immirzi parameter. KMQGB introduces a residual `Delta_gamma` measuring departure from the ideal matching surface. Independently, the Lorentzian area-metric construction relates the Immirzi parameter to a birefringence-axis angle through `sinh(2xi)=gamma^{-1}` and `psi=-(1/2)arctan(tanh xi)`. Eliminating `xi` gives the KMQGB adapter identity `gamma=-cot(4psi)`. These relations constrain a valid common realization but do not establish that the microscopic EPRL, area-metric RG and inflationary EFT objects share one physical ancestry.

Avoid wording such as:

- “Dittrich proves `gamma=-cot(4psi)`” unless the exact compact equation is found explicitly in the source;
- “Bianchi and Rincon-Ramirez derive `Delta_gamma`” — `Delta_gamma` is the KMQGB residual convention;
- “the equations prove the EPRL-to-area-metric-to-EFT bridge”;
- “gamma-duality is known to be preserved under RG”.

## 6. Remaining physical blocker

The equation layer is algebraically closed, but the physical composition layer is not. The missing object remains a same-realization certificate linking

`microscopic EPRL/spinfoam gamma`
`-> area-metric/refinement/RG gamma(mu)`
`-> EFT gamma / parity-sector coefficient ratio`
`-> common-scale normalized observables and error/comparator package`.

Therefore:

`EQUATION_ATTRIBUTION = CLEAN_FIRST_PASS`

`ALGEBRAIC_CONSISTENCY = PASS`

`SAME_REALIZATION_PHYSICAL_BRIDGE = OPEN`

`LQG_FAMILY_TERMINALITY = NOT_PROMOTED`
