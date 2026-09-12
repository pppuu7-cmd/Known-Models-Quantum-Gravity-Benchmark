# Iter437 preregistration — source-backed Lorentzian Regge boundary completion

Date: 2026-09-12
Status: FROZEN BEFORE ITER437 COMPUTATION

## Motivation

Iter436 tests a necessary local magnetic-closure condition under one diagnostic spin completion. Its preregistration explicitly forbids tuning alternative spin completions after observing Iter436. Iter437 therefore fixes an independent completion from published Lorentzian EPRL boundary data before any Iter437 result is computed.

## External source lock

Primary source: P. Donà, M. Fanizza, G. Sarno, S. Speziale, *Numerical study of the Lorentzian Engle-Pereira-Rovelli-Livine spin foam amplitude*, Phys. Rev. D 100, 106003 (2019), arXiv:1903.12624v3.

The paper constructs Lorentzian Regge boundary data from a nondegenerate Lorentzian 4-simplex with all boundary tetrahedra spacelike. For the numerical Lorentzian configuration it selects an isosceles 4-simplex with one equilateral tetrahedron and four equal isosceles tetrahedra. The ten boundary areas/spins have the homogeneous pattern:

- four faces of the equilateral reference tetrahedron: `j = 5 lambda`;
- the remaining six faces: `j = 2 lambda`;
- integer homogeneous scale `lambda >= 1`.

The source reports the ratio `2/5` as the selected admissible Lorentzian configuration and uses four thin wedges with `j=5 lambda` in the Lorentzian-Regge asymptotic evaluation.

## Frozen graph assignment

Use K5 vertices `0..4`, with vertex `0` identified with the equilateral reference tetrahedron.

- `j_(0b) = 5` for `b=1..4`;
- `j_(ab) = 2` for `1<=a<b<=4`.

The common homogeneous scale is frozen to `lambda=1` for the discrete magnetic-closure audit. Because all fixed extremal magnetic labels and all free magnetic ranges scale homogeneously, this is the primitive integer representative of the published family; no spin values may be changed after seeing the result.

## Frozen scientific question

For every one of the 16 source-specific K5 causal sigma sectors and both Iter435 slow escape clusters `s=3,4`:

1. reproduce the Iter435 extremal crossing-leg assignment `m=-j` when `kappa=+1`, `m=+j` when `kappa=-1`;
2. keep all noncrossing legs free over their exact SU(2) magnetic spectra for the source-backed `j=5/2-pattern` above (four `j=5`, six `j=2` faces);
3. test necessary local magnetic closure at all five tetrahedra by two independent algorithms:
   - explicit Cartesian enumeration of free magnetic labels;
   - doubled-integer interval/parity criterion;
4. require exact agreement of both algorithms and validate the source spin-pattern/intertwiner admissibility before classifying a lane.

## Frozen classification

- `SOURCE_BACKED_LORENTZIAN_BOUNDARY_ALLOWS_SLOW_EXTREMAL_PROFILE` if all five local closures exist.
- `SOURCE_BACKED_LORENTZIAN_BOUNDARY_EXCLUDES_SLOW_EXTREMAL_PROFILE` otherwise.
- aggregate `SOURCE_BACKED_SLOW_OBSTRUCTION_SURVIVES_LOCAL_MAGNETIC_CLOSURE` if at least one of 32 valid lanes allows closure.
- aggregate `SOURCE_BACKED_SLOW_OBSTRUCTION_KILLED_BY_LOCAL_MAGNETIC_CLOSURE` only if all 32 valid lanes exclude it.
- any failed independent control yields `CONTROL_INVALID`, never a scientific conclusion.

## Scope guard

This is a necessary local SU(2) magnetic-closure test under a published Lorentzian-Regge boundary-spin pattern. Survival is not a proof of noncompact causal-vertex divergence. Exclusion is not a no-go theorem. The test does not perform the full SU(2) Haar/intertwiner tensor contraction, angular integration, normalized causal-vertex integral, complete-stack cutoff removal, or same-realization UV-to-Regge/GR transport. D2, D4, D7-S2/S3/S4 and terminal D7 remain open unless separately closed by their own contracts.
