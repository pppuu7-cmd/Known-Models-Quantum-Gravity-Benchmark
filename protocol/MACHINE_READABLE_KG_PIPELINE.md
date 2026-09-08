# Machine-Readable Candidate Gravity Audit Pipeline

**Status:** frozen methodology / executable pre-ansatz layer.  
**Purpose:** make future Candidate Gravity construction auditable by explicit records and fail-closed validation rather than prose interpretation or chat memory.

## 1. Canonical record

Every future exploratory or promoted Candidate Gravity object must have a machine-readable record conforming to the contract in

`schema/KG_CANDIDATE_RECORD_v1.json`.

A pre-ansatz fail-closed example is

`schema/KG_CANDIDATE_RECORD_PREANSATZ_EXAMPLE.json`.

The reference validator is

`code/kg_candidate_record_validator.py`.

The record is methodology/provenance state; it does not by itself establish physical truth.

## 2. Required registries

A candidate record must explicitly bind the following objects.

### A. Parent authority

- stable candidate ID;
- repository/commit/blob provenance;
- one parent action/CTP/kernel/master/channel object;
- declared validity domain.

No chat-memory-only parent authority is accepted.

### B. Parameter incidence

Every fit/theory parameter is tagged by role and sharing scope:

- dynamics;
- shared nuisance;
- configuration-local nuisance;
- state;
- detector;
- calibration;
- mediator.

The sharing map is authority for cross-order, intervention and holdout tests. A parameter cannot be cloned per block merely to improve the fit unless the parent/generative model authorizes that scope.

### C. Observable-block registry

Every physical block records

- response order;
- configuration/control ID;
- physical dimension;
- routing/convention authority;
- complete same-parent response ledger;
- origin/cut classification;
- exact physical-constraint status;
- attribution tags;
- prospective role: training, holdout, mandatory anchor, candidate suite, null control.

### D. Comparator registry

For every applicable comparator:

- ID/theory realization;
- same-domain declaration;
- parameter incidence;
- state sector;
- prediction authority;
- Jacobian/tangent authority.

Comparator blocks must refer to the same observable/order/routing/domain as the candidate block.

### E. Covariance registry

Record

- full covariance authority;
- provenance;
- whether cross-block correlations are included;
- any supported-subspace/singularity treatment.

Deterministic nuisance directions belong in parameter/Jacobian records, stochastic uncertainty in covariance. Do not silently double count one generative uncertainty in both.

### F. Rigidity registry

Bind

- cross-order stack/shared-parameter incidence;
- intervention/configuration stack;
- train/holdout split and predictive covariance;
- minimal discriminating test-suite library/selection/LOBO robustness.

## 3. Response completeness is fail-closed

An observable block may be used for a residual only when its completeness status is `PASS` and its ledger contains all parent-required ordered-partition families or exact zero/origin proofs for omitted families.

If a required family is unknown, the block is `BLOCKED`.

Never interpret a missing family/object as zero.

## 4. Promotion-gate state machine

The conceptual gates are those in `protocol/CANDIDATE_GRAVITY_PROMOTION_GATE.md`:

- `G0`: parent dynamics;
- `G1`: response completeness;
- `G2`: physical constraints;
- `G3`: common-domain comparator object;
- `G4`: attribution stack;
- `G5`: full comparator/full-C5 matching;
- `G6`: local COR;
- `G7`: global/nonlinear separation;
- `G8`: projected identifiability/observable design;
- `G9`: rigidity/prediction;
- `G10`: promotion/downstream authorization.

Allowed machine states:

`PASS`, `BLOCKED`, `FAIL`, `N_A`.

Rules:

1. missing mandatory evidence -> `BLOCKED`;
2. a computed failed physical criterion -> `FAIL`;
3. `N_A` is allowed only when the gate is genuinely outside the declared scope and the promotion contract does not require it;
4. ansatz promotion requires all mandatory gates `PASS`;
5. Fisher/resources require an independently recorded robust global comparator-subtracted residual.

`BLOCKED` is a scientifically legitimate terminal/current state and is not a malformed record.

## 5. Residual objects must be provenance-linked

Any machine record claiming `COR`, global separation or projected singular values must include references to

- physical-basis object;
- residual vector;
- covariance;
- union comparator Jacobian;
- comparator parameter/domain declaration;
- code/result artifact or reproducible calculation.

Do not store only a scalar significance without the objects that define the quotient.

## 6. Prospective roles are immutable within an iteration

Training/holdout/null/anchor/test-suite roles must be frozen before the target residual is inspected.

Changing a block from holdout to training, dropping a failed block, or altering its local nuisance allowance is a protocol change and requires a new prospective iteration/record version.

## 7. Validator behavior

The reference validator is deliberately fail-closed.

It distinguishes

- a **valid but blocked** scientific record;
- an **invalid methodology record**;
- a **valid promotable** record only when all mandatory evidence/gates permit promotion.

The pre-ansatz example is intentionally valid-but-blocked: it records the absence of a model without pretending missing objects are errors or zeroes.

## 8. Versioning

Candidate records are append/versioned artifacts. Do not overwrite a previous scientific verdict silently.

At minimum preserve

- schema version;
- candidate-record version/iteration;
- parent-object provenance;
- comparator registry version;
- prospective split/test-suite version.

Any change that can alter the residual quotient should create a new candidate-record version.

## 9. Future automation boundary

The machine-readable layer may automate

- presence/completeness checks;
- parameter-sharing consistency;
- response-family ledger checks;
- covariance/Jacobian shape/provenance checks;
- promotion-gate consistency;
- COR/contrast/rigidity calculations once numeric objects exist.

It must **not** automatically infer a missing physical theorem, set a blocked object to zero, or promote a model merely because syntax validates.

## 10. Candidate Gravity consequence

A future KG candidate should be restorable from its record plus referenced artifacts without the chat history.

The executable pipeline is therefore part of the scientific reproducibility contract, not administrative bookkeeping.
