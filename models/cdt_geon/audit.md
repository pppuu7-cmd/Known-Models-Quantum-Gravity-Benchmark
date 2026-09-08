# T3-05 Audit — concrete discrete/Lorentzian QG observable

Benchmark ID: KMQGB-T3-M05-CDT
Concrete realization ID: `CDT-4D-CURVATURE-CORRELATOR-GEON-2026-001`
Role: concrete nonperturbative/discrete quantum-gravity observable control
State: ACTIVE / NONTERMINAL

## Why CDT is chosen for this target

T3-05 forbids benchmarking a program label such as “loop/discrete quantum gravity” without a concrete observable.

Causal Dynamical Triangulations (CDT) supplies a particularly clean realization because

- the microscopic histories are assembled from **Lorentzian causal building blocks**;
- the theory defines a nonperturbative gravitational path integral over causal triangulated geometries;
- a well-defined Wick rotation is used to make Monte Carlo evaluation possible;
- four-dimensional simulations possess a de-Sitter-like extended phase and quantitative geometric observables;
- in 2026 a concrete four-dimensional curvature-correlator analysis reported a signal compatible with a massive geon-like state over a finite distance window.

The benchmark therefore freezes the observable, not the entire CDT research program.

## Frozen 2026 realization

Use the four-dimensional CDT simulation and curvature-curvature correlation analysis of Maas, Plätzer & Pressler, *Hints for a geon from causal dynamic triangulations*, Physics Letters B 879 (2026) 140600.

The authors measure correlators of different gravitational curvature operators in a four-dimensional CDT ensemble and find behavior consistent with a massive state over a certain distance window. The extracted behavior is reported to be independent of the particular curvature operators considered within the analysis, while the authors explicitly characterize the result only as a **hint**, not a discovery.

## Frozen observable

Let `O_i` denote one of the gravitational curvature operators used in the simulation and let

`C_ij(r) = <O_i(x) O_j(y)>_c`,  `r = d(x,y)`

be the connected correlator in the declared lattice/geodesic-distance convention.

The benchmark observable is the **common effective massive falloff** inferred from the correlator family over the published fit window,

`C(r) ~ A(r) exp(-m_eff r)`

where `A(r)` contains the geometry/dimensional prefactor appropriate to the fit convention.

The robust sub-observable is not the numerical mass alone but

`I_CDT = {existence of a common massive-correlator window, operator-independence test, m_eff in lattice units, phase/volume dependence, continuum-scaling status}`.

This prevents a one-fit mass estimate from being overinterpreted as a new particle.

## F0-F7 map

| Gate | State | Reason |
|---|---|---|
| F0 dynamics/path integral | PASS_SCOPED | explicit CDT causal-triangulation path integral and Monte Carlo measure |
| F1 classical limit | PASS_PARTIAL | extended phase exhibits de-Sitter-like macroscopic behavior; full continuum phenomenological matching is not closed |
| F2 consistency | PASS/PARTIAL | causal construction and transfer/Wick-rotation framework are explicit; continuum reflection/unitarity and regulator-removal questions remain broader than this observable |
| F3 observable | PASS_SCOPED | explicit 4D curvature-curvature correlators measured |
| F4 comparator distinction | ACTIVE | a massive correlation length is not automatically unique to CDT/QG; lattice artifacts, finite-volume effects and generic composite-state interpretations must be profiled |
| F5 hard discriminator | BLOCKED_CONTINUUM_EXTRAPOLATION | no unique QG residual before regulator/phase/volume scaling is shown |
| F6 identifiability | BLOCKED | cannot precede F5 |
| F7 resources | N/A | numerical/theory benchmark; no direct apparatus claim |

## Lorentzian-status guardrail

CDT is a Lorentzian quantum-gravity construction at the level of its causal triangulated histories, but practical Monte Carlo measurements use the theory's Wick-rotated representation.

Therefore this audit does **not** claim that `C(r)` is already a directly measured real-time Lorentzian spectral function. The next step must state precisely how the fitted massive correlation scale maps back to Lorentzian physical propagation/asymptotic-state language, if such a map is justified.

This distinction is exactly why T3-05 is not terminal yet.

## Comparator risks

The geon-like signal must survive at least:

1. finite lattice spacing / discretization effects;
2. finite four-volume effects;
3. dependence on the CDT bare-coupling/phase location;
4. operator-choice dependence;
5. generic bound/composite-state correlation lengths that are not unique to quantum gravity;
6. continuum extrapolation along a line of constant physics.

A stable massive correlation length after these quotients would be scientifically stronger than a single-ensemble exponential fit.

## Candidate Gravity design lesson

A nonperturbative model prediction is not comparator-resistant merely because it is numerically difficult or background independent. Future KG observables must include their **regulator/continuum map** as part of the observable definition.

For KG this means: if a proposed signal arises from discretization, truncation, smearing, detector bandwidth or other regulator choices, the design prior must specify which combination survives the regulator-removal or controlled-effective-theory limit.

## Current blocker

`CDT_GEON_CONTINUUM_AND_LOR_REALTIME_MAP`:

1. extract the published fit definition and numerical `m_eff` values/uncertainties for each curvature operator;
2. check volume/coupling/phase dependence and whether a continuum scaling trajectory is available;
3. determine the status of the Wick-rotation-to-Lorentzian interpretation for the correlator pole/mass;
4. compare the signal to generic finite-volume/composite-state alternatives;
5. terminally classify only after the continuum/observable mapping is explicit.

## Operational completion estimate

**50%**.

## Sources

1. A. Maas, S. Plätzer, F. Pressler, *Hints for a geon from causal dynamic triangulations*, Phys. Lett. B 879 (2026) 140600.
2. J. Ambjørn, R. Loll, *Causal Dynamical Triangulations: New Lattice Theory of Quantum Gravity*, arXiv:2604.05641 (2026), current CDT framework review.
3. J. Ambjørn, R. Loll, *Causal Dynamical Triangulations: Gateway to Nonperturbative Quantum Gravity* (2024), Lorentzian path-integral and observable overview.
