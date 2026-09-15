# KMQGB Critical Review — scalar K5 collision-strata power counting

Date: 2026-09-15
Lane: independent Critical Review / Verification

## RESULT_REVIEWED

Exactly one latest terminal substantive Research result was reviewed:

- `results/SOURCE_J1_K5_GAUSSIAN_SCALAR_COLLISION_STRATA_POWER_COUNTING_TERMINAL_2026-09-15.md`
- historical result commit `81094144184751770256ab3bb144bd9189a6a9ad`
- historical classification `AUX_GAUSSIAN_K5_PROPER_COLLISION_SUBDIVERGENCES_PRESENT_SCOPED`
- preregistration commit `2f6d3af60439af4bc8b7c62e6813c58fb21ec1f4`
- implementation commit `e742afd2360d087be457b2b0bccc8f72da6e9175`
- workflow head `02a8ecb2ab7b90ddfc9f25b9a6da8bb4b821cd4d`
- authoritative Actions run `34959350188`, terminal `completed/success`
- job `104348959518`
- artifact `scalar-collision-strata-power-counting`, ID `10391514486`
- artifact digest `sha256:abaf3129d9555eed4d78f9fcb4464a60fd6c022cad82224431c9a5157ab11320`

The review is bounded to the exact scalar K5 partition/power-counting theorem and the combined-scientific-meaning sentence that imports the parent P1/P3 claim. Historical result text is not rewritten.

## PREREG_CHECK

PASS.

The gate was prospectively frozen before implementation. Direct comparison shows `e742afd...` is one commit ahead of prereg `2f6d3af...` and adds only the certificate implementation. The workflow source-lock replays the frozen preregistration from `2f6d3af...` before execution.

Frozen scientific contract is clear and outcome-sensitive:

- K5 vertex set `{1,2,3,4,5}`;
- all 52 set partitions generated independently;
- scalar collision normal dimension `d_perp = sum_B (|B|-1)`;
- one-dimensional edge scaling degree exactly 3;
- `E_int = sum_B C(|B|,2)`;
- `omega = 3 E_int - d_perp`;
- proper strata exclude all-singletons and full collision;
- PASS iff controls pass and at least one proper stratum has `omega >= 0`;
- result must state whether all or only a subset of proper strata are divergent;
- `INVALID_IMPLEMENTATION` covers wrong partition count/dimension/scaling degree, imported 3D thresholds, or label dependence.

No post-hoc threshold/domain/state selection was found.

## OBJECT_IDENTITY_CHECK

PASS for the frozen object.

The reviewed object is explicitly an auxiliary **scalar** K5 Gaussian collision-strata power count. It is not the physical EPRL vertex, not a three-dimensional collision-normal realization, not a source-authorized forest formula, and not a distributional-existence theorem.

The implementation computes exactly the preregistered set-partition object and explicitly separates proper collision strata from the full collision.

## SOURCE/REALIZATION_CHECK

PASS for the scalar surrogate; parent-dependent wording requires qualification.

The production implementation uses the frozen scalar realization, with `dimension_multiplier=1`, and includes an adversarial synthetic 3D table only as a negative control. The Actions certificate reports `scalar_formula_differs_from_3d_control = true`; therefore the historical Iter461 3D thresholds were not silently imported.

The terminal result's exact child theorem is realization-consistent. However, its combined-scientific-meaning item 2 states that the complete full-collision action did not remove **P1/P3** held-out divergence. The immediately preceding independent Critic audit `recovery/CRITICAL_REVIEW_SOURCE_J1_K5_GAUSSIAN_FULL_COLLISION_RADIAL_ACTION_COMPLETENESS_2026-09-15.md` established that P3's reported 180-digit residual is a catastrophic-cancellation artifact, while P1 remains independently stable and divergent. Therefore downstream scientific wording must consume that qualification.

## PROVENANCE_CHECK

PASS.

Authoritative run `34959350188` is terminal success at workflow head `02a8ecb...`. Job logs show checkout of that exact SHA, replay of the frozen preregistration, execution of `code/source_j1_k5_gaussian_scalar_collision_strata_power_counting.py`, verdict validation, and artifact upload.

The durable result metadata matches the live Actions record:

- job `104348959518`;
- artifact ID `10391514486`;
- artifact size 1831 bytes;
- digest `sha256:abaf3129d9555eed4d78f9fcb4464a60fd6c022cad82224431c9a5157ab11320`;
- artifact head SHA `02a8ecb2ab7b90ddfc9f25b9a6da8bb4b821cd4d`.

Green CI is treated only as execution provenance, not as scientific proof.

## SAME_REALIZATION_CHECK

PASS for the exact child theorem.

The same scalar formula is used at partition level, type aggregation, all 120 relabelings, and the production classifier. No numerical regulator-path values enter the decision.

The parent P3 numerical divergence is not needed to prove the child classification: the existence of proper superficially divergent scalar strata follows exactly from the frozen combinatorics. Therefore the P3 correction qualifies the combined narrative but does not invalidate the child theorem or classification.

## NUMERICAL/STATISTICAL_CHECK

PASS; the decisive result is exact and non-statistical.

Independent analytic control reproduces the complete type table. For any non-singleton block of size `s >= 2`, its contribution is

`3 C(s,2) - (s-1) = (s-1)(3s-2)/2 > 0`.

Hence every proper collision partition, which contains at least one non-singleton block, has strictly positive `omega`. The exact proper types are:

- `2+1+1+1`: multiplicity 10, `(E_int,d_perp,omega)=(1,1,2)`;
- `2+2+1`: multiplicity 15, `(2,2,4)`;
- `3+1+1`: multiplicity 10, `(3,2,7)`;
- `3+2`: multiplicity 10, `(4,3,9)`;
- `4+1`: multiplicity 5, `(6,3,15)`.

Thus all `10+15+10+10+5 = 50/50` proper strata are superficially divergent. The full collision gives `(10,4,26)` as frozen.

The Actions log independently reports:

- `proper_count=50`;
- `proper_divergent_count=50`;
- `all_proper_divergent=True`;
- `proper_omega_values=[2,4,7,9,15]`;
- all exact controls true, including all 120 permutations.

No floating-point conditioning or statistical inference enters this child decision.

## COUNTEREXAMPLE_ATTEMPTS

1. **Wrong partition enumeration.** Failed: Bell total 52, 51 nontrivial collision partitions, six frozen collision types and exact multiplicities are reproduced.
2. **A proper convergent stratum.** Failed analytically: each non-singleton block contributes `(s-1)(3s-2)/2 > 0` for `s>=2`, so every proper stratum has `omega>0`.
3. **Imported 3D collision dimension.** Failed: production scalar table differs from the synthetic 3D control, exactly as preregistered.
4. **Label/covariance dependence.** Failed: the full type/omega multiset is invariant under all 120 S5 relabelings.
5. **Scaling-degree classifier not actually used.** Failed: the synthetic edge-scaling-degree-1 table changes proper-stratum omega values.
6. **Finite power-count certificate promoted to a forest theorem.** Prevented by the frozen interpretation ceiling: the result establishes superficial power counting only and does not construct or prove a forest subtraction.
7. **Set-partition surrogate promoted to physical EPRL collision theorem.** Prevented by scope: this is explicitly an auxiliary scalar Gaussian witness, not source-level Eq. (4) or the physical vertex.
8. **Parent P3 divergence used as a premise.** Explicit counterexample already exists in the immediately preceding Critic: the 320-digit same-object replay invalidates the parent P3 divergence subclaim. This does not refute the child power count, but it refutes the unqualified phrase `P1/P3 held-out divergence` in combined scientific meaning.
9. **Green CI promoted to science.** Rejected: the exact combinatorial identity above independently proves the decision.

## OVERCLAIM_CHECK

The terminal child classification and its frozen consequence are correctly scoped:

`AUX_GAUSSIAN_K5_PROPER_COLLISION_SUBDIVERGENCES_PRESENT_SCOPED`

and, under the frozen scalar uniform power count, a full-collision-only subtraction is not a complete forest/stratum analysis because proper superficially divergent collision strata exist.

One sentence is overbroad: the combined-scientific-meaning statement that the complete full-collision action did not remove **P1/P3** held-out divergence must be read as **P1 confirmed; P3 not validated**. The child theorem does not repair the parent P3 numerical failure.

No forest-renormalized extension, path-independent finite limit, source authorization, physical model failure, Eq. (4) existence/nonexistence, D7 closure, terminal selector, or Candidate Gravity activation follows.

## VERDICT

`QUALIFIED`

The exact scalar K5 collision-strata theorem and terminal classification are independently confirmed. The only material qualification is inherited: the terminal result's combined narrative must not consume P3 divergence as a validated premise. That qualification does not alter the exact `50/50` proper-strata result or the scoped conclusion that full-collision-only subtraction is structurally incomplete as a forest/stratum analysis under the frozen scalar power count.

## QUALIFICATIONS

1. `50/50` proper K5 scalar collision strata superficially divergent with omega set `{2,4,7,9,15}` is confirmed exactly.
2. The classification `AUX_GAUSSIAN_K5_PROPER_COLLISION_SUBDIVERGENCES_PRESENT_SCOPED` remains valid.
3. The conclusion is about the frozen auxiliary scalar uniform power count, not a physical/source-level EPRL forest theorem.
4. Parent P1 divergence remains a validated downstream premise; parent P3 divergence does not.
5. Historical Research result remains immutable; no scientific FAIL is introduced.
6. Iter504 run `34907349374` and Iter461 run `34748503239` were freshly checked and remain `queued / conclusion=null`; no partial substantive values were consumed.
7. `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; terminal selectors remain forbidden; Candidate Gravity remains inactive.

## UPDATED_STATE

- `SOURCE_J1_K5_GAUSSIAN_SCALAR_COLLISION_STRATA_POWER_COUNTING = QUALIFIED` by independent Critic.
- exact child classification = confirmed scoped.
- exact proper-stratum census = `50/50` divergent.
- full collision = `omega=26` confirmed.
- full-collision-only analysis = structurally incomplete under the frozen scalar power count.
- parent P1 divergence = still independently stable.
- parent P3 divergence = not validated; must not be imported unqualified.
- no forest subtraction existence/uniqueness/path-independence result yet.
- governance state unchanged.

## NEXT_ADMISSIBLE_GATE

Proceed only with a prospectively frozen connected-collision / laminar-forest certificate on the same auxiliary scalar object, as the Research result already proposes. Freeze before execution:

- connected collision subsets `S subseteq {1,...,5}`, `2<=|S|<=5`;
- exact scalar superficial degree for each subset from the same frozen formula;
- laminar compatibility (`A subset B`, `B subset A`, or `A cap B = empty`);
- complete forest/orbit census, maximal nesting depth, and counterterm-order assignment;
- positive controls against the confirmed K5 partition census;
- adversarial controls that distinguish overlapping/non-laminar families and prevent a partition-level count from being promoted automatically to a forest theorem;
- interpretation ceiling separating combinatorial forest structure from existence, uniqueness, path independence, source authorization, and physical EPRL claims.

Any downstream use of the Gaussian parent numerical lane must carry the existing P3 precision qualification. A P3 numerical repair may raise precision/conditioning controls without changing the frozen scientific object; changes to grids, basis, classifier, thresholds, or object require a new prospectively frozen gate.
