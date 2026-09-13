# Iter459 -> Iter462 parallel research front — 2026-09-13

This recovery note records the consumed auto-research results and the new parallel front. Repository/source artifacts remain authoritative; D7 stays fail-closed.

## Consumed auto-research

### Iter456 — PASS (scoped)
`ITER456_REDUCED_TOLLER_APPENDIXB_RUHL_PHASE_QUALIFIED_SCOPED`; 4/4 lanes. Reduced Toller Appendix-B/Ruehl-phase reconstruction passed frozen identity, residue, phase and negative controls. No arbitrary-spin or convergence theorem.

### Iter457 — PASS (scoped)
`ITER457_TOLLER_EQ7_FULL_MAGNETIC_RECONSTRUCTION_QUALIFIED_SCOPED`; 4/4 lanes. Full magnetic Eq.(7) reconstruction passed at k=j=l=1, including route, unitarity, additive, covariance and negative controls. Still scoped.

### Iter458 — scientific FAIL of ordinary truncation
`SCIENTIFIC_FAIL_ITER458_TOLLER_FEYNMAN_IEPSILON_ORDINARY_TRUNCATION`; 0/4 scientific PASS despite structurally valid finite calculations. This rejects the frozen ordinary symmetric-real-line truncation realization only; it is not a physical causal-vertex divergence result.

### Iter459 — PASS (scoped)
Run `34746472976`; artifact `10313863332`, digest `sha256:f54e6e4ee1b787f17b7bab924409611297ce06ac73a005e308be3d1613a9aa8d`. `ITER459_TOLLER_PLEMELJ_DISTRIBUTIONAL_KERNEL_QUALIFIED_SCOPED`; 6/6 Schwartz lanes. This qualifies the universal Sokhotski-Plemelj denominator boundary value, not the non-Schwartz source-specific `P11*d_source` object.

## New parallel front

### Iter460 — source P11*d spectral tail — PASS (scoped)
Branch `research/iter460-source-spectral-tail`; run `34748501676`; artifact `10314837771`, digest `sha256:ce4f1a8a18c6c8282dad4a7f424f322e0e5133c926dfb327ce0c68f7f34163d0`.
Classification `ITER460_SOURCE_P11_D_TAIL_CHARACTERIZED_SCOPED`; 24/24 records PASS.

Frozen envelope result: `P11*d_source` has a growing oscillatory/polynomial envelope on the tested tail rather than Schwartz/L1 behavior. Four-window fitted slopes are about `+0.84` for m=0 and `+1.67` for m=+/-1 on the frozen radii. Therefore Iter459 cannot be promoted mechanically from Schwartz tests to the source object. This is not a physical divergence theorem.

### Iter461 — exact K5 collision partitions — launched
Branch `research/iter461-k5-collision-partitions`; run `34748503239`. Preregistered exact Bell(5) enumeration and naive local pair-power thresholds. Run is queued at recovery-note time; do not duplicate it.

### Iter462 — S3/S4 evidence localization — PASS (scoped)
Branch `research/iter462-d7-s3-s4-evidence-audit`; run `34748508906`; artifact `10315340931`, digest `sha256:97cc6c2e18df2467b2f4130b8cf2866b021c212d81fb9d9878a0448455adbc3a`.
Classification `ITER462_D7_S3_S4_EVIDENCE_LOCALIZATION_COMPLETE_SCOPED`; 1478 tracked text files scanned.

Six of seven unresolved S3/S4 gate names have no formal candidate artifact in the tracked snapshot. The sole candidate for `normalized_comparator_error_certificate`, `code/lqg_entropy_observable_common.py`, is explicitly negative: `same_realization_normalized_comparator_error_certificate=False`, `same_realization_transport_ready=False`, `missing_parameter_transport=True`, and `missing_normalized_observable_transport=True`. Thus no positive S3/S4 closure artifact was found by this audit. Do not invent a transport map.

## Locked status
- D7-S2: open; collision/source-distributional problem narrowed but not closed.
- D7-S3: NOT_CLOSED.
- D7-S4: PARTIAL_GLOBAL_NOT_CLOSED.
- D7-S5: NOT_AUTHORIZED.
- Candidate Gravity: false/inactive.
- Working progress metric remains D2~82%, D4~68%, D7~56%, overall~67% until a formal gate closes.
