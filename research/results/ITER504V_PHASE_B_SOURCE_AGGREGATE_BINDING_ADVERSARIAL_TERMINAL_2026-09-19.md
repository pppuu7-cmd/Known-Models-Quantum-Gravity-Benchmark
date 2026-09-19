# Iter504V Phase-B source aggregate binding adversarial gate — terminal result

Date: 2026-09-19

## Authority

- gate: `ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_ADVERSARIAL_GATE`
- preregistration commit: `04a47f859323bea69472f142ec1a2f4b97e5df0b`
- implementation commit: `31d58bec122ca0995f576660b3dfeeda15b0ba3d`
- workflow commit: `0485a04ab4646b6e80df7c7555db4b3b5bcddd72`
- execution authority commit: `32f9f5cbf2d95fb31938b0d163a446a8fa43549a`
- single launch head: `2514581ed3d93bbdc9ccefd8383627e8cb1e7e28`
- authoritative Actions run: `35420614607`, attempt 1, terminal `completed/success`
- exact immutable source aggregate blob under test: `ae1932a7cdd98a1cc74f1b2f07bc295e0c097274`
- source scientific run intentionally not consumed/classified: `35405065903`

Frozen criteria were not changed after execution.

## Terminal classification

`ITER504V_PHASE_B_SOURCE_AGGREGATE_BINDING_DEFECTS_VERIFIED_SCOPED`

This is a verifier/authority-path methodology result only. It is not scientific FAIL/PASS/INCONCLUSIVE for Phase-B source run `35405065903`.

## Result

Both Python 3.11 and 3.13 independently produced byte-identical canonical `result.json` with SHA256:

`6c62ffe7e6d75d2246e5b25bedd971ba08541fd41d06a4e98e1f1bad32ce686b`

Frozen decision SHA256:

`bfd4a7d6b853b1a6c885086bf1851c0923187aaaa6b36044eec0042a9a310f63`

Harness errors: none.

All frozen positive/sensitivity controls were live:

- coherent zero-unresolved source PASS accepted;
- coherent one-unresolved source INCONCLUSIVE accepted;
- cross-environment classification disagreement rejected as source INVALID;
- cross-environment state-identity disagreement rejected as source INVALID;
- cross-environment projection-map disagreement rejected as source INVALID.

All three independent oracles identified the preregistered candidates as contract-invalid, but the exact source aggregate accepted each candidate as nominal source PASS with `errors=[]` and `cross_environment_exact_decision_agreement=true`.

### Candidate A — classification-to-unresolved semantic binding

Synthetic assemblies contained one unresolved state, `total_unresolved_leaves=1`, and the matching counterexample state while claiming source PASS.

Independent oracle: `classification_unresolved_binding`.

Exact source aggregate nevertheless returned:

`ITER504V_BROADER_DOMAIN_LOCAL_D_CERTIFIES_COMPLETE_Q1_SCOPED`

with `errors=[]`, return code 0 and exact cross-environment agreement.

Therefore the aggregate does not independently bind source classification to unresolved evidence.

### Candidate B — canonical decision-projection key binding

One canonical state key in `decision_projection_sha256_by_state` was replaced by a foreign noncanonical key while retaining map cardinality 768, canonical `state_ids`, the unchanged projection-sequence scalar, and exact cross-environment equality.

Independent oracle: `projection_key_set`.

Exact source aggregate nevertheless returned nominal source PASS with no errors.

Therefore the aggregate does not independently bind the decision-projection map key set to the frozen canonical 768-state identity.

### Candidate C — case-provenance key binding

One canonical key in `case_file_sha256` was replaced by a foreign noncanonical key while retaining cardinality 768 and exact cross-environment equality.

Independent oracle: `provenance_key_set`.

Exact source aggregate nevertheless returned nominal source PASS with no errors.

Therefore the aggregate does not independently bind case-provenance keys to the frozen canonical 768-state identity.

## Actions provenance

Jobs:

- source-lock `105837471138`: success
- Python 3.11 `105837491172`: success
- Python 3.13 `105837491163`: success
- aggregate `105837508143`: success

Artifacts:

- Python 3.11 artifact `10577352415`, GitHub digest `sha256:8fe0d0cfe1905428952c1a82b618866c1ce56c56faaf424151fc8cbb32a5aae0`
- Python 3.13 artifact `10577866791`, GitHub digest `sha256:8fe0d0cfe1905428952c1a82b618866c1ce56c56faaf424151fc8cbb32a5aae0`
- aggregate artifact `10576787892`, GitHub digest `sha256:feda26c081203f1640be3eab91ba4461ad2e741f7fc94ff318db2a1e560ed95a`

Independent local ZIP SHA256 rehashes matched all three GitHub digests exactly.

Additional content hashes:

- `result.json`: `6c62ffe7e6d75d2246e5b25bedd971ba08541fd41d06a4e98e1f1bad32ce686b`
- `returncode.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`, value `0`
- `aggregate_result.json`: `20bbacf09b530c9d41ad69a7cfed1f0a510a4a3ac566a73364fbbc6c39dc2a33`

## New fact

The final source aggregate has three additional independently reproducible authority-binding omissions beyond the already confirmed source-assembler omissions:

1. source PASS is not rebound to zero unresolved evidence;
2. decision-projection map keys are not rebound to the exact canonical state set;
3. case-provenance map keys are not rebound to the exact canonical state set.

These defects mean green source aggregate output alone cannot establish terminal Phase-B authority. A post-terminal independent Critic must reconstruct/rebind these relations rather than trusting aggregate acceptance.

## Source-run firewall

Fresh source run `35405065903` remains nonterminal (`queued / conclusion=null`) at this terminalization point. Partial source artifact metadata now exists for two shards, but no partial source payload was opened or consumed. No source scientific classification is issued here, and no competing source execution was launched.

## Claim ceiling

This result proves only scoped synthetic verifier/authority-path defects against the exact immutable Phase-B source aggregate. It does not establish that the active source producer emitted any malformed object; does not classify source run `35405065903`; does not alter the frozen PASS/INCONCLUSIVE/INVALID science taxonomy; and authorizes no all-domain beyond q=1, model-family, D7, Candidate Gravity, Paper IV, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim.

## Downstream requirement

After source run `35405065903` is fully terminal, prospectively freeze the exact complete terminal artifact inventory/digests before substantive science consumption and execute one independent Critic closure. In addition to the already required exact shard/artifact-to-four-case binding and exact parent-inclusion dyadic-edge reconstruction, that Critic must independently rebind source classification to unresolved evidence, projection keys/sequence to the canonical 768-state set, and case-provenance keys/hashes to the canonical state set. No producer rerun is authorized merely because these verifier defects exist.
