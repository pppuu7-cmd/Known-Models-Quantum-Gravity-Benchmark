#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, sys
from pathlib import Path

PINNED_SHA = "7c749f5f0aeefe07a897123295f3647fdc56d868"
EXPECTED_LINE = "OSCILLATOR_CUTOFF = 8"


def load_variant(root: Path, cutoff: int):
    src = root / "scripts" / "rqcp_unified_qg_common.py"
    text = src.read_text()
    if text.count(EXPECTED_LINE) != 1:
        raise RuntimeError("frozen external source no longer matches expected cutoff declaration")
    patched = text.replace(EXPECTED_LINE, f"OSCILLATOR_CUTOFF = {int(cutoff)}", 1)
    tmp = root / "scripts" / f"_kmqgb_rqcp_cutoff_{int(cutoff)}.py"
    tmp.write_text(patched)
    name = f"rqcp_kmqgb_cutoff_{int(cutoff)}"
    spec = importlib.util.spec_from_file_location(name, tmp)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load patched external module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--external-root", required=True)
    ap.add_argument("--cutoff", required=True, type=int)
    ap.add_argument("--output", required=True)
    a = ap.parse_args()
    if a.cutoff < 4:
        raise ValueError("cutoff stress domain is cutoff>=4")
    root = Path(a.external_root).resolve()
    mod = load_variant(root, a.cutoff)
    geo = mod.spectral_geometry_data(None, mod.CONTINUUM_REGULATOR)
    source = mod.source_response(None, mod.CONTINUUM_REGULATOR)
    ucp = mod.ucp_data(None, mod.CONTINUUM_REGULATOR)
    out = {
        "iteration": 343,
        "external_repository": "Amordia/rqcp-toward-quantum-gravity",
        "external_scientific_payload_sha": PINNED_SHA,
        "variation": "local Hilbert oscillator cutoff only",
        "fixed_physical_band": "{0, unit-x}",
        "cutoff": a.cutoff,
        "hilbert_dimension": int(a.cutoff * a.cutoff),
        "direct_continuum_spatial_symbol": 1.0,
        "metrics": {
            "ground_energy": geo["ground_energy"],
            "mass_gap": geo["mass_gap"],
            "connected_static_four_response": source["connected_static_four_response"],
            "mixed_geometry_matter_response": source["mixed_geometry_matter_response"],
            "geometry_kinetic_coefficient_B": geo["geometry_kinetic_coefficient_B"],
            "Newton_response_G": geo["Newton_response_G"],
            "dimensionless_gravity_number_G_gap2": geo["dimensionless_gravity_number_G_gap2"],
            "unitarity_CPTP_completeness_residual": ucp["unitarity_CPTP_completeness_residual"],
        },
        "scope_guard": [
            "EXTERNAL_CODE_PINNED_TO_FROZEN_SCIENTIFIC_PAYLOAD_SHA",
            "ONLY_OSCILLATOR_CUTOFF_IS_CHANGED_BEFORE_MODULE_IMPORT",
            "SPATIAL_BAND_REMAINS_FIXED_TWO_MODE",
            "NO_ALL_BAND_QFT_CLAIM",
            "NO_PARENT_FAMILY_TERMINALIZATION",
            "NO_D7_PROMOTION"
        ]
    }
    Path(a.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, sort_keys=True))

if __name__ == "__main__":
    main()
