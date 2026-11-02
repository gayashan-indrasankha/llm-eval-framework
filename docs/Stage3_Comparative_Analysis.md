# Stage 3 — Final Comparative Analysis
**AI Evaluation Framework: Claude vs Microsoft Copilot**
**Analysis date:** 2026-11-02 · **Dataset status:** 48/48 responses human-approved · **Scope:** synthetic GRC policy-question benchmark

> **Scope disclaimer:** The study compares the specific app experiences reported during these runs on 12 fictional policy questions. It does **not** rank the general capabilities of Anthropic versus Microsoft models or establish real-world audit reliability. An approved rubric score is a human-accepted, AI-assisted assessment, **not an independent professional audit**.

## Executive summary

- **Claude:** **545/576 points = 94.62%** of available rubric points; mean **22.71/24** across 24 responses.
- **Microsoft Copilot:** **575/576 points = 99.83%** of available rubric points; mean **23.96/24** across 24 responses.
- **Recorded gap:** 30 of 576 possible points (**5.21 percentage points**, or **1.25 points per response**); **24 of 30 points (80%)** result from instruction following, primarily response length/scope.
- The rubric assigns **4/4 in accuracy, coverage, and risk awareness to every one of the 48 responses**. This means no core control-decision error was recorded under this rubric; it is **not** a measured 100% real-world accuracy rate.
- **No definite invented policy obligations were tagged** (`hallucination_count = 0` for 48/48 responses); a few conditional/speculative statements received lower groundedness scores. No zeros recorded **does not prove hallucination-free models**.
- **Trial-level stability:** 22 of 24 product-by-case pairs have identical total scores across trials. Only Claude GRC-005 (21→22) and Copilot GRC-003 (23→24) changed, each by one point. The substantive policy conclusion remained the same across the two trials in all 24 paired model-case assessments.

## 1 · Scope and design

| Aspect | Definition |
|---|---|
| Synthetic source policies | P01 Procurement; P02 Accounts Payable; P03 Third-Party Supplier and Access |
| Cases | 12; 6 P01, 3 P02, 3 P03 |
| Products compared | User-reported Claude paid/Opus 5.5 Medium setting and university/work-account Copilot Auto mode |
| Trials | 2 independent fresh-chat runs per product/case (reported workflow) |
| Outputs | 12 × 2 × 2 = 48 saved plaintext responses |
| Rubric | Accuracy, coverage, groundedness, instruction following, clarity, risk awareness; each 0–4, equal-weight aggregate 0–24 |
| Review status | 48 AI-assisted ratings explicitly accepted by the human user, including GRC-012 Trial 2 |
| External data | Fictional policy fixture only; do not infer legal or organizational compliance beyond this dataset |

Equal weights are the **existing** aggregate scoring convention; they are not evidence of empirically validated weighting. The planned methodology recommended predefining weighting and adjudication rules; this analysis does **not** claim that independent blinded adjudication or formal preregistration occurred.

## 2 · Score summary

| Metric | Claude | Microsoft Copilot |
|---|---:|---:|
| Evaluated responses | 24 | 24 |
| Total awarded / maximum | 545 / 576 | 575 / 576 |
| Mean response score / 24 | 22.71 | 23.96 |
| Share of rubric points | 94.62% | 99.83% |
| Trial 1 total / 288 | 272 | 287 |
| Trial 2 total / 288 | 273 | 288 |
| Approximate average response words* | 237.2 | 120.1 |

*Word counts computed from saved text files using a consistent Unicode word-matching rule; not an AI API token count. Copilot outputs were approximately half the length in this dataset, a plausible contributor to instruction-following differences.

### 2.1 · Points by rubric dimension

| Dimension | Claude | Copilot | Copilot − Claude |
|---|---:|---:|---:|
| Accuracy | 96/96 | 96/96 | +0 |
| Coverage | 96/96 | 96/96 | +0 |
| Groundedness | 93/96 | 95/96 | +2 |
| Instruction following | 72/96 | 96/96 | +24 |
| Clarity | 92/96 | 96/96 | +4 |
| Risk awareness | 96/96 | 96/96 | +0 |
| **Total** | **545/576** | **575/576** | **+30** |

Point-gap decomposition:
- **Instruction following:** +24 / 30 = **80.0%** of total gap.
- **Clarity:** +4 / 30 = **13.3%**.
- **Groundedness:** +2 / 30 = **6.7%**.
- **Accuracy, coverage and risk awareness:** zero observed difference.

### 2.2 · Post-hoc sensitivity check (not the primary score)

Dropping the instruction-following dimension *only to test sensitivity* leaves five equal-weight dimensions (20 points per response):
- Claude: **473/480 = 98.54%**.
- Copilot: **479/480 = 99.79%**.
- Difference: **1.25 percentage points**.

This is a descriptive post-hoc analysis. It does **not** replace the approved six-dimension scores or justify removing instruction following from the original benchmark.

## 3 · Case-by-case results

| Case | Scenario | Claude T1 | Claude T2 | Copilot T1 | Copilot T2 |
|---|---|---:|---:|---:|---:|
| GRC-001 | LKR 85k approval | 23 | 23 | 24 | 24 |
| GRC-002 | LKR 100k threshold | 22 | 22 | 24 | 24 |
| GRC-003 | LKR 145k approvals | 22 | 22 | 23 | 24 |
| GRC-004 | Self-approval | 23 | 23 | 24 | 24 |
| GRC-005 | Split purchase: 2 days | 21 | 22 | 24 | 24 |
| GRC-006 | Split purchase: 5 days | 23 | 23 | 24 | 24 |
| GRC-007 | Duplicate invoice | 23 | 23 | 24 | 24 |
| GRC-008 | Three-way match | 23 | 23 | 24 | 24 |
| GRC-009 | Supplier bank change | 23 | 23 | 24 | 24 |
| GRC-010 | High-risk supplier review | 23 | 23 | 24 | 24 |
| GRC-011 | Access revocation | 23 | 23 | 24 | 24 |
| GRC-012 | ISO 27001 unsupported claim | 23 | 23 | 24 | 24 |

Most score differences reflect response scope, presentation and groundedness comments, not different core control decisions.

**Notable cases:**
- **GRC-002 (threshold boundary):** Both classify exactly LKR 100,000 correctly. Claude lost groundedness/instruction-following points for unsupported peripheral phrasing and unnecessary split-purchase discussion.
- **GRC-003 (above-threshold approvals):** Both identify department-head and finance-manager approval; Copilot groundedness improves by one point in Trial 2.
- **GRC-005 (potential split purchase):** Both flag the LKR 135,000, two-day pattern for human review, not fraud. Claude's Trial 2 wording is more precise about combined approvals, improving groundedness by one point.
- **GRC-006 (time-window negative case):** Both correctly avoid an automatic split-purchase flag at five days.
- **GRC-008 (three-way match):** Both require holding payment where receipt/acceptance evidence is missing.
- **GRC-009 (supplier bank change):** Both require independent callback via previously verified contact details and retained evidence.
- **GRC-011 (offboarding):** Both give 24 hours from *receipt* of the official HR departure notice.
- **GRC-012 (unsupported ISO 27001):** Both refuse to infer a universal certification mandate from P03 alone.

## 4 · Two-trial consistency

**Score stability:** 22/24 model–case pairs have identical total scores across both trials (**91.7%**). Claude: 11/12 unchanged; Copilot: 11/12 unchanged.

**Core decision stability:** No case/product pair had a recorded change of core policy conclusion between Trial 1 and Trial 2 (**24/24 assessed stable**). With only two repetitions of each identical synthetic prompt, this is a small descriptive repeatability check, **not** a defensible statistical reliability estimate.

**Score changes:**
1. Claude on GRC-005: **21 → 22**, groundedness improved; overall control flag remained correct.
2. Copilot on GRC-003: **23 → 24**, groundedness improved; approval gap remained correctly identified.

## 5 · Audit integrity and data-quality checks

| Audit check | Result |
|---|---|
| Rows in final CSV | **48** |
| Unique `run_id` values | **48** |
| Complete 12-case × 2-product × 2-trial coverage | **Pass** |
| Corresponding raw response text files present | **48/48** |
| Original archived prompt SHA-256 matches archived manifest | **12/12** |
| Recorded prompt hashes match case manifest | **48/48** |
| Ratings approved by the user | **48/48** |
| Missing actual execution timestamps | **44/48** |
| Verified exact runtime model identifiers | **Not established** |
| Verified identical text pasted into each live UI | **Not established** |
| Verified search/web grounding mode for all runs | **Not established** |
| Confirmed-fabrication tags | **0/48** under the recorded evaluator labels |

**Important distinction:** Archive and manifest SHA-256 equality establishes fixture integrity in the available project materials. It **does not** independently verify what was pasted into Claude or Copilot on each occasion.

### Limitations that must accompany any project presentation

1. The questions are **short, synthetic and policy-contained**; they do not represent the volume, ambiguity, security or legal complexity of real GRC operations.
2. **Scoring was AI-assisted** and user-approved, not conducted with blinded, independent raters. Researcher/evaluator bias and score ceilings may affect findings.
3. The score distribution is near the maximum, particularly in accuracy, coverage and risk awareness, limiting discrimination between systems.
4. Copilot **Auto** is a UI selection mode; its underlying model, available grounding and license context were not verified. Claude's reported setting was not independently confirmed for every response.
5. **44 timestamps are absent**; some specific original pilot timestamps exist, but missing execution metadata prevents complete temporal and configuration auditing.
6. Two trials per prompt do not support confidence intervals or statistical generalization. Responses on repeated cases are not an independent random sample of GRC work.
7. **Concision is a meaningful rubric requirement but not the same thing as correctness.** Avoid interpreting Copilot's overall rubric advantage as evidence of broadly superior reasoning.

## 6 · Recruiter-ready findings (defensible wording)

> Designed and completed a human-reviewed comparison of Claude and Microsoft Copilot on 12 synthetic GRC policy scenarios (48 responses). Used a six-dimension, 0–4 evaluation rubric, recorded prompt hashes, preserved original outputs, and assessed two-trial decision consistency. Both systems met the benchmark's core policy-reference checks in all recorded runs; Copilot achieved 575/576 total rubric points versus Claude's 545/576, with most of the difference driven by concision/instruction following. Results are limited to the tested scenarios and reported app configurations.

**Interview takeaway:** The value of this project is the *measurement framework*: policy-grounded test cases, a repeatable execution workflow, evidence traceability, human review, and careful reporting of limitations—not a headline claiming a universally better model.

## 7 · Recommended follow-on work

**Close Stage 3 now:** keep the finalized approved CSV and export this analysis with the dashboard to `docs/` and `data/` in your repository.

**Optional Stage 4 improvement backlog:**
1. Backfill only the dates/settings you can verify from contemporaneous logs; never estimate missing values.
2. Use an independent reviewer blind to the model identity on a larger case set and track disagreements/adjudication.
3. Add harder adversarial questions, deliberately conflicting policy passages, missing-evidence prompts and multi-document cases.
4. Declare weights, severity/error taxonomy, acceptable answer criteria and adjudication rules before running the next benchmark.
5. Report rubric scores, reference-point pass rates, unsupported obligations, latency/cost and response length as *separate* metrics when all are actually measured.

## Files and reproducibility

- `AI_Evaluation_Runs_Final_Approved_48.csv` — approved raw score records, original fields and comments preserved; final two approval markers updated.
- `Stage3_Benchmark_Dashboard.xlsx` — interactive workbook with linked formula-based summaries and underlying run-level data.
- `Stage3_Metrics.json` — compact machine-readable aggregates and validation results.
- `stage3_analyze.py` — repeatable standard-library score/data audit that can run locally with repository response files.

**Source basis:** `AI_Evaluation_Runs_GRC012_Trial2_48_Records.csv`, 48 provided raw response text files, and the original `AI_Evaluation_Framework_Stage_1_Starter.zip` synthetic fixture and methodological notes.
