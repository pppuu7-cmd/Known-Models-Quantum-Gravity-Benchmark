# Iter476 preregistration — Kamiński authority versus Iter470 uniform spectral-decay requirement

Date: 2026-09-13
Status: FROZEN BEFORE IMPLEMENTATION
Parent: current `main` after Iter469–472 recovery.

## Source authority
Primary source: Wojciech Kamiński, *All 3-edge-connected relativistic BC and EPRL spin-networks are integrable*, arXiv:1010.5384.

The source theorem establishes integrability/finiteness of every 3-edge-connected relativistic EPRL spin-network in its labeled spin-network setting. Iter470, however, asks a different question: whether the Iter468 ten-spectral common group kernel admits a source-backed estimate uniform in the simultaneously varying ten spectral labels strong enough for the simple absolute-comparison burden (`c > q+10`, worst sector `c>20`).

## Frozen evidence fields
The audit must distinguish:
1. `fixed_label_integrability_theorem_present` — theorem proving the labeled network integral finite;
2. `ten_spectral_labels_simultaneously_variable_in_iter468` — source object has ten independent spectral variables;
3. `explicit_uniform_in_all_spectral_labels_bound_present` — source explicitly states a bound uniform in simultaneous variation of the relevant representation labels;
4. `explicit_decay_exponent_or_equivalent_strong_enough_for_iter470` — source gives an exponent/anisotropic bound sufficient to imply Iter470's frozen absolute-comparison condition;
5. `causal_toller_kernel_identical_to_the_theorem_integrand_without_extra_work` — an explicit source-backed reduction equating the causal Toller kernel with the theorem's integrand in the needed limit.

## Frozen decision rule
- `KAMINSKI_UNIFORM_SPECTRAL_AUTHORITY_SUFFICIENT_SCOPED` only if fields 1–5 are all positively sourced.
- Otherwise `BLOCKED_KAMINSKI_FIXED_LABEL_FINITE_NOT_YET_UNIFORM_SPECTRAL_BOUND_SCOPED`.

The BLOCKED label means the checked authority is insufficient for Iter470 as stated; it does not mean no such bound can be derived and does not contradict fixed-label finiteness.

## Negative controls
The audit must reject these invalid promotions:
- “finite for every fixed label choice” => “uniformly bounded over unbounded simultaneous label variation”;
- “3-edge-connected graph integral finite” => “causal Toller spectral boundary-value kernel already controlled uniformly”;
- “no explicit uniform exponent found” => “the amplitude diverges.”

## Scope lock
No divergence theorem, no no-go theorem, no D7-S2 closure, no terminal D7 classification. This gate only determines whether the already-checked Kamiński authority by itself closes the Iter470 global spectral-decay requirement.