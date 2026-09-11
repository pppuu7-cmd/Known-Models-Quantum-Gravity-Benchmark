# Paper IV — obstruction-topology robustness audit v0.1

Date: 2026-09-11
Applies to: 13 nonterminal Tier-1 candidate-family rows
Purpose: determine whether the manuscript's five-class obstruction topology is a reproducible projection of the frozen family states or merely an artifact of informal labeling.

## 1. Taxonomy

The manuscript uses five **primary** obstruction classes. They are intentionally not mutually exclusive descriptions of all difficulties inside a theory family. They identify the first decisive terminal blocker under a deterministic projection rule.

### C1 — `FAMILY_OR_BRANCH_SCOPE`

Use when a material branch, prescription, compactification, functional-form class or independent subfamily remains unresolved such that a child result cannot be promoted to the parent family even if the child's own observable were terminal.

### C2 — `SAME_REALIZATION_TRANSPORT`

Use when family scope is sufficiently bounded for the active claim but the decisive missing object is a physical map connecting microscopic/UV/continuum data to the normalized gravitational observable/comparator domain in one realization.

### C3 — `AMPLITUDE_OR_COMPARATOR_COMPLETENESS`

Use when the active realization is sufficiently identified and the decisive missing object is a term or package needed to complete the physical amplitude/residual and its same-domain comparator/error treatment.

### C4 — `EXPLICIT_BEYOND_BASELINE_CORRECTION_OBJECT`

Use when the continuum/baseline gravitational limit exists but the benchmark requires a concrete normalized beyond-baseline correction tensor/coefficient that has not yet been supplied.

### C5 — `PHYSICAL_STATE_RELATIONAL_OBSERVABLE_CLOSURE`

Use when the decisive blocker is definition of the physical state/Hilbert-space/clock/constraint/Dirac-observable structure required before the observable can be treated as a physical comparator object.

## 2. Deterministic baseline projection rule

For each nonterminal family, evaluate the following predicates in order and assign the **first true** predicate:

1. unresolved material family/subfamily/branch scope blocks parent-level promotion → C1;
2. otherwise, missing same-realization UV/continuum/refinement/parameter transport to physical observable → C2;
3. otherwise, incomplete amplitude/contact/comparator/error package → C3;
4. otherwise, absent explicit normalized beyond-baseline correction object → C4;
5. otherwise, unresolved physical-state/relational-observable certificate → C5.

The ordering is not a claim that C1 is more physically important than C2. It is a reproducibility convention: an unresolved parent scope logically precedes promotion of any child observable to the family.

## 3. Baseline assignment

| Family | Baseline primary class | Reason for assignment |
|---|---|---|
| Perturbative / higher-derivative gravity | C1 | materially distinct quantization/pole/prescription branches remain non-equivalent at parent scope |
| Hořava–Lifshitz gravity | C1 | projectable and non-projectable/BPS branches cannot inherit one another's status |
| Asymptotic Safety | C3 | active same-realization target is specifically missing a public contact-complete `s+t+u+A4` amplitude/comparator/error certificate |
| Nonlocal / infinite-derivative gravity | C1 | causality/form-factor/functional branches remain materially non-equivalent; family exhaustion is not closed |
| String / M-theory / holographic gravity | C1 | compactification/duality/moduli branches are not exhausted or reduced at family scope |
| Causal Set quantum gravity | C2 | missing fundamental measure/dynamics → manifoldlike 3+1 GR → normalized gravitational observable chain |
| CDT/EDT | C2 | missing continuum/RG trajectory plus scale-setting map to invariant normalized physical observable |
| LQG / EPRL-spinfoam | C2 | missing same-realization refinement/continuum → UV-to-IR/GR → normalized observable/parameter/comparator chain |
| GFT / tensor models | C2 | after explicit EPRL/FK reduction, independent branches still require continuum/FRG → gravitational-observable transport |
| Causal Fermion Systems | C4 | continuum/classical-gravity structure exists; first explicit normalized beyond-GR correction object remains absent |
| Noncommutative spectral geometry | C2 | missing spectral-data → RG/threshold → low-energy normalized observable/covariance chain |
| Canonical Wheeler–DeWitt geometrodynamics | C5 | physical Hilbert space/state/clock/constraint/relational observable certificate is the decisive blocker |
| Quantum Graphity | C2 | missing same-Hamiltonian geometrogenesis → continuum Lorentzian Einstein spin-2 → normalized observable chain |

Baseline count vector in class order `(C1,C2,C3,C4,C5)`:

`(4,6,1,1,1)`

The two structural classes C1+C2 therefore contain `10/13 = 76.9%` of current nonterminal families.

## 4. Sensitivity test A — transport-first tie breaking

Potential ambiguity exists when a family simultaneously has branch incompleteness and a UV→IR transport gap. To test dependence on the baseline priority rule, define an alternative projection in which C2 is checked before C1 whenever both are simultaneously true.

The most plausible reassignments are:

- Hořava–Lifshitz: C1 → C2, because a same-realization UV→IR extra-mode/GR trajectory is also an explicit terminal blocker;
- String/M-theory/holography: C1 → C2, because compactification/moduli→4D observable transport is also an explicit blocker.

Higher-derivative gravity and nonlocal gravity remain C1 because the prescription/functional-family split itself prevents a unique parent realization from being defined.

Alternative-A count vector:

`(2,8,1,1,1)`

C1+C2 remains `10/13 = 76.9%`.

## 5. Sensitivity test B — scope-maximal tie breaking

Define a second alternative projection in which any materially independent branch not covered by an explicit reduction map is assigned C1 even if a transport problem is already visible inside the active branch.

The strongest plausible additional reassignment is:

- GFT/tensor models: C2 → C1 because independent TGFT/condensate/random-tensor branches remain after the EPRL/FK-GFT reduction.

Alternative-B count vector:

`(5,5,1,1,1)`

Again C1+C2 remains `10/13 = 76.9%`.

## 6. Robust and non-robust conclusions

### Robust at v0.1

1. The exact split between family-scope and transport blockers is **not** invariant under reasonable tie-breaking.
2. The combined dominance of family/scope plus same-realization transport **is** invariant across the baseline and both bounded alternative projections tested here: 10/13 rows (76.9%).
3. The remaining three families retain qualitatively distinct local blockers in all tested projections: Asymptotic Safety (amplitude/comparator completion), CFS (explicit correction object), and WDW (physical-state/relational closure).
4. Therefore the manuscript should emphasize **structural comparison closure** rather than the exact numerical difference `4 versus 6`.

### Not yet robust enough for priority language

The statement “there are exactly five universal obstruction classes in quantum gravity” is not supported and must not appear. The allowed claim is narrower:

> Under the current frozen KMQGB census and a declared primary-blocker projection, the thirteen nonterminal family rows can be compressed into five recurring current obstruction classes. The precise C1/C2 split depends on tie-breaking, while the combined dominance of scope and same-realization transport blockers is stable across bounded alternative projections.

## 7. Manuscript change required for v1.1

Replace any wording that presents `(4,6,1,1,1)` as uniquely physical with wording that distinguishes:

- **baseline deterministic projection:** `(4,6,1,1,1)`;
- **robust aggregate:** C1+C2 = `10/13` across the tested alternative projections;
- **interpretation:** most current nonterminality arises before a family-level residual is numerically evaluable.

## 8. Next stronger test

Before submission, encode the assignments in machine-readable form and validate them against the current coverage contract. A future scientific-state change must trigger a taxonomy rebuild rather than manual table editing. The validator should fail if:

- a terminal family is included among the 13 nonterminal assignments;
- a nonterminal Tier-1 family has no primary class;
- a family receives more than one primary class;
- the counts do not sum to the current nonterminal Tier-1 total;
- the manuscript snapshot and D7 readiness state disagree.

## Result

`OBSTRUCTION_TOPOLOGY_BASELINE = (4,6,1,1,1)`

`STRUCTURAL_SCOPE_PLUS_TRANSPORT = 10/13 = 76.9%`

`EXACT_C1_C2_SPLIT_ROBUST = FALSE`

`COMBINED_C1_C2_DOMINANCE_ROBUST_UNDER_TESTED_PROJECTIONS = TRUE`
