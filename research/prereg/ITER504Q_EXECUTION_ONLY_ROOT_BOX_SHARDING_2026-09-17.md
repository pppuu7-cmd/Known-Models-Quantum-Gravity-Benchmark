# ITER504Q execution-only root-box sharding

Date: 2026-09-17
Status: PROSPECTIVELY FROZEN EXECUTION-ONLY REPAIR/ACCELERATION

## Trigger

Authoritative Iter504Q run `35153170282` has passed source-lock and both independent Python environments are executing the prospectively frozen full-channel adaptive diagnostic. No Iter504Q substantive lane artifact or value has been consumed.

The frozen diagnostic evaluates three mutually disjoint root amplitude boxes, 13, 14 and 15, sequentially inside each Python environment. Their adaptive trees are scientifically independent until the frozen `summarize(boxes)` call.

## Allowed execution-only transformation

For each Python environment independently:

1. execute the already-frozen `evaluate_box(root_box, direction, sign)` function from commit `18ef963041fe6ddec35e12cece0939aa18189a77` in three parallel jobs, one each for root boxes `13`, `14`, `15`;
2. persist each returned root-box dictionary without modification;
3. sort the three dictionaries by `root_box`;
4. call the already-frozen `summarize(boxes)` function from the same implementation commit;
5. serialize with the same `json.dump(..., indent=2, sort_keys=True)` convention used by the unsharded script;
6. run the already-frozen independent-environment aggregate `432c6a38b310eae177a2d0675b95994cb6a89f34`.

## Scientific immutability

The sharding MUST NOT change:

- Iter504Q preregistration `881c804f56a9a9969f8c969ea3ccd1826da92846`;
- diagnostic implementation `18ef963041fe6ddec35e12cece0939aa18189a77`;
- root boxes 13,14,15 or their exact rational endpoints;
- causal/block/path/direction/sign;
- all four rhos or all four R values;
- 384-bit Arb/Acb arithmetic or `python-flint==0.9.0`;
- full 243-channel recomputation on every subbox;
- maximum depth 6;
- exact midpoint bisection;
- robust floor +1.0;
- drift threshold 0.05;
- exact-cover requirements;
- PASS/INCONCLUSIVE/INVALID semantics.

No root-box result may be omitted because it is slow or scientifically unfavorable.

## Equivalence control

If the original unsharded lanes later complete, the assembled sharded lane JSON for the same Python environment must be byte-identical to the unsharded JSON or the sharded execution is not accepted as an equivalent production realization. A discrepancy is an execution/implementation issue, not scientific evidence.
