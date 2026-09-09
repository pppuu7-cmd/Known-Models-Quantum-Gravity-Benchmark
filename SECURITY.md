# Repository integrity and change control

KMQGB is a research benchmark repository. Security here includes preservation of scientific provenance and prevention of silent changes to frozen methodology.

## Critical paths

Changes to `protocol/`, `recovery/`, `.github/workflows/`, `schemas/`, `templates/`, `release/`, `reproducibility/`, `publication/`, or `code/` must run the complete `methodology-ci` workflow before they are considered authoritative.

## Required main-branch policy

The repository owner should configure GitHub branch protection or a repository ruleset for `main` with:

- pull requests required before merge;
- required status check: `methodology-self-tests`;
- force pushes blocked;
- branch deletion blocked;
- CODEOWNERS review required for critical paths when collaborators are added;
- administrators included where supported.

The repository itself cannot enforce GitHub-hosted branch settings from source files. Until the platform rule is enabled, `main` protection is an explicit external governance prerequisite.

## Reproducibility policy

CI dependencies, Python, runner OS and third-party Actions are frozen in `requirements-ci.txt` and `reproducibility/ENVIRONMENT_LOCK.json`. Any change requires a full regression run and an updated lock authority.

## Reporting integrity problems

Open a GitHub issue describing the affected commit, file, expected invariant, observed behavior and a minimal reproduction. Do not silently rewrite historical recovery/provenance artifacts.
