# Iter504P — terminal out-of-sample point-drift localization

Date: 2026-09-17  
Status: TERMINAL

## Classification

`ITER504P_POINT_GRID_DRIFT_WITHIN_FROZEN_TOLERANCE_SCOPED`

This is a scoped sampled-point localization PASS. It is not a continuous NONDECAY theorem.

## Frozen authority

- preregistration: `77bac4728401200b226dda16447befce85df0c66`;
- frozen classifier: `37a04752ccee6fd1caa901df36ecfcf5f50dced4`;
- frozen aggregate: `e18ed81f33271e3cab66ac8b67119587702eb7d2`;
- upstream terminal Iter504 run: `34907349374`;
- upstream workflow head: `56362459a826e3e376c529446678f2fbcaa269ae`;
- upstream terminal record: `e3816c0437a1f895196d2bbccacfb05e8dd38e74`.

The known lane `0to5-b0` was inspected before the Iter504P preregistration and remains a non-decisive control only. The decisive cohort is exactly the other 11 lanes, for exactly `11 x 4 x 9 x 4 = 1584` records.

Frozen formula:

`D_point = abs(actual_slope - early_actual_slope)`

Frozen threshold:

`D_point <= 0.05`.

## Execution-only provenance repair

The first production attempt, run `35151368577`, failed in source-lock before any decisive artifact was consumed because its ancestry check referenced a nonexistent Iter504 terminal-record SHA. No science lane or aggregate ran.

The execution-only repair was prospectively frozen in `f8f983ee98b4d01101ef6d5ca72e7ba6053e1855`. Only the terminal-record provenance binding was corrected to the actual durable Iter504 terminal record. The source run/head, 11 decisive lanes, artifact IDs/digests, formula, threshold and classifier were unchanged.

## Authoritative production run

Repaired Actions run `35151656186` at workflow head `b7f4f1f94d7668eba22c8bad25050ef632648ec9` is terminal `completed/success`.

Jobs:

- source-lock `104981172113`;
- Decimal lane `104981427613`;
- float lane `104981427636`;
- aggregate `104982529228`.

Artifacts:

- Decimal `10468939725`, `sha256:aeeac0ba27efa51bf05b7da1761b799c257d4c94b0c9c7db20bd3e935217fb06`;
- float `10469641510`, `sha256:4034866a04e7221c576ec58da3d6c2ac1429b26081e4814a958f240e7b25d621`;
- aggregate `10469975534`, `sha256:c8d031b4c3a05b49870217f688d6f6b9d4ac05312c55078760271f0968bd6786`.

Aggregate JSON SHA256:

`0fcbc4f0d8927a2fefbea0c22aae8fe1bbb4cd963ac66b4eb2d8eddc719a78a4`.

Aggregate scientific payload SHA256:

`4dc3d408e768a6bc8ad613b286e0b920b0dc294d36184f836c767f7c5b8632a1`.

Aggregate SHA256:

`cda258218526ff4f556bb901e4fb8e4a51e819eb07c7881b3438d1416bbccb75`.

## Exact scientific result

All frozen decisive structure checks pass:

- decisive lanes: `11/11` exact;
- decisive records: `1584/1584` exact;
- missing/duplicate/extra decisive records: `0`;
- threshold violations: `0`;
- control `0to5-b0` excluded from decision: yes;
- Decimal/float scientific classification agreement: exact.

Maximum decisive drift:

`D_point,max = 0.009396862546624`.

This leaves threshold margin

`0.05 - D_point,max = 0.040603137453376`.

The maximum is only `18.79372509324800%` of the frozen tolerance.

Maximum-drift witness:

- lane `0to5-b1`;
- block `1`;
- path `2`;
- sign `+1`;
- direction `[1,-1,1,-1,1,-1]`;
- amplitude `0.0025`;
- rho `1.6`;
- actual slope `4.001444332976603`;
- early actual slope `4.010841195523227`;
- `D_point = 0.009396862546624`.

Per-causal maximum drifts:

- `0to5`: `0.009396862546624`;
- `1to4`: `0.009196594991085`;
- `2to3`: `0.0052106927066000`.

Per-block maxima over the decisive cohort:

- `b0`: `0.008756656122886`;
- `b1`: `0.009396862546624`;
- `b2`: `0.009342723689345`;
- `b3`: `0.009252678041871`.

Independent adversarial replay additionally finds all `1584` decisive late slopes positive and all `1584` decisive early slopes positive.

The non-decisive control has 144 records, zero threshold violations and maximum drift `0.009276174609423`; these control values do not enter the terminal classifier.

## Independent exact reproduction / Critic

A fresh replay of the frozen official Decimal classifier, float classifier and aggregate directly from the authoritative terminal Iter504 raw point artifacts produced exactly the same output hashes as production:

- Decimal JSON `0e7722c610e5f68a5e5430974a0df40c6dfea6363556537b079bd65c9a11fdf6`;
- float JSON `83cf1c9c8f8f57b6cb65e763c79b74982a4f76eb41a6b467862e91ca11ee8385`;
- aggregate JSON `0fcbc4f0d8927a2fefbea0c22aae8fe1bbb4cd963ac66b4eb2d8eddc719a78a4`.

Thus the independent aggregate is byte-identical to the production aggregate.

Post-terminal adversarial Critic: `results/ITER504P_INDEPENDENT_ADVERSARIAL_CRITIC_2026-09-17.md`.

Verdict:

`CRITIC_CONFIRMS_ITER504P_WITHIN_FROZEN_TOLERANCE_SCOPED`.

## Scientific meaning

The independent frozen point grid itself does **not** violate the `0.05` stationarity criterion. Therefore the 1888 `INTERVAL_INCONCLUSIVE` states in Iter504 cannot be explained by sampled point-level drift above the frozen tolerance on this decisive grid.

The highest-information remaining bottleneck is now localized to the rigorous **continuous** centered interval enclosure: dependency width and nonsmooth multi-channel max-envelope competition/crossings. The known Iter504 continuous campaign can have many simultaneously possible maximizing channels even while the sampled point slopes remain stationary.

Accordingly, the next scientific gate must attack continuous enclosure width without changing the physics domain, threshold or classifier.

## Claim ceiling

This result does not prove continuous NONDECAY, distributional/Haar divergence, positive-measure behavior, cutoff removal, full ten-spectral causal-vertex behavior, D7-S2 closure or any terminal global selector. It does not establish model/family failure, Candidate Gravity activation, a solved quantum-gravity theory or new physics.

`D7-S2 = NOT_CLOSED`.  
`D7-S3 = NOT_CLOSED`.  
`D7-S4 = PARTIAL_GLOBAL_NOT_CLOSED`.
