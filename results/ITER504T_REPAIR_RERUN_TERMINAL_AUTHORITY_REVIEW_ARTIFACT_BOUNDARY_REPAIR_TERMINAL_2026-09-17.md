# ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_GATE — terminal result

Date: 2026-09-17
Status: TERMINAL

## Authority

- Gate: `ITER504T_REPAIR_RERUN_TERMINAL_AUTHORITY_REVIEW_ARTIFACT_BOUNDARY_REPAIR_GATE`.
- Reconciled starting main: `5d9ab0763d9ad64073e13b6ff9415a830483041b`.
- Prospective preregistration commit: `4a5f7d1c651527249b2831b6886cd502dc18e648`.
- Frozen authority commit: `fbfca6f932dd540898de3d9d738e9f953de8ac84`.
- Nonaborting artifact collector commit: `bb99b03fe4ea5f6e5e3950ca32191ba55e87c6e1`.
- Boundary-review implementation commit: `8f0a72165479b870405bb51478a64e607777502b`.
- Aggregate implementation commit: `2f4207d0c69f280fbe63fec4c75b45aec0041562`.
- Workflow head: `4e9a6ac95a10f89ba57eaa3aaa642a43e0236866`.
- Authoritative Actions run: `35238357310`, terminal `completed/success`.

Jobs:

- source-lock `105260048120` — success;
- boundary-control `105260104164` — success;
- Python 3.11 lane `105260104179` — success;
- Python 3.13 lane `105260104162` — success;
- aggregate `105260195631` — success.

Artifacts:

- boundary missing-artifact control `10503972713`, digest `sha256:ea0edd702d8af7a525d88b3550753c805fa38cac78d9d1cdcede8bdae0fb2fb0`;
- Python 3.11 review `10504281712`, digest `sha256:4103bd065f9351c021f2bf110088a9015cc1c0867f90877219badc1803a86c6c`;
- Python 3.13 review `10504046837`, digest `sha256:61e8da2c5327bf225d127f5ba32898c9c85adb3daad32bfb358039fbc919e80a`;
- aggregate `10504616531`, digest and independently rehashed ZIP SHA256 `sha256:89619364918da0e663eaef9d882427a30392e11d441545d17585843596453987`.

Aggregate internal hashes:

- JSON SHA256 `823026fc00dcdddff765848f9513cdbf5a26ef7794288738662f4fcc7d4cb7f8`;
- log SHA256 `38790856fdec7d1e5751b3780b3260d8e4bfc36194e5c84e0caa765234a939d0`;
- aggregate decision SHA256 `09306cd3fc13b599d000f2e937ccdcf1c1bbf219d339a0396c06ac6a2d8624bb`.

Green CI is provenance/execution evidence only.

## Frozen terminal classification

`INVALID_IMPLEMENTATION`

This is **not scientific FAIL** and does not negate the underlying Iter504T three-root calculation.

## Exact result

The gate successfully repaired the exact workflow-boundary defect identified by the preceding independent Critic:

- the boundary-control job deliberately requested nonexistent artifact `iter504t-boundary-control-definitely-missing`;
- `gh run download` was actually attempted and returned nonzero exit code `1`;
- the workflow did not abort;
- the artifact state was recorded `MISSING_OR_UNAVAILABLE`;
- the same frozen classifier was reached and emitted `ITER504T_REPAIR_RERUN_TERMINAL_REVIEW_BLOCKED_SCOPED`;
- aggregate controls `workflow_boundary_actual_download_failure_observed=true` and `workflow_boundary_missing_artifact_control_blocked=true`.

Both production lanes also independently succeeded at the substantive exact-run replay:

- all five required upstream artifacts were present with exact frozen IDs/digests;
- inherited review classification in both lanes was `ITER504T_REPAIR_RERUN_EXACT_RUN_AUTHORITY_VALIDATED_SCOPED`;
- all boundary controls and inherited semantics controls passed;
- both lanes recomputed `ITER504T_LOCAL_D_CERTIFIES_THREE_ROOT_CONTINUOUS_DRIFT_SCOPED`;
- unresolved leaves = `0` across `12` terminal leaves;
- C1 = `18` records / `70,056` component booleans / `0` false;
- no actual C4 contradiction is present in immutable run `35205054496`.

However, the prospectively frozen aggregate also required exact cross-environment review-decision SHA equality. That control failed:

- Python 3.11 review decision SHA256 `4eec7f2966d9c0df79fdf381c73e88d5cc45acbb6a688f68f78616937e17ff96`;
- Python 3.13 review decision SHA256 `c12de65d9c2d0a065230198ecab78f09ecb43148ee0c45a130636a8f74144de5`;
- `lane_classification_agreement=true` but `lane_decision_sha256_agreement=false`.

A terminal diagnostic comparison localizes the difference exactly: seven fields differ between the lane payloads — five `artifact_manifest.entries[*].local_path` values containing the environment-specific prefixes `terminal_311/...` versus `terminal_313/...`, the resulting `artifact_manifest.manifest_sha256`, and the resulting `review_decision_sha256`. After removing only those environment-local path-derived fields, both lane payloads are byte-canonical equivalent and have the same normalized SHA256 `a7eda65e7407e7188ae67763df01f40187fd7659531f5bb24f29187e8bac11d0`.

The frozen criterion cannot be changed after the result. Therefore the terminal gate classification is `INVALID_IMPLEMENTATION` despite agreement of the substantive scientific/review decision.

## New fact

The previous Critic's workflow-boundary missing-artifact counterexample is now genuinely closed at the execution level: a real missing-artifact download failure reaches the frozen BLOCKED classifier instead of killing CI. A new, narrower implementation defect is exposed: environment-specific local filesystem paths were included in the hashed scientific-review payload, causing artificial cross-environment decision-hash disagreement even though all substantive fields agree.

This defect concerns canonicalization/provenance hashing only. It is not a scientific discrepancy, not a numerical disagreement, and not evidence against the underlying three-root scientific result.

## Claim ceiling

No authority-restoration PASS is issued by this gate because its own frozen aggregate control failed. The immutable exact-run replay remains coherent supporting evidence only. No all-1888 closure, D7 closure, model/family failure, terminal selector, Candidate Gravity activation, Paper IV authorization, `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim is authorized.

Historical C4 remains `CONFIRMED_SCOPED` for the reusable scientific-validator path. Historical invalid/blocked/inconclusive results remain immutable.

## Next recommended gate

Prospectively freeze a same-object decision-canonicalization repair only. It should exclude execution-environment local paths and path-derived manifest hashes from the cross-environment decision projection while retaining all artifact IDs/digests, file-content SHA256 values, run/head identities, boundary states, missing-artifact BLOCKED control, present-identity-mismatch INVALID control, inherited semantics controls, and interpretation ceiling.

A positive control should prove that equivalent artifacts downloaded into different local directory prefixes yield identical decision SHA. A negative control should prove that changing any artifact ID/digest/content SHA or substantive review field still changes or invalidates the decision. Do not rerun physics.
