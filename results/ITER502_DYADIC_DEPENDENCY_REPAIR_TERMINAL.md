# Iter502 — dyadic dependency-repair terminal result

## Authority
- preregistration: `31394639d96d202dd00ca14e1f8026264ccf993e`
- evaluator: `b615387c4784aae451a912a10d536fb555d52b61`
- aggregate classifier: `ddb5ff8bbcd5513c1aba40ce5314515f01241603`
- production/workflow head: `8a676e37e7eb86d92671bdd2c76f763deb3d3804`
- authoritative run: `34830476485`
- source-lock job: `103932380577` — success
- aggregate job: `104048209622` — success
- aggregate artifact: `10356359599`
- aggregate artifact digest: `sha256:b25baacf2d1cc04cd71a018189234c29501faedcbd2434a4b3aa308b5f97b7e3`

## Terminal classification

`ITER502_NUMERICAL_METHOD_BLOCKER`

This is a numerical-enclosure result only. It is not a DECAY/NONDECAY scientific result and does not close D7-S2.

## What happened
The workflow was cancelled after roughly six hours. Four `2to3` lanes were cancelled before artifact upload. Eight lane artifacts were completed and consumed by the frozen aggregate classifier.

All 8/8 completed lane artifacts independently failed the unchanged source point-containment prerequisite:

- `0to5-b0` — method blocker, point regression false;
- `0to5-b1` — method blocker, point regression false;
- `0to5-b2` — method blocker, point regression false;
- `0to5-b3` — method blocker, point regression false;
- `1to4-b0` — method blocker, point regression false;
- `1to4-b1` — method blocker, point regression false;
- `1to4-b2` — method blocker, point regression false;
- `1to4-b3` — method blocker, point regression false.

The aggregate therefore reported:

- `classification = ITER502_NUMERICAL_METHOD_BLOCKER`;
- `method_blocker = true`;
- `n_jobs = 8`;
- `n_valid_subboxes = 0`;
- `point_regression_fail_job_ids` equal to all eight completed lanes;
- missing lanes `2to3-b0..b3` due run cancellation.

## Interpretation
The prospectively frozen exact 8-way subdivision of every Iter501 amplitude box did **not** recover source point containment on any completed lane. This rules out the hypothesis that a modest fixed dyadic refinement alone cures the enclosure dependency loss.

The scientific thresholds remain unchanged. No interval slope class is promotable from Iter502 because the prerequisite failed upstream.

The cancelled `2to3` lanes do not rescue the method claim: the gate already has eight independent completed counterexamples to successful containment repair. They also do not support any scientific DECAY/NONDECAY claim because the run is structurally incomplete for such an interpretation.

## Authorized next method family
Per the frozen Iter502 preregistration, the next dependency-repair attempt must use a genuinely dependency-preserving construction, such as a centered/mean-value enclosure or a direct correlated-factor enclosure. Further unregistered subdivision or threshold relaxation is forbidden.

## Scope guards
- D7-S2: `NOT_CLOSED`;
- D7-S3: `NOT_CLOSED`;
- D7-S4: `PARTIAL_GLOBAL_NOT_CLOSED`;
- terminal D7 labels remain forbidden;
- Candidate Gravity remains inactive;
- no positive-Haar-measure, absolute-Haar, spectral-integral, PV/conditional, distributional-boundary-value or K5-collision theorem follows from Iter502.
