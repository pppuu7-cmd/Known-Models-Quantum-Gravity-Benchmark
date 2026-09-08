# T5-01 Audit — massless spin-2 soft theorem / universal gravitational coupling

Benchmark ID: `KMQGB-T5-M01-SPIN2-SOFT-UNIVERSALITY`  
Concrete methodological object: `WEINBERG-SOFT-SPIN2-UNIVERSAL-001`  
Role: distinguish a genuinely gravitational quantum mediator from a tuned ordinary quantum scalar/vector force  
State: **TERMINAL — `PASS_RQIR_GATE`**  
Objective: **`SPIN2_UNIVERSAL_COUPLING_ATTRIBUTION_ESTABLISHED`**

## Terminal question

T4-05 showed that a quantized massless scalar with `g_i proportional m_i` can reproduce the Newtonian branch phase while also providing a non-EB quantum channel and a nonzero commutator.

What extra structure identifies a massless quantum mediator as **gravitational** rather than merely quantum and long range?

The leading soft spin-2 theorem supplies a concrete answer in an S-matrix setting: Lorentz/gauge consistency forces **universal coupling to energy-momentum**.

## Frozen soft factor

For emission of a soft massless spin-2 quantum with momentum `q` and polarization `epsilon_mn`, factorization gives schematically

`M_(n+1)(q) -> [sum_i eta_i kappa_i p_i^m p_i^n epsilon_mn/(p_i.q)] M_n`

at leading soft order, where `eta_i=+/-1` distinguishes outgoing/incoming hard legs.

Gauge redundancy of the massless spin-2 polarization,

`epsilon_mn -> epsilon_mn + q_m xi_n + q_n xi_m`,

must leave the physical S-matrix invariant.

The gauge variation of the leading soft factor is proportional to

`sum_i eta_i kappa_i p_i^n`.

For arbitrary processes this must vanish:

`sum_i eta_i kappa_i p_i^n = 0`.

Ordinary momentum conservation supplies only

`sum_i eta_i p_i^n = 0`.

For generic species and kinematics the two conditions are compatible process-independently only when the soft spin-2 couplings are universal,

`kappa_i = kappa`

for all matter species participating in the S-matrix.

This is the S-matrix form of the gravitational equivalence/universality principle.

## Why this beats the T4-05 tuned scalar in scope

The T4 scalar adversary can be tuned in one nonrelativistic sector:

`g_i=sqrt(4 pi G)m_i`

so its static potential mimics Newton's `1/r` law for the selected probes.

But that tuning is an adjustable scalar charge assignment. It does not follow from the scalar field's spin/gauge consistency, nor does it automatically extend to arbitrary relativistic species, momentum flow, pressure, radiation and stress-tensor components.

For a consistent massless spin-2 mediator, universal coupling is instead tied to Lorentz/gauge invariance of the soft S-matrix.

Thus the stronger gravity-attribution vector contains

`I_gravattr={massless helicity-2,soft factor,universal kappa,T_mn coupling,Ward/gauge identity,contact completion}`.

## Scope and guardrails

This result is strong but scoped.

It does **not** prove that every theory containing a universally coupled spin-2 state is exactly Einstein gravity at all energies.

It does **not** by itself close nonlinear self-interaction, UV completion, quantum loops, causality or experimental identifiability.

It does establish that a candidate long-range massless spin-2 quantum interaction cannot assign independent arbitrary gravitational charges to different matter species while retaining the soft Lorentz/gauge consistency assumptions.

EFT operators may modify subleading/subsubleading soft behavior in controlled ways, while the leading universal spin-2 soft coupling remains the key attribution structure. Modern EFT soft-theorem analyses recover the Einstein equivalence-principle consistency condition.

## F0-F7 terminal map

| Gate | State | Reason |
|---|---|---|
| F0 mediator object | PASS | massless helicity-2 soft S-matrix object explicit |
| F1 long-range/IR limit | PASS | soft pole controls long-range interaction |
| F2 gauge/Lorentz consistency | PASS_SCOPED | soft gauge invariance requires universal coupling |
| F3 observable relation | PASS | soft-emission factor links all matter species/kinematics |
| F4 gravity attribution | **PASS_RQIR_GATE** | arbitrary scalar-charge tuning is replaced by spin-2 universal stress-energy consistency |
| F5 full KG discriminator | DEFERRED | must combine with T3/T4 channel/commutator/relational vector |
| F6/F7 | DEFERRED | no concrete KG dynamics/resources yet |

## Terminal status

`PASS_RQIR_GATE`

objective:

`SPIN2_UNIVERSAL_COUPLING_ATTRIBUTION_ESTABLISHED`.

## Candidate Gravity design lesson

This is a major positive design prior:

> **Gravity attribution should be enforced by consistency, not by fitting a Newtonian potential.**

A future KG parent dynamics should not merely choose couplings proportional to mass. It should derive a universal tensor coupling / Ward identity so that composition and relativistic-source dependence are forced by the same structure that defines its nonclassical channel.

The preferred core vector becomes

`I_KG*={Theta_rel,Q_channel,A_comm,S^-_ij,chi_R,N,helicity2/tensor response,universal T_mn coupling,soft/Ward/contact identities,mediator nulls,QRF invariance}`.

The strongest eventual rigidity test is whether the **same coupling constant and parent dynamics** simultaneously determine

- static/retarded gravitational response;
- quantum-channel strength;
- commutator spectrum;
- soft spin-2 emission/absorption;
- Ward/contact terms across different source species.

## Reopen/extension condition

T5-02 should operationalize the spin/helicity distinction in a source-detector response observable rather than relying only on an S-matrix theorem.

## Terminal completion

**100% — methodological gravity-attribution PASS.**

## Sources

1. S. Weinberg, Phys. Rev. 135, B1049 (1964), soft photon/graviton S-matrix derivation of charge conservation and equality of gravitational/inertial mass.
2. S. Weinberg, Phys. Rev. 138, B988 (1965), perturbative spin-1/spin-2 consistency and Einstein/Maxwell equations.
3. M. P. Hertzberg, M. Sandora, Phys. Rev. D 96, 084048 (2017), universal soft-graviton coupling and relativity from locality/soft gauge invariance.
4. H. Elvang, C. R. T. Jones, S. G. Naculich, Phys. Rev. Lett. 118, 231601 (2017), soft graviton theorems in EFT and equivalence-principle consistency conditions.
