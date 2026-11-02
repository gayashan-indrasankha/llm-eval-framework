# GRC-001 — Trial 2 Consistency Review

**Status:** AI-assisted provisional scoring; human approval needed for Trial 2.  
**Scenario:** A requester submits a purchase request (PR) for LKR 85,000. Which approval is needed before a purchase order (PO) is issued?  
**Source:** Synthetic procurement policy P01, Rule 1 (and only as relevant, Rules 2, 3, 5, 7, 8).  
**Prompt SHA-256:** `12139ba132191eec3f56d1ecb738d2d771ac1d7603533bce5cee2a3c1b8824bc` (verified against the unchanged Stage 1 starter prompt).  
**Timing/settings:** Trial 2 execution times and current model selections were not supplied; leave fields blank/marked pending verification rather than inventing them.

## Reference-point assessment

| Required reference point | Claude Trial 2 | Copilot Trial 2 |
|---|---|---|
| LKR 85,000 is at/below LKR 100,000 threshold | Pass | Pass |
| Requester's line-manager approval before PO issuance | Pass | Pass |
| Avoid wrongly requiring both department-head and finance-manager approvals | Pass | Pass |
| Clear fabricated requirements observed | 0 | 0 |

The original benchmark defines **two** mandatory reference points: threshold interpretation and line-manager approval before PO issuance. The other checks above are useful additional safeguards, not extra mandatory scoring criteria.

## Within-product consistency (Trial 1 → Trial 2)

| Comparison | Claude | Copilot |
|---|---|---|
| Core approval conclusion | Unchanged | Unchanged |
| Approval timing | Before PO in both | Before PO in both |
| Primary policy citation | P01 Rule 1 in both | P01 Rule 1 in both |
| Reference-point coverage | Both 2/2 | Both 2/2 |
| Notable wording difference | Trial 2 adds uncertainty about unavailable line manager/documentation; both discuss ancillary policy checks | Trial 1 mentions P01 Rule 3 self-approval; Trial 2 omits it without missing a mandatory reference point |
| Newly observed clear fabrication | No | No |

**Interpretation:** Both products maintained the same substantive conclusion in these two observed runs. Different wording and optional context do not themselves constitute a failure. Two trials do not establish statistical reliability, especially when Copilot Auto's hidden model or retrieval settings may vary.

## Provisional Trial 2 human-rubric scores (0–4)

| Dimension | Claude | Copilot |
|---|---:|---:|
| Accuracy | 4 | 4 |
| Coverage | 4 | 4 |
| Groundedness | 4 | 4 |
| Instruction following | 3 | 4 |
| Clarity | 4 | 4 |
| Risk awareness | 4 | 4 |
| **Total** | **23/24** | **24/24** |
| Clear fabricated requirement count | 0 | 0 |

**Justification:** Both are correct, well-grounded, and readable. Claude provides source-supported but nonessential detail beyond the benchmark's concise-answer request, leading to a provisional one-point instruction-following deduction. Copilot is more concise; its omission of the optional self-approval detail does not justify a coverage deduction. This rubric can systematically reward brevity, so final reporting should show core correctness/reference-point coverage separately from instruction-following and total scores.

**Scoring status:** Trial 1 results were previously approved by the user. These two Trial 2 scores need explicit user approval. No factual comparison of runtime latency, hidden models, or disabled web grounding can be made from the supplied files.

## Files and recording

- `responses/GRC-001_claude_trial1.txt`
- `responses/GRC-001_copilot_trial1.txt`
- `responses/GRC-001_claude_trial2.txt`
- `responses/GRC-001_copilot_trial2.txt`
- `data/evaluation_runs.csv` (after merging/downloaded CSV and preserving existing rows)

Record Trial 2's actual `run_date_local`, visible model/mode, and any observed search/grounding before publishing claims about configuration parity. Other completed Trial 1 scores and earlier approvals are preserved in the combined CSV; GRC-011 approval was updated from pending to approved based on the user's subsequent confirmation.
