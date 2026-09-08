# KMQGB Twelfth Wave — Multi-Configuration / Intervention Rigidity

**Frozen denominator:** 5 methodology targets.  
**Historical waves 1–11:** terminal and immutable.  
**Status:** **TERMINAL 5/5 = 100%**.  
**Purpose:** use controlled source/detector/configuration changes to rotate signal/comparator geometry and break degeneracies while preserving one shared parent dynamics.

| # | Target | Terminal result | State |
|---|---|---|---|
| T12-01 | configuration-stacked observable | freeze multi-configuration observable/covariance notation | `PASS_RQIR_GATE` |
| T12-02 | parameter-incidence separation | distinguish shared dynamics, shared nuisance, configuration-local nuisance and known controls | `PASS_RQIR_GATE` |
| T12-03 | configuration-null contrasts | derive comparator/nuisance-null differences and general contrasts | `PASS_RQIR_GATE` |
| T12-04 | cross-configuration covariance | require full covariance and forbid false independence assumptions | `PASS_RQIR_GATE` |
| T12-05 | intervention design criterion | choose controls by projected rank/singular values/SNR after comparator profiling | `PASS_RQIR_GATE` |

**Twelfth-wave terminal coverage: 5/5 = 100%.**

## Authoritative protocol

`protocol/INTERVENTION_CONFIGURATION_RIGIDITY.md`

Reference code:

`code/intervention_design_reference.py`

## Central rule

Controlled variables such as source mass assignment, separation, orientation, frequency, proper time, state preparation and detector configuration are **design variables**, not free fit parameters when known.

The same dynamics parameters remain shared across configurations. Only physically justified local nuisances may vary independently.

## Dimension gain

Adding a new configuration with `k` physical observables changes the local comparator-complement dimension by

`Delta d_perp = k - Delta rank(J_union)`.

Thus a new configuration is valuable when it adds more physical directions than comparator/nuisance freedom.

## Attribution-oriented interventions

Useful controls can target specific loopholes:

- source species/composition -> universality/stress-energy attribution;
- orientation/polarization -> helicity/tidal attribution;
- frequency/time/distance sweep -> causal/retarded/analytic-origin tests;
- probe-state swaps -> state/detector attribution;
- geometry reversal/nulls -> ordinary mediator/systematic rejection;
- repeating several response orders under common controls -> cross-order rigidity.

Mass/distance scaling alone is explicitly not accepted as gravity attribution because tuned scalar mediators can mimic the Newtonian sector.

## Candidate Gravity design lesson

Future KG should be tested on a **designed family of linked configurations**, not one favorable point.

Prefer:

- few shared KG parameters;
- many controlled configurations/orders;
- few new local nuisances;
- increasing post-comparator rank/conditioning under intervention.

## Promotion guardrail

This wave is methodology only. No Candidate Gravity ansatz/readiness increase is authorized.
