# Candidate Gravity Design Priors from KMQGB

**Purpose:** preserve benchmark-derived construction constraints for a future Candidate Gravity (KG) model without modifying external RQIR Candidate Gravity authority/readiness.  
**Authority rule:** this is design evidence, not a KG ansatz and not a readiness promotion.

## 1. Core lesson

A future KG model must not be built around one unusual qualitative effect. The benchmark repeatedly finds broader comparators that reproduce isolated features.

The preferred strategy is now:

> **one explicit parent dynamics with few shared parameters/functions, complete responses, exact physical constraints, and several cross-order/cross-attribution relations that remain outside the full comparator manifold.**

This is **rigidity by overconstraint**.

## 2. Features already proven insufficient by themselves

The following may occur inside a viable theory but are not standalone KG certificates:

- nonzero deviation from GR;
- Yukawa/scalar force or one linked scalar signature;
- metric noise, decoherence, positive two-point spectrum;
- non-Gaussianity or higher symmetrized cumulants;
- end-state entanglement;
- non-entanglement-breaking channel without mediator attribution;
- raw commutator/sideband asymmetry without detector attribution;
- indefinite causal order without geometry attribution;
- cross-detector spatial correlation geometry;
- bare metric/event superposition or localization before QRF/diffeomorphism quotient;
- UV softness, scale-free UV exponent, absence of extra poles, one pole tower;
- higher derivatives or finite EFT Wilson coefficients;
- KMS/FDR relation;
- higher graviton correlators by themselves;
- squeezed/excited graviton state;
- non-Markovian memory;
- parity/chirality;
- nonanalyticity/branch cuts/logs by themselves;
- a Newtonian-looking quantum mediator;
- ghost freedom/UV health as a full causality certificate;
- a finite-regulator nonperturbative state/correlation length;
- a single-order observable whose comparator tangent already saturates that observable space.

Each item has a concrete benchmark degeneracy, comparator identity, scoped counterexample, or methodology warning recorded in the wave/model files.

## 3. Mandatory parent decomposition

Never define novelty relative only to a Gaussian/tree truncation.

Use the bookkeeping form

`Gamma_parent = Gamma_C5,full_matched + DeltaGamma_KG`.

`DeltaGamma_KG` means only what remains after matching the largest applicable same-domain/same-order C5 nonlinear/loop/EFT/state/contact structure plus all other allowed comparators.

A qualitative label is never `DeltaGamma_KG` by itself.

## 4. Compact physical design objects

A useful future KG parent should generate, from the same dynamics, at least the linked structures

`K_rel={N_ij,C_ij,chi_R,causal support,proper-time geometry,QRF invariance}`

and

`G_attr={Theta_rel,Q_channel,helicity2/tidal response,kappa_soft,T_mn universality,Ward/contact,mediator nulls}`.

The target is not each component separately but a forced relation

`F(K_rel,G_attr,cross-order/higher supporting data)=0`

with low remaining freedom after comparator profiling.

## 5. Attribution stack

A KG-specific residual must survive every applicable layer:

1. **quantum attribution** — beyond positive classical stochastic/LOCC descriptions;
2. **mediator attribution** — exclude ordinary quantum matter/EM/optical/phononic/common-bath transfer and C6 source leakage;
3. **gravity attribution** — massless helicity-2/tensor response, universal stress-energy coupling, soft/Ward/contact and static–radiative linkage;
4. **locality attribution** — retarded support/microcausality/no-signalling or an explicitly justified controlled-nonlocal replacement;
5. **relational/QRF attribution** — physical clocks/worldlines/proper times/separations/dressed observables;
6. **geometry attribution** — causal/process claims must beat ordinary quantum-switch/control implementations;
7. **detector attribution** — full backaction/readout/noise calibration;
8. **state attribution** — distinguish new dynamics from thermal/squeezed/excited C5 states;
9. **regulator/continuum attribution** where applicable;
10. **full-C5 order matching**;
11. **rigidity/identifiability** after the joint quotient.

## 6. Same-parent response completeness

Authoritative protocol: `protocol/PARENT_KERNEL_RESPONSE_COMPLETENESS.md`.

For `G=K^-1` and mixed derivative label set `S`, the complete response is the ordered-set-partition sum

`D_S G = sum_k (-1)^k sum_(B1,...,Bk in OP(S,k)) G K_B1 G ... K_Bk G`.

Every ordered partition occurs once.

Term counts grow rapidly: `1,3,13,75,541` for response orders `1..5`.

Required order:

`complete same-parent response`

`-> origin/cut classification`

`-> Ward/contact/constraint physical reduction`

`-> matched observable`

`-> comparator/COR quotient`.

Never create a residual by comparing incomplete response families.

## 7. Comparator-orthogonal residual geometry

Authoritative protocol: `protocol/RESIDUAL_SPACE_GEOMETRY.md`.

After exact physical reduction, let residual `r`, covariance `Sigma`, and union comparator Jacobian `J_union` define

`A=Sigma^(-1/2)J_union`,

`Pi_perp=I-AA^+`,

`COR=Pi_perp Sigma^(-1/2)r`.

`COR=0` means exact local tangent degeneracy.

A nonzero COR is only a local prefilter; finite/global comparator-manifold profiling remains mandatory.

For a future KG Jacobian

`B_KG=Pi_perp Sigma^(-1/2)J_KG`.

Only robust nonzero singular directions of `B_KG` are locally identifiable after comparator profiling.

## 8. Optimal observable design

Authoritative protocol: `protocol/OPTIMAL_COMPARATOR_CONTRASTS.md`.

Exact comparator-null contrasts satisfy

`J_union^T w=0`.

For pre-registered signal direction `s`, a covariance-optimal local contrast has direction

`w_opt proportional to Sigma^(-1/2)Pi_perp Sigma^(-1/2)s`.

Adding `k` physical observables changes local complement dimension by

`Delta d_perp = k - Delta rank(J_union)`.

Therefore choose future KG observables by **post-comparator dimension, projected conditioning and projected SNR**, not raw sensitivity or novelty.

## 9. Cross-order rigidity

Authoritative protocol: `protocol/CROSS_ORDER_RIGIDITY.md`.

Stack multiple complete physical response blocks from the same parent dynamics:

`y_stack=col(y_1,...,y_L)`.

Shared parent parameters must remain shared across orders. Do not create independent per-order copies merely to improve comparator fits.

If `J_ell` are block Jacobians, define

`R_shared = sum_ell rank(J_ell) - rank(J_stack) >= 0`.

`R_shared>0` measures extra comparator-orthogonal consistency directions created by shared parameters.

When exact monomial scaling exists,

`c_i=A_i product_j theta_j^(P_ij)`,

vectors `u` with `u^T P=0` yield exact global nuisance-free invariants

`I_u=product_i(c_i/A_i)^(u_i)`.

A strong KG architecture should use **few shared parent parameters to predict many linked orders/channels** rather than introduce one fresh coefficient for every effect.

## 10. Gravity-attribution anchors that survived red-team

These are not KG novelty by themselves, but they help establish that a quantum mediator is gravitational:

- massless spin-2 soft universality;
- universal coupling to stress-energy/equivalence structure;
- tensor/tidal helicity-2 response;
- static + soft + radiative linkage;
- exact Ward/contact completion;
- relational causal ordered kernels.

Under the frozen locality/Lorentz/unitarity/single-massless-spin-2/IR assumptions, leading long-range spin-2 structure collapses to GR/C5. Treat this as the **gravity anchor**, not the new residual.

## 11. Candidate Gravity Promotion Gate

Authoritative checklist: `protocol/CANDIDATE_GRAVITY_PROMOTION_GATE.md`.

Short order:

`one parent dynamics`

`-> complete responses`

`-> exact physical constraints`

`-> common-domain comparator definition`

`-> attribution stack`

`-> full C5/C0-C6/C3b quotient`

`-> nonzero COR`

`-> global separation`

`-> projected identifiability/optimal observables`

`-> rigidity`

`-> only then ansatz promotion and later Fisher/resources`.

No current KMQGB result satisfies the full promotion chain for a concrete new KG ansatz.

## 12. Mandatory red-team order for any future KG idea

At minimum try to absorb the idea with:

1. C0 GR/calibration;
2. C1 semiclassical gravity;
3. C2 Gaussian stochastic gravity;
4. non-Gaussian stochastic hierarchy;
5. C3 measurement-feedback/classical channel;
6. C3b postquantum classical gravity;
7. nonlocal classical-CQ loopholes;
8. C4 ordinary quantum scalar/vector/matter/common bath;
9. C6 quantum source + classical interface;
10. scalar/Yukawa/scalar-tensor parents;
11. detector/backaction artifacts;
12. QRF/diffeomorphism redundancy;
13. ordinary quantum-switch controls;
14. field-redefinition/on-shell equivalence;
15. Gaussian C5 null subsector;
16. full applicable C5 nonlinear/loop/EFT/state/contact parent;
17. broader same-domain UV amplitudes;
18. spin/polarization/universal-coupling attribution;
19. locality/micro/global-causality;
20. complete Ward/contact/constraint response;
21. state-sector freedom;
22. cross-order shared-parameter/global invariant tests;
23. global comparator-manifold profiling;
24. rigidity / projected singular-value identifiability.

If absorbed at any step, preserve the result as negative/design evidence and do not promote it as KG novelty.

## 13. Claims forbidden from current evidence

Do not claim:

- all known gravity/QG models are wrong;
- any one of noise, decoherence, non-Gaussianity, entanglement, non-EB channel, commutator asymmetry, causal order, chirality, memory or nonanalyticity proves quantum gravity;
- a quantum mediator with a Newtonian potential is necessarily gravity;
- a higher graviton correlator is automatically beyond perturbative quantum GR;
- a covariant action automatically proves nonlinear constraint closure;
- a finite-regulator signal is a continuum QG excitation;
- a local COR is final global theory separation;
- more precision in a rank-saturated observable set creates new residual dimension;
- benchmark methodology progress changes external Candidate Gravity readiness.

## 14. How this file evolves

After every reusable benchmark result:

1. preserve exact scope/counterexample;
2. update this file only for stable construction rules;
3. update current front/state/handoff/log and immutable recovery delta;
4. never promote external Candidate Gravity readiness from benchmark evidence alone.
