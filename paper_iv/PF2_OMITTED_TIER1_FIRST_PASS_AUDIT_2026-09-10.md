# PF2 omitted Tier-1 first-pass audit

**Date:** 2026-09-10  
**Iteration:** 186  
**RQIR authority:** Core v1.0 FROZEN  
**Purpose:** remove `NOT_YET_BENCHMARKED` only where a concrete published physical/theoretical control can be frozen, while preserving family-level nonclosure.

## Executive result

All five Tier-1 families that were still `NOT_YET_BENCHMARKED` at Iter185 now have at least one concrete literature-backed scoped control. None has a sufficient family-level same-realization comparator object. Therefore all five move to `PARTIAL_SUBFAMILY_ONLY`, not PASS/FAIL at family level.

This is a coverage advance, not evidence for `NEW_REQUIRED`.

---

## PF2-02 — CDT/EDT

### Frozen scoped controls

Primary authorities:

- J. Ambjørn, R. Loll, **Causal Dynamical Triangulations: New Lattice Theory of Quantum Gravity**, arXiv:2604.05641 (2026).
- J. Gizbert-Studnicki, **Semiclassical and Continuum Limits of Four-Dimensional CDT**, arXiv:2301.06068 (2023).

Accepted scoped facts:

1. The four-dimensional de Sitter phase exhibits an emergent semiclassical universe whose scale-factor behaviour is compatible with the classical Einstein solution.
2. Scale-factor fluctuations are described accurately by a minisuperspace effective action in the studied regime.
3. The short-distance spectral dimension approaches a value near two in the established numerical programme.
4. Current simulations indicate a possible UV fixed point / continuum route, but the 2026 review explicitly describes the construction of physical observables connecting the nonperturbative theory to early-universe phenomenology as ongoing.

### RQIR classification

`PARTIAL_SUBFAMILY_ONLY__SEMICLASSICAL_AND_SPECTRAL_CONTROLS`

Not family-terminal because a fixed four-dimensional continuum-limit trajectory, lattice-spacing map, invariant physical observable and full finite-size/discretization/comparator error package are not jointly frozen.

Exact blocker:

`CDT_4D_CONTINUUM_TRAJECTORY_PLUS_INVARIANT_OBSERVABLE_COMPARATOR_CERTIFICATE`.

---

## PF2-03 — Hořava-Lifshitz gravity

### Frozen scoped controls

Primary authorities:

- A. O. Barvinsky et al., **Renormalization of Horava Gravity**, arXiv:1512.02250.
- A. O. Barvinsky, A. V. Kurov, S. M. Sibiryakov, **Renormalization group flow of projectable Hořava gravity in (3+1) dimensions**, arXiv:2411.13574.
- M. Herrero-Valea, **The Status of Horava Gravity**, arXiv:2307.13039.

Accepted scoped facts:

1. Perturbative renormalizability is proven for the projectable theory.
2. The 3+1-dimensional projectable marginal-coupling RG system has a mapped fixed-point/trajectory structure; one asymptotically free fixed point yields trajectories spanning the unitarity-compatible kinetic-coupling range, including a near-GR region `0 < lambda-1 << 1`.
3. The projectable and non-projectable theories are materially distinct. The review records unresolved obstacles to extending the same renormalization authority to the non-projectable model and substantial low-energy/extra-mode phenomenology.

### RQIR classification

`PARTIAL_SUBFAMILY_ONLY__PROJECTABLE_RENORMALIZATION_RG_CONTROL`

The projectable UV/RG result is a real scoped pass, not a family sufficiency result. A single same-realization object connecting a UV trajectory to an IR GR limit, extra scalar-mode consistency and a normalized physical observable with identical-domain comparators is still missing.

Exact blocker:

`HORAVA_PROJECTABLE_UV_TO_IR_EXTRA_MODE_OBSERVABLE_CERTIFICATE_PLUS_NONPROJECTABLE_DISPOSITION`.

---

## PF2-04 — Causal sets

### Frozen scoped controls

Primary authorities:

- L. Machet, J. Wang, **On the continuum limit of Benincasa-Dowker-Glaser causal set action**, arXiv:2007.13192.
- S. Carlip, **Causal sets and an emerging continuum**, Gen. Rel. Grav. 56, 95 (2024).
- S. A. Adamson, P. Wallden, **Benincasa-Dowker causal set actions by quantum counting**, arXiv:2505.22217.

Accepted scoped facts:

1. For Poisson-sprinkled causal sets on a small causally convex diamond, the BDG action has a finite continuum limit containing the Einstein-Hilbert bulk term plus the expected codimension-two joint contribution.
2. The causal-set path-sum programme has strong suppression results for broad classes of entropically dominant non-manifoldlike layered orders.
3. The 2024 continuum review explicitly states that these results still do not establish full emergence of a continuum: the remaining unsuppressed causal sets are not sufficiently understood, manifoldlikeness is not algorithmically characterized in general, and the BDG action is not yet derived from first principles of a fundamental causal-set dynamics.

### RQIR classification

`PARTIAL_SUBFAMILY_ONLY__BDG_CONTINUUM_EH_IDENTITY_CONTROL`

The continuum-EH result is a scoped comparator identity, not proof of a complete quantum dynamics or a unique beyond-GR residual.

Exact blocker:

`CAUSAL_SET_FUNDAMENTAL_DYNAMICS_TO_MANIFOLD_CONTINUUM_PLUS_NORMALIZED_OBSERVABLE_CERTIFICATE`.

---

## PF2-05 — Perturbative / higher-derivative quantum gravity

### Frozen scoped controls

Primary authorities:

- M. Piva, **Higher-Derivative Quantum Gravity with Purely Virtual Particles: Renormalizability and Unitarity**, arXiv:2305.12549.
- D. Anselmi, E. Bianchi, M. Piva, **Predictions of quantum gravity in inflationary cosmology: effects of the Weyl-squared term**, arXiv:2005.10293.
- D. Anselmi, M. Piva, **Quantum Gravity, Fakeons And Microcausality**, arXiv:1806.03605.

Accepted scoped facts:

1. A higher-derivative gravity realization with the purely-virtual/fakeon prescription has a concrete renormalizable/unitary construction under its stated quantization prescription.
2. The `R + R^2 + Weyl^2` inflationary realization yields explicit scalar/tensor spectra and a constrained tensor-to-scalar ratio; it is therefore more than a formal action with no observables.
3. The same framework predicts microscopic causality violation above the fakeon scale. This is a declared physical feature and prevents us from silently substituting ordinary microcausality for the fakeon prescription.
4. Stelle-ghost, Lee-Wick/fakeon and other higher-derivative prescriptions are materially distinct; one realization cannot decide the whole family.

### RQIR classification

`PARTIAL_SUBFAMILY_ONLY__FAKEON_RENORMALIZABLE_UNITARY_OBSERVABLE_CONTROL`

Exact blocker:

`HIGHER_DERIVATIVE_POLE_PRESCRIPTION_FAMILY_MAP_PLUS_SAME_REALIZATION_CAUSALITY_OBSERVABLE_COMPARATOR_CERTIFICATE`.

---

## PF2-06 — Group Field Theory / tensor models

### Frozen scoped controls

Primary authorities:

- F. Gerhardt, D. Oriti, E. Wilson-Ewing, **The separate universe framework in group field theory condensate cosmology**, arXiv:1805.03099.
- D. Oriti, Y.-L. Wang, **Effective anisotropic dynamics in Group Field Theory cosmology**, arXiv:2311.14377.
- R. Dekhil, F. Greco, S. Liberati, D. Oriti, **Emergent scalar field dynamics in a cosmological spacetime from GFT quantum gravity**, arXiv:2608.12003.

Accepted scoped facts:

1. In relational GFT condensate constructions, effective homogeneous/perturbed cosmological equations recover the GR/Friedmann regime at late or low curvature and contain quantum-gravity corrections near the bounce/Planck-curvature regime.
2. A 2026 relational derivation obtains an effective scalar-field dynamics on emergent FLRW geometry and a perturbative modified dispersion relation with dispersive/dissipative microscopic corrections.
3. These are concrete theory-to-effective-observable maps, but they are condensate-state/cosmology scoped.
4. GFT has close spin-foam relations but cannot be silently merged with the LQG/spinfoam row: an explicit reduction/equivalence map for the chosen dynamics/state/observable is required.

### RQIR classification

`PARTIAL_SUBFAMILY_ONLY__RELATIONAL_CONDENSATE_COSMOLOGY_CONTROL`

Exact blocker:

`GFT_SPINFOAM_INDEPENDENCE_OR_REDUCTION_PLUS_FULL_GRAVITY_OBSERVABLE_COMPARATOR_CERTIFICATE`.

---

## Global consequence

After this first-pass campaign, **zero Tier-1 families remain merely `NOT_YET_BENCHMARKED`**. This does not close D2A or D2B because the new five rows remain nonterminal. It does mean that every Tier-1 family is now touched by a concrete audit rather than an empty placeholder.

The next bottleneck is no longer discovery of untouched Tier-1 schools. It is conversion of partial/BLOCKED family rows into terminal coverage/object dispositions, plus resolution of the Tier-2 classification watchlist.

No family-level exclusion is inferred here, and Candidate Gravity remains inactive.
