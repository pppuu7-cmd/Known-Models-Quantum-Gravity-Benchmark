# Iter504P independent adversarial Critic

Date: 2026-09-17  
Status: TERMINAL REVIEW

## Verdict

`CRITIC_CONFIRMS_ITER504P_WITHIN_FROZEN_TOLERANCE_SCOPED`

The terminal classification

`ITER504P_POINT_GRID_DRIFT_WITHIN_FROZEN_TOLERANCE_SCOPED`

is independently reproduced from the authoritative terminal Iter504 point artifacts under the prospectively frozen Iter504P rules.

## Frozen decision contract checked

The Critic independently enforces:

- exactly the 11 decisive lanes frozen by preregistration `77bac4728401200b226dda16447befce85df0c66`;
- `0to5-b0` is loaded only as a disclosed non-decisive control and is excluded from classification;
- exactly 4 signed paths x 9 amplitudes x 4 rhos per decisive lane;
- exactly `1584` decisive records total;
- lane/causal/block/header consistency and `valid=true`;
- no duplicate path/amplitude/rho record identity inside a lane;
- required `actual_slope` and `early_actual_slope` fields are present and finite;
- frozen formula `D_point = abs(actual_slope - early_actual_slope)`;
- frozen threshold `0.05`;
- no clipping, lane removal or outcome-dependent filtering;
- exact maximum-drift witness;
- per-lane, per-causal-family and per-block maxima;
- early and late slope signs.

Arithmetic is independently evaluated both as high-precision decimal lexical arithmetic and exact rational `Fraction` arithmetic. They agree record-by-record.

Critic script SHA256: `16592b97c4520ea6bb9e324324e00a4a98423f7f31088d291249f0c28b7897ee`.  
Critic result JSON SHA256: `d1a00e470a28b86fa93720148dd76bad2743f2a92fd556767a5c5f538ab3e3df`.  
Independent Critic core SHA256: `5da43e58804213463f1be0e14e6bce821990deda7e4bd90f838ff30342efa059`.

## Exact result

- decisive records: `1584/1584`;
- structural errors: `0`;
- threshold violations: `0`;
- maximum decisive `D_point = 0.009396862546624`;
- frozen threshold: `0.05`;
- threshold margin: `0.040603137453376`;
- all `1584` decisive late slopes are positive;
- all `1584` decisive early slopes are positive.

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

Per-causal maxima:

- `0to5`: `0.009396862546624`;
- `1to4`: `0.009196594991085`;
- `2to3`: `0.0052106927066000`.

Per-block maxima over decisive lanes:

- `b0`: `0.008756656122886`;
- `b1`: `0.009396862546624`;
- `b2`: `0.009342723689345`;
- `b3`: `0.009252678041871`.

The disclosed control `0to5-b0` has 144 records, zero violations and maximum drift `0.009276174609423`, but these values do not affect the classifier.

## Production cross-check

Authoritative repaired Actions run `35151656186` at head `b7f4f1f94d7668eba22c8bad25050ef632648ec9` completed source-lock, independent Decimal and float lanes, and aggregate successfully.

Production artifacts:

- Decimal `10468939725`, digest `sha256:aeeac0ba27efa51bf05b7da1761b799c257d4c94b0c9c7db20bd3e935217fb06`;
- float `10469641510`, digest `sha256:4034866a04e7221c576ec58da3d6c2ac1429b26081e4814a958f240e7b25d621`;
- aggregate `10469975534`, digest `sha256:c8d031b4c3a05b49870217f688d6f6b9d4ac05312c55078760271f0968bd6786`.

Independent replay of the frozen official classifier and aggregate from the terminal upstream raw artifacts produced:

- Decimal JSON SHA256 `0e7722c610e5f68a5e5430974a0df40c6dfea6363556537b079bd65c9a11fdf6`;
- float JSON SHA256 `83cf1c9c8f8f57b6cb65e763c79b74982a4f76eb41a6b467862e91ca11ee8385`;
- aggregate JSON SHA256 `0fcbc4f0d8927a2fefbea0c22aae8fe1bbb4cd963ac66b4eb2d8eddc719a78a4`.

These three hashes exactly equal the production hashes reported by the terminal aggregate. The aggregate scientific payload SHA256 is `4dc3d408e768a6bc8ad613b286e0b920b0dc294d36184f836c767f7c5b8632a1`; aggregate SHA256 is `cda258218526ff4f556bb901e4fb8e4a51e819eb07c7881b3438d1416bbccb75`.

## Critic self-correction

An initial Critic draft additionally demanded equality of the four signed-path identity sets across different causal/block lanes. That condition is not present in the frozen preregistration and is not implied by the per-lane 4-path contract. It was therefore removed as an unauthorized Critic-only overconstraint before the terminal Critic verdict. No decisive lane, record, formula, threshold or source value changed; after removing only that unsupported check, structural errors are exactly zero.

## Scientific interpretation

The frozen independent point grid itself does not exhibit drift above `0.05`. This localizes the Iter504 INCONCLUSIVE bottleneck away from sampled point-level stationarity failure and toward the rigorous continuous interval enclosure/dependency/nonsmooth max-channel layer on the frozen sampled-point scope.

This is not a continuous NONDECAY proof. Positive sampled slopes do not establish an absolute-Haar divergence theorem, and the result does not close D7-S2 or authorize any global selector/model/family/new-physics conclusion.
