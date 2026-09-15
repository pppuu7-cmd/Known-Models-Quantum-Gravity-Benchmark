#!/usr/bin/env python3
"""Outcome-sensitive source-authority extraction for the frozen j=1 K5 contact bridge.

No conclusion-bearing repository booleans/nulls are consumed. The actual outcome is derived
from a complete frozen Git-tree corpus selected by preregistered path globs and parsed into
semantic sections. Synthetic controls use the same extractor/classifier.
"""
from __future__ import annotations
import argparse, fnmatch, hashlib, json, re, subprocess
from fractions import Fraction
from pathlib import Path

CORPUS_SHA = "e7c2546236fea1b6913a253fc354efc769dc544a"
SELECTORS = [
    "research/SOURCE_J1*.md",
    "research/prereg/SOURCE_J1*.md",
    "code/source_j1*.py",
    "inputs/source_j1*.json",
    "recovery/CRITICAL_REVIEW_SOURCE_J1*.md",
]
PRELOAD_RE = re.compile(r"(?im)^.*(?:actual_[a-z0-9_]*\s*=|source_pinned\s*=|terminal\s+classification).*?$", re.M)


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).rstrip("\n")


def corpus_paths() -> list[str]:
    names = git("ls-tree", "-r", "--name-only", CORPUS_SHA).splitlines()
    return sorted(p for p in names if any(fnmatch.fnmatchcase(p, g) for g in SELECTORS))


def blob_sha(path: str) -> str:
    return git("rev-parse", f"{CORPUS_SHA}:{path}")


def source_text(path: str) -> str:
    return git("show", f"{CORPUS_SHA}:{path}")


def strip_conclusion_preloads(text: str) -> str:
    return PRELOAD_RE.sub("", text)


def split_records(path: str, text: str) -> list[dict]:
    text = strip_conclusion_preloads(text)
    if path.endswith(".md"):
        parts = re.split(r"(?m)^(#{1,6}\s+.+)$", text)
        out, heading, body = [], "<preamble>", parts[0]
        if body.strip(): out.append({"heading": heading, "text": body})
        for i in range(1, len(parts), 2):
            heading = parts[i].strip()
            body = parts[i+1] if i+1 < len(parts) else ""
            out.append({"heading": heading, "text": body})
        return out
    if path.endswith(".json"):
        try:
            obj = json.loads(text)
            return [{"heading": "<json>", "text": json.dumps(obj, sort_keys=True)}]
        except Exception:
            return [{"heading": "<json-invalid>", "text": text}]
    # Python: module plus top-level def/class blocks; enough to expose exact equations/comments.
    starts = [m.start() for m in re.finditer(r"(?m)^(?:def|class)\s+\w+", text)]
    if not starts: return [{"heading": "<python>", "text": text}]
    out = [{"heading": "<python-preamble>", "text": text[:starts[0]]}]
    for i, s in enumerate(starts):
        e = starts[i+1] if i+1 < len(starts) else len(text)
        line = text[s:text.find("\n", s) if "\n" in text[s:] else e]
        out.append({"heading": line.strip(), "text": text[s:e]})
    return out


def has(pat: str, s: str) -> bool:
    return re.search(pat, s, re.I | re.S) is not None


def features(text: str) -> dict:
    s = re.sub(r"\s+", " ", text)
    coherent = has(r"(?:coherent|spinor).{0,180}(?:delta\s*\^?\(?\s*rho|delta\s*''|theta|B\s*\(\s*z\s*,\s*g)|contact)|(?:delta\s*''|delta\s*\^?\(?\s*rho).{0,180}(?:coherent|spinor|B\s*\()", s)
    magnetic = has(r"(?:D\s*\^?\s*1|magnetic|spherical\s+basis|m\s*=\s*[+\-]?1|rank[- ]?2\s+(?:tensor|operator)|matrix\s+operator|intertwiner)", s)
    rho = has(r"rho", s) and has(r"(?:real\s+nonzero|nonzero\s+real|rho\s*!=\s*0|rho\s*\\neq\s*0|rho\s*->|rho\s+map|same\s+rho|matching.{0,40}rho)", s)
    basis = has(r"(?:spherical\s+basis|basis\s+phase|magnetic\s+(?:index|indices)|m\s*=\s*\+?1.{0,80}0.{0,80}-1|exact\s+basis\s+transform)", s)
    orientation = has(r"(?:g[_ ]?ab\s*=\s*g[_ ]?b\s*\^?-?1\s*g[_ ]?a|g_b\^-1\s*g_a|edge[- ]orientation|relative\s+group\s+orientation|left/right)", s)
    normalization = has(r"(?:normalization|gram\s+norm|intertwiner.{0,120}(?:norm|ordering|incidence)|frozen\s+K5\s+incidence)", s)
    map_words = has(r"(?:coherent.{0,180}(?:magnetic|operator|tensor)|(?:magnetic|operator|tensor).{0,180}coherent)", s) and has(r"(?:map|maps|mapped|transfer|transferred|identity|equals|=|->|transform)", s)
    distribution_bridge = coherent and magnetic and map_words and has(r"(?:distribution|delta|contact)", s)
    wrong = has(r"(?:WRONG_CONVENTION|wrong\s+(?:rho|basis|phase|normalization|orientation)|rho\s*->\s*-rho|orientation\s*=\s*wrong)", s)
    coeff = None
    # Exact coherent-contact contraction coefficient only when explicitly labelled as such.
    m = re.search(r"(?:C_contact_00000|contact_channel00000_(?:exact_)?coefficient)\s*=\s*([+-]?\d+(?:/\d+)?)", s, re.I)
    if m:
        coeff = str(Fraction(m.group(1)))
    leading_only = has(r"11\s*/\s*24|Q\s*=\s*diag\s*\(\s*1\s*,\s*-2\s*,\s*1\s*\)", s) and not distribution_bridge
    all7 = coherent and magnetic and rho and basis and orientation and normalization and distribution_bridge and not wrong
    return {"coherent_contact": coherent, "magnetic_operator": magnetic, "rho": rho, "basis_phases": basis,
            "edge_orientation": orientation, "normalization": normalization, "distribution_bridge": distribution_bridge,
            "convention_conflict": wrong, "coefficient": coeff, "leading_only": leading_only, "qualifying_bridge": all7}


def extract(docs: list[tuple[str,str]]) -> dict:
    records, qualifying, conflicts = [], [], []
    coverage = {k: 0 for k in ["coherent_contact","magnetic_operator","rho","basis_phases","edge_orientation","normalization","distribution_bridge"]}
    leading_only = 0
    for path, text in docs:
        for rec in split_records(path, text):
            f = features(rec["text"])
            for k in coverage: coverage[k] += int(bool(f[k]))
            leading_only += int(f["leading_only"])
            item = {"path": path, "heading": rec["heading"], "features": f,
                    "snippet_sha256": hashlib.sha256(rec["text"].encode()).hexdigest(),
                    "snippet": re.sub(r"\s+", " ", rec["text"]).strip()[:700]}
            if f["qualifying_bridge"]: qualifying.append(item)
            if f["convention_conflict"]: conflicts.append(item)
            if any(f[k] for k in coverage) or f["leading_only"]: records.append(item)
    coeffs = [q["features"]["coefficient"] for q in qualifying if q["features"]["coefficient"] is not None]
    return {"coverage": coverage, "qualifying": qualifying, "conflicts": conflicts, "coefficients": coeffs,
            "leading_only_records": leading_only, "evidence_records": records}


def classify(ex: dict) -> str:
    if ex["conflicts"]:
        return "INVALID_IMPLEMENTATION"
    if not ex["qualifying"] or not ex["coefficients"]:
        return "SOURCE_DERIVATION_BLOCKED_SCOPED"
    vals = {Fraction(x) for x in ex["coefficients"]}
    if len(vals) != 1:
        return "INVALID_IMPLEMENTATION"
    v = next(iter(vals))
    return "CONTACT_CANCELS_SCOPED" if v == 0 else "CONTACT_SURVIVES_SCOPED"


def synthetic(text: str) -> dict:
    ex = extract([("synthetic.md", text)])
    return {"classification": classify(ex), "extraction": ex}


def control_text(coeff: str, wrong: bool=False) -> str:
    wrong_line = "WRONG_CONVENTION: rho -> -rho; orientation = wrong." if wrong else "rho is real nonzero and maps to the same rho."
    return f'''# Exact distribution-valued coherent to magnetic bridge\nThe coherent contact distribution delta''(B(z,g)) is mapped by the exact identity to a magnetic spin-1 D^1 operator in the spherical basis m=+1,0,-1.\n{wrong_line}\nThe spherical basis phases are fixed by an exact basis transform. Edge orientation is g_ab = g_b^-1 g_a. Intertwiner normalization and frozen K5 incidence ordering are fixed.\nThis is a distribution-valued contact transfer identity, not the cubic-pole Q control.\nC_contact_00000 = {coeff}\n'''


def run_controls() -> dict:
    c = {}
    c["POSITIVE_SURVIVAL"] = synthetic(control_text("7/11"))["classification"]
    c["ADVERSARIAL_CANCELLATION"] = synthetic(control_text("0"))["classification"]
    c["WRONG_CONVENTION"] = synthetic(control_text("7/11", wrong=True))["classification"]
    missing = """# coherent source\nFor real nonzero rho != 0, coherent spinor contact delta''(B(z,g)) is nonzero.\n# unrelated magnetic leading pole\nD^1 in spherical basis has Q=diag(1,-2,1), intertwiner normalization fixed, g_ab = g_b^-1 g_a, C_00000=11/24.\n"""
    c["MISSING_BRIDGE"] = synthetic(missing)["classification"]
    c["LEADING_POLE_GUARD"] = synthetic("Q=diag(1,-2,1); D^1 spherical basis; C_00000=11/24; real nonzero rho; intertwiner normalization; g_ab = g_b^-1 g_a.")["classification"]
    base = control_text("7/11")
    preload = base + "\nactual_contact_map = null\nsource_pinned = false\nterminal classification = SOURCE_DERIVATION_BLOCKED_SCOPED\n"
    a, b = extract([("synthetic.md", base)]), extract([("synthetic.md", preload)])
    c["CONCLUSION_PRELOAD_GUARD"] = "PASS" if (classify(a)==classify(b) and a["coverage"]==b["coverage"] and a["coefficients"]==b["coefficients"]) else "FAIL"
    expected = {"POSITIVE_SURVIVAL":"CONTACT_SURVIVES_SCOPED", "ADVERSARIAL_CANCELLATION":"CONTACT_CANCELS_SCOPED",
                "WRONG_CONVENTION":"INVALID_IMPLEMENTATION", "MISSING_BRIDGE":"SOURCE_DERIVATION_BLOCKED_SCOPED",
                "LEADING_POLE_GUARD":"SOURCE_DERIVATION_BLOCKED_SCOPED", "CONCLUSION_PRELOAD_GUARD":"PASS"}
    return {"observed": c, "expected": expected, "pass": c == expected}


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--out", default="artifacts/source_j1_k5_contact_representation_derivation_v2.json")
    args = ap.parse_args()
    if git("cat-file", "-t", CORPUS_SHA) != "commit": raise SystemExit("frozen corpus commit unavailable")
    paths = corpus_paths()
    if not paths: raise SystemExit("empty frozen corpus")
    members = [{"path": p, "blob_sha": blob_sha(p), "bytes": len(source_text(p).encode())} for p in paths]
    docs = [(p, source_text(p)) for p in paths]
    controls = run_controls()
    actual = extract(docs)
    classification = "INVALID_IMPLEMENTATION" if not controls["pass"] else classify(actual)
    result = {
        "gate": "SOURCE_J1_K5_CONTACT_REPRESENTATION_DERIVATION_V2",
        "frozen_corpus_sha": CORPUS_SHA,
        "selectors": SELECTORS,
        "corpus_member_count": len(paths),
        "corpus_members": members,
        "controls": controls,
        "actual": {
            "coverage": actual["coverage"],
            "qualifying_bridge_count": len(actual["qualifying"]),
            "qualifying_bridges": actual["qualifying"],
            "conflict_count": len(actual["conflicts"]),
            "exact_contact_coefficients": actual["coefficients"],
            "leading_only_record_count": actual["leading_only_records"],
            "evidence_records": actual["evidence_records"],
        },
        "classification": classification,
        "claim_ceiling": "Scoped source-authority extraction only; BLOCKED is not FAIL; missing bridge/coefficient is not zero; cubic-pole 11/24 is not a coherent-contact coefficient; no D7 closure or terminal selector.",
    }
    out = Path(args.out); out.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"; out.write_text(payload)
    (out.parent / (out.stem + ".sha256")).write_text(hashlib.sha256(payload.encode()).hexdigest()+"  "+out.name+"\n")
    print(json.dumps({"classification": classification, "corpus_member_count": len(paths), "controls_pass": controls["pass"],
                      "coverage": actual["coverage"], "qualifying_bridge_count": len(actual["qualifying"]),
                      "exact_contact_coefficients": actual["coefficients"], "leading_only_record_count": actual["leading_only_records"]}, sort_keys=True))
    if classification == "INVALID_IMPLEMENTATION": raise SystemExit(2)

if __name__ == "__main__": main()
