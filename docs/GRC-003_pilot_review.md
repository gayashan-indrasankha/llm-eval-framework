# GRC-003 — First controlled pilot review

**Project:** AI Evaluation Framework: Claude vs Microsoft Copilot  
**Date recorded by tester:** 2026-11-01, approximately 17:15, Asia/Colombo  
**Prompt SHA-256 (verified against Stage 1 starter file):** `05697eadd2540b16254a305d858c6b2930f182e383b8f2c9a6698ed65cfd010e`  
**Evaluation status:** AI-assisted **provisional** assessment; human reviewer approval required before treating these as finalized scores.

## Configuration and limitations

| Setting | Claude | Microsoft Copilot |
|---|---|---|
| User-reported access | Paid plan | University/work account |
| UI selection | Opus 5.5 Medium | Auto |
| Underlying model disclosure | As reported by user; no independent UI verification | Not identified by Auto routing label |
| Prior memory | Disabled by tester | Disabled by tester |
| Web/search | Tester reports web search not available | Not independently verified; Work IQ unavailable per tester |
| Trial | 1 | 1 |
| Raw answer | `responses/GRC-003_claude_trial1.txt` | `responses/GRC-003_copilot_trial1.txt` |

**Evidence scope:** Reviewer read the complete attached response text and matched it to the synthetic P01 rule and reference checklist. The actual UI chat transcript and input pastes were not independently audited. The hash identifies the intended generated prompt; it cannot alone establish that the interfaces received identical pasted content.

## Ground-truth checklist from benchmark GRC-003

- LKR 145,000 exceeds LKR 100,000.
- Department-head approval is required.
- Finance-manager approval is required.
- Both are required before PO issuance (P01, Rule 2).
- Incomplete approvals should be flagged for human review; no fraud allegation should be asserted absent evidence.

**Claude:** All points satisfied, with explicit human-review and non-fraud phrasing. Correctly references P01 Rules 1, 2, 4 and related rules. Additional split-purchase, quotation and retention discussion is source-based, but broader than necessary for this prompt. Its statement that a procedural breach is established only if the PO was issued is a useful distinction about completed issuance; the missing required approvals themselves are already an incomplete control state.

**Copilot:** All core points satisfied; response is concise and explicitly recommends holding PO issuance until approvals are obtained, subject to an authorized written CFO exception. Its additional 'do not commit funds until approvals' recommendation is sensible conservatism but is broader than P01 Rule 2's exact *before PO issuance* deadline. P01 Rule 4 specifically requires written CFO exceptions before funds are committed. Record as minor source-grounding imprecision, not a fabricated factual finding.

## Provisional human-rubric scores (0–4 per criterion)

| Criterion | Claude | Copilot | Reason |
|---|---:|---:|---|
| Accuracy | 4 | 4 | Both correctly identify the threshold and approvals. |
| Coverage | 4 | 4 | Both cover the actionable GRC-003 reference points. |
| Groundedness | 4 | 3 | Claude's cited checks are policy-backed. Copilot somewhat extends the funds-commitment advice. |
| Instruction following | 3 | 4 | Claude adds much more detail than the prompt's request for concision. |
| Clarity | 3 | 4 | Claude is organized but longer; Copilot is direct and concise. |
| Risk awareness | 4 | 4 | Neither declares fraud, financial loss, or an unauthorized exception as fact. |
| **Illustrative unweighted total** | **22/24** | **23/24** | Equal weighting shown only for this pilot; benchmark weighting/adjudication rules must be fixed before aggregate comparison. |
| Clear invented policy claims observed | 0 | 0 | This is a reviewer observation, not a guarantee. |

**Interpretation:** The one-point pilot difference is largely a rubric judgment about brevity and a small grounding caveat. Do not conclude that one tool outperforms the other overall on one synthetic case. Retest in new chats and use predeclared scoring rules and, where possible, an additional independent reviewer.

## Follow-up evidence to record

1. Confirm both chats used the exact GRC-003 prompt unchanged and in fresh sessions.
2. Record the exact university Copilot product name/license tier; 'Auto' is a selection/routing label, not the underlying model identifier.
3. Record whether web grounding was active or uncontrollable in Copilot (unknown at this stage).
4. Human evaluator reviews the scores and notes disagreement/edits with reasons.
5. Pilot a contrasting case: `GRC-005` (potential split purchase) and `GRC-012` (uncertainty and non-invention).

**Do not publish private institutional data or claim the evaluation is independent of AI judgment until a human has signed off.**
