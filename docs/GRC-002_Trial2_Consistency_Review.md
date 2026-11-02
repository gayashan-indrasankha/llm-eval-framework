# GRC-002 — Trial 2 Consistency Review

**Benchmark:** GRC-002, synthetic Procurement and Approval Policy P01.  
**Question:** A requester submits a PR for exactly LKR 100,000. Is this above the approval threshold, and who must approve?  
**Prompt SHA-256 (starter fixture):** `f0f56bdd713f07c2a4cda6a646003c0f820f97af3c286e8d683c5e1f674403fd`  
**Evaluation status:** Trial 2 scoring is AI-assisted and provisional; human reviewer sign-off pending.  
**Execution time:** Not supplied. The reported Claude/Copilot model selections have not been independently reconfirmed for Trial 2.

## Frozen reference points and red flag

The starter's GRC-002 benchmark requires **(1)** recognizing that exactly LKR 100,000 is *not above* the threshold and **(2)** line-manager approval **before PO issuance** (P01 Rule 1). Red flag: claiming that exactly LKR 100,000 requires both department-head and finance-manager approvals. Both Trial 2 answers satisfy both reference points and avoid the red flag.

## Trial 1 versus Trial 2

| Assessment | Claude Opus 5.5 Medium (user-reported configuration) | Microsoft Copilot Auto (underlying model not disclosed) |
|---|---|---|
| Required approval conclusion | Stable: requester’s line manager, before PO | Stable: requester’s line manager, before PO |
| Threshold interpretation | Stable: exactly LKR 100,000 remains in lower tier | Stable: exactly LKR 100,000 remains in lower tier |
| Correct policy grounding | P01 Rules 1–2 | P01 Rule 1 |
| Supplementary checks | Both trials add self-approval and conditional split-purchase screening | Both trials add the self-approval prohibition |
| Wording difference | Trial 1 calls exact-threshold PRs a “common pattern” in split purchases; Trial 2 presents screening as a suggested watch point. Neither claim is an explicit additional trigger mandated by P01. | The wording and organization change, not the conclusion. |
| Trial 1 score (user approved) | **22/24** | **24/24** |
| Trial 2 score (provisional) | **22/24** | **24/24** |
| Score change | **0** | **0** |

## Trial 2 provisional rubric

| Dimension (0–4) | Claude | Copilot |
|---|---:|---:|
| Accuracy | 4 | 4 |
| Coverage | 4 | 4 |
| Groundedness | 3 | 4 |
| Instruction following | 3 | 4 |
| Clarity | 4 | 4 |
| Risk awareness | 4 | 4 |
| **Total** | **22/24** | **24/24** |
| Clear fabricated policy requirements | 0 | 0 |

### Scoring rationale

- **Claude:** The threshold, required approver, and timing are correct. Its optional screening of nearby purchases is conditional and defensible as an *audit suggestion*, but P01 does not prescribe screening solely because a PR equals the LKR 100,000 ceiling. We therefore retain the same **3/4 groundedness** caution as Trial 1. Additional discussion beyond the concise scope earns **3/4 instruction following**. This is not scored as a clearly fabricated control.
- **Copilot:** Correctly explains the boundary, required line manager, and pre-PO requirement; its self-approval note is supported by P01 Rule 3. The concise answer meets all required reference points with no clearly unsupported mandatory policy claim.

## Limitations and next actions

- Two independently collected answers per product demonstrate **stable core conclusions on this synthetic case**, not guaranteed model reliability or a statistically meaningful superiority finding.
- The responses themselves do not prove which underlying model Microsoft Copilot Auto selected, whether external grounding occurred, or that live product settings matched the prior trial.
- The CSV intentionally leaves Trial 2 timestamps blank until the actual run times are supplied.
- Keep separate **substantive correctness** and **concision/instruction-following** metrics when presenting aggregate model scores. Otherwise verbosity penalties may be mistaken for differences in GRC accuracy.
- Reviewer should approve or revise provisional Trial 2 scores before marking them finalized.

**Files:** `responses/GRC-002_claude_trial2.txt`, `responses/GRC-002_copilot_trial2.txt`; update `data/evaluation_runs.csv` with the two records supplied in the combined 28-record CSV.
