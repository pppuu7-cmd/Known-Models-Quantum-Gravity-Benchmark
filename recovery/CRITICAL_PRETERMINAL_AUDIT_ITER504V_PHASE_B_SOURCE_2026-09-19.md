# Independent Critical Review — preterminal Iter504V Phase-B source audit

Date: 2026-09-19
Lane: independent KMQGB Critical Review / Verification
Status: `PRETERMINAL_NO_SCIENTIFIC_VERDICT`

## Scope

Exactly one active substantive Research object is reviewed preterminally:

- gate: `ITER504V_BROADER_DOMAIN_COMPLETE_Q1_COVERAGE`;
- source execution gate: `ITER504V_PHASE_B_SOURCE_EXECUTION`;
- preregistration commit: `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
- implementation authority: `42a2f035a80c474ebc7e5f57934ad9ba78ce9937`;
- static implementation review: `eaa2d1ef84fe8370f33cec360233f60571f9bcd0` (`PASS_SCOPED`);
- execution authority: `caf67585a9fad990dd90948df51839e6ed7cf891`;
- immutable launch head: `31fcdacffcc394e96b73917083281edb90d6753c`;
- source run: `35405065903`, attempt 1.

Fresh Actions state is nonterminal. Source-lock job `105792998164` completed `success`; source case matrix jobs are active/nonterminal. No case, leaf, slope, drift, certification, assembly, aggregate or counterexample scientific value was consumed in this audit.

## Chronology / provenance precheck

Chronology is prospective:

1. terminal Phase-A parent `d03cae09c04638cb02412435a284cfd9acdf8406`;
2. Phase-B preregistration `e42caf47f9201d79cd89b79dc72b90f696e3ec5d`;
3. design authority/static review;
4. implementation authority `42a2f...` before implementation;
5. implementation and workflow hardening;
6. static implementation review `eaa2d1...` before execution authority;
7. execution authority `caf675...`;
8. single launch head `31fcd...`.

The source-lock verifies the frozen execution-authority blob, code/workflow blobs, campaign manifest, frozen scientific-core blobs, canonical 768-state SHA256, 384-shard topology, Python environments, fail-fast/max-parallel settings and authority ancestry before compute.

No provenance basis for `INVALID_PROVENANCE` is presently identified.

## Frozen contract retained statically

The source stack statically retains the preregistered domain and main science constants:

- causals `0to5,1to4,2to3`;
- blocks `0..3`;
- paths `0..3`;
- boxes `0..15`;
- 768 canonical records;
- R `[6,8,10,12]`;
- rho `[0.35,0.9,1.6,2.7]`;
- 243 channels, no pruning;
- precision 384 and `python-flint==0.9.0`;
- threshold `1/20`, floor `1`, `MAX_DEPTH=3`;
- exact dyadic midpoint recursion in the producer;
- local-D recomputation at each visited node;
- exact leaf/per-rho certification binding;
- unresolved terminal leaves only at depth 3;
- exact midpoint check in the Phase-B assembler;
- no authoritative Critic inside the source workflow.

## Outcome-independent counterexample candidate — parent-inclusion tree identity is not bound by the source assembler

The static implementation review records:

`assembler_reconstructs_exact_tree_and_parent_inclusion = true`.

Direct launch-head inspection does not support that statement.

`code/iter504v_phase_b_assemble.py::validate_case()` checks parent-inclusion records for:

- record count equals the serialized count;
- record count equals `visited_node_count - 1`;
- exact R grid for Haar/log keys;
- exact 16 R/rho channel rows;
- 243 boolean componentwise-inclusion values per row.

But it does **not** reconstruct or validate the serialized inclusion-record tree identity fields:

- `depth`;
- `amp_lower_q`;
- `amp_upper_q`;
- `parent_depth`;
- `parent_amp_lower_q`;
- `parent_amp_upper_q`.

Those fields are copied into `case_projection()` and hashed, but no parent-child dyadic relation is checked before classification.

### Explicit same-realization mutation

Starting from any otherwise structurally valid case with at least one inclusion record:

1. keep leaves, leaf dyadic cells, certification booleans, possible-max identities, inclusion cardinality, R/rho rows and all 243 inclusion bits unchanged;
2. mutate only one inclusion record's child/parent interval identity, for example set `parent_depth` to the wrong depth and/or replace `parent_amp_lower_q,parent_amp_upper_q` with a different rational dyadic interval;
3. apply the identical mutation to the corresponding record in both Python environments.

The current source assembler has no predicate that rejects this mutation. Its per-state projection SHA changes, but changes identically in both environments; the aggregate only requires equality of the per-state projection maps/sequences and therefore does not rescue the missing semantic check.

This is an outcome-independent verifier-binding counterexample candidate. It does **not** assert that the active producer emitted malformed inclusion identities. The producer code constructs inclusion records from the actual recursion stack and is statically consistent with the frozen tree.

## Significance

The active source run is not terminal and is not terminal scientific authority in any case: the execution authority explicitly requires a separately frozen independent Critic after source terminalization.

Therefore no competing PASS/INCONCLUSIVE/INVALID scientific verdict is issued now.

However, the current static-review assertion that the source assembler reconstructs exact parent-inclusion tree identity is overstated. A later independent Critic must not inherit that assertion without an explicit reconstruction check and adversarial fixture.

The source assembler may still be a valid preliminary source classifier if final authority is conditioned on a genuinely independent Critic that closes this binding. The final authority path must independently decide whether this candidate is repaired/refuted or surviving.

## Prepared terminal control

A future independent Phase-B Critic should reconstruct the expected rooted dyadic visited tree per state from leaf cells and/or a canonical node representation, then require every non-root inclusion record to correspond to exactly one actual visited child-parent edge:

- `child.depth = parent.depth + 1`;
- child interval is exactly the left or right half of the serialized parent interval;
- serialized child interval equals the record's actual child node;
- serialized parent interval/depth equals the actual parent node;
- each non-root visited node has exactly one inclusion record;
- no duplicate or orphan inclusion record exists.

Negative control: mutate only one inclusion record's parent interval/depth while holding all inclusion booleans and scientific leaf decisions fixed; the Critic must reject it.

## Governance

`RQIR Core v1.0 = FROZEN`.

No partial Phase-B science was consumed. No model-level FAIL exists in this gate. `INCONCLUSIVE != FAIL`, `BLOCKED != FAIL`, finite certificate != universal theorem, scoped result != family/global closure. D7 terminal selectors remain forbidden and Candidate Gravity remains inactive.

## Handoff

- `RESULT_REVIEWED = none; Iter504V Phase-B source run 35405065903 nonterminal`
- `PREREG_CHECK = PASS`
- `OBJECT_IDENTITY_CHECK = static PASS for domain/science constants; parent-inclusion tree binding candidate OPEN`
- `SOURCE/REALIZATION_CHECK = static PASS_SCOPED for producer; assembler semantic binding qualified`
- `PROVENANCE_CHECK = PRETERMINAL PASS`
- `SAME_REALIZATION_CHECK = static QUALIFIED; identical malformed inclusion-tree mutation can survive both lanes and aggregate`
- `NUMERICAL/STATISTICAL_CHECK = not consumed`
- `COUNTEREXAMPLE_ATTEMPTS = malformed parent-inclusion tree identity accepted by source assembler in static code path — SUCCESS candidate; exact midpoint, leaf/per-rho binding and premature unresolved depth are statically bound`
- `OVERCLAIM_CHECK = PASS`
- `VERDICT = none while authoritative Research workflow is nonterminal`
- `QUALIFICATIONS = candidate concerns source/verifier semantic binding, not observed producer science; terminal authority still requires a separate independent Critic`
- `UPDATED_STATE = one outcome-independent Phase-B source-assembler binding candidate durably frozen; static-review claim assembler_reconstructs_exact_tree_and_parent_inclusion is not independently supported`
- `NEXT_ADMISSIBLE_GATE = wait for source run terminalization without consuming partial science; then freeze exact terminal source artifacts and a separate independent Critic that explicitly reconstructs and adversarially tests parent-inclusion child/parent dyadic identity before any terminal Phase-B authority is accepted`
