"""Regressions for the human-approved, synthetic GRC experiment.

Tests verify archived evidence and recorded score consistency, not accuracy
against an independent human or a live model configuration.
"""
import csv
import hashlib
import json
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from stage3_analyze import analyze

AXES = (
    "accuracy_0to4", "coverage_0to4", "groundedness_0to4",
    "instruction_following_0to4", "clarity_0to4", "risk_awareness_0to4",
)


def records(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


class FinalEvaluationIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runs = records(ROOT / "data/evaluation_runs.csv")
        cls.manifest = {r["case_id"]: r for r in records(ROOT / "generated/prompt_manifest.csv")}
        cls.cases = {r["case_id"] for r in json.loads((ROOT / "data/test_cases.json").read_text(encoding="utf-8"))}

    def test_complete_48_run_matrix_and_unique_ids(self):
        self.assertEqual(len(self.cases), 12)
        self.assertEqual(len(self.runs), 48)
        self.assertEqual(len({r["run_id"] for r in self.runs}), 48)
        combinations = Counter((r["case_id"], r["product"], r["trial"]) for r in self.runs)
        expected = {(case, product, str(trial))
                    for case in self.cases for product in ("Claude", "Microsoft Copilot")
                    for trial in (1, 2)}
        self.assertEqual(set(combinations), expected)
        self.assertTrue(all(count == 1 for count in combinations.values()))

    def test_archived_prompts_and_raw_response_links(self):
        self.assertEqual(set(self.manifest), self.cases)
        for case, row in self.manifest.items():
            path = ROOT / row["prompt_file"]
            self.assertTrue(path.is_file(), case)
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), row["prompt_sha256"])
        for row in self.runs:
            case = row["case_id"]
            self.assertEqual(row["prompt_sha256"], self.manifest[case]["prompt_sha256"])
            product_part = "claude" if row["product"] == "Claude" else "copilot"
            expected_path = f"responses/{case}_{product_part}_trial{row['trial']}.txt"
            self.assertEqual(row["response_file"].replace("\\", "/"), expected_path)
            file = ROOT / expected_path
            self.assertTrue(file.is_file(), expected_path)
            self.assertTrue(file.read_text(encoding="utf-8").strip(), expected_path)

    def test_valid_six_axis_scores_and_human_approval(self):
        for row in self.runs:
            for dimension in AXES:
                self.assertIn(row[dimension], ("0", "1", "2", "3", "4"), (row["run_id"], dimension))
            self.assertIn("user approved", row["evaluator"].lower(), row["run_id"])
            self.assertGreaterEqual(int(row["hallucination_count"]), 0)

    def test_published_totals_match_approved_data(self):
        summary = analyze(
            ROOT / "data/evaluation_runs.csv", ROOT / "responses",
            ROOT / "generated/prompt_manifest.csv", ROOT / "generated/prompts",
        )
        self.assertEqual(summary["audit_warnings"], [])
        self.assertEqual(summary["missing_raw_files"], [])
        self.assertEqual(summary["user_approved_records"], 48)
        self.assertEqual(summary["manifest_case_hash_matches"], 12)
        self.assertEqual(summary["local_prompt_file_hash_matches"], 12)
        self.assertEqual(summary["model_metrics"]["Claude"]["rubric_points"], 545)
        self.assertEqual(summary["model_metrics"]["Microsoft Copilot"]["rubric_points"], 575)
        self.assertEqual(summary["score_stable_pairs"], 22)
        self.assertEqual(summary["missing_run_timestamps"], 44)


if __name__ == "__main__":
    unittest.main()
