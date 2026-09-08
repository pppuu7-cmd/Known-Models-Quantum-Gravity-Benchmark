# Minimal E1 Vertex-Seed Specification — Pre-Ansatz Only

**Status:** exploratory structural specification / `BLOCKED` parent kernel **and cubic causality gate** / no Candidate Gravity ansatz promoted.  
**Purpose:** identify the smallest same-spin-2 nonlocal search object that is not immediately killed by Wave 16 while preserving the exact GR free pole structure, then red-team it before model promotion.

## 1. Original cubic structural skeleton

Use a flat-background-compatible diffeomorphism-invariant parent of the schematic form

`S_skel = S_EH + (lambda/M^2) int sqrt(-g) V3[C, nabla; Phi_M]`,

where a representative cubic-curvature placement is

`V3 ~ C_mn^rs Phi_M(Box) ( C_rs^ab C_ab^mn )`.

This representative is **not the final parent action**. Exact covariant operator ordering, kernel definition, CTP completion and boundary prescription remain mandatory missing objects.

The kernel `Phi_M` must be derived/frozen by a parent rule. It may not be treated as an arbitrary function to be fitted after observing a residual.

## 2. Two-point anchor

Around Minkowski,

`C = O(h) + O(h^2) + ...`.

A regular cubic-curvature invariant begins at `O(h^3)`. Therefore, provided the parent contains no hidden inverse-curvature or singular background dependence,

- the `O(h^2)` action is exactly Einstein-Hilbert;
- the free massless spin-2 pole/residue are unchanged;
- no additional propagator pole is introduced by this cubic seed itself.

This is a structural gravity anchor, not KG novelty.

## 3. Low-energy C5 containment

For a kernel analytic near the origin,

`Phi_M(Box) = phi_0 + phi_1 Box/M^2 + phi_2 Box^2/M^4 + ...`.

At `E << M`, each finite order maps to local curvature/derivative operators in gravitational EFT/C5. The leading local `C^3`/Riemann-cubed direction is an ordinary independent gravity-EFT operator, not a beyond-C5 certificate.

Hence **no low-energy Wilson coefficient from this seed may be called `DeltaGamma_KG`.**

Any potential distinction must involve a parent-fixed all-orders/cross-regime relation that cannot be reproduced by matched C5 in its valid domain and that survives a same-domain nonlocal/UV comparator.

## 4. On-shell nontriviality search locus

Published amplitude analyses distinguish

- broad Ricci/scalar EOM-type form-factor classes that can be on-shell tree-equivalent to Einstein gravity by field redefinition;
- Riemann-sector form factors that can alter graviton scattering amplitudes.

This establishes where an on-shell-nontrivial deformation may live. It does not prove that this skeleton is viable or nondegenerate.

## 5. Critical cubic causality red-team

The cubic-first skeleton modifies the graviton three-point coupling. This invokes a major independent causality gate.

Under the assumptions of weakly coupled relativistic gravity used by the Camanho–Edelstein–Maldacena–Zhiboedov analysis, additional higher-derivative graviton three-point structures lead to high-energy causality/time-advance problems. Within that framework the problem cannot be repaired by ordinary additional particles with spin `J<=2`; an infinite tower of massive higher-spin states provides the standard resolution.

Therefore the cubic skeleton acquires the mandatory blocker

`THREE_POINT_HIGH_ENERGY_CAUSALITY_AND_HIGHER_SPIN_COMPLETION = BLOCKED`.

This is scoped, not a universal theorem against all nonlocal/strongly-coupled completions. Any proposed evasion must state which assumption is abandoned and supply the replacement causal/unitary structure.

## 6. Consequence — quartic-first fallback

If the minimality goal is to preserve both

- the Einstein-Hilbert quadratic/free graviton sector; and
- the Einstein three-graviton coupling,

then move the first prospective deformation to a regular quartic-curvature/higher `O(h^4)` structure, schematically

`S_4skel = S_EH + (lambda4/M^4) int sqrt(-g) V4[C,nabla;Psi_M]`.

A representative tensor class is `C^4` dressed by a parent-fixed kernel `Psi_M`; exact index/operator placement is not yet frozen.

Because a regular `C^4` structure starts at `O(h^4)`, it preserves the free propagator and GR cubic vertex by construction.

This avoids the **specific three-point modification gate**, but it is not automatically causal or UV complete.

## 7. Four-point causality/dispersion gate

Modern dispersion analyses of weakly-coupled four-dimensional `2->2` graviton scattering constrain higher-derivative four-graviton Wilson coefficients using causality and unitarity, relating their scale to new higher-spin states/UV data.

Therefore quartic-first candidates must still close

- crossing and unitarity;
- gravitational dispersion relations with the massless pole treated correctly;
- high-energy boundedness/time-delay constraints;
- interpretation of the UV spectrum or explicit statement of which weak-coupling/Regge assumptions are modified;
- same-domain nonlocal/UV comparator profiling.

`quartic-first` means **preserve GR 2-point and 3-point**, not “no UV completion cost.”

## 8. First physical scattering block for the original cubic skeleton

For real asymptotically flat four-dimensional massless kinematics, use the four-graviton tree amplitude as the first physical scattering target rather than treating complexified three-point amplitudes as a direct residual.

At linear order in `lambda`, a complete four-point response must include

1. the quartic contact obtained by expanding `V3` to `O(h^4)`;
2. exchange graphs containing one Einstein-Hilbert cubic vertex and one new `V3` cubic vertex in every required channel/orientation;
3. all diffeomorphism Ward/contact completion.

At higher order in `lambda`, graphs with two new cubic vertices and any other parent-required terms also enter.

No amplitude may be compared before complete same-parent response generation.

For a quartic-first parent, the leading new four-point block instead begins with the complete `V4` contact hierarchy; any parent-induced auxiliary/exchange structure must still be included if the exact parent contains it.

## 9. Cross-regime observable design

A useful future block should probe a dimensionless crossing/helicity/angle shape over several kinematic points with `E/M=O(1)` while retaining lower-energy points as EFT/IR anchors.

The same shared parameters must predict all points/configurations. Independent per-energy form-factor coefficients are forbidden.

Prospective split:

- training/anchor: IR normalization plus one cross-regime point;
- holdout: other crossing-related energy/angle/helicity points predicted without shared-parameter retuning.

## 10. Mandatory E1 taxes

Before any promotion, an exact E1 seed must close

1. kernel derivation/rigidity;
2. Lorentzian reality/CTP completion;
3. retarded/micro/global causality;
4. field-redefinition/on-shell-equivalence audit;
5. unitarity/analyticity/dispersion;
6. complete Ward response;
7. full C5 low-energy quotient;
8. same-domain nonlocal/UV comparator quotient at `E~M`;
9. cross-order/intervention/holdout rigidity;
10. nonzero COR + global separation;
11. if three-point coupling is modified, the explicit CEMZ/high-energy causality and UV-completion gate.

## 11. Current exact blockers

For cubic-first:

- `PARENT_FIXED_KERNEL_DERIVATION = BLOCKED`;
- `THREE_POINT_HIGH_ENERGY_CAUSALITY_AND_HIGHER_SPIN_COMPLETION = BLOCKED`.

For quartic-first:

- `PARENT_FIXED_KERNEL_DERIVATION = BLOCKED`;
- `FOUR_GRAVITON_DISPERSION_CAUSALITY_UV_COMPLETION = BLOCKED`.

Positive spectral density/ghost-free pole structure does not select a unique kernel and cannot close these blockers.

## 12. Promotion status

`ANSATZ_PROMOTED = false`.

The cubic skeleton is now retained mainly as a causality-red-team reference. The **more conservative next search architecture is quartic-first**, but it too remains pre-ansatz and blocked.
