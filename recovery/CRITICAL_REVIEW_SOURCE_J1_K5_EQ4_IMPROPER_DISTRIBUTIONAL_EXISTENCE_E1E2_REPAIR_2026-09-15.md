# KMQGB Critical Review — repaired Eq. (4) improper distributional-existence gate

Date: 2026-09-15
Lane: independent KMQGB Critical Review / Verification

## RESULT_REVIEWED

Exactly one latest terminal substantive Research / Closure result was reviewed:

- gate: `SOURCE_J1_K5_EQ4_IMPROPER_DISTRIBUTIONAL_EXISTENCE_E1E2_REPAIR_GATE`;
- historical Research classification: `SOURCE_J1_K5_EQ4_DISTRIBUTIONAL_EXISTENCE_BLOCKED_SCOPED`;
- terminal result: `results/SOURCE_J1_K5_EQ4_IMPROPER_DISTRIBUTIONAL_EXISTENCE_E1E2_REPAIR_RESULT_2026-09-15.md`;
- terminal result commit: `6c4d479c42d3b71de4c4c32c5abb910728b97fc9`;
- canonical JSON persistence commit: `9d6b90ca8b52896f6852c9649d2d43d521678b31`;
- Research handoff: `recovery/SOURCE_J1_K5_EQ4_IMPROPER_DISTRIBUTIONAL_EXISTENCE_E1E2_REPAIR_HANDOFF_2026-09-15.md`, commit `9ee7d28c2ac9227b593bf6f69a1abf1092be7eee`.

The claimed exact object is fixed source-order `j=1`, fixed nonzero-real-rho scope, channel `00000`, gauge-fixed `SL(2,C)^4`, full K5 collision, with ten source-defined one-wedge Toller distributions.

No Iter504 or Iter461 partial substantive value is used in this review.

## PREREG_CHECK

Prospective chronology is valid:

1. repaired preregistration `0d9615e1dec1f2fe5bcf66f3458a0e541a6b2ba4`;
2. initial structured manifest `72476e6e7d99eb2fbf2cde408e9a8d531f6270d0`;
3. implementation `a80dc307f4b109917cea0d3923761370f8d1aefa`;
4. initial workflow `9b7635dde7c14ca5df8eacf17a2b233f6675a79d`;
5. literal-only manifest repair `8d730f3bb9307dce84ab75a970020a45613edf23`;
6. production workflow/source-lock repair `1d4919f94c336f60425edd133555ccb47c420e0d`;
7. authoritative run `34942426243`;
8. terminal persistence/result commits thereafter.

The post-implementation manifest repair changed only the initial letter in one required-text literal, `do` -> `Do`. It did not alter the object, semantic facts, thresholds, PASS/FAIL/BLOCKED rules, or interpretation ceiling. The first failed run is therefore correctly treated as infrastructure/source-lock-literal failure rather than science.

However, the frozen preregistration itself contains a same-realization dependency defect described below. Repairing that defect changes the scientific contract and therefore cannot be done retroactively.

## OBJECT_IDENTITY_CHECK

The terminal result names a **fixed channel-`00000` contracted object**.

The decisive E2 premises do not establish their wavefront/Hörmander statement on that same fixed-channel object:

- `SOURCE_J1_K5_COHERENT_CONTACT_HORMANDER_RESULT_2026-09-15.md` is explicitly a **source coherent-state realization** with independently chosen wedge spinors and a frozen coherent witness `z_12=z_23=z_13=(1,0)^T`;
- `SOURCE_J1_K5_ALIGNED_CONTACT_CYCLESPACE_RESULT_2026-09-15.md` is explicitly an **aligned coherent-spinor witness** with all ten independent wedge spinors set to `z0=(1,0)^T`.

Those are legitimate scoped coherent-realization results. They are not, without an additional transfer theorem or direct calculation, the same object as the fixed intertwiner-channel `00000` network contraction used by the present existence gate.

The present certificate recomputes only the K5 conormal incidence geometry. It does not propagate the coherent contact distributions through the exact channel-`00000` Toller/intertwiner contraction and does not prove that the dangerous contact wavefront component survives that contraction with nonzero coefficient.

Therefore the exact-object identity required for E2 is not established.

## SOURCE/REALIZATION_CHECK

The following source facts remain admissible within their own scopes:

- the published `i epsilon` is a one-wedge Toller prescription and is not itself an already-proved ten-wedge joint K5 collision regulator/removal theorem;
- the coherent-state realization has an allowed contact witness at which the elementary Hörmander sufficient multiplication criterion fails;
- the aligned coherent-state witness has the exact six-dimensional K5 cycle-space relation structure;
- the independently reviewed fixed channel-`00000` object is not locally absolutely Haar-integrable near the full collision.

The invalid V1/V2 joint-selection-authority executable conclusions were correctly excluded.

What is missing is a source/representation identity theorem connecting the coherent-contact wavefront obstruction to the **specific fixed channel-`00000` contracted distribution** used as the exact object of this gate.

## PROVENANCE_CHECK

Execution provenance is sufficient and reproducible:

- authoritative Actions run `34942426243`;
- production head `1d4919f94c336f60425edd133555ccb47c420e0d`;
- run `completed/success`;
- source-lock job `104293955407`: success;
- exact-certificate job `104293987617`: success;
- artifact `10386295378`, `source-j1-k5-eq4-improper-existence-e1e2-repair`;
- artifact size `2086` bytes;
- artifact digest `sha256:1f72470954d0b8128b071f8a6de9bfdf369e42212c4ed0b2098a160a2daa27bf`;
- manifest SHA256 in the canonical result: `89f4077539655096e0d9824742ca6628d3b93feb4ea064f6af3bca24876d5ec5`.

The workflow source-locks the preregistration, repaired manifest, implementation, and each premise path against its frozen commit. Green CI is treated only as execution/provenance evidence, not as scientific proof.

## SAME_REALIZATION_CHECK

`FAILS FOR THE E2 TRANSFER USED BY THIS GATE`.

The E2 inference is:

coherent-spinor contact witness -> failure of standard Hörmander multiplication criterion -> `E2_SUFFICIENT_PRODUCT_CRITERION_PASSES=false` and `E2_SUFFICIENT_PRODUCT_CRITERION_FAILS_AT_ALLOWED_WITNESS=true` for the exact fixed channel-`00000` object.

The first arrow is valid only inside the coherent realization already frozen by the upstream gates. The second transfer to channel `00000` is not established.

An explicit abstract counterexample shows why such a transfer cannot be assumed. Let a two-component distribution-valued object have components `(delta(x), -delta(x))`. A linear/coherent evaluation selecting the first component contains the singular contact distribution and can fail a product-wavefront criterion, while the different fixed contraction `(1,1)` gives the identically zero smooth distribution. Thus wavefront obstruction of one linear realization is not invariant under an arbitrary later contraction: singular components can cancel. A K5 channel contraction may or may not cancel the relevant contact contribution; that must be proved for channel `00000`, not inferred from a different coherent evaluation.

The existing channel-`00000` full-collision leading-pole witness and absolute-divergence theorem do not repair this gap. They establish nonzero radial leading singularity / failure of ordinary absolute Haar integrability, not survival of the particular coherent `delta''(B)` wavefront combination required for the E2 Hörmander conclusion.

## NUMERICAL/STATISTICAL_CHECK

No statistical inference is involved. The certificate uses exact integer/rational linear algebra for the K5 conormal geometry and correctly verifies:

- ambient normal dimension 12;
- ten nonzero incidence conormals;
- `dB_12 + dB_23 - dB_13 = 0` exactly;
- conormal rank 4;
- relation-space dimension 6;
- star spanning-tree rank 4;
- wrong-sign control nonzero.

All six outcome-sensitivity fixtures reach the intended classifier branches, so the terminal label is not hard-coded by dead branches.

These exact checks validate the geometry of the frozen coherent witness and the classifier mechanics. They do not establish the missing coherent-to-channel-`00000` distributional transfer.

## COUNTEREXAMPLE_ATTEMPTS

1. **Prereg chronology / post-hoc repair:** no scientific post-hoc change found. The casing repair is literal-only.
2. **Invalid V2 authority leakage:** not found. The invalidated authority result is excluded and the invalid-control is live.
3. **Dead classifier branches:** not found. EXISTENCE, NONEXISTENCE, BLOCKED, and INVALID are all reachable by the frozen fixtures.
4. **Green CI promoted to science:** not found in the terminal prose; CI is explicitly called provenance only.
5. **Absolute divergence promoted to distributional nonexistence:** not found; the gate correctly rejects that inference.
6. **Failure of a sufficient criterion promoted to nonexistence:** not found; the gate correctly keeps BLOCKED distinct from FAIL.
7. **Wrong object / realization:** **counterexample found.** The E2 premises are coherent-spinor realizations whereas the target is fixed channel `00000`. The certificate has no contraction-level wavefront/contact survival proof.
8. **Linear-contraction cancellation control:** explicit abstract counterexample `(delta,-delta)` contracted by `(1,1)` demonstrates that a singular coherent/component evaluation need not imply a singular fixed contraction.
9. **Finite certificate promoted to universal theorem:** the terminal claim ceiling avoids family-wide promotion, but the finite exact conormal certificate is still over-transferred from coherent witness to the different fixed-channel E2 object.
10. **Child scope promoted to D7/family closure:** not found; governance ceiling is preserved.

## OVERCLAIM_CHECK

The result is careful not to claim distributional nonexistence, family failure, D7 closure, or a terminal selector.

Nevertheless, its exact-object sentence and terminal reasoning say that the standard Hörmander sufficient multiplication route fails for the fixed channel-`00000` Eq. (4) object. The frozen evidence establishes that failure only for coherent-spinor contact realizations. Without a same-realization bridge, the channel-specific E2 predicate is not validated.

Consequently the historical Research classification must remain immutable as history, but it must not be promoted to a validated downstream premise for the fixed channel-`00000` object.

## VERDICT

`REQUIRES_NEW_PREREGISTERED_GATE`

This is not `INVALID_IMPLEMENTATION`: the implementation follows the frozen repaired preregistration and its generic classifier is outcome-sensitive. The defect is in the frozen scientific dependency/object transfer itself. Repair requires changing the scientific contract, so the correct remedy is a new prospective gate.

This verdict does **not** establish the opposite conclusion. It does not establish distributional existence, a source-canonical extension, uniqueness, nonuniqueness, or distributional nonexistence.

## QUALIFICATIONS

1. Preserve the historical Research result and Actions artifact unchanged.
2. Preserve the published one-wedge `i epsilon` scope result within its source-audit scope.
3. Preserve the coherent-contact and aligned-cycle-space Hörmander results within their coherent-realization scopes.
4. Preserve the independently reviewed fixed channel-`00000` ordinary absolute-Haar divergence theorem.
5. Do not treat the current E2 coherent witness as a validated channel-`00000` wavefront obstruction until a transfer/direct contraction theorem is prospectively tested.
6. Do not use the current `SOURCE_J1_K5_EQ4_DISTRIBUTIONAL_EXISTENCE_BLOCKED_SCOPED` label as a validated downstream premise for the fixed channel-`00000` object.
7. No Iter504 or Iter461 partial substantive values are consumed.

## UPDATED_STATE

Critical-review qualification:

`SOURCE_J1_K5_EQ4_IMPROPER_DISTRIBUTIONAL_EXISTENCE_E1E2_REPAIR_GATE = REQUIRES_NEW_PREREGISTERED_GATE`

Historical Research label remains:

`SOURCE_J1_K5_EQ4_DISTRIBUTIONAL_EXISTENCE_BLOCKED_SCOPED` (historical, not independently validated for the claimed fixed channel-`00000` exact object).

Governance remains unchanged:

- `RQIR Core v1.0 = FROZEN`;
- `D7-S2 = NOT_CLOSED`;
- `D7-S3 = NOT_CLOSED`;
- `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`;
- terminal D7 labels and `EXISTING_SUFFICIENT / ADAPT_EXISTING / HYBRID_REQUIRED / NEW_REQUIRED` remain forbidden;
- Candidate Gravity remains inactive;
- no authority exists for `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

## NEXT_ADMISSIBLE_GATE

Prospectively freeze a **same-realization fixed-channel collision wavefront / representation-transfer gate** before reusing E2 in an existence classifier.

The new gate must choose one explicit route before calculation:

- **direct fixed-channel route:** derive the channel-`00000` distributional/contact decomposition of the ten Toller factors through the exact K5 intertwiner contraction and test the Hörmander wavefront condition on that contracted object; or
- **representation-transfer route:** prove an exact source-authoritative transform showing that the dangerous coherent contact covectors survive the channel-`00000` contraction with a nonzero coefficient and that no contraction cancellation removes the relevant wavefront component.

It must include a positive nonzero-survival control and an adversarial cancellation control. The `(delta,-delta)` type cancellation mechanism must be explicitly excluded for the actual K5 contraction, not assumed away.

Only after that same-realization bridge is prospectively established may a repaired Eq. (4) existence classifier reuse an E2 Hörmander-obstruction predicate for channel `00000`.

A separately prospectively frozen auxiliary joint-regulator/equivalence construction may still be explored, but it must not consume the current historical BLOCKED label as a validated fixed-channel premise. Any auxiliary regulator remains a candidate extension until source equivalence and path/order independence are established.