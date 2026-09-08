# T3-04 Audit — nonlinear postquantum-classical consistency

Benchmark ID: KMQGB-T3-M04-PQCG-NONLINEAR  
Concrete audit family ID: `PQCG-COVARIANT-NONLINEAR-CONSTRAINT-001`  
Role: test whether the strong C3b comparator remains consistent beyond the scoped linearized conserved-kernel sector  
State: **TERMINAL — `BLOCKED_MISSING_REQUIRED_OBJECT`**

## Terminal decision

The 2026 classical-quantum literature now establishes substantially more than the second-wave linearized control:

- general continuous memoryless CQ dynamics can be characterized under complete positivity/probability preservation;
- a manifestly covariant configuration-space CQ path integral exists;
- diffeomorphism-invariant CQ gravity can be written in that framework;
- complete positivity is proved directly in the path-integral formulation;
- in that covariant classical-field construction, the classical gravitational field is proved unable to generate entanglement between quantum systems.

However, the benchmark's nonlinear F2 target is stronger: it requires `CP`, diffeomorphism covariance, `H_i`, `H_0`, closure, Bianchi/backreaction compatibility and physical DOF to be established for the **same concrete nonlinear gravitational dynamics**.

The available 2026 covariant path-integral result does not supply a canonical or equivalent published nonlinear first-class constraint/physical-DOF audit matching that full vector. The older 2022 calculation does analyze nonlinear constraints, but for a broad discrete class and finds non-closure without additional constraints; it cannot be silently identified with the later covariant path-integral realization.

Therefore T3-04 is terminally classified

`BLOCKED_MISSING_REQUIRED_OBJECT`

at

`PQCG_SAME_REALIZATION_NONLINEAR_CONSTRAINT_CLOSURE`.

This is **not** a theory-wide inconsistency verdict.

## Authority set and what each actually proves

### 1. Oppenheim & Weller-Davies constraint analysis

For a broad discrete postquantum classical-gravity class with quantum scalar matter, the generalized Hamiltonian/momentum constraint algebra does not close without additional constraints.

This is a real scoped warning, not a universal no-go.

### 2. General continuous hybrid dynamics, 2026

The most general memoryless continuous CQ dynamics is constrained by complete positivity and probability preservation. This strengthens the mathematical admissibility of continuous hybrid dynamics but is not itself a gravitational Dirac-algebra proof.

### 3. Covariant CQ path integrals, PRX 2026

The configuration-space path integral proves complete positivity directly and permits Lorentz/diffeomorphism-invariant CQ field theories, including a diffeomorphism-invariant CQ gravity construction.

It also proves that the classical field cannot mediate entanglement. This is an important positive result for the C3b comparator ledger.

But manifest covariance and CP do not by themselves answer the benchmark's canonical/equivalent questions:

- what are the full nonlinear `H_i,H_0` constraints of this exact realization?
- do they form a first-class/consistent reduced system after all required extra constraints?
- what physical gravitational/stochastic DOF remain?
- how exactly do stochastic/backreaction identities implement the Bianchi/constraint content after reduction?

Those same-realization objects are the missing requirement.

## Frozen consistency vector

`I_PQNL = {CP, DiffCov, H_i, H_0, Closure, Bianchi, MatterBackreaction, DOF}`

Terminal state by component:

- `CP`: **PASS** for the 2026 covariant path-integral class;
- `DiffCov`: **PASS_SCOPED** for the displayed covariant gravity construction;
- `MatterBackreaction`: **PASS_SCOPED** at path-integral/action level;
- `H_i`: **MISSING_SAME_REALIZATION_AUDIT**;
- `H_0`: **MISSING_SAME_REALIZATION_AUDIT**;
- `Closure`: **MISSING_SAME_REALIZATION_AUDIT**;
- `Bianchi`: **PARTIAL/representation-level**, not a complete reduced-phase-space closure certificate;
- `DOF`: **MISSING_SAME_REALIZATION_AUDIT**.

## F0-F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 dynamics | PASS_SCOPED | explicit covariant CQ path-integral dynamics exists |
| F1 GR/classical limit | PASS_PARTIAL | gravity construction has the intended classical structure |
| F2 consistency | **BLOCKED_MISSING_REQUIRED_OBJECT** | same-realization nonlinear constraint closure/DOF audit absent |
| F3 hierarchy | STRONG_PARTIAL | stochastic classical metric + quantum matter + decoherence/backreaction explicit |
| F4 comparator role | C3b_PARENT_RETAINED | remains a strong comparator in sectors already established |
| F5-F7 | BLOCKED | no downstream promotion after F2 block |

## Comparator consequence for T3-03 / future KG

The PRX 2026 no-entanglement theorem strengthens C3b as an adversary in a very specific way:

- classical spacetime may remain CP and covariant;
- it may produce stochastic gravitational response/decoherence;
- but the classical field itself cannot mediate entanglement in the stated construction.

Therefore a gravity-attributed non-entanglement-breaking channel is a serious discriminator against this scoped C3b realization, but only after C4/C6 hidden quantum transfer is excluded.

## Candidate Gravity design lesson

Future KG must pass **both** kinds of consistency:

1. representation/action consistency: covariance, CP/unitarity/positivity, Ward/Bianchi form;
2. dynamical physical-state consistency: constraint closure, gauge reduction and physical DOF.

One cannot substitute for the other.

## Reopen condition

Reopen T3-04 only when a public same-realization analysis derives the nonlinear constraint/physical-state structure of the covariant CQ gravity path integral (or an explicitly equivalent formulation) far enough to evaluate `H_i,H_0,Closure,Bianchi,DOF` together.

## Terminal completion

**100% — terminally classified as BLOCKED, not FAIL.**

## Sources

1. J. Oppenheim, Z. Weller-Davies, JHEP 02 (2022) 080.
2. J. Oppenheim, C. Sparaciari, B. Soda, Z. Weller-Davies, Phys. Rev. A 113, 052223 (2026).
3. J. Oppenheim, Z. Weller-Davies, Phys. Rev. X 16, 031007 (2026).
4. J. Oppenheim, M. Sajjad, arXiv:2605.05375 (2026), retained as a separate linearized comparator realization.
