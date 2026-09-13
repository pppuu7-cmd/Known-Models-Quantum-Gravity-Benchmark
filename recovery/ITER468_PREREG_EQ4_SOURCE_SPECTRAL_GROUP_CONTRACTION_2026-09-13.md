# Iter468 preregistration — EQ4 source spectral/group contraction object

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Parent main: `cc7972b01a213b069c8903cc8f29247c96d58321`

## Scientific question
Does direct substitution of the published Toller Feynman spectral representation (Eq. 3 of arXiv:2601.23162) into the published causal vertex (Eq. 4) define an explicit source-faithful correlated spectral/group contraction object without inventing a common spectral variable?

## Source-locked derivation target
For the ten wedges `e=(ab)`, `1<=a<b<=5`, assign one independent spectral variable `rhot_e`. With `rho_e=gamma*j_e`, `k_e=j_e`, and causal sign `kappa_e=sigma_a*sigma_b`, define the source spectral weight

`W_e(rhot_e; eps) = kappa_e/(rhot_e-rho_e-kappa_e*i*eps) * Gamma(-j_e-i*rho_e) Gamma(j_e-i*rhot_e+1) / [Gamma(-j_e-i*rhot_e) Gamma(j_e-i*rho_e+1)]`.

Define the group-contraction kernel

`C({rhot_e}) = int prod_{a=2}^5 dg_a prod_{e=(ab)} D_e^(rhot_e,k_e)(g_b^-1 g_a)`, with `g_1=1`.

The exact formal source object to be reconstructed is

`A_sigma = lim_{eps->0+} int prod_e [drhot_e/(2*pi*i)] prod_e W_e(rhot_e;eps) * C({rhot_e})`.

This is only an algebraic/substitution identity. It does not assert existence of the epsilon limit, Fubini/Tonelli interchange, absolute convergence, or a distributional product theorem.

## Frozen gate streams
A. **Source substitution/counting.** Exactly 10 wedge-local independent spectral variables and exactly 4 unfixed SL(2,C) group integrations after `g1=1`; each spectral variable occurs only in its own Eq.(3) weight and its own Wigner-D representation label before group integration.

B. **Correlation carrier / permutation covariance.** Build the K5 wedge list and verify all 120 S5 relabelings preserve 10 spectral labels, 4 gauge-fixed group variables (after choosing the relabeled root), and the same formal contraction structure. No equality between distinct `rhot_e` may be introduced.

C. **Formal reconstruction.** Programmatically substitute ten Eq.(3)-type factors into the Eq.(4) product and verify that the expression factorizes uniquely into ten spectral weights times one common four-group contraction kernel. The common kernel must depend on all ten `rhot_e` through the ten Wigner-D factors.

D. **Frozen negative controls.** The gate must reject: (i) one shared spectral variable for all wedges; (ii) only 9 wedge spectral variables; (iii) five independent group integrations after gauge fixing; (iv) a contraction kernel with one wedge omitted; (v) an artificial spectral delta/equality constraint not present in Eqs.(3)-(4).

## Interpretation rule
PASS only if every A-D predicate holds exactly. PASS label:

`ITER468_EQ4_SOURCE_SPECTRAL_GROUP_CONTRACTION_OBJECT_PINNED_SCOPED`

If source substitution is internally inconsistent, classify SCIENTIFIC FAIL. If the script/workflow fails before predicates are evaluated, classify INFRASTRUCTURE/NUMERICAL FAIL and repair minimally without changing this preregistration.

## Scope guards
A PASS pins a formal source-faithful contraction object only. It does **not** close D7-S2, prove convergence/finiteness/divergence, justify exchanging integrations, define a non-transversal product, or authorize a D7 terminal classifier. Candidate Gravity remains inactive. The next dependent gate, if PASS, must prospectively test whether the correlated kernel admits a mathematically valid distributional/non-transversal treatment under source-defined variables.