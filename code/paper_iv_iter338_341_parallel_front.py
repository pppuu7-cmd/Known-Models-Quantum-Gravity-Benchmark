#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from decimal import Decimal, getcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
getcontext().prec = 80

TERMINAL = {
    "BENCHMARKED_COMPLETE_REALIZATION",
    "EQUIVALENCE_CLASS_CLOSED_BY_THEOREM",
    "MERGED_INTO_OTHER_ROW_WITH_EXPLICIT_REDUCTION_MAP",
    "OUTSIDE_PAPER_IV_TARGET_WITH_SCOPE_PROOF",
}

# Conservative prospective classification of the *next gate*, not of theory truth.
# COMPUTE_ELIGIBLE means repository mathematics can materially sharpen a scoped gate now;
# it never means the parent family can be terminalized without the family-scope contract.
NEXT_ROUTE = {
    "PERTURBATIVE_HIGHER_DERIVATIVE": "MIXED_COMPUTE_AND_SOURCE__FAKEON_BEYOND_LEADING_OR_CAUSAL_RESPONSE_PLUS_BRANCH_DISPOSITION",
    "HORAVA_LIFSHITZ": "SOURCE_AND_REDUCTION_OBJECT__PROJECTABLE_UV_TO_IR_TRAJECTORY_PLUS_NONPROJECTABLE_DISPOSITION",
    "ASYMPTOTIC_SAFETY": "SOURCE_OBJECT_MISSING__CONTACT_COMPLETE_SAME_REALIZATION_A4_COMPARATOR",
    "NONLOCAL_QG": "COMPUTE_ELIGIBLE__CROSS_ORDER_FUNCTIONAL_RIGIDITY_THEN_FULL_MOMENTUM_PHYSICAL_AMPLITUDE_CERTIFICATE",
    "STRING_MTHEORY_HOLOGRAPHY": "FAMILY_SCOPE_REDUCTION_MAP__MATERIAL_SUBFAMILY_EXHAUSTION",
    "CAUSAL_SETS": "SOURCE_OBJECT_MISSING__DYNAMICS_TO_EMERGENT_MANIFOLD_NORMALIZED_GRAVITY_OBSERVABLE",
    "CDT_EDT": "SOURCE_DATA_AND_CONTINUUM_MAP__4D_RG_TRAJECTORY_LATTICE_SPACING_OBSERVABLE_ERRORS",
    "LQG_SPINFOAM": "SOURCE_OBJECT_MISSING__FOREST_HAAR_NORMALIZATION_AND_SAME_REALIZATION_RG_TRANSPORT",
    "GFT_TENSOR_MODELS": "REDUCTION_MAP_OR_INDEPENDENT_GRAVITY_OBSERVABLE__GFT_TO_SPINFOAM_EQUIVALENCE",
    "CFS": "SOURCE_OBJECT_MISSING__NORMALIZED_BEYOND_GR_CORRECTION_TENSOR_COMPARATOR",
    "NONCOMMUTATIVE_SPECTRAL_GEOMETRY": "SOURCE_OBJECT_MISSING__QUANTUM_DYNAMICS_MEASURE_AND_NORMALIZED_QG_OBSERVABLE",
    "CANONICAL_WDW_GEOMETRODYNAMICS": "SOURCE_OBJECT_MISSING__PHYSICAL_INNER_PRODUCT_CLOCK_DIRAC_OBSERVABLE_SEMICLASSICAL_MAP",
    "QUANTUM_GRAPHITY": "SOURCE_OBJECT_MISSING__CONNECTED_LOW_ENERGY_LORENTZIAN_SPIN2_GR_PHASE_OBSERVABLE",
    "RELATIONAL_QUANTUM_CAUSAL_PROCESSES": "MIXED_COMPUTE_AND_SOURCE__ALL_BAND_AUTONOMY_PLUS_HILBERT_CUTOFF_RESOURCE_CLOSURE",
}

def coverage_scan() -> dict:
    p = json.loads((ROOT / "protocol/PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json").read_text())
    rows = p["tier1_required_rows"]
    assert len(rows) == 15
    outrows = []
    counts = {"terminal":0,"compute_eligible":0,"mixed":0,"source_or_reduction":0}
    for r in rows:
        status = r["coverage_status"]
        if status in TERMINAL:
            route = "ALREADY_TERMINAL"
            bucket = "terminal"
        else:
            route = NEXT_ROUTE[r["id"]]
            if route.startswith("COMPUTE_ELIGIBLE"):
                bucket = "compute_eligible"
            elif route.startswith("MIXED_COMPUTE"):
                bucket = "mixed"
            else:
                bucket = "source_or_reduction"
        counts[bucket] += 1
        outrows.append({"id":r["id"],"coverage_status":status,"next_route":route,"bucket":bucket})
    assert counts["terminal"] == 1
    assert counts["compute_eligible"] >= 1
    assert counts["mixed"] >= 2
    return {
        "iteration":338,
        "mode":"tier1_terminalization_opportunity_scan",
        "tier1_total":15,
        "counts":counts,
        "rows":outrows,
        "priority_compute_fronts":["NONLOCAL_QG","PERTURBATIVE_HIGHER_DERIVATIVE","RELATIONAL_QUANTUM_CAUSAL_PROCESSES"],
        "classification":"PASS_SCOPED_TERMINALIZATION_ROUTE_TRIAGE__COMPUTE_ONLY_WHERE_GATE_HAS_INTERNAL_MATHEMATICAL_CONTENT",
        "scope_guard":"Route triage is not theory exclusion, family terminalization, or D7 authorization. Missing source/reduction objects remain BLOCKED rather than FAIL.",
    }

def exp_form(x: Decimal) -> Decimal:
    return (-x).exp()

def forward_difference(values: list[Decimal]) -> Decimal:
    cur = values[:]
    while len(cur) > 1:
        cur = [cur[i+1]-cur[i] for i in range(len(cur)-1)]
    return cur[0]

def nonlocal_rigidity() -> dict:
    # Mathematical proxy for an entire weakly-nonlocal form factor F(z)=exp(-z).
    # Any degree-n local finite-derivative comparator polynomial has vanishing
    # (n+1)-st equal-step forward difference. F does not. This closes only a
    # cross-order functional-rigidity witness, not a physical amplitude certificate.
    probes=[]
    for n in (2,4,6,8,12):
        for hs in ("0.05","0.1","0.25","0.5"):
            h=Decimal(hs)
            vals=[exp_form(h*Decimal(k)) for k in range(n+2)]
            d=forward_difference(vals)
            analytic=(exp_form(h)-Decimal(1))**Decimal(n+1)
            rel=abs(d-analytic)/max(abs(analytic),Decimal("1e-70"))
            assert d != 0
            assert rel < Decimal("1e-60")
            probes.append({"degree":n,"h":hs,"forward_difference":str(d),"analytic":str(analytic),"relative_identity_error":str(rel)})
    return {
        "iteration":339,
        "mode":"nonlocal_cross_order_functional_rigidity",
        "form_factor":"F(z)=exp(-z)",
        "tested_local_polynomial_degrees":[2,4,6,8,12],
        "probe_count":len(probes),
        "all_nonzero_nplus1_forward_differences":True,
        "probes":probes,
        "classification":"PASS_SCOPED_NONLOCAL_CROSS_ORDER_FUNCTIONAL_RIGIDITY_WITNESS__FINITE_LOCAL_DERIVATIVE_POLYNOMIALS_CANNOT_EQUAL_DECLARED_ENTIRE_FORM_FACTOR_ON_EQUAL_STEP_GRID",
        "global_effect":"NONLOCAL_QG_REMAINS_PARTIAL_SUBFAMILY_ONLY",
        "next_gate":"PHYSICAL_RIEMANN_WEYL_FULL_MOMENTUM_NORMALIZED_AMPLITUDE_VECTOR_PLUS_IDENTICAL_ORDER_GR_LOCAL_HIGHER_CURVATURE_EFT_COMPARATOR_QUOTIENT",
        "scope_guard":"This is an exact functional-shape witness for the declared entire form factor, not the missing source-normalized graviton amplitude, not a family-wide theorem, and not D7 closure.",
    }

def higher_derivative_branch_audit() -> dict:
    m=json.loads((ROOT / "paper_iv/HIGHER_DERIVATIVE_QUANTIZATION_BRANCH_MAP_2026-09-10.json").read_text())
    branches=m["material_branches"]
    assert len(branches)==5
    terminal=sum(bool(b["terminal"]) for b in branches)
    blockers={b["id"]:b["blocker"] for b in branches}
    assert terminal==0
    fakeon=next(b for b in branches if b["id"]=="FAKEON_AVERAGE_CONTINUATION")
    assert "normalized observable/comparator" in fakeon["blocker"]
    return {
        "iteration":340,
        "mode":"higher_derivative_material_branch_closure_gap",
        "material_branch_count":len(branches),
        "terminal_branch_count":terminal,
        "nonterminal_branch_count":len(branches)-terminal,
        "blockers":blockers,
        "fakeon_leading_r_nt_already_nonidentifying":True,
        "classification":"PASS_SCOPED_BRANCH_EXHAUSTION_GUARD__0_OF_5_MATERIAL_QUANTIZATION_BRANCHES_TERMINAL__NO_PARENT_PROMOTION",
        "next_gate":"FAKEON_BEYOND_LEADING_INFLATION_OR_SAME_REALIZATION_CAUSAL_RESPONSE_COMPARATOR_CERTIFICATE_WHILE_OTHER_BRANCHES_REMAIN_SEPARATELY_UNRESOLVED",
        "scope_guard":"Counting open material branches is a closure audit, not evidence that any branch is false.",
    }

def authority_coherence() -> dict:
    old=json.loads((ROOT / "paper_iv/PAPER_IV_FROZEN_CORE_DECISION_LEDGER.json").read_text())
    cov=json.loads((ROOT / "protocol/PAPER_IV_MAJOR_FRAMEWORK_COVERAGE_CONTRACT.json").read_text())
    d7=json.loads((ROOT / "paper_iv/PAPER_IV_D7_READINESS_STATE.json").read_text())
    oldn=old["framework_coverage"]["tier1_required_rows"]
    newn=cov["current_coverage_summary"]["tier1_rows"]
    d7n=d7["coverage_snapshot"]["tier1_total"]
    assert oldn==14 and newn==15 and d7n==15
    rqcp=[r for r in cov["tier1_required_rows"] if r["id"]=="RELATIONAL_QUANTUM_CAUSAL_PROCESSES"]
    assert len(rqcp)==1
    return {
        "iteration":341,
        "mode":"authority_coherence_supersession_audit",
        "historical_decision_ledger_tier1":oldn,
        "current_coverage_contract_tier1":newn,
        "current_d7_readiness_tier1":d7n,
        "new_row":"RELATIONAL_QUANTUM_CAUSAL_PROCESSES",
        "classification":"PASS_SCOPED_STALE_DENOMINATOR_DETECTED__CURRENT_15_ROW_COVERAGE_CONTRACT_AND_D7_READINESS_SUPERSEDE_HISTORICAL_14_ROW_LEDGER_FOR_DENOMINATOR_COUNTS",
        "global_effect":"NO_D7_STATUS_CHANGE__USE_15_ROW_DENOMINATOR",
        "scope_guard":"The old ledger is retained as historical authority; this audit prevents accidental reuse of its obsolete 14-row denominator.",
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--mode",required=True,choices=["scan","nonlocal","higher_derivative","coherence"]); ap.add_argument("--output",required=True)
    a=ap.parse_args()
    f={"scan":coverage_scan,"nonlocal":nonlocal_rigidity,"higher_derivative":higher_derivative_branch_audit,"coherence":authority_coherence}[a.mode]
    result=f(); Path(a.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n"); print(json.dumps(result,sort_keys=True))
if __name__=="__main__": main()
