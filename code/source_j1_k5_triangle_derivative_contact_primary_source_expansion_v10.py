#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, tempfile, urllib.request
from pathlib import Path
from fractions import Fraction

SOURCES = {
    "arXiv:2601.23162v1": "https://arxiv.org/pdf/2601.23162v1",
    "arXiv:2604.24945v1": "https://arxiv.org/pdf/2604.24945v1",
}
TERMS = [
    "renormal", "regular", "normaliz", "counterterm", "extension", "distribution",
    "contact", "gluing", "composition", "projector", "idempot", "scale", "rg",
    "running", "finite part", "scheme", "equivalent", "quotient", "ambigu", "prescription",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower())


def rank(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    if not a:
        return 0
    m, n, r = len(a), len(a[0]), 0
    for c in range(n):
        p = next((i for i in range(r, m) if a[i][c] != 0), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][c]
        a[r] = [x/q for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                q = a[i][c]
                a[i] = [a[i][j] - q*a[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def fetch_pdf(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "KMQGB-source-audit/1.0"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = resp.read()
    if not data.startswith(b"%PDF"):
        raise RuntimeError(f"not PDF: {url}")
    return data


def extract_text(pdf_path: Path, page: int | None = None) -> str:
    cmd = ["pdftotext", "-layout"]
    if page is not None:
        cmd += ["-f", str(page), "-l", str(page)]
    cmd += [str(pdf_path), "-"]
    cp = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return cp.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", required=True)
    ap.add_argument("--v8", required=True)
    ap.add_argument("--v9", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    candidates = json.loads(Path(args.candidates).read_text())
    v8 = json.loads(Path(args.v8).read_text())
    v9 = json.loads(Path(args.v9).read_text())

    controls = {}
    controls["v8_object_lock"] = (
        len(v8.get("basis", [])) == 8
        and v8.get("solve", {}).get("rank") == 2
        and v8.get("solve", {}).get("augmented_rank") == 2
        and v8.get("solve", {}).get("nullity") == 6
    )
    v9d = v9.get("authoritative_decision_projection", {}).get("actual_decision", {})
    controls["v9_parent_blocker_lock"] = (
        v9d.get("classification") == "SOURCE_FINITE_RENORMALIZATION_AUTHORITY_BLOCKED_SCOPED"
        and v9d.get("selector_rank") == 0
        and v9d.get("remaining_affine_nullity") == 6
    )
    controls["exact_frozen_source_set"] = set(SOURCES) == {
        "arXiv:2601.23162v1", "arXiv:2604.24945v1"
    }

    source_records = {}
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        full_texts = {}
        for sid, url in SOURCES.items():
            data = fetch_pdf(url)
            p = td / (sid.replace(":", "_") + ".pdf")
            p.write_bytes(data)
            txt = extract_text(p)
            full_texts[sid] = (p, txt)
            sid_num = sid.split(":", 1)[1]
            version_ok = sid_num.lower() in txt.lower()
            scans = {term: len(re.findall(re.escape(term), txt.lower())) for term in TERMS}
            source_records[sid] = {
                "pdf_url": url,
                "pdf_sha256": sha256_bytes(data),
                "byte_length": len(data),
                "version_marker_present": version_ok,
                "term_scan_counts": scans,
            }
        controls["both_exact_versions_present"] = all(x["version_marker_present"] for x in source_records.values())

        candidate_checks = []
        for rec in candidates["candidate_records"]:
            sid = rec["source_id"]
            page_text = extract_text(full_texts[sid][0], int(rec["pdf_page"]))
            nt = norm(page_text)
            anchors = {tok: norm(tok) in nt for tok in rec["anchor_tokens"]}
            anchor_ok = all(anchors.values())
            computed_actionable = all([
                bool(rec.get("primary")), bool(rec.get("same_realization")), bool(rec.get("explicit")),
                bool(rec.get("mappable_to_v8_affine_freedom")), bool(rec.get("independent_of_v4_v5_v7_v8_v9")),
            ])
            candidate_checks.append({
                "id": rec["id"], "source_id": sid, "page": rec["pdf_page"],
                "selector_category": rec["selector_category"], "anchor_tokens": anchors,
                "page_anchor_verified": anchor_ok,
                "declared_actionable": bool(rec.get("actionable")),
                "computed_actionable": computed_actionable,
                "reason": rec["reason"],
            })

    controls["all_page_anchors_verified"] = all(r["page_anchor_verified"] for r in candidate_checks)
    controls["actionable_flags_consistent"] = all(r["declared_actionable"] == r["computed_actionable"] for r in candidate_checks)
    actual_actionable = [r for r in candidate_checks if r["computed_actionable"]]
    controls["expected_actionable_count"] = len(actual_actionable) == candidates.get("expected_actionable_record_count")

    controls["synthetic_unique_rank6"] = rank([[1 if i == j else 0 for j in range(6)] for i in range(6)]) == 6
    controls["synthetic_partial_rank3"] = rank([[1 if i == j else 0 for j in range(6)] for i in range(3)]) == 3
    controls["synthetic_quotient_rank6"] = rank([[1 if i == j else 0 for j in range(6)] for i in range(6)]) == 6
    a = [[1,0,0,0,0,0],[1,0,0,0,0,0]]
    aug = [row + [rhs] for row, rhs in zip(a, [0,1])]
    controls["synthetic_inconsistent"] = rank(a) < rank(aug)

    controls_pass = all(controls.values())
    if not controls_pass:
        classification = "INVALID_IMPLEMENTATION"
        remaining = None
    elif not actual_actionable:
        classification = "SOURCE_EXPANDED_FINITE_RENORMALIZATION_AUTHORITY_BLOCKED_SCOPED"
        remaining = 6
    else:
        classification = "INVALID_IMPLEMENTATION"
        remaining = None

    decision_projection = {
        "gate": candidates["gate"],
        "classification": classification,
        "controls_pass": controls_pass,
        "actual_actionable_record_ids": [r["id"] for r in actual_actionable],
        "actionable_record_count": len(actual_actionable),
        "remaining_affine_nullity": remaining,
        "pdf_sha256": {sid: rec["pdf_sha256"] for sid, rec in source_records.items()},
    }
    decision_sha256 = hashlib.sha256(json.dumps(decision_projection, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    out = {
        "decision_projection": decision_projection,
        "decision_sha256": decision_sha256,
        "controls": controls,
        "source_records": source_records,
        "candidate_checks": candidate_checks,
        "claim_ceiling": "Full-text audit of exactly arXiv:2601.23162v1 and arXiv:2604.24945v1 for finite-renormalization authority on the terminal V8 local delta-double-prime triangle only; no literature-global absence theorem, distributional existence/nonexistence, full-K5/model/family/D7 selector, or Candidate Gravity authority.",
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"decision_projection": decision_projection, "controls": controls}, sort_keys=True))
    print("decision_sha256=" + decision_sha256)

if __name__ == "__main__":
    main()
