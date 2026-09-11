# Recovery Delta 280 — Asymptotic Safety Lorentzian spectral-function reopen

Date: 2026-09-11

## New primary authority

Pawlowski, Reichert, Wessely, *Self-consistent graviton spectral function in Lorentzian quantum gravity*, Physics Letters B 880 (2026) 140844, DOI `10.1016/j.physletb.2026.140844`.

The paper supplies a peer-reviewed self-consistent Lorentzian graviton spectral function with positive, normalisable spectral weight in its on-shell TT fluctuation-graviton setup.

## Parallel compute

Workflow `asymptotic-safety-spectral-unitarity-audit`, run `34553743544`:
- RG fixed-point/trajectory consistency;
- UV-tail normalisability;
- reported-z spectral-weight decomposition;
- IR coefficient relation;
- 4/4 independent jobs success; aggregate success.

Aggregate digest: `sha256:a822813cd95a0a5987b79920fbcbed1f5cf3b5798ef2170f2f71c6b226a6a7f4`.

Methodology CI run `34553743421`: preflight + 4/4 methodology shards + aggregate/bundle success.

## Scoped result

`PASS_SCOPED_POSITIVE_NORMALISABLE_LORENTZIAN_TT_GRAVITON_SPECTRAL_FUNCTION_WITH_UNIT_WEIGHT__NOT_PHYSICAL_HILBERT_SPACE_NOT_CONTACT_COMPLETE_NOT_FULL_CURVE_INDEPENDENTLY_REPRODUCED`

Important boundaries:
- the source explicitly says the fluctuation-graviton states are not diffeomorphism invariant and do not belong to the physical Hilbert space;
- publisher data availability is on request; no public article-specific spectral dataset/reference implementation was located;
- full numerical spectral curve therefore remains independently unreproduced in Iter280;
- the contact-complete `s+t+u+A4` scattering certificate remains the active terminalization blocker.

## Global state

- Tier-1 = 15.
- strict terminal = 1/15.
- candidate-family terminal = 0/14.
- Asymptotic Safety remains `BLOCKED_MISSING_REQUIRED_OBJECT`.
- D7 remains NOT_CLOSED / NOT_YET_AUTHORIZED.
- Candidate Gravity remains inactive at R3 = 24%.

## Publication handoff

- Paper III: `NOT_NEEDED` as a new rule; optional corroboration of Iter277 only.
- Paper IV: `READY`; add the peer-reviewed Lorentzian spectral positive result, numerical cross-checks and explicit physical-Hilbert/reproducibility limits.

Detailed audit:
`paper_iv/P_ASYMPTOTIC_SAFETY_LORENTZIAN_SPECTRAL_AUDIT_ITER280_2026-09-11.md`

Decision delta:
`paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_280.json`
