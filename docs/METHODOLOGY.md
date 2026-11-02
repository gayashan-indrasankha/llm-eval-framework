# Evaluation methodology — completed synthetic GRC benchmark

## 1. Objective and scope

The project compares **recorded responses to fictional, policy-contained GRC questions**, not model quality across unrelated tasks or actual regulatory compliance. Its three synthetic source documents are P01 (procurement approvals), P02 (accounts payable), and P03 (third-party suppliers and access controls). There are 12 cases, two observed AI products and two manually collected trials: **48 responses**.

The observed products were user-reported Claude paid/Opus 5.5 Medium and university/work-account Microsoft Copilot Auto mode. These are **application configurations**, not proven underlying model identities. Microsoft Copilot Auto does not disclose the model used for every response in the provided evidence.

## 2. Prompt and response protocol

1. Case definitions are stored in `data/test_cases.json` and point to synthetic source policies.
2. `scripts/build_prompts.py` produces a common prompt with policy text, scope requirements, policy-source attribution, uncertainty requirements, and a case-specific question.
3. `generated/prompt_manifest.csv` records the SHA-256 of each archived prompt. Both apps were reportedly given identical prompts in fresh chats, first answer only, no follow-up or regeneration; settings were recorded to the extent available.
4. Each raw answer is stored in `responses/GRC-NNN_<product>_trial<T>.txt`; evaluation records point to these paths.
5. Archive hash equality confirms file consistency **in this repository**. It does **not** prove live input identity, browser configuration, hidden system prompts, or web-grounding state.

## 3. Six-dimension rubric (0–4 per criterion)

| Criterion | Assessed property |
|---|---|
| Accuracy | Correct conclusion relative to supplied policies |
| Coverage | Addresses key reference points and relevant controls |
| Groundedness | Correct policy attribution; no invented requirements |
| Instruction following | Honors scope, concision, source-only and uncertainty instructions |
| Clarity | Structured, readable, decision-useful response |
| Risk awareness | Avoids unsupported fraud, financial loss, or compliance assertions |

Scores are equally weighted and summed (maximum **24** per response). Detailed rationales are recorded in the CSV comments and case review notes. Responses were **AI-assisted scored and explicitly approved by the project owner**. This was not an independently blinded, multi-rater evaluation. The six dimensions and weights are working measurement choices rather than validated psychometric instruments. A score of 4/4 in accuracy does not mean a scientifically established 100% probability of correctness.

## 4. Results (descriptive)

| Measure | Claude | Microsoft Copilot |
|---|---:|---:|
| Responses | 24 | 24 |
| Total points / possible | 545/576 | 575/576 |
| Mean per response / 24 | 22.71 | 23.96 |
| Percent of awarded rubric points | 94.62% | 99.83% |
| Identical total scores across two trials | 11 of 12 cases | 11 of 12 cases |

Both products maintained the same **core policy conclusion** across the two trials for each case (24 of 24 product–case pairs). Claude GRC-005 and Copilot GRC-003 each improved by one rubric point on Trial 2. The **30-point overall gap** largely reflects instruction following (**24 points**) and clarity (**4 points**), rather than accuracy differences. A post-hoc exclusion of instruction following narrows the rubric-point gap; it is not a replacement for the approved rubric.

Zero records were tagged as definite fabricated policy obligations, but the synthetic benchmark and scorer sensitivity cannot establish absence of hallucinations in real tasks.

## 5. Auditability and unverified metadata

Local audit verifies all 48 expected records, unique run IDs, archived prompt-hash consistency (12/12), raw response presence (48/48), and human-approval labels (48/48). **44 execution timestamps are missing.** The exact underlying model, actual pasted prompt text and external search-grounding states were not independently observed. These are documented limitations, not gaps to be filled by inference.

## 6. Design limitations and research safeguards

- Small, synthetic, repetitive, source-contained prompts create a high-scoring *ceiling effect*.
- An AI-assisted scorer and human approval are not a substitute for independent blind raters and inter-rater reliability checks.
- The instruction to be concise can favor shorter responses; the rubric mixes policy quality with presentation behavior.
- Two trials cannot provide a dependable estimate of general model repeatability.
- There is no external legal fact-checking, statistical superiority test, real audit evidence, or production deployment.
- Web/connected app availability, subscription type, hidden prompts and underlying model versions may differ by run.
- Do not store personal, customer or proprietary information in synthetic benchmark repositories or submit it to consumer AI systems.

Detailed scoring and transparent cautions: [Stage 3 comparative report](Stage3_Comparative_Analysis.md). For reproducibility, see [Reproducibility](REPRODUCIBILITY.md). For background—not a certification—see the [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence).
