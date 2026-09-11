#!/usr/bin/env python3
from pathlib import Path
import json

run_id="34614776339"
methodology_run="34614776311"
scientific_head="d2238ee1e3e43b16ec550a49317c2aab459fdc01"
summary_artifact="10269418152"
artifact_digest="sha256:0cf3f16acf0a00211ef4cb55f009a5eaff296903b6ed6b38d2718bbedc4a662f"
raw_summary_digest="sha256:b638c92c7790f660a14d64410eda2c699a7589a73aebc12e5ce3058061095acf"
classification="PASS_SCOPED_FIXED_SPIN_TOLLER_BLOCK_SU2_HAAR_HALF_LINK_GLUE_COMPATIBILITY__SCHUR_CONTRACTION_SURVIVES_WITHOUT_SL2C_BRANCH_REPRESENTATION_LAW__CAUSAL_VERTEX_FINITE_NORMALIZATION_STACK_CUTOFF_AND_UV_IR_TRANSPORT_REMAIN_OPEN"
blocker="BLOCKED_MISSING_FINITE_NORMALIZED_GENERALIZED_CAUSAL_VERTEX_AND_LAMBDA_F_WEIGHTED_COMPLETE_STACK_FINITE_NORMALIZATION_AREA_CUTOFF_REMOVAL_PLUS_SAME_REALIZATION_UV_TO_CAUSAL_LARGE_SPIN_REGGE_GR_TRANSPORT_WITH_PARAMETER_IDENTITY_NORMALIZED_OBSERVABLE_COMMON_DOMAIN_COMPARATOR_AND_PROPAGATED_ERROR"
next_gate="D7_S2_LQG_GENERALIZED_CAUSAL_VERTEX_FINITE_NORMALIZATION_AND_LAMBDA_F_WEIGHTED_COMPLETE_STACK_CUTOFF_CONTROL__THEN_SAME_REALIZATION_UV_TO_CAUSAL_REGGE_GR_TRANSPORT"

Path('paper_iv').mkdir(exist_ok=True)
Path('recovery').mkdir(exist_ok=True)

audit=Path('paper_iv/P_LQG_TOLLER_SU2_HAAR_HALF_LINK_GLUE_AUDIT_ITER303_2026-09-11.md')
if not audit.exists():
    audit.write_text(f'''# Paper IV LQG Toller SU(2)-Haar Half-Link Glue Audit — Iter303

Date: 2026-09-11

## Authority and frozen scope
Primary objects: Han, *Summation and triangulation independence of Lorentzian spinfoam amplitudes for all LQG*, PRD 113, 084034 (2026); Bianchi–Chen–Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, arXiv:2604.24945 (2026); and the causal gamma-simple Toller vertex construction of arXiv:2601.23162 (2026).

The prospectively frozen contract is `benchmarks/lqg_iter303_toller_su2_haar_glue.json`. The question is narrower than Iter302: although a fixed Toller branch is not an `SL(2,C)` representation, does Han's *SU(2) boundary Haar/Schur contraction* still act on the matching finite magnetic-index spaces?

## Machine result
Scientific run `{run_id}` on exact head `{scientific_head}`: five independent probes ran with `fail-fast:false`, `max-parallel:5`; aggregate executed only after all probes succeeded.

Independent probes:
1. source/covariance contract;
2. exact Schur-Haar contraction;
3. mismatched-spin orthogonality;
4. branch bilinearity/cross-term contraction;
5. fail-closed scope guard.

All five probes plus aggregate = SUCCESS. Methodology run `{methodology_run}` = preflight + 4/4 shards + aggregate/bundle SUCCESS.

Summary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw summary digest `{raw_summary_digest}`.

Exact machine facts:
- fixed-spin Toller SU(2)-Haar half-link glue compatibility = true;
- exact Schur contraction checked for dimensions `d=1..6`;
- 49 spin channels checked; all 42 mismatched channels vanish;
- branch bilinearity checked independently for `d=2,3,4,5`;
- a fixed Toller branch remains *not* an `SL(2,C)` group representation;
- generalized causal-vertex finiteness = not proven;
- `lambda_f`-weighted causal complete-stack finiteness/normalization/cutoff control = not proven;
- same-realization UV→causal-Regge/GR transport = not proven;
- family terminal = false; D7 authorized = false.

## Frozen classification
`{classification}`

## Interpretation
Iter302 correctly forbade silently inheriting the ordinary `SL(2,C)` representation-composition law branchwise. Iter303 shows that this does **not** obstruct the separate SU(2)-Haar/Schur boundary contraction used in Han's half-link gluing: the contraction is an index-space orthogonality identity and survives at fixed matched spin without requiring the Toller branch itself to be an `SL(2,C)` representation.

This removes one sub-blocker only. It is not a finiteness proof for the generalized causal vertex, not a proof of the finite normalized `lambda_f`-weighted complete-stack amplitude or cutoff removal, and not the same-realization UV→IR observable/error certificate.

## Current blocker
`{blocker}`
''',encoding='utf-8')

decision=Path('paper_iv/PAPER_IV_DECISION_LEDGER_DELTA_303.json')
if not decision.exists():
    decision.write_text(json.dumps({
        'iteration':303,'family':'LQG_SPINFOAM','scientific_run':int(run_id),
        'scientific_head':scientific_head,'methodology_run':int(methodology_run),
        'summary_artifact':int(summary_artifact),'artifact_digest':artifact_digest,
        'raw_summary_digest':raw_summary_digest,'classification':classification,
        'fixed_spin_toller_su2_haar_half_link_glue_compatible':True,
        'exact_schur_dimensions_tested':[1,2,3,4,5,6],
        'spin_channels_checked':49,'mismatched_spin_channels_zero':42,
        'branch_bilinearity_dimensions_tested':[2,3,4,5],
        'fixed_toller_branch_sl2c_representation':False,
        'causal_vertex_finiteness_proven':False,
        'lambda_f_weighted_causal_stack_finiteness_normalization_cutoff_control_proven':False,
        'same_realization_uv_to_causal_regge_gr_transport_proven':False,
        'family_terminal':False,'d7_authorized':False,
        'terminal_count':'1/15','candidate_terminal_count':'0/14'
    },indent=2,sort_keys=True)+'\n',encoding='utf-8')

recovery=Path('recovery/RECOVERY_DELTA_303.md')
if not recovery.exists():
    recovery.write_text(f'''# Recovery Delta 303 — Toller SU(2)-Haar half-link glue

- Scientific head `{scientific_head}`.
- Scientific run `{run_id}`: 5/5 independent probes + aggregate SUCCESS.
- Methodology run `{methodology_run}`: preflight + 4/4 shards + aggregate/bundle SUCCESS.
- Summary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw digest `{raw_summary_digest}`.
- Result: `{classification}`.
- Formal fixed-spin Han half-link SU(2)-Haar/Schur glue compatibility is now scoped PASS despite the fixed Toller branch not being an `SL(2,C)` representation.
- Remaining required objects: finite normalized generalized causal vertex, `lambda_f`-weighted complete-stack normalization and controlled area-cutoff removal, then same-realization UV→causal-Regge/GR parameter/observable/comparator/error transport.
- Global D7 state unchanged: strict terminal `1/15`, candidate terminal `0/14`, D7 unauthorized, Candidate Gravity inactive at R3=24%.
- Paper III: NOT_NEEDED. Paper IV: READY.
''',encoding='utf-8')

ledger=Path('recovery/PUBLICATION_IMPACT_LEDGER.md')
text=ledger.read_text(encoding='utf-8')
if '## Iter303 — Toller SU(2)-Haar half-link glue compatibility' not in text:
    marker='\n## Standing rule\n'
    if marker not in text: raise SystemExit('fail-closed: Standing rule marker absent')
    block=f'''\n## Iter303 — Toller SU(2)-Haar half-link glue compatibility
### Paper III — `NOT_NEEDED`
- **Type:** theory-specific exact algebraic/evidentiary refinement; no new general resource-closure rule beyond Iter277.
### Paper IV — `READY`
- Add the distinction between missing `SL(2,C)` branch representation composition (Iter302) and the separate fixed-spin SU(2)-Haar/Schur boundary gluing identity used by Han.
- Report 5/5 independent probes + aggregate SUCCESS; exact Schur contraction on dimensions `1..6`, 49 spin-channel checks with all 42 mismatched channels zero, and branch-bilinearity checks on dimensions `2..5`.
- State that formal fixed-spin Toller half-link gluing is compatible with Han's SU(2) Haar contraction even though a fixed Toller branch is not an `SL(2,C)` representation.
- **Required boundary:** generalized causal-vertex finiteness, finite normalized `lambda_f`-weighted complete-stack amplitude/cutoff removal, and same-realization UV→causal-Regge/GR observable/error transport remain unproven. No family promotion and D7 remains unauthorized.
- Result: `{classification}`.
- Provenance: scientific `{run_id}`; scientific head `{scientific_head}`; methodology `{methodology_run}`; summary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw summary digest `{raw_summary_digest}`.
'''
    ledger.write_text(text.replace(marker,block+marker),encoding='utf-8')

front=Path('recovery/CURRENT_BENCHMARK_FRONT.md')
text=front.read_text(encoding='utf-8')
lines=text.splitlines()
if len(lines)<3: raise SystemExit('fail-closed: malformed front')
lines[2]='Iteration: Iter303 fixed-spin Toller SU(2)-Haar half-link glue compatibility validated; Iter302 branch-composition scope retained'
text='\n'.join(lines)+'\n'
if '### Iter303 — fixed-spin Toller SU(2)-Haar half-link glue' not in text:
    marker='\n## Infrastructure note\n'
    if marker not in text: raise SystemExit('fail-closed: Infrastructure note marker absent')
    block=f'''\n### Iter303 — fixed-spin Toller SU(2)-Haar half-link glue
Contract: `benchmarks/lqg_iter303_toller_su2_haar_glue.json`.
Scientific run `{run_id}` on exact head `{scientific_head}`: five independent probes in parallel plus aggregate SUCCESS. Methodology `{methodology_run}`: SUCCESS. Summary artifact `{summary_artifact}`; artifact digest `{artifact_digest}`; raw summary digest `{raw_summary_digest}`.

Machine result: fixed-spin Toller SU(2)-Haar half-link glue compatibility = PASS; exact Schur contraction dimensions `1..6`; 49 spin channels checked with 42 mismatched channels zero; branch bilinearity dimensions `2..5`; fixed Toller branch remains not an `SL(2,C)` representation.

Classification: `{classification}`.

Boundary: causal-vertex finiteness, `lambda_f`-weighted complete-stack finite normalization/cutoff removal, and same-realization UV→causal-Regge/GR transport remain open. No family promotion; D7 remains unauthorized.
'''
    text=text.replace(marker,block+marker)

import re
text=re.sub(r'Current blocker:\n`[^`]+`',f'Current blocker:\n`{blocker}`',text)
text=re.sub(r'Exact next permitted gate:\n`[^`]+`',f'Exact next permitted gate:\n`{next_gate}`',text)
front.write_text(text,encoding='utf-8')
