#!/usr/bin/env python3
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOURCES = {
    "lqg": {
        "bcg_causal_vertex_2601_23162": {
            "microscopic_causal_vertex": True,
            "same_realization_area_metric_map": False,
            "parent_rg_transport": False,
            "forest_haar_jet_normalization": False,
        },
        "bcg_toller_2604_24945": {
            "microscopic_causal_vertex": True,
            "same_realization_area_metric_map": False,
            "parent_rg_transport": False,
            "forest_haar_jet_normalization": False,
        },
        "beltran_generalized_2603_22661_v2": {
            "microscopic_causal_vertex": False,
            "same_realization_area_metric_map": False,
            "parent_rg_transport": False,
            "forest_haar_jet_normalization": False,
        },
    },
    "as": {
        "chiesa_pawlowski_reichert_2603_10168": {
            "exchange_amplitude": True,
            "same_realization_A4": False,
            "contact_complete_stable_package": False,
            "full_error_comparator": False,
            "note": "published calculation neglects A4/contact contribution in the evaluated scattering package",
        },
        "knorr_2602_21285": {
            "exchange_amplitude": False,
            "same_realization_A4": False,
            "contact_complete_stable_package": False,
            "full_error_comparator": False,
            "note": "contact information is from a different setup and does not establish the required same-realization package",
        },
    },
    "cfs": {
        "fischer_finster_2605_30199": {
            "curved_spacetime_continuum_limit": True,
            "einstein_dirac_limit": True,
            "explicit_normalized_beyond_gr_correction_tensor": False,
            "full_comparator": False,
        },
        "finster_2109_05906": {
            "curved_spacetime_continuum_limit": False,
            "einstein_dirac_limit": False,
            "explicit_normalized_beyond_gr_correction_tensor": False,
            "full_comparator": False,
        },
    },
}

def lqg():
    cw = (ROOT / "post_freeze_paper_iv_closure_wave_02/README.md").read_text()
    front = (ROOT / "recovery/CURRENT_BENCHMARK_FRONT_ITER330_DELTA.md").read_text()
    assert "C_observable" in cw and "M_same-realization" in cw and "T_RG" in cw
    assert "K5 degree-8 `S5 x O(3)` invariant rank = 16" in front
    allsrc = SOURCES["lqg"]
    out = {
        "iteration": 334,
        "lane": "LQG_MULTISCALE_AND_LOCAL_NORMALIZATION_AUTHORITY",
        "certificate": {
            "C_observable": True,
            "M_same_realization": any(v["same_realization_area_metric_map"] for v in allsrc.values()),
            "T_RG": any(v["parent_rg_transport"] for v in allsrc.values()),
            "source_defined_forest_haar_jet_normalization": any(v["forest_haar_jet_normalization"] for v in allsrc.values()),
        },
        "iter330_detectable_k5_dimension": 16,
        "iter332_minimum_new_information": {"K4_first_jet": 5, "K3_first_jet": 3, "K3_second_jet": 9},
        "classification": "BLOCKED_MISSING_SAME_REALIZATION_RG_AND_SOURCE_DEFINED_LOCAL_NORMALIZATION",
        "scope": "absence in audited authorities is a blocker, not proof of impossibility or family FAIL",
    }
    assert out["certificate"] == {"C_observable": True, "M_same_realization": False, "T_RG": False, "source_defined_forest_haar_jet_normalization": False}
    return out

def asymptotic_safety():
    s = SOURCES["as"]
    out = {
        "iteration": 335,
        "lane": "ASYMPTOTIC_SAFETY_CONTACT_COMPLETE_AUTHORITY",
        "required": ["exchange_amplitude", "same_realization_A4", "contact_complete_stable_package", "full_error_comparator"],
        "available_anywhere": {k: any(v.get(k, False) for v in s.values()) for k in ["exchange_amplitude", "same_realization_A4", "contact_complete_stable_package", "full_error_comparator"]},
        "same_source_terminal_object": False,
        "classification": "BLOCKED_MISSING_STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE",
        "scope": "different-setup contact information cannot be spliced into a same-realization terminal certificate",
    }
    assert out["available_anywhere"]["exchange_amplitude"] is True
    assert out["available_anywhere"]["same_realization_A4"] is False
    return out

def cfs():
    s = SOURCES["cfs"]
    out = {
        "iteration": 336,
        "lane": "CFS_NORMALIZED_CORRECTION_COMPARATOR_AUTHORITY",
        "einstein_dirac_continuum_limit": any(v["einstein_dirac_limit"] for v in s.values()),
        "normalized_beyond_gr_correction_tensor": any(v["explicit_normalized_beyond_gr_correction_tensor"] for v in s.values()),
        "full_comparator": any(v["full_comparator"] for v in s.values()),
        "classification": "BLOCKED_MISSING_FIRST_EXPLICIT_NORMALIZED_CFS_GRAVITY_CORRECTION_TENSOR_PLUS_COMPARATOR",
        "scope": "classical/Einstein-Dirac continuum closure is not a normalized beyond-GR correction object",
    }
    assert out["einstein_dirac_continuum_limit"] is True
    assert out["normalized_beyond_gr_correction_tensor"] is False and out["full_comparator"] is False
    return out

def global_d7():
    d = json.loads((ROOT / "paper_iv/PAPER_IV_D7_READINESS_STATE.json").read_text())
    cov = d["coverage_snapshot"]
    stages = d["stages"]
    assert cov["tier1_total"] == 15
    assert cov["strict_terminal_rows"] == 1
    assert stages["D7-S2"]["status"] == "NOT_CLOSED"
    assert stages["D7-S3"]["status"] == "NOT_CLOSED"
    assert stages["D7-S4"]["status"] == "PARTIAL_GLOBAL_NOT_CLOSED"
    assert stages["D7-S5"]["status"] == "NOT_AUTHORIZED"
    out = {
        "iteration": 337,
        "lane": "GLOBAL_D7_TERMINAL_COVERAGE_GUARD",
        "tier1_total": cov["tier1_total"],
        "strict_terminal_rows": cov["strict_terminal_rows"],
        "strict_nonterminal_rows": cov["strict_nonterminal_rows"],
        "stages": {k: stages[k]["status"] for k in ["D7-S0","D7-S1","D7-S2","D7-S3","D7-S4","D7-S5"]},
        "authorized_outcome": "NOT_AUTHORIZED",
        "candidate_gravity_active": d["metric_separation"]["candidate_gravity_active"],
        "classification": "GLOBAL_LOCK_PRESERVED__NEW_REQUIRED_FORBIDDEN_UNTIL_S2_S3_S4_CLOSE",
    }
    assert out["candidate_gravity_active"] is False
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--mode", required=True, choices=["lqg","as","cfs","global"]); ap.add_argument("--output", required=True)
    a = ap.parse_args()
    result = {"lqg":lqg, "as":asymptotic_safety, "cfs":cfs, "global":global_d7}[a.mode]()
    Path(a.output).write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result, sort_keys=True))
if __name__ == "__main__": main()
