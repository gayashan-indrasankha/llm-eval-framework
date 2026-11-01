# GRC-006 — Split-Purchase Window Boundary: Trial 1 Review

**Assessment status:** AI-assisted provisional, pending user score approval.  
**Date and time of actual runs:** Not supplied; fill in from the user's Claude and Copilot session records.  
**Products reported in prior trials:** Claude paid, Opus 5.5 Medium; university Microsoft Copilot, Auto. These settings have not been independently verified for the uploaded GRC-006 trial.  
**Policy/benchmark:** Synthetic P01 Rules 5–6 (plus related P01 rules in the supplied source).  
**Prompt SHA-256:** `bedb5e393d074b519f575ec6ce4528fd2720a59d044383f74e76cca1b2dbd4ee` (verified against the Stage 1 starter prompt and manifest).  
**Raw evidence:** `responses/GRC-006_claude_trial1.txt` and `responses/GRC-006_copilot_trial1.txt`.

## Original question

> The same requester buys LKR 70,000 and LKR 65,000 from the same supplier in the same category, but five calendar days apart. Does P01's specific split-purchase screening rule trigger?

## Reference-point checklist

| Check | Claude | Copilot | Evidence interpretation |
|---|---|---|---|
| Five calendar days is outside the three-day window | Pass | Pass | Both explicitly identify the five-day interval. |
| P01's **specific** split-purchase rule does not trigger by itself | Pass | Pass | Both return No and correctly cite P01 Rules 5–6. |
| Other controls or reviews could still apply | Pass | Pass | Claude suggests independent approval checks; Copilot acknowledges other checks under Rule 6. |
| Avoid benchmark red flag: definitely compliant in every respect | Pass | Pass | Neither generalizes the no-trigger finding to all procurement compliance. |
| Avoid benchmark red flag: confirmed fraud | Pass | Pass | Neither asserts misconduct; Claude explicitly rejects such conclusions. |

The sum is **LKR 135,000**, above the LKR 100,000 split-purchase amount condition. That does not override the separate **three-calendar-day window** condition, which fails. This is the key distinction being evaluated.

## Provisional rubric scores (0–4 each)

| Criterion | Claude | Copilot | Justification |
|---|---:|---:|---|
| Accuracy | 4 | 4 | Both apply the separate time and amount conditions correctly. |
| Coverage | 4 | 4 | Both meet all three original reference points. |
| Groundedness | 4 | 4 | Both attribute the no-trigger finding to P01 Rules 5–6 without inventing new policy requirements. |
| Instruction following | 3 | 4 | Claude includes extra approval and quotation checks despite the concise-answer instruction; Copilot stays within scope. |
| Clarity | 4 | 4 | Both communicate the distinction and recommendation clearly. |
| Risk awareness | 4 | 4 | Neither asserts blanket compliance, confirmed misconduct, or loss. |
| **Total** | **23/24** | **24/24** | **Awaiting reviewer sign-off.** |
| Clear fabricated policy requirements | 0 | 0 | No definitive fabrication identified in either response. |

## Qualitative observations

**Claude:** Correctly states that P01's specific split-purchase rule does not fire; identifies the shared requester, supplier and category, combined total of LKR 135,000, and five-day gap. The extra discussion of line-manager approval, self-approval, and quotations is consistent with the supplied policy but is beyond the narrow requested scope. Claude properly says approval compliance cannot be confirmed from the facts provided and recommends optional human review where appropriate.

**Copilot:** Correctly separates the monetary and temporal conditions, cites Rules 5–6, and notes that other controls may still require review. The concise answer avoids a broader declaration that the purchases are compliant under all policies.

**What is not concluded:** Neither model's answer establishes whether purchase orders were correctly approved, whether any other control failed, or whether the purchasing pattern involves misconduct. The prompt is entirely synthetic.

## Reproducibility and reviewer action

- Retain the unedited raw response text files and identical generated GRC-006 prompt.
- Record actual local execution timestamps, exact visible product settings and any available web/work grounding state; do not infer a hidden Copilot model.
- The reviewer should confirm or revise these provisional scores and explain any change before marking them approved.
- This single comparison cannot establish general product quality or real-world GRC performance.

## Existing approvals

The preceding combined CSV preserves GRC-001, GRC-002, GRC-003, GRC-005 and GRC-012 approved records. The GRC-004 rows are updated to reflect the user's subsequent explicit approval. GRC-006 remains provisional.
