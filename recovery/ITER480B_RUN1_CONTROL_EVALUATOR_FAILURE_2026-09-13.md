# Iter480B run-1 diagnostic — control evaluator failure, not scientific FAIL

Date: 2026-09-13
Frozen prereg: `da49c5b97494992e62045355579645698da91821`
Production head: `265ab546f24e922894b85b9a3737475eb38629e5`
Run: `34773180686`
Aggregate artifact: `10322597187`, digest `sha256:ff225634af68fc31444a3bf6a83a4707556fe7b31bab33a35957efcd343e395d`

## Classification
`NUMERICAL_IMPLEMENTATION_CONTROL_EVALUATOR_FAILURE_NONAUTHORITATIVE`

This run is not an authoritative scientific PASS/FAIL for Iter480B.

## First causal failure
The preregistered reindexing control requires the sorted multiset of contraction magnitudes before/after the pure dummy-index map `m -> -m` to agree within relative `1e-10`.

The run-1 implementation evaluated this as the maximum *entrywise* quantity
`|x-y| / max(|x|,|y|,1e-300)`.
For entries that are mathematically zero but acquire different floating roundoff at approximately machine-zero under changed summation order, this quantity becomes O(1). That is not the stated multiset-relative residual and causes a false control failure.

Concrete raw evidence from lane `g7-0to5`, job `103766404721`, artifact `10322961224`, digest `sha256:ccdfe812acca7e9fa89ca6201993db16ef3d801c1287fe0e5e30d1f185db6c4e`:
- Eq.(90) intertwiner support/norm/orthogonality: PASS, Gram residual `5.55e-17`;
- coefficient scale finite/positive: PASS (`2.24456412339957e-15`);
- scientific nonzero witness predicate: PASS (`130/243` witnesses, max dimensionless ratio `0.0046296296296296285`);
- all-zero negative control: PASS exactly (`0.0`);
- only the reindex evaluator failed, reporting `1.0` because of entrywise relative normalization at numerical zeros.

The six raw lane artifacts and aggregate were produced and retained. Several lanes passed even the faulty evaluator, while failed lanes show the same control-layer pattern. No frozen source model, causal panel, witness threshold, or scientific interpretation is changed.

## Minimal repair allowed
Keep `REINDEX_RTOL=1e-10` unchanged and compute the stated **multiset-level relative residual** as
`max_i |x_i-y_i| / max(max_i |x_i|, max_i |y_i|)`
for the sorted magnitude multisets. This is scale-free, treats the multiset as one object, and does not amplify mathematically-zero entries by dividing each one by its own roundoff magnitude.

Only this evaluator implementation may change. Retry must use the same frozen preregistration and all other code/science unchanged.
