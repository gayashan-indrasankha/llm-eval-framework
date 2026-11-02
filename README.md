# AI Evaluation Framework — Claude vs Microsoft Copilot

**Status: 48/48 benchmark responses collected and scores user-approved.**
**Scope: 12 fictional Governance, Risk & Compliance (GRC) cases × 2 observed AI products × 2 manual trials.**

A reproducible, evidence-based *portfolio study* of how Claude and Microsoft Copilot answered questions grounded in **three synthetic GRC policies**. It includes deterministic prompts, original plaintext responses, a six-dimension assessment rubric, human-approved (AI-assisted) scores, comparative analysis, and an Excel dashboard.

> **Not a general model ranking or a real compliance audit.** The results describe the specific app configurations and synthetic questions tested. The scoring process was AI-assisted and approved by the project owner; it was not independently blinded or professionally adjudicated.

## Results at a glance

| Metric | Claude | Microsoft Copilot |
|---|---:|---:|
| Responses | 24 | 24 |
| Rubric points earned / available | **545 / 576** | **575 / 576** |
| Share of rubric points | **94.62%** | **99.83%** |
| Mean score per response / 24 | **22.71** | **23.96** |
| Total-score-stable case pairs | **11 / 12** | **11 / 12** |

**What the scores mean:** 24 of the 30-point total gap came from *instruction following*, predominantly scope and concision rather than incorrect core policy conclusions. Under this recorded rubric, every response received 4/4 on accuracy, coverage, and risk awareness. All 24 model–case pairs retained their substantive policy conclusion between trials, while two pairs changed rubric scores by one point. No definite fabricated policy obligations were tagged. None of these observations establishes real-world accuracy, model superiority, or hallucination-free operation.

Explore [the full comparative report](docs/Stage3_Comparative_Analysis.md) and [Excel dashboard](docs/Stage3_Benchmark_Dashboard.xlsx).

## Research design

- **Synthetic documents:** P01 (procurement approvals), P02 (accounts payable), P03 (supplier and access governance).
- **12 cases:** threshold boundaries, segregation of duties, split-purchase screening, duplicate invoices, three-way matching, bank-detail verification, supplier monitoring, access revocation, and unsupported ISO 27001 claims.
- **Collection:** the same archived, generated prompt for each model per case; users reported fresh chats and two independent manual trials. Neither app was invoked by this repository.
- **Products:** user-reported Claude paid/Opus 5.5 Medium selection and university/work-account Microsoft Copilot Auto mode. Underlying Copilot model identity, exact live configurations, and web-grounding states were not independently verified.
- **Scoring:** six axes, 0–4 each (accuracy, coverage, groundedness, instruction following, clarity, risk awareness); equal-weight sum out of 24. AI-assisted assessments accepted by the project owner, not blinded independent ratings.

Read [Methodology](docs/METHODOLOGY.md) for the protocol and caveats.

## Reproduce the local checks (Python 3.10+)

This project uses **Python standard library only** to validate the dataset, regenerate prompts and compute metrics. No API key or external account is required to reproduce these *local* checks.

From the repository root (PowerShell):

```powershell
python scripts/validate_data.py
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/stage3_analyze.py
```

Expected key checks: 12 source cases, **9/9 tests passing**, 48 unique runs, 48/48 raw responses available, 12/12 archived prompt-hash matches, 48 approved records, Claude 545/576 and Copilot 575/576. Four recorded execution timestamps are populated; **44 are missing**. Timestamp gaps are not filled with guesses.

To intentionally regenerate prompts from the synthetic policy fixtures (this **overwrites** files in `generated/prompts/` and the manifest), run:

```powershell
python scripts/build_prompts.py
```

Then check `git diff` and ensure SHA-256 hashes are unchanged before committing. Prompt hashes validate **archived files**, not what was pasted into a live chat.

The workbook and the written report are reviewed Stage 3 snapshots. The script prints reproducible data metrics; it does not automatically regenerate the Excel charts or re-score the responses.

## Repository guide

```text
data/
  policies/                         P01–P03 synthetic source documents
  test_cases.json                   12 case definitions, expected points and prohibited claims
  evaluation_runs.csv               48 approved scoring records and metadata
  evaluation_runs_template.csv      Empty template for additional experiments
generated/
  prompts/                          12 deterministic, archived manual prompts
  prompt_manifest.csv               Case IDs and prompt SHA-256 hashes
responses/                          48 unmodified plaintext model responses
scripts/
  validate_data.py                  Synthetic benchmark-design checks
  build_prompts.py                  Deterministic prompt generator
  stage3_analyze.py                 Data-integrity audit and score summary
tests/
  test_benchmark.py                 Starter fixture and prompt tests
  test_evaluation_integrity.py      Final dataset, scoring and approval regression tests
docs/
  Stage3_Comparative_Analysis.md    Comparative findings and limitations
  Stage3_Benchmark_Dashboard.xlsx   Excel visual scorecard
  Stage3_Metrics.json               Archived analysis metric snapshot
  GRC-*_pilot_review.md             Trial 1 case review notes
  GRC-*_Trial2_Consistency_Review.md Trial 2 comparisons
  METHODOLOGY.md, ARCHITECTURE.md, REPRODUCIBILITY.md, ROADMAP.md
```

## Integrity and ethical limitations

- All policy documents and cases are **fictional**. Do not upload real company information or personal records to consumer AI applications.
- The 48 plaintext answers are intentionally tracked in Git to make the synthetic evidence inspectable. `.gitignore` still excludes private evidence and local secrets.
- **44/48 actual execution timestamps are blank**; exact live configurations, whether the generated prompts were pasted unchanged into each UI, and grounding behavior cannot be independently established from the archive.
- Ceiling effects, subjective instruction-following penalties, small case coverage, and lack of blinded independent scoring limit generalization. Human control owners must validate real audit findings.
- Do not equate percentage of *awarded rubric points* with a measured real-world correctness rate.

For the collection workflow and known limitations see [Reproducibility](docs/REPRODUCIBILITY.md), [Architecture](docs/ARCHITECTURE.md), and [Roadmap](docs/ROADMAP.md).
