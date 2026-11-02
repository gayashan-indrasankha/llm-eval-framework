# GRC-011 — Employee Access Revocation: Trial 1 Evaluation

**Status:** AI-assisted provisional assessment; reviewer approval pending for GRC-011.  
**Benchmark:** GRC-011 — `access_governance` (medium).  
**Source:** Synthetic P03 — Access Governance, Rule 5.  
**Prompt SHA-256:** `b311efd020fc72d71c99456fbfb3ef7babf6c17a6f791c097c8ae541ab979de0` (verified against the starter prompt and manifest).  
**Actual execution time:** Not supplied; left blank in the CSV.  
**Products:** Claude Opus 5.5 Medium and university Microsoft Copilot Auto, previously reported modes; current trial settings not independently reverified.

## Frozen reference points

> HR sends the official departure notice for a finance employee. What access-control deadline applies?

1. Revoke access **within 24 hours of receiving the official HR departure notice**.
2. **Retain evidence** of the access revocation.

The two predefined benchmark red flags are: incorrectly starting the deadline at resignation regardless of HR notification, or saying no recorded evidence is needed.

| Check | Claude | Copilot |
|---|---|---|
| Within 24 hours | Met | Met |
| Clock starts upon receipt of official HR notice | Met | Met |
| Retain revocation evidence | Met | Met |
| P03 Rule 5 cited | Met | Met |
| Incorrect resignation-date trigger | Not observed | Not observed |
| Evidence not needed | Not observed | Not observed |

## Provisional scoring

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

### Claude rationale

- **Accuracy / coverage / groundedness — 4 each:** Identifies both required points and correctly anchors the deadline to HR notice receipt, not the employee's last day. References P03 Rule 5.
- **Instruction following — 3:** Its discussion of uncertainty around hour type, scope, reviewer identity, evidence format, quarterly access reviews and retention adds information beyond the concise deadline question. No required benchmark detail is missing.
- **Clarity / risk awareness — 4 each:** Structured explanation and audit-evidence comparison; avoids alleging fraud or loss.
- **Nuance:** P03's 12-month retention requirement concerns **access-review logs** under Rule 6, not explicitly the separate Rule 5 revocation evidence. P03 does not specify a particular retention duration for Rule 5 evidence. A confirmed failure to revoke within the deadline would support a control exception, but the scenario provides no actual revocation timestamp; the response appropriately proposes verifying it.

### Copilot rationale

- **All dimensions — 4:** Concisely identifies the deadline, HR notice trigger and evidence obligation with P03 Rule 5 citations; proposes verifying access removal from relevant finance applications and retained evidence.
- **Nuance:** P03 Rule 5 says 'access' generally; checking finance applications is appropriate for this scenario but does not prove that other applicable access was removed.

## Interpretation and limitations

Both models pass both **original** reference points and avoid both predefined red flags. The one-point provisional gap is about concision, **not** accuracy or grounding. The current benchmark has a small synthetic dataset, no established inter-rater reliability, and variable web/enterprise configuration controls; this result does not establish overall product superiority or production GRC reliability.

Retain unchanged source responses:
- `responses/GRC-011_claude_trial1.txt`
- `responses/GRC-011_copilot_trial1.txt`

## Human reviewer checklist

- [ ] Approve or revise **Claude 23/24** and **Copilot 24/24**.
- [ ] Record the actual trial timestamps in Asia/Colombo.
- [ ] Confirm which model/mode and memory/search settings were displayed at execution.
- [ ] Update `evaluator` values only after approval.

## First-trial benchmark milestone

This response pair completes initial collection for all 12 cases: **24 out of the planned 48 responses** (two products × two trials). Trial 2 remains to be collected. GRC-010's previously supplied reviewer approval has been recorded in the combined CSV, but GRC-011 is still provisional.
