# External RQIR Iter590 Cross-Check — Local MSSC K3 Hard-Channel Analyticity

**Repository firewall:** this file is KMQGB-only. External RQIR remains read-only.  
**Authority:** independent methodology/algebra pre-check only; it does **not** promote RQIR Iter591 or replace raw RQIR authority.

## External authority being checked

RQIR Iteration 590 established that the complete third mixed inverse-kernel response contains

`-G K3 G + six(K1/K2) - six(K1^3)`

and that the `K3` and `K1^3` families have nonzero same-parent support on the frozen fixture.

The exact RQIR next gate asks whether the **local K3 contact itself** has nonzero hard-channel discontinuity under

`D_s = Disc_s/(2 pi i)`.

## Parent action structure

The frozen MSSC source parent is local and minimally coupled:

`S_phi = -1/2 int sqrt(-g) [g^(mu nu) partial_mu phi partial_nu phi + m^2 phi^2]`,

with `g=eta+kappa h`.

The inverse source kernel has the local form

`K[g] = -p'_mu [sqrt(-g) g^(-1)]^(mu nu) p_nu + m^2 sqrt(-g)`.

There are no internal propagators or nonlocal form factors inside `K[g]` itself.

## Cubic local expansion

Let `H=eta^(-1)h`, `t_n=Tr(H^n)`.

The determinant expansion is

`sqrt(-g) = 1 + kappa s1 + kappa^2 s2 + kappa^3 s3 + ...`,

with

`s1 = t1/2`,

`s2 = t1^2/8 - t2/4`,

`s3 = t1^3/48 - t1 t2/8 + t3/6`.

The inverse metric is the geometric series

`g^(-1)=eta^(-1) - kappa eta^(-1)h eta^(-1) + kappa^2 eta^(-1)h eta^(-1)h eta^(-1) - kappa^3 eta^(-1)h eta^(-1)h eta^(-1)h eta^(-1)+...`.

Therefore the cubic coefficient of the densitized inverse metric is an algebraic local polynomial built from

- `h^3` matrix products;
- `s1 h^2`;
- `s2 h`;
- `s3 eta^(-1)`.

After polarization in three perturbations `h1,h2,h3`, the mixed `K3(h1,h2,h3)` is still a finite local polynomial in the external momenta and metric perturbations.

## Hard-channel origin conclusion — scoped

A finite local polynomial contact with no internal propagator and no nonanalytic form factor has no dynamical branch cut in the hard Mandelstam/source invariant.

Thus, in the frozen local MSSC source theory and absent a nonanalyticity introduced solely by a coordinate/polarization parameterization,

`Disc_s K3 = 0`

and therefore

`D_s K3 = 0`.

The important distinction is

`K3 != 0` **does not imply** `D_s K3 != 0`.

This is an **origin classification**, not a claim that the full `-G K3 G` contribution to a composite response can simply be deleted before the complete observable/Ward analysis. Propagators surrounding a local insertion may belong to a larger term whose analytic structure must be classified according to the frozen observable definition.

## Required RQIR-side proof still missing here

This pre-check does not know every frozen RQIR convention/fixture dependency. External RQIR should still explicitly verify in its own authority chain that

1. the exact polarized `K3` used at Iter590 contains no hidden nonlocal coefficient;
2. the frozen hard-channel continuation does not assign an artificial branch to a kinematic square-root parameterization;
3. `D_s` acts on the intended local K3 object, not on a larger `G K3 G` composite;
4. the result is consistent with the frozen source/Ward routing.

Only that same-protocol proof can become RQIR scientific authority.

## Reusable Candidate Gravity lesson

For every future KG contact vertex, separate

`nonzero local coefficient`

from

`nonzero channel discontinuity`.

A local analytic contact may be essential for Ward/contact completeness while contributing zero standalone branch discontinuity. This origin distinction must be made **after complete response generation and before comparator subtraction**.
