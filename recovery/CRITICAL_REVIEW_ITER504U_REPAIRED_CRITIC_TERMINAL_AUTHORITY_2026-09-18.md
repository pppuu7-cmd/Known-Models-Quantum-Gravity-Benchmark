# Independent Critical Review — ITER504U repaired-Critic terminal authority

Date: 2026-09-18
Lane: independent KMQGB Critical Review / Verification
Verdict: `INVALID_IMPLEMENTATION`

## Result reviewed

Exactly one latest substantive terminal scientific authority object:

- science gate: `ITER504U_HELDOUT_LOCAL_D_GENERALIZATION_FIREWALL`;
- source run: `35246605860`, head `102c7f9cafec956f3bc7bed4384ae755c98f761a`, attempt 1;
- repaired closure gate: `ITER504U_REPAIRED_CRITIC_CLOSURE`;
- frozen closure authority commit: `3302f77593e668ab48fdff887801571fa46467b1`;
- repaired-Critic closure run: `35267499787`, head `732b9a035472f3b67b00ce985f695c03d7e90bb8`;
- historical terminal classification: `ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED`;
- terminalization/recovery commit: `a31db0d6b9f98448977a6fcdde80a45e3e7195fe`.

The later Iter504V commits are preregistration/design only and are not a newer executed scientific result.

## Preregistration and frozen object

Prospective Iter504U preregistration: `05b8e9354c9a7805f0fce18b904346a986a0787f`.

The frozen scientific object requires, among other things:

- deterministic rational dyadic midpoint subdivision;
- exact rational midpoint `m_J`;
- mean-value enclosure built as `f_i(J) subset f_i(m_J) + (J-m_J)D_i(J)`;
- local validated derivative recomputed on every visited subinterval;
- exact dyadic cell identity and complete cover;
- exact-Arb decision predicates, with floats display-only;
- leaf certification exactly equal to conjunction of all per-rho certifications;
- unresolved terminal leaves only at `MAX_DEPTH=3`.

Historical C4 and premature-unresolved controls have been repaired and remain valid controls.

## Provenance

The repaired closure authority prospectively freezes the source run/head/attempt, 16 successful required upstream jobs, and 15 required source artifacts before repaired-Critic science consumption. The obsolete original source-workflow Critic artifact is explicitly excluded.

Run `35267499787` is terminal success. The repaired review jobs under Python 3.11 and 3.13 and the closure job are all terminal success.

Fresh closure artifacts:

- `iter504u-repaired-critic-review-3.11`: id `10517615531`, digest `sha256:1d5301cc8f6cd7609989af78d1141588773e2d7c230194263cde56fa87771f2a`;
- `iter504u-repaired-critic-review-3.13`: id `10517600640`, digest `sha256:1eda7268243dfe6d2168e5063788582cf91023a5c80af0ac9004cfe76cfe271d`;
- `iter504u-repaired-critic-closure`: id `10516579339`, digest `sha256:ee2399d5efdf58a829edfab57b30e31c2955663d538f89623bbba85c8390afdc`.

The workflow log records exact artifact-identity verification against the frozen source authority and byte equality of the two repaired-Critic JSON decisions. No basis was found for `INVALID_PROVENANCE`.

## Historical terminal payload

The repaired Critic reports:

- `classification=ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED`;
- 6 frozen held-out cases;
- 19 terminal leaves;
- 0 unresolved leaves;
- `critic_errors=[]`;
- cross-environment exact-decision agreement `true`;
- repaired negative controls all true, including `C4_true_leaf_false_rho` and `premature_unresolved_leaf_depth`;
- decision projection SHA256 `b44f7bd0711a45d5469c8c1ce968f9b7f7e4cbe773dd33e0fb1bcf5beb22d3e6`;
- repaired Critic SHA256 `5e81675fa60f344643675d45e3211e41406721fd96d53b1a5329755bda5956b2`;
- closure payload SHA256 `56b86f4d8a8224544c55344cd08bfd8b9a6a05022059d1fb0af84e9e76439d6c`.

These historical values are not rewritten by this review.

## Decisive counterexample — exact midpoint is not bound by the authority validator

The source producer correctly computes

`midq = (loq + hiq) / 2`

and serializes it as `leaf.local_mid_q`.

However, the frozen environment assembler `code/iter504u_heldout_assemble.py` and the original Critic `code/iter504u_heldout_critic.py` do not validate that serialized `local_mid_q` equals the exact midpoint of `amp_lower_q` and `amp_upper_q`.

Their dyadic-cell check verifies only:

- depth in `0..MAX_DEPTH`;
- exact cell width for that depth;
- exact placement of the cell in the parent box.

They then copy `local_mid_q` into the decision projection without checking the midpoint relation.

The repaired wrapper `code/iter504u_heldout_critic_depth_binding_repair.py` adds only the missing implication

`leaf.certified is False => leaf.depth == MAX_DEPTH`

and does not add any midpoint-binding check.

Therefore the following explicit same-realization mutation survives the independent authority path:

1. start from any structurally valid source case;
2. keep `depth`, `amp_lower_q`, `amp_upper_q`, all exact certification booleans, R/rho identities, possible-max data, inclusion records, cover and all scientific values unchanged;
3. replace only `local_mid_q` by a different rational value inside the same dyadic leaf;
4. apply the same mutation in both Python lanes.

The assembler and repaired Critic accept the mutated object because no predicate recomputes the midpoint. Cross-environment equality also remains true when the same mutation is made in both lanes.

Thus the authority validator cannot distinguish the frozen exact-midpoint realization from a payload that violates the frozen construction `m_J=(a+b)/2` while preserving every currently decision-bound field.

This is not a claim that the active producer emitted a wrong midpoint. Source inspection shows the producer computes the midpoint correctly. It is an implementation-binding failure of the independent authority path.

## Secondary structural observation

Parent-inclusion records are cardinality/grid/type checked, but their serialized child/parent interval fields are not reconstructed against the actual visited dyadic tree by the original Critic. This is not needed for the present verdict because the exact-midpoint counterexample is already decisive. It should be included in the same-contract repair audit rather than promoted to a separate scientific defect without a dedicated fixture.

## Verdict

`INVALID_IMPLEMENTATION`.

Reason: the independent closure implementation does not bind a mandatory frozen component of the scientific object — the exact rational local midpoint used by the mean-value enclosure. Green closure CI and cross-environment equality therefore do not by themselves establish full frozen-contract equivalence.

This verdict does **not** assert that the six actual producer cases numerically fail, does not convert PASS to scientific FAIL, and does not alter the immutable historical Actions result.

## Downstream qualification

The later Iter504V design/preregistration commits depend on terminal Iter504U authority commit `a31db0d6b9f98448977a6fcdde80a45e3e7195fe`. They remain useful prospective design records, but execution should not use the currently qualified Iter504U closure as fully independently validated authority until this same-object verifier defect is repaired prospectively.

No Iter504V physics/source execution was present in the fresh recent-commit state inspected for this review.

## Governance

- `RQIR Core v1.0 = FROZEN`;
- `BLOCKED != FAIL`;
- `INCONCLUSIVE != FAIL`;
- finite certificate != universal theorem;
- scoped child != family closure;
- D7 required subgates remain unclosed;
- terminal selectors remain forbidden;
- Candidate Gravity remains inactive.

No global quantum-gravity claim is authorized.

## Handoff

- `RESULT_REVIEWED = ITER504U_REPAIRED_CRITIC_CLOSURE / run 35267499787; historical class ITER504U_HELDOUT_LOCAL_D_GENERALIZES_SCOPED`
- `PREREG_CHECK = PASS`
- `OBJECT_IDENTITY_CHECK = FAIL at independent-verifier binding: local_mid_q is serialized/projected but exact midpoint relation is not validated`
- `SOURCE/REALIZATION_CHECK = QUALIFIED: producer implementation computes exact midpoint; authority validator does not bind it`
- `PROVENANCE_CHECK = PASS`
- `SAME_REALIZATION_CHECK = FAIL: same wrong local_mid_q mutation in both lanes survives exact cross-environment equality`
- `NUMERICAL/STATISTICAL_CHECK = QUALIFIED; terminal exact booleans/6 cases/19 leaves/0 unresolved reproduced historically, but midpoint identity is not independently reconstructed`
- `COUNTEREXAMPLE_ATTEMPTS = C4 rejected; premature unresolved rejected; wrong exact local midpoint accepted — SUCCESS decisive`
- `OVERCLAIM_CHECK = PASS after this qualification; historical scoped claim retained as immutable result but not independently confirmed as full-contract authority`
- `VERDICT = INVALID_IMPLEMENTATION`
- `QUALIFICATIONS = no evidence active producer emitted a wrong midpoint; no scientific FAIL; defect is authority-path contract binding`
- `UPDATED_STATE = Iter504U historical terminal PASS preserved but independently qualified INVALID_IMPLEMENTATION; Iter504V execution should wait for authority repair`
- `NEXT_ADMISSIBLE_GATE = prospectively frozen same-science verifier repair: enforce Fraction(local_mid_q)==(Fraction(amp_lower_q)+Fraction(amp_upper_q))/2 in assembler and repaired Critic; add adversarial wrong-midpoint fixture; retain C4 and premature-depth controls. Also bind parent-inclusion child/parent interval identities to the reconstructed dyadic tree. No physics rerun is required if frozen source artifacts remain available and unchanged. Any change to cohort, source realization, precision, threshold, floor, depth, partition rule, classifier semantics or interpretation ceiling requires a new preregistered scientific gate.`
