# RQIR Paper IV — CQG manuscript draft v0.2

**Target journal:** Classical and Quantum Gravity  
**Article type:** Research Paper  
**Working title:** **Frozen-Observable Benchmarking Across Quantum-Gravity Frameworks: Same-Realization Closure and Global Decision Gates**

**Status:** WORKING DRAFT / NOT SUBMISSION AUTHORIZED  
**RQIR judge:** Core v1.0 FROZEN  
**Operational proving-ground readiness:** 100%  
**Strict Tier-1 terminal rows:** 1/14  
**Paper-IV global scientific decision:** NOT_YET_AUTHORIZED

---

## Abstract

Theories of quantum gravity are often compared across different states, scales, signatures, truncations, normalizations and observable definitions. A disagreement between two calculations is therefore not automatically a physical disagreement: it may instead reflect a missing map between distinct realizations or incompatible comparator domains. We introduce the Known Models / Quantum Gravity Benchmark (KMQGB), an application of the frozen Relativity–Quantum Interface Reconstruction (RQIR) Core v1.0 to a declared census of major quantum-gravity framework families. Framework-native calculations are mapped into a common observable/comparator language while model-dependent retuning of the benchmark is forbidden. The protocol additionally requires explicit same-realization provenance and quarantines missing theory, transport, normalization, observable and comparator objects as BLOCKED rather than treating them as negative evidence. We apply this construction to 14 Tier-1 families spanning effective gravity, higher-derivative gravity, Hořava–Lifshitz gravity, asymptotic safety, nonlocal gravity, string/M-theory and holography, causal sets, dynamical triangulations, loop quantum gravity and spinfoams, group field theory/tensor models, causal fermion systems, noncommutative spectral geometry, Wheeler–DeWitt geometrodynamics and quantum graphity. The benchmark is operationally saturated, with no unresolved Tier-2 classifications or internally actionable family fronts, but strict scientific closure remains only 1/14 at family level. The resulting global decision is therefore not authorized to select an existing theory, an adaptation, a hybrid construction or a new theory. The main result is an auditable topology of cross-framework comparison failures that separates genuine defined residuals from missing same-realization objects and scoped subfamily results. This provides a reproducible route to stronger future quantum-gravity comparisons without converting incompleteness into falsification.

---

## 1. Introduction

A central difficulty in quantum gravity is not merely the number of competing approaches, but the absence of a uniform physical level at which those approaches can be compared. String/M-theory, loop and spinfoam constructions, asymptotic-safety trajectories, causal sets, dynamical triangulations, higher-derivative and nonlocal theories, canonical quantization, group-field/tensor programmes, spectral geometry and emergent-graph approaches generally do not supply predictions in the same variables, at the same scales, or with the same notion of physical observable. Their calculations may differ in state, signature, regulator, truncation, normalization, response order and infrared matching procedure before any physical disagreement is considered.

This creates a methodological ambiguity. Suppose a framework has a well-defined ultraviolet object but no controlled map to a normalized low-energy gravitational observable. Suppose a second framework supplies a semiclassical observable but only in a branch whose relation to the parent family is incomplete. Suppose a third provides a numerical continuum result, but the same-realization scale-setting and comparator-error package is unavailable. None of these situations is equivalent to a defined experimental or theoretical failure. Nevertheless, broad comparisons of quantum-gravity programmes can inadvertently mix these logically distinct states.

The need for phenomenologically meaningful quantum-gravity observables is well established in comparative cosmological studies and recent multi-messenger quantum-gravity roadmaps. The problem addressed here is narrower and complementary: before asking which framework is observationally favored, when is a cross-framework comparison itself physically well defined?

We address this question using the Relativity–Quantum Interface Reconstruction (RQIR) programme. RQIR freezes a comparison judge before candidate outcomes are interpreted and distinguishes observable closure, comparator definition, parameter transport and model attribution. Paper IV applies this discipline to known quantum-gravity frameworks through the Known Models / Quantum Gravity Benchmark (KMQGB).

The basic map is

`framework-native object -> framework adapter -> frozen RQIR observable/comparator -> terminal, partial or BLOCKED status`.

The adapter may translate variables, conventions or framework-specific structures. It may not modify the frozen benchmark rules because a framework is difficult to compare or because a result appears favorable or unfavorable. In addition, two literature results may be composed only when their parent theory, state, boundary conditions, gauge/regulator choice, truncation, signature, normalization, scale transport and source routing are shown to belong to the same physical realization. Missing objects are therefore represented explicitly rather than being assigned zero residual or counted as exclusions.

This paper reports the executed benchmark, not merely the formalism. A predeclared Tier-1 census contains 14 major quantum-gravity families. All Tier-2 classification questions have been resolved by promotion or explicit reduction maps. The operational proving ground has reached internal saturation: every nonterminal family has either a terminal representation or an explicit external theory/data/authority reopen condition, and no remaining internally executable task can currently change a family-level terminal classification without introducing new physical input. Yet the strict scientific outcome remains deliberately nonterminal. Only the General Relativity plus controlled low-energy effective-field-theory baseline is presently a terminal family row; the remaining 13 families are partial or blocked at family scope. Consequently the global D7 classifier is not authorized to conclude that an existing theory is sufficient, that an adaptation or hybrid is required, or that a genuinely new theory is required.

The distinction between operational saturation and scientific closure is one of the main results of the benchmark. It makes explicit where the quantum-gravity comparison problem currently fails: incomplete family coverage at terminal scope, missing same-realization maps, non-common comparator domains, or genuinely defined residual evidence. The method therefore produces a structured map of proof obligations rather than an unsupported ranking of research programmes.

The paper is organized as follows. Section 2 defines the frozen comparison architecture and the family-scope contract. Section 3 gives the observable and same-realization closure rules. Section 4 presents the 14-family benchmark matrix. Section 5 develops representative physical case studies. Section 6 evaluates the global D-gates. Section 7 discusses what can and cannot be inferred about the present landscape of quantum-gravity theories, and section 8 summarizes the limitations and future terminal conditions.

---

## 2. Frozen comparison architecture

### 2.1 Independent benchmark judge

RQIR Core v1.0 is frozen before Paper-IV family outcomes are interpreted. The purpose is to prevent circular evaluation: a family-specific difficulty cannot be repaired by silently redefining the comparison criterion, and a favorable child result cannot enlarge the scope of the test after the fact.

Framework-specific adapters are nevertheless necessary because native theory objects differ. An adapter may perform an explicitly documented change of variables, convention matching, scale transport, normalization translation or observable extraction. Such transformations belong to the framework-facing layer. A genuine defect in the frozen core would require independent change control and cannot be inferred merely from a blocked model comparison.

### 2.2 Family-scope coverage contract

Paper IV separates a family from a particular realization or subfamily. A result obtained for one quantization prescription, compactification, truncation, branch, state or continuum construction cannot be promoted to a family-level verdict without one of the following: exhaustive resolution of materially distinct branches, a theorem-level equivalence, an explicit reduction map, or a scope proof showing that the omitted branches lie outside the declared Paper-IV target.

This rule is essential for avoiding two symmetric errors: a scoped failure cannot exclude an entire programme, and a scoped success cannot establish family-wide sufficiency.

### 2.3 Evidence states

The benchmark uses six article-facing evidence classes:

- `ESTABLISHED_EXTERNAL`: established by an external publication or public authority within its stated scope;
- `DERIVED_KMQGB`: analytically derived within the benchmark from declared assumptions;
- `REPRODUCED_EXECUTABLE`: reproduced by a stable executable control;
- `OPEN_BLOCKED`: a required physical or attribution object is absent or not composable;
- `HYPOTHESIS_ONLY`: an exploratory route lacking promotion obligations;
- `FORBIDDEN_OVERCLAIM`: wording that would exceed the frozen evidence.

The decisive semantic rule is

`BLOCKED != FAIL`.

---

## 3. Observable and same-realization closure

### 3.1 Realization vector

For a cross-framework comparison to be admitted, the benchmark freezes a realization vector containing, where relevant,

`parent theory / state / boundary conditions / gauge / regulator / truncation / signature / normalization / scale / source routing`.

Results that share a programme label but differ in materially relevant entries cannot be concatenated unless an explicit transport or equivalence map is supplied.

### 3.2 Common comparator domain

A candidate/framework result and its comparator must use the same observable definition and physical domain. At minimum, the comparison audits response order, state/background, normalization, source routing and contact/amputation conventions, together with uncertainty objects where the claim depends on them.

If a residual is undefined because one of these objects is missing, the residual remains undefined. It is never set to zero and is never counted as scientific failure.

### 3.3 Operational saturation versus terminal closure

Operational saturation means that all scientifically justified work executable from the currently available authority has been exhausted and that every remaining open family row has a concrete reopen condition. It does not imply that the underlying physical objects exist, that the family has failed, or that the global theory-selection problem is solved.

This distinction allows the proving ground to be complete as a method while remaining scientifically open as a comparison.

---

## 4. Global 14-family benchmark

The declared Tier-1 census and current family-level status are summarized below.

| Tier-1 family | Current benchmark state | Article-facing physical interpretation / terminal blocker |
|---|---|---|
| GR + controlled low-energy gravitational EFT | `BENCHMARKED_COMPLETE_REALIZATION` | Terminal baseline comparator in the declared low-energy domain. |
| Perturbative renormalizable / higher-derivative gravity | `PARTIAL_SUBFAMILY_ONLY` | Quantization/prescription branches are materially distinct; family closure requires terminal branch dispositions plus one fixed-branch normalized observable and comparator package. |
| Hořava–Lifshitz gravity | `PARTIAL_SUBFAMILY_ONLY` | Projectable and non-projectable/BPS branches cannot inherit one another's status; a complete UV-to-IR same-realization trajectory with normalized extra scalar/tensor observables is missing. |
| Asymptotic Safety | `BLOCKED_MISSING_REQUIRED_OBJECT` | Lorentzian gravitational observable/contact evidence exists, but a stable reproducible same-realization amplitude plus normalization/error/comparator certificate remains open. |
| Nonlocal / infinite-derivative gravity | `PARTIAL_SUBFAMILY_ONLY` | Causality and functional-form branches remain non-equivalent at family scope; cross-order/full-momentum rigidity and family exhaustion are incomplete. |
| String / M-theory / holographic gravity | `PARTIAL_SUBFAMILY_ONLY` | Scoped amplitude controls do not exhaust material compactification/duality branches; a same-realization compactification/moduli-to-4D observable/error chain and family-level reduction/exhaustion certificate remain open. |
| Causal Set quantum gravity | `PARTIAL_SUBFAMILY_ONLY` | Continuum/action and propagation controls exist; a fundamental measure-to-manifoldlike 3+1 GR dynamics plus normalized causal-set gravitational observable is not terminally established. |
| Causal/Euclidean Dynamical Triangulations | `PARTIAL_SUBFAMILY_ONLY` | 4D semiclassical geometry and curvature controls exist; a multi-coupling continuum trajectory, scale setting and invariant observable with full systematic errors remain external completion objects. |
| Loop Quantum Gravity / EPRL-spinfoam | `BLOCKED_MISSING_REQUIRED_OBJECT` | Microscopic/continuum adjacent authorities exist, but the same-realization EPRL/spinfoam-to-continuum/RG-to-EFT parameter and observable transport chain is incomplete. |
| Group Field Theory / tensor models | `PARTIAL_SUBFAMILY_ONLY` | Some EPRL/FK-GFT content is reducible to spinfoams; independent TGFT/condensate/tensor branches still require continuum-to-gravity observable authority. |
| Causal Fermion Systems | `BLOCKED_MISSING_REQUIRED_OBJECT` | Continuum/gravity structure and correction generation exist; the first explicit normalized beyond-GR gravity correction tensor/coefficient with a same-domain comparator remains unavailable. |
| Noncommutative spectral geometry | `PARTIAL_SUBFAMILY_ONLY` | Weak-field gravity realizations exist; the spectral-triple-to-RG/threshold-to-low-energy observable and covariance transport chain is not terminal at family scope. |
| Canonical Wheeler–DeWitt geometrodynamics | `BLOCKED_MISSING_REQUIRED_OBJECT` | Semiclassical observables exist, but a full physical-Hilbert-space/state/clock/relational-observable/error certificate remains open. |
| Quantum Graphity / dynamical-graph geometrogenesis | `PARTIAL_SUBFAMILY_ONLY` | Geometrogenesis and graph-propagation proxies exist; same-Hamiltonian continuum Lorentzian Einstein spin-2 emergence with normalized observables remains unclosed. |

The global inventory is therefore:

- Tier-1 families: 14;
- terminal family rows: 1;
- nonterminal family rows: 13;
- unresolved Tier-2 classifications: 0;
- internally actionable unresolved fronts: 0;
- operational proving-ground readiness: 100%;
- strict scientific D7 authorization: absent.

The scientific content of this table is not that thirteen programmes have failed. Rather, it identifies the exact level at which each programme ceases to support a family-level common-domain comparison under the frozen contract.

---

## 5. Representative physical case studies

### 5.1 Loop quantum gravity and the difference between an algebraic bridge and a physical bridge

The LQG/spinfoam case illustrates why internally consistent algebraic relations do not by themselves prove cross-regime physical identity. The active benchmark route combines microscopic EPRL/spinfoam structure, area-metric/RG adjacent authority and an effective observable parameterization. Within the frozen adapter, the relations

`q = 1/gamma - gamma - Delta_gamma`,

`beta_Delta = beta_rho - (1 + 1/gamma^2) beta_gamma`,

`gamma = -cot(4 psi)`,

`Delta_gamma = 2 cot(8 psi) - q`,

and

`beta_Delta = -16 csc^2(8 psi) beta_psi - beta_q`

constrain any valid multiscale bridge. They expose identifiability and RG-consistency conditions in the common observable variables.

However, these equations do not establish that the microscopic EPRL object, the area-metric continuum description and the effective gamma-dependent observable are already the same physical realization. The missing object is the provenance-controlled EPRL/spinfoam -> continuum/RG -> effective-observable chain, including same-parent parameter transport and error control. The family therefore remains BLOCKED rather than being assigned either success or failure.

### 5.2 Asymptotic safety and reproducible Lorentzian completion

Asymptotic-safety calculations can provide nontrivial gravitational running and Lorentzian scattering information. The Paper-IV question is more specific: is there a stable, reproducible same-realization observable package that can be placed beside the frozen comparator with the required normalization and errors?

The current benchmark identifies programme-level Lorentzian contact evidence but does not yet possess the full contact-complete, same-realization amplitude/error/comparator certificate required for a terminal family row. Increasing numerical precision on a different truncation or related amplitude would not close this logical gap unless the realization and normalization chain were simultaneously fixed.

### 5.3 Hořava–Lifshitz gravity and branch non-inheritance

Hořava gravity provides a clean example of family-scope discipline. Projectable and non-projectable/BPS formulations are materially distinct. A UV trajectory in one branch cannot establish the infrared gravitational status of the other. Even inside the projectable branch, ultraviolet marginal-coupling running and low-energy scalar phenomenology cannot be joined merely because both are labelled Hořava gravity.

A terminal comparison requires a same-realization trajectory through the relevant lower-derivative operators, scalar normalization and controlled infrared matching to a common GR/EFT comparator. Without that bridge the correct state is BLOCKED or partial, not family-level exclusion.

### 5.4 Higher-derivative gravity and prescription dependence

Higher-derivative gravity illustrates a different failure mode: the theory family contains materially different quantization and pole prescriptions. A result obtained under a fakeon, principal-value or another prescription may be scientifically meaningful within that branch while remaining insufficient to characterize the family.

The benchmark therefore separates action-level structure from quantization-branch observables. A family-level decision requires terminal dispositions of the material branches or an explicit equivalence/exhaustion argument, followed by a fixed-branch same-realization observable/comparator package.

### 5.5 Causal Fermion Systems and the missing correction object

For Causal Fermion Systems, the benchmark can identify continuum gravitational structure and a systematic route to corrections. The terminal Paper-IV object, however, is an explicit normalized beyond-continuum gravity correction tensor or coefficient together with a same-domain comparator. In its absence the framework cannot be assigned a defined residual at the requested order. The missing object is therefore scientifically localized rather than interpreted as evidence against the framework.

---

## 6. Global D-gate state

The global decision logic is staged so that theory-selection language cannot be reached before the comparison problem itself is closed.

- **D1 — frozen judge integrity:** PASS.
- **D2A — strict framework-set terminal coverage:** NOT_CLOSED.
- **D2B — same-realization object completeness:** NOT_CLOSED.
- **D3 — common-domain comparability:** PARTIAL.
- **D4 — family-level comparator-subtracted matrix:** PARTIAL_GLOBAL_NOT_CLOSED.
- **D5 — missing-object quarantine:** PASS.
- **D6 — same-realization discipline:** PASS_RULE_TARGETS_OPEN.
- **D7 — global terminal proof:** NOT_CLOSED / NOT_YET_AUTHORIZED.

The D7 classifier is permitted eventually to return only one of four mutually exclusive high-level outcomes:

`EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, or `NEW_REQUIRED`.

At the current state none is authorized because the strict coverage, same-realization and common-domain prerequisites are not closed.

This design prevents a particularly strong but invalid inference: operational exhaustion of currently available comparisons cannot be promoted into a claim that a new theory of quantum gravity is necessary.

---

## 7. Discussion

### 7.1 What the benchmark establishes

The executed benchmark establishes that heterogeneous quantum-gravity programmes can be interrogated under a fixed observable/comparator discipline without modifying the judge to accommodate individual frameworks. It also demonstrates that a large fraction of apparent cross-framework incompleteness is structurally classifiable. The blocking object can be identified as, for example, a family-scope reduction map, a same-realization UV-to-IR trajectory, a normalization certificate, a physical observable, a covariance/error object or a common comparator.

This is useful because these categories imply different next scientific actions. A missing numerical evaluation calls for computation; a missing same-realization map calls for analytic theory or provenance; a branch-coverage problem calls for family classification; and a genuinely defined residual can support scientific discrimination. Treating all four as generic model failure destroys this distinction.

### 7.2 What the benchmark does not establish

The present results do not show that all known quantum-gravity theories are wrong. Thirteen of fourteen Tier-1 rows are not terminal scientific failures; they are partial or blocked at family scope. Nor does the current state establish that the GR/EFT baseline is a fundamental ultraviolet theory. It serves as the terminal comparator in its declared controlled low-energy domain.

Most importantly, `NEW_REQUIRED` is not authorized. A new candidate theory may be scientifically motivated for many independent reasons, but Paper IV cannot infer its necessity until the frozen D2/D4 prerequisites close and the D7 classifier is legally reached within the benchmark.

### 7.3 Relation to quantum-gravity phenomenology

Quantum-gravity phenomenology typically organizes the problem around observables, experimental channels and constraints. The present work is complementary. It asks whether the theoretical object being attached to an observable is sufficiently specified, transported and normalized to support a cross-framework statement in the first place.

This distinction matters for future gravitational tests. A stronger detector constraint does not automatically discriminate ultraviolet frameworks if the theory-to-observable map is underdetermined or if several physically distinct branches project into the same phenomenological parameter. Conversely, a carefully closed same-realization map can make even a null result scientifically sharper by defining exactly which parent realization it constrains.

### 7.4 Why operational saturation is scientifically useful

The benchmark has reached 100% operational saturation in the narrow sense that no currently available internal task can change a family-terminal classification without genuinely new external physical input. This is not merely project-management metadata. It identifies the frontier between problems of analysis and problems of missing physics.

For each nonterminal family the next step is therefore event-driven: the row should be reopened only when a new authoritative theory object, data capsule, same-realization mapping or reduction/equivalence proof can satisfy the recorded terminal condition. Repeating literature searches or launching heavy computation against a provenance blocker would not increase scientific closure.

---

## 8. Limitations

The benchmark has several substantive limitations. First, the Tier-1 census is broad but remains a declared scientific partition rather than a theorem that every conceivable quantum-gravity proposal belongs uniquely to one row. New materially independent parent theories must be promoted rather than silently absorbed.

Second, family-level terminality is intentionally demanding. This reduces false exclusions but can leave a programme blocked when the relevant literature has not yet supplied a complete same-realization object. The method therefore favors conservative attribution over rapid ranking.

Third, Paper IV does not attempt to reproduce every calculation in every framework. The benchmark instead reproduces the comparison logic and selected executable relations while relying on external scientific authorities for framework-native results. Claims must therefore preserve the scope of those authorities.

Fourth, several current blockers are analytic or provenance problems rather than numerical ones. Heavy computation cannot substitute for an undefined parameter identity, normalization, reduction map or physical observable.

Finally, the current global result is explicitly nonterminal. Any later movement to `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED` or `NEW_REQUIRED` must be treated as a new scientific state requiring an updated frozen evidence package.

---

## 9. Conclusion

We have applied a frozen observable/comparator protocol to a declared census of fourteen major quantum-gravity framework families. The resulting KMQGB proving ground separates three states that are often conflated in broad theory comparisons: a genuinely defined residual, a scoped result that cannot yet represent its parent family, and a comparison blocked by a missing same-realization or common-domain object.

The benchmark is operationally saturated but scientifically nonterminal. All Tier-2 classifications are resolved and no internally actionable family front remains, yet only the GR plus controlled low-energy EFT baseline is currently terminal at strict family scope. The remaining thirteen families retain explicit physical reopen conditions. Consequently, no global theory-selection outcome is authorized and the present analysis does not imply that a new quantum-gravity theory is required.

The main contribution is therefore a reproducible decision architecture for quantum-gravity comparison rather than an exclusion census. By requiring family-scope provenance, same-realization transport and common observable/comparator closure before a residual is interpreted, the method converts vague incompleteness into explicit proof obligations. Future theoretical or observational advances can then be incorporated locally: when a missing object appears, the corresponding family row can be reopened without redefining the comparison judge or retroactively changing the meaning of earlier results.

---

## Data and reproducibility statement — working text

The benchmark protocols, family adapters, executable controls, machine-readable decision ledgers and deterministic reproducibility bundle are maintained in the public KMQGB repository. The submission version will cite an immutable release/tag and archive snapshot rather than a moving branch. Repository engineering details will be kept secondary to the physical analysis in the main paper.

---

## Planned figures

**Figure 1:** Frozen benchmark architecture and one-way firewall from framework-native objects to the RQIR comparator.

**Figure 2:** Same-realization vector and failure taxonomy, separating missing transport/normalization/comparator objects from defined residuals.

**Figure 3:** Fourteen-family benchmark state matrix.

**Figure 4:** D1–D7 global decision flow showing why D7 remains unauthorized despite operational saturation.

---

## Current preparation state

**Manuscript-writing readiness:** approximately 30%.  
**CQG targeting/structure:** approximately 70%.  
**Scientific D7 authorization:** NOT_YET_AUTHORIZED and tracked independently from manuscript completion.
