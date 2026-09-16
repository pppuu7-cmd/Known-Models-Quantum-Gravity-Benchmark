#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

BLOCKED = "EQ4_PHYSICAL_TRANSVERSE_QUOTIENT_PRIMARY_AUTHORITY_BLOCKED_SCOPED"
INVALID = "EQ4_PHYSICAL_TRANSVERSE_QUOTIENT_PRIMARY_AUTHORITY_INVALID"


def load(root):
    fs = sorted(Path(root).rglob("*.json"))
    if len(fs) != 1:
        raise SystemExit(f"expected one json in {root}, got {len(fs)}")
    return json.loads(fs[0].read_text()), hashlib.sha256(fs[0].read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--primary", required=True)
    ap.add_argument("--critic", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    p, hp = load(a.primary)
    c, hc = load(a.critic)
    keys = [
        "gate", "classification", "required_fields", "minimal_blocker", "source_search_status",
        "published_version_fulltext_auditable", "strong_absence_claim_authorized",
        "physical_transverse_rank", "downstream_physical_projection_authorized", "claim_ceiling", "fixtures",
        "scientific_payload_sha256",
    ]
    agree = all(p.get(k) == c.get(k) for k in keys)
    expected = bool(
        p.get("classification") == BLOCKED
        and p.get("minimal_blocker") == "PUBLISHED_VERSION_FULLTEXT_AUTHORITY_ACCESS_CEILING"
        and p.get("physical_transverse_rank") is None
        and p.get("published_version_fulltext_auditable") is False
        and p.get("strong_absence_claim_authorized") is False
        and p.get("downstream_physical_projection_authorized") is False
        and all(v == "NOT_ESTABLISHED" for v in p.get("required_fields", {}).values())
    )
    cls = BLOCKED if agree and expected else INVALID
    out = {
        "gate": p.get("gate"),
        "classification": cls,
        "independent_source_lanes_agree": agree,
        "primary_lane_json_sha256": hp,
        "critic_lane_json_sha256": hc,
        "scientific_payload_sha256": p.get("scientific_payload_sha256") if agree else None,
        "required_fields": p.get("required_fields"),
        "minimal_blocker": p.get("minimal_blocker"),
        "source_search_status": p.get("source_search_status"),
        "published_version_fulltext_auditable": p.get("published_version_fulltext_auditable"),
        "strong_absence_claim_authorized": p.get("strong_absence_claim_authorized"),
        "physical_transverse_rank": p.get("physical_transverse_rank"),
        "downstream_physical_projection_authorized": False,
        "claim_ceiling": p.get("claim_ceiling"),
    }
    raw = json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
    out["aggregate_sha256"] = hashlib.sha256(raw).hexdigest()
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if cls != INVALID else 2


if __name__ == "__main__":
    raise SystemExit(main())
