# GRC-004 — Trial 2 Consistency Review

**Case:** GRC-004 — Segregation of Duties (SoD) / Self-Approval  
**Sources:** Synthetic procurement policy P01, Rules 1, 3, 4 and 8  
**Models/modes:** Claude Opus 5.5 Medium (previously reported); Microsoft Copilot Auto (selection mode, underlying model undisclosed). Current trial configuration not independently confirmed.  
**Execution timestamps:** Not supplied; record actual Asia/Colombo times in the evaluation CSV.  
**Prompt SHA-256:** `09c27aa00ed42060835f4028fc5c6ddc56caf4cf967c24f81bcdc36dea0ec552` (original Stage 1 benchmark fixture)  
**Status:** Trial 1 scores approved by tester; Trial 2 scores AI-assisted and **awaiting human approval**.

## Original benchmark and expected checks

> A department head approves their own LKR 50,000 purchase request. Is that compliant?

The benchmark reference points are (1) the requester cannot approve their own PR regardless of title (P01 Rule 3), and (2) the situation is a segregation-of-duties exception requiring independent approval (P01 Rule 1; Rule 3). P01 Rule 4 explains the written CFO authorization exception procedure, but an unobserved exception is not presumed. The question supplies no evidence of fraud, loss, PO issuance or funds commitment.

## Trial 2 evidence review

| Evidence item | Claude Trial 2 | Copilot Trial 2 |
|---|---|---|
| Non-compliant self-approval | Pass (P01 Rule 3) | Pass (P01 Rule 3) |
| LKR 50,000 requires line-manager approval | Pass (P01 Rule 1) | Pass (P01 Rule 1) |
| Independent approver / corrective action | Pass | Pass |
| Recognizes uncertainty about actual PO / exceptions | Explicit, conditional | Checks any PO; no speculation |
| Unsupported claims of confirmed fraud/loss | None observed | None observed |
| Clear invented policy obligations | None observed | None observed |

### Claude

The answer correctly states that department-head seniority does not override the self-approval prohibition and explains the line-manager approval requirement. It asks the reviewer to inspect any valid documented CFO exception and check when a PO was issued. However, **"If neither exists, log this as a segregation-of-duties exception"** may suggest that the observed self-approval need not be documented when an exception exists; document the event and consider authorization separately. The claim that a finding cannot be "graded further" is a severity/evidence limitation, not a reason to disregard the detected self-approval. The answer is longer than the benchmark's requested concise form.

### Copilot

The answer correctly identifies the conflict of duties under P01 Rule 3, cites the line-manager approval rule for LKR 50,000, and recommends routing for independent authorization and reviewing any previously issued PO. It is concise and avoids unwarranted inferences.

## Scores and repeatability

| Criterion (0–4) | Claude T1 (approved) | Claude T2 (provisional) | Copilot T1 (approved) | Copilot T2 (provisional) |
|---|---:|---:|---:|---:|
| Accuracy | 4 | 4 | 4 | 4 |
| Coverage | 4 | 4 | 4 | 4 |
| Groundedness | 4 | 4 | 4 | 4 |
| Instruction following | 3 | 3 | 4 | 4 |
| Clarity | 4 | 4 | 4 | 4 |
| Risk awareness | 4 | 4 | 4 | 4 |
| **Total** | **23/24** | **23/24** | **24/24** | **24/24** |

**Observed consistency:** Both products reach the same correct substantive conclusion and score across both trials. Claude's extra material costs one provisional instruction-following point. The small score difference is not evidence of stronger GRC accuracy by Copilot.

**Limitations:** One synthetic case, two samples per product, subjective 0–4 rubric, possible product/model changes, and unverifiable Copilot internal routing/web grounding. No statistical significance or real-world reliability should be inferred.

## Human review checklist

- [ ] Confirm GRC-004 Trial 2 actual execution timestamps and displayed models/modes.
- [ ] Review the independent provisional scores against the raw response files.
- [ ] Approve or revise Claude 23/24 and Copilot 24/24.
- [ ] Once approved, update the two Trial 2 `evaluator` entries in `data/evaluation_runs.csv`.

**Raw evidence:** `responses/GRC-004_claude_trial1.txt`, `responses/GRC-004_copilot_trial1.txt`, `responses/GRC-004_claude_trial2.txt`, and `responses/GRC-004_copilot_trial2.txt`.
