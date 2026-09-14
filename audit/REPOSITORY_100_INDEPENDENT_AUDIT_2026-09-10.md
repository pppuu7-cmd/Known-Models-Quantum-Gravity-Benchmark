# Independent Audit of the KMQGB “100% Repository / Methodology Ready” Claim

**Date:** 2026-09-10  
**Audited branch/base:** `main` at Iter180  
**Audit type:** independent engineering/reproducibility audit of the repository-readiness claim; not a scientific review of quantum-gravity conclusions.

## Executive verdict

The statement `R1=100%, R2=100%` is **internally valid under KMQGB's own frozen completion contract**: the required files exist, the current Iter180 CI is green, the strict completion validator passes, and the reproducibility bundle is produced.

However, the stronger statement “the repository is genuinely 100% ready under an external research-software / computational-reproducibility standard” is **not supported**.

Independent audit estimate:

**83/100 (approximately ±3 points depending on how strongly repository security and archival publication are weighted).**

Therefore the correct interpretation is:

- **100/100 — internal declared-scope contract compliance**;
- **~83/100 — independent engineering/reproducibility maturity**;
- scientific readiness remains separately below 100 and is not assessed upward here.

## Evidence that the internal 100% is real

1. `protocol/READINESS_100_COMPLETION_CONTRACT.md` clearly scopes 100% to R1/R2 and explicitly separates it from R3, Closure Wave 02 and Paper IV.
2. `code/repository_completion_validator.py --require-100` is exercised in CI.
3. Current Iter180 workflow run `34414872218` / job `102677415562` completed successfully, including all 36 named validation/build/upload steps.
4. The same current run produced `kmqgb-reproducibility-bundle` artifact id `10128663744` with workflow digest `sha256:cdd268730e7415038e0af9156dc6a3407622c1a40bfcf6427b6bc97871fed2b7`.
5. `recovery/state.json` keeps R3=24%, CW2=0/3 and Paper IV `NOT_YET_AUTHORIZED`, so the anti-inflation firewall is functioning.

## Independent scorecard

| Area | Weight | Score | Audit finding |
|---|---:|---:|---|
| Declared methodology/governance completeness | 25 | 25 | Strong scope definition, recovery chain, claim firewall, candidate gates and explicit BLOCKED semantics. |
| Executable verification / CI | 20 | 19 | Broad 36-step CI plus registry/orchestrator and negative controls. Main weakness: mostly custom self-tests/reference scripts rather than an independent test framework with coverage/property/mutation checks. |
| Computational reproducibility | 20 | 14 | Source bundle is byte-deterministic and hashed, but the execution environment is not frozen strongly enough. CI uses `ubuntu-latest`, Python 3.12 and an unpinned `numpy`; GitHub Actions are referenced by mutable major tags. |
| Repository integrity / change control | 15 | 8 | CI runs on pushes, but `main` is unprotected, there are no repository rulesets, required checks are not enforced by branch protection, and commits are unsigned. A bad direct push can therefore bypass the intended governance in practice. |
| Release / archival publication readiness | 10 | 7 | Reproducibility artifacts exist, but Actions retention is 30 days and there is no GitHub Release at audit time. The bundle is therefore reproducible but not yet a durable archival release object. |
| Recovery / auditability / claim discipline | 10 | 10 | Strong recovery state, provenance corrections, explicit permitted/forbidden claim matrix and separation of infrastructure completeness from scientific completeness. |
| **Total** | **100** | **83** | **Strong research repository, but not externally defensible as absolute 100% yet.** |

## Material findings

### F1 — Critical: `main` is not protected

At audit time GitHub reports `protected=false`, protection disabled, and no required status checks on `main`. Repository rulesets are empty.

Impact: the CI/governance machinery is advisory rather than enforced. A direct forceful/incorrect change to `main` can invalidate the 100% state before CI protection prevents it.

Closure condition:

- protect `main` or add a repository ruleset;
- require the methodology CI check before merge;
- block force pushes and branch deletion;
- preferably require pull requests for changes to frozen protocol/recovery/CI files.

### F2 — High: execution dependencies are not frozen

`.github/workflows/methodology-ci.yml` uses:

- `runs-on: ubuntu-latest`;
- `python-version: '3.12'`;
- `pip install numpy` without an exact version/hash;
- `actions/checkout@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4` rather than immutable commit SHAs.

Impact: the same repository commit can execute against different NumPy, runner-image or Action implementations in the future. The ZIP builder proves deterministic packaging of files, not full computational-environment reproducibility.

Closure condition:

- add a dependency lock (or exact requirements with hashes);
- pin the runner/container image or record a reproducible container definition;
- pin GitHub Actions to immutable commit SHAs;
- include environment metadata/lock files in the reproducibility bundle.

### F3 — High: completion validator is partly self-certifying

`code/repository_completion_validator.py --require-100` checks that R1 and R2 **already equal 100** in `recovery/state.json`, then checks required artifact existence and selected invariants. It does not independently recompute every R1/R2 rubric component from atomized evidence.

Impact: it is an excellent consistency validator, but it is not an independent scoring engine. The phrase “strict 100-percent validator” is stronger than what the code actually proves.

Closure condition:

- create a machine-readable rubric with every R1/R2 point and evidence predicate;
- compute the score from those predicates rather than reading the score as input;
- make CI compare computed score with declared score.

### F4 — Medium: schema exists but is not validated by an independent JSON-Schema engine

The v1.3 validator is hand-written and checks strong scientific/governance invariants, but CI does not validate the template against `schemas/candidate_gravity_record_v1_3.schema.json` using a standards-compliant JSON-Schema validator.

Impact: schema and code validator can drift while both repository-specific self-tests remain green.

Closure condition:

- add `jsonschema` (pinned) or another standards-compliant validator;
- test valid/invalid fixtures against both the schema and semantic validator.

### F5 — Medium: release artifacts are temporary rather than archival

CI uploads the reproducibility bundle with `retention-days: 30`. At audit time the repository has no GitHub Releases.

Impact: reproducibility evidence is excellent for active development but weak as long-term publication provenance.

Closure condition:

- create a versioned/tagged release after major frozen milestones;
- attach the deterministic bundle and manifest to the release;
- for publication, archive a release in a persistent DOI-bearing service if desired.

### F6 — Medium/low: publication/reuse metadata is incomplete

The repository has strong internal claim/evidence matrices, but standard external reuse metadata is not yet part of the frozen completion object (e.g. citation metadata and an explicit repository license were not found during this audit).

Impact: this does not affect the mathematics, but it weakens external publication/reuse readiness.

Closure condition:

- add `CITATION.cff` or equivalent citation metadata;
- add an explicit license appropriate to code/text/data;
- include both in the release bundle.

## What should remain unchanged

This audit does **not** justify changing any scientific status upward or downward merely because of repository engineering findings:

- R3 Candidate Gravity remains independently controlled;
- CW2 scientific terminal count remains separate;
- Paper IV remains governed by its own frozen decision ledger;
- `BLOCKED` remains a valid scientific state and is not evidence for `NEW_REQUIRED`.

## Recommended interpretation going forward

Until findings F1-F5 are closed, avoid saying simply “the repository is 100% ready” without qualification.

Use:

> “KMQGB is 100% complete under its internal R1/R2 completion contract; independent engineering/reproducibility audit currently rates it about 83/100.”

After F1-F5 are closed and an independently computed rubric passes on a protected/tagged commit, the external score can reasonably approach 95-100%.
