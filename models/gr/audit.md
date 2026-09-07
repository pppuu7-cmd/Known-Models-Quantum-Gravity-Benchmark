# Model Audit — 4D Einstein–Hilbert General Relativity

Benchmark ID: RQIR7-M01-GR-EH-MINK
Role: null control
State: TERMINAL
Final status: `EXACT_COMPARATOR_IDENTITY`
Scope: four-dimensional classical Einstein–Hilbert gravity, Lambda=0, weak-field expansion about Minkowski spacetime, ordinary conserved matter stress tensor.

## Concrete realization

\[
S[g,\psi]=\frac{M_{\rm Pl}^2}{2}\int d^4x\sqrt{-g}\,R + S_m[g,\psi].
\]

This audit does not claim to cover arbitrary cosmological constant, nontrivial global topology, matter anomalies, quantum GR loops, low-energy QG EFT corrections, or every nonperturbative GR sector. Those require separate realizations.

## Literal RQIR protocol authority recovered

1. `README.md`, blob `e431df35d929aa8b06b1b1369a2dc80352efe9e9`: defines Q1–Q7, the operational fingerprint hierarchy, and the base residual `Delta_A = O_A^obs - O_A^baseline` with explicit baseline discipline.
2. `candidate_gravity/BASELINE_COMPARATORS.md`, blob `a2b45188710c885f979123f77fa7aad2273b9983`: defines `C0 — Classical GR / Newtonian gravity` as the controlled classical baseline appropriate to the experimental regime.
3. `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`, blob `2757e8fe1004b5c0caef51d6d9fee6f982ac81d4`: defines F0–F7 and distinguishes consistency failure from comparator/novelty identity and operational blocking.
4. Iteration-504 comparator preflight, commit `9af20b657eb89114a954b55b75b59bb3cf284777`: missing upstream comparator target is BLOCKED rather than zero/FAIL; exact comparator identity, when established, is a distinct scientific category.

See `protocol/FROZEN_RQIR_PROTOCOL_REFERENCE.md` for the full ledger.

## Evidence table

| Field | Evidence-level result | RQIR interpretation | State |
|---|---|---|---|
| Action/equations | Einstein–Hilbert action; Einstein field equations | concrete declared dynamics | PASS F0 in declared domain |
| Validity regime | classical weak-field GR about Minkowski | exactly overlaps the declared C0 weak-field classical control domain | frozen scope |
| Physical DOF | two physical radiative tensor polarizations/helicities after gauge constraints in 4D linearized GR | no extra physical scalar/vector pole | supported |
| Propagator/poles | gauge-fixed linearized theory has the massless graviton pole; gauge-dependent pieces are not extra physical modes | null-control pole structure | supported |
| Ghost/tachyon | no additional higher-derivative physical ghost/tachyon introduced by Einstein–Hilbert action with conventional sign | no pathology trigger from extra EH poles | supported within scope |
| Gauge/Ward | diffeomorphism invariance; contracted Bianchi identity is compatible with conserved source | F2 structural conservation/gauge requirement | supported |
| Causal/retarded structure | harmonic/generalized-harmonic formulations are hyperbolic; linearized perturbations admit retarded Green-function solutions | causal response object exists | supported |
| Source rule | metric couples to stress-energy; linearized equation is sourced by conserved stress-energy | classical GR source baseline | supported |
| Nonlinear vertices | Einstein–Hilbert expansion generates the standard graviton self-interaction hierarchy | concrete parent dynamics exists | supported |
| GR/classical limit | realization is GR itself | identity | exact |
| Q1–Q7 atlas | literal definitions recovered from RQIR README | applicable classical pieces are evaluated as C0 baseline; Q7 quantum-EFT correction is outside this realization | mapped |
| Comparator span | literal C0 is Classical GR / Newtonian gravity | this realization is the comparator itself in the declared domain | EXACT IDENTITY |
| Base residual | `Delta_A = O_A^model - O_A^C0` | identically zero wherever this exact C0 realization is the declared baseline | EXACT ZERO |
| F4 novelty | no model-specific direction relative to C0 | retained null-control degeneracy, not inconsistency | TERMINAL |

## Q1–Q7 fingerprint for this control

The purpose of this row is not to claim that classical GR predicts every quantum-interface observable. It records the relation to the RQIR atlas:

- Q1 quantum clocks/proper time: classical spacetime/proper-time part is C0 baseline; quantum-clock state dynamics belongs to the declared matter/QFT baseline layered on top.
- Q2 superposed sources: pure classical GR does not by itself specify a quantum source rule; only the classical controlled response sector is part of this control.
- Q3 backreaction/source rule: classical Einstein response to the declared conserved stress-energy source is the C0 rule tested here.
- Q4 gravity-mediated quantum information: no independent claim of a quantum gravitational channel is made by this classical control.
- Q5 geometry fluctuations: no fundamental quantum metric-noise sector is part of this realization.
- Q6 causal/process structure: ordinary classical Lorentzian causal structure is the C0 baseline.
- Q7 low-energy quantum-gravity EFT: outside the present classical realization and benchmarked separately as `KMQGB-M02-GR-QG-EFT`.

Therefore this model is not marked `PASS_RQIR_GATE` as a quantum-gravity candidate. It is terminal because it succeeds as the intended **null comparator control**.

## Exact comparator identity proof

The literal comparator registry defines C0 as Classical GR / Newtonian gravity in the controlled classical regime. This benchmark realization is classical Einstein–Hilbert GR in one such controlled regime.

For every observable in the overlap domain whose baseline is this same C0 realization,

\[
O_A^{\rm model}=O_A^{C0}.
\]

The RQIR residual definition then gives

\[
\Delta_A=O_A^{\rm model}-O_A^{C0}=0.
\]

No numerical tolerance is needed: this is an analytic identity by comparator construction. Any later calibration/comparator quotient cannot turn exact equality with the comparator into a distinctive nonzero model direction; the equivalence class is the comparator/null class.

## Final classification

- comparator relation: exact identity with C0 in declared domain;
- quotient/null residual: zero class by comparator construction;
- consistency failure: no;
- novelty/model-distinction claim: no;
- terminal status: `EXACT_COMPARATOR_IDENTITY`;
- benchmark interpretation: expected successful null control.

This result must never be paraphrased as “GR is false” or “GR failed RQIR.” It says the opposite methodological thing: RQIR correctly recognizes its declared classical-GR baseline as non-distinct from itself.

## Authoritative scientific sources

1. O. Sarbach and M. Tiglio, *Continuum and Discrete Initial-Boundary Value Problems and Einstein's Field Equations*, Living Reviews in Relativity 15, 9 (2012), harmonic formulation / well-posed hyperbolic reductions: https://link.springer.com/article/10.12942/lrr-2012-9
2. E. Poisson, *The Motion of Point Particles in Curved Spacetime*, Living Reviews in Relativity 7, 6 (2004), linearized gravitational equations and retarded gravitational Green functions: https://link.springer.com/article/10.12942/lrr-2004-6
3. C. P. Burgess, *Quantum Gravity in Everyday Life: General Relativity as an Effective Field Theory*, Living Reviews in Relativity 7, 5 (2004), Einstein gravity as the low-energy gravitational EFT baseline: https://link.springer.com/article/10.12942/lrr-2004-5

## Next benchmark

Start `KMQGB-M02-GR-QG-EFT`: one concrete low-energy quantum-GR EFT realization, tested separately against C5 rather than conflated with classical C0 GR.
