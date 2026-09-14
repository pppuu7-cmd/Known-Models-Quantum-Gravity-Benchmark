# Current active front index — 2026-09-15

This file is a compact navigation index over immutable result/prereg/recovery records. It supersedes stale iteration numbers in legacy `recovery/state.json`, `recovery/RESTORE_FROM_NEW_CHAT.md`, and the older `CURRENT_BENCHMARK_FRONT.md` **for locating the active frontier only**. It does not erase or rewrite their historical content.

## Frozen global state

- Repository/polygon: `pppuu7-cmd/Known-Models-Quantum-Gravity-Benchmark`.
- Judge: `RQIR Core v1.0 = FROZEN`.
- `D7-S2 = NOT_CLOSED`.
- `D7-S3 = NOT_CLOSED`.
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
- Terminal D7 selectors/labels are forbidden until their required subgates close.
- Candidate Gravity is inactive and may not tune the judge.

## D7-S2 numerical front — active Iter504

### Method blocker history

- Iter501 direct continuous natural-interval gate: `ITER501_NUMERICAL_METHOD_BLOCKER`, run `34820198677`.
- Iter502 fixed 8-way dyadic repair: `ITER502_NUMERICAL_METHOD_BLOCKER`, run `34830476485`.

### Qualified centered method chain

1. Iter503 mainline centered dependency repair: `ITER503_CENTERED_DEPENDENCY_REPAIR_ENABLED_SCOPED`, run `34895563822`.
2. Iter503D independent dual-source derivative audit: PASS, 1440/1440 identities. See `recovery/ITER503D_RECOVERY_FRONT_LEDGER_DELTA_2026-09-15.md`.
3. Iter503V independent endpoint verifier: `ITER503V_ENDPOINT_CONTRACT_CONFIRMED`, run `34898125306`, 288/288 checks. See:
   - `results/ITER503V_ENDPOINT_CONTRACT_TERMINAL.md`;
   - `recovery/ITER503V_RECOVERY_FRONT_LEDGER_DELTA_2026-09-15.md`.

### Active full science gate

Iter504 prereg authority:

`recovery/ITER504_PREREG_CENTERED_FULL_MAX_ENVELOPE_SCIENCE_2026-09-15.md`

prereg commit `1ab46b7add51b36b5499f866eb4579137838bfae`; production head `56362459a826e3e376c529446678f2fbcaa269ae`; workflow `iter504-centered-full-max-envelope-science`; run `34907349374`.

Current consumed state at time of this index update:

- source-lock job `104186984965` = success;
- all 12/12 point-regression jobs are CI-success and all 12 named point artifacts are present;
- first centered box-shard jobs are running; the remaining 96-shard matrix is queued/materializing under the same frozen run;
- aggregate result is **not yet available**;
- no Iter504 DECAY/NONDECAY classification may be inferred before the aggregate validates exact completeness, controls and point containment.

Frozen Iter504 aggregate cardinalities: 12 logical lanes, 96 centered box shards, 12 point artifacts, 768 direction/sign/box records, 3072 rho/box states, 1728 point-containment checks, all 243 channels. Frozen thresholds remain drift `0.05`, robust NONDECAY `+1.0`, NONDECAY `0.0`, uniform DECAY `-0.10`.

## Source-order causal-vertex front — new analytical separation

The primary source order is now explicitly separated from the reordered ten-spectral representation:

`one-wedge Feynman boundary value -> T_e(g) -> four-group Haar integral of product_e T_e`.

See the corrected `research/TEN_SPECTRAL_CUTOFF_LOCAL_EXISTENCE_2026-09-15.md`. Spectral/Fubini admissibility is required to identify a reordered direct-substitution `<W,C>` representation with the source-order object; it is not a prerequisite merely to define the published source-order causal vertex.

### Noncompact Haar tails away from collisions

`research/SOURCE_ORDER_K5_HAAR_TAIL_SPANNING_TREE_THEOREM_2026-09-15.md`

proves, for fixed finite labels and every fixed collision cutoff `delta>0`, absolute integrability of the complete four-group noncompact tail. The proof uses the published edge asymptotic `|T_e| <= C_delta exp(-beta_e)`, the 125 spanning trees of K5, the exact averaging identity `average_T L_T=(2/5) sum_e beta_e`, and the SL(2,C) radial Haar threshold `alpha>2` with tree exponent `5/2`.

Status:

`SOURCE_ORDER_HAAR_TAIL_AWAY_FROM_COLLISIONS = ABSOLUTE_JUSTIFIED_SCOPED`.

### Exact j=1 collision poles and full-collision absolute divergence

`research/SOURCE_J1_TOLLER_COLLISION_POLE_LEDGER_2026-09-15.md`

derives the exact causal one-edge pole

`T_plus/minus ~ +/- [3 i/(4 rho(1+rho^2))] beta^-3 D^1(U1) diag(1,-2,1) D^1(U2)`.

`research/SOURCE_J1_FULL_COLLISION_ABSOLUTE_DIVERGENCE_THEOREM_2026-09-15.md`
then proves a scoped fixed-channel result: for allowed j=1 intertwiner channel `00000`, all three frozen causal signatures have a nonzero full-collision cubic leading network. A fixed rational tangent configuration gives exact angular coefficient `11/24`; the 12-dimensional normal measure then yields `t^11 * t^-30 = t^-19`, so the ordinary absolute Haar integral diverges locally at the full K5 collision.

Exact reproducibility code:

`code/source_j1_full_collision_leading_certificate.py`

with certificate workflow run `34908370750` registered from head `020f43695f16332d749f3d6d5c65dbd0b6a098d8`; consume its terminal artifact when available.

Interpretation ceiling:

- ordinary absolute integrability is rejected for this fixed allowed j=1 channel;
- no principal-value, conditional, Feynman/distributional finite part is excluded or established;
- `D7-S2` therefore remains `NOT_CLOSED`, but its source-order blocker is now sharply localized to the legitimacy/uniqueness of a non-absolute collision extension rather than noncompact infinity away from collisions.

## Reordered ten-spectral / correlated-kernel front

Upstream audit: `research/TEN_SPECTRAL_TENSOR_PRODUCT_SOURCE_AUDIT_2026-09-14.md`. Iter468 authority: run `34770144171`, artifact `10322025879`, classification `ITER468_EQ4_SOURCE_SPECTRAL_GROUP_CONTRACTION_OBJECT_PINNED_SCOPED`.

Current records:

1. `recovery/ITER503V_PARALLEL_SPECTRAL_ADMISSIBILITY_SCAFFOLD_2026-09-15.md` — `A_abs`/`A_dist`, operation-specific microlocal obligations and exchange ledger.
2. `research/TEN_SPECTRAL_CUTOFF_LOCAL_EXISTENCE_2026-09-15.md` — explicitly distinguishes primary source order from reordered/direct-substitution order; cutoff-local reordered pairing is `PROVED_SCOPED`.
3. `research/TEN_SPECTRAL_TEMPERED_SUFFICIENT_CLASS_2026-09-15.md` — one-wedge source kernels are tempered, ten-fold tensor product lies in `S'(R^10)`, and `C in S(R^10)` is a concrete sufficient reordered spectral-pairing target, not a proved property of the physical correlated kernel.

No reordered spectral result substitutes for the source-order collision theorem or Iter504.

## Iter461 K5 collision stream — independent, do not duplicate

- branch `research/iter461-k5-collision-partitions`;
- head `05c7f87c8519349057332bf90021f1128e1eefc3c`;
- run `34748503239`;
- last checked status: queued / no computation artifact to consume.

Prospective consumer contract: `recovery/ITER461_CONSUMER_PREREG_SPECTRAL_COLLISION_MAP_2026-09-15.md`.

Do not recreate the exact collision enumeration while the authoritative run remains registered. The new full-collision theorem does not consume or replace Iter461 because Iter461 is still needed to organize all other collision strata and incidence/codimension data.

## Immediate restoration procedure

1. Inspect Iter504 run `34907349374`; if terminal, consume `iter504-summary`, never infer science from workflow color or individual shards.
2. Inspect exact collision-certificate run `34908370750`; if terminal success, record its artifact/digest in a result/recovery delta. Failure is a reproducibility/code issue and must be resolved before promoting the certificate.
3. Record any terminal Iter504 classification without changing frozen thresholds.
4. Inspect Iter461 run `34748503239`; consume only when its frozen artifact exists.
5. Continue source-defined collision-extension analysis while keeping ordinary absolute divergence, conditional/PV finite parts and distributional/Feynman amplitudes distinct.
6. Keep reordered ten-spectral exchange theorems separate from primary source-order existence.
