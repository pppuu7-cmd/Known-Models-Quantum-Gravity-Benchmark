# MISP2 Q1 — Prospective BCC Control-Geometry Freeze

**Status:** prospective Q1 control geometry, frozen before solving the spin-2 unitary classification.  
**KMQGB iteration:** 064.  
**Target:** `MISP2-QCA` — Minimal Isotropic Self-interacting Physical-spin-2 Quantum Cellular Automaton.  
**Purpose:** prevent post-hoc lattice choice after inspecting a desired spin-2 spectrum.

## 1. Why BCC is the first control geometry

The 3D QCA literature provides a strong minimal free-field control. Under homogeneity, strict locality, isotropy, unitarity and a two-dimensional internal coin, the nontrivial 3D isotropic Weyl quantum walks/QCAs live on the body-centered-cubic (BCC) Cayley lattice; up to local basis changes there are two Weyl automata.

Representative authorities:

- G. M. D'Ariano, P. Perinotti, *Derivation of the Dirac equation from principles of information processing*, Phys. Rev. A 90, 062106 (2014).
- P. Raynal, *Simple derivation of the Weyl and Dirac quantum cellular automata*, Phys. Rev. A 95, 062344 (2017).
- G. M. D'Ariano, M. Erba, P. Perinotti, *Isotropic quantum walks on lattices and the Weyl equation*, Phys. Rev. A 96, 062101 (2017).

This does **not** prove BCC is unique for spin-2. It makes BCC the first prospectively frozen control because it is already selected by an independent minimal-isotropy classification rather than chosen to fit a graviton result.

If BCC fails the spin-2 constraints, any enlargement of graph, local dimension, radius or circuit depth must be registered **before** inspecting the enlarged candidate's hard result.

## 2. Frozen Weyl control symbol

Choose one of the two equivalent Weyl automata, conventionally the `+` branch,

`A(k) = lambda(k) I - i n(k).sigma`,

with

`c_a = cos(k_a/sqrt(3))`, `s_a = sin(k_a/sqrt(3))`,

`n_x = s_x c_y c_z + c_x s_y s_z`,

`n_y = c_x s_y c_z - s_x c_y s_z`,

`n_z = c_x c_y s_z + s_x s_y c_z`,

`lambda = c_x c_y c_z - s_x s_y s_z`.

It satisfies

`lambda^2 + |n|^2 = 1`,

so `A(k)` is exactly unitary. For `|k| << 1`,

`n(k) = k/sqrt(3) + O(k^2)`,

`A(k) = exp[-i (k/sqrt(3)).sigma] + higher lattice corrections`.

The trigonometric symbol arises from a finite BCC neighborhood, so it is a strict finite-range control update.

## 3. Q1 locality choice

The exact local-TT no-go in `protocol/LOCAL_TT_PROJECTOR_NO_GO.md` forbids using an exact momentum-dependent TT projector as the microscopic finite-range gate.

Therefore the MISP2 `S-local` Q1 architecture is frozen to use a **local ambient representation with constraints**, not a two-component TT-only cell.

The first free-sector ambient control is the spin-2 irreducible representation

`R_5 = Sym^4(C^2)`,

which has complex dimension five and is equivalent to the ordinary spin-2 representation. In a continuum curvature language the same dimension is carried by a complex symmetric-traceless spatial tensor such as `E_ij + i B_ij`.

Important limitation: `R_5` is a one-particle/free-sector representation control. It is **not yet** the full finite-local-Hilbert interacting parent required by P4.

## 4. Frozen Q1 requirements

For the first BCC spin-2 control, require prospectively:

1. finite-range translation-invariant symbol `U_0(k)`;
2. exact unitarity for every `k` in the Brillouin zone;
3. covariance under the selected BCC isotropy group;
4. a local ambient register, with physical spin-2 selected by constraints/helicity reduction rather than a nonlocal TT microscopic projector;
5. exactly two physical gapless helicity `+2/-2` branches near the selected relativistic point;
6. no extra gapless physical gravitational scalar/vector branches;
7. one direction-independent leading IR propagation speed;
8. if matter and gravity share one microscopic clock/update, the spin-2 and Weyl matter branches must share the same low-energy light cone after one **common** global unit convention;
9. no helicity-dependent or sector-dependent time rescaling is allowed to repair a mismatch after inspection.

## 5. Shared-clock criterion

Let the Weyl control have eigenphases `±omega_W(k)` with

`omega_W(k) = |k|/sqrt(3) + O(k^2)`.

For a candidate spin-2 control define the physical helicity phases `omega_+(k), omega_-(k)`.

A necessary same-clock condition is

`|grad_k omega_+| = |grad_k omega_-| = |grad_k omega_W|`

at the common relativistic point, up to one global choice of microscopic length/time units applied to **all** sectors.

A candidate requiring a separate gravity-only clock rescaling is not a valid unified Q1 control.

## 6. Why this criterion matters for gravity

Universal coupling in the GR limit requires more than two helicities. The gravitational and matter sectors must share the same emergent causal cone before any candidate-specific high-energy deformation is interpreted as quantum gravity.

A finite-rule model that reproduces a massless spin-2 representation but propagates it with a different leading speed has not yet reproduced the GR infrared anchor.

## 7. Q1 enlargement policy

The first prospective architecture is therefore frozen as

`BCC + finite-range local unitary + R5 ambient spin-2 control + local constraint/helicity reduction + shared Weyl clock`.

If this fails, the next enlargement may alter only one registered axis at a time, for example:

- larger local representation dimension;
- doubled/chiral ambient register;
- increased finite neighborhood;
- multi-substep finite-depth circuit;
- explicit local constraint ancillas.

The enlargement and its additional parameter count must be frozen before solving the new spectrum.

## 8. Novelty guardrail

Historical work by I. Bialynicki-Birula already describes higher-spin generalizations of local unitary cellular automata (Phys. Rev. D 49, 6920 (1994)).

Therefore a successful free BCC spin-2 automaton is a **Q2 existence/control result**, not P4 novelty.

The first possible KG novelty remains the interacting Q3/Q4 statement:

`same finite local update -> constraint-preserving GR cubic -> derived, not independently inserted, quartic/higher hierarchy`.

## 9. Score consequence

This prospective freeze prevents lattice/clock post-selection but does not supply an interacting parent.

- R1 unchanged;
- R2 unchanged;
- R3 externally controlled;
- R4 unchanged.

Next exact step: test the simplest spin-2 representation lift of the frozen Weyl symbol as a Q2 control.
