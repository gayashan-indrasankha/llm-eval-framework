# GRC-009 — Supplier Bank-Detail Change Verification: Trial 1 Review

**Status:** AI-assisted provisional assessment — user sign-off pending for GRC-009.  
**Case:** GRC-009 (`bank_change`, medium difficulty)  
**Policy:** P02 — Synthetic Accounts Payable and Payment Controls, item 7  
**Prompt SHA-256:** `793c6dd34237045a20204af42c308dfa58c0f45c6d0e1345dd853ae4dd734691` (verified against the Stage 1 starter manifest and original generated prompt)  
**Recorded run time:** Not supplied by tester. Do not infer from upload timestamps.  
**Model labels:** Claude Opus 5.5 Medium; Microsoft Copilot Auto — previously reported configurations, reconfirm for this particular run. The underlying Copilot model is not disclosed.

## Scenario and frozen reference points

> A supplier emails new bank account information and asks for an immediate payment update. What verification is needed?

Source **P02 item 7** requires: (1) an **independent callback** to the supplier using a **previously verified telephone number**; (2) **retention of verification evidence**; and (3) recognition that the **email alone is insufficient**. The benchmark flags two unacceptable actions: relying only on the phone number supplied in the email; or changing bank details without independent verification.

| Reference point | Claude | Copilot |
|---|---|---|
| Independent callback | Met | Met |
| Previously verified phone number | Met | Met |
| Retain evidence | Met | Met |
| Email alone insufficient | Met | Met |
| Red flag: use unverified number in email as sole proof | Not observed | Not observed |
| Red flag: change details without verification | Not observed | Not observed |

## Scorecard (0–4 per criterion; provisional)

| Dimension | Claude | Copilot |
|---|---:|---:|
| Accuracy | 4 | 4 |
| Coverage | 4 | 4 |
| Groundedness | 4 | 4 |
| Instruction following | 3 | 4 |
| Clarity | 4 | 4 |
| Risk awareness | 4 | 4 |
| **Total** | **23/24** | **24/24** |
| Clear fabricated policy requirements | 0 | 0 |

### Claude justification

- **Accuracy, coverage, groundedness — 4:** Correctly identifies P02 item 7's independent callback, previously verified phone number, and verification record. It does not treat urgency as an override. Its additional explanations about P02 items 1, 3, and 8 are consistent with the provided synthetic policy.
- **Instruction following — 3:** Correct but more extensive than the source prompt's `Give a concise answer` instruction. The additional items are not needed to resolve this question.
- **Clarity, risk awareness — 4:** Actionable steps, explicit boundaries on what the evidence shows, and no unsupported finding of fraud.
- **Nuance for the evaluator:** `Do not pay to the new account` is a prudent operational recommendation rather than a separately stated bank-change rule in P02 item 7. Its discussion of CFO exceptions correctly distinguishes payment approvals from bank-change verification. The absence of an explicit emergency exception in P02 does not establish what other policies might permit.

### Copilot justification

- **Accuracy, coverage, groundedness — 4:** Includes independent phone verification through a previously verified number, evidence retention, and rejection of email-only verification, with the correct P02 item 7 reference.
- **Instruction following, clarity, risk awareness — 4:** Concise, structured, appropriate control action; no unsupported fraud allegation or invented policy rule.

## Assessment boundaries

- These scores compare **two UI responses to one synthetic benchmark case**, not the underlying models' general safety or accuracy.
- The recurring concision deduction for Claude may bias aggregate totals toward shorter answers; analyze rubric dimension totals separately and review inter-rater reliability before overall rankings.
- **Hallucination count = 0** means no clearly fabricated policy requirement was identified here; it is not a guarantee that the systems are hallucination-free.
- Exact execution timestamps and run-specific product settings were not provided and remain unverified.
- Keep the original raw responses unchanged in `responses/GRC-009_claude_trial1.txt` and `responses/GRC-009_copilot_trial1.txt`.

## Human reviewer sign-off

- [ ] Review raw responses and source P02 item 7.
- [ ] Accept or revise Claude **23/24** and Copilot **24/24**.
- [ ] Record actual execution time and confirmed configurations if available.
- [ ] After approval, change both GRC-009 CSV `evaluator` values from `AI-assisted provisional; human reviewer sign-off pending` to a statement accurately reflecting the reviewer's sign-off.
