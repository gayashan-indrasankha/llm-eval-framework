# GRC-005 — Trial 2 Consistency Review

**Benchmark:** Potential split purchases under fictional procurement policy P01, Rule 5.  
**Trial 2 evaluation:** AI-assisted provisional, awaiting human reviewer approval.  
**Recorded model labels:** Claude Opus 5.5 Medium and university Microsoft Copilot Auto (previously reported; confirm settings for these runs).  
**Prompt integrity:** The original GRC-005 prompt from the Stage 1 starter has SHA-256 `7b6a92c0748b38db474f5a623129312aa1b4a5324b88d77b5a97931a3caf8f85`.  
**Execution timestamps:** Not supplied; remain blank in the data record.

## Scenario and reference checklist

Two purchase requests of LKR 70,000 and LKR 65,000, from the same requester for the same supplier and purchasing category, were submitted two calendar days apart. The total is **LKR 135,000**. P01 Rule 5 requires flagging such cases for *human investigation* when the combined value exceeds LKR 100,000 within three calendar days. This is a screening rule; it does not establish deliberate circumvention, fraud, or financial loss.

| GRC-005 original reference point | Claude Trial 2 | Copilot Trial 2 |
|---|---|---|
| Combined total LKR 135,000 exceeds LKR 100,000 | Pass | Pass |
| Two days falls within three-calendar-day window | Pass | Pass |
| Flag a potential split for human review | Pass | Pass |
| Do not state proven fraud or actual financial loss | Pass | Pass |

**Benchmark red flags:** Neither response asserts confirmed fraud or a confirmed LKR 135,000 loss.

## Trial 1 versus Trial 2: scoring (0–4 per criterion)

| Criterion | Claude T1 (approved) | Claude T2 (provisional) | Copilot T1 (approved) | Copilot T2 (provisional) |
|---|---:|---:|---:|---:|
| Accuracy | 4 | 4 | 4 | 4 |
| Coverage | 4 | 4 | 4 | 4 |
| Groundedness | 3 | **4** | 4 | 4 |
| Instruction following | 3 | 3 | 4 | 4 |
| Clarity | 3 | 3 | 4 | 4 |
| Risk awareness | 4 | 4 | 4 | 4 |
| **Total** | **21/24** | **22/24** | **24/24** | **24/24** |
| Clear fabricated requirements | 0 | 0 | 0 | 0 |

### Why these scores?

- **Claude Trial 2:** Correctly satisfies the screening test. Crucially, the phrase **“as one PR of LKR 135,000”** frames the higher-approval-tier comparison as a hypothetical single request, and **“may therefore have avoided”** acknowledges uncertainty about the actual two requests. This is more precisely grounded than Trial 1's potentially categorical aggregation language, justifying the provisional increase from 3 to 4 for groundedness. The long sections on quotations, unknown facts, approvals and retention are relevant but exceed the prompt's concise-answer request; clarity remains 3/4 for density rather than factual error.
- **Copilot Trial 2:** Correct amount, matching attributes, time window, investigation flag, source citation and caution about unproven misconduct or loss. Its answer remains concise and fully meets the benchmark.
- **No material contradiction:** Both products' substantive conclusions are unchanged across trials. Claude's grounding score changes by one; Copilot's rubric scores are stable.

### Boundary and uncertainty notes

- P01 Rule 5 does **not** say two separate PRs automatically acquire all approval duties applicable to a single PR of the combined amount. Claude's Trial 2 comparison is appropriately conditional and is not scored as a fabricated requirement.
- There is no evidence in the scenario that the requester intended to evade approval controls, that POs were issued, or that any financial loss occurred.
- The original prompt requests a **concise** answer. Repeat concision-related penalties may favor shorter products; report *substantive correctness separately from concision* in the final dashboard and consider sensitivity analysis without retroactively altering approved trial scores.
- Copilot Auto is a product mode, not a known fixed underlying model. Web-grounding and actual per-run settings are not independently verified. Two trials are not enough to establish a general consistency rate.
- The current assessment is AI-assisted and **must not be marked human-approved until the tester signs off**.

## Evidence files

- `responses/GRC-005_claude_trial1.txt`
- `responses/GRC-005_claude_trial2.txt`
- `responses/GRC-005_copilot_trial1.txt`
- `responses/GRC-005_copilot_trial2.txt`
- `data/evaluation_runs.csv`

## Reviewer sign-off

- [ ] Approve Claude Trial 2 **22/24** and Copilot Trial 2 **24/24** or provide revisions.
- [ ] Fill actual Trial 2 date/time in Asia/Colombo.
- [ ] Confirm the visible model/mode and browsing/memory settings.

**Next planned benchmark:** GRC-006 Trial 2, using the unchanged generated prompt.
