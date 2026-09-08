# Quartic-First Helicity and Spectral-Moment Rigidity

**Status:** frozen pre-ansatz methodology / no Candidate Gravity promotion.  
**Purpose:** turn the quartic-first search architecture into a constrained cross-helicity/cross-order object while preventing misuse of local positivity bounds for genuinely nonlocal amplitudes.

## 1. Scope and free-sector anchor

This protocol applies to exploratory metric-only seeds that preserve

- the Einstein-Hilbert quadratic action around Minkowski;
- the GR massless spin-2 pole/residue;
- the GR three-graviton vertex;
- the first possible new on-shell graviton structure at four-point/higher order.

The preferred quartic-first architecture is therefore a search restriction, not a new theory.

## 2. Dimension-eight four-graviton anchor in 4D GREFT

Use the standard parity-even quartic curvature basis

`L_GRAFT superset (C_4,1/8)(R_mnab R_mnab)^2 + (C_4,2/8)(R_mnab Rtilde_mnab)^2`

with the cubic Riemann coefficient frozen to `C_3=0` for the quartic-first branch.

At tree-level EFT order, the two useful helicity combinations are

`f_2 = C_4,1 - C_4,2`

from the all-minus four-graviton contact channel, and

`g_2 = C_4,1 + C_4,2`

from the contact part of the MHV `--++` channel after the Einstein pole piece is kept separate.

For the ordinary local/polynomially-bounded positivity class,

`g_2 + f_2 > 0`,

`g_2 - f_2 > 0`,

which is equivalent to

`C_4,1>0`, `C_4,2>0`.

Define the dimensionless helicity ratio

`rho_4 = f_2/g_2 = (C_4,1-C_4,2)/(C_4,1+C_4,2)`.

Within this scoped local positivity class,

`-1 < rho_4 < 1`.

**Guardrail:** `rho_4` is an IR consistency/anchor coordinate, not Candidate Gravity novelty. Generic gravitational EFT/C5 already spans this quartic Wilson sector.

## 3. Why a parent-fixed tensor ratio matters but is not enough

A low-parameter quartic-first parent should not fit `C_4,1` and `C_4,2` independently after seeing data. It should derive a fixed ratio or a low-dimensional relation among them from the parent kernel/tensor contraction.

Cross-helicity training/holdout can then use one helicity combination to fix a shared normalization while the other tests the parent-fixed ratio.

However a single fixed `rho_4` remains locally reproducible by an ordinary GREFT point. It becomes useful only when linked by the same parent to higher-order energy/angular/helicity data.

## 4. Higher-order MHV contact hierarchy

Parameterize the MHV contact amplitude schematically as

`M(--++)_contact = spinor_prefactor * sum_(k>=j>=0) a_(k,j) s^(k-j) t^j`.

Crossing relates subsets of the `a_(k,j)`. A rigid parent with only a few shared parameters must predict a correlated tower of ratios such as

`a_(2,1)/a_(2,0)`,

`a_(4,1)/a_(4,0)`, `a_(4,2)/a_(4,0)`, ...

rather than introduce one coefficient per derivative order.

Known perturbative UV completions populate restricted islands inside the broader positivity-allowed region. Therefore the whole coefficient vector, not one Wilson coefficient, is the correct low-energy rigidity anchor.

## 5. Positive spectral moments for the local/polynomial class

For parity-preserving graviton amplitudes, appropriate helicity-eigenchannel dispersion relations generate sequences of moments of positive-semidefinite spectral-density matrices.

In the notation used by the four-graviton EFT-island analysis, one example is

`mu_(k-1) = 2 f_(2k-4,0) - h_(2k,0)`.

The associated Hankel matrix

`H_ij = mu_(i+j-1)`

must be positive semidefinite in the scoped dispersive class. Hence all supported principal minors are nonnegative.

This gives cross-order consistency conditions stronger than checking coefficient signs one order at a time.

## 6. Spectral-rank guardrail

Low-rank or saturated Hankel structure is a **spectral-complexity diagnostic**, not a KG certificate.

A simple positive spectral measure with one or a few effective mass scales can generate low-rank/extremal moment sequences. Ordinary heavy-particle UV completions can therefore mimic such relations.

Do not interpret Hankel-rank reduction by itself as quantum-gravity novelty. It must survive full same-domain UV/comparator profiling and cross-regime analytic-structure tests.

## 7. Mandatory dispersion-class attribution

Before applying local positivity/moment constraints, declare the amplitude growth/analyticity class.

### D-local

Local or polynomially/Regge-bounded amplitudes for which the chosen subtracted dispersion relation and positive-moment construction are valid after the required graviton-pole/IR treatment.

### D-nonlocal

Exponentially bounded/nonlocal amplitudes for which standard local polynomial-bounded positivity formulas are not automatically valid.

Recent nonlocal-positivity work derives modified dispersion constraints for exponentially bounded amplitudes and demonstrates allowed EFT regions that differ from purely local UV completion regions.

Therefore

`DISPERSION_CLASS_ATTRIBUTION = MANDATORY`

before any positivity, Hankel, moment-rank or UV-island verdict.

Using D-local bounds on a D-nonlocal candidate without proof is a protocol error and must fail-closed as `BLOCKED`.

## 8. Quartic-first Candidate Gravity use

A serious future quartic-first seed should attempt to derive from one parent rule

1. the tensor/helicity ratio at dimension eight;
2. the higher-order `a_(k,j)` hierarchy;
3. the applicable dispersion/growth class;
4. the Lorentzian/CTP prescription;
5. the cross-regime amplitude beyond the finite EFT Taylor series.

The low-energy coefficient tower is an IR anchor and consistency check. Candidate novelty, if any, can only be assigned to a same-parent cross-regime relation that survives full C5 and same-domain nonlocal/UV comparators.

## 9. Prospective observable split

A useful future split is

- mandatory anchor: GR two- and three-point sectors;
- training: one IR helicity combination plus selected low-order coefficient ratios;
- holdout: another helicity channel and higher-order/cross-regime kinematic points;
- null controls: channels fixed to GR or zero by symmetry/parent structure.

Shared parent parameters may not be independently refit by helicity/order/configuration.

## 10. Promotion status

`ANSATZ_PROMOTED = false`.

This protocol constrains the search space. It does not select a kernel or establish a robust residual.
