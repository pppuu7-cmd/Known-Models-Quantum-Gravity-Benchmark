# KMQGB Research Log

## 2026-09-08 — KMQGB-001 — standalone migration and authority isolation

- Created standalone benchmark authority in `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`.
- Identified the exact source as RQIR branch `rqir7-known-models-benchmark`, source HEAD `782df9af3af1ca55ca4f9bf143e2723a7a8f18bc`, base `02ad31e89f1df0d5515779e6b7526e8eb5505667`.
- Migrated all seven benchmark artifacts from `known_models_benchmark/` into root-level standalone paths.
- Rewrote recovery plumbing so future KMQGB work cannot accidentally write benchmark state into the main RQIR repository.
- Preserved RQIR source branch and `main` unchanged.
- Observed external RQIR authority at SHA `5fed1f52c013e9e469be73596e2c80932289c725`, authoritative research Iteration 563, MODEL_READINESS 24%, with rank10 heavy computation active.
- KMQGB heavy-compute policy therefore remains lightweight/read-only with respect to the shared runner until RQIR heavy work is no longer active or a separate runner is explicitly available.
- Current benchmark realization remained GR Einstein–Hilbert, Lambda=0, weak-field Minkowski.
- Initial scientific blocker was literal recovery of frozen Q1–Q7, comparator span, quotient/residual rule, and source/Ward/contact/K2 target contract.

## 2026-09-08 — KMQGB-002 — protocol recovery, two terminal controls, semiclassical start

### Literal protocol recovery

- Recovered Q1–Q7 and base residual authority from external RQIR `README.md`, blob `e431df35d929aa8b06b1b1369a2dc80352efe9e9`.
- Recovered comparator registry C0–C6 from `candidate_gravity/BASELINE_COMPARATORS.md`, blob `a2b45188710c885f979123f77fa7aad2273b9983`, introduction commit `fa841b0f5c4dc9a3f17af52f0ec5477c00b1502a`.
- Recovered F0–F7 existing-model funnel semantics from `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`, blob `2757e8fe1004b5c0caef51d6d9fee6f982ac81d4`.
- Recovered the fail-closed fixed-comparator preflight semantics from Iteration 504 commit `9af20b657eb89114a954b55b75b59bb3cf284777` and the current RQIR front.

### M01 — GR null control

- The declared classical Einstein–Hilbert weak-field realization is literally the C0 Classical GR comparator in its overlap domain.
- By the RQIR residual definition `Delta_A = O_A^model - O_A^baseline`, exact C0 identity gives analytic zero residual in the declared baseline domain.
- Terminal status: `EXACT_COMPARATOR_IDENTITY`.
- Interpretation: successful null-control recognition, not a consistency failure of GR.

### M02 — perturbative quantum GR EFT

- Located the existing RQIR concrete reference `ANSATZ-PQG-EFT-001` v0.1, instantiated at Iteration 133 commit `8f5051b8f9041ba0164b7e734be246188e664e62`.
- Imported provenance for MODEL, GATE_STATUS, ASSUMPTIONS_LEDGER and DERIVATION_MAP without modifying RQIR.
- Source RQIR explicitly states `ANSATZ-PQG-EFT-001 == C5`; D-008 marks this comparator identity `PROVED_BY_DEFINITION` and QG-007 records `REFERENCE_DEGENERACY_C5`.
- KMQGB terminal status: `EXACT_COMPARATOR_IDENTITY`.
- Interpretation: exact non-novelty relative to identical C5, not an inconsistency of perturbative quantum GR EFT.

### M03 — semiclassical gravity

- Activated concrete control `SCG-MINK-SCALAR-LR-001`: renormalized semiclassical Einstein equation with free scalar quantum matter and Minkowski linear-response control.
- Added initial audit using Hu–Verdaguer semiclassical equation/renormalization and Anderson–Molina-París–Mottola flat-space linear-response stability evidence.
- Current blocker: freeze exact scalar mass/coupling, state, renormalization/counterterm convention and observable domain before terminal comparator classification.

### Progress

- Terminal queue coverage: `2/9 = 22.22%`.
- Current active target: M03 semiclassical control.
- No heavy KMQGB job dispatched because external RQIR still reports shared-runner heavy rank10 work.

## 2026-09-08 — KMQGB-003 — semiclassical/stochastic closure and first nontrivial modified-gravity target

### M03 — semiclassical gravity closed

- Froze `SCG-MINK-SCALAR-LR-001` to one massless (`m=0`) conformally coupled (`xi=1/6`) free real scalar in the Minkowski vacuum.
- Froze `Lambda_ren=0` and renormalization condition `<0|T_ab^R[eta]|0>=0` while retaining finite curvature-squared coefficients `alpha(mu), beta(mu)` explicitly rather than hiding or zero-filling them.
- Declared low-curvature, gauge-invariant linear response on scales much larger than the Planck length as the validity domain.
- Anderson–Molina-París–Mottola's arbitrary-mass/arbitrary-curvature-coupling Minkowski analysis contains this parameter slice and supports scoped flat-space stability after unphysical Planck-scale runaway handling.
- Hu–Verdaguer supplies the renormalized semiclassical equation and the exact mean-vs-stochastic distinction.
- F0–F2: scoped pass in the declared domain.
- F3: mean source `J=<T>` is present; mean-only closure remains insufficient for full QG promotion when an independent quantum/stochastic metric-noise/operator hierarchy is required.
- F4: exact identity with C1 by comparator definition.
- Terminal status: `EXACT_COMPARATOR_IDENTITY`; matched C1 quotient residual `0`.
- Semantic guardrail: this is not a general failure of semiclassical gravity.

### M04 — stochastic gravity instantiated and closed

- Froze `SG-MINK-CONFORMAL-EL-001` using the same conformal-scalar Minkowski state but the Einstein-Langevin stochastic extension.
- Added zero-mean classical stochastic tensor source `xi_ab` with covariance equal to the stress-tensor noise kernel `N_abcd=(1/2)<{t_ab,t_cd}>`.
- Retained the CTP/influence-functional linkage of mean source, fluctuations/noise and dissipative/retarded response.
- F3 is a strong comparator pass because `J`, `N` and response are derived from one open-system parent structure.
- F4 is exact identity with C2 by comparator definition.
- Terminal status: `EXACT_COMPARATOR_IDENTITY`; matched C2 quotient residual `0`.
- Design lesson: classical stochastic metric noise and symmetrized two-point metric fluctuations alone are not sufficient evidence for a quantum gravitational mediator.

### M05 — metric f(R) activated

- Froze `FR-R2-MINK-001` with action `S=(M_Pl^2/2) int sqrt(-g)[R+R^2/(6M^2)] + S_m`, `M^2>0`.
- Around Minkowski, `F(0)=1>0` and `f_RR=1/(3M^2)>0`; the weak-field spectrum contains the GR massless spin-2 mode plus one extra scalaron of mass `M`, with no extra massive spin-2 pole from the pure `R^2` correction.
- F0–F2 are preliminarily scoped-pass in the declared Minkowski domain.
- F3 is classical/partial: deterministic modified gravity does not provide an independent QG noise/operator hierarchy.
- F4 is preliminarily distinct from C0 for traceful sources at finite `M`, but broader identifiability is open.
- First blocker: `FR_QUOTIENT_OBSERVABLE_FREEZE` — derive one explicit scalar-trace observable, exact GR-subtracted residual and full nuisance/comparator quotient.

### External RQIR state and compute firewall

- External RQIR `main` observed at `6839864cc6a2fa66616696db6b9f78b7b8b019f2`, authoritative research Iteration 564, MODEL_READINESS 24%.
- Rank10 run `34165534613` was directly checked and remains `in_progress`.
- No KMQGB heavy job was dispatched to the shared runner.

### Progress

- Terminal queue coverage: `4/9 = 44.44%`.
- M03 current-task completion: `100%`.
- M04 current-task completion: `100%`.
- New active task M05 operational completion estimate: `40%`.
