# GRC-001 — Procurement Approval Evaluation (Trial 1)

## Status and evidence

- **Status:** AI-assisted provisional evaluation; human reviewer approval pending for GRC-001. The previously accepted GRC-012 scores remain recorded as human-approved in the combined CSV.
- **Source:** Stage 1 synthetic `P01` procurement policy, `GRC-001` benchmark in `data/test_cases.json`, original prompt `generated/prompts/GRC-001.txt`.
- **Prompt SHA-256:** `12139ba132191eec3f56d1ecb738d2d771ac1d7603533bce5cee2a3c1b8824bc` (verified against the original Stage 1 starter).
- **Question:** A requester submits a PR for LKR 85,000. Which approval is needed before the PO is issued?
- **Raw responses:** `responses/GRC-001_claude_trial1.txt` and `responses/GRC-001_copilot_trial1.txt`.
- **Configurations:** Claude **Opus 5.5 Medium** and university Microsoft Copilot **Auto**, carried forward from previously reported settings. Current trial model settings, exact run date/time, and Copilot grounding have **not** been independently confirmed for these two uploads. Please fill these in after checking your experiment notes.

## Reference-point and red-flag review

| Original benchmark item | Claude | Copilot |
|---|---|---|
| LKR 85,000 is **at or below LKR 100,000** | Pass | Pass |
| **Line-manager approval before PO issuance** is required (P01 Rule 1) | Pass | Pass |
| Red flag: falsely requires both department-head and finance-manager approvals | Not triggered | Not triggered |

Both responses correctly identify the mandatory line-manager approval for this amount. Both mention avoiding requester self-approval, consistent with P01 Rule 3. Neither makes an unsupported fraud or financial loss claim.

## Provisional scores (0–4 per criterion)

| Dimension | Claude | Copilot | Scoring reason |
|---|---:|---:|---|
| Accuracy | 4 | 4 | Both correctly apply Rule 1. |
| Coverage | 4 | 4 | Both cover the two original reference points. |
| Groundedness | 4 | 4 | P01 references support the described rules; no clear invented requirement. |
| Instruction following | 3 | 4 | Claude adds more ancillary control discussion than the prompt's concise scope requires; Copilot stays focused. |
| Clarity | 4 | 4 | Both are easy to understand; Claude's answer remains well structured despite its length. |
| Risk awareness | 4 | 4 | Both avoid unsupported conclusions about fraud or control breaches beyond evidence. |
| **Total** | **23/24** | **24/24** | Provisional and subject to human adjudication. |
| **Clear fabricated requirements counted** | **0** | **0** | Ancillary checks are not automatically hallucinations. |

## Nuanced observations

**Claude:** Correctly identifies line-manager approval, notes that higher-level approvals and quotations do not apply to this single PR, mentions retention and a conditional split-purchase screen, and recommends verifying approval date and segregation of duties. The auxiliary points are supported by P01, but the question requested a concise answer specifically about approval. The extra text merits a provisional instruction-following deduction, **not** a factual-grounding deduction. The conditional split-purchase screen does not mean the current PR has actually triggered the rule.

**Copilot:** Correctly identifies the applicable approver and approval deadline and recommends checking requester self-approval. More concise. It does not mention unrelated controls; this is not an omission because the original GRC-001 reference checklist asks only for the threshold and required approver.

## Limitations and next action

- These are **single responses**. Differences in response length or a one-point rubric score are not evidence of general product superiority.
- Human reviewer should approve/adjust the provisional six-dimensional scores before marking them final.
- Record the **actual local test date/time** and verify the Claude model, Copilot mode and grounding settings for this run. Do not invent missing metadata.
- Continue Stage 2 with remaining unchanged prompts, using fresh chats and storing raw response text.
- Do not change original benchmark or scoring rules after seeing these responses; log methodology revisions separately if necessary.
