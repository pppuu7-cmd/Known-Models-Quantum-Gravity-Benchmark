# Imported RQIR reference — ANSATZ-PQG-EFT-001 v0.1

Purpose: preserve provenance of the pre-existing perturbative quantum-GR EFT control so KMQGB does not redo it as if it were new work.

External source repository: `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction`
Instantiation commit: `8f5051b8f9041ba0164b7e734be246188e664e62` (RQIR Iteration 133).

Current source files observed on RQIR main `5fed1f52c013e9e469be73596e2c80932289c725`:

| Source file | Blob SHA | Key authority |
|---|---|---|
| `candidate_gravity/models/ANSATZ-PQG-EFT-001/MODEL.md` | `33b922d209d78a23c1c8086c16a2db9d1dfce818` | concrete weak-field EFT realization; J/N/chiR hierarchy; exact C5 identity statement |
| `candidate_gravity/models/ANSATZ-PQG-EFT-001/GATE_STATUS.yaml` | `6958f8769aed9381c21a6bf7fa45ceecbfb97c01` | QG-001/002/003 PASS; QG-007 `REFERENCE_DEGENERACY_C5`; no promotion |
| `candidate_gravity/models/ANSATZ-PQG-EFT-001/ASSUMPTIONS_LEDGER.md` | `1fc9b40d1f0ddb2c2db104489cf39340fa409ddb` | weak-field/EFT/gauge/renormalization/smearing assumptions; A-008 exact C5 identity |
| `candidate_gravity/models/ANSATZ-PQG-EFT-001/DERIVATION_MAP.md` | `263ae66f07c2c211dd39e1c2b66ab1726bf094c3` | D-008 comparator identity `PROVED_BY_DEFINITION`; D-009 no independent C5 beta direction |

## Imported conclusion

The realization is deliberately the standard low-energy perturbative quantum-GR EFT comparator C5 at theory-class level. RQIR's own source artifact states

`ANSATZ-PQG-EFT-001 == C5`

and retains `CG-NG-003`: exact comparator degeneracy prevents promotion as a novel Candidate Gravity, but is not a consistency failure of perturbative quantum GR EFT.

KMQGB translates this existing negative/control result into its status ontology as `EXACT_COMPARATOR_IDENTITY`, not `FAIL_RQIR_CONSISTENCY`.

This provenance file is a KMQGB record only. No source RQIR files were modified.
