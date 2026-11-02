# Repository architecture and evidence flow

This is a **manual benchmark plus local validation and analysis pipeline**. It does not call Claude or Copilot APIs, automate their web interfaces, or access a real procurement or finance system.

```text
  data/policies/P01...P03.md      data/test_cases.json
                  \                  /
                   \                /
                    scripts/build_prompts.py
                              |
                generated/prompts/GRC-NNN.txt
                generated/prompt_manifest.csv
                              |
                  MANUAL identical-prompt runs
                   /                        \
          Claude app                       Copilot app
             |                                 |
    responses/*_claude_trial*.txt    responses/*_copilot_trial*.txt
                   \                        /
                    \  AI-assisted scoring /
                     \ + user approval    /
                          |
                data/evaluation_runs.csv
                          |
                scripts/stage3_analyze.py
                   /                  \
             metrics JSON         integrity checks
                   |
           docs/Stage3_Comparative_Analysis.md
           docs/Stage3_Benchmark_Dashboard.xlsx
```

## Layers

- **Fixture layer:** Synthetic policy text and case-specific reference expectations. No real institutional policy is asserted.
- **Prompt layer:** Deterministic, text-based, source-contained prompts; SHA-256 verifies archived bytes. `scripts/build_prompts.py` intentionally rewrites generated files if invoked.
- **Capture layer:** 48 saved plaintext model outputs. Chat execution and collection were performed manually, not by repository code.
- **Evidence layer:** CSV metadata, six-axis scores, review notes, and explicit human approvals. The evaluation is AI-assisted and not blind independent rater adjudication.
- **Analytics layer:** Standard-library metrics script; static Stage 3 report and Excel snapshot. The script recomputes CSV metrics, not the subjective evaluation itself.

## Boundaries and limitations

The input source is synthetic, so the project shows evaluation design and audit-minded reasoning rather than production audit compliance. The archive cannot independently prove the exact prompts pasted live, hidden model IDs or web-grounding states. Current records lack 44 execution timestamps.

See [Methodology](METHODOLOGY.md) and [Reproducibility](REPRODUCIBILITY.md).
