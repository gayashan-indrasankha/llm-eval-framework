# Evaluation methodology (planned; no scores yet)

## Fair comparisons
- Use the **same** generated prompt text and synthetic policy passages for Claude and Copilot.
- Record the *exact product variant*, sign-in/work or consumer mode, visible model name (if exposed), trial number, date/time and whether web/search grounding was active. Do not infer hidden model identifiers.
- Use a **fresh chat for each case and trial**. Do not add follow-up clarifications for only one product.
- Prefer to disable browsing, plugins, and external data, if the selected service permits; record if not possible. A user's web Copilot is not identical to paid Microsoft 365 Copilot.
- For a practical starting target: a pilot of GRC-003, GRC-005, GRC-012 with each app. If the pilot is usable, do two trials per case per app = 48 recorded outputs. Do not claim 48 runs before completing them.
- Protect source integrity: do not paste real company policies, passwords, personal data or university records into consumer AI chats. This project deliberately uses fictional documents.

## Human scoring rubric (planned, 0–4 per criterion)
- **Accuracy:** Are factual conclusions correct compared with the supplied policies?
- **Coverage:** Does the answer mention the required reference points without major omissions?
- **Groundedness:** Does it attribute conclusions to the right policy and avoid invented policy requirements?
- **Instruction following:** Does it follow the prescribed scope, concise format and uncertainty rules?
- **Clarity:** Is it readable, well structured and useful to an auditor?
- **Risk awareness:** Does it avoid falsely claiming fraud, losses, or compliance where evidence is insufficient?

Score each from **0** (materially unacceptable) to **4** (fully meets criterion) with recorded reasons and error labels. Do not treat the six scores as externally validated constructs. Define weights and adjudication rules *before* viewing aggregate scores in Stage 3. A human, not a model alone, must review evidence and ratings.

## Evidence and limitations
- Store raw responses in local `responses/`, create filenames by case, product, and trial. Exclude any real identifiers.
- Each prompt's SHA256 is recorded in `generated/prompt_manifest.csv`; use it to confirm prompt equivalence across products.
- Evaluation is limited by small synthetic cases, UI model changes, service configurations, evaluator subjectivity, non-determinism, and possible unobservable search or system prompts.
- Distinguish **reference-point checklists** from a claim that a single exact answer is required.
- The NIST Generative AI Profile is background guidance, not an audit certification: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
