# Terminal result — source j=1 K5 channel-00000 contact realization transfer

Date: 2026-09-15
Gate: `SOURCE_J1_K5_CHANNEL00000_CONTACT_REALIZATION_TRANSFER_GATE`
Terminal classification: `SOURCE_J1_K5_CHANNEL00000_CONTACT_REALIZATION_TRANSFER_BLOCKED_SCOPED`

## Frozen authority

The scientific contract was prospectively frozen before implementation/classification in:

- preregistration `research/SOURCE_J1_K5_CHANNEL00000_CONTACT_REALIZATION_TRANSFER_PREREG_2026-09-15.md`;
- prereg commit `d14cdd7594d23ce55fbab9504a5a003aa7c3d925`;
- frozen authority ledger `inputs/source_j1_k5_channel00000_contact_transfer_authority_2026-09-15.json`, commit `271733aaf19f8982ab2c8b46f56657b9b50d7b48`;
- certificate `code/source_j1_k5_channel00000_contact_realization_transfer_certificate.py`, commit `4160e498bc548452db6afadbacb0ef01cd4c68d0`.

No PASS/FAIL/BLOCKED/INVALID criterion was changed after seeing a substantive result.

## Actions provenance

The first workflow launch was production head `1a1957de67d806e8d12b9256517b9b8e39912932`, run `34946262055`. Its source-lock job succeeded, but the exact-certificate job failed after the certificate process started because the workflow attempted to `tee` into a missing `artifacts/` directory. No durable artifact was produced, so run 1 is retained as **infrastructure-only failure and not a scientific verdict**.

The workflow-only repair commit `278315b8332e71c89a06e35645190fc3d62aa099` added `mkdir -p artifacts`; it changed no frozen scientific criterion, authority ledger, or certificate code.

The authoritative repaired run is:

- run `34946470045`, head `278315b8332e71c89a06e35645190fc3d62aa099`, terminal `completed/success`;
- source-lock job `104306951367`, `success`;
- exact-certificate job `104307018863`, `success`;
- artifact `10387222229`, `4188` bytes;
- artifact ZIP digest `sha256:21f65599e304cf4131981089163c90151d30d1c0229240e926f057a48f9f1459`;
- canonical JSON SHA256 `454653ec9664cef94f0cae5846ac213cbc2a9fef1e63c93d617878d73c6bfd7c`;
- raw log SHA256 `454653ec9664cef94f0cae5846ac213cbc2a9fef1e63c93d617878d73c6bfd7c`.

CI success is provenance only; the scientific classification is the frozen classifier output below.

## Work performed

The certificate source-locked every frozen authority record by Git blob SHA and required semantic marker. All source locks passed.

It then recomputed the independent fixed-channel cubic-pole contraction as an exact positive control:

`C_00000 = 11/24 != 0`.

This control is explicitly marked `physical_contact_evidence=false`: it tests that the exact contraction machinery can preserve a nonzero source-pinned magnetic tensor, and is **not** promoted to the coherent contact tensor.

The exact cancellation control `C + (-C)` returned coefficient `0`.

The same generic classifier reached all four preregistered branches on synthetic fixtures:

- source-pinned nonzero coefficient -> `SOURCE_J1_K5_CHANNEL00000_COHERENT_CONTACT_SURVIVES_EXACT_CONTRACTION_SCOPED`;
- source-pinned exact zero -> `SOURCE_J1_K5_CHANNEL00000_COHERENT_CONTACT_CANCELS_EXACTLY_SCOPED`;
- missing contact-transfer map -> `SOURCE_J1_K5_CHANNEL00000_CONTACT_REALIZATION_TRANSFER_BLOCKED_SCOPED`;
- convention mismatch -> `SOURCE_J1_K5_CHANNEL00000_CONTACT_REALIZATION_TRANSFER_INVALID`.

Thus PASS, FAIL, BLOCKED and INVALID are mechanically reachable and the actual classification is outcome-sensitive rather than hard-coded.

## Result

For the actual frozen source/repository authority:

- coherent contact evidence is source-pinned and nonzero for real nonzero rho in the coherent-spinor realization;
- the independent cubic-pole magnetic/intertwiner channel-`00000` contraction is exactly nonzero (`11/24`) in its own realization;
- `actual_contact_map_source_pinned = false`;
- `actual_contact_channel00000_exact_coefficient = null`.

The frozen repository authority therefore does **not** pin an exact coherent-contact -> magnetic/intertwiner operator/tensor map in matching `j=1`, rho, basis, edge-orientation and normalization conventions. Consequently the physical channel-`00000` contact coefficient cannot be executed from the frozen source chain.

Terminal classification:

`SOURCE_J1_K5_CHANNEL00000_CONTACT_REALIZATION_TRANSFER_BLOCKED_SCOPED`

## New fact

The same-realization gap identified by the Critic is now localized sharply: nonzero coherent contact evidence and an independently nonzero fixed-channel cubic-pole contraction are both present, but they do not constitute a representation-transfer theorem. The dangerous coherent contact component is therefore neither certified to survive nor certified to cancel in channel `00000`.

In particular, the missing transfer is **not a zero residual**, and the exact `11/24` cubic-pole coefficient is **not** the contact coefficient.

## Claim ceiling

This is a source/realization **BLOCKED** result, not a scientific/model FAIL.

It does not establish:

- existence or nonexistence of the joint Eq. (4) distribution;
- survival or cancellation of the coherent contact component after the actual fixed-channel contraction;
- uniqueness/nonuniqueness of a collision extension;
- a family-level exclusion;
- D7 closure or a terminal D7 selector;
- Candidate Gravity authority;
- `QUANTUM_GRAVITY_SOLVED`, `ALL_KNOWN_MODELS_FAIL`, `NEW_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.

The historical coherent-contact Hörmander result remains valid in its coherent realization, and the fixed-channel full-collision absolute-Haar result remains valid in its magnetic/intertwiner scope. This gate only prevents an unauthorized transfer between them.

## Durable files

- prereg: `research/SOURCE_J1_K5_CHANNEL00000_CONTACT_REALIZATION_TRANSFER_PREREG_2026-09-15.md`;
- authority ledger: `inputs/source_j1_k5_channel00000_contact_transfer_authority_2026-09-15.json`;
- certificate: `code/source_j1_k5_channel00000_contact_realization_transfer_certificate.py`;
- workflow: `.github/workflows/source-j1-k5-channel00000-contact-realization-transfer.yml`;
- canonical result: `results/source_j1_k5_channel00000_contact_realization_transfer_2026-09-15.json`, persistence commit `a57f239280c627a41c0ec4d374730ff2636bc7a0`;
- raw log: `results/source_j1_k5_channel00000_contact_realization_transfer_2026-09-15.log`, persistence commit `3b24a731057cd48b4cf41ee22ef52f941d2c1e8b`;
- hashes: `results/source_j1_k5_channel00000_contact_realization_transfer_2026-09-15.sha256`, persistence commit `0a8f13a3d90b55e3f6af83a90ddef7ca3bc20726`.

## Next admissible gate

Recommended next gate:

`SOURCE_J1_K5_CONTACT_REPRESENTATION_DERIVATION_GATE`

Prospectively derive, from source-defined representation identities only, the exact distribution-valued coherent-contact -> magnetic operator map with rho, spherical-basis phases, normalization and edge orientation locked; then execute the exact K5 channel-`00000` contraction. If the derivation requires model data not fixed by the source, the outcome must be a source-derivation BLOCKER rather than scientific FAIL.

Governance remains: `RQIR Core v1.0 = FROZEN`; `D7-S2 = NOT_CLOSED`; `D7-S3 = NOT_CLOSED`; `D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`; terminal selectors remain forbidden; Candidate Gravity remains inactive.
