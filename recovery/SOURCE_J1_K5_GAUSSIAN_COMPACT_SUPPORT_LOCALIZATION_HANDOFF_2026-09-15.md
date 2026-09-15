# Durable Research / Closure handoff — Gaussian compact-support localization

Date: 2026-09-15

## STATE_READ

Fresh `main` at restoration start was `273e340e0d77a5737250afc3b168854ffcb345f4`. The then-active launch record identified `SOURCE_J1_K5_GAUSSIAN_COMPACT_SUPPORT_LOCALIZATION_GATE`, prereg commit `1e3402aa02a2f52eac5d379ba8b0c5ffc5ebc4ef`, implementation commit `55c07deb557cd22460ba1790396e332bfe3bb83c`, workflow head `0dec512b067b3b19205d2015ee62c8ab401b2e31`, and run `34954491166` as the unique authoritative active gate.

The current-front documents were stale relative to newer substantive commits: they still foregrounded the Critic-invalidated joint-Feynman authority blocker and the earlier Gaussian diagnostic. Fresh main therefore outranked them.

The latest independent Critic verdict read during restoration was `INVALID_PROVENANCE` for the historical joint-Feynman source-authority result; that invalidated blocker was not consumed as a premise here.

Independent workflows were freshly checked without consuming partial values:

- Iter504 run `34907349374`: `queued / conclusion=null`;
- Iter461 run `34748503239`: `queued / conclusion=null`.

## TARGET_GATE

`SOURCE_J1_K5_GAUSSIAN_COMPACT_SUPPORT_LOCALIZATION_GATE`

## WHY_THIS_GATE

It was already prospectively frozen and uniquely active on main, and its Actions run had become terminal. Consuming it has maximal information gain at minimal cost because it directly tests the main loophole in the parent Gaussian divergence: whether the observed growth came from the noncompact tail of the Schwartz test rather than the K5 collision neighborhood itself.

No competing authoritative gate for the same object was launched.

## PREREG

- `research/prereg/SOURCE_J1_K5_GAUSSIAN_COMPACT_SUPPORT_LOCALIZATION_2026-09-15.md`
- commit `1e3402aa02a2f52eac5d379ba8b0c5ffc5ebc4ef`

Frozen before implementation/execution:

- HYPOTHESIS;
- exact OBJECT;
- parent DEPENDENCY;
- source/realization authority;
- P1-P3 paths and `k=5..8` decision grid;
- analytic exterior-bound formula;
- positive and adversarial controls;
- PASS/PARTIAL/INCONCLUSIVE/INVALID rules;
- interpretation ceiling.

Frozen criteria were not changed after result.

## WORK_PERFORMED

1. Recovered fresh main and current-front/recovery state.
2. Read the parent terminal Gaussian diagnostic and latest Critic qualification.
3. Verified Actions run `34954491166` was terminal `completed/success` before consuming substantive values.
4. Verified source-lock job `104333122998` and certificate job `104333345136` both completed `success`.
5. Retrieved artifact `10390478550`, verified ZIP digest `sha256:05e6228012436e8ea6548258cb1e333ead9986d834f95b45d5b9cdb77f64bb8b`, extracted the sole JSON payload, and independently computed payload SHA256 `56b702a0c85945357d9b4d6a7d8fa84baa3e40252bb2d0dd475eb25f8ba0a7b8`.
6. Checked the frozen controls and path predicates from the exact artifact/log output.
7. Saved a canonical decision projection and terminal scientific result on main.
8. Rechecked Iter504 and Iter461 only for terminality; no partial scientific values were consumed.

## RESULT

All frozen controls pass. P1, P2 and P3 all classify `COMPACT_LOCAL_DIVERGENCE_CERTIFIED` on the prospectively frozen `k=5,6,7,8` decision grid.

At `k=8`, the exact exterior-bound / parent-pairing ratios are:

- P1: `1.0642267834229880065894907202235975416096540763936e-28361`;
- P2: `3.4056844890810658670334274078419193150890806548833e-1865280495`;
- P3: `3.2431864727991539050606790560266062965862730696177e-28258`.

The smallest prospectively relevant lower/upper growth ratio among all P1-P3 transitions is P2 `7->8 = 67237350.64431040654289536833564424561259`, far above the frozen threshold `4`.

The `q=0` adversarial control instead produces huge relative bounds and does not certify localization, demonstrating that the classifier genuinely uses the K5 localization input.

## CLASSIFICATION

`AUX_GAUSSIAN_UNRENORMALIZED_COMPACT_LOCAL_DIVERGENCE_SCOPED`

## NEW_FACT

For the exact frozen unrenormalized Gaussian auxiliary regulator family on the aligned highest-contact K5 witness, the previously observed divergence survives replacement of the full Schwartz test by **any** smooth compact cutoff satisfying `chi=1` on `|x|<=1`, `chi=0` on `|x|>=2`, `0<=chi<=1`. The analytic exterior tail is rigorously negligible relative to the frozen parent pairings and cannot overturn positivity or the preregistered growth inequalities on P1-P3.

Therefore the divergence is certified as a **local compact-support diagnostic**, not merely a noncompact-Schwartz-tail effect.

## CLAIM_CEILING

This result does not establish published Eq. (4) distributional nonexistence, universal regulator divergence, failure of renormalized extensions, path dependence between finite limits, source authorization/uniqueness of counterterms, family failure, D7 closure, a terminal D7 selector, Candidate Gravity, or any global quantum-gravity claim.

The result is scoped to the frozen unrenormalized Gaussian auxiliary family and aligned highest-contact witness. Existing Critic-confirmed collision-supported homogeneous ambiguity remains a separate uniqueness limitation conditional on base-extension existence.

## FILES/ARTIFACTS

Durable inputs/implementation:

- `research/prereg/SOURCE_J1_K5_GAUSSIAN_COMPACT_SUPPORT_LOCALIZATION_2026-09-15.md`
- `code/source_j1_k5_gaussian_compact_support_localization.py`
- `.github/workflows/source-j1-k5-gaussian-compact-support-localization.yml`

Durable result records:

- `results/SOURCE_J1_K5_GAUSSIAN_COMPACT_SUPPORT_LOCALIZATION_CANONICAL_2026-09-15.json`
- `results/SOURCE_J1_K5_GAUSSIAN_COMPACT_SUPPORT_LOCALIZATION_RESULT_2026-09-15.md`
- this handoff.

Actions provenance:

- run `34954491166`;
- source-lock job `104333122998`;
- certificate job `104333345136`;
- artifact `10390478550`;
- ZIP digest `sha256:05e6228012436e8ea6548258cb1e333ead9986d834f95b45d5b9cdb77f64bb8b`;
- exact JSON SHA256 `56b702a0c85945357d9b4d6a7d8fa84baa3e40252bb2d0dd475eb25f8ba0a7b8`.

## COMMITS

- prereg `1e3402aa02a2f52eac5d379ba8b0c5ffc5ebc4ef`;
- implementation `55c07deb557cd22460ba1790396e332bfe3bb83c`;
- workflow production head `0dec512b067b3b19205d2015ee62c8ab401b2e31`;
- launch recovery `273e340e0d77a5737250afc3b168854ffcb345f4`;
- canonical certificate projection `aaa720180c062184e3fec76a6b91c4540ae44290`;
- terminal result `a0ba962811b9364bceb03a28f4785aa75e42213a`.

## OPEN_BLOCKERS

- Published Eq. (4) full-collision distributional existence remains unresolved.
- A renormalized local subtraction/counterterm construction has not yet been prospectively built and tested for this Gaussian family.
- Source authorization and uniqueness of any collision-supported subtraction remain unresolved.
- The Critic-confirmed homogeneous collision ambiguity remains relevant to uniqueness conditional on base-extension existence.
- Iter504 remains nonterminal and D7-S2 is not closed.
- Iter461 remains nonterminal.
- `D7-S2 = NOT_CLOSED`, `D7-S3 = NOT_CLOSED`, `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.

## NEXT_RECOMMENDED_GATE

`SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION_GATE`

Prospectively freeze a strictly local subtraction ansatz supported on the aligned collision, with coefficients constrained before execution by the already validated permutation/covariance/source-order/off-collision requirements. Test whether the subtraction removes the compact-local Gaussian divergence on P1-P3 and whether the frozen constraints uniquely determine the finite remainder or leave a nonzero collision-supported free parameter.

The gate must distinguish:

- successful finite renormalized limits;
- path/order dependence;
- residual free counterterm dimension;
- numerical/implementation blocker;
- source-authority blocker.

Do not equate a successful KMQGB-derived subtraction with source authorization unless a separate source authority gate establishes that equivalence.

Governance remains locked: `RQIR Core v1.0 = FROZEN`; terminal D7 labels and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` forbidden; Candidate Gravity inactive.
