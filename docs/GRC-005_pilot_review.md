# GRC-005 — Controlled split-purchase pilot review

**Project:** AI Evaluation Framework: Claude vs Microsoft Copilot  
**Tester-reported run time:** November 1, 2026, 21:54 Asia/Colombo  
**Prompt:** `generated/prompts/GRC-005.txt`  
**Prompt SHA-256 (verified against Stage 1 starter):** `7b6a92c0748b38db474f5a623129312aa1b4a5324b88d77b5a97931a3caf8f85`  
**Status:** AI-assisted **provisional** scores; human reviewer sign-off pending.

## Product configuration and evidence scope

| Setting | Claude | Microsoft Copilot |
|---|---|---|
| Account / tier | Paid, user-reported | University/work, exact licensing not verified |
| UI model selection | Opus 5.5 Medium, user-reported | Auto (routing/selection mode, underlying model undisclosed) |
| Run | Trial 1 | Trial 1 |
| Raw response | `responses/GRC-005_claude_trial1.txt` | `responses/GRC-005_copilot_trial1.txt` |
| Prior-memory setting | Previously reported disabled; not independently verified for this trial | Previously reported disabled; not independently verified for this trial |
| Browsing/web grounding | Not independently verified for this trial | Not independently verified for this trial |

The evaluator reviewed the complete uploaded raw text against the bundled policy and reference points. The original UI inputs and search behavior were not independently observed. A matching benchmark file hash does not itself prove both products received the same paste unchanged.

## Ground-truth policy checks

1. **P01 Rule 5:** Same requester, supplier and purchasing category — **both responses pass**.
2. **P01 Rule 5:** Two PRs raised **two calendar days apart**, within the three-calendar-day window — **both pass**.
3. **P01 Rule 5:** LKR 70,000 + LKR 65,000 = **LKR 135,000**, greater than LKR 100,000 — **both pass**.
4. **P01 Rule 5:** Flag a **potential split purchase for human investigation** — **both pass**.
5. **P01 Rule 5 and prompt safety instruction:** This is a **screening flag, not proof of misconduct or fraud**; neither answer claims confirmed loss — **both pass**.

The benchmark has **four original reference points**. The summary above breaks out the fact pattern to explain the evaluation; it does not change the benchmark.

## Response analysis

**Claude:** Correctly identifies the numerical threshold and all matching conditions, recommends human investigation, explicitly declines to conclude fraud or loss, and adds checks of PRs, POs, approval roles, potential CFO exception, and record retention. These additional actions are generally supported by the separate P01 rules. **Caveat:** Its statement that the combined total 'would have required department head and finance manager approval' is appropriate as a hypothetical *single* PR under Rule 2, but P01 does **not** expressly require two already-separate PRs to undergo a combined approval workflow merely because Rule 5 is triggered. That imprecision should be distinguished from an actual observed approval breach. The answer is also longer than the prompt's requested concise format. No clear fabricated rule was observed, but one potentially misleading policy inference is recorded.

**Copilot:** Correctly lists the conditions, adds the amounts, explicitly identifies P01 Rule 5, and recommends investigation of whether the transactions were legitimately separate. The concise response stays within the source policy and does not allege misconduct or fraud. It does not explicitly say 'no confirmed financial loss,' but also makes no financial-loss claim; the key limitation is adequately conveyed.

## Provisional rubric (0–4 per dimension)

| Criterion | Claude | Copilot | Rationale |
|---|---:|---:|---|
| Accuracy | 4 | 4 | Correct arithmetic, eligibility conditions and risk conclusion. |
| Coverage | 4 | 4 | Both satisfy the original four reference points. |
| Groundedness | 3 | 4 | Claude's higher-approval inference needs an explicit hypothetical qualifier; Copilot stays with Rule 5. |
| Instruction following | 3 | 4 | Claude adds substantial ancillary audit detail; Copilot follows the requested concision. |
| Clarity | 3 | 4 | Claude is well structured but more extensive; Copilot is direct and easily actionable. |
| Risk awareness | 4 | 4 | Neither claims proven fraud, misconduct or confirmed financial loss. |
| **Illustrative equal-weight total** | **21/24** | **24/24** | Exploratory pilot scores; not a validated product ranking. |
| **Clearly fabricated policy requirements** | **0 observed** | **0 observed** | Claude has a separately recorded minor interpretive overreach, not a definite fabrication. |

**Scoring caveat:** The six dimensions have preliminary 0–4 anchors, not independently calibrated measurement properties. Totals here are illustrative; determine weights and adjudication rules **before** the full Stage 3 comparative analysis, and record human revisions. A 3-point difference on one synthetic prompt cannot establish model superiority.

## Required recordkeeping

- Keep the raw response text unchanged in local `responses/` files.
- Use `data/evaluation_runs.csv` for the accompanying four-row record (GRC-003 + GRC-005), replacing the previous two-row file only after review/backup.
- Confirm actual Copilot service tier, whether either chat used browsing/grounding, and whether settings remained unchanged.
- Have a human reviewer confirm or revise scores with reasons before final evaluation reporting.
- Next contrasting pilot: **GRC-012**, which tests non-invention and explicit uncertainty.
