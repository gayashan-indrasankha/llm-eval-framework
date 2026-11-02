# GRC-011 — Trial 2 Consistency Review

**Review status:** AI-assisted provisional Trial 2 scores; user approval pending.  
**Benchmark:** P03 — Synthetic Third-Party Risk and Access Control Standard (fictional policy, not an actual company rule).  
**Original prompt SHA-256:** `b311efd020fc72d71c99456fbfb3ef7babf6c17a6f791c097c8ae541ab979de0`. The archived prompt's bytes were hashed and match `generated/prompt_manifest.csv` from the original starter archive. This does **not** verify that the live model inputs were identical.  
**Trial 2 response files:** `responses/GRC-011_claude_trial2.txt` and `responses/GRC-011_copilot_trial2.txt`.  
**Execution timestamps:** Not supplied; left blank in CSV.  
**Model settings:** Claude Opus 5.5 Medium and Copilot Auto were previously reported; actual Trial 2 configurations, web grounding and underlying Copilot model were not independently verified.

## Frozen benchmark question and reference

> HR sends the official departure notice for a finance employee. What access-control deadline applies?

From **P03 Access Governance Rule 5**, revoke the departing employee's access **within 24 hours of receiving the official HR departure notice**, and **retain evidence of the action**. Rule 4 separately requires quarterly user-access reviews for finance and procurement applications. Rule 6 requires retaining user-access *review logs* for 12 months; the supplied policy does not specify a period for Rule 5 revocation evidence. The source does not establish whether access was actually removed, the receipt timestamp, the date of termination, or any observed delay.

| Reference point | Claude Trial 2 | Copilot Trial 2 |
|---|---|---|
| States the 24-hour deadline | Pass | Pass |
| Anchors time to **receipt** of official HR notice | Pass | Pass |
| Requires revocation of access | Pass | Pass |
| Requires retained evidence of revocation | Pass | Pass |
| Attributes factual rule to P03 Rule 5 | Pass | Pass |
| Does not claim revocation was already performed | Pass | Pass |
| Clearly fabricated obligation / hallucination count | None observed (0) | None observed (0) |

## Differences between systems and trials

**Claude Trial 1:** Correct deadline and evidence requirement; distinguished receipt from last working day; discussed quarterly access reviews, retention ambiguity and other unstated details; recommended timestamp and evidence checks.

**Claude Trial 2:** Retains the same correct conclusion and core audit steps. Again discusses Rule 4 access reviews and correctly limits the Rule 6 12-month retention period to review logs. Its comment that the policy does not clarify whether hours are clock or business hours is flagged as an interpretive uncertainty rather than inventing a business-hour exception. The answer is longer than requested, which affects instruction following but not factual correctness.

**Copilot Trial 1:** Correct deadline and required evidence, concise next step with Rule 5 source.

**Copilot Trial 2:** Same substantive conclusion as Trial 1, identifying receipt of HR notice as the trigger, 24-hour revocation, and retained evidence. It remains concise and correctly scoped.

**No substantive contradiction across the four responses.** The numerical difference primarily reflects response concision and scope, not correct-versus-incorrect access-control interpretation.

## Six-dimension rubric (0–4 each)

| Criterion | Claude T1 (approved) | Claude T2 (provisional) | Copilot T1 (approved) | Copilot T2 (provisional) |
|---|---:|---:|---:|---:|
| Accuracy | 4 | 4 | 4 | 4 |
| Coverage | 4 | 4 | 4 | 4 |
| Groundedness | 4 | 4 | 4 | 4 |
| Instruction following | 3 | 3 | 4 | 4 |
| Clarity | 4 | 4 | 4 | 4 |
| Risk awareness | 4 | 4 | 4 | 4 |
| **Total** | **23/24** | **23/24** | **24/24** | **24/24** |

**Scoring rationale:** Claude loses one point on instruction following for lengthy secondary detail outside the benchmark request for a concise answer. Copilot covers all required reference points with a shorter answer. Neither is scored down on accuracy, grounding, or risk awareness. Hallucination count here counts clearly fabricated policy obligations, and is zero for both Trial 2 responses.

## Audit-trail handling

- Input CSV: `AI_Evaluation_Runs_GRC010_Trial2_44_Records.csv` (**44 records**), preserved without dropping or replacing existing runs.
- GRC-010 Trial 2: The two existing evaluator status fields were updated from provisional to **user approved**, reflecting the explicit approval in this conversation (2026-11-02). No duplicate rows were added.
- GRC-011 Trial 2: Two provisional scored rows added, using the archived original GRC-011 prompt SHA-256. Output CSV: `AI_Evaluation_Runs_GRC011_Trial2_46_Records.csv` (**46 records**).
- Run dates remain blank because actual execution times were not provided. Run-time model settings remain unverified.

## Limits and sign-off

These results show decision stability on **one synthetic case over two responses per model**, not measured general reliability or superiority in access governance. Both responses were AI-assisted scored. The second-trial scores require explicit human reviewer approval.

- [ ] Approve or revise Claude GRC-011 Trial 2 **23/24**.
- [ ] Approve or revise Copilot GRC-011 Trial 2 **24/24**.
- [ ] If known, provide live execution timestamps and confirm model settings.
