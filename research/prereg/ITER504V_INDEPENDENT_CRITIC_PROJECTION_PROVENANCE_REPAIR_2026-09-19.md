# Iter504V independent Critic projection/provenance repair preregistration

GATE: ITER504V_INDEPENDENT_CRITIC_REPAIR

STATUS: PROSPECTIVELY_FROZEN_BEFORE_REPAIR_IMPLEMENTATION

Parent source run:
- run: 35365466861
- head: d10ccd5f9bb465d306dad0b74bedfd3ecf5ad05e
- source metadata freeze: 7a60b8450ae6ecd1023f3f1a012e4a0b5b443ea4
- source science changed: false
- source rerun authorized: false

Prior Critic launch:
- authority: 486061ea90810bbc91a87e984cca15ec580e98b6
- launch commit: 7b0a8a6c8048020fbff29a0ae99c121c102f54a0
- scientific payload consumed: false
- status for authority purposes: PRE_SCIENCE_CRITIC_INFRASTRUCTURE_DEFECT

Prospectively identified defects:
1. The independent Critic decision projection omitted the frozen assembler's parent_inclusion projection, so exact assembly binding would be incomplete / deterministically disagree.
2. Provenance binding must additionally require computed case.json SHA256 maps to equal the frozen assembly case_file_sha256 maps.
3. Assembly file SHA256 values must be checked against the source aggregate lane_a_sha256 / lane_b_sha256 values.
4. Source aggregate classification, projection hashes, counterexample identities, constants, and exact cross-environment decision agreement must be reconstructed rather than trusted.

Repair scope:
- Critic-only implementation/workflow repair.
- No source case, cohort, constants, classifier, or artifacts may change.
- Critic still runs independently under Python 3.11 and Python 3.13.
- Exact semantic agreement is required.
- Negative controls remain required, including C4_true_leaf_false_rho, premature_unresolved_leaf_depth, midpoint_binding, and tree_partition_binding.
- No Phase B authorization.

Allowed terminal classifications:
- ITER504V_SENTINEL_LOCAL_D_NO_COUNTEREXAMPLE_SCOPED
- ITER504V_SENTINEL_LOCAL_D_COUNTEREXAMPLE_TO_UNIFORM_CERTIFICATION_SCOPED
- ITER504V_SENTINEL_INVALID
