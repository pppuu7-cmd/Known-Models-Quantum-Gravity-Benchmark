# ITER504T_PRETERMINAL_CRITIC_DEFECT_BINDING_VERIFICATION_GATE — terminal result

Date: 2026-09-17
Status: TERMINAL

## Authority

- Closure gate: `ITER504T_PRETERMINAL_CRITIC_DEFECT_BINDING_VERIFICATION_GATE`.
- Prospective preregistration commit: `152e155692f80447cf75a97b86e17450a05534d6`.
- Frozen authority commit: `7a921224f8bc472b6cd8b77bea8c2c74463102c0`.
- Verification implementation commit: `76265f3455b50f1861a11a22f16aedf3581a2ada`.
- Aggregate implementation commit: `9fc2226bfc440c2e732f1645036f5ba35235af64`.
- Workflow head: `f3a1ac941c63d92b2842b7fc09532c5463bffa37`.
- Authoritative Actions run: `35192972048`, terminal `completed/success`.
- Jobs: source-lock `105109491926`; Python 3.11 `105109537847`; Python 3.13 `105109537816`; aggregate `105109577215`.
- Artifacts: Python 3.11 `10484507873` / `sha256:08c40f815c33258c3257bcc58369bca1e9683a00ced2d0f09201c9f8388a6029`; Python 3.13 `10484498017` / `sha256:19f01cbae99be78f0edeeb09bc5a00fed8ef652ce5e1225defd90a0df19db7ce`; aggregate `10484253835` / `sha256:7664f90e1fe24633bf8b36ab412a1b9076f30395666b6cf05daecb105e821c76`.
- Lane JSONs are byte-identical, SHA256 `e434469f558a82aabfda08202c6a49bf1b138bff59f3f430327d8835776d6bd9`.
- Lane decision SHA256 `f171fc91f3aa64bc27624601661088909ac928860d07f0f9bf24c8ef1d0a2ec9`.
- Aggregate JSON SHA256 `7fdb4388fc59a1bd21987a18eccb7e5d55e7922c88a53573ec0d70908fe253b7`.
- Aggregate raw log SHA256 `b57d87282e236120cda272cd8dfe4038b90f74e732b3b77a648c03c190d36d81`.
- Aggregate decision SHA256 `b9379768534acb840c56a3c2a9875a57a4badfdceefc0c7b7bac9a6e2984821e`.

Green CI is execution/provenance evidence only.

## Frozen terminal classification

`ITER504T_PRETERMINAL_CRITIC_DEFECT_CLAIMS_NOT_ALL_VERIFIED_SCOPED`

This is a **closure-hypothesis FAIL_SCOPED**, not a scientific FAIL of Iter504T.

The frozen hypothesis was that all three named preterminal Critic defect candidates were supported by the exact launch-head verifier implementation. That all-three hypothesis is false because one candidate is refuted.

## Exact result

Both independent Python lanes agree and all frozen positive/negative controls pass. Exact launch-head blob identities all match.

### C1 — parent-inclusion binding

`FROZEN_COMPONENTWISE_PARENT_INCLUSION_CONTROL_NOT_IMPLEMENTED_OR_RECORDED = VERIFIED`.

- the launch-head producer does not serialize a `componentwise_parent_inclusion` certificate;
- the frozen assembler accepts an otherwise valid exact-dyadic payload with the certificate absent;
- the frozen Critic accepts the same missing-certificate payload;
- no active Iter504T scientific artifact was needed or read.

Therefore this Critic defect candidate remains supported.

### C2 — dyadic split-location binding

`FROZEN_DYADIC_SPLIT_LOCATION_NOT_INDEPENDENTLY_VERIFIED = REFUTED`.

The frozen one-third split fixture for root 13 uses split `11/4800` while retaining the expected metadata string and exact gap-free root cover. Both launch-head validators reject it with two `non_dyadic_cell` errors. The exact `dyadic_cell_valid()` logic checks both the width at declared depth and integer cell position within the root.

Therefore the preterminal Critic audit's specific claim that a non-midpoint one-third split could pass the current assembler/Critic is false for the exact frozen launch-head code. Historical audit text is preserved; this terminal closure result corrects its downstream interpretation.

### C3 — R-cohort binding

`FROZEN_R_COHORT_NOT_INDEPENDENTLY_VERIFIED = VERIFIED`.

When every synthetic `possible_max` row with `R=6` is changed to `R=7` while all other fields are preserved:

- the frozen assembler accepts the changed-R payload;
- the frozen Critic accepts it;
- if both environment payloads carry the same wrong R labels, the Critic cross-environment projection remains identical.

The launch-head validation checks the expected rho tuple and possible-max row count/channel indices, but does not bind the exact R set `{6,8,10,12}`. This Critic defect candidate remains supported.

## New fact

The latest preterminal Critic handoff is partly correct but overstates the verifier defect set. Exactly two of its three named candidates are supported by executable frozen-code counterexamples: missing parent-inclusion recording/binding and missing exact R-cohort binding. Its dyadic-split candidate is refuted because exact rational dyadic-cell validation is already implemented independently in both assembler and Critic.

Consequently, any later terminal Iter504T review must not cite the refuted dyadic defect as a reason for `INVALID_IMPLEMENTATION`. It must still audit the two verified implementation defects against the prospectively frozen contract before accepting a Research PASS or INCONCLUSIVE downstream.

## Scientific firewall

- `active_scientific_artifacts_consumed=false`;
- `active_scientific_run_classified=false`;
- no Iter504T root/leaf/assembly/aggregate scientific values were downloaded, inspected or inferred by this closure gate.

## Claim ceiling

This result validates/refutes only the three named preterminal Critic implementation-defect candidates. It does not classify active Iter504T science, does not establish or refute the three-root continuous-drift mechanism, does not authorize deeper subdivision or a held-out cohort, and does not imply all-1888 closure, D7 closure, model/family failure, Candidate Gravity, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

## Next admissible work

Do not launch another scientific gate while authoritative Iter504T run `35181094204` is active. When it terminalizes, consume only its terminal assemblies/aggregate/Critic/artifact provenance and review the resulting Research classification against the two VERIFIED contract defects above. Preserve the C2 refutation.

If implementation-only repair is required, it may add parent-inclusion computation/serialization and exact R-cohort validation/negative fixture while preserving all frozen science. No dyadic-partition repair is justified by this closure result because that binding is already present.
