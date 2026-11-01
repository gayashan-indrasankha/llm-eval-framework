# GRC-002 — Approval Threshold Boundary, Trial 1

**Status:** Provisional AI-assisted review. **Human approval of these two scores is pending.**

**Source:** Original synthetic benchmark `GRC-002`, policy P01.

**Question:** A requester submits a PR for exactly LKR 100,000. Is this above the approval threshold, and who must approve?

**Benchmark SHA-256:** `f0f56bdd713f07c2a4cda6a646003c0f820f97af3c286e8d683c5e1f674403fd`

## Reference checklist

- **R1:** Exactly LKR 100,000 is **not above** the LKR 100,000 threshold (P01 Rules 1–2).
- **R2:** The requester's **line manager** must approve **before PO issuance** (P01 Rule 1).
- **Red flag:** Incorrectly requiring both department-head and finance-manager approvals at exactly LKR 100,000.

## Review of raw responses

| Observation | Claude | University Copilot |
|---|---|---|
| Correct boundary | Yes | Yes |
| Correct approver | Line manager | Line manager |
| Approval timing | Before PO | Before PO |
| Incorrectly invokes higher approval tier | No | No |
| Self-approval rule referenced | Yes; P01 Rule 3 | Yes; P01 Rule 3 |
| Clearly fabricated policy requirement | None identified | None identified |

**Claude:** Correctly cites P01 Rules 1–3 and gives the required line-manager answer. The extra quotation and split-purchase checks are largely policy-consistent, but the claim that a PR exactly at the threshold is a “common pattern” in splitting is **not established by P01**. The response labels the potential split case conditionally and does not claim proven misconduct. Record a source-grounding caution, **not** a fabricated policy rule. More expansive than the requested concise answer.

**Copilot:** Correctly interprets the inclusive lower-tier boundary, cites P01 Rules 1 and 3, and recommends confirming timely manager approval and no self-approval. Concise and well-grounded.

## Provisional scoring (0–4 per dimension)

| Dimension | Claude | Copilot | Reason |
|---|---:|---:|---|
| Accuracy | 4 | 4 | Correct threshold and approver |
| Coverage | 4 | 4 | Both reference points met |
| Groundedness | 3 | 4 | Claude's “common pattern” assertion is not supported by P01 |
| Instruction following | 3 | 4 | Claude adds avoidable ancillary analysis despite concision instruction |
| Clarity | 4 | 4 | Both understandable and actionable |
| Risk awareness | 4 | 4 | Neither alleges misconduct without evidence |
| **Total** | **22/24** | **24/24** | Descriptive comparison for a single test case only |

**Clear fabricated policy requirements counted:** Claude 0, Copilot 0. Grounding caution remains documented separately.

## Provenance and limits

- Uploaded unmodified response files: `responses/GRC-002_claude_trial1.txt` and `responses/GRC-002_copilot_trial1.txt` (move to these locations locally).
- Claude model `Opus 5.5 Medium` and Copilot mode `Auto` are **previously reported**; confirm configuration for this run.
- Actual trial timestamps and web/work-grounding state were not supplied; record them from your run notes. Do not infer the test time from file upload time.
- These scores are **AI-assisted provisional** until the user explicitly approves them.
- The other four cases in the combined CSV have previously received user score approval.
- The synthetic benchmark is too small to establish relative model quality or general hallucination rates.
