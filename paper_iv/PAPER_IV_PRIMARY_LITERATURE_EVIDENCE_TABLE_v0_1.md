# Paper IV — primary-literature evidence table v0.1

Date: 2026-09-11
Purpose: build the citation-complete external-authority layer for the CQG manuscript without substituting repository audit files for primary physics literature.
Status: FIRST PASS / NOT YET CITATION-COMPLETE

## Usage rule

Each row separates four logically different statements:

1. what a primary external source actually establishes;
2. the current KMQGB family status;
3. the terminal object still required by the frozen comparator contract;
4. what the article is forbidden to infer.

A source listed here is an evidence anchor, not automatic family-level closure. Where a family is broad, multiple anchors are intentionally retained and further source harvesting is required.

| Tier-1 family | Primary external anchors for manuscript v1.1 | What the anchors establish within scope | Current KMQGB interpretation / remaining terminal obligation |
|---|---|---|---|
| GR + controlled low-energy gravitational EFT | Donoghue, *Phys. Rev. D* 50, 3874 (1994), DOI `10.1103/PhysRevD.50.3874`; Donoghue, *Phys. Rev. Lett.* 72, 2996 (1994), DOI `10.1103/PhysRevLett.72.2996` | Gravity can be organized as a predictive low-energy EFT; leading long-distance quantum corrections can be isolated in the low-energy theory. | `BENCHMARKED_COMPLETE_REALIZATION` only in the declared low-energy comparator domain. This is a baseline, not a UV completion claim. |
| Perturbative renormalizable / higher-derivative gravity | Stelle, *Phys. Rev. D* 16, 953 (1977), DOI `10.1103/PhysRevD.16.953`; Goroff & Sagnotti, *Phys. Lett. B* 160, 81–86 (1985), DOI `10.1016/0370-2693(85)91470-4` as Einstein-gravity contrast | Curvature-squared gravity is perturbatively renormalizable in the Stelle formulation; pure Einstein gravity has a two-loop UV divergence. | `PARTIAL_SUBFAMILY_ONLY`. Quantization/pole/prescription branches are materially distinct. Need terminal branch dispositions plus a fixed-branch normalized observable/comparator/error package. |
| Hořava–Lifshitz gravity | Hořava, *Phys. Rev. D* 79, 084008 (2009), DOI `10.1103/PhysRevD.79.084008`; Blas, Pujolàs & Sibiryakov, *Phys. Rev. Lett.* 104, 181302 (2010), DOI `10.1103/PhysRevLett.104.181302` | A power-counting-renormalizable anisotropic UV proposal exists; a materially modified non-projectable/healthy extension changes the scalar sector and low-energy theory. | `PARTIAL_SUBFAMILY_ONLY`. Projectable and non-projectable/BPS branches cannot inherit one another's status. Need same-realization UV→IR trajectory and normalized extra-mode/GR comparator package. |
| Asymptotic Safety | Reuter, *Phys. Rev. D* 57, 971 (1998), DOI `10.1103/PhysRevD.57.971`; Chiesa, Pawlowski & Reichert, arXiv:`2603.10168` (2026) | Functional RG framework and nonperturbative gravitational running are established in a truncation; 2026 work computes Lorentzian-reconstructed graviton-mediated scalar scattering and recovers GR at low energy while remaining UV bounded/unitarity-compatible within its approximation. | `BLOCKED_MISSING_REQUIRED_OBJECT`. The archival 2026 scattering paper omits direct contact term `A4`; terminality requires a public reproducible same-realization `s+t+u+A4` package with forward-limit/crossing treatment, uncertainty budget and same-domain comparators. |
| Nonlocal / infinite-derivative gravity | Biswas, Gerwick, Koivisto & Mazumdar, *Phys. Rev. Lett.* 108, 031101 (2012), DOI `10.1103/PhysRevLett.108.031101`; Biswas, Mazumdar & Siegel, arXiv:`hep-th/0508194` | Covariant ghost-free nonlocal actions with improved UV behavior and an Einstein IR limit exist; explicit nonsingular cosmological solutions exist in string-inspired higher-derivative/nonlocal constructions. | `PARTIAL_SUBFAMILY_ONLY`. Need cross-order/full-momentum functional rigidity plus exhaustion or explicit equivalence of materially independent causal/form-factor branches. |
| String / M-theory / holographic gravity | Maldacena, arXiv:`hep-th/9711200`, later *Int. J. Theor. Phys.* 38, 1113 (1999) | A concrete AdS/CFT duality proposal relates large-N CFT sectors to string/supergravity on AdS compactifications and provides a nonperturbative route in that class. | `PARTIAL_SUBFAMILY_ONLY`. This does not exhaust compactifications, duality frames, moduli sectors or flat/4D phenomenological reductions. Need a same-realization compactification/moduli→4D observable/error chain and family-scope exhaustion/reduction certificate. |
| Causal Set quantum gravity | Bombelli, Lee, Meyer & Sorkin, *Phys. Rev. Lett.* 59, 521 (1987), DOI `10.1103/PhysRevLett.59.521`; Benincasa & Dowker, *Phys. Rev. Lett.* 104, 181301 (2010), DOI `10.1103/PhysRevLett.104.181301` | Causal-set kinematics are defined as locally finite partial orders; causal-set d'Alembertian/scalar-curvature constructions recover continuum operators/curvature in suitable manifoldlike limits. | `PARTIAL_SUBFAMILY_ONLY`. Need a fundamental dynamics/measure → manifoldlike 3+1 GR regime plus a normalized genuinely causal-set gravitational observable and same-domain comparator. |
| Causal/Euclidean Dynamical Triangulations | Ambjørn, Jurkiewicz & Loll, *Phys. Rev. Lett.* 93, 131301 (2004), DOI `10.1103/PhysRevLett.93.131301`; Ambjørn, Jurkiewicz & Loll, *Phys. Rev. D* 72, 064014 (2005), DOI `10.1103/PhysRevD.72.064014` | Four-dimensional CDT exhibits a dynamically emergent macroscopic 4D phase and semiclassical large-scale volume dynamics, with nonclassical short-distance geometry. | `PARTIAL_SUBFAMILY_ONLY`. Need a controlled multi-coupling continuum/RG trajectory, lattice-spacing/scale-setting map and invariant observable with full finite-size/discretization/systematic errors. |
| Loop Quantum Gravity / EPRL-spinfoam | Rovelli & Smolin, *Phys. Rev. D* 52, 5743 (1995), DOI `10.1103/PhysRevD.52.5743`; Engle, Pereira & Rovelli, *Phys. Rev. Lett.* 99, 161301 (2007), DOI `10.1103/PhysRevLett.99.161301`; Han, *Phys. Rev. D* 114, 044040 (2026), DOI `10.1103/d8s7-jqfl` | Spin-network quantum geometry and an LQG-compatible spinfoam vertex are established; Han 2026 supplies a Lorentzian covariant summed-spinfoam UV fixed-point/continuum-limit construction. | `BLOCKED_MISSING_REQUIRED_OBJECT`. Need the same-realization continuum/refinement → physical UV-to-IR/GR trajectory → normalized gravity observable/parameter transport → comparator/error certificate. |
| Group Field Theory / tensor models | Gielen, Oriti & Sindoni, *Phys. Rev. Lett.* 111, 031301 (2013), DOI `10.1103/PhysRevLett.111.031301`; Gerhardt, Oriti & Wilson-Ewing, *Phys. Rev. D* 98, 066011 (2018), DOI `10.1103/PhysRevD.98.066011` | GFT condensate states can yield effective homogeneous cosmological dynamics; relational perturbative cosmology can reproduce GR classically with quantum-gravity corrections in a condensate sector. | `PARTIAL_SUBFAMILY_ONLY`. EPRL/FK-GFT content that reduces to spinfoams must not be double-counted; independent TGFT/condensate/tensor branches require same-realization continuum→gravity observable authority beyond scoped cosmology. |
| Causal Fermion Systems | Finster, arXiv:`2109.05906` (2021); Fischer & Finster, arXiv:`2605.30199` (2026) | CFS continuum-limit constructions recover classical gravity structures; the 2026 curved-spacetime analysis gives the coupled Einstein–Dirac equations under its assumptions. | `BLOCKED_MISSING_REQUIRED_OBJECT`. Need the first explicit normalized beyond-GR gravitational correction tensor/coefficient and same-domain comparator/error package. |
| Noncommutative spectral geometry / spectral-action gravity | Chamseddine & Connes, *Commun. Math. Phys.* 186, 731–750 (1997), arXiv:`hep-th/9606001`; Chamseddine, Connes & Marcolli, arXiv:`hep-th/0610241` | The spectral action yields Einstein plus Weyl gravity coupled to particle-physics content in the relevant spectral construction; later work develops SM+gravity realizations with neutrino mixing. | `PARTIAL_SUBFAMILY_ONLY`. Need quantum dynamics/measure for spectral data and a same-realization spectral-triple → RG/threshold → low-energy normalized observable/covariance chain at family scope. |
| Canonical Wheeler–DeWitt geometrodynamics | DeWitt, *Phys. Rev.* 160, 1113 (1967), DOI `10.1103/PhysRev.160.1113` | Canonical quantization of GR leads to quantum constraints on the state and provides the foundational Wheeler–DeWitt geometrodynamical framework. | `BLOCKED_MISSING_REQUIRED_OBJECT`. Need a full physical-Hilbert-space/state/clock/constraint-closure/normalized relational-observable/error certificate for the claimed physical comparison. |
| Quantum Graphity / dynamical-graph geometrogenesis | Konopka, Markopoulou & Severini, *Phys. Rev. D* 77, 104029 (2008), DOI `10.1103/PhysRevD.77.104029` | A background-independent dynamical-graph model exhibits a low-energy phase that is ordered, low-dimensional and local, with emergent gauge structure in the studied construction. | `PARTIAL_SUBFAMILY_ONLY`. Need same-Hamiltonian continuum Lorentzian Einstein spin-2 emergence plus a normalized gravitational observable and comparator/error certificate. |

## Immediate manuscript consequences

### Safe statements

- Every Tier-1 row now has at least one external primary-physics anchor suitable for the first citation-complete pass.
- These anchors establish nontrivial physics within scope; they do not by themselves establish family-level terminality.
- The strongest article structure is to cite external primary sources for the physics and cite the immutable KMQGB release only for the benchmark transformation, gate state and reproduction artifacts.

### Still incomplete

This table is **not yet the final citation matrix**. Before submission it still needs:

1. direct primary citations for every specific blocker sentence, not only each family identity;
2. a source for every material branch distinction used in the main-text matrix;
3. primary authority for every comparator/normalization claim;
4. stable bibliographic metadata/DOIs for all arXiv-only entries where a published version exists;
5. archival citation for the September-2026 Asymptotic Safety contact-term development if/when it becomes a stable public publication;
6. exact external attribution audit for all LQG gamma/Delta/RG equations before any novelty wording is frozen.

## Article guardrail

A row with several positive primary citations can remain `PARTIAL` or `BLOCKED`; this means only that the specific family-level common-domain comparison demanded by Paper IV is not yet defined. It is forbidden to rewrite that state as “the theory failed.”
