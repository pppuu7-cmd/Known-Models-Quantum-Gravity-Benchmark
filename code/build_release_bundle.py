"""Build a deterministic KMQGB reproducibility bundle.

The bundle contains only paths frozen in release/BUNDLE_CONTENTS.json.  Every
source file is SHA-256 hashed and recorded in MANIFEST.json inside the archive.
ZIP timestamps and permissions are normalized so identical repository contents
produce byte-identical archives.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "release" / "BUNDLE_CONTENTS.json"
DEFAULT_OUTPUT = ROOT / "build" / "kmqgb-reproducibility-bundle.zip"
FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_policy() -> dict:
    data = json.loads(POLICY.read_text(encoding="utf-8"))
    if data.get("bundle_policy_version") != "1.0":
        raise ValueError("unsupported bundle policy version")
    paths = data.get("paths")
    if not isinstance(paths, list) or not paths:
        raise ValueError("bundle policy paths must be a non-empty list")
    if len(paths) != len(set(paths)):
        raise ValueError("bundle policy contains duplicate paths")
    for rel in paths:
        if not isinstance(rel, str) or not rel or rel.startswith("/") or ".." in Path(rel).parts:
            raise ValueError(f"unsafe bundle path: {rel!r}")
        if not (ROOT / rel).is_file():
            raise FileNotFoundError(f"required bundle file missing: {rel}")
    return data


def source_manifest(policy: dict) -> dict:
    entries = []
    for rel in sorted(policy["paths"]):
        raw = (ROOT / rel).read_bytes()
        entries.append({
            "path": rel,
            "size": len(raw),
            "sha256": sha256_bytes(raw),
        })
    return {
        "bundle_schema_version": "1.0",
        "bundle_policy_version": policy["bundle_policy_version"],
        "name": policy.get("name", "kmqgb-reproducibility-bundle"),
        "files": entries,
    }


def normalized_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(filename=name, date_time=FIXED_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = (0o100644 & 0xFFFF) << 16
    return info


def build(output: Path) -> tuple[Path, str, dict]:
    policy = load_policy()
    manifest = source_manifest(policy)
    manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for entry in manifest["files"]:
            rel = entry["path"]
            zf.writestr(normalized_info(rel), (ROOT / rel).read_bytes())
        zf.writestr(normalized_info("MANIFEST.json"), manifest_bytes)

    digest = sha256_bytes(output.read_bytes())
    return output, digest, manifest


def verify_archive(output: Path, manifest: dict) -> None:
    expected = {entry["path"]: entry for entry in manifest["files"]}
    with zipfile.ZipFile(output, "r") as zf:
        names = zf.namelist()
        expected_names = sorted(expected) + ["MANIFEST.json"]
        if names != expected_names:
            raise AssertionError(f"archive order/content mismatch: {names} != {expected_names}")
        archived_manifest = json.loads(zf.read("MANIFEST.json"))
        if archived_manifest != manifest:
            raise AssertionError("archived MANIFEST.json differs from generated manifest")
        for rel, entry in expected.items():
            raw = zf.read(rel)
            if len(raw) != entry["size"] or sha256_bytes(raw) != entry["sha256"]:
                raise AssertionError(f"archive integrity mismatch: {rel}")


def verify_deterministic(output: Path, first_digest: str) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        second = Path(tmp) / "bundle.zip"
        _, digest2, manifest2 = build(second)
        verify_archive(second, manifest2)
        if digest2 != first_digest or second.read_bytes() != output.read_bytes():
            raise AssertionError("bundle build is not deterministic")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--verify-deterministic", action="store_true")
    args = parser.parse_args()

    output, digest, manifest = build(Path(args.output))
    verify_archive(output, manifest)
    if args.verify_deterministic:
        verify_deterministic(output, digest)

    print(f"PASS: built {output.relative_to(ROOT) if output.is_relative_to(ROOT) else output}")
    print(f"files={len(manifest['files'])} sha256={digest}")
    if args.verify_deterministic:
        print("deterministic_rebuild=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
