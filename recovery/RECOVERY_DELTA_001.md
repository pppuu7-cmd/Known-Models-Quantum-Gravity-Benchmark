# KMQGB Recovery Delta 001

Date: 2026-09-08
Iteration: KMQGB-001
Type: repository migration / authority isolation / continuation bootstrap

## What changed

1. Migrated all seven source benchmark artifacts from RQIR branch `rqir7-known-models-benchmark` into standalone repository `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`.
2. Removed the redundant `known_models_benchmark/` path prefix in the standalone repository.
3. Rewrote recovery references so the benchmark can no longer resume by writing into the main RQIR repository.
4. Hardened the Candidate Gravity/KMQGB firewall: all KMQGB writes are local to this repository; RQIR is read-only external authority.
5. Added migration provenance, benchmark matrix, research log, and current-front recovery state.
6. Refreshed external RQIR context: `main` SHA `5fed1f52c013e9e469be73596e2c80932289c725`, authoritative Iteration 563, MODEL_READINESS 24%, active rank10 heavy computation.

## Scientific state preserved

Current realization: `RQIR7-M01-GR-EH-MINK`.
Current nonterminal status: `BLOCKED_PROTOCOL_MISMATCH`.
First blocker: `FROZEN_PROTOCOL_LITERAL_MAPPING`.
No scientific failure is inferred.

The following GR facts remain supported in the declared weak-field scope: two physical tensor modes, conventional massless graviton pole structure after gauge fixing, diffeomorphism/Bianchi source-conservation structure, hyperbolic formulations and retarded response, and Einstein-Hilbert nonlinear self-interaction hierarchy. These facts do not by themselves establish the frozen RQIR comparator identity.

## Exact unresolved authority

- literal Q1–Q7 definitions;
- literal frozen comparator basis/span and provenance;
- literal quotient/residual acceptance rule;
- exact Source/Ward/contact+K2 target contract and applicable domain conventions.

## Runner/resource decision

Because RQIR currently reports a live heavy rank10 computation, KMQGB does not dispatch competing heavy work to the shared self-hosted runner in this iteration.

## Next actions

1. Traverse RQIR repository authority read-only to locate the four unresolved frozen objects.
2. Pin each by exact path and commit/blob SHA in `protocol/FROZEN_RQIR_PROTOCOL_REFERENCE.md`.
3. Re-evaluate GR null control under those literal rules.
4. If exact baseline identity is proven, set GR to `EXACT_COMPARATOR_IDENTITY` and quotient residual 0; otherwise freeze the precise blocker/failure without broadening the claim.
5. Begin concrete low-energy GR+QG EFT control.
