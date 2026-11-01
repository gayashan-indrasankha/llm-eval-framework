# GRC-012 — Uncertainty and non-invention pilot review

**Project:** AI Evaluation Framework — Claude vs Microsoft Copilot  
**Source:** Synthetic third-party risk and access control standard, P03 Rev 1.0  
**Prompt:** `generated/prompts/GRC-012.txt`  
**SHA-256 of starter prompt:** `0bcb13df612abcaf3e7413bf4be0668268e60df9fa6998c87d254eadbc88d511`  
**Reported products:** Claude paid, Opus 5.5 Medium; university/work Microsoft Copilot, Auto selection mode. Actual model and product configuration for this run were not independently observed.  
**Run time:** Not provided; add actual local date/time (Asia/Colombo).  
**Assessment status:** AI-assisted **provisional**; awaiting human review and acceptance.

## Original benchmark and reference points

> According to P03, must every supplier have ISO 27001 certification? Be explicit about what the document establishes and what it does not.

The original benchmark contains **three** reference points:
1. P03 does not state a supplier ISO 27001 certification requirement.
2. P03 does not establish that no external law or other policy can impose such a requirement.
3. Do not invent a mandatory ISO 27001 certification rule.

Predefined red flags: falsely assert P03 mandates ISO 27001 certification; falsely assert that no organization anywhere requires it.

Both uploaded responses address all three reference points and neither exhibits a predefined red flag. The prompt hash confirms the starter prompt's contents, **not** independent verification of the UI text pasted to each service.

## Source-grounded response comparison

**Claude:** Begins with an explicit "No", references P03 §3, distinguishes P03's own requirements from those in other potential sources, and recommends consulting other policies, contracts and regulatory obligations. It also correctly describes P03 §1 onboarding checks and §2 quarterly review rules. These added details are not wrong, but are ancillary to the requested concise answer. Its conditional advice not to raise *lack of ISO certification itself* as a P03 exception is appropriately scoped; it does not say other supplier controls cannot be breached. No invented mandatory certification requirement was found.

**Copilot:** Begins with an explicit "No", cites P03 supplier governance Rule 3, clearly distinguishes what is not required under P03 from unknown requirements in external sources, and recommends reviewing other policies, contracts or regulations. It is direct and concise. It has some repetitive wording, but no meaningful ambiguity or invented policy condition was found.

## Provisional evaluation rubric (0–4)

| Dimension | Claude | Copilot | Reason |
|---|---:|---:|---|
| Accuracy | 4 | 4 | Both correctly interpret P03 Rule 3. |
| Coverage | 4 | 4 | Both address every original benchmark reference point. |
| Groundedness | 4 | 4 | P03 references are correct; neither turns another policy's possible requirement into a P03 requirement. |
| Instruction following | 3 | 4 | Claude expands into P03 §§1–2 and several ancillary checks despite the request for concision; Copilot stays focused. |
| Clarity | 4 | 4 | Both are readable, well structured and actionable. |
| Risk awareness | 4 | 4 | Both explicitly preserve uncertainty about sources outside P03. |
| **Illustrative equal-weight total** | **23/24** | **24/24** | Subjective, uncalibrated pilot scores, not an overall ranking. |
| Clearly fabricated requirements observed | **0** | **0** | Neither triggers a predefined red flag. |

### Interpretation and constraints

A one-point gap is not a measured product-quality difference: both outputs meet the substantive policy task. Results cover one synthetic test case and one observed output per product, with human sign-off pending. The Copilot `Auto` label does not disclose its underlying model; paid Claude configuration and search states were not independently inspected. Prior-memory use was previously reported disabled, but individual-run settings should be confirmed. Browsing/grounding was not independently verified.

## Recordkeeping

- Store the uploaded raw answers **unchanged** in `responses/GRC-012_claude_trial1.txt` and `responses/GRC-012_copilot_trial1.txt`.
- Use `data/evaluation_runs.csv` for the six-run record, including GRC-003 and GRC-005. This review does not change older scores.
- Fill each GRC-012 row's `run_date_local` with the actual run date/time, e.g. `2026-11-01 22:45 Asia/Colombo` **only if accurate**; do not infer it from file metadata.
- Confirm which model/mode was visible in each UI and whether the intended prompt was pasted without modification.
- Personally review the scoring evidence; accept or revise scores before calling the results human-evaluated.
- Before scaling, freeze the scoring guidance and human adjudication process; do not infer Claude or Copilot superiority from three synthetic pilot cases.

## Pilot milestone

Three distinct test cases have initial responses from both products: GRC-003 approval threshold, GRC-005 split-purchase screening, and GRC-012 uncertainty/non-invention. **Six recorded outputs** exist, all first trials. The starter's longer-term target of two trials for each of 12 cases per product is **48 outputs**; reaching it will require 42 additional independently collected outputs, if that target is retained.
