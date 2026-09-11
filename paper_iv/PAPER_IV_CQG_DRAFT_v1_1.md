# RQIR Paper IV — CQG Draft v1.1

**Target journal:** Classical and Quantum Gravity  
**Article type:** Research Paper  
**Draft snapshot:** 2026-09-11  
**Coverage authority:** KMQGB Iter275, 15 Tier-1 rows  
**D7 readiness authority:** KMQGB Iter276  
**Validation note:** Iter276 synchronization validation is pending; the older `recovery/CURRENT_BENCHMARK_FRONT.md` still lags at Iter274 and is not used as the quantitative authority for this draft.  
**Submission status:** WORKING DRAFT / NOT YET SUBMISSION-AUTHORIZED

# Frozen-observable benchmarking across quantum-gravity frameworks: same-realization closure and global decision gates

**Authors:** [to be finalized]  
**Affiliations:** [to be finalized]

## Abstract

Comparisons between quantum-gravity frameworks are often assembled from calculations performed in different states, signatures, truncations, normalizations, scales and observable definitions. Agreement or disagreement between such calculations is not automatically a physical statement unless the compared objects belong to a common realization and comparator domain. We introduce the Known Models / Quantum Gravity Benchmark (KMQGB), an application of the frozen Relativity–Quantum Interface Reconstruction (RQIR) Core v1.0 to a prospectively extensible census of quantum-gravity framework families. Framework-native objects are mapped into a common observable/comparator language while outcome-dependent retuning of the judge is forbidden. The protocol requires explicit same-realization provenance, family-scope closure and defined normalization and uncertainty objects; missing ingredients remain BLOCKED rather than being converted into negative residuals. The current coverage contract contains fifteen Tier-1 families after a newly identified independent Relational Quantum Causal Processes parent was admitted by a pre-existing promotion rule. Only the General Relativity plus controlled low-energy effective-field-theory baseline is strict terminal at family scope; fourteen candidate rows remain partial or blocked, and the global theory-selection classifier is unauthorized. Under a deterministic primary-obstruction projection the fourteen nonterminal rows map to five recurring current classes with count vector \((5,6,1,1,1)\). The exact split between family-scope and same-realization transport blockers depends on tie-breaking, but their combined dominance is stable across bounded alternative projections at \(11/14\). We formalize the associated no-promotion rule and show how recent positive results in loop/spinfoam gravity, asymptotic safety and relational quantum causal processes change evidence or coverage without changing the frozen criterion. KMQGB therefore yields neither an exclusion census nor a requirement for a new theory; it provides an auditable map of the proof obligations that must be closed before cross-framework quantum-gravity discrimination is physically defined.

**Keywords:** quantum gravity; gravitational observables; theory comparison; same-realization closure; loop quantum gravity; asymptotic safety; effective field theory; reproducibility

---

## 1. Introduction

Quantum gravity is represented by a heterogeneous collection of research programmes rather than a single model class. Perturbative and higher-derivative gravities, Hořava–Lifshitz gravity, asymptotic safety, nonlocal gravity, string and M-theory, holographic constructions, causal sets, dynamical triangulations, loop quantum gravity and spinfoams, group-field and tensor models, causal fermion systems, noncommutative spectral geometry, canonical Wheeler–DeWitt quantization, dynamical-graph approaches and newer quantum-causal constructions differ not only in their microscopic assumptions but also in the physical objects they compute. Modern reviews, maps of the field and phenomenological roadmaps accordingly organize the landscape by theoretical programme, cosmological signature, experimental channel or possible relation between approaches \cite{Barrau2017,MielczarekTrzesniewski2018,AddaziEtAl2022,BambiModestoShapiro2024,AlvesBatistaEtAl2025}.

The present work addresses a complementary question. Before asking which quantum-gravity framework is favored by observation, or even whether two frameworks disagree with one another, one must establish that the compared quantities are physically comparable. A UV fixed point, a spin-foam amplitude, a lattice observable, a spectral action, a relational cosmological perturbation, an induced gravitational response and a low-energy scattering amplitude are not automatically members of one comparison space merely because each is associated with gravity. They may differ in state, signature, boundary conditions, regulator, truncation, normalization, source routing, response order, scale-setting convention or the physical meaning assigned to a parameter.

This distinction matters because incompleteness can otherwise be mistaken for falsification. Consider three generic situations. First, a framework may possess a controlled ultraviolet construction but lack a same-realization trajectory to a normalized low-energy observable. Second, a successful calculation may apply only to one material quantization, compactification, state sector or prescription branch and therefore not determine the status of the parent framework family. Third, a numerical or analytic observable may be available while its proposed comparator uses a different state, response order or normalization. None of these cases defines an ordinary physical disagreement. The comparison itself is incomplete.

Relativity–Quantum Interface Reconstruction (RQIR) was developed to make such distinctions explicit. In the present paper we apply its frozen Core v1.0 to known quantum-gravity frameworks through the Known Models / Quantum Gravity Benchmark (KMQGB). The benchmark-facing pipeline is

\[
\text{framework-native object}
\longrightarrow \text{framework adapter}
\longrightarrow \text{same-realization gate}
\longrightarrow \text{common observable/comparator domain}
\longrightarrow \text{terminal, partial or blocked state}.
\]

The core comparison rules are frozen before framework outcomes are interpreted. Framework-specific adapters may translate variables and conventions, but they may not alter the judge to rescue or reject a difficult model. Adjacent literature results may be composed only after a same-realization map has been established. A missing physical object remains missing: it is not assigned a zero residual and is not counted as exclusion evidence.

The contribution is therefore not a new catalogue of quantum-gravity approaches. Broad comparative maps and phenomenological roadmaps already exist \cite{MielczarekTrzesniewski2018,AddaziEtAl2022,AlvesBatistaEtAl2025}. Nor is the logical core of our family-scope rule presented as a new theorem of statistical model selection. Composite hypotheses and partial identification already make clear that a statement about a restricted or unidentified object does not automatically determine an entire model class \cite{Phillips1989PartialIdentification}. The contribution here is to operationalize that logic in a physical quantum-gravity benchmark: a realization vector records the ancestry of imported objects, a residual is defined only after a common comparator map exists, family-level promotion is gated explicitly, and the rules are executed across a declared multi-framework census.

The census itself is prospectively extensible. The first full manuscript snapshot contained fourteen Tier-1 rows. After that snapshot, a concrete Relational Quantum Causal Processes (RQCP) parent with materially distinct observables and no established reduction map to an existing row was identified \cite{Xu2026RQCPFramework,Xu2026}. A pre-existing coverage rule required such an independent parent to be promoted rather than ignored. The current census therefore contains fifteen Tier-1 rows. This change is methodologically useful: the denominator becomes less favorable, from one terminal row out of fourteen to one out of fifteen, because coverage increased. The benchmark therefore does not preserve an earlier success fraction by excluding newly identified independent physics.

Four results organize this paper. First, KMQGB remains operationally saturated with respect to currently available internal work while scientific family-level closure is strongly incomplete: only the General Relativity plus controlled low-energy effective-field-theory baseline is strict terminal. Second, the fourteen current nonterminal rows can be projected onto five recurring primary obstruction classes. A deterministic baseline projection gives the count vector \((5,6,1,1,1)\). The precise split between family-scope and same-realization transport depends on a declared tie-breaking convention, but their combined share remains \(11/14\) under the bounded alternative projections studied here. Third, we formalize a protocol-level no-promotion proposition explaining why scoped evidence cannot be elevated to a parent-family sufficiency or exclusion statement while material scope or required comparison objects remain unresolved. Fourth, recent developments in loop/spinfoam gravity, asymptotic safety and RQCP provide prospective stress tests: new positive evidence and even a new independent parent alter the evidence or coverage state without changing the frozen judge.

The paper is organized as follows. Section 2 defines the frozen comparison architecture and prospectively extensible family census. Section 3 formalizes realization and comparator closure and states the no-promotion proposition. Section 4 reports the fifteen-family benchmark and the obstruction topology. Section 5 develops representative physical cases. Section 6 gives the current global D-gate state. Section 7 discusses implications for comparative quantum gravity and phenomenology. Section 8 states limitations, and section 9 concludes.

---

## 2. Frozen comparison architecture

### 2.1 Independent judge and framework adapters

The central governance choice is to freeze RQIR Core v1.0 before the Paper-IV family outcomes are interpreted. The purpose is to prevent outcome-dependent retuning. If a framework-specific calculation cannot satisfy an observable or comparator requirement, that requirement is not weakened merely to obtain a terminal row. Conversely, a favorable result in one subfamily does not enlarge its own scope after inspection.

The frozen core does not imply that all frameworks must use identical microscopic variables. A framework adapter is allowed, and in practice required, to convert a native calculation into the declared comparison language. An adapter may document a change of variables, convention translation, normalization, scale transport, observable extraction or explicit reduction map. What it may not do is alter the logical meaning of terminality, same-realization identity or a defined residual.

This separation creates a firewall,

\[
\text{framework outcome}\not\rightarrow\text{redefinition of the judge}.
\]

A genuine defect in the frozen core would require independent change control. A blocked comparison is not, by itself, evidence that the core is defective.

### 2.2 Prospectively extensible framework census

The current major-framework coverage contract contains fifteen Tier-1 rows. Broad coverage is anchored to the modern quantum-gravity literature, while additional independent programmes are promoted when they possess a distinct quantum parent and gravity/emergence claim \cite{BambiModestoShapiro2024}. The present rows are:

1. General Relativity plus controlled low-energy gravitational EFT, used as the baseline comparator;
2. perturbative renormalizable / higher-derivative quantum gravity;
3. Hořava–Lifshitz quantum gravity;
4. asymptotic safety;
5. nonlocal / infinite-derivative quantum gravity;
6. string / M-theory / holographic quantum gravity;
7. causal set quantum gravity;
8. causal and Euclidean dynamical triangulations;
9. loop quantum gravity / EPRL-spinfoam;
10. group field theory / tensor models;
11. causal fermion systems;
12. noncommutative spectral geometry / spectral-action gravity;
13. canonical Wheeler–DeWitt geometrodynamics;
14. quantum graphity / explicit dynamical-graph geometrogenesis;
15. relational quantum causal processes / RQCP-QG.

The census is not claimed to be an ontological partition of every idea called quantum gravity. It is a comparison contract. A Tier-2 label can be reduced to an existing row only through an explicit ancestry or reduction map. Conversely, a new concrete independent parent is promoted to Tier-1 when no such reduction is established. At the current snapshot, the unresolved Tier-2 count is zero.

The RQCP promotion provides an executed example of this rule. The initial fourteen-family manuscript had already frozen the condition that a concrete independent quantum parent with a gravity/emergence claim and materially distinct observables should be promoted rather than silently omitted. The subsequent RQCP audit triggered that rule, producing a fifteenth nonterminal row without altering RQIR Core or the terminality criteria. This feature will be important below because it separates prospective coverage from outcome selection.

### 2.3 Family scope

A framework family is not interchangeable with one calculation. Let a family \(F\) possess a set of material branches

\[
B_F=\{b_1,\ldots,b_n\},
\]

where a branch may be distinguished by quantization prescription, compactification, state sector, continuum phase, truncation class, regulator class or another physically material choice. A result for \(b_i\) can be promoted to the family only if at least one of the following is established:

- all material branches relevant to the claim have terminal dispositions;
- a theorem establishes the required equivalence class;
- an explicit reduction map merges the branch into another row;
- a scope proof shows that the branch lies outside the declared Paper-IV target.

This rule is symmetric. A scoped failure cannot exclude a parent family, and a scoped success cannot establish family-wide sufficiency.

### 2.4 Evidence states

For article-facing use, KMQGB distinguishes six evidence states:

- **ESTABLISHED_EXTERNAL:** established by an external publication or public data/programme authority within its stated scope;
- **DERIVED_KMQGB:** analytically derived inside KMQGB from declared inputs and frozen assumptions;
- **REPRODUCED_EXECUTABLE:** reproduced by a stable executable control;
- **OPEN_BLOCKED:** a required theory, provenance, transport, observable, normalization, comparator or uncertainty object is absent or non-composable;
- **HYPOTHESIS_ONLY:** exploratory content that has not met promotion obligations;
- **FORBIDDEN_OVERCLAIM:** a proposed statement incompatible with the admitted evidence.

The decisive semantic rule is

\[
\boxed{\mathrm{BLOCKED}\neq \mathrm{FAIL}}.
\]

A blocked row can contain highly informative positive physics. Its status says only that the current evidence does not define the family-level comparison requested by the benchmark.

### 2.5 Operational saturation and scientific closure

Operational saturation is defined independently of scientific terminality. A row is internally saturated when, given the available public authority and the frozen protocol, no presently justified internal calculation or literature operation can change its family-level terminal classification without a new external theory, data or provenance object. The benchmark can therefore be operationally complete while the physical comparison remains open.

This separation prevents a common ambiguity in computational research programmes. Completing every currently executable task does not imply that a missing physical map exists. Conversely, an externally supplied map can reopen a saturated row immediately. Operational saturation is a statement about the frontier of admissible work, not the truth or falsity of the candidate theories.

---

## 3. Same-realization and observable closure

### 3.1 Realization vector

For each imported object we associate a realization descriptor

\[
\mathcal{R}=(P,S,B,G,R,T,\Sigma,N,\mu,J),
\]

where the entries denote, as applicable, parent theory \(P\), state \(S\), boundary conditions \(B\), gauge information \(G\), regulator \(R\), truncation \(T\), signature \(\Sigma\), normalization \(N\), scale or scale-setting map \(\mu\), and source routing \(J\). The exact content is framework dependent, but the principle is not: two objects are not composable merely because they share a programme label.

An explicit map

\[
M_{12}:\mathcal{R}_1\rightarrow\mathcal{R}_2
\]

must preserve the physical identities required by the intended claim. When a parameter in one layer is said to be the same parameter as one in another layer, the ancestry or transport relation is part of the evidence, not a convention that may be inserted after comparison.

### 3.2 Common observable/comparator domain

Let a framework prediction in a realization \(\mathcal{R}\) be represented by an observable object

\[
O_F(\mathcal{R};x),
\]

where \(x\) denotes the relevant kinematic, geometric or scale variables. Let \(O_C\) be the comparator. A residual is admitted only when the domain-matching map \(\Pi\) is defined,

\[
\Delta_F(x)=\Pi[O_F](x)-O_C(x).
\]

The map \(\Pi\) contains the response order, state/background, normalization, source routing, contact/amputation convention and uncertainty treatment required by the claim. If \(\Pi[O_F]\) is undefined, then \(\Delta_F\) is undefined. KMQGB does not substitute \(\Delta_F=0\), does not infer agreement, and does not infer disagreement.

This is particularly important for cross-regime comparisons. An ultraviolet trajectory and an infrared observable may each be well defined independently while their composition is not. The missing object is then a physical transport map, not additional decimal precision.

### 3.3 Terminality

A scoped realization is terminal for an article-facing comparison only when the required physical object, same-realization provenance, common-domain comparator and error/uncertainty objects are defined to the level declared by that comparison. A family is terminal only when the family-scope rule in section 2.3 is also closed.

Accordingly, three conceptually different outcomes must be kept separate:

1. a **defined terminal comparison**, for which a residual or equivalence statement has physical meaning;
2. a **scoped result**, for which a local calculation is meaningful but parent-family scope is incomplete;
3. a **blocked comparison**, for which a required object or composition map is missing.

### 3.4 Proposition 1: no promotion under incomplete realization closure

**Proposition 1 (protocol-level no-promotion).** Let \(F\) be a Tier-1 framework family with material branches \(B_F\). Under the frozen Paper-IV coverage contract, a scoped PASS or FAIL result for a subset \(B'\subset B_F\) does not entail a family-level sufficiency or exclusion statement if either (i) at least one material branch in \(B_F\setminus B'\) lacks a terminal disposition or valid reduction/scope proof, or (ii) any physical residual required for the family-level claim is undefined because the same-realization/common-domain map is incomplete.

**Proof.** A family-level statement quantifies over the material domain declared for \(F\). In case (i), the evidence constrains only \(B'\), while at least one material branch remains admissible under the coverage contract. Promoting the scoped result would therefore add an unproved premise about the unresolved branch. In case (ii), the family-level predicate depends on a residual that is not defined in the comparison domain. Assigning a sign, magnitude or zero value to that residual would add information not contained in the evidence. In either case the family-level statement is not entailed by the admitted evidence. The frozen contract therefore permits only a partial or blocked state. \(\square\)

The proposition is not intended as a new theorem of statistical model selection. Its logical core has close analogues in composite-hypothesis reasoning and partial identification \cite{Phillips1989PartialIdentification}. Its role here is operational: KMQGB attaches the non-promotion rule to explicit physical realization, comparator and family-scope objects and then executes it over the quantum-gravity census.

**Corollary 1 (precision cannot repair structural undefinedness).** If a terminal blocker is the absence of a same-realization map, physical observable, normalization identity or comparator definition, reducing numerical uncertainty within an adjacent but non-composable calculation cannot by itself make the family-level residual defined.

The corollary explains the benchmark's current heavy-compute discipline. Numerical work becomes decisive only when a prospectively specified calculation can alter a terminal disposition. It does not imply that computational work in quantum gravity is generally unimportant.

---

## 4. Results: the fifteen-family benchmark

### 4.1 Global result matrix

Table 1 summarizes the current family-level state. `PARTIAL_SUBFAMILY_ONLY` denotes scientifically meaningful scoped results without family-scope closure. `BLOCKED_MISSING_REQUIRED_OBJECT` denotes a missing physical or attribution object at the terminal comparison level. Neither status is an exclusion.

| Family | External physics anchor(s) | Current state | Primary terminal obstruction at current snapshot |
|---|---|---|---|
| GR + controlled low-energy gravitational EFT | Donoghue \cite{Donoghue1994EFT,Donoghue1994Newtonian} | `BENCHMARKED_COMPLETE_REALIZATION` | Terminal baseline comparator in the declared low-energy domain; no UV-completion claim is implied. |
| Perturbative renormalizable / higher-derivative gravity | Stelle \cite{Stelle1977} | `PARTIAL_SUBFAMILY_ONLY` | Material quantization/pole/prescription branches require independent disposition or equivalence/exhaustion plus a fixed-branch normalized observable/comparator package. |
| Hořava–Lifshitz gravity | Hořava; Blas–Pujolàs–Sibiryakov \cite{Horava2009,BlasPujolasSibiryakov2010} | `PARTIAL_SUBFAMILY_ONLY` | Projectable and non-projectable/BPS branches cannot inherit status; a same-realization UV-to-IR extra-mode/GR observable chain remains incomplete. |
| Asymptotic Safety | Reuter; Chiesa–Pawlowski–Reichert \cite{Reuter1998,ChiesaPawlowskiReichert2026} | `BLOCKED_MISSING_REQUIRED_OBJECT` | A stable public reproducible contact-complete Lorentzian \(s+t+u+A_4\) package with forward-limit/crossing treatment, uncertainty control and same-domain comparators is not yet frozen. |
| Nonlocal / infinite-derivative gravity | Biswas et al. \cite{BiswasGerwickKoivistoMazumdar2012,BiswasMazumdarSiegel2005} | `PARTIAL_SUBFAMILY_ONLY` | Material functional-form/causality branches and cross-order/full-momentum rigidity are not exhausted at family scope. |
| String / M-theory / holographic gravity | Maldacena \cite{Maldacena1997} | `PARTIAL_SUBFAMILY_ONLY` | Scoped duality/amplitude results do not close material compactification/duality branches or a same-realization compactification/moduli-to-4D observable/error chain. |
| Causal Set quantum gravity | Bombelli et al.; Benincasa–Dowker \cite{BombelliLeeMeyerSorkin1987,BenincasaDowker2010} | `PARTIAL_SUBFAMILY_ONLY` | Fundamental measure/dynamics to manifoldlike 3+1 GR and a normalized genuinely causal-set gravitational observable remain incomplete. |
| Causal/Euclidean Dynamical Triangulations | Ambjørn–Jurkiewicz–Loll \cite{AmbjornJurkiewiczLoll2004,AmbjornJurkiewiczLoll2005} | `PARTIAL_SUBFAMILY_ONLY` | Multi-coupling continuum trajectory, scale setting, invariant observable and systematic-error capsule remain incomplete. |
| Loop Quantum Gravity / EPRL-spinfoam | Rovelli–Smolin; EPRL; Bianchi–Rincon-Ramirez; area-metric and 2026 fixed-point work \cite{RovelliSmolin1995,EnglePereiraRovelli2007,BianchiRinconRamirez2026,DittrichKogios2023,BorissovaDittrichEichhornSchiffer2025,Dittrich2026AreaMetricGW,Han2026UVFixedPoint} | `BLOCKED_MISSING_REQUIRED_OBJECT` | Strong microscopic/continuum-adjacent evidence exists, but the same-realization UV-to-IR/GR trajectory, physical observable, parameter/refinement transport and comparator/error certificate remain missing. |
| Group Field Theory / tensor models | Gielen–Oriti–Sindoni; Gerhardt–Oriti–Wilson-Ewing \cite{GielenOritiSindoni2013,GerhardtOritiWilsonEwing2018} | `PARTIAL_SUBFAMILY_ONLY` | After separating content reducible to spin foams, independent TGFT/condensate/tensor branches still require continuum-to-gravity observable authority. |
| Causal Fermion Systems | Finster; Fischer–Finster \cite{Finster2021CFS,FischerFinster2026} | `BLOCKED_MISSING_REQUIRED_OBJECT` | An explicit normalized beyond-GR gravity correction tensor/coefficient with a same-domain comparator remains unavailable at the requested level. |
| Noncommutative spectral geometry | Chamseddine–Connes and collaborators \cite{ChamseddineConnes1997,ChamseddineConnesMarcolli2006} | `PARTIAL_SUBFAMILY_ONLY` | Spectral-data to RG/threshold to low-energy observable and covariance transport is incomplete at family scope. |
| Canonical Wheeler–DeWitt geometrodynamics | DeWitt \cite{DeWitt1967Canonical} | `BLOCKED_MISSING_REQUIRED_OBJECT` | Full physical-Hilbert-space/state/clock/constraint/relational-observable/error closure is missing for the requested family-level comparison. |
| Quantum Graphity / dynamical-graph geometrogenesis | Konopka–Markopoulou–Severini \cite{KonopkaMarkopoulouSeverini2008} | `PARTIAL_SUBFAMILY_ONLY` | Same-Hamiltonian continuum Lorentzian Einstein spin-2 emergence and a normalized gravitational observable/comparator certificate remain incomplete. |
| Relational Quantum Causal Processes / RQCP-QG | Xu \cite{Xu2026RQCPFramework,Xu2026} | `PARTIAL_SUBFAMILY_ONLY` | A positive fixed-band same-family construction exists, but family-level/all-band background-independent autonomous gravity, gravity-state/constraint structure, broader regime control and normalized common-domain comparator closure remain open. |

The paired global metrics in the current coverage/D7 snapshot are

\[
N_{\rm Tier1}=15,\qquad N_{\rm terminal}=1,\qquad N_{\rm nonterminal}=14,
\]

\[
N_{\rm Tier2,unresolved}=0,\qquad N_{\rm internal\ actionable}=0.
\]

The operational proving ground remains saturated at 100% with respect to currently admissible internal work, whereas strict family-terminal scientific coverage is \(1/15\). These quantities must not be conflated. Operational saturation means that the present authority has been reduced to terminal objects or explicit reopen conditions; it does not mean that fourteen candidate families have failed.

### 4.2 Primary-obstruction topology

A second result appears when the fourteen nonterminal rows are projected onto the obstruction that currently prevents terminal promotion. The projection is deliberately a **primary-blocker** map rather than an assertion that each family has only one difficulty. Several rows possess secondary obstacles. We use a deterministic rule: unresolved material parent-family scope is checked first; otherwise a missing same-realization transport map is checked; otherwise amplitude/comparator completeness, an explicit beyond-baseline correction object, and physical-state/relational-observable closure are checked in that order.

The baseline assignments are:

**Class C1 — family or branch scope (5 families).**  
Perturbative/higher-derivative gravity, Hořava–Lifshitz gravity, nonlocal gravity, string/M-theory/holography and RQCP. In each case a positive child result cannot yet stand for the complete parent family. RQCP belongs here in the baseline rule because its controlled fixed-band result is explicitly scoped while broader all-band/background-independent family closure remains open.

**Class C2 — same-realization transport (6 families).**  
Causal sets, CDT/EDT, LQG/spinfoams, GFT/tensor models after explicit reducible-content separation, noncommutative spectral geometry and quantum graphity. These rows contain meaningful microscopic, continuum, RG, weak-field or emergent-geometry ingredients, but the terminal chain to a normalized common gravitational observable is incomplete.

**Class C3 — amplitude/comparator completeness (1 family).**  
Asymptotic safety. The active blocker is narrower than a generic UV-to-IR absence: the present target is a stable public contact-complete same-realization Lorentzian scattering package with the required forward-limit, uncertainty and comparator closure.

**Class C4 — explicit beyond-baseline correction object (1 family).**  
Causal Fermion Systems. A classical/continuum gravitational structure exists, while the comparison demands an explicit normalized beyond-baseline correction tensor or coefficient.

**Class C5 — physical-state and relational-observable closure (1 family).**  
Canonical Wheeler–DeWitt geometrodynamics. The decisive issue is not merely calculation precision but the physical state/clock/constraint/Dirac-observable certificate required before the family-level observable is fixed.

The deterministic baseline count vector is therefore

\[
(5,6,1,1,1).
\]

The exact split between C1 and C2 is not invariant under reasonable tie-breaking. A transport-first projection, in which an explicit UV/continuum-to-observable gap takes precedence whenever it coexists with parent-scope incompleteness, gives

\[
(2,9,1,1,1),
\]

whereas a scope-maximal projection gives

\[
(6,5,1,1,1).
\]

The robust result is therefore not the exact five-versus-six division. In all three bounded projections,

\[
N_{C1+C2}=11,
\qquad
\frac{N_{C1+C2}}{N_{\rm nonterminal}}=\frac{11}{14}\simeq 78.6\%.
\]

Thus, in the current declared census, most nonterminality occurs structurally upstream of a terminal numerical residual: the dominant question is which parent/branch is being claimed and how its physical object reaches the common comparator domain. This is a protocol- and snapshot-specific statement, not a claim that 78.6% of all conceivable quantum-gravity theories in nature share one defect.

### 4.3 Why the nonterminal result is scientifically informative

The result above is conservative in the sense that it does not select a winning framework. Its scientific content is instead in localizing what remains undefined. Each nonterminal row carries a reopen condition precise enough that a future publication, calculation or data product can change the state without redesigning the comparison procedure. The statement “not yet comparable at family scope” is therefore converted into a testable workflow claim: either the named object appears and the gate is re-evaluated, or it does not.

The topology also distinguishes qualitatively different kinds of incompleteness. A family-scope problem is not the same as a missing contact term; a missing UV-to-IR transport map is not the same as an unresolved physical Hilbert space; and absence of a normalized correction object is not evidence that the correction vanishes. Collapsing these situations into a single score would erase precisely the information required to close them.

### 4.4 Prospective census expansion as a stress test

The RQCP promotion supplies a particularly useful test of the benchmark's prospective behavior. The initial manuscript census contained fourteen rows. The coverage contract already stated that a new concrete independent quantum parent with a gravity/emergence claim and materially distinct observables should trigger Tier-1 promotion unless an explicit reduction map existed. When the RQCP line was audited \cite{Xu2026RQCPFramework,Xu2026}, the rule was activated.

This increased the census from fourteen to fifteen while leaving the number of strict terminal rows unchanged at one. The terminal fraction therefore decreased. That change is scientifically preferable to preserving an artificially favorable denominator. It demonstrates that the coverage contract can admit a new candidate even when doing so makes global closure more difficult.

The RQCP result itself is not treated negatively. Its fixed-band construction is a positive scoped result, and independent cross-environment semantic recomputation within KMQGB reproduced its headline gates. But the source explicitly limits the construction to a controlled fixed-band/finite-cutoff and prescribed semiclassical sector \cite{Xu2026}. The appropriate benchmark outcome is therefore `PARTIAL_SUBFAMILY_ONLY`, not either “solved quantum gravity” or “failed theory.”

---

## 5. Representative physical cases

### 5.1 Loop/spinfoam gravity: algebraic closure versus physical ancestry

The loop/spinfoam sector provides the most developed example of the distinction between an algebraically constrained bridge and a physically established bridge. The literature supplies several adjacent layers: spin-network quantum geometry and EPRL-type amplitudes \cite{RovelliSmolin1995,EnglePereiraRovelli2007}; a gamma-dual parity-sensitive effective action and primordial observable relation \cite{BianchiRinconRamirez2026}; an effective spin-foam/area-metric continuum programme \cite{DittrichKogios2023}; an area-metric renormalization-group flow for the Immirzi parameter \cite{BorissovaDittrichEichhornSchiffer2025}; a Lorentzian area-metric birefringence channel \cite{Dittrich2026AreaMetricGW}; and a 2026 Lorentzian summed-spinfoam UV fixed-point/continuum result \cite{Han2026UVFixedPoint}. The central KMQGB question is whether these layers can be composed as one realization rather than merely placed next to one another.

Bianchi and Rincon-Ramirez provide, in their chosen gamma-dual effective model, the ideal parity-sector relation

\[
\rho\equiv\frac{2f_{\rm GB}}{f_{\rm CS}}
=\gamma-\frac{1}{\gamma},
\]

and the primordial tensor combination

\[
q\equiv\frac{\pi}{8}\frac{r+8n_T}{\Pi}
=\frac{1}{\gamma}-\gamma.
\]

The same source also emphasizes that a top-down derivation of the effective action from non-perturbative spinfoam dynamics is missing \cite{BianchiRinconRamirez2026}. KMQGB therefore does not treat the ideal relation as a completed microscopic-to-EFT bridge.

To parameterize possible matching violation, KMQGB defines

\[
\Delta_\gamma
\equiv
\rho-\left(\gamma-\frac{1}{\gamma}\right).
\]

The generalized observable form is then written

\[
q=\frac{1}{\gamma}-\gamma-\Delta_\gamma.
\]

Under this common residual convention the two coordinates satisfy identically

\[
q=-\rho,
\qquad
\beta_q=-\beta_\rho.
\]

This identity is useful because it makes the sign convention between the Wilson-coefficient and observable-space representations explicit. Differentiating the residual with respect to RG time gives the KMQGB identity

\[
\beta_\Delta
=
\beta_\rho-\left(1+\frac{1}{\gamma^2}\right)\beta_\gamma.
\]

The area-metric realization provides a separate pair of source relations,

\[
\sinh(2\xi)=\frac{1}{\gamma},
\qquad
\psi=-\frac12\arctan(\tanh\xi),
\]

within the model studied in \cite{Dittrich2026AreaMetricGW}. Eliminating \(\xi\), KMQGB obtains on the positive-\(\gamma\) branch

\[
\gamma=-\cot(4\psi),
\]

and hence

\[
\frac{1}{\gamma}-\gamma=2\cot(8\psi).
\]

After transport to a common scale in one realization,

\[
\Delta_\gamma=2\cot(8\psi)-q,
\]

and differentiation yields

\[
\beta_\Delta
=-16\csc^2(8\psi)\,\beta_\psi-\beta_q.
\]

Because

\[
\beta_\psi=\frac{\beta_\gamma}{4(1+\gamma^2)},
\]

this expression is exactly equivalent to the Wilson-coordinate form once \(\beta_q=-\beta_\rho\) is used. The algebraic sign consistency therefore closes internally.

The attribution is important. The ideal parity/inflation relations are external results of Bianchi and Rincon-Ramirez; the \((\xi,\psi,\gamma)\) relations are external results of the area-metric construction; \(\Delta_\gamma\), the compact inverse \(\gamma=-\cot(4\psi)\), and the displayed residual transport equations are KMQGB definitions or algebraic reductions of those source relations. None of them proves that the microscopic EPRL object, area-metric RG flow and inflationary EFT share one physical ancestry.

The Han 2026 Lorentzian fixed-point result materially strengthens the UV/continuum side \cite{Han2026UVFixedPoint}. Under the frozen benchmark, however, the remaining proof obligation is still a same-realization path from the microscopic/refined construction through the physical infrared/GR regime to a normalized observable, including parameter ancestry and comparator/error control. This case therefore shows how algebraic closure can become stronger while family-level physical closure remains open.

### 5.2 Asymptotic safety: a high-value near miss in Lorentzian scattering

Asymptotic safety currently provides the clearest example of a narrow blocker being attacked by new external work. The functional renormalization-group programme supplies the broader nonperturbative context \cite{Reuter1998}. Chiesa, Pawlowski and Reichert compute the full momentum dependence of the scalar–graviton three-point vertex, reconstruct a timelike/Lorentzian vertex and obtain a graviton-mediated scalar-scattering amplitude and cross section with the expected low-energy GR behavior and controlled high-energy behavior within their stated approximation \cite{ChiesaPawlowskiReichert2026}.

The archival calculation writes the complete amplitude schematically as

\[
\mathcal{A}=\mathcal{A}_s+\mathcal{A}_t+\mathcal{A}_u+\mathcal{A}_4,
\]

while focusing on the graviton-mediated pieces and omitting the direct contact contribution \(\mathcal{A}_4\). The contact term is also relevant to the forward-limit treatment. A September 2026 ERG conference contribution reports progress on a gravitational contact contribution in Lorentzian signature \cite{ChiesaERG2026}. This development directly targets the previously frozen blocker.

Nevertheless, the current stable archival and reproducibility authority does not yet provide one public contact-complete same-realization package containing \(s+t+u+A_4\), forward-limit/crossing treatment, approximation and uncertainty control, reproducibility material and the required same-domain comparators. The family therefore remains `BLOCKED_MISSING_REQUIRED_OBJECT`.

The interpretation is deliberately narrow. Asymptotic safety is not excluded. Nor is the conference result ignored. It is recorded as a high-value near miss that can reopen the row immediately if a stable public package satisfying the already-declared terminal condition appears. This is the behavior expected from a frozen benchmark: new physics changes the evidence state without changing the admission criterion.

### 5.3 Relational quantum causal processes: positive scoped closure and census expansion

RQCP is useful for a different reason: it tests both scientific reproducibility and the census boundary. The broader framework develops exact and controlled relational quantum-causal constructions and explicitly discusses the boundary between emergent gravitational behavior and a completed background-independent gravity parent \cite{Xu2026RQCPFramework}. A subsequent controlled construction follows one interacting finite-Hilbert lineage across a declared fixed physical Fourier band and relates it to a Lorentzian excitation gap, nonlinear response, mixed matter–geometry response, a dynamic geometry kernel, a positive induced Newton coefficient in a prescribed local covariant two-derivative FLRW sector, and semiclassical Friedmann evolution \cite{Xu2026}.

KMQGB treated this as more than a verbal emergent-gravity proposal. The public evidence package was independently recomputed in four hosted runner configurations, using semantic rather than byte-for-byte comparison because floating linear algebra need not be bit-identical across environments. The headline physics gates were stable. The audit also identified a numerical diagnostic defect at exactly zero frequency: two analytically identical expressions were separately evaluated in floating arithmetic, their round-off difference was divided by an extremely small denominator, and a very large diagnostic number resulted. Because the analytic remainder at zero frequency is exactly zero and the defect does not flip the declared closure gates, KMQGB records it as an implementation/reproducibility issue rather than a physical divergence.

The positive scoped result is therefore preserved. At the same time, the source does not claim an all-band, background-independent autonomous quantum-gravity completion. The family-level benchmark still requires substantially broader closure: an autonomous gravity parent or equivalent construction, a gravity-state/constraint structure, broader regime and topology control, family-level exhaustion, and normalized common-domain observables and errors. The row is consequently `PARTIAL_SUBFAMILY_ONLY`.

The more general methodological result is the promotion itself. RQCP was absent from the original fourteen-row census, but the coverage rule already required an independent concrete parent without a reduction map to receive its own row. Adding it lowered the strict terminal fraction from \(1/14\) to \(1/15\). This is a prospective anti-selection-bias test: a new candidate is not omitted because its inclusion makes the benchmark appear less closed.

### 5.4 Hořava–Lifshitz gravity: branch non-inheritance

Hořava–Lifshitz gravity illustrates why family names are insufficient units of comparison. The original anisotropic proposal and later non-projectable/healthy extensions are materially different constructions \cite{Horava2009,BlasPujolasSibiryakov2010}. A UV trajectory or renormalizability result in one branch cannot automatically establish the infrared gravitational status of another. Even within one branch, a high-energy flow and a low-energy extra-mode observable can arise in distinct truncations or normalizations.

The current benchmark therefore places Hořava gravity in C1 under the deterministic primary-blocker rule. Before a parent-family residual can be interpreted, projectable and non-projectable/BPS branches require separate disposition or an explicit equivalence/scope argument. A terminal branch comparison additionally requires a same-realization UV-to-IR path through the relevant lower-derivative operators and normalized scalar/tensor observables.

The point is not that branch diversity is a defect. It is that a family-level statement must specify the domain over which it quantifies. This is a direct physical instance of Proposition 1.

### 5.5 Higher-derivative gravity: prescription-sensitive family scope

Perturbatively renormalizable higher-derivative gravity provides another C1 example. The classical action-level addition of curvature-squared terms can improve ultraviolet behavior and yields the classic perturbative renormalizability result \cite{Stelle1977}. But action-level pole structure does not by itself fix a unique quantum interpretation when materially different pole or quantization prescriptions are used.

The benchmark therefore separates common action-level structure from branch-specific physical observables. A result can be meaningful and even terminal within a fixed prescription while remaining insufficient for the parent family. Family closure requires either terminal disposition of the material prescriptions or an explicit equivalence/exhaustion result, followed by a fixed-branch same-realization observable/comparator/error package.

Again, the benchmark is not converting unresolved prescription questions into negative evidence. It is preventing a local result from acquiring a broader quantifier domain than the source supports.

### 5.6 Causal Fermion Systems: absence of the requested correction object

Causal Fermion Systems illustrates a narrower C4 obstruction. The literature supplies continuum-limit gravitational structures, and recent work treats curved spacetimes and recovers coupled Einstein–Dirac behavior under the construction's assumptions \cite{Finster2021CFS,FischerFinster2026}. Thus the current KMQGB blocker is not “absence of gravity.”

The Paper-IV terminal question is more specific. To construct the requested beyond-baseline common-domain residual, the benchmark needs an explicit normalized gravity correction tensor or coefficient with its comparator and errors. At the current authority state that particular object is not available at the required level.

The correct result is therefore neither a zero correction nor exclusion. The beyond-baseline residual remains undefined until the correction object is supplied. This case demonstrates why the primary-obstruction taxonomy retains a distinct explicit-correction class instead of merging every open row into a generic transport problem.

### 5.7 Other families and recurrence of the same structural obstacles

The remaining families reinforce the same architecture rather than generating a flat list of unrelated failures. Causal-set and triangulation programmes possess significant continuum or semiclassical information \cite{BombelliLeeMeyerSorkin1987,BenincasaDowker2010,AmbjornJurkiewiczLoll2004,AmbjornJurkiewiczLoll2005}, but the benchmark still requires a fully specified physical scale/observable chain before a family-level common residual is admitted. String/M-theory and holographic constructions contain powerful exact or dual descriptions in particular settings \cite{Maldacena1997}; the obstacle is promoting such scoped constructions across material compactification and duality sectors without an exhaustion or reduction proof. Group-field theory supplies controlled condensate cosmologies \cite{GielenOritiSindoni2013,GerhardtOritiWilsonEwing2018}, while independent branches still require continuum-to-gravity observable closure after reducible spin-foam content is separated.

Noncommutative spectral geometry provides a rich spectral-action gravity programme \cite{ChamseddineConnes1997,ChamseddineConnesMarcolli2006}, but the family-level quantum comparison requires an explicit dynamical/renormalization/threshold-to-observable chain. Quantum Graphity gives an explicit dynamical-graph geometrogenesis model with an ordered local low-energy phase \cite{KonopkaMarkopoulouSeverini2008}; the terminal gravity question additionally asks for same-Hamiltonian continuum Lorentzian Einstein spin-2 dynamics and a normalized comparator-ready observable. Wheeler–DeWitt geometrodynamics begins from the canonical quantum constraints of gravity \cite{DeWitt1967Canonical}, but the requested family-level observable additionally depends on physical-state, clock, constraint and relational-observable closure.

These examples explain why the obstruction map should be read as a topology of comparison requirements rather than a ranking of theoretical merit.

---

## 6. Global decision gates

The Paper-IV decision is staged so that theory-selection language cannot be reached before the comparison problem itself is closed. The latest D7 readiness snapshot used for this draft is Iter276 and reports:

- **D1 / D7-S0 — frozen judge integrity:** PASS;
- **internal saturation / D7-S1:** PASS;
- **D2A / D7-S2 — strict Tier-1 terminal coverage:** NOT_CLOSED, with \(1/15\) strict terminal rows;
- **D2B / D7-S3 — same-realization object completeness:** NOT_CLOSED;
- **D3 — common-domain comparability:** PARTIAL;
- **D4 / D7-S4 — global comparator-subtracted matrix:** PARTIAL_GLOBAL_NOT_CLOSED;
- **D5 — missing-object quarantine:** PASS;
- **D6 — same-realization discipline:** PASS_RULE_TARGETS_OPEN;
- **D7-S5 — global outcome classifier:** NOT_AUTHORIZED;
- **D7-S6 — Candidate Gravity activation export:** INACTIVE.

Consequently the global classifier is not authorized to return any of the eventual terminal outcomes

\[
\{\texttt{EXISTING\_SUFFICIENT},\ \texttt{ADAPT\_EXISTING},\ \texttt{HYBRID\_REQUIRED},\ \texttt{NEW\_REQUIRED}\}.
\]

This is a scientific result of the comparison protocol, not a missing manuscript conclusion. A global theory-selection statement would currently require promoting family-incomplete or undefined evidence, in direct conflict with Proposition 1 and the coverage contract.

The Iter275–276 RQCP update is particularly informative. The newly promoted parent increased the number of nonterminal rows but did not change the global classifier. This is exactly what should occur if the judge is independent of outcome: coverage changes the set being judged, while terminality continues to be evaluated by the same rules.

The Iter276 synchronization itself is marked in the repository as pending fresh validation. This draft therefore treats the numerical coverage and D7 states as the current working scientific snapshot but does not represent the Iter276 repository synchronization as a final archival release. That implementation qualification is expected to disappear from the submission manuscript once an immutable validated release is frozen.

---

## 7. Discussion

### 7.1 What has been learned without selecting a global winner

The most immediate conclusion is that the present difficulty of cross-framework quantum-gravity comparison is structured. Fourteen nonterminal rows are not fourteen identical failures and are not fourteen exclusions. Their primary blockers recur in a small set of comparison layers.

The robustness analysis changes the strongest quantitative statement relative to the first manuscript draft. It is not defensible to treat the exact split between family-scope and transport blockers as uniquely physical; reasonable tie-breaking moves individual rows between C1 and C2. What remains stable is their combination. In all bounded projections considered here, \(11/14\) nonterminal rows are blocked at family scope and/or same-realization transport before a terminal family-level residual is numerically evaluable.

This suggests a practical shift in emphasis. For many frameworks, the next decisive question is not whether a smaller uncertainty can be obtained for an already-defined number. It is whether the claimed parameter, observable and physical state can be transported from the framework-native construction into the same domain as the comparator without changing the parent theory or silently combining incompatible realizations.

The remaining three classes show why a single “transport” label would still be too coarse. Asymptotic safety is unusually close to a direct Lorentzian scattering package under the chosen criterion. CFS isolates an explicit correction-object requirement. Wheeler–DeWitt geometrodynamics isolates the physical-state and relational-observable problem. Preserving these differences makes the benchmark more useful as a research map.

### 7.2 Relation to quantum-gravity phenomenology

Quantum-gravity phenomenology asks how theoretical effects can be connected to observables, experiments and multi-messenger data \cite{AddaziEtAl2022,AlvesBatistaEtAl2025}. KMQGB addresses a preceding inference question: when a theoretical object is associated with a phenomenological signature, is its theory ancestry sufficiently specified to compare it with another framework's object in the same domain?

The two programmes are complementary. A phenomenological roadmap can identify high-value observables and experimental channels. A same-realization benchmark identifies which theory-side objects must be supplied before those channels support a parent-family comparison. In this sense, the obstruction matrix is a theory-side completion map for future phenomenology rather than a replacement for experimental discrimination.

### 7.3 BLOCKED as an informative scientific state

A blocked state can be more informative than a forced binary answer because it records the exact object whose appearance would alter the decision. The asymptotic-safety row can be reopened by a stable public contact-complete Lorentzian package satisfying a predeclared set of conditions. The LQG/spinfoam row can be advanced by a same-realization microscopic-to-continuum-to-IR observable and parameter-transport certificate. The CFS row can be advanced by a normalized beyond-baseline correction object. RQCP can be advanced by an all-band/background-independent family-level gravity bridge or an explicit equivalent construction.

This creates a prospective interface with new literature. A new paper does not require reinterpretation of the old scoring rules. It either satisfies part of a recorded reopen condition or it does not. The Iter273–276 sequence provides three qualitatively different examples: a strong UV/continuum result in LQG narrows a transport blocker; contact-term progress in asymptotic safety narrows an amplitude blocker; and RQCP adds a new parent to the census under a pre-existing promotion rule.

### 7.4 Prospective coverage and resistance to selection bias

The RQCP event strengthens the methodological case for a prospectively extensible census. Any finite list of quantum-gravity programmes risks becoming stale. A benchmark can react in two ways: freeze the list permanently and risk omission bias, or define in advance what properties cause a new proposal to enter the comparison set. KMQGB adopts the second approach.

The important feature is that the promotion rule existed before RQCP was classified. The new row therefore does not arise from a post hoc desire to change the conclusion. Indeed, its addition makes the terminal fraction smaller. This provides an internal prospective check against one form of selection bias: candidates are not excluded merely because they worsen a summary metric.

The same rule must remain conservative. Generic labels or conceptual similarities should not multiply rows without a distinct physical parent. Conversely, an explicit reduction or equivalence map should prevent double counting. The census is therefore intended to be extensible but not arbitrary.

### 7.5 Algebraic consistency is weaker than physical composability

The LQG case makes another distinction explicit. It is possible to derive a mathematically closed network of parameter relations from adjacent external results and still lack the physical map needed to compose them. The identities involving \(q\), \(\rho\), \(\Delta_\gamma\), \(\gamma\) and \(\psi\) are internally consistent, and executable controls verify their algebraic equivalence. Yet the microscopic EPRL, area-metric RG and inflationary EFT objects remain adjacent authorities until a same-realization ancestry and scale-transport theorem or calculation is supplied.

This is not a weakness unique to loop quantum gravity. It is a general warning for cross-regime theory synthesis: mathematical compatibility between equations is necessary but not sufficient evidence that the equations describe the same physical realization.

### 7.6 Why heavy computation is not automatically the next step

Many quantum-gravity programmes are computationally intensive, but the benchmark distinguishes numerical from structural blockers. If the missing element is a scale map, physical normalization, parameter identity, branch equivalence, family exhaustion or same-realization provenance, greater numerical precision in an adjacent calculation cannot define the absent object. Heavy computation becomes justified when the numerical task is prospectively specified and can change a terminal disposition.

The RQCP audit illustrates the positive side of this rule. Repeatedly recomputing an already stable fixed-band construction would not close its all-band/background-independent family blocker. The useful computation was instead a bounded cross-environment reproducibility test that could determine whether the scoped evidence itself was stable. Once that passed, further repeated runs were deprioritized.

### 7.7 Implications for future theory construction

The benchmark does not presently establish that a new theory of quantum gravity is required. That conclusion would be especially sensitive to coverage bias if unresolved frameworks were counted as failures. The D7 gate forbids this shortcut.

Nevertheless, the obstruction topology can inform future model construction. Any proposed new, adapted or hybrid model seeking stronger comparative status should address from the outset the recurring closure requirements identified here: material branch scope, same-realization UV/continuum-to-observable transport, physical normalization, comparator definition, state/relational closure and propagated uncertainties. Paper IV therefore supplies design constraints without activating a Candidate Gravity programme.

---

## 8. Limitations

Several limitations are substantive and must remain visible.

First, the fifteen-family census is a declared and prospectively extensible benchmark scope, not a proof that every possible theory of quantum gravity belongs to exactly one row. The RQCP promotion demonstrates that the census can change when a genuinely independent parent is identified. Future additions or valid reductions remain possible.

Second, the maturity of the external evidence is uneven. Some families possess direct Lorentzian, weak-field or scattering observables; others remain closer to microscopic, continuum or structural results. KMQGB does not interpret unequal maturity as unequal truth probability.

Third, the primary-obstruction topology is a projection of a richer ledger. A family may possess several simultaneous blockers. The exact C1/C2 split changes under reasonable tie-breaking, and the five classes must not be presented as universal failure modes of quantum gravity. The robust current statement is the combined structural share \(11/14\) under the tested projections.

Fourth, Proposition 1 is a formal consequence of the declared decision semantics, not a novel theorem of statistics or a fundamental no-go theorem of quantum gravity. Its contribution is operational and physical: it is coupled to explicit realization, comparator and family-scope objects. A deeper prior-art audit should precede any stronger priority language.

Fifth, the LQG adapter contains derived algebraic identities that must be distinguished from directly published source equations. The current attribution audit makes this separation explicit, but the physical EPRL-to-area-metric-to-EFT same-realization bridge remains open.

Sixth, several high-value rows depend on external calculations or reproducibility objects. The asymptotic-safety contact-complete package, the LQG physical UV-to-IR observable bridge, the explicit normalized CFS correction object, and the RQCP all-band/background-independent family bridge remain open at the current snapshot.

Seventh, the current manuscript is prepared against an Iter276 D7 readiness state whose synchronization validation is still marked pending. Before submission, all article claims must be frozen against a validated immutable release, and the stale recovery-front pointer must be synchronized or superseded.

Finally, operational saturation is not scientific closure. The paired metrics remain explicit: operational proving-ground readiness is 100%, strict family-terminal coverage is \(1/15\), fourteen candidate rows remain nonterminal, and the global D7 classifier is unauthorized.

---

## 9. Conclusion

We have applied a frozen observable/comparator decision architecture to a prospectively extensible quantum-gravity census. In the current snapshot the Known Models / Quantum Gravity Benchmark contains fifteen Tier-1 families. The benchmark is operationally saturated with respect to available internal work but scientifically nonterminal: only the General Relativity plus controlled low-energy effective-field-theory baseline is strict terminal at family scope, while fourteen candidate families remain partial or blocked.

Two structural results emerge. First, under the frozen semantics, scoped evidence cannot be promoted to parent-family sufficiency or exclusion while material branches or required same-realization/common-domain residuals remain unresolved. Second, the fourteen current nonterminal rows map, under a deterministic primary-blocker projection, to five recurring current classes. The exact division between family-scope and same-realization transport is projection-dependent, but their combined dominance is stable across the bounded alternatives tested here at \(11/14\). Most current nonterminality therefore arises before a terminal family-level numerical residual is defined.

Three prospective cases show how the protocol responds to scientific progress. New Lorentzian loop/spinfoam fixed-point evidence strengthens a previously incomplete UV/continuum chain without silently establishing infrared observable ancestry. New asymptotic-safety contact-term progress directly attacks a frozen amplitude blocker without becoming terminal before a stable public contact-complete package exists. A newly identified RQCP parent is admitted to the census by a pre-existing promotion rule, lowering the terminal fraction rather than being omitted to preserve the earlier denominator.

The present benchmark does not establish that all known quantum-gravity frameworks fail, nor does it establish that a new theory is required. Its contribution is to state what would have to be true before such a global conclusion becomes physically meaningful. By separating defined residuals from missing family scope, theory ancestry, transport, normalization, comparator and state objects, the framework turns incompleteness into an auditable set of proof obligations rather than an implicit negative result.

---

## Data and code availability

The benchmark protocols, framework audits, executable controls, machine-readable decision ledgers and reproducibility machinery are maintained in the public `Known-Models-Quantum-Gravity-Benchmark` repository. The article-facing evidence matrix distinguishes externally established facts, KMQGB-derived relations, executable reproductions, open blocked objects and forbidden overclaims. A deterministic release bundle and manifest are used to freeze the minimum authority set for reproducibility. The submission version should cite a tagged immutable release and archival DOI rather than a moving branch.

## Author contributions

[To be completed after the author list is frozen.]

## Conflict of interest

[To be completed for submission.]

## Acknowledgements

[To be completed.]

---

## Figure and table plan for v1.2

**Figure 1 — Frozen comparison architecture.** Framework-native object → adapter → same-realization gate → common observable/comparator → terminal/partial/BLOCKED state, with the firewall preventing outcome-dependent modification of RQIR Core.

**Figure 2 — Current primary-obstruction topology.** Fourteen nonterminal families mapped to C1–C5, with the baseline \((5,6,1,1,1)\) and a visual emphasis on the robust aggregate C1+C2 = \(11/14\), rather than on the projection-dependent five-versus-six split.

**Figure 3 — Prospective census expansion.** Historical Iter274 14-row census → pre-existing promotion rule → RQCP audit → Iter275/276 15-row census; terminal rows remain one. This figure should make the anti-selection-bias property visually explicit.

**Figure 4 — D7 decision ecology.** D7-S0 and S1 closed; D7-S2 and S3 open; D7-S4 partial; D7-S5 unauthorized; D7-S6 inactive.

**Table 1 — Fifteen-family benchmark matrix.** Included in this draft; submission version requires direct primary citation support for every exact blocker statement.

**Table 2 — Claim/evidence matrix.** Compact article-facing form to be placed in an appendix or supplementary material.

---

## Draft-control status

- Full v1.1 manuscript architecture: complete.
- Census: updated prospectively from historical 14-family Iter274 to current 15-family Iter275/276.
- Abstract: updated to the 15-family state.
- Core methods prose: second full pass.
- Proposition 1: retained with explicit non-priority qualification and partial-identification context.
- Fifteen-family result table: complete first pass with primary family anchors.
- Obstruction topology: corrected deterministic assignments and robustness result \(11/14=78.6\%\).
- LQG case: equation attribution and sign convention cleaned; algebraic consistency separated from physical same-realization closure.
- Asymptotic-safety case: Iter274 contact-term near miss incorporated.
- RQCP case: Iter275 promotion, scoped result and cross-environment reproducibility logic incorporated.
- Global D7 state: updated to Iter276, still `NOT_AUTHORIZED`.
- Primary blocker-sentence citation audit: incomplete; highest-priority literature task before submission.
- Figures: specified but not yet rendered.
- IOP/CQG LaTeX formatting: not yet converted.
- Immutable archival release/DOI: not yet frozen.
- Submission authorization: NOT YET; scientific D7 state remains independent of manuscript completeness.
