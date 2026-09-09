# KMQGB Recovery Delta 144

**Chronology repair:** this recovery entry records the already-existing scientific Iter144 and fills the previously missing recovery delta. It does not reuse or reinterpret the iteration ID.

## Iter144 authority

Added the independent KMQGB nonlinear detector-facing probability-likelihood regression corresponding to

`P = (1 + C cos Phi)/2`

with source-traceable physical colored phase covariance propagated through the shot-dependent detector slope and with phase, contrast, readout and calibration nuisance directions.

The regression retains required negative controls:

- static science with free phase offset is non-identifiable;
- modulation without calibrated reference is non-identifiable;
- an unconstrained reference amplitude is non-identifiable;
- finite independent reference calibration restores the science direction;
- detector/contrast/readout stresses do not manufacture or erase the nominal PASS by hidden regularization.

## Score rule

Iter144 by itself creates the executable closure candidate. The R2 score change is deferred to Iter145, after methodology-ci run `34397157673` independently completed `success`.

This delta repairs recovery continuity only.