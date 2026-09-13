# Iter463 control authority record — 2026-09-13

Initial production head `4aa4f51e68cae30e6cec766e7359103218cb3b16`, run `34748683091` is **CONTROL/IMPLEMENTATION INVALID for terminal scientific classification**, not a scientific FAIL.

All six raw lane artifacts were consumed. The substantive source-tail witnesses are supportive across all 24 records: P11 route agreement is at machine precision, scaled leading-power magnitudes stabilize, wrong-power controls separate strongly, and the intended leading-phase recurrence/increment errors collapse toward zero.

The first causal failure is isolated to the m=0 wrong-phase negative control implementation. The code compared the inferred phase increment against `1.35 * beta * h` with frozen `h=0.15/beta`, so even an exact correct source signal produces a wrong-control separation of only `(1.35-1)*0.15 = 0.0525 rad`. The preregistered frozen control threshold is `>=0.20 rad`; therefore this particular control instantiation could not satisfy its own frozen threshold by construction.

Scientific target, source formulas, panel, radii, leading-power hypotheses, P11 route criterion, stabilization criterion, phase-error threshold, wrong-power threshold, and wrong-phase threshold are unchanged. The only authorized repair is to choose a sufficiently separated wrong-phase control while keeping the frozen threshold fixed. Initial run remains immutable provenance and is excluded from terminal scientific classification.
