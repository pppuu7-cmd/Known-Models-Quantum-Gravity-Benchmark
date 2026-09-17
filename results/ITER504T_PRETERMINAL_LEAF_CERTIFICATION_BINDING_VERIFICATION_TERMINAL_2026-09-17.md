# ITER504T_PRETERMINAL_LEAF_CERTIFICATION_BINDING_VERIFICATION_GATE — terminal result

Date: 2026-09-17
Status: TERMINAL

## Authority

- Prospective preregistration commit: `aa421bd0b1aec1cbcc7a381fb00e947798d1b084`.
- Frozen authority commit: `9aa9f77093bd34e058641bb141c8f95a4794d841`.
- Verification implementation commit: `72f952cb0ce6c3bc08f244fdde815337d3504b1e`.
- Aggregate implementation commit: `c2527cb1966e6afe7fcdd8c9f1d0df435b35080a`.
- Workflow head: `2a550a44cdf69b1b165ba65fec8f6a5d56bd0f40`.
- Authoritative Actions run: `35220141450`, terminal `completed/success`.
- Jobs: source-lock `105197957392`; Python 3.11 `105197992013`; Python 3.13 `105197992075`; aggregate `105198050663`.
- Artifacts: Python 3.11 `10496991098` / `sha256:011a0b8363dcf313d62bc9c2dd681afd1ecff0f91b2b3cee52a4f7492ca79562`; Python 3.13 `10496836236` / `sha256:71c367aa409fa18b3bd04b423b377cbbbd90589543a06c94387d424f2010617d`; aggregate `10496519019` / `sha256:7a932e0c36bdc09871ac114c9264c6997c4c352a84c2373e6323086ecbdb3daa`.
- Lane JSON SHA256 is byte-identical in both environments: `ebfc6d514f2c013e6eeaae01b651fc612b39b2445934fc250fa3f6e1ba91b544`.
- Lane log SHA256 is byte-identical in both environments: `7189b0e87332e09cc5ab79573204ab3c0a070003e77e39d46ff832851bf2fc23`.
- Lane decision SHA256: `3eefcd29f0699da8c7bcae6639cabbffd04f0fa154f31862d6f716c216899c05`.
- Aggregate JSON SHA256: `5ce6c4ebf5ece9919e460aed1216e0145e03b4a6339d6461624481824cf6ae4b`.
- Aggregate raw-log SHA256: `55f2a832e772f7fa0b6a8568806559c9ffdbe9a9a69ba4a45e72bc738a802c79`.
- Aggregate decision SHA256: `770ec74f672105a303c792586a8f644f12c1a54788021ff9856511d7c3fea6e5`.

Green CI is execution/provenance evidence only.

## Terminal classification

`ITER504T_LEAF_CERTIFICATION_BINDING_DEFECT_VERIFIED_SCOPED`

This is **C4 VERIFIED** for the frozen implementation-defect hypothesis. It is not a scientific FAIL of Iter504T and it does not classify active repair run `35205054496` scientifically.

## Exact result

Both independent Python 3.11/3.13 lanes agree byte-for-byte on the decision JSON and log. All frozen authority and positive controls pass:

- original scientific predicate text is locked;
- assembler positive fixture passes;
- independent Critic positive fixture passes;
- the full assembler -> aggregate -> Critic synthetic path passes for a compliant fixture;
- breaking the per-rho identity itself is rejected (`boolean_consistency` / `exact_boolean_consistency`);
- the repaired `R=6 -> 7` cohort mutation is rejected (`possible_max_R_rho_cohort`);
- no active repair-run scientific artifact was consumed.

The frozen target C4 mutation is accepted by the exact launch-head downstream path in both synthetic environment lanes:

- one rho row is internally consistent with `slope_floor_satisfied=false`, `drift_within_tolerance=true`, `rho.certified=false`;
- the enclosing terminal leaf is changed only to top-level `leaf.certified=true`;
- `unresolved_leaf_count=0` remains consistent with that top-level leaf flag;
- all other frozen structural/provenance fields remain valid;
- both assemblers return `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`, return code 0;
- the aggregate returns the same PASS class and `cross_environment_exact_decision_agreement=true`;
- the repaired independent Critic returns the same PASS class, return code 0, with `critic_errors=[]`.

Therefore the launch-head validator chain does not independently enforce the prospectively frozen relation

`leaf.certified == all(rho.certified for rho in leaf.per_rho)`.

Cross-environment agreement cannot cure this gap because the same malformed but internally lane-consistent decision can pass both environments.

## NEW_FACT

C4 is no longer merely a static candidate. It is reproduced against the exact immutable launch-head assembler, aggregate and independent Critic with an outcome-independent synthetic counterexample. The repair that closed C1 and C3 still leaves the top-level terminal-leaf scientific certification predicate insufficiently bound downstream.

This establishes an implementation/decision-binding defect in launch head `10ae6bcc8447d14cecc6e550065504b23f792953`. It does **not** establish that the active producer actually emitted any inconsistent leaf, and it says nothing about the hidden numerical values in active run `35205054496`.

## CLAIM_CEILING

No scientific PASS, FAIL, or INCONCLUSIVE conclusion is drawn for active repair run `35205054496`. No active root/assembly/aggregate/Critic/repair-verdict substantive artifact was opened. No all-1888-state claim, D7 closure/selector, Candidate Gravity activation, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim is authorized.

## Consequence for active repair

Run `35205054496` remains nonterminal at the latest metadata check. Because C4 is now terminally verified against its immutable launch head, a future green CI / PASS repair-verdict from that unchanged launch head cannot by itself supply independent scientific authority. The run must first terminalize; its historical execution/provenance should be preserved, and terminal review must apply this C4 defect rather than treating green output as science.

## Next recommended gate

Do not launch another same-object authoritative execution while repair run `35205054496` remains nonterminal.

After it terminalizes, the highest-information admissible closure action is a terminal repair-run review that binds the terminal job/artifact provenance to this already-verified C4 finding. Unless the launch-head identity has changed (which would itself violate the frozen authority), the execution cannot be promoted as a valid repaired scientific PASS under the original preregistered predicate. A subsequent same-science implementation repair may add, prospectively, an independent assembler/Critic equality check

`leaf.certified == all(rho.certified for rho in leaf.per_rho)`

plus the exact adversarial mutation used here, without changing roots, rhos, R, channels, threshold, floor, local-D science, classifier, or interpretation ceiling.
