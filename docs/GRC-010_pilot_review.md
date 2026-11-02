# GRC-010 — High-Risk Supplier Review: Trial 1 Evaluation

**Status:** AI-assisted provisional assessment; user sign-off pending for GRC-010.  
**Benchmark case:** GRC-010 — `third_party_governance` (medium difficulty)  
**Source:** Synthetic Third-Party Risk and Access Control Standard, **P03 — Supplier Governance, Rule 2**.  
**Prompt SHA-256:** `0533a08a0483fd59e795e6bc1e35591d8a0882ca54e04072a26a73796f806668` (verified against the original Stage 1 starter prompt and manifest).  
**Run timestamp:** Not supplied. Leave blank rather than inferring from file upload times.  
**Configurations:** Claude Opus 5.5 Medium, Microsoft Copilot Auto, as previously reported; confirmation for the GRC-010 run not independently provided.

## Frozen benchmark and expected answer

> How often must High-risk suppliers be reviewed, and what should the record contain?

The original `data/test_cases.json` contains **two reference points**:

1. High-risk suppliers must be reviewed **quarterly**.
2. Record **decisions, ownership, and follow-up actions**.

The benchmark red flags are incorrectly stating **monthly** reviews or asserting **no documentation is needed**.

| Benchmark item | Claude | Copilot |
|---|---|---|
| Quarterly review frequency | Met | Met |
| Decisions included in review record | Met | Met |
| Ownership recorded | Met | Met |
| Follow-up actions recorded | Met | Met |
| Correct P03 Rule 2 attribution | Met | Met |
| Monthly-review red flag | Not observed | Not observed |
| No-documentation red flag | Not observed | Not observed |

## Provisional scores

| Dimension (0–4) | Claude | Copilot |
|---|---:|---:|
| Accuracy | 4 | 4 |
| Coverage | 4 | 4 |
| Groundedness | 4 | 4 |
| Instruction following | 3 | 4 |
| Clarity | 4 | 4 |
| Risk awareness | 4 | 4 |
| **Total** | **23/24** | **24/24** |
| Clearly fabricated policy requirements | 0 | 0 |

### Claude evidence and rationale

- **Accuracy, coverage, groundedness — 4:** States quarterly review frequency and all three required record elements; attributes the rule to P03 Rule 2.
- **Instruction following — 3:** Its analysis of high-risk classification, reviewer identity and record retention, plus the proposed audit approach, exceeds the prompt's requirement for a concise answer.
- **Clarity, risk awareness — 4:** Clear structure, appropriate audit testing plan, and no accusation of fraud or financial loss.
- **Nuance:** The request for the *last four quarters* is a reasonable suggested audit sample; P03 does **not** specify a mandatory four-quarter lookback. Claude correctly identifies that the P03 Rule 6 12-month retention period is specifically for user-access review logs, **not** supplier-review records. Missing a required record can justify a potential finding, but ultimate conclusions require human verification.

### Copilot evidence and rationale

- **Accuracy, coverage, groundedness — 4:** Clearly states quarterly review and the required decisions, ownership and follow-up actions, with a correct citation to P03 Supplier Governance Rule 2.
- **Instruction following, clarity, risk awareness — 4:** Concise, understandable, operational next step; avoids ungrounded claims.
- **Nuance:** Its review-check recommendation is an auditor's proposed procedure, not a new requirement in the P03 text.

## Interpretation and limitations

Both systems meet the two frozen reference points and avoid both predefined red flags. The **one-point difference** reflects the concision criterion; it does not establish a meaningful difference in underlying policy accuracy. Scores are an AI-assisted provisional assessment and should be approved or changed by the human evaluator before being described as final. Neither response establishes real-world GRC performance.

The recorded user/model configuration does not independently establish the hidden Copilot model, whether search grounding occurred, or the exact local execution timestamp. Preserve the complete, unchanged raw outputs in:

- `responses/GRC-010_claude_trial1.txt`
- `responses/GRC-010_copilot_trial1.txt`

## Human reviewer sign-off

- [ ] Review the original P03 policy and both raw responses.
- [ ] Approve or revise **Claude 23/24** and **Copilot 24/24**.
- [ ] Fill actual execution timestamps and verify model/mode settings if available.
- [ ] Update the `evaluator` status in `data/evaluation_runs.csv` only once sign-off is given.
