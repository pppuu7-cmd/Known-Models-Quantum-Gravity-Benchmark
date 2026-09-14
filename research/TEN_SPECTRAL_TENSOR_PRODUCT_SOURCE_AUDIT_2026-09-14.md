# Ten-spectral source audit — tensor product versus correlated group kernel

Date: 2026-09-14
Status: SOURCE/MATHEMATICAL AUDIT ONLY; NO D7-S2 PROMOTION

## 1. Primary-source object
The primary causal-vertex paper is Bianchi–Chen–Gamonal, arXiv:2601.23162.

Its Eq.(3) defines one Toller matrix by

`T^(±,rho,k)(g) = lim_{eps->0+} int_R [d rhot/(2*pi*i)] [±1/(rhot-rho∓i eps)] P_jl(rhot;rho) D^(rhot,k)(g)`

with

`P_jl(rhot;rho) = Gamma(-j-i rho) Gamma(l-i rhot+1) / [Gamma(-j-i rhot) Gamma(l-i rho+1)]`.

Eq.(4) defines the causal vertex as a product of ten wedge Toller factors inside four unfixed `SL(2,C)` group integrations after `g1=1`.

The companion paper arXiv:2604.24945 makes the one-wedge status sharper:
- its Eqs.(17)-(20) define the Feynman functional `I_eps^(±)` and prove that `lim eps->0+ I_eps^(±)` projects the Wigner matrix onto the unique Toller branch;
- the proof is one-variable contour/residue analysis;
- Eq.(13) restores full Toller matrices from reduced matrices by compact KAK factors;
- Eq.(14) explicitly states that Toller matrices are **not** Lorentz-group representations;
- Eqs.(12)/(15) give the additive relation `T+ + T- = D`.

Iter468 already pins the formal direct-substitution shape:
- ten independent wedge spectral variables;
- ten local spectral weights;
- one common four-group kernel depending on all ten spectral labels;
- no shared spectral variable, no artificial spectral delta.

Iter468 authority: run `34770144171`, aggregate artifact `10322025879`, digest `sha256:f45fe3012ed14fa4449554e9cd87edbedbe81a551a694d349adae2211a61a5ff`, classification `ITER468_EQ4_SOURCE_SPECTRAL_GROUP_CONTRACTION_OBJECT_PINNED_SCOPED`.

## 2. What is and is not ambiguous about ten spectral boundary values
For each wedge `e`, define the one-variable regulated distribution

`u_{e,eps}(x_e) = kappa_e/(x_e-rho_e-kappa_e i eps)`

including the smooth/meromorphic Toller kernel factor where appropriate. The ten variables `x_e` are independent coordinates of `R^10`.

### Established mathematical fact: separate-variable tensor products exist
Distributions on different factors always admit a tensor product. Therefore once the one-wedge limits

`u_{e,eps} -> u_e` in `D'(R)`

exist, the ten-fold object

`U = u_1 tensor ... tensor u_10`

is a well-defined distribution on `R^10` before it is composed/paird with the correlated group kernel.

Moreover, a common diagonal regulator path is not intrinsically a new distributional ambiguity at this separate-variable level. For a finite product, if every one-variable family converges in `D'(R)`, then for any path with every `eps_e -> 0+`,

`u_{1,eps_1} tensor ... tensor u_{10,eps_10} -> u_1 tensor ... tensor u_10`

in `D'(R^10)`.

Reason: convergent families in `D'` are bounded; the tensor-product map is hypocontinuous. For two factors,

`u_eps tensor v_eta - u tensor v = (u_eps-u) tensor v_eta + u tensor (v_eta-v)`,

and each term tends to zero because the other family is bounded. Finite induction gives the ten-factor statement.

Thus **the mere use of ten independent Feynman boundary values does not require choosing an iterated order**. A common epsilon and independent epsilons have the same tensor-product limit at the level of the separate spectral variables, provided the one-wedge distributional limits are the source-defined ones.

This observation does NOT justify any exchange with the group integrations.

## 3. The actual unresolved object
After direct substitution, the formal amplitude has the shape

`< U , C >`

where

`C({rhot_e}) = int prod_{a=2}^5 dg_a prod_e D_e^(rhot_e,k_e)(g_b^-1 g_a)`

with boundary magnetic/intertwiner contractions understood.

The unresolved question is whether this correlated kernel `C` is an admissible test function or multiplier for `U`, or whether the joint group/spectral object admits a source-defined extension when singular group configurations are included.

The cited source papers do **not** establish:
1. absolute convergence of the four-group integral defining `C` after causal branch selection;
2. sufficient decay/growth bounds in all ten real spectral variables to pair `C` directly with `U`;
3. Fubini/Tonelli conditions allowing the ten spectral integrals to be moved through the four group integrations;
4. a wavefront/transversality theorem for the pullback/product at shared group-collision loci;
5. equality of an iterated numerical quadrature/finite-part prescription with the source-defined distributional amplitude;
6. finiteness or divergence of the physical fully contracted causal vertex.

The causal-vertex paper explicitly says the finiteness question of the new causal model must be reinvestigated because of Toller poles. The existing benchmark collision/Haar streams address pieces of this problem but do not yet prove the required joint distributional statement.

## 4. Consequence for future spectral work
Do **not** spend a future gate choosing an arbitrary order among the ten independent spectral variables: there is no source or mathematical reason to privilege such an order at the separate-variable tensor-product level.

The next decisive spectral/distributional gate should instead test one of the following equivalent bottlenecks on a fully specified source-backed local object:
- whether the correlated group kernel belongs to a function/distribution class on which the ten-fold Toller boundary-value tensor product acts continuously;
- or whether a microlocal pullback/product criterion is satisfied away from, and then across, the K5 collision strata;
- or produce a fully contracted source-faithful counterexample showing regulator/path dependence that survives the group/spinor/intertwiner contractions.

Iter461 collision partitions are an independent queued stream and must be consumed rather than duplicated before selecting a collision-stratum theorem.

## 5. Claim guards
This audit does not prove the physical causal vertex exists, is finite, diverges, is independent of all regularizations, or closes D7-S2. It only removes a false subproblem: the ten one-variable Feynman boundary values do not require an arbitrary iterated spectral order merely because there are ten of them. The hard problem is their action on the correlated group kernel / collision geometry.
