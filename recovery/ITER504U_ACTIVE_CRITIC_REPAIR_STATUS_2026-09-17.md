# Active Iter504U Critic-repair status

Date: 2026-09-17

## Active source science run

Run `35246605860`, head `102c7f9cafec956f3bc7bed4384ae755c98f761a`.

Source-lock is terminal success. Producer jobs are still completing. No duplicate producer run is authorized.

## Outcome-blind defect found before terminal science consumption

The originally frozen Critic control `C4_true_leaf_false_rho` is outcome-dependent: it only forces one serialized `per_rho.certified` bit false and therefore is not guaranteed to create a C4 contradiction if the baseline leaf/rho is already false.

Repair preregistration:

`5ad9664e88e517cd64bd9971bac5c4c239ba4672`

The defect is synthetic-Critic-only. Producer evaluator, held-out cohort, source realization, threshold, floor, precision, R/rho grids, channels, MAX_DEPTH, partition, local-D construction and scientific PASS/INCONCLUSIVE rules are unchanged.

## Frozen repair

Repair wrapper commit:

`3dadd0aa18bcac46366b1210f51ce678d06c6734`

Wrapper blob:

`ff82b1dee8c26788083ad2ac6aff46c96040305c`

The wrapper imports frozen Critic blob `c2a7ea31ddc151bf02a3995d761cae95bdabd0db` and replaces only the negative-control constructor. Its deterministic C4 fixture forces all rho rows into a self-consistent certified state, then makes exactly one rho self-consistently uncertified while keeping the leaf top-level certified, guaranteeing violation of `leaf.certified == all(per_rho.certified)` independent of baseline science.

Methodology run `35250463093` is terminal `completed/success`; its self-test covers baseline leaf true/false and selected-rho true/false.

## Authority rule

The original Critic result from source run `35246605860`, whether green or not, is **not sufficient by itself** for terminal scientific authority because its synthetic C4 fixture is outcome-dependent.

No producer rerun is authorized for this defect.

Prepared closure-only workflow:

- commit `101a4e02867b0702fc8ecdd114c1d02678a7478d`;
- workflow blob `6dc053c06402b31f17ebef1c34b6444c1cb31fe2`.

After the source run is terminal and its required 15 upstream artifacts exist, closure authority must prospectively freeze their exact artifact IDs/digests without inspecting science values, then execute repaired Critic review independently under Python 3.11/3.13 against those exact immutable artifacts. Only that repaired closure may terminalize Iter504U science.

## Current artifact metadata consumed

Only artifact metadata, not scientific JSON payloads, has been consumed while the source run is nonterminal. At this record point both H3 producer artifacts exist and are tied to source head `102c7f9cafec956f3bc7bed4384ae755c98f761a`; their science content has not been used to alter any criterion.

## Claim ceiling

`INCONCLUSIVE != FAIL`; implementation/critic invalidity != scientific failure. No all-domain, D7, model/family, selector, Candidate Gravity, Paper IV or global quantum-gravity claim is authorized.
