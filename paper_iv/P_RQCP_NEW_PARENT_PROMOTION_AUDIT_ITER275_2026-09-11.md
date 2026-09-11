# RQCP new-parent promotion and reproducibility audit — Iter275

Date: 2026-09-11
Candidate family: `RELATIONAL_QUANTUM_CAUSAL_PROCESSES`
RQIR Core: `v1.0 FROZEN`
D7 stage: `D7-S2 STRICT_TIER1_TERMINAL_COVERAGE`

## Trigger

The frozen major-framework coverage contract contains a conservative promotion rule:

`new_concrete_independent_parent_triggers_tier1_promotion = true`

A 2026 RQCP line now supplies a concrete quantum parent with gravity/emergence claims and materially distinct observables rather than a generic adjective or a relabeling of an already-covered action.

Primary authorities checked:

- Yipeng Xu, **Relational Quantum Causal Processes: Exact Models, Continuum Limits, and the Boundary of Emergent Gravity**, arXiv:`2607.26672` (2026-07-29).
- Yipeng Xu, **Relational Quantum Causal Processes toward Quantum Gravity with Controlled Einstein Response**, arXiv:`2608.23117` (2026-08-24).
- Public reproducibility archive: `Amordia/rqcp-toward-quantum-gravity`, release `v1.0.3`, release-metadata commit `3ec71888890453ea487eb0cc8a92548b24e3ed98`, frozen scientific payload `7c749f5f0aeefe07a897123295f3647fdc56d868`.

No explicit reduction/equivalence map from this RQCP parent to an existing KMQGB Tier-1 family was located in the bounded classification audit. Under the frozen coverage rule, omission would therefore be less conservative than promotion.

## What the controlled RQCP result supplies

The August 2026 controlled benchmark uses one refining finite-Hilbert interacting quantum family on a declared fixed physical Fourier band. Within that declared domain it connects one process/generating-functional lineage to:

- a Lorentzian excitation gap;
- connected four-response;
- mixed matter-geometry response;
- a dynamic geometry kernel;
- a positive induced Newton coefficient in the declared local covariant FLRW two-derivative sector;
- a quantum-matter stress contribution used in a semiclassical Friedmann trajectory;
- two inequivalent spatial regulators with analytic convergence/error control toward a common limiting Hamiltonian;
- a non-fitted dimensionless gravity-related spectral combination.

This is materially more than a verbal emergent-gravity proposal. It provides an executable, same-family, fixed-band construction with an explicit public evidence generator.

Scoped result:

`PASS_SCOPED_FIXED_BAND_SAME_FAMILY_EINSTEIN_RESPONSE_AND_REPRODUCIBILITY_CONTROL`

## Independent KMQGB computation

KMQGB added two independent audit layers instead of accepting the archive's own `PASS` string.

### Release / figure / evidence audit

The frozen RQCP release tree was checked independently. Release-integrity and publication-figure regeneration passed. The evidence generator itself also completed successfully.

A raw byte-for-byte JSON comparison failed because floating linear-algebra output is not bit-identical across the hosted environment and because one diagnostic at exactly `omega=0` is numerically ill-conditioned.

### Four-way cross-environment audit

KMQGB then recomputed the same frozen evidence concurrently in four independent runner configurations:

1. Ubuntu 22.04, one BLAS thread;
2. Ubuntu 24.04, one BLAS thread;
3. Ubuntu 24.04, two BLAS threads;
4. Ubuntu 24.04, four BLAS threads.

GitHub Actions run `34549781006` completed with conclusion `success`; all four matrix jobs passed the independent semantic comparator.

The comparator requires exact agreement of structure and discrete gates, tight agreement of headline physics quantities, and explicit survival of the external algorithmic threshold inequalities. Derived ratios are compared separately because they divide small numerical differences.

Cross-environment result:

`PASS_CORE_WITH_ZERO_FREQUENCY_DIAGNOSTIC_DEFECT`

## Numerical diagnostic defect found

The external implementation's continuum row has declared frequency `omega = 0`. At that point its `exact_kernel` and `static` expressions are algebraically identical. They are nevertheless evaluated separately in floating arithmetic and subtracted; the round-off residual is then divided by `1e-30` in the `geometry_derivative_remainder` diagnostic.

On the GitHub hosted environment this turns a subtraction residual of order machine precision into a reported diagnostic of approximately

`8.881784197001251e14`.

The analytic remainder at exact zero frequency is zero. The archive itself reports the corresponding bound and bound ratio as zero, and the anomaly does not flip the declared closure gates. KMQGB therefore records this as a reproducibility/diagnostic implementation defect, not as a physical divergence and not as evidence of quantum-gravity completion.

This defect should be fixed upstream by handling `omega == 0` analytically or by using a scale-aware denominator rather than `1e-30`.

## Why RQCP is not terminal

The RQCP authors explicitly limit the result. The August paper calls it a same-family **fixed-band closure theorem**, not an all-band QFT or completed quantum gravity. The declared construction takes the finite oscillator cutoff, fixed band, covariant two-derivative FLRW sector and semiclassical Einstein equation as inputs.

The broader July framework likewise states that the available controlled models do not yet constitute one background-independent microscopic law that jointly generates adjacency, time, volume normalization, dimension, signature, nonlinear Einstein constraints and quantum matter.

Consequently the controlled result does **not** establish, at family scope:

- one all-band interacting Lorentzian local quantum theory;
- autonomous selection/generation of adjacency, clock/time, volume normalization, effective dimension and signature;
- a quantum metric Hilbert space or an independently equivalent complete gravity-state structure;
- unrestricted anomaly-free quantum constraint / BV-BRST closure;
- topology change, black-hole and singularity control;
- the Standard Model or complete matter sector;
- family-level exhaustion of materially distinct RQCP realizations;
- a full common-domain comparator/error capsule sufficient for global D4/D7 terminal classification.

The external machine-readable claim boundary itself records `all_band_nonperturbative_QG_completion = false` and canonical `NP1--NP6 = 0/6`.

## Coverage classification

Because this is a concrete independent quantum parent and no explicit reduction map has been established, the frozen coverage rule requires a new Tier-1 row.

Promotion result:

`PROMOTE_TO_TIER1_NONTERMINAL__RQCP_CONCRETE_INDEPENDENT_QUANTUM_PARENT_WITH_FIXED_BAND_SAME_FAMILY_EINSTEIN_RESPONSE_CONTROL`

Coverage status:

`PARTIAL_SUBFAMILY_ONLY`

Active blocker:

`BLOCKED_MISSING_ALL_BAND_BACKGROUND_INDEPENDENT_AUTONOMOUS_GRAVITY_PARENT_QUANTUM_METRIC_OR_EQUIVALENT_GRAVITY_HILBERT_STRUCTURE_ANOMALY_FREE_CONSTRAINT_CLOSURE_TOPOLOGY_CONTROL_AND_NORMALIZED_SAME_DOMAIN_COMPARATOR_CERTIFICATE`

This is not a scientific `FAIL`. It is also not family-level sufficiency.

## Census consequence

Before this audit the frozen coverage ledger contained 14 Tier-1 rows, of which only `GR_EFT` was strict terminal.

After conservative promotion of RQCP:

- Tier-1 total: `15`;
- strict terminal: `1/15`;
- strict nonterminal: `14/15`;
- Tier-2 unresolved: remains `0`;
- D7-S2: remains `NOT_CLOSED`;
- D7-S3: remains `NOT_CLOSED`;
- D7-S4: remains `PARTIAL_GLOBAL_NOT_CLOSED`;
- D7-S5: remains `NOT_AUTHORIZED`;
- Candidate Gravity remains inactive at canonical R3 `24%`;
- `NEW_REQUIRED` remains unauthorized.

The terminal fraction decreases because coverage became more complete. That is scientifically preferable to preserving an artificially favorable denominator.

## Exact next RQCP gate

Do not spend compute repeating the already stable fixed-band calculation. Reopen the RQCP family when a materially new object supplies one of the missing family-scope bridges, especially:

`RQCP_FIXED_BAND_CONTROL -> ALL_BAND_BACKGROUND_INDEPENDENT_AUTONOMOUS_GRAVITY_PARENT -> QUANTUM_GRAVITY_STATE/CONSTRAINT_STRUCTURE -> NORMALIZED COMMON_DOMAIN OBSERVABLE/COMPARATOR/ERROR PACKAGE`

Independent compute should instead be used for new bridge candidates or for prospective falsification/robustness tests that can change the family classification.

## Repository audit artifacts

- `.github/workflows/rqcp-reproducibility-audit.yml`
- `.github/workflows/rqcp-cross-environment-audit.yml`
- `code/rqcp_evidence_semantic_compare.py`
- cross-environment run: `34549781006` = `success`

## Iter275 conclusion

RQCP is scientifically interesting and unusually reproducible for a new emergent-gravity proposal in its declared fixed-band domain, but it does not yet solve quantum gravity. The correct KMQGB action is **coverage promotion without terminal promotion**: add it to Tier-1 as a new nonterminal parent, preserve the positive fixed-band result, record the zero-frequency numerical diagnostic defect, and keep D7 globally unauthorized.