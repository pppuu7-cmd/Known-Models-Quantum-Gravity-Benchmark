# Iter456 — reduced Toller Appendix-B / Rühl-phase qualification

Date: 2026-09-13

## Frozen gate
Prospectively preregistered before implementation in `recovery/ITER456_PREREG_REDUCED_TOLLER_APPENDIXB_2026-09-13.md` (prereg commit `9e7231eb5e9f08001de1e87d48be5acc740fb77b`). The gate tests only the source-published pure-boost Appendix-B formulas for `k=j=l=1`, `m=-1,0,+1`, under the stated Rühl phase convention.

## Authoritative provenance
- implementation commit: `b3d835f0e102e663398a50ff7f79d045cdf462bd`
- workflow/head: `697da0a1b0a277f9164e5d4486032b5f22ea82ce`
- run: `34741722163`
- jobs: L2 `103682422641`, L1 `103682422716`, L0 `103682422731`, L3 cross-check `103682422745`, aggregate `103682446066`
- raw artifacts: L3 `10313360553` (`sha256:1b0e815799713769759b2717e9379f0e856a9dc3a69e90d4dcaddfeea48ccb05`), L0 `10312546224` (`sha256:d37e9cd70792260d55294e9859150f1385cefdc62c13f8df65b61935043c315d`), L1 `10312424750` (`sha256:94906b1029b88bc1e23891154f1767d59a4a059824c37de6174618264bd707d4`), L2 `10312394841` (`sha256:16bee85b036177fc30d9d6e08824f14d58a0c3e46b766f7e7470e98f8c227238`)
- summary artifact: `10312439637`
- summary digest: `sha256:d701f3562a86e514430a4a3eafc12290238d791d126a22282cde9fbd6cbaa65b`

## Terminal scientific classification
`ITER456_REDUCED_TOLLER_APPENDIXB_RUHL_PHASE_QUALIFIED_SCOPED`

Frozen aggregate: 4/4 artifacts present, 4/4 valid, 4/4 pass.

### Numerical results
All six frozen predicates passed in each magnetic lane and in the all-m cross-check:
- additive source identity `t+ + t- = d`;
- independent algebraic reorganization agreement;
- simple-pole scaling/residue stability at the source pole set;
- near-pole branch-sum stability;
- wrong-phase negative control;
- wrong-pole-location negative control.

Worst additive residual across `m=-1,0,+1`: `8.5524392998424e-80`.
Worst independent-formula residual: `2.7034315057431e-79`.
Worst near-pole relative branch-sum residual: `2.4591383284364e-57`.
Wrong-phase negative-control hit fraction: `1.0` in every magnetic lane.
All applicable simple-pole residue-drift errors are below `4.0e-15` versus the frozen `5e-6` ceiling; all local divergence-slope errors are far below `5e-6`.

## Interpretation
This qualifies the explicit source-faithful reduced Toller pure-boost layer only for `k=j=l=1`, `m=-1,0,+1` and the published Rühl-phase/additive/pole structure. It materially narrows D7-S2 but does not close it.

## Scope guards
No Eq.(7) full magnetic/group reconstruction is proved here. No arbitrary-spin theorem. No noncompact group-integration convergence. No causal-vertex finiteness/divergence theorem. No D7-S2 closure. No terminal D7 classifier. No `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, or `NEW_REQUIRED`. Candidate Gravity remains inactive.
