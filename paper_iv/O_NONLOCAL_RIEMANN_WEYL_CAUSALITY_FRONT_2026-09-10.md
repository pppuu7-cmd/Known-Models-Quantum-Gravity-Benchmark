# O-NONLOCAL — Riemann/Weyl Scattering and Causality Front

**Date:** 2026-09-10  
**Iteration:** 184  
**RQIR Core:** v1.0 FROZEN

## Why this front exists

PF2-01A closes a large Ricci/EOM-squared weakly-nonlocal subclass at tree-level as an exact GR S-matrix comparator identity. That theorem explicitly does not cover an independent nonlocal Riemann/Weyl-sector deformation. The next discriminating object must therefore live in that independent sector.

## Published boundary evidence

### Tree amplitudes

Donà et al., JHEP 08 (2015) 038, arXiv:1506.04589, explicitly find that adding an independent operator quadratic in the Riemann tensor changes the four-graviton result (except the four-dimensional local Gauss-Bonnet special case): amplitudes can depend on the form factors. Thus the Riemann/Weyl branch is materially independent in the scattering observable and cannot be collapsed into PF2-01A by the field-redefinition theorem.

### Eikonal causality

Giaccari & Modesto, arXiv:1803.08748, analyse a definite Weyl-basis nonlocal gravity. Their eikonal/Shapiro-delay calculation distinguishes form-factor choices:

- for `H_2 = H_0 = H_K` (and for the illustrative `H_2 = H_0 = sigma Box` choice), the Weyl-basis theory develops a causality-violating time advance;
- for the `H_T` entire-function choice considered there, the same dangerous time advance is absent in the stated weak-coupling/eikonal regime.

Therefore `unitary/finite nonlocal gravity` is not a single causality verdict. Form-factor realization is part of the physical object.

### 2026 nonperturbative/classical boundary

Zhao, Modesto & Bambi, *Acausal exact vacuum solutions in nonlocal gravity*, EPJC 86, 713 (2026), arXiv:2605.01413, exhibit a particular but large form-factor subclass admitting exact vacuum Gödel-type solutions with closed timelike curves. They conclude that renormalizability alone is not sufficient to exclude causality violation in vacuum. This is an independent warning against upgrading perturbative UV consistency into a universal causality PASS.

## RQIR implications

1. PF2-01A exact GR tree-S-matrix identity remains valid in its scoped Ricci/EOM-squared class.
2. The Riemann/Weyl branch is physically independent for scattering and must be separately benchmarked.
3. A form-factor-specific Shapiro time advance is eligible as a **scoped consistency/causality negative result**, but only after the exact realization and applicable RQIR causality obligation are frozen.
4. The causal `H_T` branch prevents a family-wide causality FAIL from being inferred from the `H_K` branch.
5. The 2026 Gödel result is a second, non-eikonal causality warning but likewise applies only to its stated form-factor class.

## Exact PF2-01B split

Rather than force mutually different form factors into one row, PF2-01B should be split prospectively:

- `PF2_01B1_WEYL_HK_EIKONAL_CAUSALITY` — freeze the Weyl-basis `H_K` realization and test the sign of the Shapiro delay/time advance against the exact comparator and RQIR causality obligation.
- `PF2_01B2_WEYL_HT_EIKONAL_CAUSALITY` — freeze the `H_T` realization as the matched negative control; verify absence of time advance within the same stated regime.
- `PF2_01B3_RIEMANN_WEYL_AMPLITUDE_RESIDUAL` — obtain a normalized form-factor-dependent scattering residual beyond the Ricci field-redefinition class and quotient it against the allowed local higher-curvature EFT space.
- `PF2_01B4_GODEL_VACUUM_CAUSALITY` — decide whether the exact Gödel/CTC realization falls inside the Paper-IV causality domain and, if so, freeze its state/form-factor assumptions as a separate scoped result.

## Fail-closed rule

No family-level status beyond `PARTIAL_SUBFAMILY_ONLY` is permitted until these materially distinct branches are either benchmarked, explicitly reduced/equated, or excluded from Paper-IV scope by a written proof.

## Heavy compute

Not yet justified. The next work is exact realization extraction, observable/comparator normalization and RQIR-domain matching. Numerical eikonal reproduction may be useful later as a reproducibility check, but it cannot substitute for the missing family/subfamily attribution.
