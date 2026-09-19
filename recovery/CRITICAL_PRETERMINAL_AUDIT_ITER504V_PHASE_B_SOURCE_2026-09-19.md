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

Fresh Actions state remains nonterminal. The run endpoint is `queued / conclusion=null` while the job endpoint reports active/queued matrix execution. Source-lock is terminal `success`; no complete terminal source inventory exists. No case, leaf, slope, drift, certification, assembly, aggregate or counterexample scientific value was consumed in this audit.

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

## Outcome-independent counterexample candidate A — parent-inclusion tree identity is not bound by the source assembler

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

### Explicit same-realization mutation A

Starting from any otherwise structurally valid case with at least one inclusion record:

1. keep leaves, leaf dyadic cells, certification booleans, possible-max identities, inclusion cardinality, R/rho rows and all 243 inclusion bits unchanged;
2. mutate only one inclusion record's child/parent interval identity, for example set `parent_depth` to the wrong depth and/or replace `parent_amp_lower_q,parent_amp_upper_q` with a different rational dyadic interval;
3. apply the identical mutation to the corresponding record in both Python environments.

The current source assembler has no predicate that rejects this mutation. Its per-state projection SHA changes, but changes identically in both environments; the aggregate only requires equality of the per-state projection maps/sequences and therefore does not rescue the missing semantic check.

This is an outcome-independent verifier-binding counterexample candidate. It does **not** assert that the active producer emitted malformed inclusion identities. The producer code constructs inclusion records from the actual recursion stack and is statically consistent with the frozen tree.

## Outcome-independent counterexample candidate B — frozen shard identity/cover is not bound by source assembly

A second, distinct preterminal gap is present at the execution-topology/provenance layer.

The Phase-B preregistration freezes exactly 192 deterministic quartile shards per Python environment, with shard identity

`(python, causal, block, path, box_quartile)`,

and requires the eventual independent Critic to verify the **exact complete shard cover**. The frozen shard producer writes a `shard.json` containing the shard's `causal`, `block`, `path`, `quartile`, exact four boxes, exact four state IDs, record count and invalid count.

However, `code/iter504v_phase_b_assemble.py` does not read or validate any `shard.json` at all. It recursively discovers only `case-*.json`, keys them by the internal `state_id`, and validates that the union is the canonical 768-state set. The aggregate then compares only the two assembled 768-state projections/counts. No source classifier binds a case file to the artifact/shard identity that was supposed to produce it.

### Explicit topology-preserving-science mutation B

Starting from a structurally valid complete source inventory in one Python environment:

1. keep all 768 `case-*.json` bytes unchanged;
2. permute case files between two quartile shard artifact directories so that each case's internal `state_id` remains unchanged but at least one file is stored under the wrong frozen `(causal,block,path,quartile)` shard;
3. optionally leave each original `shard.json` in place, creating a direct mismatch between its declared four state IDs and the case files actually present below that artifact directory;
4. apply the same directory/artifact permutation in the other Python environment.

The current assembler still sees exactly the same 768 unique internal state IDs and exactly the same scientific case payloads, so its classification and per-state decision map are unchanged. Because it never consumes `shard.json` or derives expected state IDs from the artifact directory identity, the frozen shard-partition violation is invisible to source assembly. Cross-environment aggregate equality also remains unchanged if the same mutation is present in both lanes.

This candidate is about provenance/topology binding, **not** about the numerical science values. The actual workflow matrix passes the correct causal/block/path/quartile arguments to the shard producer and artifact names are deterministic, so no claim is made that the active Actions run actually permuted records. The point is that the current source validation path cannot independently detect that class of contract violation.

## Significance

The active source run is nonterminal and is not terminal scientific authority in any case: the execution authority explicitly requires a separately frozen independent Critic after source terminalization.

Therefore no competing PASS/INCONCLUSIVE/INVALID scientific verdict is issued now.

The two prepared candidates identify requirements that the future Critic must close independently rather than inherit from source green CI:

1. reconstruct and bind every parent-inclusion child/parent dyadic edge;
2. bind every immutable source artifact/shard identity to exactly its frozen four-record cohort, consume/validate `shard.json`, and prove exact 192-shard cover per environment before accepting the 768-state union.

The source producer/workflow may still be correct in the actual execution. These are independent-verification gaps, not observed scientific failures.

## Prepared terminal controls

A future independent Phase-B Critic should reconstruct the expected rooted dyadic visited tree per state and require every non-root inclusion record to correspond to exactly one actual visited child-parent edge:

- `child.depth = parent.depth + 1`;
- child interval is exactly the left or right half of the serialized parent interval;
- serialized child interval equals the record's actual child node;
- serialized parent interval/depth equals the actual parent node;
- each non-root visited node has exactly one inclusion record;
- no duplicate or orphan inclusion record exists.

Negative control A: mutate only one inclusion record's parent interval/depth while holding all inclusion booleans and scientific leaf decisions fixed; the Critic must reject it.

For source topology, the Critic should freeze the exact terminal artifact IDs/digests, map every expected artifact name to one exact `(python, causal, block, path, quartile)`, parse that artifact's `shard.json`, require its four state IDs to equal the frozen quartile and require the case files physically contained in that artifact to match exactly those four states. Across artifacts, require exactly 192 unique shard identities per environment and no missing/duplicate/misplaced case artifact.

Negative control B: swap one case file between two shard directories without changing either case payload; the Critic must reject the resulting shard/content mismatch even though the 768-state union is unchanged.

## Governance

`RQIR Core v1.0 = FROZEN`.

No partial Phase-B science was consumed. No model-level FAIL exists in this gate. `INCONCLUSIVE != FAIL`, `BLOCKED != FAIL`, finite certificate != universal theorem, scoped result != family/global closure. D7 terminal selectors remain forbidden and Candidate Gravity remains inactive.

## Handoff

- `RESULT_REVIEWED = none; Iter504V Phase-B source run 35405065903 nonterminal`
- `PREREG_CHECK = PASS`
- `OBJECT_IDENTITY_CHECK = static PASS for domain/science constants; parent-inclusion tree binding and shard/artifact topology binding candidates OPEN`
- `SOURCE/REALIZATION_CHECK = static PASS_SCOPED for producer/workflow; independent source-assembly semantic/provenance binding qualified`
- `PROVENANCE_CHECK = PRETERMINAL PASS for observed authority chronology; exact terminal shard/artifact binding not yet independently established`
- `SAME_REALIZATION_CHECK = static QUALIFIED; identical malformed inclusion-tree mutation or identical cross-shard case permutation can survive both lanes and aggregate`
- `NUMERICAL/STATISTICAL_CHECK = not consumed`
- `COUNTEREXAMPLE_ATTEMPTS = malformed parent-inclusion tree identity accepted by source assembler — SUCCESS candidate A; wrong frozen shard placement with unchanged 768-state union accepted by source assembler — SUCCESS candidate B; exact midpoint, leaf/per-rho binding and premature unresolved depth are statically bound`
- `OVERCLAIM_CHECK = PASS`
- `VERDICT = none while authoritative Research workflow is nonterminal`
- `QUALIFICATIONS = candidates concern source/verifier contract binding, not observed producer science; terminal authority still requires a separately frozen independent Critic`
- `UPDATED_STATE = two outcome-independent Phase-B verifier-binding candidates durably frozen; source run remains nonterminal and unclassified`
- `NEXT_ADMISSIBLE_GATE = wait for complete source terminalization without consuming partial science; then prospectively freeze exact terminal source artifact IDs/digests and run one independent Critic that (A) reconstructs parent-inclusion dyadic edges and (B) binds every artifact/shard identity and shard.json cohort to its exact four contained case records before any terminal Phase-B authority is accepted`
