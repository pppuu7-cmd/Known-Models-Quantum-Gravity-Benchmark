# KMQGB Sixteenth Wave — Prospective Minimal DeltaGamma Screening

**Frozen denominator:** 5 structural templates.  
**Historical waves 1–15:** terminal and immutable.  
**Purpose:** kill the cheapest/natural candidate locations for `DeltaGamma_KG` before parameter fitting or ansatz promotion.

This is **pre-ansatz screening**.  A terminal rejection means only that the frozen structural template is not a KG-specific residual under the current comparator registry.

## T16-01 — local analytic metric-only EFT deformation

Canonical seed:

`S = S_EH + (c3/Lambda^2) int sqrt(-g) Riemann^3 + ...`, with `Q << Lambda`.

Classification: `EXACT_COMPARATOR_IDENTITY` with the full applicable gravitational EFT/C5 parent.

Reason: a local generally covariant analytic higher-curvature deformation in the low-energy domain is precisely a Wilson-operator direction already belonging to C5.  It can be useful physics but cannot define `DeltaGamma_KG` relative to a full matched C5 comparator.

## T16-02 — zero-free entire nonlocal metric kernel

Canonical seed: the already-audited EOM-squared / entire-form-factor weakly nonlocal gravity class with no additional propagator pole in the frozen Minkowski sector.

Classification: `OPERATIONALLY_DEGENERATE` for the frozen on-shell tree observable.

Reason: for the known stable class, tree-level n-point amplitudes coincide with the underlying local theory by analytic field redefinition.  Beyond-tree/off-shell/global-causality sectors require separate objects, and arbitrary entire form-factor freedom lowers rigidity rather than supplying a unique KG residual.

## T16-03 — graviton state-only deformation

Canonical seed: ordinary quantized GR/C5 dynamics with a squeezed/nonthermal graviton state `rho_h != |0><0|`, no new parent dynamics.

Classification: `OPERATIONALLY_DEGENERATE` with the C5 state sector.

Reason: noise, transition rates, decoherence and higher state-dependent correlators may change strongly, but this is state freedom inside ordinary quantized gravity unless a new dynamical law fixes the state and survives the state-profile quotient.

## T16-04 — generic quadratic CTP noise/dissipation deformation

Canonical seed:

`DeltaGamma_2 = int T_a deltaD_R T_r + (i/2) int T_a deltaN T_a`,

with no independently specified beyond-C5 spin-2 parent dynamics.

Classification: `OPERATIONALLY_DEGENERATE`.

Reason: this is the generic Gaussian influence-functional/open-system structure.  Quantum fields, stochastic gravity, ordinary baths and the Gaussian C5 graviton sector already generate retarded/dissipative and noise kernels.  A KMS/FDR relation does not make the kernel gravity-specific.

## T16-05 — extra quantum scalar mediator tuned to a Newtonian sector

Canonical seed:

`S = S_GR + S_phi + sum_i g_i phi O_i`, with a massless quantized scalar and a frozen weak-source choice capable of reproducing a `1/r` interaction.

Classification: `OPERATIONALLY_DEGENERATE` with C4/extra-mediator and scalar/modified-gravity comparator directions; fails KG-specific gravity attribution in the frozen sector.

Reason: a quantum mediator can carry a commutator, entanglement/non-EB channel and a Newtonian-looking force without being the massless helicity-2 gravitational mediator.  Spin-2/tensor Ward and universal stress-energy attribution remain mandatory.

## Rollup

The five lowest-complexity structural escape routes are comparator-contained or insufficient as KG-specific novelty:

1. local analytic metric EFT -> C5;
2. entire nonlocal tree deformation -> field-redefinition/tree degeneracy plus rigidity/causality caveats;
3. state-only -> C5 state freedom;
4. generic quadratic influence kernel -> open-system/C2/C5 structure;
5. extra quantum mediator -> C4/modified-gravity attribution failure.

## Surviving design requirement

A prospective `DeltaGamma_KG` must therefore be more constrained than any of the above.  At minimum it should be

- not a local analytic EFT coefficient direction;
- not merely a state choice;
- not representable as a generic Gaussian bath kernel;
- not attributable to an extra non-gravitational mediator;
- not removable by analytic field redefinition in the claimed observable sector;
- finite-parameter / parent-dynamics-fixed rather than an arbitrary nonlocal form factor;
- spin-2/Ward/locality/relationally complete;
- cross-order/cross-configuration predictive with the same shared parameters;
- capable of yielding a comparator-orthogonal joint residual after full-C5 matching.

The next useful object is **not yet an ansatz**.  It is a constrained specification for a non-EFT, state-independent, gravity-attributed linked hierarchy that can be red-teamed before promotion.
