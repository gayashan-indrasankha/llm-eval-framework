# AI Evaluation Framework: Claude vs Microsoft Copilot

**Status: Stage 1 starter — evaluation design only. No model outputs, rankings, or measured scores yet.**

A reproducible, human-reviewed benchmark for analyzing the accuracy, completeness, evidence grounding, instruction following, clarity and risk awareness of responses to **fictional Governance, Risk & Compliance (GRC) policy questions**.

## Scope
- 3 **synthetic** policies: procurement approvals, accounts payable controls, and third-party/access governance.
- 12 policy-grounded test cases with reference-point checklists and explicit prohibited overclaims.
- Identical copy/paste prompt files for manual Claude and Microsoft Copilot testing.
- A CSV template for recording response metadata and future human ratings.
- No APIs, paid subscriptions, real company data, or AI-generated evaluation scores required for Stage 1.

## Quick start (Python 3.10+)
```powershell
python scripts/validate_data.py
python scripts/build_prompts.py
python -m unittest discover -s tests -p "test_*.py" -v
```

Inspect `generated/prompts/GRC-003.txt` for the first approval-control pilot test and `generated/prompt_manifest.csv` for SHA256 hashes. Read `docs/METHODOLOGY.md` before collecting outputs.

## Repository structure
```text
data/policies/                  Synthetic policy documents (P01–P03)
data/test_cases.json            12 tasks, expected points and red flags
data/evaluation_runs_template.csv   Blank recording template
generated/prompts/              Deterministic prompts (generated)
generated/prompt_manifest.csv   Prompt hashes and case IDs
scripts/                        Data validation and prompt builder
tests/                          Local dataset and prompt tests
docs/                           Methodology and 6-stage roadmap
```

## Evaluation integrity
This is a **comparison of specific consumer/work app configurations tested at particular dates**, not an intrinsic ranking of Anthropic and Microsoft models. Microsoft consumer Copilot and Microsoft 365 Copilot have materially different capabilities and data access. Record your actual app and plan. All project materials are fictional; do not upload proprietary audit records to personal AI accounts. Decisions about real audit findings require human verification.

Read [methodology](docs/METHODOLOGY.md) and [project roadmap](docs/ROADMAP.md).
