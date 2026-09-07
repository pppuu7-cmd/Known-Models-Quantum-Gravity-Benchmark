# RQIR Baseline Comparator Registry — frozen snapshot for KMQGB provenance

Source repository: `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction`
Source path: `candidate_gravity/BASELINE_COMPARATORS.md`
Observed on RQIR `main` at `5fed1f52c013e9e469be73596e2c80932289c725`
Source blob SHA: `a2b45188710c885f979123f77fa7aad2273b9983`
Original registry-introduction commit: `fa841b0f5c4dc9a3f17af52f0ec5477c00b1502a` (Iteration 130)

This is a read-only provenance snapshot copied into KMQGB so a future benchmark session does not need to reconstruct the comparator registry from chat memory. The external RQIR file remains the methodological source of truth for RQIR itself.

## Required comparator classes

### C0 — Classical GR / Newtonian gravity
Use the controlled classical limit appropriate to the experimental regime.
Question: is the claimed signal already reproduced by ordinary classical gravitational dynamics plus the declared matter state and apparatus noise?

### C1 — Semiclassical gravity
Representative structural baseline: `G_mn = 8 pi G <T_mn>` or the appropriate controlled semiclassical EFT formulation.
Question: does the candidate differ beyond mean-source backreaction once source/preparation/calibration freedom is included?

### C2 — Stochastic gravity / noise-kernel baseline
Include models in which stress-energy fluctuations/noise kernels drive classical metric fluctuations.
Question: can the candidate's `N`, response or higher-statistics signature be reproduced by an admissible stochastic source/kernel?

### C3 — Classical-channel / measurement-feedback / postquantum hybrid gravity
Include classical communication, measurement-feedback, stochastic classical metric, and related hybrid constructions that can generate decoherence/noise while mediating effective interactions.
Question: is the proposed discriminator genuinely quantum-gravitational, or only evidence for a broader non-semiclassical classical/hybrid channel?

### C4 — Ordinary quantum matter + quantized/non-gravitational mediator nuisance
Where experimentally relevant, include conventional quantum interactions, electromagnetic/Casimir/patch/technical channels and quantized mediator alternatives that can mimic transfer/correlation structure.

### C5 — Perturbative quantum gravity / low-energy quantum GR
Use as comparator when the candidate claims a modification relative to standard quantized weak-field gravity or when the observable lies in its controlled EFT regime.

### C6 — Full QFT source + classical detector/interface alternatives
Include ordinary QFT source correlations combined with a classical or phenomenological transfer channel.
Question: does the RQIR signal require a quantum gravitational interface, or only quantum source statistics plus a non-quantum transfer map?

## Comparator-state rule

Each tested realization should record one row per applicable comparator with state `DISTINCT`, `DEGENERATE`, `BLOCKED`, or `N/A`, together with observable, nuisance/profile result, and authority.

A claimed difference is publishable only at the weakest level supported after the applicable comparator set and nuisance/profile treatment. Exact identity with an applicable comparator is a genuine negative/degeneracy result, not a consistency failure.
