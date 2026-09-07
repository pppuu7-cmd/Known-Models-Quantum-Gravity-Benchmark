# Model Audit — perturbative quantum GR as low-energy EFT

Benchmark ID: KMQGB-M02-GR-QG-EFT
Imported concrete realization: `ANSATZ-PQG-EFT-001` v0.1
Role: EFT / comparator control
State: TERMINAL
Final status: `EXACT_COMPARATOR_IDENTITY`

## Why this realization is concrete enough

RQIR already instantiated this model at Iteration 133 rather than merely naming the broad idea “quantum GR EFT”. The realization fixes:

- background split `g_mn = eta_mn + kappa h_mn`, `kappa=sqrt(32 pi G)`;
- one real scalar matter field;
- Einstein–Hilbert + scalar matter + covariant gauge fixing + ghosts + EFT operators;
- weak-field, asymptotically Minkowski, `E << M_Pl` domain;
- BRST/physical-state separation;
- matter-gravity interaction `S_int^(1)=-(kappa/2) int h_mn T^mn`;
- common source hierarchy `J=<T>`, centered symmetrized `N`, and retarded `chi^R` from the same matter dynamics/CTP structure.

External authority is recorded in `legacy_rqir/ANSATZ-PQG-EFT-001_PROVENANCE.md`.

## RQIR source-state evidence

The imported RQIR `GATE_STATUS.yaml` records:

- QG-001 PASS — perturbative state space / BRST separation;
- QG-002 PASS — one covariant EH+matter EFT action;
- QG-003 PASS — classical/Newtonian limit in the declared reference branch;
- QG-004 not tested in that historical closure;
- QG-005 blocked for a complete relational detector-observable audit;
- QG-006 not tested in full;
- QG-007 FAIL with reason `REFERENCE_DEGENERACY_C5`;
- QG-008–010 blocked because no independent beta direction exists relative to C5.

Those historical incomplete validation gates do not erase the exact theory-class comparator fact. KMQGB is not promoting this realization as a new theory; it is testing whether the benchmark correctly recognizes a permanent reference comparator.

## Exact comparator identity

The literal RQIR comparator registry defines C5 as perturbative quantum gravity / low-energy quantum GR.

The RQIR MODEL authority states explicitly:

`ANSATZ-PQG-EFT-001 == C5` at the declared theory-class level.

The RQIR derivation map records this identity as `PROVED_BY_DEFINITION`. Therefore there is no independent C5-distinguishing model direction. In KMQGB terms this is not `FAIL_RQIR_CONSISTENCY`; it is the expected terminal comparator result:

`EXACT_COMPARATOR_IDENTITY`.

## Evidence table

| Field | Result | KMQGB interpretation |
|---|---|---|
| Exact realization | `ANSATZ-PQG-EFT-001` v0.1 | concrete RQIR reference imported by provenance |
| Action | EH + real scalar + gauge fixing + ghosts + EFT higher operators | fixed low-energy theory class |
| Regime | weak-field, asymptotically Minkowski, sub-Planckian EFT | explicit |
| Physical DOF | BRST physical graviton sector + matter Fock space | gauge modes excluded from observables |
| GR limit | leading classical order -> GR; Newtonian static limit historically checked | supported in source RQIR |
| Source hierarchy | `J`, `N`, `chi^R`, higher CTP correlators from same dynamics | structurally mapped |
| Gauge/Ward | perturbative diffeomorphism/BRST structure | historical full detector audit incomplete |
| Renormalization/smearing | required before numerical local composite-operator values | declared unresolved assumptions, not hidden |
| Comparator | C5 low-energy perturbative quantum GR | exact theory-class identity |
| Distinct beta direction | none versus C5 | exact degeneracy |
| Terminal KMQGB status | `EXACT_COMPARATOR_IDENTITY` | expected comparator-control success |

## Q1–Q7 relevance

This control is especially relevant to Q7 (low-energy quantum gravity EFT) and structurally supplies Q3/Q5 response/noise objects through the shared stress-tensor/CTP hierarchy. It may also feed Q1/Q2/Q4/Q6 only after an explicit observable setup is chosen. KMQGB does not infer a universal numerical fingerprint from theory-class identity alone.

## Scientific meaning of the negative result

The result means: standard perturbative quantum GR EFT cannot be advertised as a **new theory distinct from C5**, because C5 is that theory class. It does **not** mean low-energy quantum GR EFT is inconsistent or experimentally false.

This is a valuable positive control of the benchmark taxonomy: the funnel recognizes a viable known theory as scientifically non-novel relative to an identical comparator rather than misclassifying it as inconsistent.

## Source authority

- RQIR Iteration-133 instantiation commit: `8f5051b8f9041ba0164b7e734be246188e664e62`.
- MODEL blob: `33b922d209d78a23c1c8086c16a2db9d1dfce818`.
- GATE_STATUS blob: `6958f8769aed9381c21a6bf7fa45ceecbfb97c01`.
- ASSUMPTIONS_LEDGER blob: `1fc9b40d1f0ddb2c2db104489cf39340fa409ddb`.
- DERIVATION_MAP blob: `263ae66f07c2c211dd39e1c2b66ab1726bf094c3`.

## Next benchmark

Start a concrete semiclassical-gravity realization as KMQGB-M03. It must be treated as C1 baseline/control in its declared domain, not as a single verdict on all semiclassical gravity.
