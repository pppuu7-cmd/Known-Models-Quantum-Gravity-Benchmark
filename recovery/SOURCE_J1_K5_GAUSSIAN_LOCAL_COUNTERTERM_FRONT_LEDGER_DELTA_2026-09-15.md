# Recovery/front ledger delta — Gaussian local-counterterm renormalization

Date: 2026-09-15

## STATE_READ

Authoritative parent before this delta:

- `AUX_GAUSSIAN_UNRENORMALIZED_COMPACT_LOCAL_DIVERGENCE_SCOPED`
- parent result commit `a0ba962811b9364bceb03a28f4785aa75e42213a`

Prospectively frozen child gate:

- `SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION_GATE`
- final pre-run frozen prereg commit `ef8d34d3e82bec110c072f2b23361f7e2d07339c`

## TERMINAL RESULT

Production run `34958385950`, head `d6def218a9977db5a8ee881dc0c3ddbfaaaeeb19`, aggregate job `104346212113`.

Terminal scientific classification:

`AUX_GAUSSIAN_LOCAL_COUNTERTERM_ANSATZ_INSUFFICIENT_SCOPED`

Canonical result:

`results/SOURCE_J1_K5_GAUSSIAN_LOCAL_COUNTERTERM_RENORMALIZATION_TERMINAL_2026-09-15.md`

Result commit: `ae29ddbb41153e73d182173d6261e01f48a0bd00`.

Aggregate artifact:

- ID `10391698051`
- digest `sha256:5b177b1ddb812997344ae7567924cd0af260fcb3b5ac74db2f5f1a43d3631880`

All frozen aggregate controls passed.

For every held-out alpha `{0.55,0.95,1.35,1.75,1.95}`:

- P1 = `DIVERGENT_AFTER_LOCAL_SUBTRACTION`
- P2 = `FINITE_COMPATIBLE`
- P3 = `DIVERGENT_AFTER_LOCAL_SUBTRACTION`

## NEW SCIENTIFIC FACT

On the exact auxiliary scalar aligned-K5 Gaussian witness, subtracting the complete prospectively frozen O(4)-invariant full-collision local basis through the naive uniform divergence degree 26 (`Delta^j delta_0`, j=0..13) does not remove the held-out divergence on P1 and P3.

This rejects that frozen full-collision radial ansatz/test protocol. It does not reject all local/stratified renormalizations.

## COLLISION-PARTITION STREAM STATUS

Historical branch `research/iter461-k5-collision-partitions` still points to `05c7f87c8519349057332bf90021f1128e1eefc3`.
Historical run `34748503239` remains `queued` with zero materialized jobs as of 2026-09-15, so it has no scientific artifact to consume and must not be cited as a terminal result.

However the frozen branch code at parent commit `e2dc23b53672693b9a61e6a7687f59e80670a5ed` explicitly enumerates the 52 set partitions of K5 vertices, 51 nontrivial collision partitions, and six partition types. Its combinatorics may be source-locked and independently rechecked in a new gate, but its 3D local-dimension thresholds must not be imported into the present scalar Gaussian surrogate without adaptation.

## ACTIVE FRONT

The immediate methodological question is now whether the failed full-collision-only subtraction omitted required proper collision-stratum counterterms and/or used inappropriate uniform power counting for anisotropic correlated regulator paths.

The next admissible gate should therefore first produce an exact collision-stratum superficial-divergence certificate for the **scalar Gaussian surrogate**, reusing only K5 partition combinatorics while recomputing scalar dimensions and divergence degrees. It must not merely increase the polynomial degree post hoc.

## CLAIM CEILING / GLOBAL LOCKS

Unchanged:

- RQIR Core v1.0 = FROZEN.
- D7-S2 = NOT_CLOSED.
- D7-S3 = NOT_CLOSED.
- D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED.
- terminal D7 labels forbidden.
- `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` forbidden.
- Candidate Gravity inactive.
- KMQGB remains downstream of pinned DSIR authority.
