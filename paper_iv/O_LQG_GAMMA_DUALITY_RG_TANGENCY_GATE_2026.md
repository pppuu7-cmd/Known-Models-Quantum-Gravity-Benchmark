# O-LQG γ-Duality RG Tangency Gate — 2026-09-10

**KMQGB iteration:** 175  
**RQIR standard:** Core v1.0 FROZEN  
**CW2 object:** CW2-02 / O-LQG

> Provenance note: this audit first landed during a concurrent Iter174 write. Canonical chronology keeps the independently completed area-metric bridge audit as Iter174 and assigns this RG-tangency result to Iter175.

## Question

Can exact microscopic EPRL gamma-duality be promoted to the renormalized EFT relation merely because the microscopic theory has the duality and a running Immirzi parameter exists in a spin-foam-motivated effective programme?

**No.** The renormalization-group vector field must preserve the gamma-dual matching surface.

## Why Iter174 changes the question

Iter174 identified a concrete area-metric programme with

- a spin-foam-motivated RG flow for the Immirzi parameter;
- left/right non-length sectors whose mismatch controls parity violation;
- a Lorentzian area-metric GW/birefringence observable in which the Barbero-Immirzi parameter is in principle measurable.

The 2025 area-metric RG analysis extracts `beta_gamma`, while public technical material writes the inverse-Immirzi flow in terms of the chiral couplings schematically as

`gamma^{-1} ~ alpha_+^2 - alpha_-^2`,

`beta_{gamma^{-1}} ~ alpha_+ beta_{alpha_+} - alpha_- beta_{alpha_-}`,

with the gamma flow freezing when the non-length sector decouples in the stated limit.

This is a material advance: a running parity parameter is no longer hypothetical.

But CW2-02 needs more than `beta_gamma`. It needs to know whether the **observable gamma-duality coefficient relation** is preserved by that same coarse-graining trajectory.

## Literature constraint

The wider first-order/Holst renormalization literature does not provide a generic nonrenormalization theorem for the Immirzi parameter. Functional-RG analyses treat it as a running coupling, and perturbative first-order gravity with fermions exhibits explicit radiative renormalization of the Immirzi parameter.

A separate Einstein-Cartan/Holst flow study also identifies a small/large-Immirzi coordinate duality related to `gamma <-> 1/gamma` in a restricted setting. This is useful structural evidence, but it is not itself the EPRL gamma-dual GB/CS Wilson-coefficient matching theorem required by CW2-02.

Therefore KMQGB must test preservation of the **full matching relation**, not only a symmetry or beta function of gamma itself.

## Renormalized matching surface

Define

`rho = 2 f_GB^ren / f_CS^ren`,

`h(gamma) = gamma - 1/gamma`,

and

`Delta_gamma = rho - h(gamma)`.

The ideal gamma-dual relation is the codimension-one surface

`Delta_gamma = 0`.

Let RG time be `t=ln(mu)` and define

`beta_gamma = d gamma/dt`,

`beta_rho = d rho/dt`.

Then exactly

`beta_Delta = beta_rho - (1 + 1/gamma^2) beta_gamma`.

Hence the gamma-dual surface is RG invariant **if and only if**

`beta_Delta |_(Delta=0) = 0`.

This is the required tangency condition.

## Wilson-coefficient form

Let

`beta_GB = d f_GB/dt`,

`beta_CS = d f_CS/dt`.

For nonzero `f_CS`,

`beta_rho = 2 (beta_GB f_CS - f_GB beta_CS)/f_CS^2`.

Therefore the exact tangency test is

`2 (beta_GB f_CS - f_GB beta_CS)/f_CS^2 = (1+1/gamma^2) beta_gamma`

on the gamma-dual surface.

If both Wilson coefficients admit multiplicative flows

`beta_GB = eta_GB f_GB`,

`beta_CS = eta_CS f_CS`,

then for `gamma^2 != 1`, using `rho=h(gamma)`, the gate becomes

`(gamma - 1/gamma)(eta_GB-eta_CS) = (1+1/gamma^2) beta_gamma`.

Equivalently,

`eta_GB-eta_CS = [(gamma^2+1)/(gamma(gamma^2-1))] beta_gamma`.

Thus a running gamma generally requires **different matched running** of the parity-even and parity-odd Wilson sectors.

## Immediate consequences

### 1. Constant gamma is a special case

If

`beta_gamma = 0`,

then away from `gamma^2=1`, gamma-duality is preserved by multiplicative flows if

`eta_GB = eta_CS`.

The coefficients may run, but their ratio stays fixed.

### 2. Running gamma destroys the relation unless the ratio runs in lockstep

If

`beta_gamma != 0`

while

`eta_GB = eta_CS`,

then

`beta_Delta = -(1+1/gamma^2) beta_gamma != 0`.

Therefore common anomalous scaling of GB and CS does **not** protect gamma-duality when gamma itself runs.

### 3. Area-metric decoupling supplies one potentially simple boundary regime

The area-metric RG programme reports that the inverse-Immirzi flow freezes when the non-length modes decouple in its stated limit. If a same-realization EPRL-to-area-metric map eventually establishes that this gamma is the gamma entering the parity-sector Wilson relation, then the low-energy boundary condition may approach

`beta_gamma -> 0`.

In that regime the remaining tangency test simplifies to

`beta_rho -> 0`

or, in the multiplicative case,

`eta_GB -> eta_CS`.

This is not yet a closure result because the GB/CS projection has not been derived from the area-metric realization, but it provides a concrete IR matching target rather than an abstract one.

### 4. The point gamma=1 needs the direct gate

At positive `gamma=1`,

`h(1)=0`.

For finite nonzero `f_CS`, the ideal relation gives `f_GB=0`, so the multiplicative `eta_GB` form is singular. The direct tangency equation gives

`2 beta_GB/f_CS = 2 beta_gamma`,

or

`beta_GB/f_CS = beta_gamma`.

This is especially relevant because perturbative first-order gravity has identified `gamma^2=1` as a special fixed-point value in specific Euclidean matter-coupled settings. That literature does not establish the EPRL-to-EFT matching but shows why the direct gate cannot be omitted.

## Small/large-gamma duality is necessary-looking but insufficient

The ideal relation is algebraically equivariant under

`gamma -> 1/gamma`,

`rho -> -rho`,

because

`h(1/gamma) = -h(gamma)`.

This is compatible with small/large-Immirzi structures found in first-order RG studies.

However, algebraic equivariance of the constraint is weaker than dynamical preservation. The RG vector field must also transform covariantly and remain tangent to `Delta_gamma=0`.

Thus KMQGB distinguishes:

- **constraint duality:** `rho=h(gamma)` maps to itself under the involution;
- **RG duality:** beta functions transform covariantly under the involution;
- **matching preservation:** `beta_Delta=0` on the physical constraint surface.

Only the third condition directly closes the renormalized gamma-duality requirement.

## Updated interpretation of Delta_gamma

Iter173 showed that an unknown `Delta_gamma` is structurally degenerate with `gamma_EFT` in primordial observables.

Iter175 now identifies its RG source:

`Delta_gamma(mu) = Delta_gamma(mu0) + integral[beta_Delta dt]`.

Therefore the key theory task is no longer simply to ask whether gamma runs. It is to calculate or constrain

`beta_Delta`.

A running `gamma` is fully compatible with the observable gamma-dual fingerprint **if** the relevant parity-sector ratio runs exactly so that `beta_Delta=0`.

Conversely, even a modest mismatch in relative parity-sector running generates a physical duality-breaking residual that must enter the RQIR fingerprint.

## Sharpened closure object

The Iter174 area-metric bridge and the Iter173 identifiability object combine into

`RG_COVARIANT_EPRL_TO_AREA_METRIC_GAMMA_MATCH`.

Required payload:

1. `gamma_micro -> gamma_AM(k) -> gamma_EFT` same-realization map;
2. area-metric chiral-coupling flow defining `beta_gamma`;
3. projection of the same realization into `f_GB^ren` and `f_CS^ren`, or an equivalent frozen RQIR parity basis;
4. `beta_rho` and therefore `beta_Delta`;
5. boundary/matching condition for `Delta_gamma`;
6. propagated state/regulator/truncation uncertainty.

Strong closure:

`beta_Delta = 0` along the physical matching trajectory, plus a derived gamma identity/running map.

Allowed nonzero-breaking closure:

`beta_Delta != 0` but calculable, with `Delta_gamma(mu)` predicted from a frozen boundary/matching condition and propagated to the geometry/cosmology/area-metric fingerprint without independent refitting.

## What current literature does and does not establish

Current authority establishes that:

- gamma running is a real possibility rather than a bookkeeping fiction;
- area-metric gravity now provides an explicit spin-foam-motivated running gamma and Lorentzian observable parity sector;
- the inverse-Immirzi flow is controlled by chiral-sector imbalance and freezes in the reported decoupling limit;
- no generic nonrenormalization assumption is justified.

It does **not** yet establish the same-realization projection from that area-metric flow into the Bianchi-Rincon-Ramirez gamma-dual GB/CS coefficient ratio. Therefore `beta_Delta` remains unknown.

## Executable control

Reference fixture:

`code/lqg_gamma_duality_rg_tangency_reference.py`.

It verifies:

- `h(1/gamma)=-h(gamma)`;
- exact RG tangency condition;
- required relative Wilson running for nonzero `beta_gamma`;
- negative control: equal GB/CS anomalous scaling fails when gamma runs;
- fixed-gamma common-scaling preservation;
- the special direct gate at `gamma=1`.

## Status after Iter175

CW2-02 remains **OPEN**.

Updated classification:

`PROMISING_ADAPT_EXISTING__AREA_METRIC_GAMMA_FLOW_EXISTS__GAMMA_DUALITY_REDUCED_TO_SAME_REALIZATION_RG_TANGENCY__BETA_DELTA_MISSING`.

The active analytic target is now extremely specific:

**derive or bound `beta_Delta` after mapping the same EPRL realization into the area-metric parity flow.**

Heavy detector computation remains idle because no numerical likelihood can substitute for this missing RG-attribution object.
