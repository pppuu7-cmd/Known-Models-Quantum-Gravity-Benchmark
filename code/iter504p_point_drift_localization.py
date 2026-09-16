#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path

GATE = "ITER504P_OUT_OF_SAMPLE_POINT_DRIFT_LOCALIZATION_GATE"
PREREG = "77bac4728401200b226dda16447befce85df0c66"
UPSTREAM_RUN = 34907349374
UPSTREAM_HEAD = "56362459a826e3e376c529446678f2fbcaa269ae"
THRESHOLD_DEC = Decimal("0.05")
THRESHOLD_FLOAT = 0.05

WITHIN = "ITER504P_POINT_GRID_DRIFT_WITHIN_FROZEN_TOLERANCE_SCOPED"
VIOLATION = "ITER504P_POINT_GRID_DRIFT_VIOLATION_SCOPED"
INVALID = "ITER504P_POINT_GRID_DRIFT_INVALID"

DECISIVE = (
    "0to5-b1", "0to5-b2", "0to5-b3",
    "1to4-b0", "1to4-b1", "1to4-b2", "1to4-b3",
    "2to3-b0", "2to3-b1", "2to3-b2", "2to3-b3",
)
KNOWN_CONTROL = "0to5-b0"
EXPECTED_PATHS = 4
EXPECTED_AMPLITUDES = 9
EXPECTED_RHOS = 4
EXPECTED_RECORDS_PER_LANE = EXPECTED_PATHS * EXPECTED_AMPLITUDES * EXPECTED_RHOS
EXPECTED_DECISIVE_RECORDS = len(DECISIVE) * EXPECTED_RECORDS_PER_LANE

EXPECTED_ARTIFACT_DIGESTS = {
    "0to5-b0": "a70dbfe331738ae6bf560d49410178aea9d9d4e60d487e476514aec7aca1fa40",
    "0to5-b1": "ceb96d269fcbfb8aa083eb849f373e6347b6ce1e1c3ba575a41364ae3bed91c1",
    "0to5-b2": "bbaea53e3516fa11f257c7bf9bc09e1d31d7980f1f83c0f4b76224b2a9740358",
    "0to5-b3": "45476ce8a96b137f9721b5126217684cdd1559edd1c0c4465202c3c77d59d6b6",
    "1to4-b0": "7bf964d4dfb22f0dbb67b557694d4b6e362c47b6494d0fe9fd352616f9de8fe4",
    "1to4-b1": "3cebcf6003c23b25df133f7fa25be5aacb8d23175f082b616c6f3737659afde9",
    "1to4-b2": "55ab67fe2a13a4c590147bfc0e213a089ef15bdf8df96a1373b7494c41225651",
    "1to4-b3": "38a849c2ef34bbfa529fd60e8302a2029e745546030d49c7c90ccb9aa710f1df",
    "2to3-b0": "af15bc13ccd70a6dd4870f8d71ca364097bf5551406e3d356524f6307a0cb065",
    "2to3-b1": "1f549341d9e7307b01d9b04838253374fbc43117235c44c57b1ac315aa9ad1ff",
    "2to3-b2": "46dbefb97858b2d797ffc7882a02dab24164018dd8ea7a72a114ea06414796ac",
    "2to3-b3": "ccd7e9bf7dd16c9daa74f10ca98cde854f87f0a15842624890723ed0056f9ed2",
}


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical_sha(obj) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256_bytes(raw)


def discover_json(root: Path, lane: str) -> Path:
    expected = f"iter504-point-{lane}.json"
    matches = [p for p in root.rglob(expected) if p.is_file()]
    if len(matches) != 1:
        raise ValueError(f"lane {lane}: expected exactly one {expected}, got {len(matches)}")
    return matches[0]


def load_lane(root: Path, lane: str, method: str):
    path = discover_json(root, lane)
    raw = path.read_bytes()
    if method == "decimal":
        obj = json.loads(raw, parse_float=Decimal)
    else:
        obj = json.loads(raw)
    return obj, path, sha256_bytes(raw)


def validate_lane_header(obj, lane: str):
    causal, block_text = lane.split("-b")
    expected_block = int(block_text)
    checks = {
        "iteration_504": obj.get("iteration") == 504,
        "kind_point_lane": obj.get("kind") == "point_lane",
        "lane_id_exact": obj.get("lane_id") == lane,
        "causal_exact": obj.get("causal") == causal,
        "block_exact": obj.get("block") == expected_block,
        "valid_true": obj.get("valid") is True,
        "path_count": len(obj.get("paths", [])) == EXPECTED_PATHS,
    }
    return checks


def iter_records(obj, lane: str, method: str):
    recs = []
    structure_ok = True
    for p in obj.get("paths", []):
        amps = p.get("amplitudes", [])
        if len(amps) != EXPECTED_AMPLITUDES:
            structure_ok = False
        for amp in amps:
            rhos = amp.get("rho", [])
            if len(rhos) != EXPECTED_RHOS:
                structure_ok = False
            for rho in rhos:
                if method == "decimal":
                    actual = rho["actual_slope"]
                    early = rho["early_actual_slope"]
                    drift = abs(actual - early)
                    within = drift <= THRESHOLD_DEC
                    drift_text = str(drift)
                else:
                    actual = float(rho["actual_slope"])
                    early = float(rho["early_actual_slope"])
                    drift = abs(actual - early)
                    within = drift <= THRESHOLD_FLOAT
                    drift_text = repr(drift)
                recs.append({
                    "lane": lane,
                    "path": p.get("path"),
                    "sign": p.get("sign"),
                    "direction": p.get("direction"),
                    "amplitude": str(amp.get("amplitude")),
                    "rho": str(rho.get("rho")),
                    "actual_slope": str(rho.get("actual_slope")),
                    "early_actual_slope": str(rho.get("early_actual_slope")),
                    "drift": drift_text,
                    "within": within,
                })
    structure_ok = structure_ok and len(recs) == EXPECTED_RECORDS_PER_LANE
    return recs, structure_ok


def drift_num(rec, method):
    return Decimal(rec["drift"]) if method == "decimal" else float(rec["drift"])


def max_locator(rec):
    return {
        "lane": rec["lane"],
        "path": rec["path"],
        "sign": rec["sign"],
        "direction": rec["direction"],
        "amplitude": rec["amplitude"],
        "rho": rec["rho"],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-root", required=True)
    ap.add_argument("--method", choices=("decimal", "float"), required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    if args.method == "decimal":
        getcontext().prec = 80

    root = Path(args.input_root)
    all_records = []
    per_lane = []
    source_json_hashes = {}
    all_structure_ok = True

    for lane in DECISIVE:
        obj, path, json_sha = load_lane(root, lane, args.method)
        header = validate_lane_header(obj, lane)
        recs, rec_structure = iter_records(obj, lane, args.method)
        structure_ok = all(header.values()) and rec_structure
        all_structure_ok &= structure_ok
        source_json_hashes[lane] = json_sha
        all_records.extend(recs)
        lane_max = max(recs, key=lambda r: drift_num(r, args.method)) if recs else None
        per_lane.append({
            "lane": lane,
            "source_json_sha256": json_sha,
            "record_count": len(recs),
            "structure_ok": structure_ok,
            "header_checks": header,
            "violation_count": sum(not r["within"] for r in recs),
            "max_drift": lane_max["drift"] if lane_max else None,
            "max_locator": max_locator(lane_max) if lane_max else None,
        })

    control_obj, _, control_json_sha = load_lane(root, KNOWN_CONTROL, args.method)
    control_header = validate_lane_header(control_obj, KNOWN_CONTROL)
    control_records, control_structure = iter_records(control_obj, KNOWN_CONTROL, args.method)
    control_max = max(control_records, key=lambda r: drift_num(r, args.method))

    decisive_structure = bool(
        all_structure_ok
        and len(all_records) == EXPECTED_DECISIVE_RECORDS
        and set(source_json_hashes) == set(DECISIVE)
    )
    violations = [r for r in all_records if not r["within"]]
    max_rec = max(all_records, key=lambda r: drift_num(r, args.method)) if all_records else None

    if not decisive_structure:
        classification = INVALID
    elif violations:
        classification = VIOLATION
    else:
        classification = WITHIN

    scientific_core = {
        "gate": GATE,
        "classification": classification,
        "preregistration_commit": PREREG,
        "upstream_iter504_run_id": UPSTREAM_RUN,
        "upstream_iter504_head": UPSTREAM_HEAD,
        "threshold": "0.05",
        "decisive_lanes": list(DECISIVE),
        "known_control_lane": KNOWN_CONTROL,
        "known_control_is_decisive": False,
        "decisive_lane_count": len(DECISIVE),
        "expected_records_per_lane": EXPECTED_RECORDS_PER_LANE,
        "expected_decisive_record_count": EXPECTED_DECISIVE_RECORDS,
        "decisive_record_count": len(all_records),
        "decisive_structure_ok": decisive_structure,
        "violation_count": len(violations),
        "max_drift_locator": max_locator(max_rec) if max_rec else None,
        "max_drift_within_threshold": bool(max_rec and max_rec["within"]),
        "known_control_structure_ok": all(control_header.values()) and control_structure,
        "known_control_record_count": len(control_records),
        "known_control_violation_count": sum(not r["within"] for r in control_records),
        "known_control_max_locator": max_locator(control_max),
        "source_json_hashes": source_json_hashes,
        "known_control_json_sha256": control_json_sha,
        "claim_ceiling": "finite frozen Iter504 point-grid drift localization only; no continuous-interval, positive-measure Haar, D7-S2 closure, blocked K5 contact/physical-quotient, selector, model/family or new-physics conclusion",
    }

    out = dict(scientific_core)
    out.update({
        "method": args.method,
        "max_drift": max_rec["drift"] if max_rec else None,
        "max_drift_record": max_rec,
        "per_lane": per_lane,
        "known_control_max_drift": control_max["drift"],
        "known_control_max_record": control_max,
        "expected_artifact_digests": EXPECTED_ARTIFACT_DIGESTS,
        "scientific_payload_sha256": canonical_sha(scientific_core),
    })

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True, ensure_ascii=False))
    return 0 if classification != INVALID else 2


if __name__ == "__main__":
    raise SystemExit(main())
