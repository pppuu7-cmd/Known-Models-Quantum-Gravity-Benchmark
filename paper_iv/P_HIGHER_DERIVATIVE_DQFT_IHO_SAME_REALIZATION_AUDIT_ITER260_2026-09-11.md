# Higher-derivative DQFT/dual-IHO same-realization audit — Iter260

Date: 2026-09-11
Family: `PERTURBATIVE_HIGHER_DERIVATIVE`
Branch: `B6_DQFT_DUAL_IHO_SPACELIKE_PURELY_VIRTUAL_BRANCH`
RQIR Core: `v1.0 FROZEN`

## Question
Can the new B6 branch identified in Iter259 supply a comparator-ready same-realization package, or can it at least be reduced to a bounded set of missing external objects and parked?

## Primary authority
- K. Sravan Kumar & João Marto, arXiv:2603.07150v3, *Quantum (quadratic) gravity: replacing the massive tensor ghost with an inverted harmonic oscillator-like instability*.
- K. Sravan Kumar & João Marto, arXiv:2604.19707v3, *Unitary Quadratic Quantum Gravity in 4D*.
- DQFT framework context: Kumar & Marto, PTEP 2024 123E01 / arXiv:2307.10345; related DQFT curved-spacetime works.

## Gate decomposition

### 1. Fixed action / pole support — SCOPED PASS
The 2026 unitarity paper fixes the local quadratic action
`S = ∫√-g [M_p^2 R/2 + α R^2/2 + β W^2/2]`
and declares the branch `β>0`. In its signature convention the additional spin-2 pole is spacelike and represented as a dual-IHO sector rather than a timelike particle ghost.

Status:
`PASS_SCOPED_FIXED_ACTION_AND_SPACELIKE_DUAL_IHO_POLE_DOMAIN`.

### 2. Hilbert/asymptotic-state and spectral rule — SCOPED PASS AS AUTHOR CLAIM
The authority argues that the dual-IHO has no normalizable vacuum particle state, that the physical Källén-Lehmann spectral weight on the spacelike shell vanishes, and that the Green distribution is consequently principal-value with no physical delta-function spectral contribution.

Status:
`PASS_SCOPED_PRIMARY_AUTHORITY__DQFT_DUAL_IHO_NO_ASYMPTOTIC_PARTICLE_AND_ZERO_PHYSICAL_KL_WEIGHT`.

This records the theorem claimed/proved in the primary preprint; it is not independent replication.

### 3. Optical theorem / loop singularity structure — SCOPED PASS AS AUTHOR CLAIM
The 2026 unitarity paper gives a Cutkosky argument excluding the extra spin-2 from physical absorptive cuts and a Landau analysis arguing that the spacelike pole does not generate the timelike principal-value pinch/nonlocal-divergence pathology. The full four-derivative propagator retains 1/k^4 UV behavior and the authors argue that counterterms remain local.

Status:
`PASS_SCOPED_PRIMARY_AUTHORITY__OPTICAL_THEOREM_AND_LANDAU_LOOP_CONTROL_FOR_DECLARED_B6_BRANCH`.

### 4. Physical observable — PARTIAL PASS
arXiv:2603.07150v3 derives inflationary scalar/tensor perturbation formulas for the same quadratic-gravity framework, including a Weyl-squared correction to the tensor-to-scalar ratio relative to a Starobinsky baseline, and DQFT parity-asymmetric scalar/tensor/CMB spectra. This establishes that B6 is not purely formal: normalized phenomenological observables are written down.

However, the parity-asymmetry sector depends on the broader DQFT inflationary vacuum construction and is not by itself a unique diagnostic of the dual-IHO spin-2. The `r(β)` correction is the cleaner quadratic-gravity observable for same-action ancestry.

Status:
`PARTIAL_PASS__NORMALIZED_INFLATIONARY_OBSERVABLE_EXISTS__UNIQUE_DUAL_IHO_ATTRIBUTION_AND_FULL_COMMON_DOMAIN_LIKELIHOOD_CAPSULE_OPEN`.

### 5. Causality — PARTIAL FRAMEWORK CONTROL / REALIZATION-SPECIFIC OPEN
DQFT framework papers state standard spacelike commutativity/causal separation properties for their direct-sum field construction. But the checked B6 quadratic-gravity papers do not provide a realization-specific theorem establishing the exact causal/microcausal response of the interacting dual-IHO spin-2 sector with its principal-value Green distribution across the same domain used for the unitarity and cosmological claims.

KMQGB therefore does not transport generic DQFT causality into B6 as a terminal certificate.

Status:
`BLOCKED_MISSING_REQUIRED_OBJECT__B6_REALIZATION_SPECIFIC_CAUSALITY_OR_CONTROLLED_REPLACEMENT_CERTIFICATE`.

### 6. Comparator / uncertainty / remainder — OPEN
The Starobinsky limit supplies a natural scoped comparator, but the checked authority does not provide one KMQGB-complete object combining the B6 observable with identical-domain experimental covariance/nuisance treatment plus propagated quantum/loop/truncation/scheme/remainder uncertainties. The cited inflationary tables/formulas are useful prospective observables, not a full comparator/error capsule.

Status:
`BLOCKED_MISSING_REQUIRED_OBJECT__B6_COMMON_DOMAIN_COMPARATOR_COVARIANCE_AND_PROPAGATED_THEORY_ERROR_CAPSULE`.

### 7. Independent validation — OPEN
The central dual-IHO/KL/Cutkosky/Landau construction is a new 2026 preprint line by the same authors. A targeted search through 2026-09-11 did not identify an independent paper that reproduces the full B6 unitarity theorem for the same β>0 quadratic action and quantization. This is a bounded search statement, not proof that no such work exists.

Status:
`BLOCKED_PENDING_INDEPENDENT_SAME_REALIZATION_VALIDATION_OR_EQUIVALENT_REPRODUCIBLE_CERTIFICATE`.

## Branch disposition
B6 has genuine same-realization content and cannot be dismissed as a relabeling of fakeon/Lee-Wick/PT routes. It also cannot be promoted to terminal PASS.

Disposition:
`SCOPED_MULTI_LAYER_PASS__B6_FIXED_ACTION_SPECTRAL_UNITARITY_AND_INFLATIONARY_OBSERVABLE_PRESENT__CAUSALITY_ERROR_CAPSULE_AND_INDEPENDENT_VALIDATION_OPEN`.

Operational status:
`PARKED_PENDING_B6_CAUSALITY_ERROR_AND_INDEPENDENT_VALIDATION_OBJECTS`.

This is not scientific FAIL and not family PASS.

## Family consequence
`PERTURBATIVE_HIGHER_DERIVATIVE` remains `PARTIAL_SUBFAMILY_ONLY`. The presence of mutually distinct B1-B6 quantization branches continues to forbid a family-level verdict by citation counting or by one child branch.

## Polygon saturation
Because the new B6 branch is now explicitly scoped to finite missing objects rather than left as an unknown active branch, operational known-school polygon saturation increases from ~94% to ~95%.

This is operational saturation only. Strict coverage remains governed by the Tier-1 contract; D2=`NOT_CLOSED`, D4=`PARTIAL_GLOBAL_NOT_CLOSED`, D7=`NOT_CLOSED / NOT_YET_AUTHORIZED`. Candidate Gravity R3=24%. Heavy compute=`IDLE`.

## Next gate
Do not continue generic B6 searches. Move to the next finite family blocker, preferably `GFT_TENSOR_MODELS` independence/reduction against spinfoams or a branch-disposition audit of the remaining higher-derivative B1-B5 forks if a specific theorem can terminally reduce one branch.
