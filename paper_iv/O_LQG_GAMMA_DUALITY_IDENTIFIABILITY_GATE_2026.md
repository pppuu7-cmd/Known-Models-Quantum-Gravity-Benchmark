# O-LQG γ-Duality Structural-Identifiability Gate — 2026-09-10

**KMQGB iteration:** 167  
**RQIR standard:** Core v1.0 FROZEN.

## Frozen relation

For the gamma-dual inflationary model,

`1/gamma - gamma = (pi/8) (r + 8 n_T) / Pi`.

Define

`q = (pi/8) (r + 8 n_T) / Pi`.

For `gamma>0`,

`q(gamma)=1/gamma-gamma`

has derivative

`dq/dgamma = -1/gamma^2 - 1 < 0`.

Therefore it is globally one-to-one on positive gamma and has the unique inverse

`gamma(q) = (sqrt(q^2+4)-q)/2`.

## Structural result

If `Pi != 0` and the combination `(r+8 n_T)/Pi` is measured, the model's positive `gamma` is structurally identifiable from this observable block.

This is stronger than a multi-parameter EFT fit because the same parameter is then available for independent cross-representation checks (parity-even/odd EFT ratio, area gap, spinfoam/entropy data).

## Required negative controls

### No parity signal

If `Pi=0`, this channel does not determine gamma. It must not be regularized by inserting a tiny arbitrary denominator or by fitting gamma from unrelated data and feeding it back into the same test.

### GR-consistency branch

When `Pi=0` and `r=-8 n_T`, the usual parity-even consistency branch carries no gamma information through this relation. This is a genuine null, not a failed detection.

### Near-null conditioning

For very small `|Pi|`, experimental inference can be ill-conditioned even though algebraic identifiability exists away from zero. A future detector/cosmology likelihood must propagate covariance and inflationary nuisance parameters rather than rely on the ratio alone.

## Executable reference

`code/lqg_gamma_duality_identifiability_reference.py`

checks

- inversion over representative positive gamma values;
- strict monotonicity / uniqueness;
- a synthetic observable triple;
- the `Pi=0` negative control.

## What this does not prove

This gate does **not** close the microscopic attribution gap. The source paper explicitly states that the top-down derivation of the effective action from non-perturbative spinfoam dynamics is missing.

Thus the scientific state is

`OBSERVABLE_RELATION_IDENTIFIABLE__MICRO_TO_EFT_BRIDGE_BLOCKED`.

CW2-02 remains open.
