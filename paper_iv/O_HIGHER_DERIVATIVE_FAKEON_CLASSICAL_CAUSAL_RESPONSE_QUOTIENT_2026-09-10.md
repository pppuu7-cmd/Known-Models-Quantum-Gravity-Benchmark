# Higher-derivative fakeon gravity — classical causal-response attribution quotient

**Date:** 2026-09-10  
**KMQGB iteration:** 189  
**Parent family:** `PERTURBATIVE_HIGHER_DERIVATIVE`  
**RQIR Core:** v1.0 FROZEN

## Frozen question

Can the classical fakeon response kernel, by itself, identify the fakeon quantization prescription relative to same-action alternative prescriptions?

## Same-realization physical object

Use the fixed higher-derivative realization whose massive spin-2 mode is quantized as a fakeon. In the tree/classical limit, the fakeon prescription gives the principal-value propagator

`PV[1/(p^2-m^2)] = 1/2 (G_ret + G_adv)`

and, in the toy response representation, the projected response is a symmetric nonlocal average over past and future values with characteristic scale set by the fakeon mass/time scale.

For gravity, the classicized projection similarly integrates out the fake spin-2 field by the half sum of retarded and advanced Green functions before reinserting the projected field into the physical equations.

## Primary authority

Anselmi, *Fakeons, Microcausality And The Classical Limit Of Quantum Gravity*, arXiv:1809.05037, gives the tree fakeon principal-value propagator and explicitly states that different quantization prescriptions may have the same classical limit, so the fakeon prescription cannot be inferred from that principal-value expression alone. The same paper derives the projected gravitational equations by solving for the fake spin-2 field with the half-retarded plus half-advanced Green function.

Anselmi and Piva, *Quantum Gravity, Fakeons And Microcausality*, arXiv:1806.03605 / JHEP 11 (2018) 021, shows that prescription-sensitive causal information survives at the quantum/dressed level through fakeon widths and threshold structure; the spin-2 fakeon has a negative width and causality violation above the fakeon mass scale.

## RQIR comparator logic

Define the classical response object

`O_cl = K_PV`,

where `K_PV` is the projected principal-value / half-retarded-plus-half-advanced kernel in the declared linearized/classical regime.

Because the primary source explicitly warns that distinct quantization prescriptions can share this classical limit, there exists at least one admissible same-action comparator direction `Q_alt` such that

`O_cl(fakeon) = O_cl(Q_alt)`.

Therefore the fakeon-attribution residual in this classical kernel is

`delta O_classical-attribution = 0`

on the shared domain. After whitening and projection against any comparator space containing that same-classical-limit direction,

`Pi_perp Sigma^(-1/2) delta O_classical-attribution = 0`.

This is an attribution non-identifiability result. It does **not** say that the response is causal; the advanced component is precisely the source of microcausality violation. It says that this classical response object alone does not uniquely certify the underlying fakeon quantization prescription.

## Classification

**`PASS_RQIR_GATE__SCOPED_FAKEON_CLASSICAL_CAUSAL_RESPONSE_QUANTIZATION_NONIDENTIFIABILITY`**

Residual:

**`EXACT_ZERO_FAKEON_ATTRIBUTION_RESIDUAL_IN_CLASSICAL_PRINCIPAL_VALUE_RESPONSE_BLOCK`**.

This is a negative uniqueness result, not a scientific FAIL of fakeon gravity.

## What remains genuinely prescription-sensitive

The primary literature identifies the correct next discriminator as a quantum/dressed object rather than the classical principal-value kernel alone. Candidate objects include:

- dressed fakeon pole/width and sign;
- average-continuation threshold structure;
- absorptive self-energy around the fakeon mass;
- a normalized time-domain response derived from the dressed prescription with a comparator using the same local action;
- beyond-leading inflationary quantities if they depend on the quantization prescription itself.

Any future terminal fakeon discriminator must carry the same-realization action, pole/width normalization, physical-state rule, threshold prescription, common-domain comparator, and remainder/error ledger.

## Family consequence

No family-level promotion is allowed. `PERTURBATIVE_HIGHER_DERIVATIVE` remains `PARTIAL_SUBFAMILY_ONLY` because other material quantization branches remain nonterminal and the quantum/dressed fakeon causal observable has not yet been placed into a full comparator quotient.

## Refined next gate

`HIGHER_DERIVATIVE_FAKEON_DRESSED_POLE_WIDTH_THRESHOLD_COMPARATOR_CERTIFICATE`

Minimum payload:

1. fixed quadratic-gravity action and fakeon branch;
2. renormalized spin-2 pole and width with sign convention;
3. average-continuation / threshold prescription;
4. normalized physical observable sensitive to that prescription;
5. same-action alternative-quantization comparator on the same kinematic domain;
6. uncertainty/remainder and perturbative-validity domain;
7. no promotion from child to family without material-branch coverage.

## D7 consequence

D2 and D4 remain open at family level; D7 remains `NOT_CLOSED`; `NEW_REQUIRED` remains unauthorized; Candidate Gravity remains inactive at R3=24%.
