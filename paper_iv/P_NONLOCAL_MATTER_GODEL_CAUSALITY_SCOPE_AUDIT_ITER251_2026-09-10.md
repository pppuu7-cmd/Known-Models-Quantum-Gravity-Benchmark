# Nonlocal QG matter-coupled Gödel/causality scope audit — Iter251

**Date:** 2026-09-10  
**RQIR Core:** v1.0 FROZEN  
**Family:** `NONLOCAL_QG`

## Question
Does the matter-coupled literature actually close the Iter250 Gödel-degeneracy obstruction for one fixed weakly-nonlocal realization, or only provide a narrower chronology test?

## Primary authorities
1. Z. Zhao & L. Modesto, *Quantum avoidance of Gödel’s closed timelike curves*, Eur. Phys. J. C 83, 517 (2023), arXiv:2304.10318. The analysis studies homogeneous Gödel-type metrics that already solve Einstein equations. For a large class of local/nonlocal higher-derivative theories **minimally coupled** to matter, the CTC-containing Einstein-sourced Gödel metrics are not exact solutions when the gravitational theory is (super-)renormalizable, while non-CTC metrics survive. The authors explicitly limit the analysis to Einstein-EOM Gödel metrics and cannot exclude other Gödel-type solutions that solve the full higher-derivative/nonlocal equations but not Einstein’s equations. For a nonminimally matter-coupled class, all Gödel-type metrics are exact classical solutions by construction.
2. S. Giaccari & L. Modesto, *Causality in Nonlocal Gravity*, Phys. Rev. D 99, 104001 (2019), arXiv:1803.08748. This establishes absence of Shapiro time advance for a declared weakly-nonlocal high-energy weak-coupling/eikonal domain and gives a construction recipe for UV-complete matter-coupled theories. This is a kinematic/eikonal causality result, not a theorem excluding every globally acausal exact solution.
3. Z. Zhao, L. Modesto & C. Bambi, *Acausal exact vacuum solutions in nonlocal gravity*, Eur. Phys. J. C 86, 713 (2026), arXiv:2605.01413. A special but large form-factor subclass admits exact vacuum Gödel-type CTC solutions. The paper identifies matter as the physical ingredient expected to break the Minkowski/Gödel vacuum degeneracy, but does not supply a single fixed matter-coupled action with a global solution-space chronology-exclusion theorem plus comparator-ready observable/error ledger.

## Result 1 — minimal-matter homogeneous Einstein-Gödel scoped PASS
There is genuine positive chronology evidence for the 2023 **minimal-matter, Einstein-sourced homogeneous Gödel sector**: within the paper’s declared class, (super-)renormalizability excludes the CTC-containing Einstein-Gödel solutions while causal homogeneous Gödel-type solutions remain.

Scoped disposition:
`PASS_SCOPED_CAUSALITY_GATE__MINIMAL_MATTER_SUPERRENORMALIZABLE_NONLOCAL_GRAVITY_EXCLUDES_EINSTEIN_SOURCED_HOMOGENEOUS_GODEL_CTC_SOLUTIONS_IN_DECLARED_SECTOR`.

This PASS is not a family-level causal certificate because the authority explicitly does not cover non-Einstein Gödel solutions of the full nonlocal equations.

## Result 2 — nonminimal matter is not a universal cure
In the 2023 nonminimal matter-coupled class, all Gödel-type spacetimes are exact classical solutions by construction, including CTC cases. The paper speculates that quantum corrections may spoil exactness, but does not prove the needed chronology exclusion.

Scoped disposition:
`FAIL_SCOPED_CLASSICAL_CAUSALITY_GATE__NONMINIMAL_MATTER_COUPLED_NONLOCAL_CLASS_RETAINS_GODEL_CTC_EXACT_SOLUTIONS_BY_CONSTRUCTION`.

No transfer from this child to all nonminimal couplings or to the family is licensed beyond the authority’s declared class.

## Result 3 — Shapiro causality and global chronology are distinct comparators
The 2018/2019 Shapiro-time-delay result probes weakly-coupled high-energy scattering/eikonal causal response. It is a useful scoped PASS but cannot overwrite the 2026 exact-vacuum Gödel obstruction. Therefore KMQGB must keep at least two distinct causal objects:

- `eikonal/Shapiro causal response`;
- `global exact-solution chronology / CTC exclusion`.

A PASS on the first cannot certify the second without an explicit equivalence theorem for the same realization and domain.

## Result 4 — Iter250 matter suggestion does not yet close the same-realization chain
The combined 2023+2026 authorities sharpen the missing object. Matter can change the Gödel disposition, but the sign and scope depend on the coupling and on which solution class is tested. No checked authority supplies one fixed Riemann/Weyl weakly-nonlocal action that simultaneously demonstrates:

`fixed action + fixed matter coupling -> no CTC/pathological exact-solution sector in declared domain -> perturbative unitarity/UV control -> nontrivial full-momentum physical observable -> common-domain GR/EFT comparator -> propagated theory/remainder error`.

Disposition:
`BLOCKED_MISSING_REQUIRED_OBJECT__NONLOCAL_RIEMANN_WEYL_FIXED_MATTER_COUPLED_ACTION_GLOBAL_CHRONOLOGY_EXCLUSION_PLUS_UNITARITY_FULL_MOMENTUM_OBSERVABLE_COMPARATOR_AND_PROPAGATED_ERROR`.

## Family consequence
`NONLOCAL_QG` remains `PARTIAL_SUBFAMILY_ONLY`; family residual remains `UNDEFINED`. Neither the minimal-matter scoped PASS nor the nonminimal scoped FAIL is promoted to family level. D2 remains `NOT_CLOSED`; D4 remains `PARTIAL / globally NOT_CLOSED`; D7 remains `NOT_CLOSED`, decision `NOT_YET_AUTHORIZED`. Candidate Gravity remains inactive at R3=24%.

## Heavy compute
`IDLE`. The blocker is solution-space scope/provenance/matching, not numerical resolution.

## Exact next gate
`NONLOCAL_QG_FIXED_ACTION_GLOBAL_CAUSAL_SOLUTION_SPACE_OR_CHRONOLOGY_PROTECTION_PLUS_FULL_MOMENTUM_OBSERVABLE_CERTIFICATE`.
