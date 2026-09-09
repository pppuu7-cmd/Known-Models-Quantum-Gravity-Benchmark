# O-LQG Multiscale Observable-Space RG Transport Gate — 2026-09-10

**KMQGB iteration:** 177  
**RQIR standard:** Core v1.0 FROZEN  
**CW2 object:** CW2-02 / O-LQG

## Purpose

Convert the Iter175 Wilson/RG tangency condition and the Iter176 birefringence holdout into an observable-space transport relation that can eventually be tested without independently fitting gamma at each scale.

## Observable representation

On the positive-gamma area-metric branch,

`gamma = -cot(4 psi)`

and therefore

`1/gamma - gamma = 2 cot(8 psi)`.

The generalized gamma-duality relation becomes

`Delta_gamma = 2 cot(8 psi) - q`,

where

`q = (pi/8)(r+8 n_T)/Pi`.

This identity is understood only after `q` and `psi` are transported to a common renormalization/matching scale in one realization.

## RG transport equation

Let `t=ln(mu)` and define

`beta_psi = d psi/dt`,

`beta_q = d q/dt`.

Differentiating the observable residual gives exactly

**`beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q`**.

The area-metric angle/gamma relation also gives

`beta_psi = beta_gamma/[4(1+gamma^2)]`.

Substitution yields

`beta_Delta = -(1+1/gamma^2) beta_gamma - beta_q`,

which is the same transport content as differentiating

`q = 1/gamma - gamma - Delta_gamma`.

Thus Iter175 and Iter176 are mathematically consistent representations of the same matching problem.

## Ideal-duality observable tangency

If renormalized gamma-duality is exactly preserved,

`beta_Delta = 0`,

then the observable quantities must obey

**`beta_q + 16 csc^2(8 psi) beta_psi = 0`**.

This is the direct observable-space RG tangency condition.

It is stronger operationally than saying that the Immirzi parameter runs consistently: it prescribes how the primordial gamma-sensitive combination and the low-energy area-metric birefringence angle must co-evolve under the common theoretical scale transport.

## Nonzero duality breaking

If the parent dynamics predicts

`beta_Delta != 0`,

then the same equation becomes

`beta_q + 16 csc^2(8 psi) beta_psi = -beta_Delta`.

With a frozen matching value `Delta_gamma(mu0)`, integration predicts the observable mismatch at another scale:

`Delta_gamma(mu1) - Delta_gamma(mu0) = integral beta_Delta dt`.

This is allowed by RQIR. What is forbidden is to fit an unrelated `Delta_gamma` or gamma independently in each representation.

## Negative control

A useful failure mode is immediate.

If `q` is held fixed while `psi` runs because gamma runs, then

`beta_q=0`, `beta_psi!=0`

implies

`beta_Delta != 0`.

Therefore one cannot combine a running low-energy gamma with a scale-independent primordial gamma-duality relation unless the derived matching flow justifies that approximation.

This directly guards against a common cross-scale composition error.

## Relation to same-realization closure

This observable transport equation does **not** remove the need for the microscopic EPRL -> area-metric matching theorem. It becomes authorized only after the following are fixed:

1. one common realization vector;
2. a common scale convention and RG trajectory;
3. `gamma_micro -> gamma_AM(mu) -> gamma_EFT(mu)`;
4. the parity-sector projection that determines `beta_Delta`;
5. definitions of the scales at which primordial `q` and detector-facing `psi` are evaluated.

Once those are supplied, the theory can be expressed directly in the observable coordinates `(q,psi)` rather than requiring gamma to be treated as an independently fitted latent parameter at each stage.

## New compact closure certificate

The strongest form of CW2-02 can now be represented as a three-part certificate:

`MULTISCALE_GAMMA_CERTIFICATE = {M_same-realization, T_RG, C_observable}`

where

- `M_same-realization` proves the EPRL -> area-metric parameter/provenance map;
- `T_RG` predicts `beta_Delta` and transports parameters between scales;
- `C_observable` verifies `Delta_gamma = 2 cot(8 psi) - q` and its RG transport law.

For exact duality,

`C_observable: beta_q + 16 csc^2(8 psi) beta_psi = 0`.

For controlled breaking,

`C_observable: beta_q + 16 csc^2(8 psi) beta_psi = -beta_Delta_predicted`.

This is a substantially narrower target than deriving a generic complete quantum-gravity EFT.

## Executable control

Reference fixture:

`code/lqg_multiscale_observable_rg_transport_reference.py`.

It verifies:

- `2 cot(8 psi)=1/gamma-gamma`;
- equality of observable-space and gamma-space `beta_Delta`;
- the ideal-duality observable tangency condition;
- the negative control in which `q` is frozen while gamma/psi runs;
- exact finite-endpoint reconstruction of `Delta_gamma`.

## Status after Iter177

CW2-02 remains **OPEN**.

Updated classification:

`PROMISING_ADAPT_EXISTING__MULTISCALE_GAMMA_FINGERPRINT_HAS_OBSERVABLE_RG_CLOSURE_EQUATION__SAME_REALIZATION_MAP_AND_BETA_DELTA_AUTHORITY_MISSING`.

The next decisive theoretical task is now precisely scoped: construct or find `M_same-realization` and derive `T_RG`; the observable closure equation is already fixed.

No R1/R2/R3/R4 score change. Closure Wave 02 remains `0/3`. Heavy detector compute remains idle until the same-realization map and RG transport authority are frozen.
