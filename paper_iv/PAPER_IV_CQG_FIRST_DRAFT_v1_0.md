# RQIR Paper IV — First Full Draft v1.0

**Target journal:** Classical and Quantum Gravity  
**Article type:** Research Paper  
**Draft snapshot:** 2026-09-11, KMQGB through Iter274  
**Submission status:** WORKING DRAFT / NOT YET SUBMISSION-AUTHORIZED

# Frozen-observable benchmarking across quantum-gravity frameworks: same-realization closure and global decision gates

**Authors:** [to be finalized]  
**Affiliations:** [to be finalized]

## Abstract

Comparisons between quantum-gravity frameworks are frequently assembled from calculations performed in different states, signatures, truncations, normalizations, scales and observable definitions. A disagreement between two such calculations is therefore not automatically a physical disagreement, while agreement may be equally non-diagnostic if the compared quantities do not belong to a common physical realization. We introduce the Known Models / Quantum Gravity Benchmark (KMQGB), an application of the frozen Relativity–Quantum Interface Reconstruction (RQIR) Core v1.0 to a declared census of fourteen major quantum-gravity framework families. Framework-native objects are mapped into a common observable/comparator language while model-dependent retuning of the comparison rules is forbidden. The protocol requires explicit same-realization provenance, family-scope closure and common-domain comparators; missing theory, transport, normalization, observable or uncertainty objects are preserved as non-exclusion states rather than converted into negative residuals. The benchmark is operationally saturated, with zero unresolved Tier-2 classifications and no remaining internally actionable family fronts, but strict family-level scientific closure is only one of fourteen rows. The thirteen nonterminal rows reduce, under a primary-obstruction projection, to five recurring classes: family/branch-scope incompleteness, ultraviolet-to-infrared or continuum-to-observable transport gaps, amplitude/comparator incompleteness, absence of an explicit beyond-baseline correction object, and physical-state/relational-observable closure. We formulate a protocol-level no-promotion proposition showing that a scoped result cannot entail a family-level sufficiency or exclusion statement while a material branch or required same-realization residual remains undefined. Recent positive developments in loop/spinfoam gravity and asymptotic safety illustrate that new physical results can narrow a blocker without changing the frozen judge or forcing premature theory selection. The present global classifier therefore remains unauthorized to select an existing, adapted, hybrid or new quantum-gravity theory. KMQGB instead supplies an auditable map of the proof obligations required for such a comparison to become physically meaningful.

**Keywords:** quantum gravity; gravitational observables; theory comparison; loop quantum gravity; asymptotic safety; effective field theory; reproducibility; same-realization closure

---

## 1. Introduction

Quantum gravity is represented by a heterogeneous collection of research programmes rather than a single model class. Perturbative and higher-derivative gravities, asymptotic safety, nonlocal gravity, string and M-theory, holographic constructions, loop quantum gravity and spinfoams, causal sets, dynamical triangulations, group-field and tensor models, causal fermion systems, spectral approaches, canonical Wheeler–DeWitt quantization and emergent graph models differ not only in their microscopic assumptions but also in the physical objects they compute. Modern reviews, maps of the field and phenomenological roadmaps accordingly organize the landscape by theoretical programme, cosmological signature, experimental channel or possible relation between approaches \cite{Barrau2017,MielczarekTrzesniewski2018,AddaziEtAl2022,BambiModestoShapiro2024,AlvesBatistaEtAl2025}.

The present work addresses a complementary problem. Before asking which quantum-gravity framework is favored by an observation, or even whether two frameworks disagree with one another, one must establish that the compared quantities are physically comparable. A ultraviolet fixed point, a spin-foam amplitude, a lattice observable, a spectral action, a relational cosmological perturbation and a low-energy scattering amplitude are not automatically members of one comparison space merely because each is associated with gravity. They may differ in state, signature, boundary conditions, regulator, truncation, normalization, source routing, response order or scale-setting prescription. A chain built from adjacent results in the literature may therefore fail before any numerical residual is defined.

This distinction matters because incompleteness can otherwise be mistaken for falsification. Consider three generic situations. First, a framework may possess a controlled ultraviolet construction but lack a same-realization trajectory to a normalized low-energy observable. Second, a successful calculation may apply only to one material quantization or prescription branch and therefore not determine the status of the entire framework family. Third, a numerical or analytic observable may be available but its comparator may use a different state, response order or normalization. In each case the correct outcome is not a conventional PASS or FAIL. The comparison itself is incomplete.

Relativity–Quantum Interface Reconstruction (RQIR) was developed to make such distinctions explicit. In the present paper we apply its frozen Core v1.0 to known quantum-gravity frameworks through the Known Models / Quantum Gravity Benchmark (KMQGB). The benchmark-facing pipeline is

\[
\text{framework-native object}
\longrightarrow \text{framework adapter}
\longrightarrow \text{frozen observable/comparator domain}
\longrightarrow \text{terminal, partial or blocked state}.
\]

The core comparison rules are frozen before framework outcomes are interpreted. Framework-specific adapters may translate variables and conventions, but they may not alter the judge to rescue or reject a difficult model. Adjacent literature results may be composed only after a same-realization map has been established. A missing physical object remains missing: it is not assigned a zero residual and is not counted as exclusion evidence.

The contribution is therefore not a new catalogue of quantum-gravity approaches. Broad comparative maps and phenomenological roadmaps already exist \cite{MielczarekTrzesniewski2018,AlvesBatistaEtAl2025}. Instead, we execute a fixed decision protocol across a declared fourteen-family census and ask a narrower question: under what conditions do results from different programmes constitute statements about the same gravitational observable? A recent controlled same-family construction likewise emphasizes the importance of fixed comparison conditions \cite{Xu2026}; here the scope is different, because the object of study is a multi-family comparison under a common frozen decision architecture.

Three results organize the paper. First, the fourteen-family benchmark reaches operational saturation while remaining scientifically nonterminal: all Tier-2 classification questions are resolved and no internally executable family front remains, yet only the General Relativity plus controlled low-energy effective-field-theory row is terminal at strict family scope. Second, the thirteen nonterminal rows exhibit a compressed obstruction topology. When each row is projected onto its current primary terminal blocker, the obstacles fall into five recurring classes rather than thirteen unrelated failures. Third, we formulate a protocol-level no-promotion proposition: if a material family branch is unresolved or a required same-realization/common-domain residual is undefined, then a scoped PASS or FAIL cannot entail a family-level sufficiency or exclusion statement under the frozen coverage contract. This result is decision-theoretic rather than a no-go theorem about the underlying physics, but it makes explicit why more precision cannot repair a missing physical map.

Recent developments provide useful stress tests. A 2026 Lorentzian EPRL/KKL summed-spinfoam fixed-point result materially strengthens the loop/spinfoam ultraviolet side of the comparison, yet does not by itself establish the required same-realization ultraviolet-to-infrared gravitational observable chain. In asymptotic safety, a 2026 archival Lorentzian scalar-scattering calculation is a strong positive control, while a September 2026 conference report directly attacks the previously missing contact contribution. The family remains nonterminal because the public reproducible contact-complete same-realization package required by the pre-frozen criterion is not yet available. These cases show why a frozen protocol is useful: scientific progress changes the evidence state without changing the standard by which evidence is admitted.

The paper is organized as follows. Section 2 defines the benchmark architecture and family census. Section 3 formalizes realization and comparator closure and states the no-promotion proposition. Section 4 presents the fourteen-family result matrix and the five-class obstruction topology. Section 5 develops representative physical case studies. Section 6 reports the current global decision-gate state. Section 7 discusses the implications for comparative quantum gravity and phenomenology. Section 8 states the limitations, and section 9 concludes.

---

## 2. Frozen comparison architecture

### 2.1 Independent judge and framework adapters

The central governance choice is to freeze RQIR Core v1.0 before the Paper-IV framework outcomes are interpreted. This prevents an otherwise subtle form of circularity. If a framework-specific calculation cannot satisfy an observable or comparator requirement, the requirement is not weakened merely to obtain a terminal row. Conversely, a successful result in one subfamily does not enlarge its own scope after inspection.

The frozen core does not imply that all frameworks must use identical microscopic variables. A framework adapter is allowed, and in practice required, to convert a native calculation into the declared comparison language. An adapter may document a change of variables, convention translation, normalization, scale transport, observable extraction or explicit reduction map. What it may not do is alter the logical meaning of terminality, same-realization identity or a defined residual.

This separation creates a firewall:

\[
\text{framework outcome} \not\rightarrow \text{redefinition of the judge}.
\]

If a genuine defect in the core were demonstrated, it would require independent change control. A blocked comparison is not, by itself, evidence that the core is defective.

### 2.2 Declared framework census

The major-framework coverage contract uses a fourteen-row Tier-1 census. Its broad coverage is anchored to the modern quantum-gravity literature, with additional independent programmes promoted when they possess a distinct quantum parent and gravity/emergence claim \cite{BambiModestoShapiro2024}. The rows are:

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
14. quantum graphity / explicit dynamical-graph geometrogenesis.

The census is not claimed to be an ontological partition of every idea called quantum gravity. It is a declared comparison contract. Additional concrete parents can be promoted when they are materially independent. Conversely, a Tier-2 label can be reduced to an existing row only through an explicit ancestry or reduction map. At the current snapshot, the Tier-2 unresolved count is zero.

### 2.3 Family scope

A family is not interchangeable with a single calculation. Let a family \(F\) possess a set of material branches \(B_F=\{b_1,\ldots,b_n\}\), where a branch may be distinguished by quantization prescription, compactification, state sector, continuum phase, truncation class or another physically material choice. A result for \(b_i\) can be promoted to the family only if at least one of the following is established:

- all material branches relevant to the claim have terminal dispositions;
- a theorem establishes an equivalence class;
- an explicit reduction map merges the branch into another row;
- a scope proof shows that the branch lies outside the declared Paper-IV target.

This rule is symmetric. A scoped FAIL cannot exclude a parent family, and a scoped PASS cannot establish family-wide sufficiency.

### 2.4 Evidence classes

For article-facing use, KMQGB distinguishes six evidence states:

- **ESTABLISHED_EXTERNAL:** established by an external publication or public data/programme authority within its actual scope;
- **DERIVED_KMQGB:** analytically derived inside KMQGB from declared inputs and frozen assumptions;
- **REPRODUCED_EXECUTABLE:** reproduced by a stable executable control;
- **OPEN_BLOCKED:** a required theory, provenance, transport, observable, normalization, comparator or uncertainty object is absent or non-composable;
- **HYPOTHESIS_ONLY:** exploratory content that has not met promotion obligations;
- **FORBIDDEN_OVERCLAIM:** a proposed statement incompatible with the evidence state.

The decisive semantic rule is

\[
\boxed{\mathrm{BLOCKED}\neq \mathrm{FAIL}}.
\]

A blocked row can contain highly informative positive physics. Its status says that the current evidence does not define the family-level comparison requested by the benchmark.

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
M_{12}:\mathcal{R}_1\rightarrow \mathcal{R}_2
\]

must preserve the physical identities required by the intended claim. When a parameter in one layer is said to be the same parameter as one in another layer, the ancestry or transport relation is part of the evidence, not a convention that can be inserted after comparison.

### 3.2 Common observable/comparator domain

Let a framework prediction in a realization \(\mathcal{R}\) be represented by an observable object

\[
O_F(\mathcal{R};x),
\]

where \(x\) denotes the physical kinematic, geometric or scale variables. Let \(O_C\) be the comparator. A residual is admitted only when the domain-matching map \(\Pi\) is defined:

\[
\Delta_F(x)=\Pi[O_F](x)-O_C(x).
\]

The map \(\Pi\) includes the response order, state/background, normalization, source routing, contact/amputation convention and uncertainty treatment required by the claim. If \(\Pi[O_F]\) is undefined, then \(\Delta_F\) is undefined. KMQGB does not substitute \(\Delta_F=0\), does not infer agreement, and does not infer disagreement.

This is particularly important for cross-regime comparisons. An ultraviolet trajectory and an infrared observable may each be well defined independently while their composition is not. The missing object is then the transport map, not additional decimal precision.

### 3.3 Terminality

A scoped realization is terminal for an article-facing comparison only when the required physical object, same-realization provenance, common-domain comparator and error/uncertainty objects are defined to the level declared by that comparison. A family is terminal only when the family-scope rule in section 2.3 is also closed.

Accordingly, three conceptually different outcomes must be kept separate:

1. **defined terminal comparison**, for which a residual or equivalence statement has physical meaning;
2. **scoped result**, for which the local calculation is meaningful but the family scope is incomplete;
3. **blocked comparison**, for which a required object or composition map is missing.

### 3.4 Proposition: no promotion under incomplete realization closure

**Proposition 1 (protocol-level no-promotion).** Let \(F\) be a Tier-1 framework family with material branches \(B_F\). Under the frozen Paper-IV coverage contract, a scoped PASS or FAIL result for a subset \(B'\subset B_F\) does not entail a family-level sufficiency or exclusion statement if either (i) at least one material branch in \(B_F\setminus B'\) lacks a terminal disposition or valid reduction/scope proof, or (ii) any physical residual required for the family-level claim is undefined because the same-realization/common-domain map is incomplete.

**Proof.** A family-level statement quantifies over the material domain declared for \(F\). In case (i), the evidence constrains only \(B'\), while at least one material branch remains admissible under the coverage contract. Promoting the scoped result would therefore add an unproved premise about the unresolved branch. In case (ii), the family-level predicate depends on a residual that is not defined in the comparison domain. Assigning a sign, magnitude or zero value to that residual would add information not contained in the evidence. In either case the family-level statement is not entailed by the admitted evidence. The frozen contract therefore permits only a partial or blocked status. \(\square\)

This proposition is deliberately modest. It is not a theorem that any quantum-gravity family is correct or incorrect, and it is not a fundamental no-go theorem. It is a logical consequence of the predeclared comparison semantics.

**Corollary 1 (precision cannot repair structural undefinedness).** If a terminal blocker is the absence of a same-realization map, physical observable, normalization identity or comparator definition, reducing numerical uncertainty within an adjacent but non-composable calculation cannot by itself make the family-level residual defined.

The corollary explains the current heavy-compute disposition of the benchmark. Numerical work becomes high value only after a prospectively frozen numerical task can change a terminal classification.

---

## 4. Results: the fourteen-family benchmark

### 4.1 Global result matrix

Table 1 summarizes the current family-level state. `PARTIAL_SUBFAMILY_ONLY` means that scientifically meaningful child results exist but family scope is not closed. `BLOCKED_MISSING_REQUIRED_OBJECT` means that a required physical or attribution object is absent at the terminal comparison level. Neither status is an exclusion.

| Family | Current state | Primary terminal obstruction at current snapshot |
|---|---|---|
| GR + controlled low-energy gravitational EFT | `BENCHMARKED_COMPLETE_REALIZATION` | Terminal baseline comparator in the declared low-energy domain. |
| Perturbative renormalizable / higher-derivative gravity | `PARTIAL_SUBFAMILY_ONLY` | Material quantization/prescription branches require independent disposition or equivalence/exhaustion plus a fixed-branch normalized observable/comparator package. |
| Hořava–Lifshitz gravity | `PARTIAL_SUBFAMILY_ONLY` | Projectable and non-projectable/BPS branches cannot inherit status; complete same-realization UV-to-IR extra-mode observable/renormalization chain is missing. |
| Asymptotic Safety | `BLOCKED_MISSING_REQUIRED_OBJECT` | Contact-complete public reproducible Lorentzian \(s+t+u+A_4\) scattering package with forward-limit treatment, uncertainty control and same-domain comparators is not yet frozen. |
| Nonlocal / infinite-derivative gravity | `PARTIAL_SUBFAMILY_ONLY` | Material functional-form/causality branches and cross-order/full-momentum rigidity are not exhausted at family scope. |
| String / M-theory / holographic gravity | `PARTIAL_SUBFAMILY_ONLY` | Scoped amplitude controls do not close material compactification/duality branches or a same-realization compactification/moduli-to-4D observable/error chain. |
| Causal Set quantum gravity | `PARTIAL_SUBFAMILY_ONLY` | Fundamental measure/dynamics to manifoldlike 3+1 GR and a normalized genuinely causal-set gravitational observable remain incomplete. |
| Causal/Euclidean Dynamical Triangulations | `PARTIAL_SUBFAMILY_ONLY` | Multi-coupling continuum trajectory, scale setting, invariant observable and systematic-error capsule remain incomplete. |
| Loop Quantum Gravity / EPRL-spinfoam | `BLOCKED_MISSING_REQUIRED_OBJECT` | New Lorentzian continuum/fixed-point evidence strengthens the UV side, but the same-realization UV-to-IR/GR trajectory, physical observable, parameter/refinement transport and comparator/error certificate remain missing. |
| Group Field Theory / tensor models | `PARTIAL_SUBFAMILY_ONLY` | Reducible EPRL/FK-GFT content is separated from independent TGFT/condensate/tensor branches, whose continuum-to-gravity observable authority remains incomplete. |
| Causal Fermion Systems | `BLOCKED_MISSING_REQUIRED_OBJECT` | First explicit normalized beyond-GR gravity correction tensor/coefficient with a same-domain comparator is missing. |
| Noncommutative spectral geometry | `PARTIAL_SUBFAMILY_ONLY` | Spectral-triple to RG/threshold to low-energy observable and covariance transport is incomplete at family scope. |
| Canonical Wheeler–DeWitt geometrodynamics | `BLOCKED_MISSING_REQUIRED_OBJECT` | Full physical-Hilbert-space/state/clock/relational-observable/error certificate is missing. |
| Quantum Graphity / dynamical-graph geometrogenesis | `PARTIAL_SUBFAMILY_ONLY` | Same-Hamiltonian continuum Lorentzian Einstein spin-2 emergence and normalized observable certificate remain incomplete. |

The paired global metrics at the Iter274 snapshot are:

\[
N_{\rm Tier1}=14,\qquad N_{\rm terminal}=1,\qquad N_{\rm nonterminal}=13,
\]

\[
N_{\rm Tier2,unresolved}=0,\qquad N_{\rm internal\ actionable}=0.
\]

The operational proving ground is therefore saturated at 100%, while strict family-terminal scientific coverage remains \(1/14\). These quantities must not be conflated. Operational saturation states that the current public authority has been reduced to terminal objects or explicit external reopen conditions; it does not state that thirteen theories have failed.

### 4.2 Primary-obstruction topology

A second result appears when the thirteen nonterminal rows are projected onto the obstruction that currently prevents terminal promotion. The projection is not intended to assert that each family has only one difficulty. Several rows possess secondary obstacles. Instead, it identifies the present first terminal blocker in the frozen decision path.

We obtain five primary classes:

**Class A — family/branch-scope incompleteness (4 families).**  
Perturbative/higher-derivative gravity, nonlocal gravity, string/M-theory/holography and group-field/tensor models contain materially distinct branches for which a scoped result cannot yet stand for the parent family. The recurring problem is not simply lack of calculations; it is lack of a terminal exhaustion, equivalence or reduction structure at family scope.

**Class B — UV/continuum-to-IR observable transport (6 families).**  
Hořava–Lifshitz gravity, causal sets, CDT/EDT, LQG/spinfoams, noncommutative spectral geometry and quantum graphity possess meaningful microscopic, continuum, RG or weak-field ingredients, but the terminal chain to a common physical gravitational observable is incomplete. This is the largest class in the current snapshot.

**Class C — amplitude/comparator completeness (1 family).**  
Asymptotic safety has unusually direct Lorentzian scattering progress. Its current blocker is narrower: a public reproducible contact-complete same-realization amplitude with the required forward-limit, approximation/uncertainty and comparator closure.

**Class D — explicit beyond-baseline correction object (1 family).**  
Causal Fermion Systems has a continuum/gravity structure and systematic correction route, but the terminal object is an explicit normalized beyond-GR gravity correction tensor or coefficient in the comparison domain.

**Class E — physical-state and relational-observable closure (1 family).**  
Canonical Wheeler–DeWitt geometrodynamics has meaningful semiclassical observables, while the family-level terminal object additionally requires physical-Hilbert-space, clock/state, constraint and relational-observable closure.

Thus the thirteen nonterminal rows compress to the count vector

\[
(4,6,1,1,1)
\]

under the current primary-obstruction projection. This is useful because it replaces a flat list of open theories with a smaller set of recurring comparison problems. The dominant obstruction is not a universal contradiction with GR but incomplete transport from a framework-native object to a same-realization observable/comparator domain.

### 4.3 Why the nonterminal result is scientifically informative

The result above may appear conservative because it does not select a winning theory. Its scientific content is instead in the localization of what is missing. For each nonterminal row, the benchmark records a reopen condition precise enough that a future publication, calculation or data product can change the family status without redesigning the comparison procedure. This converts the statement “the framework is not yet comparable” into a falsifiable workflow claim: either the named object is supplied and the gate can be re-evaluated, or it is not.

The distinction also limits false certainty. In a conventional scorecard, absent data can silently become a zero, or a child calculation can be counted as representative of an entire programme. KMQGB prevents both moves. The price is a larger blocked region; the benefit is that terminal outcomes carry a stronger scope meaning.

---

## 5. Representative physical cases

### 5.1 Loop/spinfoam gravity: algebraic bridge constraints versus physical ancestry

The loop/spinfoam sector provides the most developed example of a distinction between an algebraically constrained bridge and a physically established bridge. KMQGB combines microscopic EPRL-related structure, area-metric/RG adjacent authority and an observable-facing parameterization without assuming in advance that the layers belong to one physical realization.

Within the adapter, the following relations have been derived and executable-tested:

\[
q=\frac{1}{\gamma}-\gamma-\Delta_\gamma,
\]

\[
\beta_\Delta=\beta_\rho-\left(1+\frac{1}{\gamma^2}\right)\beta_\gamma,
\]

and on the positive branch used by the area-metric mapping,

\[
\gamma=-\cot(4\psi).
\]

After common-scale transport this yields

\[
\Delta_\gamma=2\cot(8\psi)-q,
\]

and

\[
\beta_\Delta=-16\csc^2(8\psi)\,\beta_\psi-\beta_q.
\]

These equations are not a proof that the adjacent microscopic and continuum descriptions are the same realization. Their value is different: any proposed same-realization bridge using this parameterization must satisfy the induced identifiability and RG relations. In particular, a \(q\)-only observation is rank deficient in the pair \(\{\gamma,\Delta_\gamma\}\), so additional structure is required to identify the components separately.

The 2026 Lorentzian EPRL/KKL summed-spinfoam fixed-point result by Han materially strengthens the microscopic/continuum side of this programme. Under the frozen benchmark, however, it does not automatically close the row. The remaining proof obligation is a physical same-realization path from the ultraviolet/continuum construction through the appropriate infrared/GR regime to a normalized observable, including parameter/refinement ancestry and comparator/error control. This is a useful example of a positive scientific advance that narrows a blocker without being converted into family-level sufficiency.

### 5.2 Asymptotic safety: a high-value near miss in Lorentzian scattering

Asymptotic safety currently provides the clearest example of a blocker being attacked by new external work. Chiesa, Pawlowski and Reichert (2026) compute the full momentum dependence of the scalar–graviton three-point vertex within the functional renormalisation group, reconstruct a timelike/Lorentzian vertex, and obtain a graviton-mediated scalar-scattering amplitude and cross section with the expected low-energy GR behavior and controlled high-energy behavior. The archival calculation writes the complete amplitude schematically as

\[
\mathcal{A}=\mathcal{A}_s+\mathcal{A}_t+\mathcal{A}_u+\mathcal{A}_4,
\]

but explicitly omits the direct contact term \(\mathcal{A}_4\). That term is also relevant to the forward-limit treatment.

A September 2026 ERG conference contribution subsequently reports a gravitational contact contribution resummed directly in Lorentzian signature. This development directly targets the pre-existing KMQGB blocker and is therefore a high-information positive signal. Nevertheless, the current public authority is split: the stable archival calculation is reproducible but omits \(\mathcal{A}_4\), whereas the newer conference report indicates contact-term progress without yet supplying a stable public contact-complete same-realization package containing \(s+t+u+A_4\), forward-limit/crossing treatment, an approximation and uncertainty budget, reproducibility material and same-domain comparators.

The row therefore remains `BLOCKED_MISSING_REQUIRED_OBJECT`. This is not a judgment against asymptotic safety. It is a demonstration that the frozen standard does not move when a promising result appears. If the missing archival package is released, the row can be reopened immediately against the same criterion.

### 5.3 Hořava–Lifshitz gravity: branch non-inheritance

Hořava–Lifshitz gravity illustrates why family names are insufficient units of comparison. Projectable and non-projectable/BPS formulations are materially distinct. A ultraviolet renormalisation-group trajectory in one branch cannot establish the infrared gravitational status of the other. Even within one branch, a ultraviolet flow in marginal Lifshitz couplings and a low-energy scalar phenomenology result may come from distinct truncations and cannot be concatenated without a map through the relevant lower-derivative operators and normalization conventions.

The current benchmark therefore asks for a same-realization UV-to-IR chain including the extra scalar/tensor sector and an observable that can be normalized against the common comparator. Until this chain exists, a local ultraviolet success is retained as a scoped positive result rather than promoted to family sufficiency.

### 5.4 Higher-derivative gravity: prescription-sensitive family scope

Perturbative renormalizable and higher-derivative gravity supplies a different obstruction. Action-level pole structure does not uniquely determine a physical family result when materially different quantization or pole prescriptions are used. Fakeon, principal-value and other branches can alter the interpretation of additional poles and the associated causality/unitarity questions.

The benchmark therefore separates the common action-level structure from branch-specific physical observables. A result in one prescription can be terminal for that branch while the family remains `PARTIAL_SUBFAMILY_ONLY`. Family closure requires either terminal disposition of the material branches or an explicit equivalence/exhaustion result, together with at least one fixed-branch same-realization normalized observable and comparator package.

This case is a direct illustration of Proposition 1: a precise calculation in one branch does not license a parent-family verdict when the quantifier domain of the family contains unresolved material branches.

### 5.5 Causal Fermion Systems: absence of the requested correction object

Causal Fermion Systems has continuum/gravity authority and a systematic mechanism for generating corrections. The Paper-IV terminal question is more specific. To form the requested beyond-baseline comparator residual, the benchmark requires an explicit normalized gravity correction tensor or coefficient in the same observable domain as the comparator.

At the current authority state, that object is not available. The correct result is therefore not that the correction is zero, and not that CFS is excluded. The result is that the beyond-continuum gravitational residual requested by the benchmark is undefined until the correction object is supplied.

### 5.6 Additional families and the recurrence of the same obstruction classes

The remaining families reinforce the five-class structure rather than adding thirteen independent logical problems. Causal-set and triangulation programmes possess significant continuum or semiclassical information but require complete physical scale/observable transport. String/M-theory/holographic comparisons require careful family-scope treatment across material compactification and duality branches. Group-field/tensor models additionally require separation of content reducible to spin foams from independent continuum branches. Noncommutative spectral geometry requires a controlled chain from spectral data and running/threshold structure to the low-energy observable and covariance used in the comparator. Quantum Graphity requires same-Hamiltonian emergence of Lorentzian Einstein spin-2 dynamics rather than only geometrogenesis or propagation proxies. Wheeler–DeWitt geometrodynamics emphasizes a distinct obstruction: a semiclassical prediction can exist while physical-state, relational-clock and Dirac-observable closure remain incomplete at the family level.

These examples explain why the primary-obstruction topology should be read as a map of comparison architecture rather than a ranking of theoretical merit.

---

## 6. Global decision gates

The Paper-IV global decision is staged. At the current Iter274 snapshot the state is:

- **D1 — frozen judge integrity:** PASS;
- **D2A — strict Tier-1 terminal coverage:** NOT_CLOSED;
- **D2B — same-realization object completeness:** NOT_CLOSED;
- **D3 — common-domain comparability:** PARTIAL;
- **D4 — family-level comparator-subtracted matrix:** PARTIAL_GLOBAL_NOT_CLOSED;
- **D5 — missing-object quarantine:** PASS;
- **D6 — same-realization discipline:** PASS_RULE_TARGETS_OPEN;
- **D7 — global terminal decision:** NOT_CLOSED / NOT_YET_AUTHORIZED.

The D7 wrapper further separates the final path into stages. Frozen-judge integrity and internal saturation are closed, while strict terminal coverage, same-realization completeness and global comparability are not. Consequently the global classifier is not authorized to return any of the four eventual terminal outcomes

\[
\{\texttt{EXISTING\_SUFFICIENT},\ \texttt{ADAPT\_EXISTING},\ \texttt{HYBRID\_REQUIRED},\ \texttt{NEW\_REQUIRED}\}.
\]

This is a central result rather than a missing conclusion. A global theory-selection statement would currently require promoting undefined or family-incomplete evidence, in direct conflict with Proposition 1 and the frozen coverage contract.

The same logic keeps a prospective Candidate Gravity programme inactive. A new model is not activated simply because many existing rows are difficult to close. Activation would require an authorized global outcome after the relevant coverage and comparator conditions are satisfied.

---

## 7. Discussion

### 7.1 What has been learned despite the absence of a global winner

The most immediate conclusion from the benchmark is that the present difficulty of cross-framework quantum-gravity comparison is structured. The thirteen nonterminal rows are not thirteen identical failures and are not thirteen exclusions. They are dominated by a small number of recurring proof obligations.

The largest class is transport: a theory may have a meaningful ultraviolet, microscopic or continuum construction but still lack a controlled path to the physical observable required by a common comparator. This observation shifts attention from the existence of formal results to the ancestry of the observable itself. A prediction becomes useful for cross-framework inference only when its parameter identity, state, normalization and physical domain survive the transport.

The second broad difficulty is family scope. Quantum-gravity programmes often contain materially different branches. Treating one convenient branch as the whole theory can make a comparison appear more decisive than it is. The benchmark's branch non-inheritance rule is therefore not a penalty applied to diverse programmes; it is the cost of making a family-level statement have a defined quantifier domain.

The narrower obstruction classes are also informative. Asymptotic safety is currently close to a direct Lorentzian scattering object under the chosen criterion, making its blocker substantially different from a programme with no comparator-ready observable. CFS isolates the need for a specific correction object. Wheeler–DeWitt geometrodynamics isolates the physical-state/relational-observable problem. A useful comparison framework should preserve these differences rather than reduce them to a single numerical score.

### 7.2 Relation to quantum-gravity phenomenology

Quantum-gravity phenomenology asks how theoretical effects can be connected to observables, experiments and multi-messenger data \cite{AddaziEtAl2022,AlvesBatistaEtAl2025}. KMQGB addresses a preceding inference question: when a theoretical object is associated with a phenomenological signature, is its theory ancestry sufficiently specified to compare it with another framework's object in the same domain?

The two programmes are therefore complementary. A phenomenological roadmap can identify high-value observables and experimental channels. A same-realization benchmark can identify which theory-side objects must be supplied before those channels support a family-level comparison. In this sense, the obstruction table can be interpreted as a theory-side completion map for future phenomenology.

### 7.3 The role of BLOCKED states

A blocked state is often more scientifically useful than a forced binary answer. It records the exact object whose appearance would alter the decision. For example, the asymptotic-safety row can be reopened by a public contact-complete Lorentzian package satisfying a predeclared set of conditions. The LQG/spinfoam row can be advanced by a same-realization UV-to-IR physical observable and parameter-transport certificate. The CFS row can be advanced by an explicit normalized correction object.

This property also provides a natural response to new literature. A new paper does not require reinterpretation of the old scoring rules. It either satisfies part of a recorded reopen condition or it does not. The Iter273–274 developments show both possibilities: strong new physical evidence materially narrows the scientific gap while the terminal count remains unchanged because the remaining required object is explicit.

### 7.4 Why heavy computation is not automatically the next step

Many quantum-gravity programmes are computationally intensive, but the benchmark distinguishes numerical from structural blockers. If the missing element is a scale map, physical normalization, parameter identity, branch equivalence or same-realization provenance, greater numerical precision in an adjacent calculation cannot define the absent map. Heavy computation becomes justified when the numerical task is prospectively specified and can change a terminal disposition.

At the present snapshot, the global heavy-compute state is idle because the decisive open fronts are predominantly external theory, data, provenance or matching objects. This is an application of Corollary 1 rather than a general claim that numerical work in quantum gravity is unimportant.

### 7.5 Implications for future theory construction

The benchmark does not presently establish that a new theory of quantum gravity is required. That conclusion would be particularly sensitive to coverage bias: it could be generated artificially if unresolved frameworks were counted as failures. The D7 gate forbids this shortcut.

Nevertheless, the obstruction topology may be useful for future model construction. Any proposed new or hybrid model seeking a stronger comparative status should address, from the outset, the recurring failure modes identified here: material branch scope, UV-to-IR observable transport, physical normalization, comparator definition, state/relational closure and uncertainty propagation. In this sense, Paper IV produces design constraints without yet authorizing a Candidate Gravity model.

---

## 8. Limitations

Several limitations are substantive.

First, the fourteen-family census is a declared benchmark scope rather than a proof that every possible theory of quantum gravity belongs to exactly one row. The protocol contains promotion and reduction rules, but the census can evolve when genuinely independent parents are identified.

Second, the maturity of the external evidence is uneven. Some families possess direct Lorentzian or weak-field observables; others remain closer to microscopic, continuum or structural results. The benchmark does not interpret unequal maturity as unequal truth probability.

Third, a primary-obstruction projection is a compression of a richer ledger. A family can possess multiple simultaneous blockers. The five-class topology reported here identifies the current first terminal obstruction and should not be read as an exhaustive ontology of all problems in each programme.

Fourth, the no-promotion proposition is a theorem of the declared decision semantics, not a fundamental theorem of quantum gravity. Its physical usefulness depends on whether the frozen realization and comparator requirements capture the inference being attempted.

Fifth, several high-value rows remain dependent on external calculations or reproducibility objects. In particular, the loop/spinfoam same-realization infrared observable chain, the asymptotic-safety public contact-complete Lorentzian package and the explicit normalized CFS correction object remain open at the current snapshot.

Finally, operational saturation is not scientific closure. The paired metrics must remain explicit: operational proving-ground readiness is 100%, strict family-terminal coverage is \(1/14\), and the global D7 classifier remains unauthorized.

---

## 9. Conclusion

We have applied a frozen observable/comparator decision architecture to a declared fourteen-family quantum-gravity census. The resulting Known Models / Quantum Gravity Benchmark is operationally saturated but scientifically nonterminal. This separation is not a contradiction. It shows that a reproducible comparison procedure can exhaust the work permitted by current authority while refusing to manufacture physical residuals from missing objects.

Two cross-framework results emerge from the benchmark. First, scoped evidence cannot be promoted to a family-level sufficiency or exclusion statement while material branches or required same-realization/common-domain residuals remain unresolved. Second, the thirteen current nonterminal rows reduce, under a primary-obstruction projection, to five recurring classes dominated by family-scope incompleteness and ultraviolet/continuum-to-observable transport gaps. The comparison problem is therefore structured rather than a flat list of failed theories.

Representative cases show how the protocol behaves under real scientific progress. New loop/spinfoam fixed-point evidence strengthens a previously incomplete chain but does not silently establish infrared observable ancestry. New asymptotic-safety contact-term progress directly attacks a frozen blocker but does not become terminal until a public reproducible contact-complete package exists. In both cases the evidence changes while the judge does not.

The present benchmark does not establish that all known quantum-gravity frameworks fail, nor does it establish that a new theory is required. Its contribution is to state what would have to be true before such a global conclusion could be physically meaningful. By separating defined residuals from missing theory, transport, normalization and comparator objects, the framework turns incompleteness into an auditable set of proof obligations rather than an implicit negative result.

---

## Data and code availability

The benchmark protocols, framework audits, executable controls, machine-readable decision ledgers and reproducibility machinery are maintained in the public `Known-Models-Quantum-Gravity-Benchmark` repository. The article-facing evidence matrix distinguishes externally established facts, KMQGB-derived relations, executable reproductions, open blocked objects and forbidden overclaims. A deterministic release bundle and manifest are used to freeze the minimum authority set for reproducibility. A submission version should cite a tagged archival release/DOI rather than a moving branch.

## Author contributions

[To be completed after author list is frozen.]

## Conflict of interest

[To be completed for submission.]

## Acknowledgements

[To be completed.]

---

## References currently frozen in the CQG bibliography

- Barrau A 2017 *Testing different approaches to quantum gravity with cosmology: An overview*, Comptes Rendus Physique 18, 189–199.
- Mielczarek J and Trześniewski T 2018 *Towards the map of quantum gravity*, General Relativity and Gravitation 50, 68.
- Addazi A et al 2022 *Quantum gravity phenomenology at the dawn of the multi-messenger era—A review*, Progress in Particle and Nuclear Physics 125, 103948.
- Bambi C, Modesto L and Shapiro I (eds.) 2024 *Handbook of Quantum Gravity*, Springer.
- Alves Batista R et al 2025 *White paper and roadmap for quantum gravity phenomenology in the multi-messenger era*, Classical and Quantum Gravity 42, 032001.
- Xu Y 2026 *Relational Quantum Causal Processes toward Quantum Gravity with Controlled Einstein Response*, arXiv:2608.23117.

**Draft citation note:** the family-specific primary bibliography is intentionally not declared complete in v1.0. It must be generated from the authority/provenance ledgers for every row before submission; repository audit filenames are not substitutes for primary literature citations in the final manuscript.

---

## Figure and table plan for v1.1

**Figure 1. Frozen comparison architecture.** Framework-native object → adapter → same-realization gate → common observable/comparator → terminal/partial/BLOCKED state, with a firewall preventing outcome-dependent modification of RQIR Core.

**Figure 2. Primary-obstruction topology.** Thirteen nonterminal families mapped to Classes A–E, visually separating branch-scope and transport-dominated blockers from narrower amplitude, correction-object and state/relational closure blockers.

**Figure 3. D7 decision ecology.** D7-S0 and S1 closed; D7-S2 and S3 open; D7-S4 partial; D7-S5 unauthorized; D7-S6 inactive.

**Table 1. Fourteen-family benchmark matrix.** Included in this draft; v1.1 must add primary literature citations and exact reopen objects.

**Table 2. Claim/evidence matrix.** Move the compact article-facing form to supplementary material or an appendix.

---

## Draft-control status

- Manuscript architecture: complete for first draft.
- Abstract: first CQG-ready pass, <300 words target retained.
- Core methods prose: first full pass.
- Formal result: Proposition 1 + Corollary 1 added.
- Global 14-family result table: first full pass.
- Cross-framework obstruction topology: first full pass.
- Representative case studies: first full pass, with Iter273–274 updates incorporated.
- Discussion/limitations/conclusion: first full pass.
- Primary family-specific citation audit: incomplete; highest-priority task for v1.1.
- Figures: specified but not yet rendered.
- LaTeX/IOP formatting: not yet converted.
- Submission authorization: NOT YET; D7 scientific state remains independent of manuscript completeness.
