# Candidate Gravity Design Priors — Beyond-C5 / Escape Appendix

**Status:** permanent supplement to `protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md`.  
**Authority:** design/red-team evidence only; no KG ansatz/readiness promotion.

## A. Wave-16 dead-end screen — do not rebuild these seeds

The cheapest prospective `DeltaGamma_KG` routes were explicitly screened before parameter fitting:

1. **local analytic metric EFT deformation** -> contained in full matched C5;
2. **EOM/Ricci-type zero-free entire nonlocal tree deformation** -> scoped tree/on-shell field-redefinition degeneracy plus functional-rigidity/causality caveats;
3. **graviton state-only deformation** -> C5 state freedom;
4. **generic quadratic CTP noise/dissipation kernel** -> generic open-system/C2/C5 structure, no gravity-specific parent attribution;
5. **extra quantum scalar mediator tuned to a Newtonian sector** -> C4/modified-gravity direction and fails minimal spin-2 gravity attribution.

Do not reintroduce any of these as KG novelty without a genuinely new cross-order relation surviving the comparator quotient.

## B. Beyond-C5 escape declaration

Every future seed must say which assumption of the low-energy local analytic metric-QFT/C5 theory space it leaves.

Canonical doors are defined in `protocol/BEYOND_C5_ESCAPE_TAXONOMY.md`:

- `E1`: nonlocal/nonanalytic parent dynamics;
- `E2`: extra propagating DOF/mediator;
- `E3`: genuinely nonperturbative/transseries sector;
- `E4`: modified fundamental quantum dynamics;
- `E5`: modified symmetry/causal/microstructure.

New machine records should use schema `KG_CANDIDATE_RECORD_v1_1.json` and declare `escape_doors`, `escape_claim`, evidence and door-specific blockers.

If no escape door is declared, a prospective beyond-C5 seed is methodologically invalid.

## C. Current search priority after Waves 16–17

The least-trivial current search region is an **E1 parent-fixed same-spin-2 deformation informed by E5-style rigidity lessons**, not arbitrary nonlocal gravity and not direct import of a causal-set operator.

Required properties:

- GR massless spin-2 IR anchor;
- low functional freedom: one/few scales/couplings, not a fitted arbitrary form factor;
- explicit Lorentzian/CTP reality and causal prescription;
- complete Ward/contact response from one parent;
- cross-order/intervention/holdout predictions;
- on-shell/relational non-equivalence to full C5;
- same-domain nonlocal/UV comparator.

Causal-set constructions are retained only as structural precedents for Lorentz/causal microstructure. Published 4D stability caveats and newer local causal-set d'Alembertian proposals prevent treating a particular causal-set nonlocal operator as the KG kernel.

`E3` remains a second-priority research door but is currently blocked by the absence of a concrete controlled 4D Lorentzian relational observable tied to a fixed nonperturbative parent saddle/transseries sector.

## D. Spectral positivity is not a kernel-selection principle

Positive spectral density / ghost-free pole structure is a **consistency filter**, not sufficient rigidity.

Entire/asymptotically-polynomial nonlocal form-factor families can admit positive spectral representations while retaining broad functional freedom. Therefore one may not select `Phi(Box)` merely by saying

- no extra free pole;
- positive Källén-Lehmann-like spectral density;
- good UV suppression.

A future kernel must be fixed by a stronger parent principle that also determines higher vertices and its Lorentzian causal/CTP completion.

## E. Three-graviton causality gate — critical correction to cubic-first E1

A cubic Weyl/Riemann deformation that changes the on-shell graviton three-point coupling is not a harmless way to keep only a massless spin-2 mode.

For weakly coupled gravity under the assumptions of the Camanho–Edelstein–Maldacena–Zhiboedov causality analysis, additional higher-derivative graviton three-point structures generate high-energy causality/time-advance problems that cannot be repaired by ordinary extra particles with spin `J<=2`; an infinite tower of higher-spin states is the standard cure within that framework.

Therefore every cubic-first E1 seed gets a mandatory blocker:

`THREE_POINT_HIGH_ENERGY_CAUSALITY_AND_HIGHER_SPIN_COMPLETION`.

This result is scoped to the assumptions of the causality analysis. A genuinely nonlocal/strongly-coupled/nonstandard completion may evade an assumption, but it must state exactly which one and demonstrate the replacement causal structure.

## F. Quartic-first fallback — safer but not automatically viable

If the design goal is to preserve

- the Einstein-Hilbert propagator; and
- the Einstein three-graviton coupling,

then the first deformation can be pushed to a quartic-curvature/higher `O(h^4)` sector.

This avoids the **specific** cubic CEMZ three-point modification gate, but does not bypass general four-graviton causality/unitarity constraints.

Modern 2-to-2 graviton dispersion analyses derive two-sided bounds on gravitational Wilson coefficients in terms of the scale of new higher-spin states in weakly-coupled EFT. Therefore a quartic-first seed must still close

- crossing/unitarity/dispersion relations;
- high-energy boundedness/time-delay constraints;
- UV state/spectrum interpretation;
- same-domain comparator profiling.

Do not treat `quartic-first` as proof that no new UV states are needed.

## G. Revised minimal search hierarchy

For same-spin-2 minimality, test candidate architectures in this order:

1. preserve GR two-point pole/residue;
2. preferably preserve the GR three-point coupling unless a complete CEMZ-compatible UV/causal mechanism is supplied;
3. locate first prospective novelty in a Ward-complete four-point or higher relational observable;
4. show the low-energy derivative expansion is fully profiled as C5;
5. require a parent-fixed cross-regime shape with few shared parameters;
6. impose four-graviton dispersion/causality/unitarity constraints;
7. profile same-domain nonlocal/UV amplitudes;
8. require cross-order/configuration/holdout rigidity and global COR separation.

## H. Status

No concrete seed currently passes this hierarchy. `ANSATZ_PROMOTED=false` remains mandatory.
