# Model Audit — weakly nonlocal entire-form-factor gravity

Benchmark ID: KMQGB-S2-M01-NONLOCAL
Concrete realization ID: NL-EOM-ENTIRE-MINK-001
Role: ghost-free nonlocal / Stelle-contrast control
State: TERMINAL
Final status: `OPERATIONALLY_DEGENERATE`

## Frozen realization

Use the special weakly nonlocal theory built from a local Einstein(-matter) action and operators quadratic in the local equations of motion:

`S[Phi] = ∫ d^D x sqrt(|g|) [ L_loc + E_i F_ij(Delta) E_j ]`,

with

`S_loc = ∫ sqrt(|g|) L_loc`,

`E_i = delta S_loc / delta Phi_i`,

`Delta_ki = delta E_i / delta Phi_k`,

and the entire form factor fixed by

`2 Delta F(Delta) = exp(H(Delta)) - 1`,

with the concrete choice

`H(z)=z/M_*^2`, `M_*>0`, and `V(E)=0`.

For amplitudes, freeze the Euclidean-definition / analytic-continuation prescription used in the perturbative-unitarity literature rather than a naive direct-Minkowski loop-energy prescription.

The primary frozen observable is the full set of on-shell tree-level `n`-point amplitudes around Minkowski for asymptotic states belonging to the underlying local theory.

## Why this is the correct Stelle contrast

The first-wave M07 standard fundamental Stelle realization improves UV scaling through an additional massive spin-2 pole with opposite residue and therefore fails F2 under the standard physical-state interpretation.

For the present nonlocal realization the kinetic form factor is an exponential of an entire function and has no zeros. Hence the propagator has the same pole spectrum as the underlying local theory: the massless graviton pole is retained and no extra Stelle-like massive spin-2 pole is introduced.

The 2012 Biswas-Gerwick-Koivisto-Mazumdar analysis gives the simple special case

`Pi = [1/(k^2 a(-k^2))] [P^2 - (1/2) P_s^0]`

with `a` entire and zero-free, and explicitly illustrates `a(Box)=exp(-Box/M^2)` as a no-new-pole UV-softened realization.

The 2024 Briscese-Calcagni-Modesto-Nardelli spectral analysis finds positive-definite spectral density and the same spectrum as the corresponding local theory for the relevant entire-form-factor class.

## Prescription and causality guardrail

Perturbative unitarity is prescription-sensitive. The Euclidean amplitudes, analytically continued to real external energies, obey the Cutkosky-rule construction used for nonlocal theories. This must not be conflated with directly integrating real Minkowski loop energies, for which the same unitarity claim is not automatic.

Nonlocal Green functions can exhibit off-shell microscopic acausal tails / violation of strict local commutativity at distances of order the nonlocality scale. Therefore this benchmark does **not** upgrade the S-matrix result into a universal proof of strict microcausality for arbitrary source-detector observables.

## Exact tree-level comparator result

Modesto and Calcagni (JHEP 2021) prove for the frozen EOM-squared class that an analytic field redefinition maps the nonlocal action to the underlying local action at tree level. Consequently:

`A_n^nonlocal(tree,on-shell) = A_n^local(tree,on-shell)`

for every `n` in the declared class, including gravity coupled consistently to matter in that construction.

For the pure-gravity Minkowski slice, the applicable local theory is Einstein gravity. In the RQIR tree-level on-shell scattering observable,

`Delta_A_n = A_n^NL - A_n^GR = 0`

identically for all `n`.

This is not a claim that loop amplitudes, off-shell Green functions, short-distance potentials, or all nonlocal models are identical to GR.

## F0-F7 classification

| Gate | Result | Reason |
|---|---|---|
| F0 dynamics | PASS_SCOPED | exact EOM-squared nonlocal action and explicit entire `H(z)` frozen |
| F1 required limits | PASS | `H(0)=0`; local/GR IR state space and solutions retained |
| F2 consistency | PASS_SCOPED_S_MATRIX / CAUSALITY_CAVEAT | no extra propagator poles; positive spectral evidence; perturbative unitarity under frozen Euclidean-continuation prescription; strict off-shell microcausality not promoted |
| F3 RQIR hierarchy | PARTIAL | propagator/response structure is concrete; full detector CTP hierarchy not needed for the frozen scattering closure |
| F4 comparator distinction | FAIL_TO_DISTINGUISH_TREE | all frozen on-shell tree amplitudes equal underlying local/GR amplitudes |
| F5 hard discriminator | ZERO_AFTER_COMPARATOR | exact tree S-matrix residual vanishes by field-redefinition theorem |
| F6 identifiability | NOT_APPLICABLE_AFTER_ZERO | no tree-level beta direction remains in the frozen observable |
| F7 resources | NOT_APPLICABLE_AFTER_ZERO | no experiment can identify a zero tree-level theory difference in this observable |

## Q1-Q7 fingerprint

- Q1: no unique tree-level on-shell clock/scattering signature relative to the mapped local theory in the frozen sector.
- Q2: no new asymptotic branch state arises from an additional propagator pole.
- Q3: off-shell/source response may be nonlocal, but it is not promoted from the tree S-matrix identity.
- Q4: the frozen tree S-matrix cannot certify a new quantum mediator beyond GR because it is identical to GR.
- Q5: propagator UV form is modified without a new pole; off-shell fluctuation structure requires a separate observable.
- Q6: nonlocal microcausal structure is prescription/domain sensitive and remains a caveat rather than a claimed PASS.
- Q7: loop/UV quantum behavior may differ and is not erased by the present tree-level field-redefinition result.

## Terminal interpretation

`NL-EOM-ENTIRE-MINK-001` demonstrates that the Stelle ghost can be avoided without introducing an extra propagating pole, but the chosen strongest clean tree-level scattering observable then supplies no model-specific residual: it is exactly mapped to GR.

Terminal status: `OPERATIONALLY_DEGENERATE` in the frozen on-shell tree-level Minkowski S-matrix.

This is a scoped observable non-identifiability result, **not** a global disproof of weakly nonlocal gravity and **not** a proof that loops/off-shell observables are identical to GR.

## Sources

1. T. Biswas, E. Gerwick, T. Koivisto, A. Mazumdar, *Towards Singularity- and Ghost-Free Theories of Gravity*, Phys. Rev. Lett. 108, 031101 (2012), arXiv:1110.5249.
2. L. Modesto, G. Calcagni, *Tree-level scattering amplitudes in nonlocal field theories*, JHEP 10 (2021) 169, arXiv:2107.04558.
3. F. Briscese, G. Calcagni, L. Modesto, G. Nardelli, *Form factors, spectral and Källén-Lehmann representation in nonlocal quantum gravity*, JHEP 08 (2024) 204, arXiv:2405.14056.
4. F. Briscese, L. Modesto, *Cutkosky rules and perturbative unitarity in Euclidean nonlocal quantum field theories*, Phys. Rev. D 99, 104043 (2019), arXiv:1803.08827.
5. L. Buoninfante et al., *Ghost-free infinite derivative quantum field theory*, Nucl. Phys. B 944 (2019) 114646, for off-shell acausal/microcausal caveats of infinite-derivative Green functions.
