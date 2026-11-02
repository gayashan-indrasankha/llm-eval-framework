# GRC-008 — Three-Way Matching | Trial 1 Evaluation Review

**Status:** AI-assisted **provisional** scoring; user review and sign-off pending.  
**Dataset:** Synthetic GRC benchmark, Serendib Services Ltd; not a real audit or live payment decision.  
**Case ID:** `GRC-008` | **Category:** `payment_matching` | **Difficulty:** Medium.  
**Prompt SHA-256:** `3aff8f4c6ea4290ad06bbcb30c779418adcfd816b8ccdc69b37936987a4f765c` (verified against the Stage 1 starter's original `generated/prompts/GRC-008.txt`).  
**Run date/time:** Not supplied for either response; complete from your original experiment notes.  
**Products:** Claude (previously reported: Opus 5.5 Medium, paid) and Microsoft Copilot (previously reported: university account, Auto mode). **Confirm the model/mode actually used for GRC-008**; Copilot Auto does not disclose its underlying model. External grounding settings for this run were not independently verified.

## Benchmark question

> Accounts Payable has an approved PO and supplier invoice but no goods receipt or documented service acceptance. Should payment be released?

**Supplied source:** P02 — Synthetic Accounts Payable and Payment Controls, items 1–2; only P02 was included in the benchmark prompt.

### Frozen reference-point checklist

| Reference point from `data/test_cases.json` | Claude | Copilot |
|---|---|---|
| Three-way match requires approved PO, receipt/documented acceptance, and invoice | Met | Met |
| Hold payment and seek the missing evidence | Met | Met |
| Do not invent the missing receipt | Met | Met |

**Predefined red flag:** Release payment because two out of the three documents exist. **Triggered:** Neither response.

## Response observations

### Claude

- Correctly concludes that **payment must be held** because the goods receipt/documented service acceptance is missing, citing **P02 items 1 and 2**.
- Explicitly notes that AP must **not invent or backfill missing evidence** and asks for authentic receipt/acceptance documentation.
- Separately mentions approvals specified by P01 under **P02 item 3** while acknowledging P01 itself was not included, so actual approval compliance cannot be evaluated.
- Clearly separates an absent receipt from proof of non-delivery, fraud, or loss, and does not invent an alert severity.
- Includes considerable additional commentary about CFO exceptions, approvals, and severity that goes beyond the narrow, concise answer requested. These are not clear fabricated policy requirements.

### Microsoft Copilot

- Correctly concludes that **payment must not be released**, identifies the missing component of the three-way match, and cites **P02 items 1–2**.
- Correctly instructs AP to **hold the payment**, seek review, and avoid inventing missing evidence.
- Provides a short, directly relevant next action without unsupported accusations.
- Wording note: “or other valid evidence required by the policy” is potentially ambiguous. **P02 items 1–2 identify a goods receipt or documented service acceptance**; the response should not be treated as permission to replace those with an unspecified alternative document. This wording does not clearly state that a different document is sufficient, so it is recorded as a caution, not a fabricated requirement.

## Provisional six-dimension scoring

| Dimension (0–4) | Claude | Copilot | Rationale |
|---|---:|---:|---|
| Accuracy | 4 | 4 | Both correctly prohibit release with an incomplete three-way match. |
| Coverage | 4 | 4 | All three original reference points are covered. |
| Groundedness | 4 | 4 | Correctly cite P02 and do not assert an invented exception; note Copilot's ambiguous wording. |
| Instruction following | 3 | 4 | Claude provides additional tangential detail despite the request for concision; Copilot stays focused. |
| Clarity | 4 | 4 | Both give understandable, actionable recommendations. |
| Risk awareness | 4 | 4 | Neither treats a documentation gap as proven misconduct or loss; both recommend review. |
| **Total** | **23 / 24** | **24 / 24** | **Provisional, reviewer sign-off pending.** |

**Clearly fabricated policy requirements:** 0 in either response, under this review.  
**Actual run date/time:** Not recorded.  
**Raw responses:** `responses/GRC-008_claude_trial1.txt` and `responses/GRC-008_copilot_trial1.txt`.

## Evidence, scope, and fairness cautions

1. A single response per product is not a measurement of repeatability, hallucination rate, or overall model superiority.
2. Each product was evaluated against the same **frozen** synthetic policy and reference points, but underlying system instructions, model routing, and hidden retrieval settings can differ.
3. The six 0–4 scores are judgment-based. User review is required; preserve any disagreements in `comments` rather than overwriting evidence without explanation.
4. There is a repeated pattern in this benchmark of taking one point from Claude for verbosity and awarding full marks to concise Copilot responses. Before interpreting aggregate differences, check that the criteria really measure the intended GRC quality and that equal standards are applied across products.
5. The sample is fictional and does not demonstrate handling of real production invoices, financial risk or enterprise Copilot features.

## Reviewer sign-off

- [ ] Confirm actual GRC-008 Claude model/mode and Copilot mode used.
- [ ] Fill in the two actual local run timestamps in `data/evaluation_runs.csv`.
- [ ] Read both unedited responses and check the references to P02.
- [ ] Approve or adjust the provisional scores with documented reasons.
- [ ] Preserve raw responses and prompt fingerprint.

**Next case:** GRC-009 (copy the original generated prompt; do not change reference answers or evaluation rubric after seeing responses).
