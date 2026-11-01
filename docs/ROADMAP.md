# Six-stage project roadmap

1. **Benchmark definition (now):** synthetic policy corpus, twelve verified scenarios, reference-answer checklists, prompt controls, and data validation. No model runs claimed.
2. **Response collection:** compare available Claude and Microsoft Copilot interfaces with *identical prompts*, new chat per run, fixed document context, two trials per case if feasible; store raw output and metadata. A 3-case pilot precedes the full test.
3. **Evaluation engine:** implement transparent human rubric, scoring CSV validation, weighted averages, error taxonomy and disagreement resolution; unit test calculations. Never auto-award correctness based solely on a second LLM.
4. **Excel / Power BI scorecard:** build importable dataset and views by product, task type, accuracy, completeness, groundedness, and error types. No dashboard is claimed before implementation.
5. **Reliability and audit:** blind scoring sample, prompt reproducibility, repeatability assessment, limitations, privacy and data-handling review, evidence register, paired comparisons with small-sample caveats.
6. **Portfolio and interview:** professional README, screenshots, research methodology, limitations, demo, and only measured CV achievements.

**Deliverable:** a comparative evaluation of *observed app configurations on this small, synthetic benchmark*, not a general claim one model is globally better.
