# KMQGB Iter447 numerical repair delta

Initial production run `34721476885` on head `316e3e392e66ff24c1242f6173e8f6893cc3710e` is **NUMERICAL/IMPLEMENTATION FAIL, not scientific FAIL**.

First causal failure (representative job `103628062480`, identical failure family across all four lanes): mpmath 1.3.0 `hyp2f1` near z->1 entered an internal analytic-continuation path that attempted an ordering comparison on a complex value and raised `TypeError: no ordering relation is defined for complex numbers` before any lane JSON was emitted. Artifact upload consequently failed for lane jobs. Frozen science, matrix, beta grid, 100 dps and thresholds were never evaluated.

Minimal repair commit: `2b4b70ad3aacb19c4cfc4376077aacf0da9e46c2`.

Repair method: exact Euler hypergeometric transformation
`2F1(a,b;c;z) = (1-z)^(c-a-b) 2F1(c-a,c-b;c;z)`.
For the frozen Toller parameters, `c-b` is a non-positive integer, so the transformed hypergeometric terminates. This is an exact representation change of the same source function; no frozen physics object, parameter, threshold or interpretation rule was altered.

Repaired authoritative production run: `34721563256`, head `2b4b70ad3aacb19c4cfc4376077aacf0da9e46c2`.
At recovery-write time it is queued. Consume its artifacts before any scientific classification.

Formal locks unchanged: D7-S2 remains open; D7-S3/D7-S4 remain open; terminal D7 classifier and candidate classification/activation remain unauthorized.
