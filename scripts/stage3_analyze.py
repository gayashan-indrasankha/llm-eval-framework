#!/usr/bin/env python3
"""Validate and summarize the approved synthetic GRC benchmark.

Standard-library only. Designed for the AI Evaluation Framework project layout.

Examples:
    python scripts/stage3_analyze.py
    python scripts/stage3_analyze.py --runs data/evaluation_runs.csv \
        --response-dir responses --manifest generated/prompt_manifest.csv \
        --prompts-dir generated/prompts --json docs/stage3_metrics.json
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

AXES = (
    "accuracy_0to4", "coverage_0to4", "groundedness_0to4",
    "instruction_following_0to4", "clarity_0to4", "risk_awareness_0to4",
)
PRODUCTS = ("Claude", "Microsoft Copilot")


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def analyze(runs: Path, response_dir: Path, manifest: Path | None, prompts_dir: Path | None) -> dict:
    records = csv_rows(runs)
    if not records:
        raise ValueError("No evaluation records found")
    seen = set()
    audit = []
    missing_files = []
    case_hashes = defaultdict(set)
    grouped = defaultdict(list)
    for r in records:
        required = ("run_id", "case_id", "product", "trial", "prompt_sha256", "response_file", "evaluator") + AXES
        if not all(k in r for k in required):
            raise ValueError(f"Missing required CSV fields: {set(required) - set(r)}")
        if r["run_id"] in seen:
            audit.append(f"Duplicate run_id {r['run_id']}")
        seen.add(r["run_id"])
        if r["product"] not in PRODUCTS or r["trial"] not in ("1", "2"):
            audit.append(f"Unexpected product/trial: {r['run_id']}")
        for a in AXES:
            if int(r[a]) not in range(5):
                audit.append(f"Invalid rubric score in {r['run_id']}: {a}")
        case_hashes[r["case_id"]].add(r["prompt_sha256"])
        grouped[r["product"]].append(r)
        raw = response_dir / Path(r["response_file"]).name
        if not raw.is_file():
            missing_files.append(str(raw))

    for case, hashes in case_hashes.items():
        if len(hashes) != 1:
            audit.append(f"Multiple prompt hashes for {case}")
    expected = {(case, product, trial) for case in case_hashes for product in PRODUCTS for trial in ("1", "2")}
    actual = {(r["case_id"], r["product"], r["trial"]) for r in records}
    missing_combinations = sorted(expected - actual)
    repeated_combinations = [str(k) for k, n in Counter((r["case_id"], r["product"], r["trial"]) for r in records).items() if n != 1]
    if missing_combinations or repeated_combinations:
        audit.append("Case × product × trial completeness check failed")

    manifest_matches = None
    live_archive_matches = None
    if manifest and manifest.exists():
        m = {r["case_id"]: r for r in csv_rows(manifest)}
        manifest_matches = sum(c in m and next(iter(hashes)) == m[c]["prompt_sha256"] for c, hashes in case_hashes.items() if len(hashes) == 1)
        if prompts_dir and prompts_dir.exists():
            live_archive_matches = sum(
                (prompts_dir / f"{c}.txt").is_file()
                and hashlib.sha256((prompts_dir / f"{c}.txt").read_bytes()).hexdigest() == m[c]["prompt_sha256"]
                for c in case_hashes if c in m
            )

    def score(r: dict) -> int:
        return sum(int(r[a]) for a in AXES)

    product_summary = {}
    for product, rr in grouped.items():
        points = sum(score(r) for r in rr)
        product_summary[product] = {
            "responses": len(rr), "rubric_points": points,
            "possible_points": 24 * len(rr),
            "mean_score_of_24": round(points / len(rr), 4),
            "rubric_percentage": round(100 * points / (24 * len(rr)), 4),
            "criterion_point_totals": {a: sum(int(r[a]) for r in rr) for a in AXES},
            "trial_totals": {t: sum(score(r) for r in rr if r["trial"] == t) for t in ("1", "2")},
        }
    pairs = defaultdict(dict)
    for r in records:
        pairs[(r["case_id"], r["product"])][r["trial"]] = score(r)
    changed = [
        {"case": c, "product": p, "trial_1": v["1"], "trial_2": v["2"]}
        for (c, p), v in sorted(pairs.items())
        if "1" in v and "2" in v and v["1"] != v["2"]
    ]
    return {
        "records": len(records), "unique_run_ids": len(seen),
        "cases": len(case_hashes), "missing_raw_files": missing_files,
        "missing_case_product_trial_combinations": missing_combinations,
        "repeated_combinations": repeated_combinations,
        "manifest_case_hash_matches": manifest_matches,
        "local_prompt_file_hash_matches": live_archive_matches,
        "user_approved_records": sum("user approved" in r["evaluator"].lower() for r in records),
        "missing_run_timestamps": sum(not r.get("run_date_local", "").strip() for r in records),
        "tagged_definite_fabrications": sum(int(r.get("hallucination_count", 0) or 0) for r in records),
        "score_stable_pairs": len(pairs) - len(changed),
        "score_changed_pairs": changed,
        "model_metrics": product_summary,
        "audit_warnings": audit,
        "interpretation_warning": "Synthetic benchmark rubric points are not estimates of real-world model accuracy.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs", type=Path, default=Path("data/evaluation_runs.csv"))
    parser.add_argument("--response-dir", type=Path, default=Path("responses"))
    parser.add_argument("--manifest", type=Path, default=Path("generated/prompt_manifest.csv"))
    parser.add_argument("--prompts-dir", type=Path, default=Path("generated/prompts"))
    parser.add_argument("--json", type=Path, default=None, help="Optional JSON output path")
    args = parser.parse_args()
    result = analyze(args.runs, args.response_dir, args.manifest, args.prompts_dir)
    payload = json.dumps(result, indent=2, ensure_ascii=False)
    print(payload)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(payload + "\n", encoding="utf-8")
    if result["audit_warnings"] or result["missing_raw_files"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
