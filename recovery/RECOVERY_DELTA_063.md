# RECOVERY_DELTA_063 — Exact Finite-Range Local TT-Projector No-Go

**Date:** 2026-09-08  
**KMQGB iteration:** 063  
**External RQIR authority observed:** Iteration 621, `MODEL_READINESS=24%`.

## Stable readiness

- R1 repository readiness: **92%**.
- R2 KMQGB methodology/material readiness: **89%**.
- R3 Candidate Gravity scientific readiness: **24%**.
- R4 `MINIMAL_NOVEL_PARENT_PRINCIPLE_SEARCH`: **45%**.

No percentage changes. Iter063 closes a necessary MISP2 Q1 design lemma but does not produce the interacting P4 parent.

## New permanent theorem

Authority:

`protocol/LOCAL_TT_PROJECTOR_NO_GO.md`.

A translation-invariant finite-range linear lattice operator has a Fourier symbol

`P(k)=sum_r P_r exp(i k.r)`

with finite support, so its matrix elements are trigonometric polynomials and are continuous at `k=0`.

The exact continuum transverse projector

`P_T(k)=I-k k^T/|k|^2`

has different limits as `k->0` along different momentum rays. For example the limits along the x and y axes are `I-e_x e_x^T` and `I-e_y e_y^T`.

The spin-2 TT projector is built from this transverse projector and inherits the same direction-dependent zero-momentum limit.

Therefore no exact translation-invariant finite-range linear microscopic operator can itself be the physical transverse/TT projector on a punctured neighborhood of the zero mode.

## Correct interpretation

This does **not** rule out local gravity or local QCA gravity.

It rules out the shortcut

`local cell = only the two exact TT physical components`

when exact TT extraction is implemented as a finite-range local projector.

For an `S-local` microscopic branch, local gauge-redundant tensor/tetrad/connection variables plus local constraints/code ancillas are required; the two helicities emerge after physical reduction.

An explicitly nonlocal microscopic projector must instead enter the `D-nonlocal` audit.

## Executable witness

New reference:

`code/local_tt_projector_no_go_reference.py`.

For momentum rays `k=eps e_x` and `k=eps e_y`, independent of `eps`:

- vector transverse-projector Frobenius separation is `sqrt(2)`;
- spin-2 TT-projector separation is `sqrt(7/2)`;
- each TT projector is idempotent and has rank 2 on the full tensor embedding used by the check.

The nonzero ray separation remains as `eps -> 0`, witnessing the absence of a unique continuous zero-momentum limit.

The methodology CI now runs this executable witness and checks both the MISP2 triage and local-TT theorem entrypoints.

## Q1 consequence

A future MISP2 proposal that uses an exact TT-only local register and a momentum-dependent TT projector as a microscopic local gate is classified

`BLOCKED__MICROSCOPIC_TT_PROJECTION_IS_NONLOCAL`.

It may proceed only by reintroducing a local redundant/constraint formulation or by explicitly declaring microscopic nonlocality.

## Further comparator finding

Historical QCA literature already describes higher-spin generalizations of local unitary lattice automata (Bialynicki-Birula, Phys. Rev. D 49, 6920 (1994)).

Therefore solving a **free** spin-2 QCA alone cannot establish KMQGB novelty. Q2 is a required existence/consistency gate; the first possible KG novelty must occur at the interacting constraint-preserving Q3/Q4 hierarchy and then survive A3/P5 comparator profiling.

## Exact continuation front

1. prospectively freeze a minimal Q1 graph/register architecture;
2. use BCC as the first graph control because minimal 3D isotropic Weyl-QCA classifications select it;
3. choose a local redundant or constrained spin-2 ambient representation, not TT-only microscopic variables;
4. classify an exact finite-range unitary symbol and its physical two-helicity sector;
5. treat any free higher-spin solution as comparator/control;
6. move novelty testing to the interacting constraint-preserving update and cubic-to-quartic rigidity.

No heavy computation is justified before the interacting update is frozen.
