# Model Audit — modern postquantum classical gravity

Benchmark ID: KMQGB-S2-M04-POSTQUANTUM-CLASSICAL
Concrete realization ID: PQCG-MINK-STOCHASTIC-MODES-2026-001
Role: modern C3b postquantum classical-spacetime comparator
State: ACTIVE / NONTERMINAL

## Frozen starting realization

Use the 2026 Oppenheim–Sajjad linearized Minkowski stochastic-mode realization of postquantum classical gravity, derived from the classical–quantum path integral.

Declared features from the source realization:

- spacetime metric remains fundamentally classical;
- quantum matter is coupled to it through a classical–quantum framework;
- mathematical consistency requires stochastic metric evolution;
- linearization around Minkowski plus scalar-vector-tensor decomposition;
- dynamical stochastic spin-2 and spin-0 modes diffusing around their respective wave equations;
- additional non-dynamical vector/scalar sectors;
- positive-semidefinite action on all dynamical modes in the analyzed sector;
- calculable two-point function / power spectral density for Newtonian-potential fluctuations;
- current phenomenological handles from LISA Pathfinder, stochastic-GW bounds and decoherence experiments.

This is an explicit 2026 realization, not the generic phrase "postquantum gravity".

## Why the audit is not yet terminal

The source literature now contains an important tension that must be resolved at the exact-realization level before a consistency verdict:

1. Oppenheim–Sajjad (2026) present the stochastic-mode action as positive semidefinite on all dynamical modes and discuss consistency between several pure-gravity stochastic formulations.
2. Hirotani–Matsumura (2026), analyzing the original white-noise Oppenheim-type kernel in geodesic deviation, find that the simple kernel may not strictly satisfy the Bianchi identities and construct a modified transverse kernel that is manifestly Bianchi-consistent.
3. Earlier constraint-algebra work for a broad discrete postquantum class found non-closure without additional constraints; this cannot be transferred blindly to every later realization, but it is a retained warning.

Therefore the benchmark must identify whether these papers are testing exactly the same kernel/action/convention before declaring either a consistency PASS or FAIL.

## Current F0-F7 map

| Gate | State | Reason |
|---|---|---|
| F0 dynamics | PASS_SCOPED | explicit classical-quantum path-integral / stochastic-mode realization exists |
| F1 required limits | PASS/PARTIAL | GR classical limit is part of the program; exact parameter/domain matching retained |
| F2 consistency | BLOCKED_REALIZATION_RECONCILIATION | PSD dynamical modes are positive evidence, but Bianchi/noise-kernel compatibility must be reconciled for the exact frozen realization |
| F3 RQIR hierarchy | STRONG_PARTIAL | stochastic metric modes, two-point PSD and matter decoherence channels are concrete |
| F4 comparator distinction | EXACT_MEMBER_OF_C3B_IF_CONSISTENT | postquantum classical gravity is a retained C3 comparator class, but consistency gate precedes comparator closure |
| F5 | BLOCKED | cannot promote before F2 and exact observable quotient |
| F6 | BLOCKED | cannot precede F5 |
| F7 | PARTIAL_RESOURCE_EVIDENCE | LISA/LIGO/decoherence constraints exist, but no final resource certificate before upstream closure |

## Current phenomenological evidence

Oppenheim–Sajjad compute Newtonian-potential fluctuation spectra and compare them with LISA Pathfinder excess noise, while stochastic gravitational-wave constraints bound another coupling combination.

Hirotani–Matsumura derive geodesic-deviation strain spectra and argue that simple white-noise realizations are testable with current gravitational-wave sensitivity. They also find parameter regions where the original noise kernel is not positive semidefinite and identify a far-future divergence for the scale-free white-noise model in their approximation.

These are meaningful model constraints; they are not yet a universal rejection of all postquantum classical gravity.

## Current first blocker

`PQCG_KERNEL_BIANCHI_PSD_RECONCILIATION`:

1. identify the exact noise/decoherence kernel used in `2605.05375` and compare it term-by-term with the "original" white-noise kernel critiqued in `2603.29230`;
2. determine whether the Bianchi critique applies to the same stochastic realization or only to a simplified phenomenological kernel;
3. if the same realization fails transversality/Bianchi compatibility, assign a scoped F2 failure;
4. if not, freeze the Bianchi-consistent kernel and continue to the C3b comparator quotient;
5. retain observational exclusions only for the parameter/kernel slices actually tested.

## Current completion estimate

Operational completion: **35%**.

## Sources

1. J. Oppenheim, M. Sajjad, *Stochastic modes in postquantum classical gravity*, arXiv:2605.05375 (2026).
2. T. Hirotani, A. Matsumura, *Testing classical-quantum gravity with geodesic deviation*, Phys. Rev. D 114, 026014 (2026), arXiv:2603.29230.
3. J. Oppenheim, Z. Weller-Davies, *The constraints of post-quantum classical gravity*, JHEP 02 (2022) 080, arXiv:2011.15112.
4. J. Oppenheim, *A Postquantum Theory of Classical Gravity?*, Phys. Rev. X 13, 041040 (2023).
