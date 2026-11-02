# Stage 4 — local repository audit and integration record

**Basis:** `llm-eval-framework-stage4-audit.zip` supplied by the project owner. **Scope:** source and evidence files contained in that snapshot, not the owner's live Git remote or installed app configurations.

## Findings prior to integration

- The original README and Methodology still described an unexecuted Stage 1 starter. The roadmap also presented the workbook and audits as future work.
- The repository held all **48 plaintext responses**, 12 case definitions, three synthetic policy files, 12 prompt text files, a SHA-256 manifest, 24 per-case review notes, and a 48-row CSV.
- The local `data/evaluation_runs.csv` had the **last two records (GRC-012 Trial 2) still marked provisional**, although the user had subsequently approved those scores. The supplied final approved CSV differs from the snapshot only in these two `evaluator` and `comments` fields; no numeric scores changed.
- The original test suite passed **5/5** checks, but did not validate the scored dataset, raw file links, approvals or score totals.
- The Stage 3 analysis report, workbook and analysis script were absent from this snapshot's `docs/` and `scripts/` directories.
- `.gitignore` contained `responses/`, despite the project owner reporting 48 already tracked raw response files. This was inconsistent with preserving public synthetic evidence and could silently ignore future response additions.
- Generated Python `__pycache__` files existed in the upload; they are excluded from the cleaned distribution rather than treated as source.

## Changes applied to the deliverable

1. Replaced `data/evaluation_runs.csv` with the **final 48-record, user-approved** version; left original raw responses and individual score values untouched.
2. Added `scripts/stage3_analyze.py`, `docs/Stage3_Comparative_Analysis.md`, `docs/Stage3_Benchmark_Dashboard.xlsx`, and `docs/Stage3_Metrics.json` from the previously generated Stage 3 analysis package.
3. Updated README, Methodology, Roadmap and validation-script status messaging to reflect actual work, results and limitations.
4. Added an architecture guide and reproducibility guide, and **4 new regression tests** for run completeness, prompt+response evidence, approvals and published aggregates.
5. Updated `.gitignore` to explicitly track synthetic `responses/` while still ignoring local secrets and private evidence.
6. Preserved `data/test_cases.json`, policies, prompt files and hashes, all original 48 raw AI outputs and all original case-review notes.

## Checks on integrated deliverable

- Existing + new unit tests: **9/9** (5 original + 4 new).
- Dataset design: 12/12 synthetic cases valid.
- Run matrix: 48 unique records, 12 × 2 × 2 present.
- Archived prompt SHA-256: 12/12 consistent with manifest; recorded prompt hashes: 48/48 consistent with corresponding case.
- Raw saved response links: 48/48 present and nonempty.
- Project-owner approval labels: 48/48.
- Score summary: Claude **545/576**; Microsoft Copilot **575/576**.
- Trial score stability: 22/24 case–product pairs.
- Missing execution timestamps: **44/48**. These were **not** inferred or filled.

## Not verified; publication checklist

- Actual prompts pasted into live Claude/Copilot UI, hidden model IDs, grounding and search settings.
- Independent blinded second-rater scoring or actual generalizable real-world accuracy.
- Publication to the owner's GitHub remote; repository changes must be applied locally and committed by the owner.
- Personal/confidential information in any external files not included in the snapshot. A pattern-based check in this snapshot found no obvious email addresses or common token patterns, but this is not a privacy guarantee.

Read [Methodology](METHODOLOGY.md) and [Reproducibility](REPRODUCIBILITY.md) before citing findings externally.
