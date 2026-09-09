# O-LQG γ-Duality RG Tangency Gate — 2026-09-10

**KMQGB iteration:** 174  
**RQIR standard:** Core v1.0 FROZEN  
**CW2 object:** CW2-02 / O-LQG

## Question

Can exact microscopic EPRL gamma-duality be promoted to the renormalized EFT relation merely because the microscopic theory has the duality and the Immirzi parameter is the same named coupling?

**No.** The renormalization-group vector field must preserve the gamma-dual matching surface.

## Literature constraint

The existing first-order/Holst renormalization literature does not provide a general nonrenormalization theorem for the Immirzi parameter. Functional-RG analyses treat it as a running coupling, and perturbative first-order gravity with fermions exhibits explicit radiative renormalization of the Immirzi parameter.

Separately, an Einstein-Cartan/Holst flow study identifies a small/large-Immirzi coordinate duality related to `gamma <-> 1/gamma` in a restricted setting. This is useful structural evidence, but it is not itself the EPRL gamma-dual GB/CS Wilson-coefficient matching theorem required by CW2-02.

Therefore KMQGB must test preservation of the **full matching relation**, not only a symmetry of the gamma beta function.

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

That is, the two coefficients may run, but their ratio must remain fixed.

### 2. Running gamma destroys the relation unless the ratio runs in lockstep

If

`beta_gamma != 0`

while

`eta_GB = eta_CS`,

then

`beta_Delta = -(1+1/gamma^2) beta_gamma != 0`.

Therefore common anomalous scaling of GB and CS does **not** protect gamma-duality when gamma itself runs.

### 3. The point gamma=1 needs the direct gate

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

This is compatible with the existence of small/large-Immirzi duality structures in first-order RG studies.

However, algebraic equivariance of the constraint is weaker than dynamical preservation. The RG vector field must also transform covariantly and remain tangent to `Delta_gamma=0`.

Thus KMQGB distinguishes:

- **constraint duality:** `rho=h(gamma)` is mapped to itself under the involution;
- **RG duality:** beta functions transform covariantly under the involution;
- **matching preservation:** `beta_Delta=0` on the constraint surface.

Only the third condition directly closes the renormalized gamma-duality requirement.

## Updated interpretation of Delta_gamma

Iter173 showed that an unknown `Delta_gamma` is structurally degenerate with `gamma_EFT` in primordial observables.

Iter174 now identifies its first-principles RG source:

`Delta_gamma(mu) = integral beta_Delta dt + matching constant`.

Therefore the key theory task is no longer simply to ask whether gamma runs. It is to calculate or constrain

`beta_Delta`.

A running `gamma` is fully compatible with the observable gamma-dual fingerprint **if** the GB/CS ratio runs exactly so that `beta_Delta=0`.

Conversely, even a seemingly modest mismatch in the relative Wilson running generates a physical duality-breaking residual that must enter the RQIR fingerprint.

## Sharpened closure object

The Iter173 object

`IDENTIFIABLE_RENORMALIZED_GAMMA_MATCH`

is now refined to require an RG certificate:

`RG_COVARIANT_GAMMA_MATCH = {gamma_micro->gamma_EFT, beta_gamma, beta_rho or beta_GB/beta_CS, beta_Delta, matching uncertainty}`.

Strong closure:

`beta_Delta = 0` along the physical matching trajectory, plus a derived gamma identity/running map.

Allowed nonzero-breaking closure:

`beta_Delta != 0` but calculable, with `Delta_gamma(mu)` predicted from a frozen boundary/matching condition and propagated to the geometry/cosmology fingerprint without independent refitting.

## What current literature does and does not establish

Current first-order RG literature establishes that:

- treating gamma as scale dependent is scientifically legitimate;
- no generic nonrenormalization principle can simply be assumed;
- explicit gamma running can occur;
- small/large-gamma beta-function duality structures can arise in restricted truncations.

It does **not** establish the same-realization EPRL/coarse-grained flow of `f_GB^ren` and `f_CS^ren`, so it cannot supply `beta_Delta` for CW2-02.

Therefore these results are comparator/constraint authority, not a composable closure certificate.

## Executable control

Reference fixture:

`code/lqg_gamma_duality_rg_tangency_reference.py`.

It verifies:

- `h(1/gamma)=-h(gamma)`;
- exact RG tangency condition;
- required relative Wilson running for nonzero `beta_gamma`;
- the negative control that equal GB/CS anomalous scaling fails when gamma runs;
- fixed-gamma common-scaling preservation;
- the special direct gate at `gamma=1`.

## Status after Iter174

CW2-02 remains **OPEN**.

Updated classification:

`PROMISING_ADAPT_EXISTING__RENORMALIZED_GAMMA_DUALITY_REDUCED_TO_RG_TANGENCY__SAME_REALIZATION_BETA_DELTA_MISSING`.

The active analytic target is now extremely specific:

**derive or bound `beta_Delta` from the same coarse-grained EPRL realization.**

Heavy detector computation remains idle because no numerical likelihood can substitute for this missing RG-attribution object.
