# Candidate Gravity Design Research — Handoff / Recovery Method

This file is the continuation entrypoint for using KMQGB results as design constraints for a future Candidate Gravity model. It does not replace `recovery/RESTORE_FROM_NEW_CHAT.md`; it supplements it.

## A. Restoration order from a new chat

1. Open repository `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`, branch `main`.
2. Read `recovery/RESTORE_FROM_NEW_CHAT.md` completely.
3. Read `recovery/CURRENT_BENCHMARK_FRONT.md`.
4. Read `recovery/state.json`.
5. Read `protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md` completely.
6. Read the highest-numbered `recovery/RECOVERY_DELTA_NNN.md`.
7. Read `logs/research_log.md` from the latest KMQGB iteration onward.
8. Read the active third-wave model audit(s).
9. Read external RQIR `candidate_gravity/recovery/CURRENT_QG_FRONT.md` read-only to know whether shared heavy compute is active.
10. Resume from the exact open blocker in the latest state/front; do not reconstruct it from chat memory.

## B. Permanent historical benchmark state

### First wave

Frozen denominator: `9/9 = 100%` terminal coverage.

The first-wave denominator is immutable and must never be expanded retroactively.

### Second wave

Frozen denominator: `5/5 = 100%` terminal coverage.

The second-wave denominator is also immutable.

### Candidate Gravity readiness

KMQGB benchmark coverage is **not** Candidate Gravity readiness. The last externally observed RQIR Candidate Gravity readiness is stored separately in `state.json` and must be refreshed from RQIR read-only authority before reporting it as current.

## C. Core design lesson to preserve

The strongest accumulated lesson is:

> A future KG model cannot be justified merely by a new force law, new noise, new decoherence, UV softness, scale-free UV behavior, a special pole spectrum, or a nonzero difference from GR. The candidate must produce a linked observable hierarchy from one parent dynamics that survives stronger comparator classes and nuisance/calibration profiling in a common validity domain.

Do not shorten this to “existing theories are wrong.” That conclusion is not supported.

## D. Current preferred KG design target

A useful provisional observable bundle is

`O_KG = {J, N, chi_R, ordered/noncommuting response, higher cumulants, entanglement/non-LOCC witness, Ward/contact identities}`.

This is a **design target**, not yet a derived Candidate Gravity model.

The research task is to find a parent dynamics for which the joint relations among these observables cannot be reproduced by C0–C6, C3b, scalar/scalar-tensor parents, field-redefinition-equivalent models, or broader UV amplitude families.

## E. Mandatory red-team order for every new KG idea

For each proposed KG mechanism, test in this order:

1. C0 GR/classical calibration.
2. C1 semiclassical mean gravity.
3. C2 stochastic gravity.
4. C3 measurement-feedback/classical-channel gravity.
5. C3b postquantum classical gravity.
6. C4 ordinary quantum-matter/non-gravitational mediator nuisance.
7. C5 low-energy quantum GR EFT.
8. C6 QFT source + classical interface alternatives.
9. scalar/Yukawa/scalar-tensor parent degeneracy.
10. analytic field-redefinition/on-shell equivalence.
11. broader UV-completion amplitude degeneracy.
12. common validity-domain check.

If the feature is absorbed at any step, retain it as a negative/design result and do not promote it as KG novelty.

## F. Current third-wave research front

The next research wave should remain separate from the frozen first and second waves.

Highest-value current direction:

### T3-01 — generalized dual-resonance / Coon / bespoke UV amplitudes

Goal: test whether string-like pole/residue/Regge fingerprints remain distinctive against a broad unitary dual-resonance family.

Current new lesson from the literature:

- bespoke dual-resonance constructions permit customizable mass spectra with dual resonance and good UV behavior;
- open parameter regions can deviate from ordinary string theory while satisfying partial-wave unitarity;
- later unitarity work rules out broad asymptotically nonlinear Regge families and narrows viable asymptotically linear subclasses;
- therefore **pole support alone is not a robust UV discriminator**.

Next exact discriminator to test should combine at least:

`{pole locations, residues/spin decomposition, crossing/duality, Regge trajectory, high-energy bounds/sum rules, low-energy coefficient correlations}`.

### T3-02 — full Planck-crossover asymptotic-safety vector

Do not reuse only `p_UV=0`; that exponent is already known non-unique. Freeze a larger vector such as normalization, angular dependence, crossover scale/shape, resonance-like structure and crossing-completed amplitude.

### T3-03 — nonclassical interface discriminator

Construct a test explicitly designed to survive C2/C3/C3b:

- ordered vs symmetrized response;
- entanglement/non-LOCC generation;
- higher cumulants;
- shared Ward/contact constraints.

This is currently the most directly useful branch for eventual KG construction.

### T3-04 — nonlinear postquantum-classical consistency

Move beyond the scoped linearized conserved-kernel control and test nonlinear matter-coupled constraint/Bianchi closure for one concrete realization.

### T3-05 — concrete loop/canonical/discrete QG realization

Instantiate only if an explicit Lorentzian observable kernel exists. Do not benchmark program names.

## G. Heavy-compute policy

Before launching KMQGB heavy work:

1. check external RQIR `CURRENT_QG_FRONT.md` and active Actions run;
2. if shared RQIR heavy computation is active, KMQGB may continue literature, algebra, protocol mapping and lightweight calculations but must not dispatch a competing heavy job;
3. a separate runner may be used only when explicitly available and isolated.

## H. What to write after every research iteration

Every iteration that changes scientific state must update:

- `protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md` if a reusable KG design lesson appears;
- `recovery/CURRENT_BENCHMARK_FRONT.md`;
- `recovery/state.json`;
- `logs/research_log.md`;
- a new immutable `recovery/RECOVERY_DELTA_NNN.md`;
- active model `audit.md` / `result.json` as applicable.

Every user-facing research summary should include:

- first-wave coverage (historical 9/9);
- second-wave coverage (historical 5/5);
- current third-wave coverage once denominator is frozen;
- current active-task completion estimate;
- external Candidate Gravity readiness separately;
- what was proven versus what remains blocked.

## I. Minimal continuation instruction for a new chat

`Продолжай исследование KMQGB и полезные наработки для будущей Candidate Gravity. Восстанови состояние по recovery/RESTORE_FROM_NEW_CHAT.md и recovery/CANDIDATE_GRAVITY_RESEARCH_HANDOFF.md, затем читай protocol/CANDIDATE_GRAVITY_DESIGN_PRIORS.md. Не меняй исторические 9/9 и 5/5 и не записывай benchmark-изменения в основной RQIR.`
