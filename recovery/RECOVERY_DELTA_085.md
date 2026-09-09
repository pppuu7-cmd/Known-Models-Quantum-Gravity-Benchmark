# Recovery Delta 085

**Date:** 2026-09-09  
**Iteration:** 085  
**Score change:** none.

## Scientific change

Added `candidate_synthesis/SYNTHESIS_002_PHYSICAL_HELICITY_PARQUET_CLOSURE.md`.

A gravity-sensitive parquet/Bethe-Salpeter closure was tested using physical graviton helicity sewing in the `s,t,u` channels.

The attempt fails because factorization/unitarity propagate hard information but do not select the channel-irreducible kernel `K4`:

- with Einstein-only seed it is standard GR QFT resummation and inherits the nonrenormalizable C5 counterterm tower;
- adding a local analytic `K4` is full C5;
- adding a nonlocal/nonanalytic `K4` simply moves the P4 selection problem into that function.

Classification: `A1 BLOCKED__IRREDUCIBLE_HARD_KERNEL_NOT_SELECTED_BY_FACTORISATION`; `A2 FAIL_AS_UV_PARENT`; `A3 FAIL__STANDARD_QFT_SELF_CONSISTENT_RESUMMATION_OF_GR`.

CI run `34320205564` / `#128` later completed successfully.

**R1=92%, R2=89%, R3=24%, R4=45%.**