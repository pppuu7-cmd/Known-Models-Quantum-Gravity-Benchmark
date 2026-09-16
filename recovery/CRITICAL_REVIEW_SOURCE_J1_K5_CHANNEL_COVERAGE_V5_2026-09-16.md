# KMQGB Critical Review — exact K5 channel coverage V5

Date: 2026-09-16
Lane: independent Critical Review / Verification

## RESULT_REVIEWED

Exactly one latest terminal substantive Research execution was reviewed:

- gate: `SOURCE_J1_K5_CHANNEL_COVERAGE_V5`
- preregistration commit: `d30274a74e206287b5dc3cf9cba02fa66e13c74b`
- implementation commit: `abff2fceb51519ef47461f0060454f89ca798353`
- workflow head: `22fb468b79218176fe628266d311909cf87ddca5`
- authoritative Actions run: `35041893961`, terminal `completed/success`
- Python 3.11 job: `104623351833`
- Python 3.13 job: `104623351638`
- aggregate job: `104624134356`
- Python 3.11 artifact: `10424574808`, digest `sha256:847ce7d9f818069861adb98e8b05c62ca4a9f5ceefb3a3437ec5b8ce0b5c238f`
- Python 3.13 artifact: `10425721638`, digest `sha256:c4cd1f7c94254344347d55cff51eac7f5d0464a7780ec5485c01fc5a00122b29`
- aggregate artifact: `10425727109`, digest `sha256:a8775abfca4f5059eb55a72d1ed58a1ee4464fecc211e122ca15a51850666e7d`
- Research classification emitted by both exact lanes and aggregate: `CHANNEL_COVERAGE_NONZERO_SCOPED`

No historical result is rewritten by this audit.

## PREREG_CHECK

PASS for chronology; QUALIFICATION for scientific discriminating power.

Chronology is prospective and clean:

`fd790552...` parent -> `d30274a...` preregistration -> `abff2fc...` implementation -> `22fb468...` workflow.

A direct compare from the parent `fd790552...` to workflow head `22fb468...` shows exactly three added files: the V5 preregistration, V5 code, and V5 workflow. No parent V4 source/input/contraction file changed between the Critic-confirmed parent front and this execution.

The frozen V5 contract requires:

- same V4 repaired source realization and same fixed tangent witness;
- the exact three-dimensional `j=1` four-valent intertwiner channel basis at each of five vertices;
- exact enumeration of all `3^5 = 243` channel tuples without duplicates;
- no floating-point decision path;
- exact lock `channel 00000 = 11/24`;
- one zero-edge negative control making the complete cube vanish;
- two Python lanes with fail-fast disabled and complete map/count agreement;
- classification `CHANNEL_COVERAGE_NONZERO_SCOPED` iff controls pass and exact nonzero support exists.

The contract has one important design limitation: the required positive control `channel_00000 = 11/24` already guarantees that nonzero support exists. Therefore the frozen classification cannot discriminate a cube with only channel `00000` nonzero from a broadly supported cube. The new scientific information is the exact channel map/count itself, not the logical fact of nonzero support.

## OBJECT_IDENTITY_CHECK

PASS_SCOPED.

The implementation enumerates the frozen fixed-tangent `j=1` K5 angular contraction over channel tuples in `{0,1,2}^5`. For four spin-1 legs the invariant recoupling space is three-dimensional, corresponding to intermediate channels `J=0,1,2`; hence `3^5=243` is the complete channel cube for this frozen basis.

The implementation preserves the V4 tangent points and K5 edge tensors by reading the existing V4 input and reusing the exact Cartesian intertwiner, `Q(v)`, contraction-path, and rational contraction routines. Parent-to-head comparison confirms no source/input mutation in those files.

This object remains a finite fixed-tangent channel tensor. It is not all tangents, all spins, a joint distribution product, or the complete EPRL vertex.

## SOURCE/REALIZATION_CHECK

PASS_SCOPED with a provenance hardening note.

V5 imports the established exact V4 kernel module `source_j1_k5_highest_contact_magnetic_leading_transfer_v4` for the Cartesian intertwiner basis, K5 edge list, `Q(v)`, and contraction routine. The later V4 repair wrapper itself delegates these same exact kernel functions to that base module; the repair changed V4 control/classifier logic, not the angular contraction kernel used here.

No source/realization mismatch was found in the channel map computation. However, V5 does not itself emit a blob lock for the imported kernel/input. The repository ancestry makes the execution reproducible for run `35041893961`, but a future repair/hardening should record exact imported blob SHAs in the artifact rather than relying only on workflow-head ancestry.

## PROVENANCE_CHECK

PASS.

Run `35041893961` is terminal `completed/success` at exact head `22fb468b79218176fe628266d311909cf87ddca5`. Both exact jobs and aggregate completed successfully. Aggregate logs show both lane artifacts were downloaded with expected digests, compared on classification, controls, counts, complete channel map, map SHA256, and channel `00000`, then re-uploaded as aggregate artifact.

The aggregate reports:

- `channel_00000 = 11/24`;
- `channel_map_sha256 = 2bceeb84db17ef0f01df4aa3350f8800d9e8e531ed68ed9ef10ca10cecfc9d0d`;
- `total_channels = 243`;
- `nonzero_count = 224`;
- `zero_count = 19`;
- controls `channel_00000_lock`, `enumeration_complete`, and `zero_edge_negative` all true.

Green CI is used only as provenance. Scientific confirmation below comes from exact replay/analytic structure.

## SAME_REALIZATION_CHECK

PASS_SCOPED.

The same exact tangent points, edge tensors, intertwiner basis, contraction path, and rational contraction function are used for all 243 production channels and for the zero-edge negative fixture. No floating-point threshold or post-hoc channel selection enters the map.

The zero-edge negative fixture is mathematically valid but weak: because the network contraction is multilinear in each edge tensor, replacing any one edge tensor by exact zero forces every channel contraction to zero. It confirms that the executed network consumes that edge factor, but it does not independently validate the 224/19 support pattern.

## NUMERICAL/STATISTICAL_CHECK

PASS_EXACT_NONSTATISTICAL.

The production map is computed with exact `fractions.Fraction` entries in object arrays. The only floating-point arrays are dummy arrays used to choose an einsum contraction path; they do not enter decision values.

An independent exact replay of the frozen Cartesian tensors, tangent points, ten `Q(v)` edge matrices, and all `3^5` channel contractions reproduces:

- exactly 243 distinct channels;
- channel `00000 = 11/24`;
- exactly 224 nonzero channels;
- exactly 19 zero channels.

Thus the observed support census is independently confirmed as an exact finite statement on the frozen basis and tangent witness.

## COUNTEREXAMPLE_ATTEMPTS

1. **Incomplete channel cube.** Failed: the four-spin-1 invariant channel basis has dimension 3 and the product basis has exactly `3^5=243` tuples; enumeration contains 243 unique tuples.
2. **Duplicate/ordering omission.** Failed: `itertools.product(range(3), repeat=5)` gives the complete lexicographic cube and the result contains 243 distinct keys.
3. **Wrong fixed-channel parent lock.** Failed: independent exact replay gives `00000 = 11/24`.
4. **Floating-point support misclassification.** Failed: values are exact rational objects and zero/nonzero is exact.
5. **Lane dependence.** Failed: Python 3.11 and 3.13 agree on the complete channel map and its SHA256.
6. **Edge factor ignored.** The frozen zero-edge fixture passes, but this is only a weak structural control because multilinearity makes its expected outcome automatic once the edge participates.
7. **Classification discriminates broad support.** Counterexample succeeds against that stronger interpretation: a hypothetical exact map with `00000=11/24` and all other 242 channels zero would pass the frozen positive lock, enumeration completeness, and zero-edge negative control and would still classify `CHANNEL_COVERAGE_NONZERO_SCOPED`. Therefore the classification by itself cannot establish "broad" support.
8. **Finite channel census promoted to all tangents/spins/family closure.** Rejected by the frozen interpretation ceiling.
9. **Green CI promoted to science.** Rejected: exact replay independently confirms the finite map/count.

## OVERCLAIM_CHECK

The literal finite result is sound:

- the frozen fixed-tangent `j=1` K5 channel cube has 224 nonzero and 19 zero entries in the frozen intertwiner basis;
- `00000 = 11/24`;
- complete map digest is `2bceeb84db17ef0f01df4aa3350f8800d9e8e531ed68ed9ef10ca10cecfc9d0d`.

The classification `CHANNEL_COVERAGE_NONZERO_SCOPED` is technically true but scientifically weaker than the enumeration: because `00000=11/24` is itself a mandatory positive control, nonzero support was already frozen in advance. The phrase "broad nonzero support" has no prospectively frozen metric or threshold in V5 and must not be used as a decision predicate after seeing `224/243`.

The exact count `224/243` may be consumed downstream as a scoped observed fact. Any claim that support is "broad enough" to authorize a new physical/scientific conclusion must be frozen prospectively in the next gate.

No joint distribution-product existence/nonexistence, all-tangent statement, all-spin statement, complete-vertex convergence/divergence, model/family failure, D7 closure, selector, or Candidate Gravity activation follows.

## VERDICT

`QUALIFIED`

The exact finite channel map and the `224/243` support census are independently confirmed. The qualification is that the frozen PASS classification is logically guaranteed by the already-required nonzero `00000` positive control and therefore does not itself test broad channel support. V5 is valid as an exact enumeration/census, not as a prospectively discriminating theorem that support is "broad".

## QUALIFICATIONS

1. `243` complete frozen-basis channels = confirmed.
2. `224` nonzero / `19` zero = confirmed exactly.
3. `00000 = 11/24` = confirmed.
4. Full channel-map SHA256 `2bceeb84db17ef0f01df4aa3350f8800d9e8e531ed68ed9ef10ca10cecfc9d0d` = reproduced across both Actions lanes.
5. `CHANNEL_COVERAGE_NONZERO_SCOPED` is true but tautologically implied by its mandatory positive control once controls pass.
6. No prospectively frozen definition of "broad support" exists in V5.
7. The result remains fixed-tangent, `j=1`, finite-basis scoped.
8. Iter504 run `34907349374` and Iter461 run `34748503239` were freshly checked and remain `queued / conclusion=null`; no partial substantive values were consumed.
9. `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; terminal selectors remain forbidden; Candidate Gravity remains inactive.

## UPDATED_STATE

- `SOURCE_J1_K5_CHANNEL_COVERAGE_V5 = QUALIFIED` by independent Critic.
- exact channel census `224/243` nonzero = confirmed scoped.
- exact complete channel map = confirmed for frozen tangent/basis.
- historical/fresh V4 parent results remain unchanged.
- V5 classification must not be promoted to a thresholded "broad support" claim.
- governance unchanged.

## NEXT_ADMISSIBLE_GATE

Two admissible directions remain distinct.

1. If the next scientific question is **channel-support breadth**, prospectively freeze a new gate before consuming V5's observed support pattern as a decision criterion. Define in advance the support statistic, basis dependence, any symmetry/orbit quotient, and the exact PASS/FAIL threshold. Do not retrofit a threshold to `224/243`.

2. If the next scientific question is **joint contact-distribution transversality/wavefront admissibility**, prospectively freeze the actual joint distribution-product object, covectors/wavefront criterion, same-realization dependencies, PASS/FAIL/BLOCKED semantics, and counterexamples. V5's exact channel map may be an input, but `224/243` by itself does not establish product existence or failure.

For provenance hardening, pin and emit exact blob SHAs of the imported V4 contraction kernel and tangent/input file in future artifacts. Any change of tangent realization, intertwiner basis, channel definition, source authority, or decision threshold requires a new prospectively frozen gate.
